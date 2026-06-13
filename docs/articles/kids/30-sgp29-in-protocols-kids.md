---
description: "Where the EID appears across eSIM protocols: from discovery service lookups and profile matching to the mutual handshake that proves a chip's identity before any secret key is delivered."
title: "Show Your ID! How Chips Prove Who They Are"
date: 2026-06-07
---

# Show Your ID! How Chips Prove Who They Are 🪪📡

## Imagine...

You walk up to a hotel front desk. "I have a reservation," you say. The clerk asks: "What's your name?" You tell them, they look it up, and: yes! : a room is waiting. Then they ask for your ID to prove you really are that person before handing over the key.

That's exactly how the EID works in eSIM protocols: showing your ID card to prove who you are. The EID is how eSIM chips announce themselves, get matched to waiting profiles, and prove their identity before receiving secret keys.

---

## Where the EID Shows Up 🗺️

The EID appears in at least four major operations across the eSIM world:

### 1. 🔍 Discovery Service: "Any Mail for Me?"

The **SM-DS** (Subscription Manager Discovery Service) is like a post office for eSIM profiles. Here's how it works:

```
1. Carrier prepares a profile for your chip → registers it with SM-DS using your EID
2. Your device asks SM-DS: "Anything waiting for EID 12345...?"
3. SM-DS looks up the EID: "Yes! A profile from carrier XYZ is ready!"
4. Your device goes to download it
```

Without the EID, the post office wouldn't know which pigeonhole belongs to which chip!

---

### 2. 📡 ES11 Polling: "Checking In!"

The **ES11** interface is how the helper app on your device (the LPA) checks for waiting profiles:

```
LPA → SM-DS: "Any pending events for EID 12345...00133?"
SM-DS → LPA: "Yes → download from dp.example.com"
```

The EID is the primary lookup key in every ES11 query. The helper app polls periodically (or when you open the eSIM settings), always using the EID as the identifier.

---

### 3. 🔐 ES8+ Download: The Mutual Handshake

This is where the EID becomes a security anchor. Before any profile is delivered, the chip and the Key Maker do a two-way identity check:

| Step | What Happens |
|---|---|
| **Key Maker → Chip** | "I have a key for EID 12345... : is that you?" |
| **Chip verifies** | "Is this Key Maker's certificate valid? Is this key really for me?" |
| **Chip → Key Maker** | "Yes, I am EID 12345... Here's my cryptographic proof!" |
| **Key Maker verifies** | "Does the EID match? Is the certificate valid? Is the signature correct?" |
| **Key Maker → Chip** | "Confirmed! Here's your encrypted key package!" |

The EID is the name on both sides of this handshake. It's how the chip claims its identity, and how the Key Maker confirms it's talking to the right chip.

---

### 4. 📨 Event Registration: "Tell Me When It's Ready!"

Sometimes a profile isn't ready immediately. The Key Maker can register an event:

```
Key Maker → SM-DS: "Register: when EID 12345... checks in,
                    tell them a profile is ready at dp.example.com"
```

The next time that chip polls the SM-DS, the waiting event appears. The EID is the link between the event and the chip.

---

## Across Different eSIM Worlds 🌐

The EID is universal: it works across all major eSIM specifications:

| Specification | How EID Is Used |
|---|---|
| **SGP.22 (Consumer)** | ES8+ downloads, ES11 polling, SM-DS discovery: your phone's eSIM |
| **SGP.32 (IoT)** | Same pattern, but for smart sensors, meters, and trackers |
| **SGP.02 (M2M)** | Profile download and management for machine-to-machine devices |

Same EID format, same rules, different device types. That's the beauty of a universal identifier!

---

## Why Uniqueness Matters (A Lot!) ⚠️

SGP.29 Principle **EID.P02** demands global EID uniqueness. Here's what would happen if two chips shared the same EID:

| Scenario | Disaster |
|---|---|
| **Wrong profile delivery** | Chip B receives a profile meant for Chip A: potentially giving an attacker access to someone else's mobile plan |
| **SM-DS confusion** | The Discovery Service can't tell which chip should get which profile |
| **Authentication failure** | Cryptographic handshakes fail because the Key Maker can't distinguish between two chips claiming the same identity |

Global uniqueness is not optional: it's the foundation everything else rests on!

---

When your eSIM helper app polls the SM-DS for pending profiles, it does so using your chip's real EID: but the connection is encrypted, and the SM-DS requires authentication. Knowing someone's EID alone isn't enough to steal their profiles. The EID is a *claim* of identity, but the cryptographic proof (the chip's private key) is what actually *proves* it!

---

*Kid-friendly version of GSMA SGP.29 v1.1: EID in RSP Protocols, Section 6*

← [Back to Kids Articles](index)
