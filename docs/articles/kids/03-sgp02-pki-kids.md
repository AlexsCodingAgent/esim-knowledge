---
title: "The ID Badge Family Tree for Robots"
date: 2026-06-07
---

# The ID Badge Family Tree for Robots 🪪

## Imagine...

You're a security guard at the robot factory. A stranger walks up and says, "I'm the Commander — let me send new orders to Robot #8721." How do you know they're legit? You check their ID badge. But how do you know the ID badge is real? You trace it up the chain — to see who signed it.

That's the **ID Badge Family Tree** (PKI — Public Key Infrastructure) that keeps SGP.02 secure. Every helper in the M2M network carries a signed badge, and every badge traces back to one trusted source.

---

## The Family Tree 🌳

```
     🏛️ The Passport Office (CI)
              │
              │ Signs badges for...
     ┌────────┼────────┐
     │        │        │
🏭 Chip    🔑 Key   🦾 Robot Fleet
Builder   Factory   Commander
(EUM)     (SM-DP)    (SM-SR)
     │
     │ Signs badges for...
     │
  🤖 Robot Vault Chip
     (eUICC)
```

---

## Three Levels of Trust 🏛️

### Level 1: The Passport Office (CI Root)
The **Certificate Issuer** creates the master stamp. Its public key is installed in every robot vault chip at birth. This is the ultimate trust anchor — if a badge doesn't trace back to the CI, the robot ignores it completely.

**Analogy:** The government passport office. Every passport must trace back to their master seal.

### Level 2: The Trusted Helpers
The CI signs badges for three kinds of helpers:
- **Chip Builder (EUM)** — proves the manufacturer is GSMA-accredited
- **Key Factory (SM-DP)** — proves the key maker is legitimate
- **Commander (SM-SR)** — proves the fleet commander is authorised

### Level 3: The Robots Themselves
Each robot gets a unique badge signed by its Chip Builder — not by the CI directly. This badge contains the robot's public key, its 32-digit EID fingerprint, and a reference to its security certification.

---

## Two Different Badge Formats 📋

Here's something tricky: the ID badges come in two different formats!

| Format | Who Uses It | Why |
|---|---|---|
| **X.509** (like website certificates) | CI, Chip Builders | Servers understand this format natively |
| **GlobalPlatform** (compact TLV) | Key Factories, Commanders, Robots | Smart cards can't parse X.509 — they need a compact format |

The robot chip can't read X.509! That's why Key Factory and Commander badges use a special compact format that fits in the chip's tiny brain.

---

## The Robot's Crown Jewel 👑

The most important secret in the entire system is the robot's private key: `SK.ECASD.ECKA`.

- Generated inside the chip during manufacturing
- **Never leaves the chip — ever**
- Used to prove "I am genuinely Robot #8721"
- Used to calculate shared secrets with the Key Factory
- If anyone extracts this key, the robot's identity is stolen

---

## What Happens When a Badge Goes Bad? 🚫

Sometimes a helper's ID badge gets compromised — maybe a Key Factory's private key was stolen. SGP.02 handles this with **CRLs** (Certificate Revocation Lists):

| Who Checks? | What They Do |
|---|---|
| The Operator (Fleet Owner) | Downloads the CRL regularly from the CI |
| The Operator decides | "Hmm, that Key Factory's badge is revoked — I won't send them new orders" |
| The robot chip | Does NOT check the CRL — too memory-intensive for a tiny chip |

This is the **"informed decision" model**: the Operator (a big server with lots of resources) checks the WANTED list. The robot just verifies that any badge it sees traces back to the CI.

---

## M2M PKI vs Consumer PKI

| Feature | Consumer (SGP.22) | M2M Robots (SGP.02) |
|---|---|---|
| Trust levels | 3 (same) | 3 (same) |
| Badge formats | X.509 + GP (same) | X.509 + GP (same) |
| Server role badges | SM-DP+ only (combined) | SM-DP AND SM-SR (separate) |
| Who checks CRLs? | SM-DP+ server-side | Operator — informed decision |
| Robot's private key | Same ECASD key | Same ECASD key |

---

## 🧠 Did You Know?

The cryptographic algorithms in SGP.02 are chosen to stay secure through the year **2030**: 256-bit elliptic curves, AES-128 encryption, and SHA-256 hashing. When a utility meter sealed in a basement needs to stay secure for 15 years, you plan ahead!

---

*Kid-friendly version of GSMA SGP.02 v4.2 §2.3 — Security Overview*

← [Back to Kids Articles](index)
