---
title: "SGP.33 Overview: The IoT eSIM Test Family"
description: "Explains the three-part SGP.33 IoT eSIM test specification family — covering IPA, SM-DP+, and eIM testing — built for IoT devices that lack user interfaces and rely on remote management via the eUICC IoT Manager."
date: 2026-06-05
---

# SGP.33 Overview: The IoT eSIM Test Family

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.33-3 eIM Testing]({{ site.baseurl }}/docs/articles/sgp33-3/) > SGP.33 Overview: The IoT eSIM Test Family**

> **💡 Why this matters:** Consumer eSIM testing (SGP.23) is well-established, but IoT devices operate under fundamentally different constraints: they may lack a user interface, have no local profile assistant, rely on remote management, and must support entirely new architectural elements like the eIM (eUICC IoT Manager). SGP.33 is the three-part test specification family built specifically for the IoT eSIM ecosystem defined by SGP.31 and SGP.32. Without it, there is no standardised path to prove that an IoT eSIM deployment actually works.

> **Key takeaways:**
> - SGP.33 is a family of three test specifications: SGP.33-1 (IPA), SGP.33-2 (SM-DP+), and SGP.33-3 (eIM) : each testing a different IoT-specific architectural component
> - IoT devices differ from consumer devices: no End User, remote profile management via the eIM, and new interfaces (ESep, ESipa, ES9+', ES11') that don't exist in consumer eSIM
> - SGP.33-3 targets the eUICC IoT Manager (eIM) : the remote server that manages profiles and eIM configuration on IoT devices without any device-side user interaction
> - The test family references SGP.22 (consumer RSP Technical Specification) and SGP.32 (IoT eSIM Technical Specification) as its normative baseline
> - All three documents share a common test methodology: simulator-based isolation, Optional Features Tables for conditional applicability, and conformance testing across interface compliance and system behaviour
> - As of v1.2 (January 2025), many test sequences: particularly on the ESipa interface: remain marked FFS (For Future Study), reflecting the evolving nature of IoT eSIM testing

The GSMA's SGP.33 document family was created in 2023 as a companion to the IoT specifications (SGP.31/SGP.32) to give IoT-specific testing the dedicated attention it required. Where SGP.23 tests consumer eSIM components (eUICC, LPAd/Device, SM-DP+, SM-DS) against SGP.22 V2.x, SGP.33 tests IoT-specific components against SGP.22 and SGP.32.

---

## The Three-Part Test Architecture

### SGP.33-1: IPA Test Specification

Tests the IoT Profile Assistant (IPA) : the IoT equivalent of the consumer LPA, but designed for devices that may lack a user interface. The IPA handles profile discovery, download initiation, and local profile management on the IoT device side. Tests cover ES10a (profile discovery), ES10b (profile download), ES9+ (SM-DP+ communication), and ES11 (SM-DS discovery).

### SGP.33-2: SM-DP+ Test Specification

