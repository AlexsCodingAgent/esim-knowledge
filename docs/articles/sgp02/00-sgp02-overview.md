---
date: 2026-06-07
---

# SGP.02 v4.2: The M2M eSIM Push Architecture

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > SGP.02 v4.2: The M2M eSIM Push Architecture**

> **📚 Prerequisites:** New to eSIM or smart card technology? Read our [Prerequisites Guide]({{ site.baseurl }}/docs/prerequisites) first. The [Glossary]({{ site.baseurl }}/docs/glossary) defines all acronyms used in these articles.

> **💡 Why this matters:** SGP.02 is the original eSIM standard, designed before smartphones needed QR-code activation. It powers millions of devices you'll never touch — utility meters, automotive telematics units, and industrial sensors — using a fundamentally different "push" philosophy from the consumer eSIM you know.

> **Key takeaways:**
> - SGP.02 uses a **push model**: the SM-SR decides when profiles arrive on the eUICC, not the device or user
> - It was designed for M2M devices that are unattended, headless, and often unreachable
> - The spec is 452 pages (v4.2, July 2020) defining the complete M2M remote provisioning ecosystem
> - Unlike SGP.22's combined SM-DP+, SGP.02 splits the server-side role into SM-DP (profile preparation) and SM-SR (secure routing and OTA channel ownership)
> - SGP.02 predates SGP.22 consumer and SGP.32 IoT — it was the first eSIM standard ever published

---

## What is SGP.02?

**SGP.02** is the GSMA's technical specification for *Remote Provisioning Architecture for Embedded UICC* — the "M2M eSIM standard." Published as version 4.2 in July 2020, it defines how mobile operator credentials (Profiles) are securely delivered to and managed on embedded SIM chips in machine-to-machine devices.

At its core, SGP.02 solves a problem that consumer eSIM standards don't face: **how do you provision a SIM card in a device that has no screen, no user, and may be sealed inside a utility meter bolted to a basement wall?**

The answer is the **push model**. In SGP.02, the server-side entity called the SM-SR (Subscription Manager — Secure Routing) owns the Over-The-Air communication channel to the chip. It pushes profiles down when the operator decides — no QR code scanning, no user tapping "Install," no device-initiated pull.

---

## Why a Separate Standard for M2M?

When the GSMA began work on embedded SIM technology in the early 2010s, the primary use case was not smartphones. It was **machine-to-machine communication**: connected cars, smart meters, industrial sensors, fleet tracking devices, and vending machines. These devices share characteristics that make a consumer-style "pull" model impractical:

- **Headless operation**: No screen, no keyboard, no user interaction
- **Unattended deployment**: Installed in inaccessible locations for years or decades
- **Unreliable reachability**: May be powered off, in sleep mode, or in areas with intermittent coverage
- **Batch provisioning**: Thousands of devices may need profiles simultaneously
- **Operator-controlled lifecycle**: The mobile network operator — not the device owner — typically decides when to switch connectivity providers

SGP.02 was designed around these constraints. The spec's own scope states it targets "machine-to-machine Devices which are not easily reachable" (SGP.02 §1.3). The push model puts the server in control: when the operator wants to install, enable, disable, or delete a profile, the SM-SR pushes commands to the eUICC over whatever bearer is available.

---

## The Push Model in Depth

The push model is the defining architectural characteristic of SGP.02. Here's what it means in practice:

**In SGP.22 (consumer "pull"):**
1. User buys an eSIM plan, receives a QR code
2. User's device scans the QR code
3. The LPA (Local Profile Assistant) on the device initiates contact with the SM-DP+
4. Mutual authentication happens, profile is downloaded
5. The device/user is always the initiator

**In SGP.02 (M2M "push"):**
1. Operator orders a profile from the SM-DP via the ES2 interface
2. SM-DP prepares the profile and works with the SM-SR via the ES3 interface
3. The SM-SR establishes a secure OTA channel to the eUICC (using SMS, HTTPS, or CAT_TP)
4. The SM-SR pushes the platform management commands and relays the encrypted profile
5. The device never initiates — the SM-SR is always the caller

This means the SM-SR must maintain knowledge of how to reach each eUICC. It stores the **EIS** (eUICC Information Set) which includes addressing parameters, security keys, and the current state of every profile on the chip. The ES1 interface is used by the EUM (eUICC Manufacturer) to register a new eUICC with its first SM-SR at manufacturing time.

The push model also means that **connectivity parameters** are critical. The eUICC needs to know the SMSC address for SMS, or have DNS resolver configuration for HTTPS. These parameters are managed carefully — the SM-SR can update them, and the eUICC can request DNS resolution when needed.

---

## SGP.02 in the GSMA eSIM Family

