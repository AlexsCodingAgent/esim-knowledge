---
date: 2026-06-07
layout: default
title: "SGP.02 vs SGP.22 vs SGP.32: Push, Pull, and the Evolution of eSIM"
---

# SGP.02 vs SGP.22 vs SGP.32: Push, Pull, and the Evolution of eSIM

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > SGP.02 vs SGP.22 vs SGP.32: Push, Pull, and the Evolution of eSIM**

> **📚 Prerequisites:** You should have read the full SGP.02 series (at minimum Articles 1–2 for architecture, plus the procedure articles for lifecycle understanding). Familiarity with SGP.22's consumer architecture (LPA, SM-DP+, SM-DS) is helpful — see the SGP.22 overview on this site.

> **💡 Why this matters:** The GSMA has published three major eSIM specifications targeting different device categories. Choosing the wrong architecture for your deployment can mean the difference between a smooth fleet operation and a logistical nightmare. This comparison gives you the framework to make that decision.

> **Key takeaways:**
> - SGP.02 (2014) was first — designed for M2M push, where servers control provisioning of unattended devices
> - SGP.22 (2016) introduced the consumer pull model — user-initiated, QR-code-driven, designed for smartphones
> - SGP.32 (2023) brings pull to IoT — combining consumer-style UX with M2M-scale fleet management
> - Each spec uses a fundamentally different model for who initiates provisioning and who holds the OTA channel
> - The line between M2M and IoT blurs — SGP.32 now covers many use cases that were historically SGP.02 territory

---

## The Three Generations of eSIM

The GSMA's eSIM standardisation didn't follow a linear progression from simple to complex. Instead, each specification was designed for a fundamentally different class of device, with different constraints and different answers to the central question: **who initiates profile provisioning?**

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

---

## The Push Model (SGP.02)

SGP.02 is built around a simple principle: the device is dumb, the server is smart. The SM-SR owns the OTA channel and decides when profiles arrive.

**Key architectural characteristics:**
- **Split server roles:** SM-DP builds profiles; SM-SR manages platform operations. This separation creates a two-vendor ecosystem — you can change SM-DP without changing SM-SR, and vice versa
- **SM-SR as central hub:** All profile operations route through the SM-SR. The SM-SR holds the Platform Management keys, maintains the EIS, and is the single point of OTA contact
- **Operator-controlled lifecycle:** The Operator (not the device owner) decides when to provision, enable, disable, or delete profiles
- **No user interface path:** The ESx interface exists only for Device-initiated Test/Emergency profile switching — not for normal profile management
- **SM-SR Change procedure:** The spec includes a complete handover protocol (32 steps, four entities) to prevent vendor lock-in at the SM-SR level

**Best for:** Devices that are truly unreachable — sealed, headless, installed in inaccessible locations for years. Automotive telematics units with no screen, utility meters in basements, remote environmental sensors.

**Limitations:** Complex ecosystem with more roles and interfaces. Overhead of split DP/SR architecture. No end-user self-service path. Higher integration cost for small deployments.

---

## The Consumer Pull Model (SGP.22)

SGP.22 flipped the script: the device/user initiates everything. The LPA (Local Profile Assistant) running on the device pulls profiles from the SM-DP+.

**Key architectural characteristics:**
- **Unified SM-DP+:** Combines the functions of SM-DP and SM-SR into a single server role. Simpler ecosystem, fewer interfaces
- **LPA as device-side orchestrator:** Three sub-components (LDS for discovery, LPD for download, LUI for user interface) handle everything on-device
- **SM-DS for discovery:** A notification service that tells the LPA when a profile is waiting — the SM-DS holds pointers, not profiles
- **QR code activation:** The standard activation mechanism is an `LPA:1$SMDP_ADDRESS$MATCHING_ID` string encoded in a QR code
- **User-driven lifecycle:** Enable, disable, delete, nickname — all through the LUI
- **ES8+ end-to-end security:** The SM-DP+ communicates directly with the eUICC's ISD-P through an encrypted tunnel that the LPA cannot see inside

**Best for:** Consumer devices with screens and user interaction. Smartphones, tablets, smartwatches, laptops — any device where the end user makes connectivity decisions.

**Limitations:** Requires a functioning LPA on the device (software dependency). No fleet management infrastructure built into the spec. The pull model assumes the device is reachable and powered on when the user wants to act.

---

## The IoT Pull Model (SGP.32)

SGP.32 is the newest member of the family — designed to bring pull-model flexibility to IoT while addressing the fleet management needs that SGP.22 lacks and the accessibility constraints that make SGP.02's push model impractical for some IoT deployments.

**Key architectural characteristics:**
- **IPA (IoT Profile Assistant):** The device-side component, analogous to LPA but designed for constrained IoT devices. May run on the device itself or on a companion gateway
- **eIM (eSIM IoT Manager):** A new server-side role for fleet orchestration. The eIM can trigger profile operations on behalf of the device owner, providing a server-driven element within the pull architecture
- **Reuses SM-DP+ and SM-DS:** Leverages the existing consumer infrastructure — operators don't need to deploy new profile servers
- **Flexible initiation:** Supports both device-initiated pull (like SGP.22) and eIM-triggered operations (server-initiated within a pull framework)
- **Gateway model:** IPA can run on a gateway device managing multiple eUICCs — enabling provisioning of very constrained sensors through a more capable hub

