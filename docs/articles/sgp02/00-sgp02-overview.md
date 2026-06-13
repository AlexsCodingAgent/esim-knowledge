---
title: "SGP.02 v4.2: The M2M eSIM Push Architecture"
3|description: "Covers the GSMA SGP.02 M2M RSP architecture : the push model for headless unattended devices, the SM-DP, SM-SR, and Operator roles, and the ES1–ES8 interface framework that connects them."
date: 2026-06-07
---

# SGP.02 v4.2: The M2M eSIM Push Architecture

**[eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > SGP.02 v4.2: The M2M eSIM Push Architecture**

Here's the problem SGP.02 was built for.

You've got a gas meter bolted to a basement wall. It's been running since 2018 and it's supposed to keep running until 2038. No screen. No keyboard. No human anywhere near it. And you need to switch its mobile operator.

QR codes? Useless (there's no camera, no user to hold up a phone). A "tap to install" button? There's no screen. Asking the device to pull a profile from a server is optimistic — it might be in deep sleep, powered down, or sitting in a signal shadow.

So what do you do?

**You push.** Some server, somewhere, decides it's time. It reaches down through the network, wakes the chip, authenticates, and installs the profile. The device never asked for it. The device didn't have to.

That's SGP.02.

## Not your phone's eSIM

SGP.02 is the GSMA's *Remote Provisioning Architecture for Embedded UICC* : the M2M eSIM standard. Published as version 4.2 in July 2020, all 452 pages of it. It's the *original* eSIM specification, written years before anyone thought about QR codes and consumer activation flows.

If you know consumer eSIM (SGP.22), you know a **pull model**: the device's LPA reaches out to an SM-DP+, downloads a profile, done. The device is the initiator. The user is in the loop.

SGP.02 flips that completely. The device is passive. The server (specifically the SM-SR (Subscription Manager) Secure Routing) : owns the over-the-air channel to the chip and pushes profiles down when the operator decides. No QR scanning. No LPA. No user.

The spec was written for devices that share a particular set of annoying characteristics:

- **Headless**: no screen, no keyboard, nobody to interact with
- **Unattended**: installed somewhere inaccessible for years or decades
- **Unreliable**: might be asleep, powered off, or in a coverage dead zone when you try to reach it
- **Deployed in batches**: thousands of meters all need profiles at the same time
- **Operator-controlled**: the MNO (not the device owner) decides who provides connectivity

The spec's scope section puts it plainly: SGP.02 targets "machine-to-machine Devices which are not easily reachable" (§1.3).

## Push means the server calls the shots

Here's what push actually looks like, compared to the consumer pull model most people know:

**Consumer eSIM (SGP.22, pull):**
1. You buy a plan, get a QR code or activation code
2. Your phone's LPA scans it and reaches out to the SM-DP+
3. Mutual authentication happens, profile downloads
4. Your device was the initiator every step of the way

**M2M eSIM (SGP.02, push):**
1. An operator orders a profile from the SM-DP (using the ES2 interface)
2. The SM-DP prepares the profile and coordinates with the SM-SR (via ES3)
3. The SM-SR opens a secure OTA channel to the eUICC (using SMS, HTTPS, or CAT_TP) and pushes platform management commands
4. The encrypted profile flows through the SM-SR as a relay to the chip
5. The device never initiated anything

The SM-SR has to know how to reach every eUICC under its management. It stores the **EIS** (eUICC Information Set) : addressing parameters, security keys, the state of every profile on every chip. When the EUM (manufacturer) creates a new chip, it registers that chip with a designated SM-SR through the ES1 interface before the chip ever leaves the factory floor.

Connectivity parameters matter a lot here. The eUICC needs to know its SMSC address for SMS-based OTA, or have working DNS for HTTPS. These aren't optional, they're what keeps the chip reachable, and the SM-SR can update them remotely if they change.

## Where SGP.02 sits in the eSIM family

SGP.02 was the first. It established the concepts every later spec inherited: the EID, the ISD-R/ISD-P/ECASD security domain architecture, the GSMA CI-rooted PKI, the profile package format. SGP.22 (consumer) and SGP.32 (IoT) both descend from it.

But they're built for different worlds:

| Aspect | SGP.02 (M2M) | SGP.22 (Consumer) | SGP.32 (IoT) |
|--------|---------------|-------------------|--------------|
| **Model** | Push (server-initiated) | Pull (device-initiated) | Pull with eIM orchestration |
| **Server role** | SM-DP + SM-SR (separate) | SM-DP+ (combined) | SM-DP+ + eIM |
| **Device agent** | None required | LPA (on-device) | IPA (lightweight) |
| **User interaction** | None | QR code, LUI | Minimal or none |
| **Activation** | Operator-driven | User-driven | eIM-driven |
| **Target devices** | Meters, automotive, sensors | Phones, tablets, watches | Constrained IoT |
| **Published** | 2013 (v1.0), v4.2 in 2020 | 2015 (v1.0), v3.1 in 2024 | 2023 (v1.0) |

SGP.02 and SGP.22 evolved side by side for years, each optimized for its domain. SGP.32 came later, bringing a modern pull model to IoT, which overlaps with some of SGP.02's territory. But SGP.02 still owns the deeply unattended deployments. The ones where the operator has to be able to reach down and flip a switch, whether the device is awake or not.

## What's inside those 452 pages

SGP.02 v4.2 is organized into five chapters, and the split tells you something about the architecture:

- **Chapter 1** (pp. 8–18): Definitions, abbreviations, scope
- **Chapter 2** (pp. 19–43): Architecture, roles, interfaces, eUICC internals, security model, OTA communication
- **Chapter 3** (pp. 44–187): The procedures, profile download and installation, lifecycle management, SM-SR change, fall-back, notifications. This is the meat of the spec.
- **Chapter 4** (pp. 188–247): On-card interfaces, ES5, ES6, ES8, ESx. Everything that touches the chip.
- **Chapter 5** (pp. 248–452): Off-card interfaces, ES1 through ES7, SOAP bindings, function specs. Everything that runs in data centers.

Notice the boundary: Chapters 4 and 5 are the "on-card" and "off-card" halves of the interface specification. That boundary (between what runs in silicon and what runs on a server) defines the entire ecosystem.

## What makes SGP.02 different from consumer eSIM

Beyond the push model, a few architectural choices set SGP.02 apart:

**Split SM-DP and SM-SR.** Consumer eSIM glues profile preparation and delivery together in the SM-DP+. SGP.02 separates them. The SM-DP builds and encrypts profiles. The SM-SR manages the OTA channel and all platform operations. An operator can buy profile generation from one vendor and secure routing from another, and can switch SM-SR providers without touching its profiles, using the SM-SR Change procedure (§3.8).

**No LPA.** There's no Local Profile Assistant on an SGP.02 device. The ESx interface between device and eUICC provides only the bare minimum: enabling or disabling emergency and test profiles locally. Everything else goes through the SM-SR.

**The M2M Service Provider.** SGP.02 introduces the M2M SP (a fleet manager who doesn't own connectivity. Think of an automotive OEM managing telematics units across countries, contracting with local operators for each region. The M2M SP gets authorized (via PLMA) Profile Lifecycle Management Authorization) to perform lifecycle operations on profiles the operator owns.

**Fall-Back.** Unique to SGP.02, one profile can be flagged with the Fall-Back Attribute. If the currently active profile loses connectivity, the eUICC automatically fails over to the fall-back. The device can always be reached for management, even when its primary operator's network is down.

---

SGP.02 was the first eSIM standard, written for devices that can't ask for help. The push model puts the server in command. The split SM-DP/SM-SR architecture gives operators vendor flexibility. If you're working on anything that sits in a wall, an engine, or a field (something that needs to switch operators without anyone touching it) this is the spec you're living with.

---

<div align="center">

<a href="{{ site.baseurl }}/"> Home</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp02/01-sgp02-architecture">M2M Ecosystem: EUM, SM-DP, SM-SR, and the Operator</a> →

</div>

---

*Based on GSMA SGP.02 v4.2 (07 July 2020) : Remote Provisioning Architecture for Embedded UICC Technical Specification*


---

[Section Index](index) | Next: [M2M Ecosystem: EUM, SM-DP, SM-SR, and the Operator](01-sgp02-architecture) →
