---
title: "eSIM for IoT: Why It Needed Its Own Architecture"
date: 2026-05-22
---

# eSIM for IoT: Why It Needed Its Own Architecture

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.32 IoT eSIM]({{ site.baseurl }}/docs/articles/sgp32/) > eSIM for IoT: Why It Needed Its Own Architecture**

> **📚 Prerequisites:** This series assumes you've read the SGP.22 Consumer eSIM articles (01–06) or understand eSIM RSP fundamentals. The [Glossary]({{ site.baseurl }}/docs/glossary) defines all acronyms used in these articles.

> **💡 Why this matters:** Consumer eSIM (SGP.22) was built for smartphones — always-on, TCP/IP-connected, with a human user at the helm. IoT devices share none of those properties. The GSMA had to design a parallel architecture from scratch, and understanding *why* reveals the engineering constraints that shaped SGP.31 and SGP.32.

> **Key takeaways:**
> - Consumer eSIM assumptions (SMS, HTTPS, GUI, always-on connectivity) all break down in IoT
> - SGP.31's 30+ Basic Principles drive every design decision in the IoT eSIM stack
> - New concepts — `eIM`, `IPA`, `PSMO`, `eCO`, fallback/rollback mechanisms — replace consumer patterns
> - The specification is split into SGP.31 (architecture/requirements, 62 pp.) and SGP.32 (technical spec, 231 pp.)

SGP.22's consumer eSIM architecture assumes a smartphone: full TCP/IP stack, an always-on user, a GUI for profile management, and HTTPS transport. IoT devices share none of these properties. The GSMA's **SGP.31** and **SGP.32** specifications define a parallel architecture designed from first principles for constrained devices.

---

## What Consumer RSP Can't Do

Consumer eSIM (SGP.22) makes assumptions that break down completely in IoT:

| Consumer Assumption | IoT Reality |
|---------------------|-------------|
| SMS available for triggering | Many IoT devices lack SMS (NB-IoT, LTE-M) |
| TCP/IP and HTTPS | LPWA networks use CoAP over UDP, or non-IP delivery |
| User interacts with LUI | No screen, no keyboard, deployed in a sealed box |
| One user, one device, one profile at a time | Fleet of thousands, managed remotely, no human present |
| Always connected, always reachable | eDRX (extended Discontinuous Reception) / PSM (Power Saving Mode) cycles, device sleeps for days |
| Profile switching is manual | Profile operations must be remotely triggered and automated |

---

## The Fundamental Principles

SGP.31's Section 2 lays out approximately 30 basic principles (BP01 through BP34) that drive the entire design. The most important:

**BP03 — No SMS required.** Profile provisioning must work without SMS transport. This alone eliminates a major dependency from the consumer model.

**BP04 — No TCP/IP required.** The architecture must support connectionless protocols. Enter **CoAP** (Constrained Application Protocol) over UDP — the lightweight alternative to HTTP/TLS-heavy consumer flows.

**BP05 — Lightweight protocol.** CoAP-based transport (including LwM2M) must be supported for profile download and management over LPWA networks.

**BP06 — Asynchronous operations.** Profile operations may execute hours or days after being requested, when the device next wakes from eDRX or PSM cycles.

**BP12 — Remote management.** An entity (operator, enterprise, device owner) must be able to remotely enable, disable, and delete profiles. No user interaction required.

**BP13 — Fleet automation.** Profile operations should be automatable across thousands of devices — bulk provisioning, scheduled rollouts, staged upgrades.

**BP24 — Single round-trip.** The key management protocol should establish the secure channel in one round trip, minimising airtime on constrained networks.

**BP28 — Minimise NAND writes.** Operations on the eUICC must limit flash memory wear — IoT devices may have 10+ year operational lifetimes.

**BP29 — Unreachable for days.** The architecture must cope with devices being offline for prolonged periods.

---

## New Terminology

SGP.31 and SGP.32 introduce concepts that don't exist in the consumer world:

**eSIM IoT Remote Manager (`eIM`):** The remote entity that manages profiles across fleets. Replaces the consumer's "user interacting with an LUI." The `eIM` can be a standalone component or part of a device management platform like AWS IoT, Azure IoT Hub, or LwM2M servers.

**IoT Profile Assistant (`IPA`):** The on-device component. Similar in spirit to the consumer LPA, but stripped down — it acts as a proxy rather than a decision-maker. Two variants: **`IPAd`** (in the IoT Device) and **`IPAe`** (in the eUICC).

**Profile State Management Operations (`PSMO`):** Enable, disable, and delete — executed remotely without local user consent dialogs.

**eIM Configuration Operations (`eCO`):** Adding, updating, removing, and listing eIMs associated with an eUICC — a concept that has no consumer equivalent.

**Fallback Mechanism:** An eUICC-based safety net. If a profile switch fails and the device loses connectivity, the eUICC can automatically enable a designated "fallback profile" — the one with the Fallback Attribute set.

**Rollback Mechanism:** If a profile download fails mid-installation, the eUICC can revert the ISD-P to its pre-installation state rather than leaving a partially corrupted profile.

---

## What's Different from Consumer

In consumer eSIM, the LPA decides everything — when to download, which profile to enable, what to display. In IoT:

- **Decisions are remote.** The `eIM` tells the `IPA` what to do. The `IPA` is a conduit, not a controller.
- **Profiles have no nicknames.** There's no user to give them names.
- **No `ES10c` interface.** No Enable/Disable/Delete via a local UI. All management flows through the `eIM`.
- **No Activation Code scanning.** The `eIM` receives the Activation Code from the operator's backend and pushes it to the `IPA` — no QR codes, no camera.
- **Two download modes.** Direct (`IPA` talks to SM-DP+ directly) and Indirect (`eIM` mediates the entire exchange, useful when the device can't reach the internet).

---

## The Specification Split

SGP.31 and SGP.32 are designed to be used together:

- **SGP.31** (Architecture & Requirements) — the "what": principles, architecture diagrams, functional and security requirements, threat models. 62 pages.
- **SGP.32** (Technical Specification) — the "how": interface definitions, ASN.1 structures, procedure flows, eIM package formats, certificate profiles. 231 pages.

Together they form the complete IoT eSIM specification stack, sitting alongside SGP.22/SGP.21 for consumer devices and SGP.02 for M2M.

---

## 📋 Summary

- Consumer eSIM assumptions (SMS, HTTPS, GUI, always-on) break completely for constrained IoT devices
- SGP.31/SGP.32 replace user-driven flows with remote, asynchronous, automated profile management
- New components (`eIM`, `IPA`, `PSMO`, `eCO`) and mechanisms (fallback, rollback) are purpose-built for fleet-scale IoT
- The architecture supports multiple transports (CoAP/DTLS, HTTP/TLS), offline operation for days, and 10+ year device lifetimes

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

Next: [The eSIM IoT Architecture: eIM, IPA, and the New Interfaces]({{ site.baseurl }}/docs/articles/sgp32/08-iot-architecture-im-ipa) →

</div>

---

*Based on GSMA SGP.31 v1.3 and SGP.32 v1.3 (22 May 2026)*


---

[Section Index](index) | Next: [The eSIM IoT Architecture: eIM, IPA, and the New Interfaces](08-iot-architecture-im-ipa) →


---

[Section Index](index) | Next: [The eSIM IoT Architecture: eIM, IPA, and the New Interfaces](08-iot-architecture-im-ipa) →
