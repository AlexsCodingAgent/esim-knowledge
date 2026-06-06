---
date: 2026-06-07
---

# Inside the M2M eUICC: ISD-R, ISD-P, ECASD, and EID

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > Inside the M2M eUICC: ISD-R, ISD-P, ECASD, and EID**

> **📚 Prerequisites:** Read the [SGP.02 Architecture]({{ site.baseurl }}/docs/articles/sgp02/01-sgp02-architecture) article first to understand the roles and interfaces. The [Prerequisites Guide]({{ site.baseurl }}/docs/prerequisites) covers GlobalPlatform security domains and smart card fundamentals.

> **💡 Why this matters:** The eUICC's internal security domain architecture is what makes multi-stakeholder isolation possible — one chip hosting profiles from competing operators, each unable to see or touch the others. This article shows you how that isolation is achieved at the hardware level.

> **Key takeaways:**
> - Three security domains form the eUICC's backbone: ISD-R (platform manager), ECASD (root of trust), ISD-P (profile container)
> - The ISD-R is the on-card representative of the SM-SR — there's exactly one per chip
> - ISD-Ps are cryptographically isolated containers, each holding exactly one Profile
> - The ECASD holds the chip's unique identity (EID and private key) and is immutable after manufacturing
> - Profile isolation is absolute: no ISD-P can access another ISD-P's keys, data, or applications

---

## The Security Domain Architecture

SGP.02 §2.2 defines the eUICC's internal architecture, which builds directly on the GlobalPlatform Card Specification. The chip is organized into **Security Domains** — isolated execution environments with their own keys, privileges, and lifecycle states. Three types of Security Domain form the core:

```
┌─────────────────────────────────────┐
│               eUICC                  │
│  ┌──────────┐  ┌──────────────────┐ │
│  │  ECASD   │  │      ISD-R       │ │
│  │ (CI rep) │◄─┤  (SM-SR rep)     │ │
│  │          │  │                  │ │
│  │ PK.CI    │  │ Platform Mgmt    │ │
│  │ SK.ECASD │  │ SCP80/SCP81 keys │ │
│  │ CERT     │  │ POL2 storage     │ │
│  │ EID      │  └──────┬───────────┘ │
│  └──────────┘         │              │
│                ┌──────┴──────┐       │
│                │  Associate  │       │
│       ┌────────┴──┐  ┌──────┴────┐  │
│       │  ISD-P 1  │  │  ISD-P n  │  │
│       │ (SM-DP)   │  │ (SM-DP)   │  │
│       │           │  │           │  │
│       │ Profile 1 │  │ Profile n │  │
│       │ MNO-SD    │  │ MNO-SD    │  │
│       │ NAA, FS   │  │ NAA, FS   │  │
│       │ Applets   │  │ Applets   │  │
│       └───────────┘  └───────────┘  │
└─────────────────────────────────────┘
```

This architecture achieves something remarkable: **multiple stakeholders share one chip with hardware-enforced isolation**. The EUM manufactured it. The CI signed its certificates. The SM-SR manages it. One operator's profile lives in ISD-P 1. A competitor's profile lives in ISD-P 2. None can touch each other's keys.

---

## ECASD — The Root of Trust

The **ECASD** (eUICC Controlling Authority Security Domain) is the chip's immutable identity. There is exactly one per eUICC, installed and personalized by the EUM during manufacturing. After manufacturing it cannot be modified — it has no keys that can be updated and no lifecycle transitions after PERSONALIZED.

### What the ECASD Holds

The ECASD is personalized with four critical items ($2.2.1.2):

- **`PK.CI.ECDSA`** — The CI's root public key. This is the trust anchor that verifies SM-DP and SM-SR certificates. If you control this key, you control which servers the eUICC will trust.

- **`SK.ECASD.ECKA`** — The eUICC's unique private key. This never leaves the chip. It's used during Scenario#3 key establishment to generate the shared secret (`ShS`) with the SM-DP's ephemeral key pair.

- **`CERT.ECASD.ECKA`** — The eUICC's certificate, signed by the EUM. This is the chip's cryptographic identity document. It contains the corresponding public key (`PK.ECASD.ECKA`), the EID, and a technical reference identifying the Common Criteria certification report.

- **`EID`** — The 32-digit eUICC Identifier, retrievable by the Device at any time via the GlobalPlatform `GET DATA` command.

### ECASD Services

The ECASD is involved in exactly two operations:

1. **SM-DP key set establishment** during Profile Download and Installation (§3.1.2) — it verifies `CERT.DP.ECDSA` using `PK.CI.ECDSA`, generates a random challenge, and computes the shared secret using its private key
2. **SM-SR key set establishment** during SM-SR Change (§3.8) — it authenticates the new SM-SR

