---
title: "The ID Badge Family Tree for Robots"
date: 2026-06-07
---

# The ID Badge Family Tree for Robots 🪪

Every time the Commander sends an order to one of your 10,000 devices, that tiny chip faces the same question a bouncer faces at an exclusive club: *"Can I trust this person?"*

The chip can't Google the Commander. It can't phone a friend. It has no internet connection beyond the cellular network it's trying to authenticate with. All it has is mathematics: a chain of digital signatures that either traces back to a trusted source or doesn't.

That chain is the **PKI** (Public Key Infrastructure) underlying SGP.02. And if any link in it breaks, the whole system stops trusting.

---

## Tracing the chain

```
     🏛️ The Passport Office (CI)
              │
              │ Signs badges for...
     ┌────────┼────────┐
     │        │        │
🏭 Chip    🔑 Key   🦾 Commander
Builder   Factory
(EUM)     (SM-DP)    (SM-SR)
     │
     │ Signs badges for...
     │
  🤖 Device Chip
     (eUICC)
```

Every badge in this tree traces up to one root: the **Certificate Issuer (CI)**. If a badge doesn't trace back to the CI, the chip ignores it. No exceptions.

---

## Level 1: The root of all trust

The CI's public key (`PK.CI.ECDSA`) is burned into every vault chip at manufacturing. It's the one thing the chip trusts unconditionally: the ultimate anchor. The CI issues and signs certificates for every accredited player in the ecosystem, and it publishes Certificate Revocation Lists (CRLs) when someone's credentials get compromised.

If you're not on the CI's list of approved badge-holders, you don't exist as far as the chip is concerned. Period.

---

## Level 2: The trusted helpers

The CI signs badges for three kinds of organisations:

- **Chip Builders (EUMs)** : proving the manufacturer is GSMA-accredited and their chips can be trusted
- **Key Factories (SM-DPs)** : proving the profile maker is legitimate
- **Commanders (SM-SRs)** : proving the fleet commander is authorised to give orders

When the Commander sends a command to a device, it presents its CI-signed badge. The chip verifies the signature chain. If it checks out, the chip obeys. If not, the command is dropped like a fake ID at the door.

---

## Level 3: The devices themselves

Each device gets a unique badge signed by its Chip Builder, not by the CI directly. This badge bundles the device's public key, its 32-digit EID fingerprint, and a reference to its security certification.

When a Key Factory needs to encrypt a profile for Device #8721, it uses the public key from that device's badge. Only the matching private key (the one locked inside the chip's ECASD vault) can decrypt it.

---

## Two badge formats (because chips are picky)

Here's a wrinkle most people miss: not all badges use the same format.

| Format | Who Uses It | Why |
|---|---|---|
| **X.509** (like website certificates) | CI, Chip Builders | Servers handle this natively |
| **GlobalPlatform** (compact TLV) | Key Factories, Commanders, Devices | Smart cards can't parse X.509 |

The device chip is a tiny embedded processor with limited memory and no operating system that understands X.509 certificates. So Key Factory and Commander badges use a compact GlobalPlatform format the chip *can* parse. The CI's root certificate lives in the ECASD in a pre-processed form the chip can verify against. It's not elegant, but it works.

---

## The crown jewel: `SK.ECASD.ECKA`

If there's one secret in the entire SGP.02 ecosystem that matters above all others, it's the device's private key. This key:

- Is generated inside the chip during manufacturing
- Never leaves the chip, not during delivery, not during operation, not ever
- Proves "I am genuinely Device #8721" during every authentication handshake
- Is used to calculate shared session secrets with the Key Factory
- Self-destructs if anyone tries to physically extract it

Lose this key and the device's identity is stolen. The entire security model collapses to this one secret living inside a chip the size of a grain of rice.

---

## What happens when a badge goes bad?

Keys get compromised. It happens. Maybe a Key Factory's private key was stolen. SGP.02 handles this without requiring the chip to download anything.

The **Operator** (a big server with plenty of resources) regularly downloads the **CRL** : the Certificate Revocation List, from the CI. When the Operator sees a revoked badge, they simply stop sending orders to that organisation. The chip itself never checks the CRL. It's too small. Too memory-constrained.

This is the **"informed decision" model**: let the powerful server do the heavy lifting, and let the tiny chip stick to what it does best, verifying that signatures trace back to the CI. Elegant, pragmatic, and very SGP.02.

---

## M2M PKI vs Consumer PKI

| Feature | Consumer (SGP.22) | M2M (SGP.02) |
|---|---|---|
| Trust levels | 3 (same) | 3 (same) |
| Badge formats | X.509 + GP (same) | X.509 + GP (same) |
| Server role badges | SM-DP+ only (combined) | SM-DP AND SM-SR (separate) |
| Who checks CRLs? | SM-DP+ server-side | Operator, informed decision |
| Device private key | Same ECASD key | Same ECASD key |

---

## Built for 2030

The maths behind all of this isn't random. SGP.02 uses 256-bit elliptic curves, AES-128 encryption, and SHA-256 hashing, algorithms chosen to stay secure through at least 2030. When you're sealing a utility meter in a concrete basement for 15 years, you plan the cryptography for the world it'll be living in at the end of its life, not the one it was installed in.

---

*Kid-friendly version of GSMA SGP.02 v4.2 §2.3, Security Overview*

← [Back to Kids Articles](index)
