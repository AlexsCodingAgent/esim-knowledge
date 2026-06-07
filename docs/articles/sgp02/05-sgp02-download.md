---
description: "Breaks down the SGP.02 profile download procedure — ISD-P container creation, Scenario#3 mutual authentication with ECKA-EG, encrypted profile streaming through SCP03t tunnels, and post-download cleanup."
date: 2026-06-07
---

# Profile Download: ISD-P Creation, SCP03, and Encrypted Delivery

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > Profile Download: ISD-P Creation, SCP03, and Encrypted Delivery**

This is the procedure every other article in this series has been building toward. Profile download (SGP.02 §3.1) is where an operator's credentials actually land on a chip. The architecture, the PKI, the OTA channel, the ISD-R and ISD-P and ECASD: they all converge here. If you skipped the earlier articles, you'll want to loop back: the architecture ([roles and interfaces]({{ site.baseurl }}/docs/articles/sgp02/01-sgp02-architecture)), eUICC internals ([ISD-R, ISD-P, ECASD]({{ site.baseurl }}/docs/articles/sgp02/02-sgp02-euicc-internals)), PKI ([certificates and key establishment]({{ site.baseurl }}/docs/articles/sgp02/03-sgp02-pki)), and OTA ([ES5/ES8 tunneling]({{ site.baseurl }}/docs/articles/sgp02/04-sgp02-ota)) are all load-bearing here.