Only the ISD-R and ISD-Ps can use ECASD services. No profile component has direct access to the ECASD.

---

## ISD-R — The Platform Manager

The **ISD-R** (Issuer Security Domain — Root) is the on-card representative of the SM-SR. There is exactly one per eUICC. It's installed and first personalized by the EUM during manufacturing and enters the PERSONALIZED lifecycle state immediately — it never supports the LOCKED state.

### ISD-R Responsibilities

The ISD-R is the gatekeeper for all Platform Management operations. It:

- **Creates ISD-Ps** — when the SM-SR sends `ES5.CreateISDP`, the ISD-R instantiates a new profile container
- **Enables and disables Profiles** — making one profile's NAA selectable over the UICC-Terminal interface and deactivating the previous one
- **Deletes ISD-Ps** — permanently removing a profile and its container, including during Master Delete
- **Manages the Fall-Back Attribute** — setting which profile activates automatically on connectivity loss
- **Relays ES8 traffic** — forwarding SCP03/SCP03t commands between the SM-SR and the target ISD-P
- **Enforces POL1** — checking profile policy rules before executing lifecycle operations

The ISD-R holds the SCP80 and optionally SCP81 key sets used to secure the ES5 OTA channel with the SM-SR. These are the keys that protect platform management commands over SMS, HTTPS, or CAT_TP.

### GlobalPlatform Privileges

The ISD-R's privileges are defined in SGP.02 Annex C. Critically, it has the **Authorized Management** (AM) privilege over every ISD-P. This means it can perform Token Verification (checking that commands originate from an authorized source) and manage ISD-P lifecycle — but it **cannot read Profile contents** beyond POL1 and Connectivity Parameters.

---

## ISD-P — The Profile Container

An **ISD-P** (Issuer Security Domain — Profile) hosts exactly one Profile. Multiple ISD-Ps can exist on an eUICC, but only one can be in the **ENABLED** state at any time.

### ISD-P Creation and Lifecycle

An ISD-P follows a strictly defined lifecycle (SGP.02 §2.2.1.3, Figure 3):

```
  [Created via ES5.CreateISDP]
            │
            ▼
       SELECTABLE ◄── ISD-P exists but empty
            │
            │ Key Establishment (§3.1.2)
            ▼
      PERSONALIZED ◄── SCP03 keys loaded, ready for profile
            │
            │ Profile Download (§3.1.3)
            ▼
        DISABLED ◄──────────┐
            │                │
            │ Enable (§3.2)  │ Disable (§3.4)
            ▼                │ or Fall-Back
        ENABLED ────────────┘
            │
            │ Delete
            ▼
        [Deleted — ISD-P removed from eUICC]
```

Key points:
- The INSTALLED state (from GlobalPlatform) is skipped — `ES5.CreateISDP` takes the ISD-P directly to SELECTABLE
- The LOCKED state is not supported for ISD-Ps
- After profile download completes successfully, the ISD-P transitions to DISABLED
- Enabling a new profile automatically disables the previously enabled one
- The Fall-Back Mechanism can also trigger enable/disable transitions

### ISD-P Privileges

All Profile Components created within an ISD-P remain permanently affiliated with it. You cannot change the affiliation of a profile component. This ensures that when an ISD-P is deleted, every component within it is cleanly removed.

ISD-P privileges (Annex C) include the ability to create applications (NAAs, applets), create supplementary security domains (like the MNO-SD), and manage the profile's file system — but only within its own container.

---

## Profile Structure

A Profile inside an ISD-P is a complete operator subscription. It contains (SGP.02 §2.2.4):

**MNO-SD** (Mobile Network Operator Security Domain) — The operator's on-card representative. Holds the SCP80/SCP81 keys for the ES6 OTA channel. The Operator uses this to perform post-install profile management directly, bypassing the SM-DP and SM-SR.

**NAAs** (Network Access Applications) — The authentication applications: USIM (for 3G/4G/5G), ISIM (for IMS/VoLTE), or CSIM (for CDMA). These contain the IMSI, authentication keys, and network parameters.

**File System** — Standard UICC files: phonebook, SMS storage, network parameters, service tables. The ISD-R has read access to Connectivity Parameters (SMSC address, DNS configuration) but nothing else.

**Applets and Supplementary Security Domains** — Payment applications, NFC secure elements, proprietary operator applets. These run inside the ISD-P's isolation boundary.

