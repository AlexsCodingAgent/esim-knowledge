---
title: "How a Profile Gets Delivered: The eSIM Download Process"
date: 2026-05-29
---

# How a Profile Gets Delivered: The eSIM Download Process

> **💡 Why this matters:** The profile download is the core transaction in the eSIM ecosystem — it's where the security model proves itself. Understanding the three-phase flow (initiation, mutual authentication, install) is essential for debugging, implementing, or integrating with any RSP component.

> **Key takeaways:**
> - Profile delivery has three phases: ordering via `ES2+`, mutual authentication via `ES9+`/`ES10b`, and encrypted installation via `ES8+`
> - Mutual authentication requires the server to prove its identity **first** — the eUICC reveals nothing before verifying the SM-DP+
> - The profile package goes through four transformation stages: UPP → PPP → BPP → SBPP
> - Every `ES8+` function call uses SCP03t encryption with Perfect Forward Secrecy session keys
> - The LPA is a completely passive transport — all security is end-to-end between SM-DP+ and eUICC

---

Downloading an eSIM profile involves a carefully choreographed three-phase dance between the end user, the operator, the SM-DP+, the SM-DS, the LPA, and the eUICC. Here's exactly how it works, protocol step by protocol step.

---

## Phase 1: Initiation — Making the Order

Before anything can be downloaded, the operator must prepare a Profile for a specific eUICC. Here's the full download sequence from ordering through installation:

<img src="../diagrams/05-profile-download-sequence.svg" alt="Profile download sequence: initiation, mutual authentication, and encrypted installation across all three phases" style="width:100%;max-width:800px;display:block;margin:20px auto;border-radius:8px;">

The Activation Code the user receives is deceptively simple — it's an `LPA:1$` format string containing just the SM-DP+ address and a Matching ID. Everything else happens automatically.

**Ordering modes:**

| Mode | `ES2+` Flow | Use Case |
|------|-----------|----------|
| **Default** | `DownloadOrder` → `ConfirmOrder` | Standard postpaid subscription |
| **Activation Code** | `ConfirmOrder` only (with MatchingID) | Prepaid / QR code purchase |
| **SM-DS** | `ConfirmOrder` + SM-DS address | Push delivery via discovery server |

---

## Phase 2: Mutual Authentication — Who Are You?

Before any profile data moves, both sides must cryptographically prove their identities. This is the **Common Mutual Authentication** procedure, used identically for SM-DP+ and SM-DS communication.

```
Step 1-4: eUICC Challenge Generation
    LPA → eUICC: ES10a.GetEUICCInfo (optional, return euiccInfo1)
    LPA → eUICC: ES10b.GetEUICCChallenge
    eUICC: Generate random euiccChallenge
    eUICC → LPA: Return euiccChallenge

Step 5: TLS Connection
    LPA ↔ SM-DP+: Establish HTTPS (TLS server-auth mode)
    LPA verifies CERT.DP.TLS against GSMA CI chain

Step 6-7: Server Authentication
    LPA → SM-DP+: ES9+.InitiateAuthentication
        (euiccChallenge, euiccInfo1, SM-DP+ address)
    SM-DP+: Check SM-DP+ address, verify euiccInfo1
    SM-DP+: Generate TransactionID + serverChallenge

Step 8-9: Server Signs Challenge
    SM-DP+: Build serverSigned1 = {TransactionID,
        euiccChallenge, serverChallenge, SM-DP+ address}
    SM-DP+: Compute serverSignature1 over serverSigned1
    SM-DP+ → LPA: TransactionID, serverSigned1, serverSignature1,
                  euiccCiPKIdToBeUsed, CERT.DPauth.ECDSA

Step 10-14: eUICC Verifies Server
    LPA → eUICC: ES10b.AuthenticateServer
        (serverSigned1, serverSignature1, euiccCiPKIdToBeUsed,
         CERT.DPauth.ECDSA, ctxParams1)
    eUICC: Verify CERT.DPauth.ECDSA chain → GSMA CI
    eUICC: Verify serverSignature1 over serverSigned1
    eUICC: Verify serverSigned1 contents (challenge matches)
    eUICC: Generate euiccSigned1 = {TransactionID,
        serverChallenge, euiccInfo2, ctxParams1}
    eUICC: Compute euiccSignature1 over euiccSigned1
    eUICC → LPA: euiccSigned1, euiccSignature1,
                 CERT.EUICC.ECDSA, CERT.EUM.ECDSA

Step 15-16: Server Verifies eUICC
    LPA → SM-DP+: ES9+.AuthenticateClient
        (euiccSigned1, euiccSignature1,
         CERT.EUICC.ECDSA, CERT.EUM.ECDSA)
    SM-DP+: Verify CERT.EUM.ECDSA chain → GSMA CI
    SM-DP+: Verify CERT.EUICC.ECDSA
    SM-DP+: Verify euiccSignature1 over euiccSigned1
    SM-DP+: Verify euiccSigned1 (challenge + TransactionID match)
```

