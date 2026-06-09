---
title: "EID Format Decoded: The 32-Digit Structure"
description: "Decodes the SGP.29 EID's 32-digit hierarchical structure — EIN delegation chain, ESIN assignment, and modulo-97 check digits — showing how to validate any EID with simple arithmetic."
date: 2026-06-05
---

# EID Format Decoded: The 32-Digit Structure

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.29 EID]({{ site.baseurl }}/docs/articles/sgp29/) > EID Format Decoded: The 32-Digit Structure**

> **💡 Why this matters:** The EID's 32-digit structure is not arbitrary: it encodes a hierarchical delegation chain from the GSMA down to individual eUICC manufacturers, with built-in cryptographic verification. Understanding the format reveals how EID ranges are delegated through a tree of assignment authorities, how manufacturers encode their identity, and how anyone can validate an EID's authenticity using simple modular arithmetic.

> **Key takeaways:**
> - The EID is exactly 32 digits, composed of EIN (N digits) + ESIN (30−N digits) + 2 check digits
> - The EIN (EUM Identification Number) is a concatenation of one or more ERHI (EID Range Holder Identifier) values, forming a delegation chain
> - The ESIN (EUM Specific Identification Number) is assigned by the eUICC Manufacturer for individual chips
> - Check digits are computed using a modulo-97 algorithm (ISO/IEC 7064 MOD 97-10, also used for IBAN validation)
> - Verification is simple: compute the remainder of the full 32-digit number divided by 97; if the result is 1, the EID is valid
> - Unlike ICCID, EIDs are NOT required to start with "89" (the industry identifier for telecommunications)

The EID structure specified in SGP.29 Section 10 is a hierarchical numbering scheme that supports multiple levels of delegation. It was designed to accommodate the complex supply chain of eSIM manufacturing, where the GSMA may delegate ranges to national authorities, who in turn delegate to device manufacturers, who assign to eUICC manufacturers.

---

## The Three-Part Structure

```
┌──────────────────────────────────────────────────────────────┐
│                     EID: 32 Digits Total                     │
├──────────────────────────┬───────────────────┬───────────────┤
│       EIN (N digits)     │  ESIN (30−N digits)│ Check (2)    │
│   EUM Identification     │  EUM-Specific      │  Mod-97      │
│   Number                 │  Identification    │  validation  │
│   (Variable length N)    │  (Variable length)  │              │
└──────────────────────────┴───────────────────┴───────────────┘
```

### Part 1: EIN: EUM Identification Number

The EIN identifies the eUICC Manufacturer (EUM) and the delegation path that granted them their numbering range. It is composed of one or more concatenated **ERHI** (EID Range Holder Identifier) values:

```
EIN = ERHI1 || ERHI2 || ERHI3 || ... || ERHIx
  │         │         │               │
  │         │         │               └─ Last ERHI assigned to the EUM
  │         │         └─ Assigned by a Device Manufacturer or intermediate EAA
  │         └─ Assigned by a National Authority or intermediate EAA  
  └─ Assigned by the GSMA (First Level EAA)
```

**Key rules for ERHIs:**

| Property | Rule |
|----------|------|
| **Variable length** | Each ERHI can be a different number of digits: the assigning EAA decides the length |
| **Prefix reservation** | Assigning ERHI "11" blocks all numbers starting with "11" (e.g., 110–119) |
| **Uniqueness** | Each EAA is responsible for uniqueness within its assigned range |
| **Delegation chain** | The hierarchical chain can be as long or short as needed |

### Part 2: ESIN: EUM Specific Identification Number

The ESIN fills the remaining digits up to position 30 (before the check digits). Since the EIN takes N digits, the ESIN is always **30 − N digits**. The EUM assigns ESINs to individual eUICC chips and is responsible for their uniqueness.

### Part 3: Check Digits: Modulo-97 Validation

The final 2 digits provide cryptographic-strength validation of the entire EID, using the same algorithm as IBAN (International Bank Account Number) validation.

---

## The MOD 97-10 Check Digit Algorithm (ISO 7064)

> **Note:** While commonly described as a "Luhn-style" algorithm, SGP.29 actually specifies ISO/IEC 7064 MOD 97-10: the same standard used for IBANs. This is a different (and stronger) algorithm than the MOD 10 Luhn algorithm used for credit cards.

### Calculation (by the EUM)

```
Step 1:  Set the two check digits to "00"
Step 2:  Treat the entire 32-digit string as a decimal integer
Step 3:  Compute: remainder = 32_digit_number MOD 97
Step 4:  Set check digits = 98 − remainder
Step 5:  If result is a single digit, prefix with "0"
```

### Verification (by any party)

