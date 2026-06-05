---
title: "Inside the eUICC: The Secure Element That Powers Your eSIM"
date: 2026-05-27
---

# Inside the eUICC: The Secure Element That Powers Your eSIM

> **💡 Why this matters:** The eUICC is the hardware root of trust for every eSIM. Its internal architecture — ECASD, ISD-R, ISD-Ps, and Profile Policy Enabler — determines what's possible and what's impossible in the eSIM security model.

> **Key takeaways:**
> - The eUICC is a Java Card secure element, not just storage — it actively verifies certificates, enforces policies, and interprets profile packages
> - The **ECASD** is the factory-installed root of trust — permanent, immutable, and containing the chip's unique identity
> - **ISD-Ps** provide GlobalPlatform-level isolation — no profile can ever access another's keys or data
> - The **Profile Policy Enabler** enforces rules like "disabling not allowed" that even the end user cannot override
> - All cryptography uses NIST P-256 ECDSA with 128-bit security strength

---

The eUICC (embedded Universal Integrated Circuit Card) is not just a storage chip — it's a fully-fledged secure computing platform that runs a Java Card operating system inside a tamper-resistant package. Understanding its internal architecture reveals how profiles remain cryptographically isolated, how the root of trust is established at the factory, and why no profile can ever access another's keys.

---

## The High-Level Architecture

At the top level, the eUICC consists of an operating system, a telecom framework, and several security domains and services:

<img src="../diagrams/02-euicc-internals.svg" alt="eUICC internal architecture: ECASD, ISD-R, ISD-Ps, Telecom Framework, Profile Policy Enabler, Profile Package Interpreter, and LPA Services" style="width:100%;max-width:800px;display:block;margin:20px auto;border-radius:8px;">

---

## ECASD — The Root of Trust

The **Embedded UICC Controlling Authority Security Domain** is the single most critical component on the chip. It is:

- **Installed by the EUM during manufacturing** — never modified after the factory
- **One per eUICC** — there is exactly one ECASD, and it cannot be deleted
- **In PERMANENT lifecycle state** — it can never transition out of this state after manufacturing

The ECASD securely stores:

| Contents | Purpose |
|----------|---------|
| `SK.EUICC.ECDSA` | The eUICC's private key for ECDSA signatures — proves "I am this specific chip" |
| `CERT.EUICC.ECDSA` | The eUICC's certificate containing its public key, signed by the EUM |
| `PK.CI.ECDSA` | The GSMA Certificate Issuer's public keys — used to verify SM-DP+, SM-DS, and EUM certificates |
| `CERT.EUM.ECDSA` | The EUM's own certificate, signed by the CI — proves the chip is genuinely manufactured |
| **CI key metadata** | Certificate serial numbers, CI identifiers, Subject Key Identifiers for CRL management |

The ECASD provides two services to the `ISD-R`:

1. **Signature creation** — signs material on behalf of the eUICC using `SK.EUICC.ECDSA`
2. **Certificate verification** — validates off-card entity certificates (SM-DP+, SM-DS) against the CI's public key

The ECASD is personalised in a certified **GSMA SAS-UP** (Secure Accreditation Scheme — UICC Production) environment — one of the most secure manufacturing processes in the telecom industry.

The security strength is ECC256 (128-bit security strength), which NIST SP 800-57 considers sufficient beyond 2031.

---

## ISD-R — The Profile Manager

The **Issuer Security Domain — Root** is the operational heart of the eUICC:

- **One per eUICC** — exactly one, installed during manufacturing
- **Creates ISD-Ps** — every profile container is created by the `ISD-R`
- **Cannot be deleted or disabled** — it's permanent
- **Holds GlobalPlatform privileges** as defined in the specification's Annex A

The `ISD-R` is the only entity on the chip that can:

- Create new ISD-Ps for profile installation
- Manage the lifecycle of all ISD-Ps
- Access Profile Metadata across profiles (but never profile contents)
- Enforce Profile Policy Rules

---

## ISD-P — The Profile Container

