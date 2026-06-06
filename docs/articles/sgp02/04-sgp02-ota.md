---
date: 2026-06-07
---

# OTA Communication: SMS, PSK-TLS, CAT_TP, and DNS

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > OTA Communication: SMS, PSK-TLS, CAT_TP, and DNS**

> **📚 Prerequisites:** Read the [Architecture]({{ site.baseurl }}/docs/articles/sgp02/01-sgp02-architecture) article to understand the ES5 interface and the SM-SR's role. The [eUICC Internals]({{ site.baseurl }}/docs/articles/sgp02/02-sgp02-euicc-internals) article explains the ISD-R and secure channels.

> **💡 Why this matters:** The ES5 OTA channel is the physical manifestation of the push model. Understanding how the SM-SR reaches the eUICC — across SMS, HTTPS, and CAT_TP — is essential for anyone deploying or troubleshooting M2M devices in the field.

> **Key takeaways:**
> - The SM-SR exclusively owns the OTA channel — no other entity can initiate communication with the eUICC
> - Three transport protocols are available: SMS (for short commands), HTTPS with PSK-TLS (for bulk data), and CAT_TP (for constrained network scenarios)
> - All ES5 traffic is protected by SCP80 or SCP81 secure channels regardless of transport
> - PSK-TLS keys are derived from the SCP81 key set shared between SM-SR and ISD-R
> - DNS resolution is optional but critical for deployments where the SM-SR's IP address changes

---

## The ES5 Interface: Exclusive OTA Ownership

SGP.02 §2.4 states it plainly: "In the eUICC Remote Provisioning and Management system the OTA communication is exclusively handled by the SM-SR." This is the push model made concrete. No other off-card entity — not the Operator, not the SM-DP, not the M2M SP — can send a single byte to the eUICC without going through the SM-SR.

The SM-SR selects the transport protocol based on:
- The eUICC's and Device's capabilities (declared in the EIS)
- The type of operation being performed
- Network conditions and efficiency considerations
- The SM-SR's own preferences

The eUICC **SHALL** support SMS and either CAT_TP or HTTPS (or both). The SM-SR **SHALL** support all three. For LTE network deployments, SMS support must comply with GSMA PRD IR.92.

All ES5 traffic is secured by either **SCP80** or **SCP81** — GlobalPlatform secure channel protocols that provide origin authentication, integrity protection, and confidentiality. The security level is independent of the transport layer beneath.

---

## SMS — The Universal Fallback

SMS is the most fundamental ES5 transport. Its use cases fall into three categories (SGP.02 §2.4.3):

### 1. Direct Command Delivery

When a platform management command fits into a few SMS messages, it's more efficient to send it directly via SMS than to open a full HTTPS session. Commands like profile enabling, disabling, or policy updates can often be delivered in a single secure SMS.

SMS commands use the **Expanded Remote Command** structure defined in ETSI TS 102 226, with SCP80 security:
- **Cryptographic Checksum (CC)**: 64-bit AES-CMAC for integrity and origin authentication
- **Encryption**: AES in CBC mode
- **Proof of Receipt (PoR)**: Typically requested (`SPI2 = '39'`), which triggers a response SMS with its own CC and encryption
- **Counter management**: The SM-SR verifies that the PoR counter value matches the command packet's counter

If the eUICC cannot authenticate the SM-SR (SCP80 verification fails), it discards the command silently and sends no PoR — preventing information leakage about the chip's configuration.

### 2. HTTPS Session Triggering

For bulk operations — like profile download — SMS triggers an HTTPS session. The SM-SR sends a special SMS addressed to the ISD-R containing the Administration Session Triggering Parameters defined in GlobalPlatform Amendment B. The TAR (Toolkit Application Reference) for the ISD-R is included in the EIS.

The SM-SR can choose whether to request a PoR for the triggering SMS. A PoR confirms the eUICC received the trigger, but adds latency. For time-sensitive operations, skipping the PoR is acceptable since the subsequent HTTPS session opening confirms delivery implicitly.

### 3. CAT_TP Session Triggering

For CAT_TP transport, the triggering SMS is more complex. Per ETSI TS 102 226, it includes two commands in the same push SMS:
- **"Request for BIP channel opening"** — opens the Bearer Independent Protocol channel
- **"Request for CAT_TP link establish"** — establishes the CAT_TP layer on top

The corresponding "Data for BIP channel opening" and "Data for CAT_TP link establishment" parameters configure the session.

---

## HTTPS with PSK-TLS — The Bulk Data Workhorse

