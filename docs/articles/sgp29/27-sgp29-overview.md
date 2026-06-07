---
title: "SGP.29 Overview: The eUICC Identifier (EID)"
description: "Explains GSMA SGP.29's definition of the eUICC Identifier (EID): a 32-digit globally unique numbering system for eSIM chips, replacing ICCID-based identifiers with a cryptographically verifiable format."
date: 2026-06-05
---

# SGP.29 Overview: The eUICC Identifier (EID)

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.29 EID]({{ site.baseurl }}/docs/articles/sgp29/) > SGP.29 Overview: The eUICC Identifier (EID)**

> **💡 Why this matters:** Every eSIM chip on the planet needs a globally unique identifier: the EID. Without a standardised numbering scheme, eUICC manufacturers would face a fragmented landscape of incompatible national numbering authorities, each with different rules for issuing identifiers. SGP.29 establishes the GSMA as the central authority for EID assignment, replacing the ad-hoc use of ICCID-based identifiers with a purpose-built, cryptographically verifiable 32-digit numbering system designed specifically for the eSIM ecosystem.

> **Key takeaways:**
> - The EID (eUICC Identifier) is a 32-digit globally unique serial number that identifies each individual eUICC chip
> - SGP.29 v1.1 (March 2024) defines the EID format, principles, and assignment process under GSMA administration
> - Before SGP.29, EIDs were issued through ITU-T E.118 (ICCID scheme) by different National Regulatory Authorities with inconsistent rules
> - In 2019, industry stakeholders asked the GSMA to assume responsibility for EID administration
> - The EID is explicitly NOT a Primary Account Number: it cannot be used for charging, service subscriptions, or subscriber identification
> - GSMA serves as the First Level EIN Assignment Authority, issuing ERHI1 (EID Range Holder Identifier Level 1) to manufacturers, device makers, and national authorities

SGP.29 is a concise but foundational specification in the GSMA eSIM ecosystem. At only 13 pages (plus annexes), it establishes the definitive rules for what an EID is, how it is structured, who may assign it, and how manufacturers obtain their allocations. While SGP.22 defines the protocol and SGP.25 defines security certification, SGP.29 defines the identity layer: without which no eUICC could participate in the RSP ecosystem at all.

---

## Why EID Needed Its Own Standard

### The Pre-SGP.29 Landscape

The original EID format was inherited from the Integrated Circuit Card Identifier (ICCID) format, defined by ITU-T Recommendation E.118 as a Primary Account Number (PAN). Within the ICCID, the Issuer Identifier Number (IIN) is typically administered by national authorities. This created three fundamental problems:

1. **The EID is not a PAN** : Its primary purpose is chip identification, not charging for services. Forcing it into the PAN framework was a category error.

2. **Fragmented administration** : Different National Regulatory Authorities issued IINs/ICCIDs for use as EIDs using different rules, creating inconsistent operating conditions for manufacturers. Some manufacturers could not obtain EIDs at all.

3. **No central governance** : Without a single authority, there was no guarantee of global uniqueness, no coherent assignment policy, and no lifecycle management for identifiers.

### The 2019 Consensus

In 2019, the GSMA was formally asked by industry stakeholders to assume responsibility for the administration of the EID. SGP.29 v1.0 was published on 31 July 2020 as the first release of this new governance framework. Version 1.1 followed on 22 March 2024, adding the ability for Device Manufacturers and Groups of Device Manufacturers to obtain ERHI1 values directly from the GSMA.

---

## What SGP.29 Specifies

SGP.29 covers three core areas:

```
┌─────────────────────────────────────────────────────────────┐
│                       SGP.29 Scope                          │
├─────────────────────────────────────────────────────────────┤
│  1. EID Principles & Requirements                           │
│     └─ What the EID is (and isn't), who must follow rules   │
│                                                             │
│  2. EID Format                                              │
│     └─ 32-digit structure, EIN/ESIN/Check Digits            │
│                                                             │
│  3. EID Assignment Process                                  │
│     └─ How ERHI1s are assigned, verified, and cancelled     │
└─────────────────────────────────────────────────────────────┘
```

---

## The EID in the RSP Ecosystem

The EID is not just a label: it is an operational identifier used throughout the Remote SIM Provisioning workflow:

| Protocol | EID Role |
|----------|----------|
| **SM-DS (Discovery Service)** | EID is used to match pending profiles to specific eUICCs |
| **ES11 (SM-DS polling)** | The LPA queries the SM-DS using the EID to discover available profiles |
| **ES8+ (Profile download)** | SM-DP+ uses the EID to bind a profile to the correct eUICC |
| **Event Registration** | EID registers eUICCs for specific event notifications |
| **eUICC Authentication** | EID participates in the cryptographic mutual authentication between SM-DP+ and eUICC |

Without a globally unique, verifiable EID, none of these operations could function reliably.

---

## Key Principles (EID.P01–P06)

SGP.29 establishes six foundational principles:

| Principle | Rule |
|-----------|------|
| **EID.P01** | Existing ICCID issuance by national authorities is not affected |
| **EID.P02** | Central purpose: uniquely identify an individual eUICC (independent of form factor: discrete or integrated) |
| **EID.P03** | The EID is NOT a Primary Account Number (PAN) |
| **EID.P04** | The EID is NOT intended for charging telecommunication services |
| **EID.P05** | EID assignment is separate from ICCID and IIN assignment |
| **EID.P06** | The EID is not required to maintain compatibility with ISO/IEC 7812-1 (no requirement for first digits to be "89") |

> **Note on EID.P02:** Uniqueness is required for cryptographic mutual authentication and eUICC security mechanisms. Two eUICCs with the same EID would break the entire trust model.

---

## GSMA as First Level Authority

SGP.29 establishes the GSMA as the sole First Level EIN Assignment Authority. The GSMA:

- Assigns ERHI1 (EID Range Holder Identifier Level 1) values to eligible entities
- Maintains a registry of all assigned ERHI1s and their status
- Ensures integrity of the assignment process through yearly reviews
- Provides expertise and advice on EID issues
- Ensures cancelled ERHI1s are never reassigned

However, it is important to note: **EIDs assigned under the ITU-T E.118 based scheme remain valid** in the eSIM ecosystem. SGP.29 does not invalidate legacy identifiers: it creates a parallel, purpose-built scheme going forward.

---

## 📋 Summary

- SGP.29 solves the fragmented EID landscape by establishing the GSMA as the central EID assignment authority
- The EID is a 32-digit globally unique identifier for eUICCs: not a charging number, not a subscriber identifier
- Six principles govern the EID, emphasising uniqueness, independence from ICCID, and separation from payment systems
- The EID is operational throughout the RSP ecosystem: discovery, profile matching, download, and event registration
- SGP.29 v1.1 extends ERHI1 eligibility to Device Manufacturers and Groups of Device Manufacturers

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

Next: [EID Format Decoded: The 32-Digit Structure]({{ site.baseurl }}/docs/articles/sgp29/28-sgp29-eid-format) →

</div>

---

*Based on GSMA SGP.29 v1.1 (22 March 2024) : EID Definition and Assignment Process, Sections 1–7*


---

[Section Index](index) | Next: [EID Format Decoded: The 32-Digit Structure](28-sgp29-eid-format) →


---

[Section Index](index) | Next: [EID Format Decoded: The 32-Digit Structure](28-sgp29-eid-format) →
