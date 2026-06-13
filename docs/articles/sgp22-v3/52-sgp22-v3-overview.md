---
description: "Introduces SGP.22 v3.x : the GSMA's unified RSP specification merging consumer and M2M architectures, covering Multiple Enabled Profiles, Push Service, Remote Profile Management, Device Change, and enterprise controls."
layout: default
title: "SGP.22 v3.x Overview: The Unified eSIM Specification"
date: 2026-06-06
---

# SGP.22 v3.x Overview: The Unified eSIM Specification

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.22 v3.x Unified RSP]({{ site.baseurl }}/docs/articles/sgp22-v3/) > SGP.22 v3.x Overview: The Unified eSIM Specification**

> **💡 Why this matters:** SGP.22 v3.x represents the biggest architectural shift in consumer eSIM since the original specification. It merges the consumer (SGP.22) and M2M (SGP.02) paradigms into a single unified specification, adds support for multiple simultaneously-active profiles, introduces push-based notifications to replace polling, and defines entirely new lifecycle operations like remote profile management, device change, and profile recovery. If you're planning an eSIM platform for the next decade, v3.x is the foundation you need to understand.

> **Key takeaways:**
> - SGP.22 v3.x is the GSMA's **unified RSP specification**, merging consumer and M2M architectures into one document
> - v3.0 was published October 2022; v3.1 (the current version) was published **01 December 2023**
> - v3.x coexists with v2.x: they are parallel tracks with different capabilities, not a replacement
> - Key new features: Multiple Enabled Profiles (MEP), Push Service, Remote Profile Management (RPM), Device Change, Profile Recovery, eUICC Root Public Key Update, LPA Proxy/Profile Content Management
> - A built-in **version interoperability** mechanism allows v2.x and v3.x devices and servers to coexist
> - The **Feature Support** system uses tagged acronyms (`#SupportedFromV3.X.Y#`) so senders can limit messages to what a receiver supports

---

## Why a Unified Specification?

The GSMA recognised that the consumer eSIM ecosystem (SGP.22 v2.x) and the M2M/IoT ecosystem (SGP.02) shared significant architectural overlap. Both needed profile download, secure channels, mutual authentication, and lifecycle management: but they used different protocols, different actors, and different trust models.

Rather than maintaining two entirely separate specification families in perpetuity, the GSMA began work on a single RSP Technical Specification that could serve consumer devices, IoT devices, and M2M equipment. This became the **v3.x track**.

In v2.x (consumer), the model is pull-based: the LPA on the device polls the SM-DS and downloads profiles from the SM-DP+. The end user initiates everything. In v3.x, the architecture also supports push-based operations: an operator can remotely trigger profile management commands (enable, disable, delete, update metadata, contact PCMP) without end user initiation. This brings M2M-style remote management capabilities into the consumer specification.

---

## The v3.x Timeline

| Version | Date | Key Contents |
|---------|------|-------------|
| **v3.0** | 19 October 2022 | First unified release: RPM, Enterprise Profiles, LPA Proxy, Multi-CI Security, Sub-CAs, Cancel Session, OS Update capability |
| **v3.1** | 01 December 2023 | Multiple Enabled Profiles, Push Service, Device Change & Profile Recovery, eUICC Root Public Key Update, RpmOrder enhancements, Contact PCMP, Unified Notifications |

v3.0 was the foundational release, introducing Remote Profile Management (RPM) : the Operator can remotely issue lifecycle commands to a Profile via the SM-DP+. It also introduced the concept of Enterprise Profiles, the LPA Proxy for Profile Content Management, support for subordinate Certificate Authorities (Sub-CAs), and multi-CI (Certificate Issuer) security.

v3.1 (the current version at the time of writing) added the headline consumer features: **Multiple Enabled Profiles (MEP)** : letting devices use more than one profile simultaneously: and **Push Service** : replacing SM-DS polling with push notifications. It also added the complete Device Change and Profile Recovery procedures, eUICC Root Public Key Update, and the Contact PCMP RPM command.

---

## What's New in v3.x vs v2.x

The v3.x specification includes every feature from v2.x and adds these major new capabilities:

### Architecture-Level Changes

1. **Multiple Enabled Profiles (MEP)** : v2.x allows only one profile Enabled at a time. v3.x allows several simultaneously, each assigned to an eSIM Port. This is the killer feature for multi-SIM devices.

2. **Push Service** : v2.x relies on the LDS polling the SM-DS periodically (the "pull" model). v3.x adds a push-based notification mechanism where the SM-DS can notify the device immediately when an Event Record is pending.

3. **Version Interoperability** : A built-in negotiation mechanism (`EuiccRspCapability`, `lpaRspCapability`, `rspCapability`) ensures v2.x and v3.x entities can communicate, discovering and adapting to each other's capabilities.

