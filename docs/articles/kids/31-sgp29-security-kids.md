---
title: "Privacy and Secrets: Keeping Your Chip Name Safe"
date: 2026-06-07
---

# Privacy and Secrets: Keeping Your Chip Name Safe 🕵️🔐

## Imagine...

Your house has a street address. The mail carrier needs it to deliver packages. But the address doesn't reveal who lives inside, what they're eating for dinner, or what's in the packages. It's just a location label: nothing more.

The EID works the same way. It tells the eSIM ecosystem *which chip* to talk to, but it doesn't reveal anything about *who you are* or *what you're doing*. SGP.29 builds strong privacy walls to keep it that way.

---

## What the EID Reveals (and What It Doesn't) 🎭

```
EID DOES reveal:                    EID does NOT reveal:
┌──────────────────────┐            ┌──────────────────────┐
│ • Chip manufacturer  │            │ • Your name          │
│ • Chip generation    │            │ • Your phone number  │
│ • Manufacturing batch│            │ • Your carrier       │
│ • Delegation chain   │            │ • Your location      │
│   (who authorised it)│            │ • Active profiles    │
└──────────────────────┘            │ • Device model       │
                                    │ • Who you are        │
                                    └──────────────────────┘
```

The EID identifies **hardware**, not **people**. This separation is enforced by two key rules:

- **EID.P03**: The EID is NOT a payment account number: it can't be used in financial systems to charge or track you
- **EID.P04**: The EID is NOT for billing: your phone bill isn't linked to your EID

---

## Tracking Risks: Should You Worry? 📊

Because the EID is permanent (it survives resets, profile changes, and even factory wipes), there are theoretical tracking risks. Here's the honest assessment:

| Risk | How Bad Is It? | What Stops It |
|---|---|---|
| **Cross-profile tracking** | Medium | SM-DS access requires authentication: random people can't just look up EIDs |
| **Supply chain snooping** | Low | The ERHI chain shows the manufacturer, not the end user |
| **Device fingerprinting** | Low | EID doesn't say if it's a phone, car, or smart meter |
| **Impersonation** | High: but blocked! | Cryptographic authentication (SGP.22) means knowing an EID isn't enough to fake a chip's identity |

**The golden rule**: The EID is a *claim* ("I am chip #12345..."), not *proof*. The actual proof comes from the chip's private key: a secret cryptographic code that never leaves the chip. An attacker who knows your EID still can't impersonate your chip without also stealing its private key (which is locked in tamper-proof hardware).

---

## How the GSMA Keeps the System Honest 🏛️

The GSMA's governance isn't just bureaucracy: it's the enforcement backbone of EID security:

### 1. 🔒 Central Registry

Every ERHI1 ever assigned lives in one master list. No duplicates. No gaps. Complete audit trail.

### 2. ✅ Applicant Verification (≤5 days)

Before giving out any numbers, the GSMA checks: is this a real company? Do they meet all the rules? If verification raises fraud concerns, the GSMA can escalate to relevant authorities.

### 3. 📋 Yearly Integrity Review

```
Collect → Analyse → Report → Act
   │          │         │       │
   │          │         │       └─ Fix problems
   │          │         └─ Present to GSMA oversight group
   │          └─ Check for anomalies, underuse, violations
   └─ Gather usage data from all number holders
```

This yearly cycle catches problems before they become crises.

### 4. 🚫 No Recycling

Once an ERHI1 is cancelled, it's gone forever. Never reassigned. This prevents "EID resurrection attacks" where a cancelled range is given to a new company who accidentally clashes with old chips still in the field.

---

## The EID Lifecycle 🔄

Every EID range follows a carefully managed lifecycle:

```
ASSIGNMENT ──▶ ACTIVE USE ──▶ CANCELLATION ──▶ EXPIRED (archived forever)
     │              │                │                    │
     │              │                │                    │
 GSMA verifies  EUM stamps      Holder requests      Never, ever
 ≤5 days        ESINs onto      cancellation;        reassigned
 authenticity   real chips      GSMA verifies
                                and cancels
```

Once a range reaches "Expired," it's permanently archived. Those numbers will never appear on a new chip: guaranteeing that every EID ever created remains unique for all time.

---

## The "89" Firewall 🔥

SGP.29 builds in one more clever protection: **GSMA-assigned EIDs never start with "89."** That prefix is reserved for old-style SIM card identifiers (ICCIDs).

```
89XXXXXXXX... = Old SIM card territory (ITU-T E.118 legacy)
00-88XXXX...  = GSMA SGP.29 territory
90-99XXXX...  = GSMA SGP.29 territory

No collision possible! The "89" prefix acts as a permanent wall.
```

This means old and new systems coexist peacefully: an eSIM chip identified under SGP.29 will never be confused with one identified under the old ICCID scheme.

---

## The Check Digit Shield 🛡️

The MOD 97-10 check digit algorithm provides banking-grade error detection:

| Error Type | Detection Rate |
|---|---|
| Single digit typo (7 → 8) | **100%** guaranteed |
| Swapped digits (12 → 21) | **100%** guaranteed |
| Twin errors (11 → 22) | **100%** guaranteed |
| Other random errors | ~99.0% |

If anyone: a factory worker, a database, a QR code scanner: makes a single-digit mistake in an EID, the check will catch it instantly. This prevents misrouted profiles, misidentified chips, and all the chaos that would follow.

---

The EID is one of the few truly permanent identifiers in the digital world. Your phone number changes when you switch carriers. Your IMEI changes when you get a new phone. But the EID on an eSIM chip stays the same forever: from the factory floor to the recycling centre. That's why SGP.29 takes its privacy and security so seriously!

---

*Kid-friendly version of GSMA SGP.29 v1.1: EID Security, Sections 7–9, 12–14, and Annex A*

← [Back to Kids Articles](index)
