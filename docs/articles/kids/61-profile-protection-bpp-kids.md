---
title: "The Unbreakable Envelope"
date: 2026-06-07
---

# The Unbreakable Envelope ✉️🔒

## Imagine...

You need to send your house key across the internet. The internet is full of snoops, thieves, and nosy neighbours. How do you make sure ONLY the right person can get that key?

You don't just put it in a plain envelope. You put it in a **titanium box**, lock it with a padlock that only the recipient has the key to, wrap THAT in another layer of armour, and send it through an underground tunnel. Even if someone grabs the package mid-transit, they get nothing but gibberish.

That's how **Profile Protection** works. When the Key Maker sends your eSIM profile to your phone, it goes through four layers of protection: and only YOUR magic vault chip can unwrap it.

---

## The Four Layers of Protection 🧅

Every profile passes through four stages before it lives safely in your vault:

| Stage | Name | What Happens |
|---|---|---|
| 1 | **UPP** : Unprotected | The raw key, like a blueprint. Never leaves the Key Maker's workshop. |
| 2 | **PPP** : Protected | Wrapped in encryption: scrambled with a secret code. |
| 3 | **BPP** : Bound | Locked to YOUR vault: a special handshake ensures only your chip can unlock it. |
| 4 | **SBPP** : Segmented | Chopped into tiny pieces (255 bytes) to fit through the narrow pipe to your vault. |

---

## The Secret Handshake 🤝

At the heart of the protection is a mathematical magic trick called **key agreement**:

1. Your vault creates a one-time key pair: public (shareable) and private (top secret)
2. The Key Maker creates its own one-time key pair
3. They exchange public keys
4. Using clever math (Elliptic Curve Diffie-Hellman), both sides independently calculate the SAME shared secret
5. This shared secret becomes the encryption key: nobody watching the exchange can figure it out!

It's like two people mixing paint: each starts with a secret colour, adds a public colour, exchanges, then adds their secret colour again. Both end up with the same final colour: but an observer only saw the public mixes.

---

## Two Locking Strategies 🔐

| Strategy | How It Works | Best For |
|---|---|---|
| **Lock on Demand** | Key Maker encrypts just-in-time using your session keys | One-off profiles |
| **Pre-Locked** | Key Maker bulk-produces protected profiles with random keys, wraps them in your session later | Scalability: thousands of profiles |

---

## What's Inside the Bound Package? 📦

| Section | Protection | Purpose |
|---|---|---|
| **Key Agreement** | Clear text (but signed) | Agree on the shared secret |
| **Configure ISD-P** | Encrypted + MAC | Create a new locked room in the vault |
| **Store Metadata** | MAC only | Label: profile name, icon, rules (vault reads without decrypting) |
| **Replace Session Keys** | Encrypted + MAC | Swap to profile's own dedicated keys |
| **Profile Elements** | Encrypted + MAC | The actual secret key: NAA, file system, applets |

---

## The Unforgeable Receipt ✍️

After installation, the vault signs a **Profile Installation Result** : cryptographic proof of what happened. The vault's unique signature confirms the outcome, the transaction ID, and whether installation succeeded or failed. Even if the phone loses power, the result is saved to permanent memory. No "he said, she said" : the carrier knows with mathematical certainty what happened.

---

The encryption has **Perfect Forward Secrecy**. That means even if someone steals the vault's long-term master key years later, they STILL can't decrypt profiles downloaded in the past. Each download session creates fresh, disposable keys destroyed right after use. It's like burning the envelope after reading the letter!

---

*Kid-friendly version of GSMA SGP.22 v3.x, Sections 2.5 and 2.6.4: Profile Protection and BPP Security Protocol*

← [Back to Kids Articles](index)
