---
description: "The detailed security checklist for eUICC chips — four security policies, identity checks for every actor, and sealed communication channels that keep messages secret and tamper-proof."
title: "The Security Checklist: Steel Doors, Alarms, and Guards"
date: 2026-06-07
---

# The Security Checklist: Steel Doors, Alarms, and Guards 📋

## Imagine...

You're the head of security for a bank vault. Your checklist has specific items: steel doors that lock automatically, motion sensors on every wall, guards who check ID badges, and separate locked rooms for different customers' safe deposit boxes. If anything is missing: the vault fails inspection.

SGP.25 has exactly this kind of checklist. They're called **Security Functional Requirements** (SFRs) : precise, testable statements that say exactly what the eUICC chip must *do* to be secure. Not vague suggestions. Not "best efforts." Specific, measurable requirements.

---

## The Four Security Policies 🏛️

SGP.25 organises its requirements around four Security Function Policies (SFPs):

| Policy | What It Controls | Everyday Analogy |
|--------|-----------------|-----------------|
| **Secure Channel Protocol SFP** | Communications with remote servers | Encrypted phone line to the bank |
| **Platform Services SFP** | Access to the chip's internal tools | Only authorised staff can use the vault's drill |
| **ISD-R Content Access SFP** | Who can manage profiles | Only the vault manager has the master key |
| **ECASD Access SFP** | Who can touch secret keys | Only the security director knows the combination |

Each policy has specific rules about who can do what: and what happens when someone tries to break them.

---

## Who Goes There? Identification & Authentication 🎫

Before anyone can do *anything* on the chip, they must prove who they are:

| Requirement | What It Means |
|-------------|---------------|
| **FIA_UID.1** | "Show your ID before entering." : Every actor identified first |
| **FIA_UAU.1** | "Now prove it's really you." : Authentication must succeed |
| **FIA_USB.1** | "Here's your access badge." : Bind identity to permissions |
| **FIA_UAU.4** | "No re-using old passwords." : Single-use authentication only |
| **FIA_API.1** | "Here's proof of MY identity." : Chip proves it's real to others |

Different actors get authenticated differently:

- **Remote Key Maker (SM-DP+)** → Authenticated via certificates and signatures
- **Remote Operator (MNO-OTA)** → Authenticated via secure channel protocols
- **Remote Mission Control (EIM)** → Authenticated via eIM signatures (IoT only)
- **Local Profile App (MNO-SD)** → Authenticated via on-card application identity

---

## Sealed Envelopes: Communication Protection ✉️

Every message going in or out of the chip travels through protected channels:

```
FTP_ITC.1  : "Build a secure tunnel."
FDP_UCT.1  : "Keep the contents secret."
FDP_UIT.1  : "Make sure nobody tampered with it."
FDP_IFC.1  : "Here are the rules for what flows where."
```

Three secure channel protocols handle different conversations:

| Protocol | Between | Interface |
|----------|---------|-----------|
| **SCP-SGP22** | Key Maker ↔ Chip | ES8+ (profile delivery) |
| **SCP80** | Operator ↔ Profile | ES6 (profile management) |
| **SCP81** | Operator ↔ Profile (HTTP) | ES6 (web-based management) |

Each channel uses its own encryption keys, ensuring that breaking into one channel doesn't compromise the others.

---

## Separate Locked Rooms: Security Domain Isolation 🏠

The chip keeps everything in strictly separated compartments:

### ISD-R (The Vault Manager's Office)
- Creates and deletes profile rooms (ISD-Ps)
- Controls profile states: Installed → Selectable → Enabled → Disabled
- Enforces profile policy rules

### ECASD (The Secret Keeper's Safe)
- Holds the chip's private key (never leaves this room!)
- Stores the eSIM CA public key (the ultimate trust anchor)
- Generates signatures and verifies certificates
- Access is the **most restricted** on the entire chip

### ISD-Ps (Individual Safe Deposit Boxes)
- Each holds exactly **one** operator profile
- Profile #1 cannot see or touch Profile #2
- Deleting a profile removes its entire ISD-P room

The access control rules (FDP_ACC.1, FDP_ACF.1) enforce that ISD-R can manage ISD-Ps, ECASD keeps its secrets private, and profiles stay isolated.

---

## Who Holds the Keys? Security Management 🔑

Not everyone can change security settings. SGP.25 defines specific rules:

| Management Area | Who Can Change It |
|----------------|-------------------|
| **Profile Policy Rules** | Operator who owns the profile |
| **Rules Authorisation Table** | Only during manufacturing or initial setup |
| **eSIM CA keys and CRLs** | eUICC Manufacturer (EUM) |
| **ISD-P State** | ISD-R, under strict rules |
| **Profile creation/deletion** | ISD-R, authorised by authenticated operators |

The RAT (Rules Authorisation Table) is especially important: it's set once at manufacturing and can never be changed. It defines what operations are forever forbidden on each profile. Think of it as the vault's constitution: the rules that even the vault manager can't override.

---

## Failure Must Be Safe 🛑

What happens when things go wrong? The chip must fail **securely**:

- **FPT_FLS.1** : If an operation fails, the chip returns to a secure state. No half-installed profiles, no partially deleted keys.
- **FDP_SDI.1** : The chip constantly monitors its own data integrity. If something looks corrupted, it raises the alarm.
- **FDP_RIP.1** : When data is deleted, it's *really* deleted. No leftover scraps of secret keys in freed memory.
- **FCS_RNG.1** : All random numbers used for keys and challenges must come from a properly certified random number generator. No shortcuts!

---

## What's NOT Covered (And Why) 🚫

SGP.25 is specific about its boundaries:

| Not Covered | Why |
|-------------|-----|
| **Operator profiles themselves** | They're user data, controlled by the operator |
| **The Runtime Environment (e.g., Java Card)** | Has its own separate certification |
| **The physical chip hardware** | Certified under its own Protection Profile (PP0084) |
| **The phone's eSIM assistant (LPA)** | It's on the device side, not in the chip |

This clean separation means each layer is independently certified and trusted. The eUICC software doesn't have to re-prove what the hardware already guarantees.

---

The TOE (Target of Evaluation: what's actually tested) for SGP.25 includes the ISD-R, ECASD, ISD-Ps, and Platform Layer, but explicitly **excludes** the MNO-SD, profiles, and runtime environment. It's like inspecting the vault's security system without inspecting what customers put in their safe deposit boxes!

---

*Kid-friendly version of GSMA SGP.25 v2.1: Security Functional Requirements*

← [Back to Kids Articles](index)