**Best for:** IoT devices that benefit from pull flexibility but need fleet management. Asset trackers, smart home devices, edge gateways, agricultural sensors — devices that are reachable but deployed in large fleets.

**Relationship to SGP.02:** SGP.32 explicitly addresses many use cases that were previously SGP.02's domain. For new IoT deployments, SGP.32 is generally preferred. SGP.02 remains relevant for legacy fleets and truly unreachable devices.

---

## When to Use Which Standard

### Use SGP.02 when:

- The device has no screen, no user interaction, and no LPA-capable OS
- The Operator (not the device owner) controls connectivity decisions
- Devices are sealed and physically inaccessible for their entire lifecycle
- You need the split SM-DP/SM-SR architecture (e.g., separate vendors for profile preparation and platform management)
- You're supporting an existing M2M fleet built on SGP.02 infrastructure
- You need the SM-SR Change procedure for SM-SR-level vendor portability

### Use SGP.22 when:

- The device has a screen and end-user interaction
- Users need to self-manage profiles (add travel eSIMs, switch plans)
- QR code activation is the expected onboarding flow
- You're building a consumer product (phone, tablet, wearable, laptop)
- You want the simplest server-side architecture (single SM-DP+ vendor)

### Use SGP.32 when:

- You're deploying a new IoT fleet and want pull-model flexibility
- You need fleet management at scale (thousands of devices) with central orchestration
- Devices are constrained but reachable — they can check in periodically
- You want to reuse existing consumer SM-DP+ infrastructure
- You need the gateway model for very constrained sensors
- You want the option of both device-initiated and server-initiated operations

---

## Architectural Differences at a Glance

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

## Migration Paths

Organisations with existing SGP.02 deployments have several migration options:

**Stay on SGP.02:** For deeply embedded M2M devices with 10+ year lifecycles, staying on SGP.02 may be the right choice. The spec is mature, infrastructure is proven, and the SM-SR Change procedure ensures SM-SR portability. The GSMA continues to maintain the spec (v4.2 from 2020 remains current).

**Hybrid Architecture:** Some operators run both SGP.02 and SGP.22/SGP.32 infrastructure, serving different device categories from the same core network. The SM-DP component can be shared if the vendor supports both protocols.

**Greenfield SGP.32:** New deployments should strongly consider SGP.32 for any IoT use case — it provides better fleet management, simpler server architecture, and a modern security model. The only reason to choose SGP.02 for a new deployment is if the devices are truly unreachable (no IP connectivity, no periodic check-in capability).

**SGP.02 → SGP.32 transition:** Physical eUICCs manufactured for SGP.02 can potentially support SGP.32 if the eUICC OS is updated to include IPA-like functionality. However, the ISD-R architecture differs significantly, and in practice most transitions involve new hardware.

---

## The Enduring Relevance of SGP.02

Despite being the oldest of the three specifications, SGP.02 remains relevant for specific niches:

- **Automotive:** SGP.02 was designed with automotive requirements in mind (Emergency Profile for eCall, Fall-Back for connectivity resilience). While SGP.32 is gaining adoption, SGP.02 has a 10+ year head start in connected cars
- **Utility metering:** Meters installed in 2018 running SGP.02 will operate into the 2030s. Replacing the eUICC means replacing the meter
- **Industrial sensors in harsh environments:** Devices sealed against water, dust, and tampering where physical SIM replacement is impossible
- **Regulatory compliance:** Some regulatory frameworks reference SGP.02 specifically; migrating requires regulatory approval

The spec's longevity is a feature, not a bug — the M2M world moves slowly, and SGP.02 was designed for that reality.

---

## 📋 Summary

- SGP.02 (M2M Push), SGP.22 (Consumer Pull), and SGP.32 (IoT Pull) represent three generations of eSIM architecture, each optimised for different device categories
- SGP.02's push model puts the SM-SR in control — ideal for unreachable, headless devices where the Operator manages connectivity
- SGP.22's pull model empowers end users — ideal for consumer devices with screens and QR code onboarding
- SGP.32 bridges the gap — bringing pull flexibility to IoT with the eIM for fleet management, suitable for most new IoT deployments
- For new projects, SGP.32 is generally preferred for IoT; SGP.02 remains relevant for legacy fleets, automotive, and truly unreachable deployments
- The choice between standards is ultimately about who initiates provisioning, who controls the OTA channel, and how the device manages profiles

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

Previous: [Off-Card Interfaces: ES1–ES7 and the SOAP Binding](10-sgp02-offcard-interfaces) →

</div>

---

*Based on GSMA SGP.02 v4.2 (07 July 2020), SGP.22 v2.7 (24 April 2026), and SGP.32 — cross-specification comparative analysis*


---

← Previous: [Off-Card Interfaces: ES1–ES7 and the SOAP Binding](10-sgp02-offcard-interfaces) | [Section Index](index)