HTTPS is the preferred transport for operations involving significant data transfer — most importantly, profile download and installation. The HTTPS stack in SGP.02 uses **PSK-TLS** (Pre-Shared Key TLS) rather than certificate-based TLS (SGP.02 §2.4.4).

### Why PSK-TLS?

Certificate-based TLS would require the eUICC to possess an X.509 certificate and private key recognized by a public CA — a heavy requirement for a constrained smart card. PSK-TLS instead uses symmetric keys already shared between the SM-SR and ISD-R through the SCP81 key set.

The **Pre-Shared Keys** must have at least **128 bits of entropy**. The eUICC supports TLS 1.2 with at least one of these cipher suites:
- `TLS_PSK_WITH_AES_128_GCM_SHA256` (preferred — GCM authenticated encryption)
- `TLS_PSK_WITH_AES_128_CBC_SHA256`

TLS session resumption (RFC 4507/5077) and parallel TLS sessions are **not supported** — there's exactly one HTTPS session per OTA interaction.

### PSK Identity Format

During the TLS handshake, the eUICC presents a PSK Identity that tells the SM-SR which key to use. The PSK-ID is a TLV structure (SGP.02 §2.4.4.1, Table 4):

| Tag | Content | Length | Example |
|-----|---------|--------|---------|
| `80` | Format identifier | 1 byte | `02` (full qualified, random PSK) |
| `81` | EID | 16 bytes | Hex-encoded 32-digit EID |
| `4F` | ISD-R AID | 16 bytes | The ISD-R's application identifier |
| `82` | Key identifier | 1 byte | Which key within the key set |
| `83` | Key version | 1 byte | `40`–`4F` (reserved for SCP81) |

This TLV binary is converted to a hex string, then encoded as UTF-8 for the TLS `psk_identity` field. The SM-SR uses the EID and key identifier to look up the correct PSK.

### HTTP POST Request/Response Pattern

The HTTPS session follows the **GlobalPlatform RAM over HTTP** protocol (Amendment B). It's a half-duplex, POST-driven conversation:

**Session opening** (SMS-triggered):
1. SM-SR sends MT-SMS with HTTPS triggering command (SCP80 protected)
2. ISD-R verifies SCP80 security
3. ISD-R performs PSK-TLS handshake with SM-SR
4. ISD-R sends initial `POST <initial-uri>` with headers:
   - `X-Admin-Protocol: globalplatform-remote-admin/1.0`
   - `X-Admin-From: //se-id/eid/<EID>;//aa-id/aid/<ISD-R AID>`

**Command delivery** (SM-SR → eUICC):
- SM-SR responds `HTTP/1.1 200` with `Content-Type: application/vnd.globalplatform.card-content-mgt;version=1.0`
- `X-Admin-Next-URI` provides the URI for the eUICC's next POST
- If targeting an ISD-P: `X-Admin-Targeted-Application: //aid/<rid>/<pix>` identifies the ISD-P by AID
- Body contains the command script (Expanded Remote Command format)

**Response delivery** (eUICC → SM-SR):
- eUICC sends `POST <next-uri>` with `Content-Type: application/vnd.globalplatform.card-content-mgt-response;version=1.0`
- `X-Admin-Script-Status: ok` (or error status)
- Body contains the response script

**Session management:**
- `HTTP/1.1 204` (No Content) with `X-Admin-Next-URI` keeps the session alive for the next exchange
- `HTTP/1.1 204` without `X-Admin-Next-URI` closes the session

The eUICC uses **Chunked Transfer Encoding** for POST requests. The SM-SR uses chunked encoding for POST responses. This allows streaming of large profile packages without buffering.

---

## CAT_TP — Constrained Network Transport

**CAT_TP** (Card Application Toolkit Transport Protocol) provides an alternative to HTTPS for scenarios where TCP/TLS overhead is problematic — very low bandwidth, high latency, or intermittent connections (SGP.02 §2.4.3.2).

CAT_TP operates over the **BIP** (Bearer Independent Protocol) channel defined in ETSI TS 102 223. The transport provides reliable, connection-oriented data transfer with flow control, optimized for the constrained environment of a UICC communicating through a modem.

Commands sent over CAT_TP use the same SCP80 security as SMS — the expanded remote command structure with AES-CMAC cryptographic checksums and AES-CBC encryption. The security is at the application layer, not the transport layer.

CAT_TP is particularly valuable for:
- 2G/3G networks where TCP performance is poor
- Devices with limited IP stack capabilities
- Deployments where the SM-SR wants a lightweight, persistent connection without TLS overhead

---

## DNS Resolution — Finding the SM-SR