Each **Issuer Security Domain — Profile** hosts exactly one Profile. It's created by the `ISD-R` during profile installation and destroyed when the profile is deleted.

**Isolation guarantee:** An ISD-P cannot see any other ISD-P. No component outside an ISD-P can see inside it — the `ISD-R` can access Profile Metadata but not Profile Components (NAAs, applets, file system, keys).

This isolation is implemented through GlobalPlatform security domains — the same mechanism used in banking SIMs to keep payment applications separate from network authentication.

---

## What's Inside a Profile

A Profile is a complete operator subscription, containing:

| Component | Description |
|-----------|-------------|
| **MNO-SD** | Operator's on-card representative with OTA keys for remote management |
| **NAAs** | Network Access Applications — USIM, ISIM, or CSIM that authenticate to the network |
| **File System** | Phonebook, SMS storage, network parameters (EFs like ICCID, IMSI, LOCI) |
| **SSDs and CASD** | Supplementary Security Domains and Controlling Authority Security Domains for payment/NFC apps |
| **Applets** | Java Card applications for NFC, secure element services |
| **Profile Metadata** | ICCID, profile name, operator name, profile class, policy rules |

When a Profile is **Enabled**, the eUICC behaves exactly like a physical UICC — the NAAs and file system are selectable by the device's modem. When **Disabled**, the file system cannot be selected, applications cannot be triggered, and OTA management via `ES6` is blocked.

---

## The Telecom Framework

The **Telecom Framework** provides the standardised interface between the Profiles and the device's baseband processor. It handles:

- Proactive commands (`REFRESH`, `SET UP MENU`, etc.)
- File selection and access arbitration
- Logical channel management
- Event handling (call control, MO-SMS control)

When a Profile switch occurs, the Telecom Framework ensures the baseband transparently sees the newly enabled Profile's NAAs and file system without needing to power-cycle the device.

---

## Profile Policy Enabler (PPE)

The **PPE** enforces **Profile Policy Rules** — constraints defined per-profile in the Rules Authorisation Table (RAT). Examples:

- `ppr1` — "Disabling not allowed" (corporate-managed devices)
- `ppr2` — "Deletion not allowed"
- `ppr3` — "Delete after disable" (auto-cleanup)

The PPE ensures these rules cannot be circumvented by the LPA or the end user.

---

## Profile Package Interpreter

During profile installation, the SM-DP+ sends a **Bound Profile Package** — a structured sequence of TLV commands. The Profile Package Interpreter decodes each element:

1. `InitialiseSecureChannel` — key agreement for session keys
2. `ConfigureISDP` — create the ISD-P and configure it
3. `StoreMetadata` — write profile metadata (ICCID, name, rules)
4. `ReplaceSessionKeys` — swap in profile-specific protection keys
5. **Profile Elements** — file system, NAAs, applets, keys (streamed as SCP03t segments)

Each element is verified, decrypted, and installed. If any element fails, the installation is rolled back with a specific error code — the spec defines 14 distinct failure reasons.

---

## Hardware and Platform Requirements

The eUICC must implement **Java Card 3.0.4 Classic Edition** (or higher) with specific extension packages for memory access, TLV parsing, HCI protocol support, and GlobalPlatform contactless services. The hardware must provide sufficient non-volatile memory for multiple Profiles, and the cryptographic operations must use hardware acceleration where available to meet performance requirements for ECDSA signatures and key agreement.

---

## 📋 Summary

- The eUICC is a tamper-resistant secure computing platform with a permanent root of trust (ECASD) burned in at the factory
- `ISD-R` manages all profile containers; ISD-Ps provide hardware-enforced isolation between operator profiles
- A full Profile includes NAAs, a file system, applets, and OTA keys — it's a complete virtual SIM
- The Profile Policy Enabler and Profile Package Interpreter enforce rules and process encrypted profile payloads, ensuring secure multi-profile operation
- All crypto is hardware-backed ECDSA on NIST P-256 with 128-bit security strength

---

*Based on GSMA SGP.22 v2.2.2, Section 2.4 — eUICC Architecture*
