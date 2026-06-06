---
title: "The M2M Dream Team: Six Special Helpers"
date: 2026-06-07
---

# The M2M Dream Team: Six Special Helpers 🦸

## Imagine...

A giant robot factory needs six different specialists to keep 10,000 robots connected across the world. Not just anyone can do every job — each helper has one special role, and they all work together like a well-oiled machine.

In SGP.02, six special helpers make the entire robot fleet work. Let's meet the Dream Team!

---

## The Six Helpers 👥

### 🏭 The Chip Builder (EUM)
The **eUICC Manufacturer** builds the physical vault chip. They:
- Manufacture the tamper-proof hardware
- Install the robot's unique secret ID and private key
- Register every new robot with the Commander
- **Analogy:** The factory that builds the safe and sets the first combination

### 🏛️ The ID Authority (CI)
The **Certificate Issuer** is the root of all trust. They:
- Issue the master ID badge that all helpers trust
- Sign certificates for Chip Builders, Key Factories, and Commanders
- Publish "WANTED" lists for revoked badges
- **Analogy:** The government passport office — if they didn't sign your passport, nobody trusts it

### 🔑 The Key Factory (SM-DP)
The **Subscription Manager — Data Preparation** builds profiles. They:
- Craft secret keys locked to one specific robot
- Encrypt profiles so nobody can read them — not even the Commander
- Talk to the Fleet Owner (Operator) and the Commander (SM-SR)
- **Analogy:** A high-security key cutting shop that makes keys that only work in one specific lock

### 🦾 The Robot Fleet Commander (SM-SR)
The **Subscription Manager — Secure Routing** is the star of the show. They:
- Own the secret radio channel to every robot
- Store information about every robot's status (the EIS database)
- Push commands and relay encrypted keys
- Can hand over command to a new Commander if needed
- **Analogy:** Mission Control — the only one with the radio frequency to talk to the robots

### 📡 The Fleet Owner (Operator)
The **Mobile Network Operator** owns the profiles and subscriber relationships. They:
- Order new profiles from the Key Factory
- Decide when robots switch networks
- Manage their own OTA channel for post-install tweaks (ES6)
- **Analogy:** The company that owns the fleet and pays for connectivity

### 🚛 The Fleet Manager (M2M SP)
The **M2M Service Provider** manages fleets without owning the network. They:
- Handle day-to-day operations for the fleet
- Can enable/disable/delete profiles — with Operator permission
- Common in automotive: a car company managing telematics across countries
- **Analogy:** A logistics company that manages trucks but doesn't own the fuel stations

---

## The Commander is the Hub 🕸️

Notice something special? The Commander (SM-SR) connects to *everyone*:

- Chip Builder → Commander (ES1): "Here's a new robot!"
- Key Factory → Commander (ES3): "Deliver this key!"
- Fleet Owner → Commander (ES4): "Switch robot #8721 to network B!"
- Commander → Commander (ES7): "Handing over these 5000 robots to you!"

---

## M2M Team vs Consumer Team

| Role | Consumer (SGP.22) | M2M Robots (SGP.02) |
|---|---|---|
| Key Maker | SM-DP+ (combined role) | SM-DP + SM-SR (split) |
| On-Device Helper | LPA (app on phone) | None — ISD-R is passive |
| Notification | SM-DS post office | Commander handles everything |
| Fleet Manager | Not applicable | M2M SP |
| User Interface | QR codes, touch screen | Headless — no screen |

---

## 🧠 Did You Know?

The split between Key Factory (SM-DP) and Commander (SM-SR) is unique to SGP.02. In consumer eSIM, these are combined into one role (SM-DP+). But splitting them lets a fleet owner change Key Factories without changing Commanders — or switch Commanders without touching any keys!

---

*Kid-friendly version of GSMA SGP.02 v4.2 §2.1 — General Architecture*

← [Back to Kids Articles](index)
