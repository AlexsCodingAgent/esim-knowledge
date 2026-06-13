---
description: "Decoding the three-part EID structure: the manufacturer's delegation chain, the individual chip serial number, and two check digits that together form a mathematical fingerprint for verification."
title: "Cracking the Code: What Those 32 Digits Mean"
date: 2026-06-07
---

# Cracking the Code: What Those 32 Digits Mean 🔍🔢

## Imagine...

You look at an international phone number: `+1-555-123-4567`. Even without knowing whose number it is, you can decode it: `+1` means North America, `555` is the area code, and the rest is the local number. The EID works the same way: those 32 digits aren't random. They're a carefully structured code that tells a story!

---

## The Three-Part Recipe 🧩

Every EID is exactly 32 digits long, built from three pieces:

```
┌──────────────────────────────────────────────────────────┐
│              EID: 32 Digits Total                        │
├──────────────────────┬─────────────────┬─────────────────┤
│   EIN (N digits)     │ ESIN (30-N)     │ Check (2)       │
│   Who made the chip? │ Which chip?     │ Is this valid?  │
└──────────────────────┴─────────────────┴─────────────────┘
```

| Part | Name | What It Tells You |
|---|---|---|
| **EIN** | EUM Identification Number | The delegation chain: who authorised this chip's name |
| **ESIN** | EUM Specific Identification Number | Which individual chip this is (like a serial number within a batch) |
| **Check** | Check Digits (2 digits) | A mathematical fingerprint that proves the EID is genuine |

The EIN can be different lengths (N digits). The ESIN fills whatever's left up to position 30. The last 2 digits are always the check. So: **EIN + ESIN = always 30 digits + 2 check digits = 32 total.**

---

## The EIN: A Delegation Chain ⛓️

The EIN isn't just a single number: it's built by chaining together **ERHI** (EID Range Holder Identifier) values, one from each level of authority:

```
EIN = ERHI1 + ERHI2 + ERHI3 + ... + ERHIx
       │        │        │            │
       │        │        │            └─ Assigned to the chip maker (EUM)
       │        │        └─ Assigned by a device maker or national authority
       │        └─ Assigned by a national authority or device maker
       └─ Assigned by the GSMA (the head librarian!)
```

### Example Delegation Chains:

**Three levels** (GSMA → National Authority → Device Maker → Chip Maker):
```
GSMA assigns "12" → National Authority
    → National Authority assigns "345" → Device Maker
        → Device Maker assigns "67" → Chip Maker
            → EIN = "1234567" (N=7)
```

**Two levels** (GSMA → Device Maker → Chip Maker):
```
GSMA assigns "98" → Device Maker
    → Device Maker assigns "76" → Chip Maker
        → EIN = "9876" (N=4)
```

The chain can be as short or as long as needed: whatever fits the real-world supply chain!

---

## The Check Digits: The Magic Number Test 🪄

Here's the coolest part. The last 2 digits let anyone verify an EID with simple math using the **MOD 97-10** algorithm: the same one banks use to validate IBAN numbers!

### How to Verify Any EID:

1. Take the full 32-digit number
2. Divide it by 97
3. If the remainder is **exactly 1** → ✅ Valid EID!
4. Any other remainder → ❌ Fake or corrupted!

### Worked Example:

Let's check this EID: `12345000000000000000000000000133`

```
12345000000000000000000000000133 ÷ 97 = ???

Remainder = 1 ✅ VALID!
```

If someone accidentally typed `12345000000000000000000000000134`:

```
Remainder ≠ 1 ❌ INVALID! (someone made a typo!)
```

This check catches **100% of single-digit typos** and **100% of swapped digits**. It's incredibly reliable!

---

## EID vs Old SIM Cards vs Phone IDs 📊

| Property | EID (SGP.29) | ICCID (Old SIM) | IMEI (Phone ID) |
|---|---|---|---|
| **Length** | 32 digits | Up to 20 digits | 15 digits |
| **Purpose** | Identify eSIM chip | Identify SIM account | Identify phone device |
| **Starts with** | Anything except "89" | Always "89" | Type code (8 digits) |
| **Check method** | MOD 97-10 (bank-grade!) | Luhn MOD 10 | Luhn MOD 10 |
| **Who manages it** | GSMA | National authorities | GSMA / TIA |

The big difference? EIDs **never** start with "89" : that prefix is reserved for old-style SIM card identifiers. This prevents any possible mix-up between the two systems!

---

The MOD 97-10 check digit algorithm is the exact same one used for IBANs (International Bank Account Numbers). Your eSIM chip's identity is verified with banking-grade mathematics. If a single digit is wrong anywhere in the 32-digit EID, the check will catch it every single time!

---

*Kid-friendly version of GSMA SGP.29 v1.1: EID Format, Section 10*

← [Back to Kids Articles](index)