```
Step 1:  Treat the entire 32-digit EID as a decimal integer
Step 2:  Compute: remainder = 32_digit_number MOD 97
Step 3:  If remainder == 1 → valid EID
         Otherwise → invalid EID
```

---

## Worked Example

Let's walk through an example with a simplified EIN.

**Setup:**
- GSMA assigns ERHI1 = `12` (2 digits) to Device Manufacturer Alpha
- Alpha assigns ERHI2 = `345` (3 digits) to EUM Beta
- EIN = `12345` (N = 5)
- EUM Beta assigns ESIN = `0000000000000000000000001` (25 digits, filling 30−5)
- Raw EID (before check digits): `12345000000000000000000000000100`

**Calculate check digits:**

```
32-digit integer = 12345000000000000000000000000100
Remainder ÷ 97   = 12345000000000000000000000000100 MOD 97
                 = 65

Check digits     = 98 − 65 = 33

Final EID        = 12345000000000000000000000000133
```

**Verify:**

```
12345000000000000000000000000133 MOD 97 = 1  ✓ Valid
```

---

## Delegation Chain Examples

SGP.29 provides three concrete examples of ERHI delegation chains:

### Example 1: Three-Level Delegation

```
GSMA ──ERHI1──▶ EAA (National Authority) ──ERHI2──▶ Device Manufacturer ──ERHI3──▶ EUM

  [GSMA]               [National Authority]         [Device Mfr]              [EUM]
  Assigns ERHI1         Assigns ERHI2 values        Assigns ERHI3 values      Assigns ESINs
  to EAA                to Device Manufacturers     to EUMs                   to individual chips
```

### Example 2: Two-Level Delegation

```
GSMA ──ERHI1──▶ Device Manufacturer ──ERHI2──▶ EUM

  [GSMA]               [Device Mfr]              [EUM]
  Assigns ERHI1         Assigns ERHI2 values      Assigns ESINs
  to Device Mfr          to EUMs                   to individual chips
```

### Example 3: Group Delegation

```
GSMA ──ERHI1──▶ Group of Device Mfrs ──ERHI2──▶ Single Device Mfr ──ERHI3──▶ EUM

  [GSMA]          [Group]                  [Single Device Mfr]         [EUM]
  Assigns ERHI1   Assigns ERHI2 values     Assigns ERHI3 values        Assigns ESINs
  to Group        to individual members    to EUMs                     to individual chips
```

---

## EID vs ICCID vs IMEI

| Property | EID (SGP.29) | ICCID (ITU-T E.118) | IMEI (3GPP) |
|----------|-------------|---------------------|-------------|
| **Length** | 32 digits | Up to 19–20 digits | 15 digits |
| **Purpose** | Identify eUICC chip | Identify SIM card account | Identify mobile device |
| **First digits** | Not constrained (but NOT 89) | 89 (telecom industry) | Type Allocation Code (8 digits) |
| **Check algorithm** | MOD 97-10 (ISO 7064) | Luhn MOD 10 | Luhn MOD 10 |
| **Governance** | GSMA | National authorities / ITU-T | GSMA / TIA |
| **Relation to service** | None (not a PAN) | May be linked to subscriber | Linked to device, not subscriber |

> **Critical distinction:** SGP.29 explicitly states that EIDs starting with `89` are **reserved** for the ITU-T E.118 based scheme. GSMA-assigned EIDs will never start with `89`, preventing any collision with legacy ICCID-based identifiers.

---

## 📋 Summary

- The EID is a 32-digit hierarchical identifier: EIN (N digits) + ESIN (30−N) + 2 check digits
- The EIN encodes a delegation chain of ERHIs from GSMA down to the EUM
- Check digits use MOD 97-10 validation: the same algorithm as IBANs: providing strong error detection
- Verification is trivial: compute `EID MOD 97` and check if the result equals 1
- Three delegation chain patterns support different supply chain structures: GSMA→EAA→DevMfr→EUM, GSMA→DevMfr→EUM, and GSMA→Group→Member→EUM
- EIDs are explicitly NOT ICCIDs and must not start with "89"

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp29/27-sgp29-overview">SGP.29 Overview: The eUICC Identifier (EID)</a> · <a href="{{ site.baseurl }}/">🏠 Home</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp29/29-sgp29-assignment">EID Assignment: How Manufacturers Get Their Allocations</a> →

</div>

---

*Based on GSMA SGP.29 v1.1 (22 March 2024) : EID Definition and Assignment Process, Section 10 (eUICC Numbering System) and Section 8 (EID Scheme Requirements)*


---

← Previous: [SGP.29 Overview: The eUICC Identifier (EID)](27-sgp29-overview) | [Section Index](index) | Next: [EID Assignment: How Manufacturers Get Their Allocations](29-sgp29-assignment) →