### Lifecycle Operations

4. **Remote Profile Management (RPM)** : Operators can remotely trigger Enable, Disable, Delete, ListProfileInfo, UpdateMetadata, and Contact PCMP commands via the SM-DP+. This is completely new in v3.x.

5. **Device Change** : End users can transfer a subscription from an old device to a new device, with the SM-DP+ orchestrating the process and optionally issuing a new profile for the new device.

6. **Profile Recovery** : If a Device Change fails (e.g., profile installation on the new device encounters a permanent error), the end user can recover the deleted profile on the old device.

7. **eUICC Root Public Key Update** : A mechanism to update the set of eSIM CA RootCA Public Keys in the ECASD, allowing deployed eUICCs to trust new Certificate Issuers.

8. **LPA Proxy / Profile Content Management (PCM)** : An LPA role (LPRd) that enables post-installation management of Profile contents via a PCMP (Profile Content Management Platform), triggered by profile enabling, RPM commands, or device applications.

### Security and Infrastructure

9. **Feature Support System** : Tagged acronyms (`#SupportedFromV3.X.Y#`, `#SupportedForRpmV3.X.Y#`, etc.) allow senders to conditionally include or omit data elements based on the receiver's declared capabilities.

10. **Sub-CAs and Multi-CI** : Support for subordinate Certificate Authorities and multiple Certificate Issuers, enabling more flexible PKI deployments.

11. **Enterprise Profiles** : A new Profile class for enterprise-managed devices, with associated Enterprise Rules.

---

## The v3.x Architecture Diagram

SGP.22 v3.1 introduces several new entities that don't exist in v2.x:

| New Entity | Role |
|-----------|------|
| **LPRd** (LPA Proxy in Device) | Establishes Profile Content Management sessions with a PCMP |
| **PCM Admin Agent (PCMAA)** | Mediates between LPRd and PCMP, executing APDU scripts on the Profile |
| **PCMP** (Profile Content Management Platform) | Server-side platform that manages profile contents post-installation |
| **Push Server / Push Client** | Infrastructure for push-based SM-DS notifications (out of scope for SGP.22) |
| **Enterprise Device App** | Application on enterprise-managed devices interacting via ES22 |
| **DLOA Registrar / DLOA Management System** | Delegated Letter of Approval infrastructure |

New interfaces in v3.x: `ES20` (LPRd ↔ PCMP), `ES21` (Device App ↔ LPRd), `ES22` (Enterprise Device App ↔ LPAd), `ESdsps` (SM-DS ↔ Push Server), `ESps` (Push Server ↔ Push Client), `ESpc` (Push Client ↔ LPAd).

---

## Relationship Between v2.x and v3.x

v3.x is **not** a replacement for v2.x. The GSMA maintains both tracks in parallel:

- **v2.x** continues as the consumer-focused evolution track (latest: v2.7, April 2026)
- **v3.x** is the unified track that merges consumer and M2M capabilities (latest: v3.1, December 2023)

Both tracks share the same core architecture (eUICC, SM-DP+, SM-DS, LPA, Operator), the same PKI, and the same profile package format. A v3.x eUICC declares its support for both v2.x and v3.x profile package versions via `euiccInfo2.additionalProfilePackageVersions`. An SM-DP+ selects the appropriate version based on what the eUICC declares.

The key difference is **scope**: v2.x targets consumer devices with pull-based provisioning and the end user always in the loop. v3.x adds push-based remote management, M2M-style operations, multiple simultaneously-enabled profiles, and enterprise features: all in one specification.

---

## Summary

- SGP.22 v3.x is the GSMA's unified eSIM RSP specification, merging consumer and M2M architectures
- v3.0 (October 2022) introduced RPM, Enterprise Profiles, LPA Proxy, and Multi-CI security
- v3.1 (December 2023) added MEP, Push Service, Device Change, Profile Recovery, and Root Key Update
- v3.x and v2.x coexist as parallel tracks: choose v3.x if you need M2M-style push operations, multiple enabled profiles, or enterprise features
- The Feature Support system ensures forward and backward compatibility through capability negotiation

---

<div align="center">

<a href="{{ site.baseurl }}/">🏠 Home</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp22-v3/53-multiple-enabled-profiles">Multiple Enabled Profiles: Running Several eSIMs at Once</a> →

</div>

---

*Based on GSMA SGP.22 v3.1 (01 December 2023), Sections 1.1–1.10, 2.1–2.13, and cross-references to SGP.22 v2.7*


---

[Section Index](index) | Next: [Multiple Enabled Profiles: Running Several eSIMs at Once](53-multiple-enabled-profiles) →
