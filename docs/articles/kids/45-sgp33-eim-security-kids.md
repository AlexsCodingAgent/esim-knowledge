---
description: "The three security layers protecting IoT eSIM commands: encrypted tunnels, digital wax stamps, and anti-replay counters, and the SGP.33-3 tests that verify each one holds."
title: "Secret Codes and Signed Orders: Security Testing"
date: 2026-06-07
---

# Secret Codes and Signed Orders: Security Testing 🔐

## Imagine...

You're a general sending orders to troops in the field. If the enemy intercepts your message, they could cause chaos. So you use **sealed envelopes** with a **wax stamp** : only the right person can open it, and the stamp proves it really came from you. Any message without the stamp gets thrown away.

That's how the eIM protects its commands to IoT robots. Every order is wrapped in encryption, signed with a digital stamp, and protected against replay. SGP.33-3's security tests make sure these protections actually work.

---

## The Three Layers of Protection 🛡️

Mission Control's security has three layers:

| Layer | Technology | What It Prevents |
|-------|-----------|-----------------|
| **Encrypted Tunnels** | TLS v1.2 | Eavesdropping on messages in transit |
| **Signed Orders** | ECDSA signatures | Fake orders from imposters |
| **Anti-Replay Counters** | counterValue | Old orders being replayed |

Each layer gets its own set of test cases to verify it works under attack.

---

## Layer 1: Encrypted Tunnels (TLS) 🔒

Every connection between the eIM and other servers uses **TLS v1.2** : the same technology that puts the padlock icon in your browser. But in IoT eSIM, it works one-way:

> **Server Authentication mode**: The eIM verifies the server it's talking to, but doesn't prove its own identity with a client certificate. It's like calling a bank: you check it's really the bank, then prove who you are with your account details.

The test cases verify:

- ✅ The eIM establishes TLS connections with approved cipher suites
- ✅ It rejects servers with invalid certificates
- ✅ It rejects expired certificates
- ✅ It uses fresh encryption keys for every session (no key reuse!)

Two cipher suites are allowed:
- **Preferred**: TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 (the fancy one)
- **Fallback**: TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 (the backup)

---

## Layer 2: Signed Commands (Digital Wax Stamps) ✍️

Every order the eIM sends to a robot's vault is **cryptographically signed**. Here's what a signed order looks like:

```
Envelope {
    From: Mission Control #EIM_ID
    To: Robot Vault #EID1
    Counter: #42
    Order: "Enable Profile X"
}
Digital Signature: ✍️ [generated with eIM's private key]
```

The robot vault checks:
1. Is the signature valid? (Proves it came from the real eIM)
2. Is the counter higher than last time? (Prevents replay)
3. Is the order for this robot? (Prevents mix-ups)

Result packages flow back the same way: signed by the robot's vault to prove it really executed the order.

---

## Layer 3: Anti-Replay Protection 🔢

The **counterValue** is a simple but powerful idea. Every time the eIM sends an order, it increments a counter by one:

| Order | counterValue |
|-------|-------------|
| First order ever | 1 |
| Second order | 2 |
| Third order | 3 |
| ...and so on | 4, 5, 6... |

The robot vault remembers the last counter it saw from each Mission Control. If an attacker captures an old order and tries to replay it:

> "Order #2 again? No thanks: I already did that one!"

This prevents **replay attacks** where someone records a legitimate command and sends it again later to cause trouble.

---

## The Certificate Family Tree 🌳

Trust in the eSIM world works like a family tree of digital ID cards:

```
eSIM Certificate Authority (CI)
    │  "I vouch for this manufacturer"
    ▼
EUM Certificate
    │  "I vouch for this chip"
    ▼
eUICC Certificate
    │  "I am this specific chip"
    ▼
Robot Vault
```

Test cases verify that the eIM correctly validates this whole chain:

- ❌ Invalid EUM certificate → rejected!
- ❌ Expired eUICC certificate → rejected!
- ❌ Wrong Certificate Issuer → rejected!
- ✅ Valid chain → accepted!

---

## Special Case: ESipa Server Auth 🎭

On the ESipa interface (eIM talking to the robot's translator), the roles flip:

> The eIM acts as the **TLS server** and presents its own certificate (called the "Variant O certificate"). The robot's translator authenticates *the eIM* before accepting commands.

This is like the difference between calling customer service (you verify them) versus receiving a delivery (the courier verifies you). The test cases make sure the eIM can play both roles correctly.

---

Notifications about profile changes are also signed: by the robot vault itself. They include the full certificate chain (eUICC + EUM certificates) along with the signature, so the Key Maker can verify them without needing any pre-loaded information about that specific chip. It's like including your photo ID along with your signature!

---

*Kid-friendly version of GSMA SGP.33-3: eUICC IoT Manager Test Specification, Security Testing*

← [Back to Kids Articles](index)