DNS resolution is an optional but powerful ES5 feature (SGP.02 §2.4.5). It allows the eUICC to resolve the SM-SR's FQDN to an IP address dynamically, rather than relying on a hardcoded IP.

### When DNS Resolution Triggers

The eUICC performs DNS resolution when ALL of these conditions are met:
1. The eUICC is requested to open an HTTPS session
2. The eUICC supports DNS resolution
3. The ISD-R has no hardcoded IP address in its Connection Parameters or the triggering SMS
4. The ISD-R has an FQDN and DNS server IP addresses configured
5. The ISD-R hasn't already resolved the FQDN, or considers the cached value stale

### DNS Protocol Details

The DNS resolver on both SM-SR and eUICC must:
- Comply with **RFC 1035** and **RFC 3596** (Domain Name System)
- Support query types **A** (IPv4) and **AAAA** (IPv6)
- Use **UDP** transport

The flow is simple: the eUICC's DNS Resolver Client sends a query to the configured DNS Resolver Server (typically the SM-SR itself or a network-provided DNS server), which returns the resolved IP addresses. This happens after the SMS trigger but before the TLS handshake.

The eUICC may implement proprietary retry procedures, load balancing across multiple resolved IP addresses, and fallback logic — but these implementation details are out of scope for SGP.02.

---

## The ES8 Tunnel — A Secure Channel Inside a Secure Channel

ES8 is the interface between the SM-DP and the ISD-P, but it has no physical layer of its own. Instead, it's a tunnel (SGP.02 §2.5):

```
SM-DP ──ES3──▶ SM-SR ──ES5──▶ ISD-R ──▶ ISD-P
  └── SCP03/SCP03t ────────────┘
  └──── ES8 logical channel ────┘
```

The SM-DP encrypts commands for the ISD-P using SCP03 or SCP03t. This encrypted payload is carried over ES3 (SM-DP to SM-SR) using whatever secure transport those two servers have agreed upon. The SM-SR then wraps the SCP03 payload inside the SCP80/SCP81-protected ES5 channel to the ISD-R. The ISD-R forwards the payload to the target ISD-P, which decrypts and processes it.

The SM-SR **cannot decrypt the ES8 payload** — it sees only the encrypted SCP03 data. This ensures the SM-SR, despite being the OTA gateway, has no access to profile contents.

---

## ES6 and ES1 — Other Communication Paths

Two additional communication interfaces complete the picture:

**ES6 (Operator → MNO-SD)**: The Operator's OTA platform communicates directly with the MNO-SD inside a Profile. This uses the same SCP80/SCP81 secure channel model as ES5, following ETSI TS 102 225/226. The initial OTA keys are loaded during profile download or at manufacturing. This is how the operator manages its profile post-install — updating network parameters, installing applets, or refreshing file contents — without involving the SM-DP or SM-SR.

**ES1 (EUM → SM-SR)**: At manufacturing time, the EUM sends the EIS to the first SM-SR. The ISD-R key sets in the EIS are protected by a mechanism agreed between the EUM and SM-SR, which must include at minimum: AES-128 transport key, ECB cipher mode, and PKCS#7 padding when needed.

---

## 📋 Summary

- The SM-SR has exclusive OTA access to the eUICC via the ES5 interface — the defining characteristic of the push model
- SMS handles short platform management commands and triggers HTTPS/CAT_TP sessions for bulk operations
- HTTPS uses PSK-TLS (not certificate TLS), with keys derived from the SCP81 key set shared between SM-SR and ISD-R
- The HTTP POST pattern follows GlobalPlatform RAM over HTTP: half-duplex, chunked, with X-Admin headers for session management
- CAT_TP provides a lightweight alternative for constrained networks, with the same SCP80 application-layer security as SMS
- DNS resolution lets the eUICC dynamically locate the SM-SR, decoupling the chip from hardcoded IP addresses
- ES8 tunnels SCP03/SCP03t through ES3→ES5, ensuring the SM-SR never sees profile plaintext despite being the OTA gateway

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

← Previous: [M2M Certificate Hierarchy]({{ site.baseurl }}/docs/articles/sgp02/03-sgp02-pki) | Next: [Profile Download]({{ site.baseurl }}/docs/articles/sgp02/05-sgp02-download) →

</div>

---

*Based on GSMA SGP.02 v4.2 §2.4–2.8 — OTA Communication and Secure Channels*


---

← Previous: [M2M Certificate Hierarchy: CI, EUM, SM-DP, SM-SR, and eUICC](03-sgp02-pki) | [Section Index](index) | Next: [Profile Download: ISD-P Creation, SCP03, and Encrypted Delivery](05-sgp02-download) →
