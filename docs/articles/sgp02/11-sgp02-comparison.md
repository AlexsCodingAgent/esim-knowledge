---
description: "Compares the three GSMA eSIM specifications : SGP.02 push for M2M, SGP.22 pull for consumer devices, and SGP.32 for IoT orchestration : highlighting provisioning models, device requirements, and deployment trade-offs."
date: 2026-06-07
layout: default
title: "SGP.02 vs SGP.22 vs SGP.32: Push, Pull, and the Evolution of eSIM"
---

# SGP.02 vs SGP.22 vs SGP.32: Push, Pull, and the Evolution of eSIM

**[eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > SGP.02 vs SGP.22 vs SGP.32: Push, Pull, and the Evolution of eSIM**

You're standing in front of a whiteboard with three boxes labeled SGP.02, SGP.22, and SGP.32. Someone (your boss, your architect, your client) wants to know which one to use. And if you get this wrong, the cost isn't a code refactor. It's 10,000 truck rolls in year five when your fleet needs to switch operators and every device needs a technician visit because you picked a pull architecture for a device that can't pull.

So let's get this right.

The GSMA has published three major eSIM specifications. They weren't designed as v1, v2, v3 of the same thing; each targets a fundamentally different class of device, and they answer the central question differently: **who initiates profile provisioning?**

- **SGP.02** says the server does. A push model, written for headless meters, automotive telematics, industrial sensors: devices nobody touches for a decade.
- **SGP.22** says the user does. A pull model, built for smartphones. QR codes, touch screens, end-user choice.
- **SGP.32** says... it depends. A pull model with a server-side orchestrator, designed to give IoT deployments the best of both worlds.

Before we get into the details: if you've been reading this series from the start, you've already absorbed 10 articles about SGP.02. This one zooms out. You won't need to have memorized every procedure, but you should know the roles (SM-DP, SM-SR, Operator, M2M SP), the push model, and the idea that the SM-SR owns the OTA channel. If those are fuzzy, the [Architecture article]({{ site.baseurl }}/docs/articles/sgp02/01-sgp02-architecture) will get you sorted. For the consumer side, familiarity with SGP.22's LPA and SM-DP+ helps but isn't mandatory; I'll explain what you need.

---

## The short answer: a decision table

If you want to skip the nuance (don't, but I get it, you're busy), here's the one-minute version:

| You're building... | Use this | Because... |
|---|---|---|
| A smartphone, tablet, or smartwatch | SGP.22 | QR onboarding, LPA, end-user self-service |
| A new IoT fleet with manageable devices | SGP.32 | Pull flexibility + eIM fleet orchestration |
| Truly unreachable M2M: sealed meters, buried sensors, eCall | SGP.02 | Push model; the server reaches in, no device cooperation needed |
| You already have 50,000 SGP.02 devices deployed | SGP.02 | Migration to SGP.32 involves new hardware; your fleet's got another decade to run |

Obvious caveat: reality is messier than a 2×4 table. Your automotive module might talk SGP.02 today but have an SGP.32 roadmap for 2028. Your smart meter fleet might be split; SGP.02 for the meters already in basements, SGP.32 for the new generation. Let's walk through why.

---

## SGP.02: the server knows best

SGP.02 was first, published in 2014 (current version: v4.2, July 2020). It was designed for a world where the device is dumb and the server is smart; and that's not an insult, it's a design constraint. When your device has no screen, no keyboard, and sits in a concrete vault for 15 years, you don't ask it to make decisions. You push.

The SM-SR sits at the center of the architecture. It holds the Platform Management keys, stores the EIS for every eUICC under management, and owns the OTA channel: SMS, HTTPS, CAT_TP, whatever it takes to reach the chip. The SM-DP builds profiles. The Operator decides when. The SM-SR delivers. The device accepts.

The split SM-DP/SM-SR architecture isn't an accident. It means an operator can buy profile generation from one vendor and secure routing from another, and can switch SM-SR providers without rebuilding profiles (the SM-SR Change procedure: 32 steps, four entities, one atomic commit point at step 23). That procedure alone is a 15-year insurance policy against vendor lock-in.

SGP.02 also has things no other eSIM spec replicates in quite the same way: the Fall-Back Mechanism (fully eUICC-autonomous, no server trigger path — SGP.32's version adds IPA and EIM-initiated variants), the Emergency Profile for eCall compliance, and the M2M SP role (fleet managers who don't own connectivity but need to manage it).

**The reason to still pick SGP.02 for new deployments in 2026:** your devices are truly unreachable. Not "occasionally offline"; actually unreachable. Sealed. No IP stack. Deep sleep for months. The kind of device where the server has to reach down and flip a switch whether the device is awake or not.

**The reason not to:** if your devices can check in periodically, even once a day, SGP.32 almost certainly gives you more flexibility with less complexity.

---

## SGP.22: the user is in charge

SGP.22 (first published 2016, current v2.7 from April 2026) flipped everything SGP.02 established. No SM-SR. No push. The LPA (Local Profile Assistant) runs on the device and initiates everything. It pulls profiles from the SM-DP+, a combined server role that handles both profile preparation and delivery.

The activation flow is the one everyone knows: scan a QR code encoded with `LPA:1$SMDP_ADDRESS$MATCHING_ID`. The LPA reaches out, mutual authentication happens, the profile downloads, done. The user tapped a button.

SGP.22 unified the SM-DP and SM-SR into the SM-DP+, collapsing two server roles into one. The ecosystem got simpler. The end-to-end security got stronger: ES8+ creates an SCP03t-encrypted tunnel between the SM-DP+ and the eUICC's ISD-P that the LPA can't see inside. The SM-DS (Discovery Server) acts as a bulletin board: the operator posts "there's a profile waiting for EID X," the LPA checks in, finds the pointer, and pulls.

**The reason to pick SGP.22:** consumer devices. Screens, QR codes, users who want to switch plans while sitting in an airport. If your device has an LPA (and every modern smartphone OS ships one), SGP.22 is the answer.

**The reason not to for IoT:** SGP.22 was never designed for fleet management. There's no server-side orchestrator. Managing 10,000 devices through SGP.22 means 10,000 individual QR code scans or activation codes. The spec doesn't stop you from building fleet tooling on top, but it doesn't help you either.

---

## SGP.32: IoT grows up

SGP.32 (first published 2023) is the newest member of the family, and it's explicitly designed to fill the gap SGP.22 left open: IoT devices that want pull-model flexibility but need fleet management at scale.

It introduces two new pieces:

**The IPA (IoT Profile Assistant)**, the device-side component, conceptually similar to the LPA but lighter. It can run on the device itself or on a companion gateway that manages multiple constrained eUICCs. Think of a smart home hub managing eSIMs for a dozen sensors.

**The eIM (eSIM IoT Manager)** is a server-side fleet orchestrator. The eIM can trigger profile operations on behalf of the device owner, giving you a server-driven element within the pull architecture. It doesn't replace the SM-DP+; SGP.32 reuses the existing consumer infrastructure. Operators don't need to deploy new profile servers.

The flexibility is the headline. A device can pull a profile on its own (like SGP.22). Or the eIM can trigger the pull (server-initiated within a pull framework). Or the IPA on a gateway can manage profiles for devices that are too constrained to run their own assistant.

The gateway model is genuinely new. A cellular router with an IPA can provision eSIMs on sensors that don't even have an IP stack; they just need the eUICC hardware. The IPA handles the heavy lifting.

**The reason to pick SGP.32 for new IoT:** pull flexibility, fleet management with the eIM, reuse of consumer SM-DP+ infrastructure, and the gateway model for the really constrained stuff. Unless your devices are completely unreachable (in which case, back to SGP.02), SGP.32 is the modern answer.

**The catch:** SGP.32 is newer. The ecosystem is still maturing. SGP.02 has been in production for a decade; SGP.32 is ramping up now. For a deployment starting in 2026, that's probably fine, but worth knowing.

---

## The specs side by side

### Architecture overview

| Dimension | SGP.02 (M2M Push) | SGP.22 (Consumer Pull) | SGP.32 (IoT Pull) |
|-----------|-------------------|----------------------|-------------------|
| **First Published** | 2014 (v4.2: July 2020) | 2016 (v2.7: April 2026) | 2023 (v1.0) |
| **Target Devices** | Utility meters, automotive, industrial sensors | Smartphones, tablets, wearables, laptops | IoT sensors, trackers, edge gateways, smart home |
| **Initiation Model** | Server push (SM-SR) | User/device pull (LPA) | Device pull (IPA) or server-managed (eIM) |
| **OTA Channel Owner** | SM-SR (dedicated server role) | SM-DP+ (combined DP+SR) | SM-DP+ (same as consumer) |
| **User Interaction** | None (headless) | Full (QR codes, LUI screens) | Minimal to none |
| **Server Architecture** | Split: SM-DP + SM-SR | Unified: SM-DP+ | Unified: SM-DP+ (extended) |
| **Discovery** | Not applicable (push) | SM-DS (discovery server) | SM-DS (reused) or eIM-directed |
| **Fleet Management** | Operator-driven (ES4) | Not designed for fleet | eIM (eSIM IoT Manager) |
| **Gateway Model** | Not applicable | Not applicable | IPA in gateway devices |
| **Spec Pages** | 452 pages | 296 pages | Evolving |

### Technical differences

| Feature | SGP.02 | SGP.22 | SGP.32 |
|---------|--------|--------|--------|
| Profile delivery trigger | Operator (ES4) / SM-SR | User (QR code) / LPA | User, IPA, or eIM |
| Server split | SM-DP ≠ SM-SR | SM-DP+ (combined) | SM-DP+ (combined) |
| Device component | None (ISD-R passive) | LPA (LDS+LPD+LUI) | IPA |
| Fleet management | Operator via ES4 | Not specified | eIM |
| Profile discovery | N/A (push) | SM-DS pull | SM-DS or eIM-directed |
| Key establishment | ECKA-EG (ElGamal) | ECDH (PFS via ES8+) | ECDH (shared with SGP.22) |
| Secure channel | SCP80 (legacy) / SCP03t | SCP03t (ES8+) | SCP03t |
| Vendor lock-in prevention | SM-SR Change procedure | SIM swap (physical or eSIM transfer) | eIM portability |
| First-attach notification | eUICC→SM-SR (automatic) | Not applicable | Configurable |

---

## "But I already have SGP.02 devices in the field"

This is the question that actually matters for anyone reading these articles because they're responsible for a real fleet. You're not starting from a blank whiteboard. You've got 10,000 smart meters running SGP.02, and they're supposed to keep running until 2038. What now?

**Option 1: Stay put.** SGP.02 is mature, proven, and the GSMA still maintains it (v4.2 from 2020 is current). Your SM-SR Change procedure protects you against vendor lock-in at the backend level. If your devices are working and your operator relationships are stable, doing nothing is a legitimate strategy. The spec was designed for 15-year lifecycles; it's not going anywhere.

**Option 2: Run both.** Several operators already do this: SGP.02 infrastructure for the legacy M2M fleet, SGP.22/SGP.32 for new device types, all behind the same core network. The SM-DP component can be shared between architectures if your vendor supports both protocols. Your existing devices stay on SGP.02; new deployments start on SGP.32.

**Option 3: Plan a hardware transition.** If you're refreshing your device hardware anyway (next-generation meters, a new telematics module), go SGP.32 on the new hardware. The eUICCs manufactured for SGP.02 can't simply get a firmware update to become SGP.32 devices; the ISD-R architecture is fundamentally different, and the IPA requires capabilities the M2M eUICC wasn't built for. Most transitions mean new chips.

The real-world path is usually Option 2 with a slow drift toward Option 3. The SGP.02 fleet keeps running. New devices arrive with SGP.32. Over a decade, the fleet composition shifts. Nobody does a flag-day cutover. M2M doesn't work that way.

---

## Where SGP.02 still owns the terrain

Despite being the oldest of the three, SGP.02 isn't legacy; it's specialized. Here's where it still wins:

**Automotive.** SGP.02 was designed with automotive requirements in mind from the start. The Emergency Profile exists because eCall regulation demanded it. The Fall-Back Mechanism exists because a car crossing borders can't afford to lose connectivity when one operator's network drops. SGP.32 is gaining traction in automotive, but SGP.02 has a 10+ year head start in production telematics units. That installed base isn't going anywhere.

**Utility metering.** Meters installed in 2018 running SGP.02 will operate into the 2030s. Replacing the eUICC means replacing the meter. Nobody's doing that voluntarily.

**Regulatory frameworks.** Some jurisdictions reference SGP.02 by name in their certification requirements. Migrating means not just a hardware swap but a regulatory re-approval process that can take years.

**Industrial environments.** Devices sealed against water, dust, and tampering (where physical access means breaking environmental seals) are SGP.02's natural habitat. The push model was literally invented for them.

The spec's longevity isn't a sign that it's outdated. The M2M world moves slowly, and SGP.02 was designed for that reality from page one.

---

## Summary

- SGP.02 (M2M Push, 2014), SGP.22 (Consumer Pull, 2016), and SGP.32 (IoT Pull, 2023) aren't sequential versions; they're three architectures optimized for different device categories
- The decision hinges on one question: who initiates provisioning? Server (SGP.02), user (SGP.22), or device with optional server orchestration (SGP.32)
- SGP.02 owns the unreachable-device niche: push model, SM-SR as OTA gateway, Fall-Back and Emergency mechanisms built in
- SGP.22 owns consumer devices: pull model, LPA on-device, QR code activation, unified SM-DP+
- SGP.32 bridges the gap for IoT: pull flexibility with eIM fleet management, IPA on-device or on-gateway, reuses consumer infrastructure
- For existing SGP.02 fleets: stay, run hybrid, or plan hardware refresh; there's no flag day
- For new deployments in 2026: SGP.22 for consumer, SGP.32 for IoT, SGP.02 only if your devices are truly unreachable

---

<div align="center">

<a href="{{ site.baseurl }}/">Home</a>

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp02/10-sgp02-offcard-interfaces">Off-Card Interfaces: ES1–ES7 and the SOAP Binding</a>

</div>

---

*Based on GSMA SGP.02 v4.2 (07 July 2020), SGP.22 v2.7 (24 April 2026), and SGP.32, cross-specification comparative analysis*


---

← Previous: [Off-Card Interfaces: ES1–ES7 and the SOAP Binding](10-sgp02-offcard-interfaces) | [Section Index](index)
