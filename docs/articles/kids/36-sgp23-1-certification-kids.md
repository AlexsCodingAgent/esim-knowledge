---
description: "How eUICC chips pass their final factory inspection: the SAS-UP security accreditation that verifies the production line matches the tested design, from declaration through accredited manufacturing."
title: "The Ultimate Safety Inspection: SAS-UP"
date: 2026-06-07
---

# The Ultimate Safety Inspection: SAS-UP 🏭✅

## Imagine...

You've designed the world's safest car seat. It passed every crash test, every material check, every durability trial. But there's one more hurdle: an inspector visits the **factory** where it's made. They check that the assembly line doesn't mix up parts, that workers follow safety protocols, and that every seat coming off the line is identical to the one that passed testing.

A brilliant design made in a sloppy factory is NOT a safe product.

This is the logic behind **SAS-UP** : the Security Accreditation Scheme for UICC Production. It's the final check that transforms a tested eUICC design into a production-ready chip.

---

## The Six-Stage Certification Journey 🗺️

| Stage | What Happens |
|---|---|
| **1. Declaration** | Chip maker fills out the Optional Features Table (30+ options) and provides IUT Settings |
| **2. Applicability** | The Applicability Table determines exactly which tests apply (Mandatory, Conditional, or Not Applicable) |
| **3. Execution** | Tests run in TE_eUICC or TE_Integrated eUICC environment |
| **4. Results** | Each test gets Pass, Fail, or Inconclusive (infrastructure problems don't count against the chip!) |
| **5. SAS-UP Link** | The `sasAcreditationNumber` in the chip's response is verified against the accredited factory |
| **6. DLOA** | Digital Letter of Approval issued by GlobalPlatform |

---

## The Declaration: What Can Your Chip Do? 📋

Before testing starts, the vendor fills out an honest self-assessment:

| Category | Example Options |
|---|---|
| **Encryption Curves** | NIST P-256, BrainpoolP256r1, FRP256V1, SM2 |
| **LPA Features** | Built-in LPAe, LPA Proxy support |
| **Profile Features** | Remote Profile Management, Enterprise Profiles, Device Change, OS Update |
| **MEP Modes** | MEP-A1, MEP-A2, MEP-B, MEP-B without Refresh |
| **Form Factor** | Standard removable chip or Integrated (SoC-embedded) |

If a vendor supports both "with" and "without" a feature (providing different chip samples), the test tool runs all applicable tests for each sample independently.

---

## Applicability: The Smart Filter 🧠

The Applicability Table uses logic to decide which tests to run:

- **M** (Mandatory) : Every chip must pass these, no exceptions
- **N/A** (Not Applicable) : Impossible in this context (e.g., SGP.22 V2.1 tests are N/A for SGP.23-1 which targets V3.1)
- **Ci** (Conditional) : Only runs IF certain options are declared:
  - `C001` = IF O_E_NIST THEN run NIST-specific tests
  - Complex nesting: `IF ... THEN (IF ... THEN ... ELSE ...) ELSE ...`

This means a simple chip gets a manageable test suite, while a feature-packed chip gets a comprehensive one.

---

## Pass, Fail, or Inconclusive? 🤔

SGP.23-1 is fair about failures:

| Result | Meaning |
|---|---|
| **Pass** ✅ | Every step produced the expected result |
| **Fail** ❌ | The chip did something unexpected at some step |
| **Inconclusive** ⚠️ | The test couldn't finish because of setup problems: NOT the chip's fault! |

The inconclusive category prevents false negatives. If the test tool has a bug or the card reader glitches, the chip isn't penalised.

---

## SAS-UP: The Factory Check 🏭

SAS-UP doesn't test the chip design: it audits the **manufacturing site**:

- Physical security of the production facility
- How cryptographic material is handled during manufacturing
- Access controls: who can touch what?
- Key injection procedures: are secret keys loaded securely?
- Audit trails: can you trace every chip back through production?

The link between testing and manufacturing is the `sasAcreditationNumber` : a unique identifier embedded in every production chip that SGP.23-1 test cases explicitly verify.

---

## The Final Prize: DLOA 🏆

When all applicable tests pass, the **Digital Letter of Approval** is issued:

- **Globally recognised** : Accepted by mobile operators worldwide
- **Machine-verifiable** : Stored on a DLOA Registrar with a discovery URL
- **Specific** : Lists exactly which SGP.22 version, which optional features, and which test lab
- **Gateway to production** : Without a DLOA, an eUICC cannot be deployed in commercial devices

---

## The Layered Trust Model 🧅

eSIM certification is like an onion: layers of trust, each depending on the layer below:

1. **SAS-UP** certifies the factory
2. **SGP.23-1** certifies the chip from that factory
3. **SGP.23** uses the certified chip to test everything else
4. **Operators** trust the whole stack because every layer has been independently verified

---

The GSMA runs regular Test Events where vendors bring their implementations for formal assessment. SGP.23-1's document history shows Change Requests flowing in from these events: each one fixing an ambiguity that real testers discovered. The specification has evolved from v2.0 (2018) through v3.1.3 (2025) based on actual testing experience!

---

*Kid-friendly version of GSMA SGP.23-1, Sections 2.1, 2.2, 3, Annexes F, G, L; GlobalPlatform GPC_SPE_095*

← [Back to Kids Articles](index)