At this point, the SM-DP+ knows it's talking to a genuine eUICC, and the eUICC knows it's talking to an authorised SM-DP+. The mutual authentication is complete.

**Key security properties:**

- The server authenticates **first** — the eUICC never reveals private data or generates signed material before the server is verified
- The LPA is a **pass-through** — all cryptographic verification happens on the eUICC itself
- The TransactionID binds the entire session across multiple function calls

---

## Phase 3: Profile Download and Installation

With mutual authentication complete, the real work begins. The profile is delivered through a series of `ES8+` function calls tunnelled through the LPA.

### Step 1: Secure Channel Establishment

```
SM-DP+ → eUICC (via LPA): ES8+.InitialiseSecureChannel
    Performs ECDH key agreement → generates session keys:
        S-ENC (encryption), S-MAC (integrity), initial MAC chaining value

    These session keys provide Perfect Forward Secrecy —
    compromising the SM-DP+'s long-term key cannot expose past downloads.
```

The `InitialiseSecureChannel` block is sent in the clear — integrity and authenticity are ensured by the signatures from the mutual authentication phase.

### Step 2: ISD-P Creation

```
SM-DP+ → eUICC (via LPA): ES8+.ConfigureISDP
    Creates a new ISD-P (profile container)
    Content encrypted with S-ENC, MAC protected with S-MAC
```

### Step 3: Store Metadata

```
SM-DP+ → eUICC (via LPA): ES8+.StoreMetadata
    Writes profile metadata:
        - ICCID
        - Profile name
        - Operator name
        - Profile class (operational/provisioning/test)
        - Profile Policy Rules
    MAC protected (not encrypted — metadata is non-sensitive)
```

### Step 4: Replace Session Keys (Optional)

```
SM-DP+ → eUICC (via LPA): ES8+.ReplaceSessionKeys
    Swaps in profile-specific protection keys (PPK-ENC, PPK-MAC)
    Only used when the profile was pre-encrypted with different keys
    Protected by the original S-ENC/S-MAC session keys
```

### Step 5: Load Profile Elements

```
SM-DP+ → eUICC (via LPA): ES8+.LoadProfileElements (repeated)
    Streams the profile payload in SCP03t (GlobalPlatform Secure Channel
    Protocol 03 with transport-friendly encoding)-encrypted segments:
        - File system
        - Network Access Applications (NAAs)
        - Applets and supplementary security domains
        - Cryptographic keys

    The Profile Package Interpreter decodes each Profile Element TLV
    If any element fails, the installation rolls back with a specific error
```

### Step 6: Completion

The ISD-P is sealed, and the Profile transitions to the **Disabled** state. It's now installed on the eUICC but not yet active — the user must explicitly Enable it (or it may auto-enable if it's the only profile).

---

## Profile Package Stages

The profile data transforms through four stages on its journey from the operator to the eUICC:

| Stage | Name | Format | Location |
|-------|------|--------|----------|
| 1 | **UPP** — Unprotected Profile Package | SIMalliance TLV sequence | Inside SM-DP+ |
| 2 | **PPP** — Protected Profile Package | SCP03t-encrypted and MACed | Inside SM-DP+ |
| 3 | **BPP** — Bound Profile Package | PPP + key agreement + ISD-P creation + metadata | SM-DP+ output |
| 4 | **SBPP** — Segmented Bound Profile Package | BPP split into STORE DATA APDUs | LPA → eUICC delivery |

The BPP is cryptographically bound to one specific eUICC through the key agreement. Even if intercepted, it cannot be installed on any other chip.

---

## Error Handling

Key examples include:

| Error | Meaning |
|-------|---------|
| `installFailedDueToIccidAlreadyExistsOnEuicc(9)` | ICCID collision — profile already installed |
| `installFailedDueToInsufficientMemoryForProfile(10)` | Not enough storage space |
| `installFailedDueToInterruption(11)` | Download interrupted mid-stream |
| `installFailedDueToPEProcessingError(12)` | Profile Element TLV decoding failed |
| `installFailedDueToDataMismatch(13)` | Data integrity check failed |
| `pprNotAllowed(15)` | Blocked by Profile Policy Rules |

Each error is returned to the SM-DP+ via the `ES8+` channel, allowing the SM-DP+ to report installation status back to the operator via `ES2+` notifications.

---

## 📋 Summary

- Profile delivery is a three-phase protocol: ordering (`ES2+`), mutual authentication (`ES9+`/`ES10b`), and encrypted installation (`ES8+`)
- Server-authenticates-first ordering ensures the eUICC never exposes itself to an unverified SM-DP+
- The profile goes through four packaging stages (UPP → PPP → BPP → SBPP), with the BPP cryptographically bound to one specific chip
- All `ES8+` communication uses SCP03t with Perfect Forward Secrecy session keys — the LPA sees nothing
- Fourteen distinct error codes cover every failure mode from ICCID collision to policy rule violations

---

*Based on GSMA SGP.22 v2.2.2, Section 3 — Procedures*
