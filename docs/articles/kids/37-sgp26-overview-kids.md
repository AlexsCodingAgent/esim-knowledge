---
title: "Practice ID Badges: The Test Certificate System"
date: 2026-06-07
---

# Practice ID Badges: The Test Certificate System 🎭

## Imagine...

You're designing a new security badge system for a giant company. Before printing real badges that open actual doors, you need to test everything. But you can't use *real* badges: real badges unlock real doors! So you print special **practice badges** instead. They look exactly like real badges, with the same holograms and barcodes, but they all have the word **"TEST"** stamped across them in big red letters.

That's exactly what **SGP.26 Test Certificates** are for the eSIM world: practice ID badges for the testing lab.

---

## Real Badges vs Practice Badges 🪪

When your phone downloads an eSIM profile, everyone shows digital ID badges (certificates) to prove who they are. Real badges are locked in super-secure vaults. Nobody can peek at them: which makes testing impossible!

SGP.26 solves this by creating a complete set of practice badges:

| Real Badges (Production) | Practice Badges (SGP.26 Test) |
|---|---|
| Secret private keys in vaults | Private keys published openly |
| Real company names | Placeholder names like "RSPTEST" |
| Guarded by security teams | Anyone can download and use |
| Must never leave the vault | Shared in a ZIP file with the spec |
| Valid for real door-opening | Only valid in the testing lab |

---

## What's in the Practice Badge Kit? 🎒

The SGP.26 practice kit comes with badges for every helper in the eSIM ecosystem:

- 🏛️ **The Grandparent Badge** : the GSMA Test CI root, the ultimate trust anchor
- 🏭 **The Factory Badge** : the eUICC Manufacturer (EUM) certificate
- 📱 **The Phone Badge** : the eUICC certificate for the chip in your phone
- 🔑 **The Key Maker Badges** : SM-DP+ certificates (three flavours: authentication, profile binding, and TLS)
- 📬 **The Post Office Badges** : SM-DS certificates for discovery services
- 🤖 **The Robot Badges** : eIM certificates for IoT device management

Every kit also includes all the private keys: the secret codes that make each badge work. In the *real* world, these secrets are locked away forever. In the practice kit, they're right there for anyone to inspect and use!

---

## Why We Need Practice Badges 🧪

Think about what happens without them. You're building a new eSIM phone and want to make sure it can verify badges correctly. But you can't get real badges: they're controlled by a security company (the GSMA Certificate Issuer) that keeps them in a vault.

With SGP.26, you get a parallel universe of badges. Same shapes, same holograms, same barcodes: but all stamped "TEST." Now you can:

- **Test your phone's badge-checker** without risking real credentials
- **Make sure all helpers can talk to each other** using badges they all recognise
- **Test broken badges on purpose** : bent corners, wrong holograms, expired dates: to make sure your phone rejects them properly

---

## The Golden Rule: Never Take Practice Badges Outside 📛

There's one absolutely unbreakable rule: **practice badges must never appear in a real phone sold to customers.**

Why? Because the practice badges' secret codes are publicly known. A real phone loaded with practice badges would trust *anyone* who has those codes: which is everyone! It's like leaving your house keys under a mat labelled "KEYS HERE."

The spec says it clearly: test certificates *SHALL NOT* be present in any commercial RSP product in its operational lifecycle.

---

## Five Flavours of Practice Badge Families 🍦

Not all practice badge families look the same. SGP.26 defines five variants (O, Ov3, A, B, C) that mirror different real-world setups:

- **Variant O** : The simplest. Grandpa CI signs everyone directly. No middle layers.
- **Variant B** : Grandpa delegates to a Parent (CI SubCA), who signs everyone else.
- **Variant A** : Grandpa signs three specialist Parents: one for the Factory, one for the Key Maker, one for the Post Office.
- **Variant C** : The deepest family: Grandpa → Parent → Specialist Parents → Children.
- **Variant Ov3** : Like the others but using a newer version of the badge design rules.

Each variant tests different badge-checking logic: just like different real companies organise their badge systems differently.

---

The SGP.26 package ships as a ZIP file containing everything: private keys, public certificates, CRL "WANTED" posters, and even the recipe files (OpenSSL configurations) for baking fresh badges yourself. It's the complete testing lab in a box!

---

*Kid-friendly version of GSMA SGP.26: RSP Test Certificates Definition*

← [Back to Kids Articles](index)
