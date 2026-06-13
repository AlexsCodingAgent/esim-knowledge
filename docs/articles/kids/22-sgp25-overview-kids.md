---
description: "SGP.25 is the security rulebook every eUICC chip must meet: a Common Criteria Protection Profile that defines how tough the vault must be to host multiple operator profiles safely."
title: "The Vault's Security Rulebook: How Tough Is Tough Enough?"
date: 2026-06-07
---

# The Vault's Security Rulebook: How Tough Is Tough Enough? 📜

## Imagine...

You're building a bank vault to store the world's most valuable treasures. You could make it out of cardboard (cheap, easy, useless), steel (better), or reinforced titanium with laser sensors (the real deal). But how do you *prove* it's secure? You follow a **rulebook** : a checklist written by security experts that says exactly how tough the vault must be.

For eSIM chips, that rulebook is **SGP.25** : the GSMA's Protection Profile. It's the official security standard that every eUICC chip must meet before it can hold real operator profiles. Not "should meet" : **must meet**.

---

## What Is a Protection Profile? 📖

A **Protection Profile** (PP for short) is like a building code for digital security:

| Concept | Building Analogy | eSIM Equivalent |
|---------|-----------------|-----------------|
| **Protection Profile** | National building code | SGP.25: security rules for all eUICCs |
| **Security Target** | Architect's plans for one building | Vendor's plan for their specific chip |
| **Target of Evaluation** | The actual building being inspected | The eUICC software being evaluated |
| **Evaluation Level** | Inspection rigour (visual check vs. stress test) | EAL4+ : the highest practical level |

Protection Profiles are part of an international system called **Common Criteria** (ISO/IEC 15408). It's used by 31 countries that mutually recognise each other's security certificates. So a chip certified in Germany is trusted in Japan, Brazil, and Australia.

---

## Why eSIM Chips Need Their Own Rulebook 🎯

A normal SIM card is simple: one carrier, installed at the factory, never changes. An eUICC is different:

- 🏠 Hosts **multiple** operator profiles at the same time
- 📡 Accepts profiles downloaded **over the air** : from servers it's never met
- 🔐 Stores **long-lived secret keys** that must survive 10+ years
- 🌍 Deployed in **hostile environments** : phones in pockets, sensors in fields, trackers on trucks

An attacker with physical access to the chip could try to extract keys, clone the eUICC, or switch profiles without permission. SGP.25's job is to make sure the chip is built to resist all of that.

---

## What Gets Evaluated: The TOE 🏗️

SGP.25 evaluates the **eUICC software** : specifically:

### Application Layer (The Brain)

| Component | Job |
|-----------|-----|
| **ISD-R** | Profile life-cycle manager: creates, enables, disables, deletes profiles |
| **ECASD** | Secret keeper: holds private keys, certificates, and the eSIM CA public key |
| **ISD-P** | Profile container: each profile lives in its own locked room |

### Platform Layer (The Support Crew)

| Component | Job |
|-----------|-----|
| **Telecom Framework** | Network authentication (3G/4G/5G algorithms) |
| **Profile Package Interpreter** | Translates downloaded packages into installed profiles |
| **Profile Rules Enforcer** | Makes sure nobody breaks the rules |

The physical chip hardware is evaluated separately (under its own Protection Profile). SGP.25 focuses on the software that runs on top.

---

## The Modular Rulebook 📚

SGP.25 isn't one-size-fits-all. It uses a modular approach:

| Module | Covers |
|--------|--------|
| **Base-PP** | Core eUICC security: required for everyone |
| **LPAe Module** | Extra rules when the phone's helper app lives inside the chip |
| **IPAe Module** | Extra rules when the IoT robot's helper lives inside the chip |
| **Dual Module** | Rules for chips that support BOTH consumer and IoT |

Plus a mandatory **OS Update Module** if the chip supports remote software updates. This modularity means the rulebook scales from a basic consumer eSIM to a dual-purpose IoT+consumer powerhouse.

---

## The Threat Landscape: What Are We Afraid Of? ⚠️

SGP.25 defines threats in two tiers:

### First-Level Threats (Logical Attacks)

- 👤 **Imposters** : Unauthorised actors trying to manage profiles or modify platform functions
- 🎭 **Identity tampering** : Changing who the chip thinks it is
- 🧬 **Cloning** : Copying a legitimate profile onto a fake chip
- 🎪 **LPA impersonation** : Pretending to be the phone's eSIM assistant
- 📶 **Network theft** : Stealing access to mobile networks

### Second-Level Threats (Physical Attacks)

- 🔬 **Side-channel analysis** : Extracting keys by measuring power consumption
- ⚡ **Fault injection** : Flipping bits with voltage spikes or lasers
- 🔧 **Physical tampering** : Probing internal buses and memory

---

## EAL4+: The Toughness Rating 💪

SGP.25 requires **EAL4 augmented** : the highest practical level for a commercial product:

```
EAL4+ = EAL4 + ALC_DVS.2 + AVA_VAN.5
```

| Component | What It Means |
|-----------|---------------|
| **EAL4** | Methodically designed, tested, and reviewed. Source code examined by evaluators. |
| **ALC_DVS.2** | The development environment itself must be secure: physical, procedural, and personnel controls |
| **AVA_VAN.5** | Advanced penetration testing by experts with elevated attack potential |

EAL1 is a quick check. EAL7 is for military satellites. EAL4+ is the sweet spot for commercial products that need real security without infinite cost.

---

The "augmented" in EAL4+ is crucial. Standard EAL4 only requires basic vulnerability analysis. AVA_VAN.5 means evaluators actively try to break the chip using the same techniques real attackers would use: power analysis, fault injection, and protocol attacks. It's the difference between checking the vault door looks solid and actually trying to drill through it!

---

*Kid-friendly version of GSMA SGP.25 v2.1: eUICC Common Criteria Protection Profile*

← [Back to Kids Articles](index)
