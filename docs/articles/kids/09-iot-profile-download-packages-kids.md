---
title: "IoT Profile Download: Direct, Indirect, and eIM Package Handling"
date: 2026-05-29
---

# 📦 How Robot SIM Cards Get Their Permission Slips

**Imagine...** you're at school and you need a permission slip to go on a field trip. You could get it two ways: your teacher hands it to you directly, or your parent picks it up from the office and brings it to you. IoT devices get their "permission slips" (called **profiles**) the exact same way — directly or indirectly!

---

## 🏃 Direct Download — The Device Gets It Itself

In **Direct Download**, the device's translator (IPA) talks straight to the **profile factory** (SM-DP+). The remote control centre just says "go get it!" and sends a **secret code** (Activation Code) to kick things off.

No QR codes, no cameras, no humans — the code arrives through the air. The translator does all the work, fetching the profile and installing it on the chip.

---

## 🚚 Indirect Download — The Control Centre Delivers

Sometimes the device can't reach the profile factory — maybe it's on a super-slow network, or it doesn't have full internet access. In **Indirect Download**, the remote control centre (eIM) handles everything:

1. Control centre fetches the profile from the factory
2. Control centre securely packages it
3. Control centre delivers it to the device translator
4. Translator feeds it to the chip

The device never talks to the factory at all! It's like having a friend pick up your parcel because you can't leave the house.

---

## ✉️ The Signed Command Package

Here's the cleverest part. Instead of sending commands one at a time (like "enable this profile," "disable that one"), the control centre bundles everything into one **signed digital envelope** called an **eIM Package**.

The package contains:
- A list of actions: enable a profile, disable it, delete it
- A **digital signature** — like a wax seal proving it's genuine
- An **anti-replay counter** — so old commands can't be replayed by bad actors

When the chip receives the package, it:
1. Checks the signature against the control centre's stored key 🗝️
2. Verifies the counter hasn't been used before 🧮
3. Executes every command inside ✅
4. Creates a **signed result** proving it did everything correctly 📜

---

## 🛡️ Replay Protection — No Cheating!

Every package has a **counter value** (like a ticket number) that only goes up. The chip remembers the highest number it's seen. If someone tries to replay an old package with a lower number, the chip says "Nope, I've already seen this!" and rejects it.

---

## 📋 In a Nutshell

- **Direct download**: device fetches its own permission slip
- **Indirect download**: control centre delivers it
- **eIM Packages** bundle multiple commands into one signed envelope
- **Counters** prevent old commands from being replayed

---

🧠 **Did You Know?** The counter can go all the way up to 8,388,607 — that's enough for 800 operations *every single day* for 28 years without running out!

← [Back to Kids Articles](index)