SGP.02 was the first eSIM specification. It established the foundational concepts — the EID, the ISD-R/ISD-P/ECASD security domain architecture, the GSMA CI-rooted PKI, and the profile package format — that later specifications inherited. Here's how the three major eSIM standards compare:

| Aspect | SGP.02 (M2M) | SGP.22 (Consumer) | SGP.32 (IoT) |
|--------|---------------|-------------------|--------------|
| **Model** | Push (server-initiated) | Pull (device-initiated) | Pull with eIM orchestration |
| **Server role** | SM-DP + SM-SR (separate) | SM-DP+ (combined) | SM-DP+ + eIM |
| **Device agent** | None required | LPA (on-device) | IPA (lightweight) |
| **User interaction** | None | QR code, LUI | Minimal or none |
| **Activation** | Operator-driven | User-driven | eIM-driven |
| **Target devices** | Meters, automotive, sensors | Phones, tablets, watches | Constrained IoT |
| **Published** | 2013 (v1.0), v4.2 in 2020 | 2015 (v1.0), v3.1 in 2024 | 2023 (v1.0) |

SGP.02 and SGP.22 evolved in parallel for years, each optimized for its domain. SGP.32 arrived later, bringing a modern "pull" model to IoT devices that might previously have used SGP.02 — but SGP.02 remains relevant for truly embedded, deeply unattended deployments where the operator must retain full control of the connectivity lifecycle.

---

## Document Scope and Structure

SGP.02 v4.2 is a 452-page specification covering:

- **Chapter 1**: Introduction, definitions, abbreviations (pages 8–18)
- **Chapter 2**: General architecture — roles, interfaces, eUICC internals, security model, OTA communication (pages 19–43)
- **Chapter 3**: Detailed procedure specifications — profile download, lifecycle management, SM-SR change, fall-back, notifications (pages 44–187)
- **Chapter 4**: eUICC interface descriptions — ES5, ES6, ES8, ESx (pages 188–247)
- **Chapter 5**: Off-card interface descriptions — ES1 through ES7, SOAP binding, function specifications (pages 248–452)

The interfaces within the eUICC (ES5, ES6, ES8, ESx) are specified in Chapter 4, while the off-card interfaces between servers (ES1, ES2, ES3, ES4, ES7) are specified in Chapter 5. This reflects the architectural boundary: everything "on-card" is implemented in the eUICC chip, and everything "off-card" runs on servers in data centers.

---

## What Makes SGP.02 Different

Beyond the push model, several architectural choices distinguish SGP.02:

**Separate SM-DP and SM-SR**: In SGP.22, the SM-DP+ combines profile preparation and delivery. In SGP.02, these are separate roles. The SM-DP prepares and encrypts profiles. The SM-SR manages the OTA channel and all platform operations. This separation allows an operator to use different vendors for profile generation and secure routing — and to change SM-SR providers without replacing profiles via the SM-SR Change procedure.

**No LPA**: SGP.02 devices don't have a Local Profile Assistant. The ESx interface (Device ↔ eUICC) provides only minimal local operations — enabling/disabling test and emergency profiles. Everything else goes through the SM-SR.

**M2M Service Provider**: SGP.02 introduces the M2M SP role — an entity that manages a fleet of devices on behalf of the end customer but relies on operators for connectivity. The M2M SP can be authorized (via PLMA — Profile Lifecycle Management Authorization) to perform lifecycle operations on profiles owned by an operator.

**Fall-Back Mechanism**: Unique to SGP.02, one profile can be designated with the Fall-Back Attribute. If the currently enabled profile loses connectivity, the eUICC automatically switches to the fall-back profile, ensuring the device can always reconnect for management commands.

---

## 📋 Summary

- SGP.02 is the original eSIM standard, designed for unattended M2M devices that need operator-controlled, push-based profile management
- The push model puts the SM-SR in command of all OTA communication — profiles arrive when the server decides, not when the device requests them
- SGP.02 sits alongside SGP.22 (consumer pull) and SGP.32 (IoT pull) in the GSMA eSIM family, each optimized for different deployment scenarios
- Key architectural differences from consumer eSIM include the split SM-DP/SM-SR roles, the absence of an LPA, the M2M SP role, and the Fall-Back Mechanism
- Understanding SGP.02 is essential for anyone working with automotive, smart metering, industrial IoT, or any deployment where devices cannot rely on user interaction

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

Next: [M2M Ecosystem: EUM, SM-DP, SM-SR, and the Operator]({{ site.baseurl }}/docs/articles/sgp02/01-sgp02-architecture) →

</div>

---

*Based on GSMA SGP.02 v4.2 (07 July 2020) — Remote Provisioning Architecture for Embedded UICC Technical Specification*


---

[Section Index](index) | Next: [M2M Ecosystem: EUM, SM-DP, SM-SR, and the Operator](01-sgp02-architecture) →