Tests the SM-DP+ in the IoT context, where the SM-DP+ communicates not only with the IPA (via ES9+) but also directly with the eIM (via ES9+'). This introduces new test scenarios where profile delivery is coordinated through the remote eIM rather than a local LPA.

### SGP.33-3: eIM Test Specification (This Document)

Tests the eUICC IoT Manager (eIM) : the defining architectural innovation of IoT eSIM. The eIM is a remote server that:

- Manages Profile State Management Operations (Enable, Disable, Delete) via ESep eUICC Packages
- Handles eIM configuration (AddEim, UpdateEim, DeleteEim, ListEim) on the eUICC
- Communicates with SM-DP+ (ES9+') and SM-DS (ES11') for profile delivery and event discovery
- Interfaces with the IPA (ESipa) to trigger profile downloads and receive results
- Processes notifications from the eUICC through the IPA about profile state changes

SGP.33-3 v1.2 (74 pages, 27 January 2025) is the youngest and most forward-looking of the three: it defines test cases for an architectural component that didn't exist in consumer eSIM at all.

---

## Why IoT Needs Separate Test Specifications

### Architectural Differences from Consumer eSIM

Consumer eSIM (SGP.22) assumes:
- A Local Profile Assistant (LPA) running on a device with a screen and user input
- **End User Consent** required for profile operations
- Profile management initiated by the device owner scanning a QR code or tapping an activation code

IoT eSIM (SGP.31/SGP.32) operates differently:
- **No End User**: IoT devices may be headless sensors, meters, or trackers with no UI
- **Remote Management via eIM**: Profile operations are triggered remotely by the eIM, not locally by a user
- **New Interfaces**: ESep (eIM-to-eUICC logical channel), ESipa (eIM-to-IPA), ES9+' (eIM-to-SM-DP+), and ES11' (eIM-to-SM-DS) are IoT-specific
- **eIM Configuration Management**: The concept of associating, updating, and deleting eIM configurations on the eUICC is unique to IoT
- **TransactionID Support**: Optional correlation identifier for tracing eIM Package requests across multiple interfaces (option O_S_TRID)

### Testing Philosophy: Simulator-Based Isolation

SGP.33-3 follows the same simulator-based testing philosophy as SGP.23:

- The **IUT** is the eUICC IoT Manager (eIM) : the real implementation under test
- **S_SM-DP+**: Simulated SM-DP+ for ES9+' testing
- **S_SM-DS**: Simulated SM-DS for ES11' testing
- **S_eUICC**: Simulated eUICC for ESep testing
- **S_IPA**: Simulated IPA for ESipa testing
- **S_CLIENT** / **S_SERVER**: TLS testing simulators

This isolation ensures the eIM can be tested independently of real SM-DP+, SM-DS, eUICC, and IPA implementations.

---

## Optional Features and Conditional Applicability

SGP.33-3 defines three optional features (Table 4) that drive conditional test applicability:

| Mnemonic | Feature |
|----------|---------|
| `O_S_TRID` | A TransactionId is sent with eUICC Package Request |
| `O_S_PKG_RETRIEVAL` | The eIM supports the eIM Package Retrieval mode |
| `O_S_ESIPA_HTTPS` | The eIM uses TLS protocol over ESipa |

Condition C3000 governs the only behaviour test case currently defined: `IF (O_S_PKG_RETRIEVAL AND O_S_ESIPA_HTTPS) THEN M ELSE N/A`. This means the Profile Enable behaviour test sequence is only mandatory for eIM implementations that support both eIM Package Retrieval mode and TLS over ESipa.

---

## Version and Document History

SGP.33-3 v1.2 was published on 27 January 2025, but this is effectively the first published version: v1.0 and v1.1 were never published. The version number was aligned with the Core Specifications numbering. The document was initially split from SGP.23 v1.14 and revised through eSIM Working Group sessions.

---

## 📋 Summary

- SGP.33 is a three-part IoT-specific test family: SGP.33-1 (IPA), SGP.33-2 (SM-DP+), and SGP.33-3 (eIM) : created as a companion to SGP.31/SGP.32 in 2023
- SGP.33-3 targets the eUICC IoT Manager (eIM), the remote server that manages profiles and configuration on IoT devices without End User interaction
- IoT eSIM introduces new interfaces (ESep, ESipa, ES9+', ES11') and architectural concepts (eIM Configuration, eIM Package Retrieval) not present in consumer eSIM
- The test environment isolates the eIM using five simulator types (S_SM-DP+, S_SM-DS, S_eUICC, S_IPA, and TLS simulators)
- Three optional features (TransactionID support, eIM Package Retrieval, TLS over ESipa) drive conditional test applicability
- Many test sequences remain FFS as of v1.2, reflecting the evolving maturity of IoT eSIM testing

---

<div align="center">

<a href="{{ site.baseurl }}/">🏠 Home</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp33-3/43-sgp33-eim-architecture">eIM Test Architecture: Simulated eIM and Reference IPA</a> →

</div>

---

*Based on GSMA SGP.33-3 v1.2 (27 January 2025) : eUICC IoT Manager Test Specification, Sections 1–3*


---

[Section Index](index) | Next: [eIM Test Architecture: Simulated eIM and Reference IPA](43-sgp33-eim-architecture) →


---

[Section Index](index) | Next: [eIM Test Architecture: Simulated eIM and Reference IPA](43-sgp33-eim-architecture) →
