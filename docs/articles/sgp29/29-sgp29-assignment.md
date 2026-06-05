---
title: "EID Assignment: How Manufacturers Get Their Allocations"
date: 2026-06-05
---

# EID Assignment: How Manufacturers Get Their Allocations

**🏠 [eUICC.tech](/) > [SGP.29 EID](/docs/articles/sgp29/) > EID Assignment: How Manufacturers Get Their Allocations**

> **💡 Why this matters:** Behind every eSIM chip's EID is a formal assignment process that verifies the legitimacy of the requesting entity, prevents fraud, and ensures global uniqueness. Without this governance, bad actors could obtain EID ranges and manufacture counterfeit eUICCs — undermining the entire RSP trust model. Understanding the ERHI1 assignment flow reveals the administrative machinery that keeps the eSIM numbering system secure.

> **Key takeaways:**
> - ERHI1 assignment is a 5-stage process: Form Filling → Submission → Verification (≤5 days) → Assignment → Confirmation
> - Applicants must be EUMs, Device Manufacturers, or Groups of Device Manufacturers — single corporate entities under specific legislative regulation
> - The GSMA DAG (EIN Assignment Services) handles all ERHI1 applications via EISRegistration@gsma.com
> - Eligibility criteria include: must not already hold an ERHI1 (with limited justified exceptions) and must commit to use within 12 months
> - A parallel cancellation process exists for ERHI1s that are no longer needed, with identical verification rigour
> - Subsequent Level EAAs (Level ≥2) have their own responsibilities under SGP.29, including complying with all EID requirements and reporting to their parent EAA

The ERHI1 assignment process is the gatekeeper of the eSIM numbering system. Every EID in existence traces back to an ERHI1 issued by the GSMA — making this process the foundation of eUICC identity governance.

---

## Who Can Apply?

SGP.29 v1.1 defines four categories of eligible applicants for ERHI1:

### 1. eUICC Manufacturers (EUMs)

The most direct path. EUMs who manufacture eUICC chips apply directly to the GSMA for an ERHI1. They then assign ESINs to individual chips under their assigned EIN.

### 2. Device Manufacturers

Added in SGP.29 v1.1 (March 2024, CR11000R06). Device manufacturers — companies that embed eUICCs into consumer devices (phones, tablets, wearables) or IoT equipment — can now obtain ERHI1 values directly. This allows them to manage EID allocation for the eUICCs they integrate without going through an intermediate authority.

### 3. National Authorities

National Regulatory Authorities may apply for ERHI1 values, which they can then sub-delegate to entities within their jurisdiction. This preserves the ability of national administrations to maintain oversight of numbering resources within their territories.

### 4. Groups of Device Manufacturers

Also added in v1.1 (CR11001R02). A collection of Device Manufacturers represented by a single entity can apply as a group, receiving an ERHI1 that they then sub-delegate to individual member companies.

---

## Eligibility Criteria (Section 11)

All applicants must satisfy three mandatory criteria:

```
┌─────────────────────────────────────────────────────────────┐
│                 ERHI1 Eligibility Checklist                  │
├─────────────────────────────────────────────────────────────┤
│  □  Applicant does NOT already hold an ERHI1                │
│     (unless a justified exception applies)                  │
│                                                             │
│  □  Applicant commits to use the ERHI1 within 12 months     │
│     of the release date                                     │
│                                                             │
│  □  Applicant is a single corporate entity operating under  │
│     a specific legislative regulation (non-National         │
│     Authorities only)                                       │
│                                                             │
│  □  Applicant is one of:                                    │
│     • eUICC Manufacturer (EUM), or                         │
│     • Device Manufacturer, or                              │
│     • Group of Device Manufacturers, or                    │
│     • National Authority                                    │
└─────────────────────────────────────────────────────────────┘
```

---

## The 5-Stage Assignment Process (Section 12)

### Stage 1: Form Filling

