---
title: "EID Security: Privacy, Tracking, and GSMA Governance"
description: "Examines SGP.29's EID privacy and governance controls: separation from subscriber identity, GSMA registry enforcement against fraudulent ERHI1 acquisition, non-reassignment of cancelled ranges, and modulo-97 check digit verification."
date: 2026-06-05
---

# EID Security: Privacy, Tracking, and GSMA Governance

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.29 EID]({{ site.baseurl }}/docs/articles/sgp29/) > EID Security: Privacy, Tracking, and GSMA Governance**

> **💡 Why this matters:** The EID is a permanent, globally unique identifier burned into every eSIM chip. If misused, it could become a surveillance mechanism: allowing third parties to track devices across networks, correlate eSIM activity with physical locations, or impersonate legitimate eUICCs. SGP.29 establishes governance and privacy controls designed to prevent these outcomes, while the GSMA's central registry and verification processes form the enforcement backbone.

> **Key takeaways:**
> - The EID is a permanent identifier: it survives profile changes, factory resets, and device transfers: making privacy controls essential
> - SGP.29 explicitly separates the EID from subscriber identity: EID identifies the chip, not the person or the subscription
> - The EID is NOT a Primary Account Number and cannot be used for charging: limiting its value for financial fraud
> - GSMA's central registry and verification process (≤5 day authentication of applicants) prevents fraudulent ERHI1 acquisition
> - Cancelled ERHI1s are never reassigned, preventing EID recycling attacks
> - EIDs starting with "89" are reserved for ITU-T E.118 scheme, preventing collision with legacy identifiers
> - EID lifecycle management follows formal processes: assignment, usage, cancellation, and non-reuse
> - The modulo-97 check digit scheme provides cryptographic-strength error detection: a single-digit error or transposition will always be detected

The EID's security model isn't about encryption or access control (that's SGP.22 and SGP.25's domain). It's about identity governance: ensuring that EIDs are issued only to legitimate entities, that they remain globally unique, that they can be verified, and that their lifecycle is managed to prevent abuse.

---

## The Privacy Architecture of the EID

### What the EID Reveals: and What It Doesn't

```
┌─────────────────────────────────────────────────────────────────┐
│                     EID Privacy Boundaries                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   EID DOES reveal:                    EID does NOT reveal:      │
│   ┌──────────────────────┐            ┌──────────────────────┐  │
│   │ • eUICC manufacturer │            │ • Subscriber identity │  │
│   │ • Chip generation    │            │ • Phone number        │  │
│   │ • Manufacturing batch│            │ • Network operator    │  │
│   │ • ERHI delegation    │            │ • Current location    │  │
│   │   chain              │            │ • Active profiles     │  │
│   └──────────────────────┘            │ • Device model        │  │
│                                       │ • End user identity   │  │
│                                       └──────────────────────┘  │
│                                                                  │
│   EID.P03: "The EID is not a Primary Account Number (PAN)."     │
│   EID.P04: "The EID is not intended to be used to charge for    │
│             telecommunication services."                         │
└─────────────────────────────────────────────────────────────────┘
```

**Principle EID.P03** and **EID.P04** are the core privacy protections. By explicitly declaring that the EID is not a PAN and cannot be used for charging, SGP.29 prevents the identifier from being co-opted as a subscriber tracking mechanism within billing and financial systems.

### Tracking Risk Assessment

Despite these protections, the EID's permanence creates inherent tracking risks:

| Risk | Severity | Mitigation |
|------|----------|------------|
| **Cross-profile correlation** | Medium | EID is needed for protocol operations; GSMA governance limits who can query SM-DS |
| **Supply chain surveillance** | Low | ERHI chain reveals manufacturer, not end user |
| **Device fingerprinting** | Low | EID does not identify the device model or OS |
| **Location tracking via SM-DS polling** | Medium | SM-DS access requires authentication; EID alone is insufficient |
| **Impersonation** | High | Prevented by cryptographic authentication (SGP.22) : the EID is an identity claim, not an authenticator |

> **Key point:** The EID is a *claim* of identity, not *proof* of identity. Proof is provided by the eUICC's private key and certificate chain, verified through cryptographic challenge-response. An attacker who knows an EID cannot impersonate the eUICC without also possessing its private key.

---

## GSMA Governance Controls

### 1. Centralised Assignment Authority

By establishing the GSMA as the sole First Level EIN Assignment Authority, SGP.29 eliminates the fragmented and inconsistent assignment landscape that existed under ITU-T E.118. Every ERHI1 traces back to a single, auditable source.

### 2. Applicant Verification (≤5 Days)

Before any ERHI1 is assigned, the GSMA verifies:

- The **authenticity** of the applicant company (is it a real, registered entity?)
- The **validity** of the application (does the applicant meet all criteria?)

If verification fails due to suspected fraud, the GSMA may take further actions: including reporting to relevant authorities if the attempt targeted a legitimate ERHI1 owner.

### 3. Central Registry

The GSMA maintains a list of all assigned ERHI1s and their status. This is the authoritative source of truth for the EID numbering system. The registry enables:

- **Uniqueness enforcement** : No duplicate ERHI1 assignments
- **Lifecycle tracking** : Status of each ERHI1 (active, cancelled)
- **Yearly auditing** : GSMA reviews actual assignments and usage
- **Collision prevention** : Ensures new assignments don't conflict with existing ones

### 4. Yearly Integrity Review