The download breaks into four movements: create an empty ISD-P container on the chip, run a cryptographic handshake to establish session keys (Scenario#3 mutual authentication with ECKA-EG), stream the encrypted profile package through an SCP03t tunnel, and optionally flip the new profile to active. Every bit of it is end-to-end encrypted between the SM-DP and the ISD-P; the SM-SR relays the bytes but never sees the plaintext. And if something goes wrong mid-download, cleanup routines make sure you don't wind up with orphaned ISD-Ps littering the chip.

---

## ISD-P Creation: Building the Container

Before anything can be downloaded, the chip needs somewhere to put it. ISD-P creation (SGP.02 §3.1.1) spins up an empty container.

```
Operator          SM-DP           SM-SR          ISD-R         ISD-P
   │                │               │              │              │
   │─(1) download──▶│               │              │              │
   │  Profile()     │               │              │              │
   │                │─(2) getEIS───▶│              │              │
   │                │   (eid)       │─(3) Retrieve │              │
   │                │◀─(4) EIS──────│  EIS          │              │
   │                │               │              │              │
   │                │─(5) Check     │              │              │
   │                │  eligibility  │              │              │
   │                │               │              │              │
   │                │─(6) create───▶│              │              │
   │                │  ISDP(eid,    │─(7) Check    │              │
   │                │   iccid, ...) │  conditions  │              │
   │                │               │              │              │
   │                │               │──(8) Trigger │              │
   │                │               │  HTTPS──────▶│              │
   │                │               │              │              │
   │                │               │──(9) ES5.───▶│              │
   │                │               │  CreateISDP  │──(10) New───▶│
   │                │               │              │◀─────────────│
   │                │               │◀─(11) POST───│              │
   │                │               │  response    │              │
   │                │               │              │              │
   │                │               │─(12) Update  │              │
   │                │               │  EIS         │              │
   │                │◀─(13) create──│              │              │
   │                │  ISDP resp.   │              │              │
```

**(1)** The Operator kicks things off with `ES2.DownloadProfile`, providing the SM-SR identification, EID, ICCID, the desired final state (Enabled or Disabled), and the profile type. They can also ask for the profile to be enabled automatically after installation.

**(2-4)** The SM-DP calls `ES3.GetEIS` to pull the eUICC Information Set from the SM-SR. The SM-SR looks up the EID. Unknown EID → error. Found → complete EIS, including the ECASD certificate.

**(5)** The SM-DP runs its eligibility checks: Is this profile compatible with this eUICC type? Enough remaining memory? Is the eUICC certified? But the one that really matters: the SM-DP verifies `CERT.ECASD.ECKA` against the EUM Certificate and CI Root Certificate, extracting `PK.ECASD.ECKA` for the key establishment that comes next. If this verification fails, the whole procedure stops dead. The chip can't be trusted.

**(6-7)** `ES3.CreateISDP` goes to the SM-SR. The SM-SR checks authorization and resources, then creates a new Profile entry in the EIS marked "In-Creation" (invisible to `GetEIS` until confirmed).

**(8-9)** The SM-SR triggers HTTPS (if not already open) and sends `ES5.CreateISDP` in the HTTP POST response.

**(10-11)** The ISD-R creates the ISD-P. The new ISD-P enters **SELECTABLE** state. Response flows back through the next HTTP POST.

**(12-13)** The SM-SR promotes the EIS entry from "In-Creation" to **"Created"** and returns `ES3.CreateISDP` response to the SM-DP.

At this point you've got an empty ISD-P: no keys, no profile, just an AID and an ICCID. If the SM-DP signals "no more to do," the SM-SR can close the HTTPS session.

---

## Key Establishment: The Cryptographic Handshake

This is where SGP.02 gets serious. The SM-DP and eUICC need a shared SCP03 keyset, and they need to prove to each other that they are who they claim to be, without either side exposing its long-term private key (SGP.02 §3.1.2).

The mechanism is Scenario#3 from GlobalPlatform Amendment E: ECKA-EG key agreement, plus an extra SM-DP authentication step. Hence the name "Scenario#3 Mutual Authentication."

### The Protocol, Step by Step

```
SM-DP                    SM-SR              ISD-R       ISD-P       ECASD
  │                        │                  │           │           │
  │─(1) sendData(eid, ────▶│                  │           │           │
  │  ES8.EstablishISDP     │                  │           │           │
  │  KeySet(CERT.DP))      │                  │           │           │
  │                        │─(3) HTTP 200────▶│           │           │
  │                        │  CERT.DP.ECDSA   │──(3a)───▶│           │
  │                        │                  │  CERT.DP  │           │
  │                        │                  │           │─(3b)─────│
  │                        │                  │           │Verify it's│
  │                        │                  │           │ SM-DP cert│
  │                        │                  │           │           │
  │                        │                  │           │─(4)──────▶│
  │                        │                  │           │CERT.DP    │
  │                        │                  │           │           │─(5) Verify
  │                        │                  │           │           │  with PK.CI
  │                        │                  │           │           │  Extract PK.DP
  │                        │                  │           │           │  Generate RC
  │                        │                  │           │◀─(6) RC───│
  │                        │                  │◀──(7) RC──│           │
  │                        │◀─(8) sendData───│            │           │
  │                        │  resp: RC        │           │           │
  │                        │                  │           │           │
  │─(9) Generate          │                  │           │           │
  │  (eSK.DP, ePK.DP)    │                  │           │           │
  │  Sign(RC, ePK.DP)    │                  │           │           │
  │  with SK.DP.ECDSA    │                  │           │           │
  │                        │                  │           │           │
  │─(10) sendData(eid,───▶│                  │           │           │
  │  ES8.EstablishISDP     │                  │           │           │
  │  KeySet(ePK.DP, sig))  │─(11) HTTP 200───▶│           │           │
  │                        │  ePK.DP, sig     │──(12)────▶│           │
  │                        │                  │           │           │
  │                        │                  │           │──(13)────▶│
  │                        │                  │           │Verify sig │
  │                        │                  │           │with PK.DP │
  │                        │                  │           │Compute ShS│
  │                        │                  │           │◀─(14) ShS─│
  │                        │                  │           │           │
  │                        │                  │           │─(15)     │
  │                        │                  │           │Derive     │
  │                        │                  │           │SCP03 keys │
  │                        │                  │           │Calc receipt│
  │                        │                  │◀──(16)───│           │
  │                        │                  │receipt(DR)│           │
  │                        │◀─(18) sendData───│           │           │
  │                        │  resp: receipt   │           │           │
  │                        │                  │           │           │
  │─(19) Compute ShS     │                  │           │           │
  │  from eSK.DP and     │                  │           │           │
  │  PK.ECASD.ECKA       │                  │           │           │
  │  Derive SCP03 keys   │                  │           │           │
  │  Verify receipt      │                  │           │           │
```

**(1-3)** The SM-DP sends `CERT.DP.ECDSA` toward the eUICC via `ES3.SendData`. The SM-SR relays it through the ES5 HTTPS session.

**(3a-3b)** The ISD-R hands the certificate to the ISD-P, which checks that it's actually an SM-DP certificate, not an SM-SR or something else.

**(4-6)** The ISD-P forwards `CERT.DP.ECDSA` to the ECASD. Now the ECASD goes to work:
1. Verify the certificate against `PK.CI.ECDSA`, the CI root public key from manufacturing
2. If valid, extract and store `PK.DP.ECDSA` (the SM-DP's public key)
3. Generate a **Random Challenge (RC)**: 16 or 32 fresh random bytes

The RC pulls double duty: it proves the response isn't a replay, and the SM-DP will sign it to prove it holds the private key matching `CERT.DP.ECDSA`.

**(7-8)** The RC climbs back up the chain: ISD-P → ISD-R → SM-SR → SM-DP.

**(9)** The SM-DP generates an ephemeral EC key pair (`ePK.DP.ECKA` / `eSK.DP.ECKA`), brand new, never used before, never used again. Then it signs RC concatenated with `ePK.DP.ECKA` using its long-term private key (`SK.DP.ECDSA`). That signature proves two things at once: the SM-DP controls the private key behind `CERT.DP.ECDSA` (authentication), and the ephemeral public key genuinely came from this SM-DP (binding).

**(10-11)** The signed bundle (`ePK.DP.ECKA` plus signature over RC and `ePK.DP.ECKA`) heads back to the eUICC through `ES3.SendData` → ES5 relay.

**(12-14)** The ISD-P forwards to the ECASD, which:
1. Verifies the signature using the previously stored `PK.DP.ECDSA`
2. If good, computes the **Shared Secret (ShS)** from `ePK.DP.ECKA` (the SM-DP's ephemeral public key) and `SK.ECASD.ECKA` (the eUICC's long-term private key)

ECKA-EG guarantees that ShS matches what the SM-DP will independently compute using `eSK.DP.ECKA` and `PK.ECASD.ECKA`, without either side revealing its private key.

**(15-16)** The ISD-P optionally generates a **Derivation Random (DR)** if the SM-DP requested one, derives the SCP03 keyset from ShS (and DR if present) via a key derivation function, calculates a **receipt** (cryptographic proof that key derivation succeeded), and returns the receipt (plus optional DR) to the ISD-R.

**(17-18)** The receipt travels back to the SM-DP.

**(19)** The SM-DP independently computes ShS from `eSK.DP.ECKA` and `PK.ECASD.ECKA` (extracted from the ECASD certificate back in step 5), derives the same SCP03 keyset, and verifies the receipt. A matching receipt confirms the eUICC landed on the same key material.

Both sides now hold identical SCP03 keys and have mutually authenticated. The ISD-P transitions from **SELECTABLE** to **PERSONALIZED**.

### What This Gets You

Three security properties fall out of this handshake:

**Forward secrecy.** `eSK.DP.ECKA` is ephemeral, destroyed after use. If `SK.ECASD.ECKA` gets compromised later, past session keys remain unrecoverable.

**Mutual authentication.** The SM-DP proves itself by signing RC with `SK.DP.ECDSA` (verifiable against `CERT.DP.ECDSA` → CI root). The eUICC proves itself by computing ShS with `SK.ECASD.ECKA` (verified when the SM-DP's independently computed receipt matches).

**Key confirmation.** The receipt gives both sides explicit confirmation they derived the same key material. No ambiguity.

---

## Download and Installation: Streaming the Profile

Now the SCP03 channel is up. Time to actually deliver the profile (SGP.02 §3.1.3).

The download runs as a repeated call loop:

```
SM-DP ──ES3.SendData(profile data)──▶ SM-SR ──ES5 relay──▶ ISD-R ──▶ ISD-P
  ◀──ES3.SendData response─────────  SM-SR ◀──ES5 POST──  ISD-R ◀── ISD-P
```

Each iteration:
1. The SM-DP calls `ES3.SendData` with a chunk of profile data, targeted at the ISD-P AID
2. The SM-SR verifies, triggers HTTPS if needed, sends the data in an HTTP POST response with `X-Admin-Targeted-Application: //aid/<ISD-P AID>`
3. The ISD-R forwards the secured data to the right ISD-P
4. The ISD-P handles SCP03/SCP03t: decrypt, verify MAC, execute the command TLVs
5. Responses flow back through the same chain
6. The SM-DP calls `ES3.SendData` as many times as needed to stream the entire profile package

### The Profile Package

The profile data arrives as a Profile Package conforming to the SIMalliance eUICC Profile Package Interoperable Format (version 2.3.1 minimum). It's wrapped in **SCP03t**, a variant of SCP03 defined in SGP.02 §4.1.3.3 that's tuned specifically for profile transport.

SCP03t provides:
- **AES-128 CBC** encryption on profile elements
- **C-MAC** (Command MAC) on SM-DP → ISD-P data
- **R-MAC** and **R-ENCRYPTION** on ISD-P → SM-DP responses
- Pseudo-random card challenge (mode `i='70'`)

The ISD-P's Profile Package Interpreter decodes each TLV element and installs the corresponding Profile Component:

- **MNO-SD** with its SCP80/SCP81 key sets
- **NAAs** (USIM, ISIM, CSIM): the IMSI and authentication keys
- **File System**: MF, DF, EF structures
- **Applets and Supplementary Security Domains**
- **POL1**: Policy Rules for this Profile

### Wrapping Up

When every profile element has been delivered, the SM-DP calls `ES3.ProfileDownloadCompleted`. This tells the SM-SR the profile is fully installed, lets the SM-DP set **POL2** on the profile (Operator specifies POL2 content, which may be empty), and the SM-SR updates the EIS: profile state moves from "Created" to **"DISABLED"**.

What happens to the SCP03 keyset after this? Three options:
- The SM-DP **retains** it (for future profile management via ES8)
- It gets **handed over** to the Operator (who can replace the keys)
- The SM-DP **deletes** it from the eUICC

---

## Optional Enabling

If the Operator requested the profile be enabled after download:

1. The SM-DP asks the SM-SR to enable the new profile (following §3.3 with modifications)
2. The SM-SR sends `ES5.EnableProfile` to the ISD-R
3. The ISD-R enforces POL1 and POL2, disables whatever profile is currently enabled, enables the new one
4. The eUICC fires a REFRESH proactive command at the Device, triggering a fresh network attach

If enabling fails (say connectivity drops before completion), the SM-DP returns `Executed-WithWarning`. The profile is downloaded and installed, just not yet active.

---

## When Things Go Wrong: Error Management and Cleanup

SGP.02 defines two cleanup sub-routines for when the download doesn't go smoothly (§3.1.4, §3.1.5):

### Error Management Sub-Routine

If something breaks during key establishment or download (before the optional enabling phase), the SM-DP calls `ES3.DeleteISDP` to remove the partially created ISD-P. The SM-SR relays `ES5.DeleteProfile` to the ISD-R, which deletes the ISD-P, but only if POL1 doesn't forbid deletion. If POL1 blocks it, the SM-DP treats the profile installation as having succeeded anyway: the ISD-P exists on the eUICC and can't be removed.

### ISD-P Cleanup Sub-Routine

Before installing a new profile, the SM-DP checks the EIS for an existing ISD-P in "Created" state associated with the same SM-DP (same `smdp-id`). If it finds one, it deletes it first (same ICCID or not), cleaning up debris from a previous failed attempt.

---

## The Notification Cascade

Once the profile is successfully downloaded (and optionally enabled), the notification chain fires:

1. The SM-DP returns `ES2.DownloadProfile` response to the Operator
2. If a M2M SP is authorized for notifications, the SM-SR sends `ES4.HandleProfileDownloadedNotification` to that M2M SP
3. If the M2M SP is another Operator connected through its own SM-DP, the notification routes through `ES3.HandleProfileDownloadedNotification` → `ES2.HandleProfileDownloadedNotification`

Every stakeholder who needs to know the profile is live gets the signal.

---

## Summary

- Profile download runs four phases: ISD-P creation (empty container), Scenario#3 mutual authentication with ECKA-EG (key establishment), SCP03t-encrypted streaming (profile delivery), and optional enabling
- The key establishment handshake delivers mutual authentication, forward secrecy via ephemeral keys, and key confirmation via receipts; without transmitting either side's private key
- SCP03 keyset is derived from an ECKA-EG shared secret, optionally mixed with a Derivation Random for additional material diversity
- Profile packages stream in chunks through the SM-SR relay, encrypted end-to-end between SM-DP and ISD-P
- Error management cleans up failed downloads (subject to POL1 constraints) so you don't accumulate orphaned ISD-Ps
- Post-download, the SCP03 keys can be retained, handed off to the Operator, or deleted; giving operators flexibility in how they handle post-install key material

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

← Previous: [OTA Communication]({{ site.baseurl }}/docs/articles/sgp02/04-sgp02-ota) | Next: [Profile Lifecycle]({{ site.baseurl }}/docs/articles/sgp02/06-sgp02-lifecycle) →

</div>

---

*Based on GSMA SGP.02 v4.2 §3.1: Profile Download and Installation*


---

← Previous: [OTA Communication: SMS, PSK-TLS, CAT_TP, and DNS](04-sgp02-ota) | [Section Index](index) | Next: [Profile Lifecycle: Enable, Disable, Delete, and Fall-Back](06-sgp02-lifecycle) →
