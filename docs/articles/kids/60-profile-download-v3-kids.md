---
title: "The Great Key Delivery"
date: 2026-06-07
---

# The Great Key Delivery 📦✈️

## Imagine...

You've ordered something precious — a custom-made key that only works in YOUR lock. The Key Maker (SM-DP+) crafts it in their workshop, wraps it in layers of magical protection, and dispatches it through a secure courier. When it arrives at your vault, only YOUR vault can unwrap it. Even the courier can't peek inside!

That, in a nutshell, is how **Profile Download** works in SGP.22 v3.x. It's the single most important operation in the entire eSIM world — the moment your phone gets its secret internet key.

---

## Before the Delivery: The Backstage Prep 🎭

Before you ever tap "Download," a lot happens behind the curtain:

1. **You sign up** with a carrier — you give them your info and maybe your phone's EID (its unique serial number)
2. **The carrier places an order** with the Key Maker: "One profile for this EID, please!"
3. **The Key Maker reserves a key** — it picks one from its pre-made inventory or crafts a fresh one
4. **The carrier confirms** the order and gets a MatchingID — a claim ticket
5. **The Key Maker releases** the profile — it's now ready and waiting for you

The claim ticket (MatchingID) is what's inside the QR code you scan. It says: "I'm here to pick up my key!"

---

## The Three-Phase Delivery 🚚

Once you scan that QR code, the delivery unfolds in three phases:

### Phase 1: The Identity Check 🔍

- Your Assistant (LPA) finds the Key Maker — from the QR code, a notification from the Post Office (SM-DS), or the vault's default address book
- Both sides check each other's ID badges using digital certificates
- The vault proves: "Yes, I am the vault with EID 890123..."
- The Key Maker checks: "Is there a key waiting for this claim ticket? Is it still valid? Hasn't been picked up too many times?"

### Phase 2: The Lock & Key Handshake 🤝

This is where v3.x adds several important checks:

- **PPR Check:** Does the key come with rules like "DO NOT DELETE"? Are those rules allowed on this vault?
- **Enterprise Check:** Is this a work keycard? Does it conflict with existing keys? Does the device support enterprise rules?
- **MEP Check:** On vaults that can hold multiple active keys, the "one key at a time" rule is relaxed
- **User Consent:** You confirm: "Yes, I want this key. I understand the rules."

The vault then generates a **one-time lock** — a special key pair created just for this delivery. It's like the vault saying: "Here's a padlock. Only I have the key to open it. Lock the package with this."

### Phase 3: The Unwrapping 🎁

- The Key Maker wraps the profile in a **Bound Profile Package (BPP)** — encrypted so only your vault can unwrap it
- The BPP is chopped into tiny pieces (255 bytes each) so even memory-tiny vaults can handle it
- Piece by piece, your Assistant feeds the BPP to the vault
- The vault decrypts, verifies, and installs — file system, secret keys, applets, everything
- Finally, the vault signs a **receipt**: "Profile installed successfully on ISD-P AID 1234" — cryptographic proof for the carrier

---

## How v3.x Improves the Delivery 📈

| Enhancement | What It Means |
|---|---|
| Enterprise profile validation | Work keys get special checks during download |
| RPM chaining | After installing, the vault can automatically run remote commands |
| MEP-aware rules | Vaults with multiple active keys handle rules differently |
| Manufacturer certificates | Devices can restrict which Key Makers are trusted |
| Service Provider messages | Carriers can show you custom messages during download |

---

## What If Something Goes Wrong? ⚠️

The delivery system is built to handle failures gracefully:

- **Temporary errors** (out of memory, interruption): Retry the download — the vault can pick up where it left off
- **Permanent errors** (wrong EID, bad certificate): The profile moves to Error state, the carrier is notified
- **Too many tries**: If you enter the wrong Confirmation Code too many times, the profile locks out
- **Power loss**: The vault writes the installation result to permanent memory before reporting — so it always knows whether the key was installed or not

---

## 🧠 Did You Know?

The Key Maker can pre-generate thousands of protected profiles in advance using random encryption keys — without knowing which vault will receive them! When you show up with your claim ticket, the Key Maker binds the pre-made key to YOUR specific vault in seconds. It's like having a warehouse full of wrapped gifts, and the wrapping paper only sticks to the right person when they arrive.

---

*Kid-friendly version of GSMA SGP.22 v3.x, Section 3.1 — Profile Download and Installation*

← [Back to Kids Articles](index)
