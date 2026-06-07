---
description: "Follow the three-stage spy mission of downloading an eSIM profile: placing the order, the cryptographic handshake proving identities, and the encrypted key delivery."
title: "Mission: Download a Digital Key"
date: 2026-05-29
---

# Mission: Download a Digital Key 🕵️

## Imagine...

You've just bought an eSIM plan for your trip to Japan. You scan a QR code, and within seconds your phone has a brand new digital key. But what *actually* happened in those few seconds? It was a three-stage secret mission: and you were the spy master who launched it!

---

## Stage 1: The Order 📋

Before anything can happen, your carrier needs to prepare a key just for you.

Here's what happens behind the scenes:

1. You give your carrier your phone's **EID** (a 32-digit number unique to your chip: like its name tag)
2. The carrier calls the **Key Maker** server and says: "Build a key for this specific phone"
3. The Key Maker reserves a spot and creates a **Matching ID** : a secret codeword
4. That Matching ID gets baked into the QR code you scan
5. Optionally, a note gets left at the **Notifier** post office

The QR code is surprisingly simple. It looks something like this:
```
LPA:1$keymaker.example.com$SECRET-CODE-123
```

That's it! Just an address and a code. All the real security happens next.

---

## Stage 2: The Handshake 🤝

This is where the spy-movie stuff happens. Before the Key Maker hands over any secrets, both sides must prove who they are.

The **server goes first** : this is *very* important:

1. Your phone's Assistant asks the Vault chip for a **random challenge** (a big random number)
2. The Assistant sends this challenge to the Key Maker
3. The Key Maker signs the challenge with its secret key and sends back its ID badge
4. Your Vault chip checks the badge against the GSMA master key stored inside it
5. Only if the badge checks out does the Vault respond with its own signature

Now the Key Maker knows it's talking to a real chip, and your chip knows it's talking to a real Key Maker.

**Cool detail:** The Assistant app on your phone carries all these messages back and forth, but it can never read them. It's like a courier delivering sealed envelopes.

---

## Stage 3: The Delivery 📦

Now the real transfer begins. The Key Maker builds a special encrypted package called a **Bound Profile** : a key locked specifically to your chip.

The delivery uses a super-secure tunnel:
- The Key Maker and your Vault create **one-time secret codes** just for this conversation
- Every piece of the key is wrapped in layers of encryption
- The package is streamed in chunks, each one verified before the next arrives
- If anything goes wrong, the entire download is rolled back: no half-installed keys!

Inside the package are all the pieces of a working profile: network keys, a mini file system, and applets. The chip's **Profile Package Interpreter** unwraps each piece and builds the profile inside a new locked box (ISD-P).

When it's done, the profile is installed but **not yet active**. You have to flip the switch to turn it on!

---

## The Four Transformations 🔄

On its journey, the key goes through four stages:

1. **Raw ingredients** : the carrier's data, unprotected
2. **Wrapped up** : encrypted with profile-specific keys
3. **Locked to you** : cryptographically bound to your chip (useless anywhere else!)
4. **Chopped up** : split into tiny chunks for safe delivery

---

If you copy a Bound Profile from one phone and try to install it on another, it won't work! The encryption is tied to the original chip's unique secret. It's like a key that reshapes itself to fit only one lock: and that lock is inside your phone.

---

*Kid-friendly version of GSMA SGP.22, Section 3: Procedures*

← [Back to Kids Articles](index)
