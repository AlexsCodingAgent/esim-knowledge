---
title: "OTA Communication: SMS, PSK-TLS, CAT_TP, and DNS"
3|description: "Examines the SGP.02 over-the-air communication stack : how the SM-SR uses SMS, PSK-TLS, and CAT_TP transports wrapped in SCP80/SCP81 secure channels to deliver commands to the ISD-R on the eUICC."
date: 2026-06-07
---

# OTA Communication: SMS, PSK-TLS, CAT_TP, and DNS

**[eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > OTA Communication: SMS, PSK-TLS, CAT_TP, and DNS**

The SM-SR has one job nobody else gets to do: talk directly to the eUICC over the air. SGP.02 §2.4 puts it bluntly: "the OTA communication is exclusively handled by the SM-SR." If you're coming from [the Architecture article]({{ site.baseurl }}/docs/articles/sgp02/01-sgp02-architecture), you already know the ES5 interface is where the push model gets physical. And if you've read [the eUICC Internals piece]({{ site.baseurl }}/docs/articles/sgp02/02-sgp02-euicc-internals), you know the ISD-R is the on-chip endpoint that receives these commands.

Here's what the SM-SR actually has at its disposal: three transport protocols: SMS for short commands, HTTPS with PSK-TLS for bulk data, and CAT_TP for constrained networks. All of it gets wrapped in SCP80 or SCP81 secure channels regardless of what's underneath. The eUICC must speak SMS plus at least one of HTTPS or CAT_TP; the SM-SR must speak all three. And through it all, no other off-card entity (not the Operator, not the SM-DP, not the M2M SP) can send a single byte to the chip without going through the SM-SR.

---

## SMS: The Universal Fallback

SMS does three things in SGP.02 (SGP.02 §2.4.3):

### 1. Direct Command Delivery

When a platform management command fits in a handful of SMS messages, sending it directly is faster than opening a full HTTPS session. Profile enabling, disabling, policy updates; these often squeeze into a single secure SMS.

Commands use the Expanded Remote Command structure from ETSI TS 102 226, with SCP80 riding on top:

- **Cryptographic Checksum (CC):** 64-bit AES-CMAC for integrity and origin authentication
- **Encryption:** AES in CBC mode
- **Proof of Receipt (PoR):** Typically requested with `SPI2 = '39'`, triggering a response SMS with its own CC and encryption
- **Counter management:** The SM-SR verifies that the PoR counter value matches the command packet's counter

If the eUICC can't authenticate the SM-SR (if SCP80 verification fails), it drops the command silently and sends no PoR. No information about the chip's configuration leaks to a potential attacker.

### 2. HTTPS Session Triggering

For bulk operations like profile download, SMS plays a lighter role: it kicks open the door for HTTPS. The SM-SR sends a special SMS addressed to the ISD-R carrying Administration Session Triggering Parameters from GlobalPlatform Amendment B. The ISD-R's TAR (Toolkit Application Reference) is listed in the EIS.

The SM-SR can request a PoR for this triggering SMS, but it's optional. A PoR confirms the eUICC got the trigger, at the cost of some added latency. For time-sensitive operations, skipping it is fine; the subsequent HTTPS session opening implicitly confirms delivery.

### 3. CAT_TP Session Triggering

When the transport is CAT_TP, the triggering SMS gets a bit more involved. Per ETSI TS 102 226, it packs two commands into one push SMS:

- **"Request for BIP channel opening"**: opens the Bearer Independent Protocol channel
- **"Request for CAT_TP link establish"**: layers CAT_TP on top

The corresponding "Data for BIP channel opening" and "Data for CAT_TP link establishment" parameters configure the session specifics.

---

## HTTPS with PSK-TLS: The Bulk Data Workhorse

For anything involving serious data transfer (and profile download is the prime example), HTTPS is the default choice. But SGP.02 doesn't use certificate-based TLS. It uses PSK-TLS (Pre-Shared Key TLS), and the reason is straightforward: certificate TLS would demand an X.509 certificate and private key on the eUICC that a public CA recognizes. That's a big ask for a constrained smart card. PSK-TLS sidesteps the problem by using symmetric keys already shared between the SM-SR and ISD-R through the SCP81 key set (SGP.02 §2.4.4).

The Pre-Shared Keys need at least 128 bits of entropy. The eUICC supports TLS 1.2 with at least one of:

- `TLS_PSK_WITH_AES_128_GCM_SHA256` (preferred: GCM authenticated encryption)
- `TLS_PSK_WITH_AES_128_CBC_SHA256`

No session resumption (RFC 4507/5077), no parallel TLS sessions. One HTTPS session per OTA interaction, period.

### PSK Identity Format

During the TLS handshake, the eUICC presents a PSK Identity that tells the SM-SR which key to reach for. It's a TLV structure (SGP.02 §2.4.4.1, Table 4):

| Tag | Content | Length | Example |
|-----|---------|--------|---------|
| `80` | Format identifier | 1 byte | `02` (full qualified, random PSK) |
| `81` | EID | 16 bytes | Hex-encoded 32-digit EID |
| `4F` | ISD-R AID | 16 bytes | The ISD-R's application identifier |
| `82` | Key identifier | 1 byte | Which key within the key set |
| `83` | Key version | 1 byte | `40`–`4F` (reserved for SCP81) |

This TLV binary gets converted to a hex string, then encoded as UTF-8 for the TLS `psk_identity` field. The SM-SR pulls the EID and key identifier, looks up the matching PSK, and the handshake proceeds.

### HTTP POST Request/Response Pattern

The HTTPS session follows GlobalPlatform RAM over HTTP (Amendment B). It's a half-duplex, POST-driven conversation:

**Session opening** (SMS-triggered):
1. SM-SR sends MT-SMS with HTTPS triggering command (SCP80 protected)
2. ISD-R verifies SCP80 security
3. ISD-R performs PSK-TLS handshake with SM-SR
4. ISD-R sends initial `POST <initial-uri>` with headers:
 - `X-Admin-Protocol: globalplatform-remote-admin/1.0`
 - `X-Admin-From: //se-id/eid/<EID>;//aa-id/aid/<ISD-R AID>`

**Command delivery** (SM-SR → eUICC):
- SM-SR responds `HTTP/1.1 200` with `Content-Type: application/vnd.globalplatform.card-content-mgt;version=1.0`
- `X-Admin-Next-URI` tells the eUICC where to POST next
- If targeting an ISD-P: `X-Admin-Targeted-Application: //aid/<rid>/<pix>` identifies it by AID
- Body carries the command script in Expanded Remote Command format

**Response delivery** (eUICC → SM-SR):
- eUICC sends `POST <next-uri>` with `Content-Type: application/vnd.globalplatform.card-content-mgt-response;version=1.0`
- `X-Admin-Script-Status: ok` (or an error status)
- Body carries the response script

**Session management:**
- `HTTP/1.1 204` (No Content) with `X-Admin-Next-URI` keeps the session alive
- `HTTP/1.1 204` without `X-Admin-Next-URI` closes it

Both sides use Chunked Transfer Encoding: the eUICC for POST requests, the SM-SR for POST responses. This lets large profile packages stream through without buffering the whole thing in memory.

---

## CAT_TP: Constrained Network Transport

CAT_TP (Card Application Toolkit Transport Protocol) exists for the scenarios where TCP/TLS overhead becomes a problem: very low bandwidth, high latency, intermittent connections (SGP.02 §2.4.3.2).

It runs over the BIP (Bearer Independent Protocol) channel from ETSI TS 102 223: reliable, connection-oriented data transfer with flow control, designed for a UICC talking through a modem. Commands over CAT_TP use the same SCP80 security as SMS: expanded remote command structure with AES-CMAC checksums and AES-CBC encryption. The security lives at the application layer, not the transport.

Where CAT_TP shines:

- 2G/3G networks where TCP performance is rough
- Devices with limited IP stacks
- Deployments where the SM-SR wants a lightweight, persistent connection without TLS overhead

---

## DNS Resolution: Finding the SM-SR

DNS resolution is optional but useful (SGP.02 §2.4.5). It lets the eUICC resolve the SM-SR's FQDN to an IP address dynamically instead of relying on a hardcoded IP that might change.

The eUICC performs DNS resolution when all of these hold:

1. The eUICC has been asked to open an HTTPS session
2. The eUICC supports DNS resolution at all
3. The ISD-R has no hardcoded IP in its Connection Parameters or the triggering SMS
4. The ISD-R has an FQDN and DNS server IP addresses configured
5. The ISD-R hasn't already resolved that FQDN, or considers the cached value stale

The resolver on both SM-SR and eUICC must comply with RFC 1035 and RFC 3596, support query types A (IPv4) and AAAA (IPv6), and use UDP transport.

The flow is simple: the eUICC's DNS Resolver Client fires off a query to the configured DNS Resolver Server (often the SM-SR itself, or a network-provided DNS server), gets back the resolved IPs. This happens after the SMS trigger, before the TLS handshake. What the eUICC does with multiple resolved addresses (retry logic, load balancing, fallback) is implementation-specific and outside SGP.02's scope.

---

## The ES8 Tunnel: A Secure Channel Inside a Secure Channel

ES8 connects the SM-DP to the ISD-P, but it has no physical layer. It's a tunnel riding on other people's wires (SGP.02 §2.5):

```
SM-DP ──ES3──▶ SM-SR ──ES5──▶ ISD-R ──▶ ISD-P
 └── SCP03/SCP03t ────────────┘
 └──── ES8 logical channel ────┘
```

The SM-DP encrypts commands for the ISD-P using SCP03 or SCP03t. That encrypted payload travels over ES3 (SM-DP to SM-SR) using whatever secure transport those two servers have negotiated. The SM-SR then wraps the SCP03 payload inside the SCP80/SCP81-protected ES5 channel to the ISD-R. The ISD-R forwards it to the target ISD-P, which decrypts and processes it.

And here's the part that matters: the SM-SR can't read what's inside. It sees only the SCP03 ciphertext. Despite being the OTA gateway (despite touching every byte that flows to and from the chip), the SM-SR has zero access to profile contents.

---

## ES6 and ES1: The Other Communication Paths

Two more interfaces round out the picture:

**ES6 (Operator → MNO-SD).** The Operator's OTA platform talks directly to the MNO-SD inside a Profile, using the same SCP80/SCP81 model as ES5, following ETSI TS 102 225/226. The initial OTA keys get loaded during profile download or at manufacturing. Post-install, this is how the operator manages its profile (updating network parameters, installing applets, refreshing file contents) without involving the SM-DP or SM-SR at all.

**ES1 (EUM → SM-SR).** At manufacturing time, the EUM sends the EIS to the first SM-SR. The ISD-R key sets in the EIS are protected by a mechanism the EUM and SM-SR agree on, which must include at minimum: AES-128 transport key, ECB cipher mode, and PKCS#7 padding when needed.

---

## Summary

- The SM-SR owns the OTA channel; no other entity can reach the eUICC over the air without going through it
- SMS handles short platform management commands and triggers HTTPS or CAT_TP sessions for anything bulkier
- HTTPS uses PSK-TLS (not certificate TLS), with keys derived from the SCP81 key set shared between SM-SR and ISD-R
- The HTTP POST pattern follows GlobalPlatform RAM over HTTP: half-duplex, chunked, with X-Admin headers managing session state
- CAT_TP gives you a lightweight alternative for constrained networks, with the same SCP80 application-layer security SMS uses
- DNS resolution decouples the eUICC from hardcoded IPs; the chip can find the SM-SR dynamically
- ES8 tunnels SCP03/SCP03t through ES3→ES5; the SM-SR carries the bytes but never sees profile plaintext

---

<div align="center">

<a href="{{ site.baseurl }}/"> Home</a>

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp02/03-sgp02-pki">M2M Certificate Hierarchy</a> | Next: <a href="{{ site.baseurl }}/docs/articles/sgp02/05-sgp02-download">Profile Download</a> →

</div>

---

*Based on GSMA SGP.02 v4.2 §2.4–2.8: OTA Communication and Secure Channels*


---

← Previous: [M2M Certificate Hierarchy: CI, EUM, SM-DP, SM-SR, and eUICC](03-sgp02-pki) | [Section Index](index) | Next: [Profile Download: ISD-P Creation, SCP03, and Encrypted Delivery](05-sgp02-download) →