```
┌─────────────────────────────────────────────────────────────────┐
│               GSMA Yearly Integrity Review Cycle                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Collect:    Gather assignment data from all Subsequent        │
│               Level EAAs (usage reports, sub-delegations)       │
│                    │                                             │
│                    ▼                                             │
│   Analyse:    Compare actual usage against assigned ranges      │
│               Identify any anomalies or policy violations       │
│                    │                                             │
│                    ▼                                             │
│   Report:     Present findings to the GSMA group responsible    │
│               for SGP.29 (eSIMG / ISAG)                         │
│                    │                                             │
│                    ▼                                             │
│   Act:        Take corrective action if needed                  │
│               (e.g., address underutilised ranges,               │
│                investigate violations)                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## EID Lifecycle Management

SGP.29 defines a complete lifecycle for EIDs and their ranges:

```
 ┌──────────┐    ┌──────────┐    ┌──────────────┐    ┌──────────┐
 │ASSIGNMENT│───▶│  ACTIVE  │───▶│ CANCELLATION │───▶│ EXPIRED  │
 │          │    │   USE    │    │   REQUEST    │    │(archived)│
 └──────────┘    └──────────┘    └──────────────┘    └──────────┘
      │               │                │                   │
      │               │                │                   │
  GSMA verifies   EUM assigns     Holder submits      Never reassigned
  ≤5 days         ESINs to        cancellation        to any other
  authenticity    individual       form                 entity
                  chips
                                  │
                                  ▼
                           GSMA verifies
                           ≤5 days, then
                           cancels ERHI1
```

### Cancellation Safeguards

The cancellation process includes specific safeguards:

- **Only the verified holder** can request cancellation: preventing hostile third-party cancellation
- **Cancelled ERHI1s are never reassigned** : preventing EID recycling attacks where a cancelled identifier is issued to a different entity
- **Post-cancellation use is prohibited** : "Once an ERHIx has been cancelled, it SHALL NOT be used after the date indicated in the Cancellation Form"
- **Cancellation requires the same verification rigour** as assignment: preventing fraudulent cancellation requests

---

## Collision Prevention: The "89" Reservation

SGP.29 Requirement **AE.R02** states: "The EID assignment defined in this document SHALL not use EIDs that start with 89; such values are reserved for the ITU-T E.118 based scheme."

This is a critical security requirement:

```
┌─────────────────────────────────────────────────────────────────┐
│                    EID Numbering Namespace                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  89XXXXXXXX...          ┌──────────────────┐                    │
│  (ITU-T E.118 legacy)   │ Reserved for      │                   │
│                         │ ICCID-based EIDs  │                   │
│                         └──────────────────┘                    │
│                                                                  │
│  00-88XXXXXXXX...        ┌──────────────────┐                    │
│  90-99XXXXXXXX...        │ GSMA SGP.29      │                   │
│                         │ assigned EIDs     │                   │
│                         └──────────────────┘                    │
│                                                                  │
│  Both schemes coexist. No collision is possible because         │
│  the "89" prefix acts as an unambiguous namespace separator.     │
└─────────────────────────────────────────────────────────────────┘
```

This ensures that GSMA-assigned EIDs and legacy ICCID-based EIDs can coexist without ambiguity: an eUICC manufactured under one scheme will never collide with one manufactured under the other.

---

## Check Digit Security

The modulo-97 check digit scheme (ISO/IEC 7064 MOD 97-10) provides strong error detection:

| Error Type | Detection Rate |
|------------|---------------|
| Single digit error | 100% (guaranteed) |
| Single transposition (e.g., 12 → 21) | 100% (guaranteed) |
| Twin errors (e.g., 11 → 22) | 100% (guaranteed) |
| Other errors | ~99.0% |

This is significantly stronger than the Luhn MOD 10 algorithm (used for credit card numbers and ICCIDs), which cannot detect all single transpositions. MOD 97-10 is the same algorithm used for IBANs: a deliberate choice to provide banking-grade validation for eSIM identity.

---

## 📋 Summary

- The EID is a permanent identifier: privacy controls are architectural, not optional
- EID.P03 and EID.P04 explicitly separate the EID from subscriber identity and charging: limiting tracking and financial fraud
- GSMA governance includes applicant verification (≤5 days), a central registry, yearly integrity reviews, and anti-fraud escalation
- EID lifecycle management ensures cancelled identifiers are never reused, preventing recycling attacks
- The "89" prefix reservation prevents collision between GSMA-assigned and legacy ITU-T EIDs
- MOD 97-10 check digits provide 100% detection of single-digit errors and transpositions
- The EID is a claim of identity, not proof: cryptographic authentication (SGP.22) prevents EID-based impersonation

---

<div align="center">

← Previous: [EID in RSP Protocols: Discovery, Matching, and Events]({{ site.baseurl }}/docs/articles/sgp29/30-sgp29-in-protocols) · [🏠 Home]({{ site.baseurl }}/)

</div>

---

*Based on GSMA SGP.29 v1.1 (22 March 2024) : EID Definition and Assignment Process, Sections 7 (EID Principles), 8 (EID Scheme Requirements), 9 (Assignment Authority Requirements), 12–14 (Assignment Process and GSMA Responsibilities), and Annex A*


---

← Previous: [EID in RSP Protocols: Discovery, Matching, and Events](30-sgp29-in-protocols) | [Section Index](index)