**POL1** — Policy Rules embedded in the Profile (stored in the ISD-P's file system). These govern what lifecycle operations are permitted on this specific profile. The ISD-R reads POL1 when considering whether to allow an enable, disable, or delete operation.

**POL2** — Policy Rules associated with a Profile but stored in the ISD-R (outside the ISD-P). This allows faster access during platform management. When POL1 and POL2 conflict, SGP.02 defines priority rules.

### Profile Isolation

The isolation between ISD-Ps is absolute (SGP.02 §2.2.1.3):
- No component outside an ISD-P has visibility or access to any Profile Component (except the ISD-R's read access to POL1 and Connectivity Parameters)
- A Profile Component cannot see or access anything outside its ISD-P
- An ISD-P cannot see or access any other ISD-P
- The same AID or TAR can be allocated within different Profiles — the ISD-P boundary prevents collisions

When an ISD-P is not in the enabled state, the eUICC ensures that its file system is unselectable by the Device, its applications cannot be triggered, and remote management via ES6 is blocked.

---

## The EID — eUICC Identifier

The **EID** is a 32-digit number that uniquely identifies each eUICC globally. Its structure (SGP.02 §2.2.2):

- **Digit 1**: Always `8` (Major Industry Identifier per ISO/IEC 7812)
- **Digit 2**: Always `9` (telecommunications per ISO/IEC 7812)  
- **Digits 3-5**: Country code (padded with leading zeros if shorter than 3 digits)
- **Digits 6-31**: Issuer-specific identifier
- **Digit 32**: Check digit per ISO/IEC 7812 Luhn algorithm

The EID is stored in the ECASD and can be retrieved by the Device at any time using the GlobalPlatform `SELECT` (targeting the ECASD AID) and `GET DATA` (tag `'5A'`) commands. It's the primary identifier used throughout the ecosystem — in ES2 profile orders, ES3 EIS lookups, ES4 lifecycle operations, and ES7 handovers.

---

## Secure Channels on the eUICC

SGP.02 §2.2.5 specifies how the various interfaces are secured:

| Interface | Between | Protocol | Protection |
|-----------|---------|----------|------------|
| ES5 | SM-SR ↔ ISD-R | SCP80 (or SCP81) | Origin authentication, integrity, confidentiality |
| ES6 | Operator ↔ MNO-SD | SCP80 (or SCP81) | Same security level as ES5 recommended |
| ES8 | SM-DP ↔ ISD-P | SCP03 / SCP03t | AES-128 CBC, C-MAC, R-MAC, R-ENCRYPTION |

The ES8 secure channel is the most interesting. SCP03 commands are wrapped, encrypted, and tunneled through the ES3 (SM-DP↔SM-SR) link, then through the SCP80/SCP81-protected ES5 channel to the ISD-R, which forwards them to the target ISD-P. The SM-SR acts as a secure relay — it transports the encrypted SCP03 payload but cannot decrypt it.

---

## Java Card and Hardware

The eUICC **MAY** support Java Card™ (SGP.02 §2.2.7). If supported, it must implement at least version 3.0.4 of the Java Card Classic Platform Specification. This enables post-issuance applet installation within profiles.

Hardware-wise (§2.2.8), the eUICC must be a **Tamper Resistant Element** — a hardware security module designed to resist physical attacks. It can be:
- **Discrete eUICC**: A separate chip, either removable (in an ETSI TS 102 221 form factor like MFF2) or non-removable (soldered)
- **Integrated eUICC**: Built into a larger SoC (System-on-Chip), sharing silicon with the modem or application processor

---

## 📋 Summary

- The eUICC's three Security Domains — ECASD (root of trust), ISD-R (platform manager), ISD-P (profile container) — partition the chip into isolated stakeholder zones
- The ECASD stores the chip's immutable identity (EID, private key, certificate, CI root key) and participates only in key establishment during profile download and SM-SR change
- The ISD-R is the SM-SR's sole on-card agent, enforcing POL1/PO2, managing profile lifecycle, and relaying ES8 traffic without seeing plaintext
- ISD-Ps provide hardware-enforced cryptographic isolation — profiles from competing operators coexist without any possibility of cross-access
- Profiles contain a complete operator subscription: MNO-SD, NAAs, file system, applets, and policy rules (POL1/POL2)
- The 32-digit EID uniquely identifies each eUICC globally, with the distinctive `89` prefix inherited from ISO/IEC 7812

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

← Previous: [M2M Ecosystem]({{ site.baseurl }}/docs/articles/sgp02/01-sgp02-architecture) | Next: [M2M Certificate Hierarchy]({{ site.baseurl }}/docs/articles/sgp02/03-sgp02-pki) →

</div>

---

*Based on GSMA SGP.02 v4.2 §2.2 — eUICC Architecture*


---

← Previous: [M2M Ecosystem: EUM, SM-DP, SM-SR, and the Operator](01-sgp02-architecture) | [Section Index](index) | Next: [M2M Certificate Hierarchy: CI, EUM, SM-DP, SM-SR, and eUICC](03-sgp02-pki) →
