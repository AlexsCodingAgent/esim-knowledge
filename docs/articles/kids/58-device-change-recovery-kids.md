---
description: "Moving eSIM profiles to a new phone without calling your carrier — SGP.22 v3's Device Change standardises the process, with a built-in safety net so keys are never lost."
title: "Moving Your Secret Keys to a New Vault"
date: 2026-06-07
---

# Moving Your Secret Keys to a New Vault 🏠➡️🏠

## Imagine...

You're moving house. You've got a keychain full of important keys: your front door key, your office key, your safety deposit box key. You can't just leave copies lying around. You need to pack them up securely, lock them in a special briefcase, and hand-deliver them to your new home.

That's exactly what **Device Change** does for your eSIM profiles! When you get a new phone, it moves your secret digital keys from your old magic vault to your new one: safely, securely, and without losing anything along the way.

---

## The Old Way vs The New Way 📱

| Old Way (Before v3.x) | New Way (v3.x Device Change) |
|---|---|
| Call your carrier and ask for a new QR code | Tap a few buttons on your old phone |
| Wait on hold, explain your situation | Your phone talks to the Key Maker automatically |
| Each manufacturer does it differently | One standard way that works the same everywhere |
| If something goes wrong, you lose your keys forever | Built-in safety net: Profile Recovery! |

---

## The Two Ways to Move 🔑

There are two ways to pack up your secret keys:

### The Full-Service Move: `requestToDp`

Like hiring professional movers:

1. You tell your old phone: "I'm moving to a new vault!"
2. Your phone calls the **Key Maker** (SM-DP+) and says: "We're moving house"
3. The Key Maker checks in with your mobile company: "Is this move okay?"
4. The company might give you a brand new key, or let you reuse your old one
5. You confirm: "Yes, I really want to do this" (Strong Confirmation)
6. The old vault deletes your key and creates a special moving receipt
7. That receipt becomes a QR code for your new phone
8. Your new phone downloads the key fresh: ready to go!

### The DIY Move: `usingStoredAc`

Like already having a spare key in an envelope marked "NEW HOUSE":

1. Your profile already has a pre-packed Activation Code stored inside
2. You trigger the move, the old profile gets deleted
3. You scan the stored code on your new phone
4. Done: quick and simple!

---

## What If Something Goes Wrong? 🆘

Imagine you've packed up all your keys, the movers have left... and the door of your new house won't open. Panic! You've already given up your old keys!

That's where **Profile Recovery** comes in: the safety net:

- Your old phone saves recovery information before deleting the profile
- If the new phone fails to install, you can go back to the old phone
- The Key Maker verifies: "Yep, the new vault didn't work: let's restore"
- A fresh download brings your key back to the old vault
- But hurry: the recovery ticket expires after a while!

It's like having a spare key hidden under the doormat, but only for a limited time.

---

## Who's Involved? 🦸

| Helper | Role in the Move |
|---|---|
| **Old Vault** (eUICC) | Packs up the keys, deletes them after safe transfer |
| **New Vault** (eUICC) | Receives and stores the fresh keys |
| **Key Maker** (SM-DP+) | Orchestrates the whole move, makes sure nobody steals the keys |
| **Your Assistant** (LPA) | Guides you through the process on both phones |
| **Your Carrier** | Approves the move, may issue a brand new key |

---

Device Change and Profile Recovery are **brand new in v3.x** : before this, every eSIM transfer was a different process depending on which phone you owned. Now it's one standardised, safe way to move all your secret keys to a new vault!

---

*Kid-friendly version of GSMA SGP.22 v3.x, Section 3.11: Device Change and Profile Recovery*

← [Back to Kids Articles](index)
