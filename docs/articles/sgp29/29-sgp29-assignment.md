---
title: "EID Assignment: How Manufacturers Get Their Allocations"
description: "Walks through the 5-stage ERHI1 assignment process where EUMs and device manufacturers obtain EID ranges from GSMA's DAG : covering eligibility, verification, and cancellation procedures."
date: 2026-06-05
---

# EID Assignment: How Manufacturers Get Their Allocations

**[eUICC.tech]({{ site.baseurl }}/) > [SGP.29 EID]({{ site.baseurl }}/docs/articles/sgp29/) > EID Assignment: How Manufacturers Get Their Allocations**

> **Why this matters:** Behind every eSIM chip's EID is a formal assignment process that verifies the legitimacy of the requesting entity, prevents fraud, and ensures global uniqueness. Without this governance, bad actors could obtain EID ranges and manufacture counterfeit eUICCs: undermining the entire RSP trust model. Understanding the ERHI1 assignment flow reveals the administrative machinery that keeps the eSIM numbering system secure.

> **Key takeaways:**
> - ERHI1 assignment is a 5-stage process: Form Filling → Submission → Verification (≤5 days) → Assignment → Confirmation
> - Applicants must be EUMs, Device Manufacturers, or Groups of Device Manufacturers: single corporate entities under specific legislative regulation
> - The GSMA DAG (EIN Assignment Services) handles all ERHI1 applications via EISRegistration@gsma.com
> - Eligibility criteria include: must not already hold an ERHI1 (with limited justified exceptions) and must commit to use within 12 months
> - A parallel cancellation process exists for ERHI1s that are no longer needed, with identical verification rigour
> - Subsequent Level EAAs (Level ≥2) have their own responsibilities under SGP.29, including complying with all EID requirements and reporting to their parent EAA

The ERHI1 assignment process is the gatekeeper of the eSIM numbering system. Every EID in existence traces back to an ERHI1 issued by the GSMA: making this process the foundation of eUICC identity governance.

---

## Who Can Apply?

SGP.29 v1.1 defines four categories of eligible applicants for ERHI1:

### 1. eUICC Manufacturers (EUMs)

The most direct path. EUMs who manufacture eUICC chips apply directly to the GSMA for an ERHI1. They then assign ESINs to individual chips under their assigned EIN.

### 2. Device Manufacturers

Added in SGP.29 v1.1 (March 2024, CR11000R06). Device manufacturers: companies that embed eUICCs into consumer devices (phones, tablets, wearables) or IoT equipment: can now obtain ERHI1 values directly. This allows them to manage EID allocation for the eUICCs they integrate without going through an intermediate authority.

### 3. National Authorities

National Regulatory Authorities may apply for ERHI1 values, which they can then sub-delegate to entities within their jurisdiction. This preserves the ability of national administrations to maintain oversight of numbering resources within their territories.

### 4. Groups of Device Manufacturers

Also added in v1.1 (CR11001R02). A collection of Device Manufacturers represented by a single entity can apply as a group, receiving an ERHI1 that they then sub-delegate to individual member companies.

---

## Eligibility Criteria (Section 11)

All applicants must satisfy three mandatory criteria:

<div align="center">

