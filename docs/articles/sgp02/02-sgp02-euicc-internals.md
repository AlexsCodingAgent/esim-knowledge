---
title: "Inside the M2M eUICC: ISD-R, ISD-P, ECASD, and EID"
description: "Walks through the M2M eUICC's internal security domain architecture — ISD-R for platform management, ISD-P containers for operator profiles, the ECASD as hardware root of trust, and the EID as unique chip identity."
date: 2026-06-07
---

# Inside the M2M eUICC: ISD-R, ISD-P, ECASD, and EID

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > Inside the M2M eUICC: ISD-R, ISD-P, ECASD, and EID**

Imagine you're two competing mobile operators. Your profiles are both sitting on the same physical chip inside a smart meter in rural Germany. How do you know (really know, in the cryptographic sense) that the other guy can't see your keys? Your IMSI? Your OTA channel?

SGP.02 answers this with hardware-enforced isolation. Not software. Not policy. The chip itself guarantees that one profile can't touch another.

This is what the eUICC's security domain architecture does. It's built on GlobalPlatform's card specification (SGP.02 §2.2), and it partitions the chip into three types of Security Domain. Each has its own keys, its own lifecycle, its own privileges. They can talk to each other through strictly controlled interfaces. They can't cross boundaries without the chip saying no.

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

Three domain types. One chip. Multiple stakeholders (manufacturer, CI, SM-SR, operators) each with their own locked room.

## ECASD: the birth certificate you can't change

Every eUICC has exactly one ECASD (eUICC Controlling Authority Security Domain). The EUM creates it during manufacturing. After that, it's frozen: no key updates, no lifecycle transitions beyond PERSONALIZED. It's the chip's cryptographic identity, and four things live inside it (§2.2.1.2):

**`PK.CI.ECDSA`** : the CI's public key. This is the trust anchor. Every certificate verification on the chip starts here. If someone swapped this key, they could make the chip trust a fake SM-DP. They can't, because the ECASD is immutable.

**`SK.ECASD.ECKA`** : the eUICC's private key. This one *never leaves the chip*. It's used during Scenario#3 key establishment: the chip and the SM-DP each generate an ephemeral key pair, exchange the public halves, and compute a shared secret (`ShS`) from which session keys are derived.

**`CERT.ECASD.ECKA`** : the chip's certificate, signed by the EUM. It contains the corresponding public key, the EID, and a reference to the chip's Common Criteria security certification. This is what the SM-DP checks during mutual authentication.

**`EID`** : the 32-digit identifier, retrievable at any time with a GlobalPlatform `GET DATA` command.

The ECASD only wakes up for two operations: SM-DP key establishment during profile download (§3.1.2) and SM-SR key establishment during an SM-SR change (§3.8). That's it. It's a vault that opens twice in the chip's lifetime.

No profile component can access the ECASD directly. Only the ISD-R and ISD-Ps can call its services.

## ISD-R: the SM-SR's man on the inside

There's exactly one ISD-R (Issuer Security Domain (Root) per chip, and it's the on-card representative of the SM-SR. The EUM installs it during manufacturing and it enters the PERSONALIZED state immediately) no locked state, no transitional phase.

The ISD-R is the gatekeeper. When the SM-SR wants something done on the chip, the ISD-R is the one that does it:

- **Creates ISD-Ps** : the `ES5.CreateISDP` command makes a new empty profile container
- **Enables and disables profiles** : switches which profile's NAA is selectable over the UICC-Terminal interface, automatically deactivating the previous one
- **Deletes ISD-Ps** : permanently wipes a profile and its container (including Master Delete)
- **Manages Fall-Back** : sets which profile activates automatically if the current one loses connectivity
- **Relays ES8 traffic** : forwards encrypted SCP03/SCT03t commands between the SM-SR and the target ISD-P
- **Enforces POL1** : checks profile policy rules before letting lifecycle operations through

The ISD-R holds the SCP80 (and optionally SCP81) key sets that secure the ES5 channel with the SM-SR. These protect platform management commands over SMS, HTTPS, or CAT_TP.

Under GlobalPlatform rules (Annex C), the ISD-R has **Authorized Management** privilege over every ISD-P. That lets it verify command tokens (proving an operation came from an authorized source) and control ISD-P lifecycle. But it *can't read profile contents* beyond POL1 and Connectivity Parameters. It's the building superintendent, not the tenant, it has the master key to the hallway, not to your apartment.

## ISD-P, one profile, one container, no peeking

An ISD-P (Issuer Security Domain, Profile) holds exactly one Profile. A chip can have many ISD-Ps, but only one is in the ENABLED state at any time.

### The life of an ISD-P

An ISD-P follows a strict lifecycle (SGP.02 §2.2.1.3, Figure 3):

```
  [Created via ES5.CreateISDP]
            │
            ▼
       SELECTABLE ◄── exists but empty
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
        [Deleted, ISD-P removed from eUICC]
```

A few things about this lifecycle that matter:

The INSTALLED state from GlobalPlatform is skipped, `ES5.CreateISDP` jumps straight to SELECTABLE. The LOCKED state isn't supported at all. After profile download finishes, the ISD-P goes to DISABLED, not enabled: the operator has to explicitly enable it. Enabling a new profile automatically disables whatever was enabled before. And the Fall-Back Mechanism can trigger enable/disable transitions on its own, without any server command.

