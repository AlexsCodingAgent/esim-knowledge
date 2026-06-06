---
date: 2026-06-07
---

# Profile Download: ISD-P Creation, SCP03, and Encrypted Delivery

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > Profile Download: ISD-P Creation, SCP03, and Encrypted Delivery**

> **📚 Prerequisites:** This article ties together concepts from all previous articles — the architecture (roles and interfaces), eUICC internals (ISD-R/ISD-P/ECASD), PKI (certificates and key establishment), and OTA communication (ES5/ES8 tunneling). Reading those first is strongly recommended.

> **💡 Why this matters:** Profile download is the main event — it's the procedure that actually puts an operator's credentials onto a chip. Every security mechanism in SGP.02 converges here: certificate verification, ephemeral key agreement, SCP03 session establishment, and encrypted profile delivery.

> **Key takeaways:**
> - Profile download has four phases: ISD-P creation, Key Establishment (Scenario#3), encrypted download, and optional enabling
> - Key Establishment uses ECKA-EG (ElGamal) with mutual authentication — both SM-DP and eUICC prove their identities cryptographically
> - The SCP03 keyset is derived from an ephemeral-ephemeral key agreement, providing forward secrecy for every download
> - Profile packages are delivered as SCP03t-encrypted TLV structures, processed by the ISD-P's Profile Package Interpreter
> - Error management and cleanup sub-routines ensure failed downloads don't leave orphaned ISD-Ps

---

## The Four-Phase Procedure

SGP.02 §3.1 defines the Profile Download and Installation procedure as the most complex and security-critical operation in the specification. It's sub-divided into four phases:

1. **ISD-P Creation** — A new profile container is instantiated on the eUICC
2. **Key Establishment with Scenario#3 Mutual Authentication** — The SM-DP and eUICC authenticate each other and derive session keys
3. **Download and Installation of the Profile** — The encrypted profile package is streamed and installed
4. **Optional: Enabling** — The newly installed profile is activated

Each phase involves coordination across the entire ecosystem: Operator, SM-DP, SM-SR, ISD-R, ISD-P, and ECASD.

---

## Phase 1 — ISD-P Creation

Before a profile can be downloaded, a container must exist. ISD-P creation (SGP.02 §3.1.1) establishes the empty ISD-P on the eUICC. Here's the flow:

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

**Step-by-step:**

**(1)** The Operator calls `ES2.DownloadProfile` providing the SM-SR identification, EID, ICCID, final state (Enabled or Disabled), and profile type. The Operator may request that the profile be enabled after installation.

**(2-4)** The SM-DP calls `ES3.GetEIS` to retrieve the eUICC's Information Set from the SM-SR. The SM-SR looks up the EID. If unknown, it returns an error. If found, it returns the complete EIS including the ECASD certificate.

**(5)** The SM-DP checks eUICC eligibility:
- Is the target profile compatible with this eUICC type?
- Does the eUICC have enough remaining memory?
- Is the eUICC certified?
- **Critically**: The SM-DP verifies `CERT.ECASD.ECKA` using the EUM Certificate and CI Root Certificate, extracting `PK.ECASD.ECKA` for later key establishment. If this verification fails, the procedure stops immediately — the chip cannot be trusted.

If any check fails, the SM-DP returns an error to the Operator.

**(6-7)** The SM-DP calls `ES3.CreateISDP`. The SM-SR verifies the request is acceptable (authorization, resource availability) and creates a new Profile entry in the EIS with state "In-Creation" — this profile won't appear in `GetEIS` responses until the creation is confirmed.

**(8-9)** The SM-SR triggers an HTTPS session (if not already open) and sends `ES5.CreateISDP` in the HTTP POST response.

**(10-11)** The ISD-R creates the ISD-P. The new ISD-P enters the **SELECTABLE** state. The ISD-R returns the response via the next HTTP POST.

**(12-13)** The SM-SR updates the EIS entry state from "In-Creation" to **"Created"** and returns the `ES3.CreateISDP` response to the SM-DP.

At this point, an empty ISD-P exists. It has no keys, no profile — just a container with an AID and an ICCID. If the SM-DP does not indicate "more to do," the SM-SR may close the HTTPS session.

---

## Phase 2 — Key Establishment with Scenario#3 Mutual Authentication

This is the cryptographic heart of SGP.02. The SM-DP and eUICC must establish a shared SCP03 keyset without either revealing their long-term private key, while simultaneously proving their identities (SGP.02 §3.1.2).

The procedure uses **Scenario#3** from GlobalPlatform Amendment E (ECKA-EG key agreement) plus an additional SM-DP authentication step — hence "Scenario#3-Mutual Authentication."

### The Protocol in Detail

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

**Step-by-step:**

**(1-3)** The SM-DP sends its certificate (`CERT.DP.ECDSA`) to the eUICC via `ES3.SendData`. The SM-SR relays it through the ES5 HTTPS session.

**(3a-3b)** The ISD-R forwards the certificate to the ISD-P. The ISD-P verifies it's an SM-DP certificate (not an SM-SR or other certificate type).

**(4-6)** The ISD-P forwards `CERT.DP.ECDSA` to the ECASD. The ECASD:
1. Verifies the certificate using `PK.CI.ECDSA` (the CI root public key stored during manufacturing)
2. If valid, extracts and stores `PK.DP.ECDSA` (the SM-DP's public key)
3. Generates a **Random Challenge (RC)** — 16 or 32 bytes of fresh randomness

The RC serves two purposes: it proves the response is fresh (preventing replay attacks), and it will be signed by the SM-DP to prove possession of the corresponding private key.

**(7-8)** The RC travels back up the chain: ISD-P → ISD-R → SM-SR → SM-DP.

**(9)** The SM-DP generates an **ephemeral EC key pair** (`ePK.DP.ECKA` / `eSK.DP.ECKA`) — fresh for this transaction, never used before, never used again. It then signs the RC concatenated with `ePK.DP.ECKA` using its long-term private key (`SK.DP.ECDSA`). This signature proves two things:
- The SM-DP controls the private key corresponding to `CERT.DP.ECDSA` (authentication)
- The ephemeral public key genuinely came from this SM-DP (binding)

**(10-11)** The signed data (`ePK.DP.ECKA` + signature over RC and `ePK.DP.ECKA`) is sent back to the eUICC via `ES3.SendData` → ES5 relay.

**(12-14)** The ISD-P forwards the data to the ECASD, which:
1. Verifies the signature using the previously stored `PK.DP.ECDSA`
2. If valid, computes the **Shared Secret (ShS)** using `ePK.DP.ECKA` (SM-DP's ephemeral public key) and `SK.ECASD.ECKA` (the eUICC's long-term private key)

The ECKA-EG algorithm ensures that ShS is identical to what the SM-DP will independently compute using `eSK.DP.ECKA` and `PK.ECASD.ECKA` — without either side revealing its private key.

**(15-16)** The ISD-P:
- Optionally generates a **Derivation Random (DR)** if requested by the SM-DP
- Derives the SCP03 keyset from ShS (and DR if present) using a key derivation function
- Calculates a **receipt** — a cryptographic proof that key derivation succeeded correctly
- Returns the receipt (and optional DR) to the ISD-R

**(17-18)** The receipt travels back to the SM-DP.

**(19)** The SM-DP independently:
1. Computes ShS using `eSK.DP.ECKA` and `PK.ECASD.ECKA` (extracted from the ECASD certificate in step 5)
2. Derives the same SCP03 keyset from ShS (and DR if used)
3. Verifies the receipt — confirming the eUICC derived the same keyset

At this point, both sides hold identical SCP03 keys and have mutually authenticated. The ISD-P transitions from **SELECTABLE** to **PERSONALIZED**.

### Key Security Properties

- **Forward secrecy**: `eSK.DP.ECKA` is ephemeral and destroyed after use. Even if `SK.ECASD.ECKA` is later compromised, past session keys cannot be recovered.
- **Mutual authentication**: The SM-DP proves its identity by signing RC with `SK.DP.ECDSA` (verified against `CERT.DP.ECDSA` → CI root). The eUICC proves its identity by computing ShS with `SK.ECASD.ECKA` (verified when the SM-DP's independently computed receipt matches).
- **Key confirmation**: The receipt provides explicit confirmation that both sides derived the same key material.

---

## Phase 3 — Download and Installation

With the SCP03 channel established, the actual profile can be delivered (SGP.02 §3.1.3).

### The Delivery Protocol

The download uses a repeated call pattern:

```
SM-DP ──ES3.SendData(profile data)──▶ SM-SR ──ES5 relay──▶ ISD-R ──▶ ISD-P
  ◀──ES3.SendData response─────────  SM-SR ◀──ES5 POST──  ISD-R ◀── ISD-P
```

Each iteration:
1. The SM-DP calls `ES3.SendData` providing a chunk of profile data, targeted at the ISD-P AID
2. The SM-SR verifies the request, triggers HTTPS if needed, and sends the data in an HTTP POST response with `X-Admin-Targeted-Application: //aid/<ISD-P AID>`
3. The ISD-R forwards the secured data to the identified ISD-P
4. The ISD-P processes the SCP03/SCP03t security: it decrypts, verifies the MAC, and executes the command TLVs
5. Responses travel back through the same chain
6. The SM-DP may call `ES3.SendData` repeatedly — as many times as needed to stream the entire profile package

### The Profile Package

The profile data is formatted as a **Profile Package** conforming to the SIMalliance eUICC Profile Package Interoperable Format (version 2.3.1 minimum). The package is wrapped in **SCP03t** — a variant of SCP03 defined in SGP.02 §4.1.3.3 that's optimized for profile transport.

SCP03t provides:
- **AES-128 CBC** encryption of profile elements
- **C-MAC** (Command MAC) on data from SM-DP to ISD-P
- **R-MAC** and **R-ENCRYPTION** on responses from ISD-P to SM-DP
- Pseudo-random card challenge (mode `i='70'`)

The ISD-P's **Profile Package Interpreter** decodes each TLV element and installs the corresponding Profile Component:
- **MNO-SD** with its SCP80/SCP81 key sets
- **NAAs** (USIM, ISIM, CSIM) with IMSI and authentication keys
- **File System** (MF, DF, EF structures)
- **Applets and Supplementary Security Domains**
- **POL1** — Policy Rules for this Profile

### Completion

When all profile elements have been delivered, the SM-DP calls `ES3.ProfileDownloadCompleted`. This:
- Signals the SM-SR that the profile is fully installed
- Allows the SM-DP to set **POL2** on the profile (the Operator specifies POL2 content, which may be empty)
- The SM-SR updates the EIS: profile state moves from "Created" to **"DISABLED"**

The SCP03 keyset may then be:
- **Retained** by the SM-DP (for future profile management via ES8)
- **Handed over** to the Operator (who may replace the keys)
- **Deleted** from the eUICC by the SM-DP

---

## Phase 4 — Optional Enabling

If the Operator requested the profile be enabled after download:

1. The SM-DP requests the SM-SR to enable the newly installed profile (following the procedure in §3.3 with modifications)
2. The SM-SR sends `ES5.EnableProfile` to the ISD-R
3. The ISD-R enforces POL1 and POL2, disables the currently enabled profile, enables the new one
4. The eUICC sends a REFRESH proactive command to the Device, triggering a new network attach

If enabling fails (e.g., connectivity lost before completion), the SM-DP returns `Executed-WithWarning` — the profile is downloaded but not yet active.

---

## Error Management and Cleanup

SGP.02 defines two sub-routines for handling failures during the download procedure (§3.1.4, §3.1.5):

### Error Management Sub-Routine

If an error occurs during key establishment or download (before the optional enabling), the SM-DP calls `ES3.DeleteISDP` to remove the partially created ISD-P. The SM-SR relays this via `ES5.DeleteProfile` to the ISD-R, which deletes the ISD-P — but only if **POL1** doesn't forbid deletion. If POL1 prevents deletion, the SM-DP considers the profile installation succeeded (the ISD-P exists on the eUICC and can't be removed).

### ISD-P Cleanup Sub-Routine

Before installing a new profile, the SM-DP checks if the EIS indicates an existing ISD-P in "Created" state associated with the same SM-DP (same `smdp-id`). If so, it deletes that ISD-P first — whether it has the same or a different ICCID — to clean up from a previous failed attempt.

---

## Notification Flow

Once the profile is successfully downloaded (and optionally enabled), a notification cascade begins:

1. The SM-DP returns the `ES2.DownloadProfile` response to the Operator
2. If a M2M SP is authorized to receive notifications, the SM-SR sends `ES4.HandleProfileDownloadedNotification` to the M2M SP
3. If the M2M SP is another Operator connected through its SM-DP, the notification routes through `ES3.HandleProfileDownloadedNotification` → `ES2.HandleProfileDownloadedNotification`

This ensures all stakeholders know the profile is installed and available.

---

## 📋 Summary

- Profile download has four phases: ISD-P creation (empty container), key establishment (Scenario#3 mutual authentication with ECKA-EG), encrypted delivery (SCP03t tunnel), and optional enabling
- Key establishment provides mutual authentication, forward secrecy via ephemeral keys, and key confirmation via receipts — all without transmitting either side's private key
- The SCP03 keyset is derived from an ECKA-EG shared secret, optionally mixed with a Derivation Random for additional key material diversity
- Profile packages are streamed in chunks through the SM-SR relay, encrypted end-to-end between SM-DP and ISD-P
- Error management ensures failed downloads don't leave orphaned ISD-Ps, subject to POL1 constraints
- After download, the SCP03 keys can be retained, handed over to the Operator, or deleted — giving operators flexibility in post-install key management

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

← Previous: [OTA Communication]({{ site.baseurl }}/docs/articles/sgp02/04-sgp02-ota) | Next: Profile Lifecycle — Coming Soon →

</div>

---

*Based on GSMA SGP.02 v4.2 §3.1 — Profile Download and Installation*


---

← Previous: [OTA Communication: SMS, PSK-TLS, CAT_TP, and DNS](04-sgp02-ota) | [Section Index](index) | Next: [Profile Lifecycle: Enable, Disable, Delete, and Fall-Back](06-sgp02-lifecycle) →