<svg width="620" height="300" viewBox="0 0 620 300" xmlns="http://www.w3.org/2000/svg">
 <defs>
 <filter id="glow"><feGaussianBlur stdDeviation="1.5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
 <linearGradient id="headerGrad" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0%" stop-color="#1e5799"/><stop offset="100%" stop-color="#2989d8"/>
 </linearGradient>
 </defs>

 <!-- Card background -->
 <rect x="10" y="10" width="600" height="280" rx="8" fill="#151b23" stroke="#30363d" stroke-width="1.5"/>

 <!-- Header -->
 <rect x="10" y="10" width="600" height="42" rx="8" fill="url(#headerGrad)"/>
 <rect x="10" y="42" width="600" height="10" fill="url(#headerGrad)"/>
 <text x="310" y="37" text-anchor="middle" fill="#fff" font-family="system-ui,sans-serif" font-size="15" font-weight="700">ERHI1 Eligibility Checklist</text>

 <!-- Check items -->
 <g font-family="system-ui,sans-serif" font-size="13" fill="#c9d1d9">
 <!-- Item 1 -->
 <rect x="34" y="68" width="18" height="18" rx="3" fill="#1c2128" stroke="#30363d" stroke-width="1.5"/>
 <text x="42" y="81" text-anchor="middle" fill="#58a6ff" font-size="16">□</text>
 <text x="62" y="82" fill="#e6edf3">Applicant does NOT already hold an ERHI1</text>
 <text x="62" y="99" fill="#8b949e" font-size="11">(unless a justified exception applies)</text>

 <!-- Item 2 -->
 <rect x="34" y="116" width="18" height="18" rx="3" fill="#1c2128" stroke="#30363d" stroke-width="1.5"/>
 <text x="42" y="129" text-anchor="middle" fill="#58a6ff" font-size="16">□</text>
 <text x="62" y="130" fill="#e6edf3">Applicant commits to use the ERHI1 within 12 months</text>

 <!-- Item 3 -->
 <rect x="34" y="161" width="18" height="18" rx="3" fill="#1c2128" stroke="#30363d" stroke-width="1.5"/>
 <text x="42" y="174" text-anchor="middle" fill="#58a6ff" font-size="16">□</text>
 <text x="62" y="175" fill="#e6edf3">Applicant is a single corporate entity operating under</text>
 <text x="62" y="192" fill="#8b949e" font-size="11">a specific legislative regulation (non-National Authorities only)</text>

 <!-- Item 4 -->
 <rect x="34" y="209" width="18" height="18" rx="3" fill="#1c2128" stroke="#30363d" stroke-width="1.5"/>
 <text x="42" y="222" text-anchor="middle" fill="#58a6ff" font-size="16">□</text>
 <text x="62" y="223" fill="#e6edf3">Applicant is one of:</text>
 <text x="62" y="241" fill="#8b949e" font-size="11">• eUICC Manufacturer (EUM) • Device Manufacturer • Group of Device Manufacturers • National Authority</text>
 </g>
</svg>

</div>

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

1. **Authenticity of the applicant company** : Is this a legitimate, registered corporate entity?
2. **Validity of the application** : Does the applicant meet all eligibility criteria?

The entire verification process is estimated to take **no more than 5 working days** after receipt of the correctly completed form.

<div align="center">

<svg width="500" height="200" viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg">
 <defs>
 <marker id="arrowGreen" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
 <path d="M0,0 L8,3 L0,6 Z" fill="#3fb950"/>
 </marker>
 <marker id="arrowRed" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
 <path d="M0,0 L8,3 L0,6 Z" fill="#f85149"/>
 </marker>
 <filter id="shadow"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.15"/></filter>
 <linearGradient id="verGrad" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0%" stop-color="#1e5799"/><stop offset="100%" stop-color="#2989d8"/>
 </linearGradient>
 </defs>

 <!-- Background -->
 <rect x="0" y="0" width="500" height="200" rx="8" fill="#151b23" stroke="#30363d" stroke-width="1.5"/>

 <!-- Verification node -->
 <rect x="205" y="20" width="90" height="44" rx="22" fill="url(#verGrad)" filter="url(#shadow)"/>
 <text x="250" y="47" text-anchor="middle" fill="#fff" font-family="system-ui,sans-serif" font-size="13" font-weight="700">Verification</text>

 <!-- Arrow from Verification -->
 <line x1="250" y1="64" x2="250" y2="88" stroke="#8b949e" stroke-width="1.5"/>
 <line x1="250" y1="88" x2="90" y2="116" stroke="#8b949e" stroke-width="1.5"/>
 <line x1="250" y1="88" x2="410" y2="116" stroke="#8b949e" stroke-width="1.5"/>

 <!-- FAILS branch -->
 <rect x="20" y="116" width="140" height="30" rx="6" fill="#1c2128" stroke="#f85149" stroke-width="1.5"/>
 <text x="90" y="135" text-anchor="middle" fill="#f85149" font-family="system-ui,sans-serif" font-size="13" font-weight="700"> FAILS</text>
 <text x="90" y="172" text-anchor="middle" fill="#8b949e" font-family="system-ui,sans-serif" font-size="11">Further action depending</text>
 <text x="90" y="188" text-anchor="middle" fill="#8b949e" font-family="system-ui,sans-serif" font-size="11">on reason (e.g. fraud)</text>

 <!-- SUCCEEDS branch -->
 <rect x="340" y="116" width="140" height="30" rx="6" fill="#1c2128" stroke="#3fb950" stroke-width="1.5"/>
 <text x="410" y="135" text-anchor="middle" fill="#3fb950" font-family="system-ui,sans-serif" font-size="13" font-weight="700"> SUCCEEDS</text>
 <text x="410" y="172" text-anchor="middle" fill="#8b949e" font-family="system-ui,sans-serif" font-size="11">Proceed to</text>
 <text x="410" y="188" text-anchor="middle" fill="#8b949e" font-family="system-ui,sans-serif" font-size="11">Stage 4</text>