All Profile Components created inside an ISD-P stay permanently affiliated with it. You can't move a component between ISD-Ps. When an ISD-P gets deleted, everything inside it goes with it, clean removal, no orphans.

ISD-P privileges (Annex C) let it create applications (NAAs, applets), spin up supplementary security domains (like the MNO-SD), and manage its own file system, but only within its own container walls.

## What's inside a profile

A Profile inside an ISD-P is a complete operator subscription. Here's what's in the box (§2.2.4):

**MNO-SD** : the operator's on-card representative. Holds SCP80/SCP81 keys for the ES6 OTA channel. After installation, the operator uses this to manage the profile directly, bypassing the SM-DP and SM-SR.

**NAAs** : Network Access Applications: USIM (3G/4G/5G), ISIM (IMS/VoLTE), or CSIM (CDMA). These hold the IMSI, authentication keys, and network parameters.

**File System** : standard UICC files: phonebook, SMS storage, network parameters, service tables. The ISD-R gets read access to Connectivity Parameters (SMSC address, DNS config) but nothing else.

**Applets and Supplementary Security Domains** : payment apps, NFC secure elements, proprietary operator code. All sandboxed inside the ISD-P.

**POL1** : Policy Rules stored in the ISD-P's file system. These govern what lifecycle operations are allowed on this specific profile. The ISD-R reads POL1 before saying yes to an enable, disable, or delete.

**POL2** : Policy Rules associated with the profile but stored *in the ISD-R* (outside the ISD-P), for faster access during platform management. When POL1 and POL2 disagree, SGP.02 defines which one wins.

### How tight is the isolation?

Absolute (§2.2.1.3):

- Nothing outside an ISD-P can see or touch any Profile Component inside it (except the ISD-R's limited read of POL1 and Connectivity Parameters)
- Nothing inside an ISD-P can see or reach anything outside it
- No ISD-P can access any other ISD-P
- Two profiles can reuse the same AID or TAR: the ISD-P boundary prevents collisions

When an ISD-P isn't enabled, the eUICC makes its file system unselectable to the Device, blocks its applications, and shuts down ES6 remote management. A disabled profile is invisible to the outside world.

## The EID, 32 digits that identify a chip forever

The eUICC Identifier follows ISO/IEC 7812, the same standard that gives credit cards their numbers. Its structure (§2.2.2):

- **Digit 1**: `8` (Major Industry Identifier, telecommunications)
- **Digit 2**: `9` (telecommunications sub-identifier)
- **Digits 3–5**: Country code (padded with leading zeros)
- **Digits 6–31**: Issuer-specific identifier
- **Digit 32**: Luhn check digit

The EID lives in the ECASD and is retrievable through GlobalPlatform `SELECT` (ECASD AID) followed by `GET DATA` (tag `'5A'`). It's the primary key used everywhere, ES2 profile orders, ES3 EIS lookups, ES4 lifecycle operations, ES7 handovers.

The leading `89` is distinctive. If you see a 32-digit number starting with `89`, you're looking at an eUICC.

## How the chip talks to the outside world

Three secure channels, three different protocol pairs (SGP.02 §2.2.5):

| Interface | Path | Protocol | What it protects |
|-----------|------|----------|------------------|
| ES5 | SM-SR ↔ ISD-R | SCP80 (or SCP81) | Platform management: auth, integrity, confidentiality |
| ES6 | Operator ↔ MNO-SD | SCP80 (or SCP81) | Post-install profile management |
| ES8 | SM-DP ↔ ISD-P | SCP03 / SCP03t | Profile download: AES-128 CBC, C-MAC, R-MAC, R-ENCRYPTION |

ES8 is the interesting one because it's not a direct connection. SCP03 commands are encrypted, sent to the SM-SR over ES3, then tunneled through the SCP80/SCP81-protected ES5 channel to the ISD-R, which forwards them to the correct ISD-P. The SM-SR carries the bytes but can't decrypt them. Two layers of encryption, two different key sets: the SM-SR is a secure courier, not a reader.

## Java Card and physical form factors

The eUICC *may* support Java Card (§2.2.7). If it does, it needs at least version 3.0.4 of the Java Card Classic Platform, enough to run post-issuance applets inside profiles.

On the hardware side (§2.2.8), it's a Tamper Resistant Element. Physical attacks should fail. It can be a discrete chip (removable in an MFF2 form factor, or soldered down) or integrated into a larger SoC, sharing silicon with the modem or application processor.

---

Three Security Domains. One immutable identity in the ECASD. One platform manager in the ISD-R. As many profile containers as the chip can hold, each cryptographically walled off from the others. Competing operators on the same silicon, unable to see each other's keys. That's the eUICC's architecture, and it's what makes multi-stakeholder remote provisioning possible.

---

<div align="center">

<a href="{{ site.baseurl }}/">🏠 Home</a>

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp02/01-sgp02-architecture">M2M Ecosystem</a> | Next: <a href="{{ site.baseurl }}/docs/articles/sgp02/03-sgp02-pki">M2M Certificate Hierarchy</a> →

</div>

---

*Based on GSMA SGP.02 v4.2 §2.2, eUICC Architecture*


---

← Previous: [M2M Ecosystem: EUM, SM-DP, SM-SR, and the Operator](01-sgp02-architecture) | [Section Index](index) | Next: [M2M Certificate Hierarchy: CI, EUM, SM-DP, SM-SR, and eUICC](03-sgp02-pki) →
