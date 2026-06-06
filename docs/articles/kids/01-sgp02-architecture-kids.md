---
title: "The M2M Dream Team: Six Special Helpers"
date: 2026-06-07
---

# The M2M Dream Team: Six Special Helpers 🦸

A city doesn't run on one person. You need the power company, the water authority, the road crews, the building inspectors: each with their own job, none of them doing anyone else's. If the water guys tried to rewire a substation, you'd have a very bad day.

SGP.02 works the same way. Six separate roles keep the whole machine-to-machine ecosystem humming. No single player does everything, and that's by design. Let's meet them.

---

## The lineup

**🏭 The Chip Builder (EUM: eUICC Manufacturer)**
Before anything else happens, someone has to build the actual chip. The EUM manufactures the tamper-proof hardware and installs the device's unique secret identity: a private key generated right on the silicon, never leaving it. Every new chip gets registered with the Commander so the fleet knows it exists. The EUM is the factory that builds the safe and sets the first combination.

**🏛️ The ID Authority (CI: Certificate Issuer)**
If nobody can verify who's who, the whole system collapses. The CI is the root of all trust: the organisation that issues the master ID badges everyone else's credentials trace back to. It signs certificates for Chip Builders, Key Factories, and Commanders. It also publishes revocation lists when a badge goes bad. Think of it as the passport office: if they didn't sign your passport, border control doesn't let you through.

**🔑 The Key Factory (SM-DP: Subscription Manager Data Preparation)**
When the fleet owner needs new profiles, this is who builds them. The SM-DP crafts secret keys locked to one specific device, encrypts them so thoroughly that not even the Commander can peek, and coordinates delivery through the Commander's secure channel. It's a high-security locksmith: cutting keys that only work in one specific lock, then sealing them in an envelope the courier can't open.

**🦾 The Commander (SM-SR: Subscription Manager Secure Routing)**
The star of the show. The Commander owns the secret radio channel to every device in the fleet. It maintains the EIS database (a roster of every device, its status, and its current network), pushes commands, relays encrypted keys from the Key Factory, and can hand over an entire fleet to a new Commander if required. Everything flows through the Commander. It's the hub.

**📡 The Fleet Owner (Operator: Mobile Network Operator)**
The Operator owns the profiles and the subscriber relationships. They order new keys from the Key Factory and decide when devices switch networks. After a profile is installed, the Operator maintains their own direct channel (ES6) for tweaks and updates, completely separate from the Commander's delivery channel.

**🚛 The Fleet Manager (M2M SP: M2M Service Provider)**
Not every company that runs a device fleet also owns a mobile network. Enter the M2M SP: a logistics partner who handles day-to-day operations without owning the cellular infrastructure. They can enable, disable, and delete profiles, but only with the Operator's permission. Common in automotive: a car company managing telematics across multiple countries, working through local Operators in each region. They manage the trucks but don't own the fuel stations.

---

## Everything runs through the Commander

Look at how the Commander sits at the centre:

- **Chip Builder → Commander (ES1):** "Here's a new device for the fleet!"
- **Key Factory → Commander (ES3):** "Deliver this encrypted key to Device #8721."
- **Fleet Owner → Commander (ES4):** "Switch Device #8721 to network B. Now."
- **Commander → Commander (ES7):** "I'm handing over these 5,000 devices to you, here are their records."

The Operator talks to the Key Factory directly (ES2) to order new profiles, and maintains their own post-install channel (ES6) to devices, but every command that touches the fleet runs through the Commander. That's the design: one control point, one radio frequency, one accountable party.

---

## Why split the Key Factory and Commander?

In consumer eSIM (SGP.22), these two roles are merged into one: the SM-DP+. SGP.02 keeps them separate, and that's a feature, not a bug.

Splitting them means a fleet owner can swap out their Key Factory without touching the Commander, or migrate to a new Commander without reissuing any keys. The roles are independent contracts. It's the difference between hiring one company to do everything and hiring specialists you can replace individually.

| Role | Consumer (SGP.22) | M2M (SGP.02) |
|---|---|---|
| Key Maker | SM-DP+ (combined) | SM-DP + SM-SR (split) |
| On-Device Helper | LPA (app on phone) | None, ISD-R is passive |
| Notification | SM-DS post office | Commander handles everything |
| Fleet Manager | Not applicable | M2M SP |
| User Interface | QR codes, touch screen | Headless: no screen |

---

*Kid-friendly version of GSMA SGP.02 v4.2 §2.1, General Architecture*

← [Back to Kids Articles](index)
