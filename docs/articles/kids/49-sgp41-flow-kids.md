---
description: "The 16-step IFPP journey from carrier order to factory installation — how profiles get locked to specific chips in advance and pushed onto the assembly line without internet."
title: "From Factory Floor to Your Pocket"
date: 2026-06-07
---

# From Factory Floor to Your Pocket 🏭➡️👖

## Imagine...

You're building a treasure chest. First, you build the wooden box: strong hinges, a sturdy lock, a velvet interior. That's the **Manufacturing Step**. Then, when a customer orders one, you place a specific treasure inside and lock it with a unique key only they can open. That's the **Configuration Step**.

SGP.41's entire flow follows this same two-phase pattern: build the vault, then fill it with keys.

---

## The 16-Step Journey 🗺️

The IFPP process has 16 steps, but they're grouped into five easy-to-understand phases. Let's follow a key from order to installation!

### Phase 1: 📋 Placing the Order

```
Carrier ──"I need 10,000 keys!"──▶ Factory Key Maker
```

**Step 1**: A mobile carrier calls up the Factory Key Maker (SM-DPf) and says: "I need profiles for a batch of new laptops!" The Key Maker can create all 10,000 at once (bulk generation) and lock them individually as needed.

---

### Phase 2: 📦 Shipping the Chips

**Step 2**: The Chip Maker (EUM) ships eSIM chips with pre-loaded one-time keys to the factory.

**Steps 3–4**: The chip's public data (its "ID card" : certificates, public keys, capabilities) gets sent to the Factory Key Maker. This can go directly from Chip Maker to Key Maker, or through the Factory Boss first.

Think of this as sending the locksmith a photo of your keyhole so they can cut the right key.

---

### Phase 3: 🔐 Making the Keys

```
Factory Boss ──"Lock keys for these chips"──▶ Key Maker
              [Key Maker creates locked packages]
Factory Boss ◀──"Here they are!"── Key Maker
```

**Step 5**: The Factory Boss requests locked profiles, including each chip's one-time public key (like sending the lock's serial number).

**Step 6**: Inside the Key Maker's vault, the magic happens: each profile is encrypted so only one specific chip can unlock it. This uses **Perfect Forward Secrecy** : even if someone later steals the Key Maker's master key, old packages stay safe.

**Step 7**: The locked packages are delivered to the factory. They can now sit in storage until needed: days, weeks, even months!

---

### Phase 4: 🏭 Loading on the Assembly Line

This is where it all comes together: and the best part: **no internet needed!**

```
Factory Boss ──"Load this!"──▶ Factory Robot ──"Receiving!"──▶ eSIM Chip
                                [Chip unlocks and installs]
Factory Boss ◀──"Done!"── Robot ◀──"Installed!"── eSIM Chip
```

**Step 8**: The Boss hands a locked key package to the Robot.

**Step 9**: The Robot pushes it into the eSIM chip over the special `ES10f` interface.

**Step 10**: Inside the chip, the profile is unlocked, verified, and installed. The one-time key is consumed: destroyed forever.

**Step 11–12**: The chip signs a receipt ("Profile Installation Result") and sends it back through the Robot to the Boss.

---

### Phase 5: 📊 Reporting Back (Optional)

**Steps 13–16**: The Factory Boss collects all the receipts, bundles them into a **Profile Loading Report**, and sends it to the Key Maker. The Key Maker verifies everything and tells the Carrier: "All 10,000 keys loaded successfully!"

---

## The Two-Phase Magic 🪄

| Phase | What Happens | Real-World Example |
|---|---|---|
| **Manufacturing Step** | Build generic hardware, put in stock | PC motherboards built in bulk in Asia |
| **Configuration Step** | Pull from stock, load customer-specific keys, ship | Laptop gets a European carrier profile before shipping to Germany |

This split is incredibly powerful. A factory can build 5 million generic devices, store them, and only add country-specific keys when they know where each device is going. Without SGP.41, they'd need separate production lines for every country!

---

## Flexible Like a Yoga Master 🧘

The IFPP flow is designed for real factory chaos:

- **Steps can be reordered**: Chips can arrive after keys are already prepared. The Key Maker can generate profiles in bulk but lock them in smaller batches.
- **Multiple keys per chip**: Repeat the whole process to load keys from different carriers onto the same chip: a "Home" key and a "Travel" key, both pre-loaded!
- **Multiple Key Makers**: One factory can work with many carriers, each with their own Key Maker.

---

Steps 8–12 (the actual factory-floor loading) can happen in milliseconds: a single push, no network round-trips, no waiting. That's why IFPP works at the speed of a production line, where every second counts!

---

*Kid-friendly version of GSMA SGP.41 v1.0: IFPP Flow, Section 5.1 and Annex A*

← [Back to Kids Articles](index)
