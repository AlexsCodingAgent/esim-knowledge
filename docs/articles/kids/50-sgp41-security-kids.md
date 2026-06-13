---
description: "How SGP.41 treats the factory floor as an untrusted courier: plain keys exist only inside the certified vault and the eSIM chip, with everything in between encrypted and unreadable."
title: "Factory Secrets: How Keys Stay Safe on the Assembly Line"
date: 2026-06-07
---

# Factory Secrets: How Keys Stay Safe on the Assembly Line 🔒🏭

## Imagine...

You're mailing a priceless diamond necklace to a jewellery shop. You don't just toss it in an envelope: you lock it in a titanium box, seal it with a code only the shop owner knows, and send it through a courier who can't possibly open it. Even if the courier goes rogue, the necklace stays safe.

That's the security philosophy of SGP.41: **the factory is a courier, not a custodian**. The factory handles key packages all day long: but it can never see what's inside.

---

## The Golden Rule: Factory = Untrusted 👀

SGP.41 starts from one blunt principle: factory floors are not secure enough to hold secrets. Assembly line workers, production-line computers, even the Factory Robot: none of them should ever see a real key in plain form.

Two hard rules enforce this:

| Rule | What It Means |
|---|---|
| **GENS09** | Plain keys exist *only* inside the chip: nowhere else in the factory |
| **GENS10** | The factory never gets the secret keys used for locking profiles |

---

## Where Does the Key Actually Live? 🗺️

```
Key Maker's Vault (HSM)         Factory (untrusted)            eSIM Chip
─────────────────────         ────────────────────           ──────────
[Plain Key]                      [Locked Package]            [Plain Key]
     │                                │                          ▲
     ├─ Encrypt to eSIM's            ├─ Push through Robot       │
     │  one-time key                 │  (cannot unlock)          │
     │                                │                          │
     ├─ Sign with Key Maker's        ├─ Store in warehouse      ├─ Unlock with
     │  private key                  │  (cannot unlock)          │  one-time private key
     │                                │                          │
     └─ Package and ship ───────────▶├─ Load onto chip ────────▶├─ Verify signature
                                                                │
                                                                └─ Key installed!
```

The key exists in **plain form at exactly two places**: inside the Key Maker's SAS-certified vault, and inside the eSIM chip after installation. At every point in between: in transit, in storage, on the assembly line: it's a locked, scrambled, unreadable package.

---

## One-Time Keys: The Secret Weapon 🔑

The foundation of IFPP security is the **one-time key**. Think of it as a disposable, single-use padlock:

1. **Born in a secure vault**: One-time keys are created during chip manufacturing in a SAS-UP certified environment: like being born in a hospital with armed guards.

2. **One key, one profile**: Each key can lock exactly **one** profile. After use, it's destroyed. This prevents cloning: a profile locked to Chip A's key can never be installed on Chip B.

3. **Private key never leaves the chip**: The secret part stays buried in the eSIM forever. Only the public part (like a lock's serial number) is shared.

4. **No long-term correlation**: Because each key is used once, stealing one locked package tells you nothing about other packages for the same chip.

---

## What the Factory Does NOT Need 🚫

This is the best part for manufacturers:

| They DON'T Need | Why Not? |
|---|---|
| **SAS Accreditation** | All security work happens at the Key Maker: the factory just moves locked boxes |
| **An HSM (Hardware Security Module)** | The factory never holds secret keys, so there's nothing for an HSM to protect |

These two options (**GENS01** and **GENS02**) mean a high-volume IoT factory making cheap sensors doesn't need expensive security certification or special tamper-proof hardware. They just pass through encrypted packages.

---

## Perfect Forward Secrecy ⏪🔒

SGP.41 requires **Perfect Forward Secrecy (PFS)** for every profile binding. Here's what that means:

- Even if someone steals the Key Maker's master key **in the future**, all the old locked packages from **the past** stay safe
- Each binding uses fresh, temporary key material that's thrown away immediately after use
- Combined with one-time keys, you get "double forward secrecy" : neither the Key Maker's long-term key nor one chip's one-time key can compromise anything else

It's like using a brand-new padlock for every single delivery, then melting the key.

---

## Locking the Factory Door After Hours 🚪

Two clever controls prevent post-factory attacks:

- **FPA Services lock after production** (GENS13): The factory-only interface on the chip permanently deactivates when the device leaves the factory. No back door!

- **Field services blocked during factory mode** (EUICCF04): While one-time keys remain on the chip, normal eSIM management is blocked: and vice versa. The factory phase and the consumer phase can never overlap.

---

If someone on the assembly line copied a locked key package and tried to install it on a different chip, it would fail instantly. The one-time key binding means the package is cryptographically tied to one specific chip's private key. It's like a lock that only opens for one specific key in the entire universe!

---

*Kid-friendly version of GSMA SGP.41 v1.0: IFPP Security, Sections 4.2 and Annex B*

← [Back to Kids Articles](index)