</svg>

</div>

### Stage 4: ERHI1 Assignment

Upon successful verification, the GSMA assigns a unique ERHI1 value to the applicant. The GSMA registers this assignment in its central registry and updates the status of the ERHI1 to "assigned."

### Stage 5: GSMA Confirmation

The GSMA notifies the applicant of the assigned ERHI1 by returning the completed and approved registration form. From this point, the ERHI1 is active and the holder may begin assigning sub-ranges or manufacturing eUICCs with EIDs under their EIN.

---

## Process Diagram

<div align="center">

<svg width="640" height="520" viewBox="0 0 640 520" xmlns="http://www.w3.org/2000/svg">
 <defs>
 <marker id="arr" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
 <path d="M0,0 L8,3 L0,6 Z" fill="#58a6ff"/>
 </marker>
 <marker id="arrRed" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
 <path d="M0,0 L8,3 L0,6 Z" fill="#f85149"/>
 </marker>
 <marker id="arrGreen" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
 <path d="M0,0 L8,3 L0,6 Z" fill="#3fb950"/>
 </marker>
 <linearGradient id="headerG" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0%" stop-color="#1e5799"/><stop offset="100%" stop-color="#2989d8"/>
 </linearGradient>
 <filter id="sh"><feDropShadow dx="0" dy="1" stdDeviation="2" flood-opacity="0.12"/></filter>
 </defs>

 <!-- Background -->
 <rect x="0" y="0" width="640" height="520" rx="8" fill="#151b23" stroke="#30363d" stroke-width="1.5"/>

 <!-- Title -->
 <rect x="0" y="0" width="640" height="40" rx="8" fill="url(#headerG)"/>
 <rect x="0" y="32" width="640" height="8" fill="url(#headerG)"/>
 <text x="320" y="27" text-anchor="middle" fill="#fff" font-family="system-ui,sans-serif" font-size="14" font-weight="700">ERHI1 Assignment: 5-Stage Process</text>

 <!-- Lane headers -->
 <rect x="20" y="56" width="295" height="28" rx="5" fill="#1c2a3a" stroke="#58a6ff" stroke-width="1" opacity="0.7"/>
 <text x="167" y="76" text-anchor="middle" fill="#58a6ff" font-family="system-ui,sans-serif" font-size="12" font-weight="700"> Applicant</text>

 <rect x="325" y="56" width="295" height="28" rx="5" fill="#1c2a3a" stroke="#f0c040" stroke-width="1" opacity="0.7"/>
 <text x="472" y="76" text-anchor="middle" fill="#f0c040" font-family="system-ui,sans-serif" font-size="12" font-weight="700"> GSMA EIN Assignment Services (DAG)</text>

 <!-- Divider -->
 <line x1="320" y1="56" x2="320" y2="505" stroke="#30363d" stroke-width="1" stroke-dasharray="4,4"/>

 <!-- Stage 1: Fill Registration Form (Applicant) -->
 <rect x="35" y="96" width="270" height="52" rx="7" fill="#1c2128" stroke="#58a6ff" stroke-width="1.3" filter="url(#sh)"/>
 <rect x="35" y="96" width="36" height="52" rx="7" fill="#1e3a5f" opacity="0.6"/>
 <rect x="35" y="96" width="36" height="20" rx="7" fill="#58a6ff" opacity="0.3"/>
 <text x="53" y="112" text-anchor="middle" fill="#58a6ff" font-family="system-ui,sans-serif" font-size="14" font-weight="700">1</text>
 <text x="80" y="115" fill="#e6edf3" font-family="system-ui,sans-serif" font-size="12" font-weight="600">Fill Registration Form</text>
 <text x="80" y="135" fill="#8b949e" font-family="system-ui,sans-serif" font-size="10">Download &amp; complete form from gsma.com</text>

 <!-- Arrow 1→2 -->
 <path d="M170,148 L170,168 L472,168 L472,180" stroke="#58a6ff" stroke-width="1.5" fill="none" marker-end="url(#arr)"/>

 <!-- Stage 2: Submit (GSMA side -- actually it's applicant submitting TO GSMA) -->
 <rect x="340" y="182" width="270" height="52" rx="7" fill="#1c2128" stroke="#f0c040" stroke-width="1.3" filter="url(#sh)"/>
 <rect x="340" y="182" width="36" height="52" rx="7" fill="#3d3520" opacity="0.6"/>
 <rect x="340" y="182" width="36" height="20" rx="7" fill="#f0c040" opacity="0.2"/>
 <text x="358" y="198" text-anchor="middle" fill="#f0c040" font-family="system-ui,sans-serif" font-size="14" font-weight="700">2</text>
 <text x="385" y="201" fill="#e6edf3" font-family="system-ui,sans-serif" font-size="12" font-weight="600">Submit Form</text>
 <text x="385" y="221" fill="#8b949e" font-family="system-ui,sans-serif" font-size="10">Email to EISRegistration@gsma.com</text>

 <!-- Arrow 2→3 (GSMA internal) -->
 <line x1="475" y1="234" x2="475" y2="256" stroke="#58a6ff" stroke-width="1.5" marker-end="url(#arr)"/>

 <!-- Stage 3: Verification (GSMA) -->
 <rect x="340" y="258" width="270" height="52" rx="7" fill="#1c2128" stroke="#f0c040" stroke-width="1.3" filter="url(#sh)"/>
 <rect x="340" y="258" width="36" height="52" rx="7" fill="#3d3520" opacity="0.6"/>
 <rect x="340" y="258" width="36" height="20" rx="7" fill="#f0c040" opacity="0.2"/>
 <text x="358" y="274" text-anchor="middle" fill="#f0c040" font-family="system-ui,sans-serif" font-size="14" font-weight="700">3</text>
 <text x="385" y="277" fill="#e6edf3" font-family="system-ui,sans-serif" font-size="12" font-weight="600">Verification</text>
 <text x="385" y="297" fill="#8b949e" font-family="system-ui,sans-serif" font-size="10">Authenticity &amp; eligibility check (≤ 5 working days)</text>

 <!-- Fail path (back to Applicant) -->
 <path d="M340,284 L200,284 L200,340" stroke="#f85149" stroke-width="1.2" stroke-dasharray="6,3" fill="none" marker-end="url(#arrRed)"/>
 <text x="260" y="277" fill="#f85149" font-family="system-ui,sans-serif" font-size="9">Fails →</text>

 <!-- Fail box -->
 <rect x="105" y="320" width="195" height="30" rx="5" fill="#1c2128" stroke="#f85149" stroke-width="1"/>
 <text x="203" y="340" text-anchor="middle" fill="#f85149" font-family="system-ui,sans-serif" font-size="10"> Further action (e.g. fraud)</text>

 <!-- Arrow 3→4 (GSMA) -->
 <line x1="475" y1="310" x2="475" y2="344" stroke="#58a6ff" stroke-width="1.5" marker-end="url(#arr)"/>

 <!-- Stage 4: Assign (GSMA) -->
 <rect x="340" y="346" width="270" height="52" rx="7" fill="#1c2128" stroke="#f0c040" stroke-width="1.3" filter="url(#sh)"/>
 <rect x="340" y="346" width="36" height="52" rx="7" fill="#3d3520" opacity="0.6"/>
 <rect x="340" y="346" width="36" height="20" rx="7" fill="#f0c040" opacity="0.2"/>
 <text x="358" y="362" text-anchor="middle" fill="#f0c040" font-family="system-ui,sans-serif" font-size="14" font-weight="700">4</text>
 <text x="385" y="365" fill="#e6edf3" font-family="system-ui,sans-serif" font-size="12" font-weight="600">Assign ERHI1</text>
 <text x="385" y="385" fill="#8b949e" font-family="system-ui,sans-serif" font-size="10">Unique ERHI1 registered, status → "assigned"</text>

 <!-- Arrow 4→5 (back to Applicant) -->
 <path d="M340,372 L170,372 L170,420" stroke="#3fb950" stroke-width="1.5" fill="none" marker-end="url(#arrGreen)"/>
 <text x="240" y="366" fill="#3fb950" font-family="system-ui,sans-serif" font-size="9">Success →</text>

 <!-- Stage 5: Confirmation (Applicant) -->
 <rect x="35" y="420" width="270" height="52" rx="7" fill="#1c2128" stroke="#58a6ff" stroke-width="1.3" filter="url(#sh)"/>
 <rect x="35" y="420" width="36" height="52" rx="7" fill="#1e3a5f" opacity="0.6"/>
 <rect x="35" y="420" width="36" height="20" rx="7" fill="#58a6ff" opacity="0.3"/>
 <text x="53" y="436" text-anchor="middle" fill="#58a6ff" font-family="system-ui,sans-serif" font-size="14" font-weight="700">5</text>
 <text x="80" y="439" fill="#e6edf3" font-family="system-ui,sans-serif" font-size="12" font-weight="600">Confirmation Received</text>
 <text x="80" y="459" fill="#8b949e" font-family="system-ui,sans-serif" font-size="10">Approved form with ERHI1 returned by GSMA</text>

 <!-- Legend -->
 <rect x="20" y="488" width="600" height="1" fill="#30363d"/>
 <circle cx="112" cy="507" r="3" fill="#58a6ff"/>
 <text x="120" y="511" fill="#8b949e" font-family="system-ui,sans-serif" font-size="9">Standard flow</text>
 <line x1="177" y1="507" x2="197" y2="507" stroke="#f85149" stroke-width="1.2" stroke-dasharray="4,2"/>
 <text x="202" y="511" fill="#8b949e" font-family="system-ui,sans-serif" font-size="9">Failure path</text>
 <line x1="267" y1="507" x2="287" y2="507" stroke="#3fb950" stroke-width="1.2"/>
 <text x="292" y="511" fill="#8b949e" font-family="system-ui,sans-serif" font-size="9">Success return</text>
</svg>

</div>

---

## The Cancellation Process (Section 13)

An ERHI1 that is no longer used may be voluntarily cancelled. The process mirrors the assignment flow:

| Stage | Action |
|-------|--------|
| **1. Form Filling** | Applicant completes the Cancellation Form from gsma.com |
| **2. Submission** | Form submitted to EISRegistration@gsma.com with the ERHI1 to be cancelled |
| **3. Verification** | GSMA verifies authenticity and validity (≤5 working days) |
| **4. Cancellation** | GSMA cancels the ERHI1: it is marked as cancelled in the registry |
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

Any Level X EIN Assignment Authority (where X ≥ 2) : e.g., a National Authority that received an ERHI1 and is assigning ERHI2 values: has its own set of responsibilities:

1. **Comply with EID requirements** : Must follow Sections 8 (EID Scheme Requirements), 9 (Assignment Authority Requirements), and 10 (Numbering Scheme)
2. **Complete forms accurately** : Fill in all required information on Registration or Cancellation Forms
3. **Ensure ERHIx uniqueness** : Each sub-delegated ERHI must be unique within the EAA's range
4. **Only the verified company cancels** : A third party cannot request cancellation of another entity's identifier
5. **No reuse after cancellation** : Cancelled ERHIx values must not be used after the cancellation date
6. **Report to parent EAA** : Comply with assignment reporting requirements for the Level X−1 authority that granted their range

---

## Summary

- ERHI1 assignment is a formal 5-stage process: form → submit → verify (≤5 days) → assign → confirm
- Eligibility is restricted to EUMs, Device Manufacturers, Groups of Device Manufacturers, or National Authorities
- A parallel cancellation process exists for unused ERHI1s, preventing identifier waste
- The GSMA maintains a central registry of all assignments, conducts yearly integrity reviews, and ensures cancelled identifiers are never reused
- Subsequent Level EAAs (Level ≥2) have their own compliance obligations, including reporting to their parent authority
- The entire process is designed to verify legitimacy, prevent fraud, and maintain global EID uniqueness

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp29/28-sgp29-eid-format">EID Format Decoded: The 32-Digit Structure</a> · <a href="{{ site.baseurl }}/"> Home</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp29/30-sgp29-in-protocols">EID in RSP Protocols: Discovery, Matching, and Events</a> →

</div>

---

*Based on GSMA SGP.29 v1.1 (22 March 2024) : EID Definition and Assignment Process, Sections 11–15*


---

← Previous: [EID Format Decoded: The 32-Digit Structure](28-sgp29-eid-format) | [Section Index](index) | Next: [EID in RSP Protocols: Discovery, Matching, and Events](30-sgp29-in-protocols) →