The applicant downloads and completes the Registration Form from [gsma.com](https://gsma.com). The form captures:

- Company identity and legal registration details
- Type of applicant (EUM / Device Manufacturer / Group / National Authority)
- Contact information for the responsible officer
- Declaration of commitment to SGP.29 requirements

### Stage 2: Submission

The completed and signed Registration Form is sent to **EISRegistration@gsma.com**.

### Stage 3: GSMA Verification Process (≤5 working days)

The GSMA verifies two things:

1. **Authenticity of the applicant company** — Is this a legitimate, registered corporate entity?
2. **Validity of the application** — Does the applicant meet all eligibility criteria?

The entire verification process is estimated to take **no more than 5 working days** after receipt of the correctly completed form.

```
If verification FAILS:
  → GSMA may take further actions depending on the reason
  → Examples: fraud attempt against a legitimate ERHI1 owner
  
If verification SUCCEEDS:
  → Proceed to Stage 4
```

### Stage 4: ERHI1 Assignment

Upon successful verification, the GSMA assigns a unique ERHI1 value to the applicant. The GSMA registers this assignment in its central registry and updates the status of the ERHI1 to "assigned."

### Stage 5: GSMA Confirmation

The GSMA notifies the applicant of the assigned ERHI1 by returning the completed and approved registration form. From this point, the ERHI1 is active and the holder may begin assigning sub-ranges or manufacturing eUICCs with EIDs under their EIN.

---

## Process Diagram

```
 ┌──────────┐     ┌──────────────────────┐
 │ Applicant│     │ GSMA EIN Assignment  │
 │          │     │ Services (DAG)       │
 └────┬─────┘     └──────────┬───────────┘
      │                      │
      │ [1] Fill Registration│
      │     Form             │
      │                      │
      │ [2] Submit Form ────▶│
      │   (EISRegistration    │
      │    @gsma.com)         │
      │                      │
      │              ┌───────┴────────┐
      │              │ [3] Verification│
      │              │   (≤ 5 days)    │
      │              └───────┬────────┘
      │                      │
      │   ◀─── Verification  │
      │        fails (if     │
      │        applicable)   │
      │                      │
      │              ┌───────┴────────┐
      │              │ [4] Assign     │
      │              │   ERHI1        │
      │              └───────┬────────┘
      │                      │
      │ [5] Confirmation ◀───│
      │   (approved form     │
      │    with ERHI1)       │
      │                      │
      ▼                      ▼
```

---

## The Cancellation Process (Section 13)

An ERHI1 that is no longer used may be voluntarily cancelled. The process mirrors the assignment flow:

| Stage | Action |
|-------|--------|
| **1. Form Filling** | Applicant completes the Cancellation Form from gsma.com |
| **2. Submission** | Form submitted to EISRegistration@gsma.com with the ERHI1 to be cancelled |
| **3. Verification** | GSMA verifies authenticity and validity (≤5 working days) |
| **4. Cancellation** | GSMA cancels the ERHI1 — it is marked as cancelled in the registry |
| **5. Confirmation** | GSMA notifies applicant that the ERHI1 has been cancelled |

> **Important:** Once cancelled, an ERHI1 is **never reassigned** to any other entity. And the former holder **SHALL NOT use** any EIDs under that ERHI1 after the cancellation date specified in the Cancellation Form.

---

## GSMA Responsibilities (Section 14)

The GSMA's ongoing responsibilities extend beyond the assignment itself:

| Responsibility | Description |
|---------------|-------------|
| **Register / Cancel ERHI1s** | Process all assignment and cancellation requests |
| **Maintain Registry** | Keep a current list of all assigned ERHI1s and their status |
| **Ensure Integrity** | Yearly review and report to the GSMA group responsible for SGP.29 on actual assignments and usage by Subsequent Level EAAs |
| **Provide Expertise** | Offer advice on EID issues to stakeholders |
| **Prevent Reassignment** | Ensure cancelled ERHI1s are never assigned to another entity |

---

## Subsequent Level EAA Responsibilities (Section 15)

Any Level X EIN Assignment Authority (where X ≥ 2) — e.g., a National Authority that received an ERHI1 and is assigning ERHI2 values — has its own set of responsibilities:

1. **Comply with EID requirements** — Must follow Sections 8 (EID Scheme Requirements), 9 (Assignment Authority Requirements), and 10 (Numbering Scheme)
2. **Complete forms accurately** — Fill in all required information on Registration or Cancellation Forms
3. **Ensure ERHIx uniqueness** — Each sub-delegated ERHI must be unique within the EAA's range
4. **Only the verified company cancels** — A third party cannot request cancellation of another entity's identifier
5. **No reuse after cancellation** — Cancelled ERHIx values must not be used after the cancellation date
6. **Report to parent EAA** — Comply with assignment reporting requirements for the Level X−1 authority that granted their range

---

## 📋 Summary

- ERHI1 assignment is a formal 5-stage process: form → submit → verify (≤5 days) → assign → confirm
- Eligibility is restricted to EUMs, Device Manufacturers, Groups of Device Manufacturers, or National Authorities
- A parallel cancellation process exists for unused ERHI1s, preventing identifier waste
- The GSMA maintains a central registry of all assignments, conducts yearly integrity reviews, and ensures cancelled identifiers are never reused
- Subsequent Level EAAs (Level ≥2) have their own compliance obligations, including reporting to their parent authority
- The entire process is designed to verify legitimacy, prevent fraud, and maintain global EID uniqueness

---

<div align="center">

← Previous: [EID Format Decoded: The 32-Digit Structure](/docs/articles/sgp29/28-sgp29-eid-format) · [🏠 Home](/)

Next: [EID in RSP Protocols: Discovery, Matching, and Events](/docs/articles/sgp29/30-sgp29-in-protocols) →

</div>

---

*Based on GSMA SGP.29 v1.1 (22 March 2024) — EID Definition and Assignment Process, Sections 11–15*
