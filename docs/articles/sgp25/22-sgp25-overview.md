---
title: "SGP.25 Overview: The eUICC Common Criteria Protection Profile"
description: "Introduces the SGP.25 Common Criteria Protection Profile at EAL4+ for eUICC software — a modular Base-PP with optional LPAe, IPAe, and Dual modules, mandated for any eUICC carrying production profiles."
date: 2026-06-05
---

# SGP.25 Overview: The eUICC Common Criteria Protection Profile

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.25 eUICC Security]({{ site.baseurl }}/docs/articles/sgp25/) > SGP.25 Overview: The eUICC Common Criteria Protection Profile**

> **💡 Why this matters:** SGP.22 defines *how* eSIM works on a protocol level, and SGP.23 defines *how to test it*. SGP.25 defines *how to trust it* : the Common Criteria Protection Profile that every commercial eUICC must be evaluated against before it can carry real operator profiles. This is the security certification foundation that underpins the entire consumer and IoT eSIM ecosystem.

> **Key takeaways:**
> - SGP.25 is a Common Criteria (CC) Protection Profile at EAL4+, defining security requirements for eUICC software
> - The TOE (Target of Evaluation) is the eUICC software implementing GSMA RSP specifications for Consumer and/or IoT Devices
> - EAL4 augmented with ALC_DVS.2 (development security) and AVA_VAN.5 (advanced penetration testing) is the mandated assurance level
> - The PP follows a modular approach: Base-PP covers core eUICC, with optional LPAe, IPAe, and Dual PP-Modules
> - Published as SGP.25 v2.1 (3 February 2025), conformant to CC:2022 release 1, authored and maintained by the GSMA
> - Certification against this PP is the prerequisite for any eUICC to handle production operator profiles

SGP.25 is the GSMA's Common Criteria Protection Profile for the eUICC: the embedded SIM chip that forms the trust anchor of Remote SIM Provisioning. While SGP.22 (RSP Technical Specification) defines protocol behaviours and SGP.23 (RSP Test Specification) defines conformance test cases, SGP.25 defines the security requirements and assurance levels that an eUICC must demonstrably meet, evaluated by an accredited independent laboratory.

---

## What Is a Common Criteria Protection Profile?

A Protection Profile (PP) is a technology-specific security standard under the Common Criteria for Information Technology Security Evaluation (ISO/IEC 15408) : an internationally recognised framework for specifying and evaluating the security properties of IT products.

Key concepts:

- **Protection Profile (PP)** : An implementation-independent set of security requirements for a category of products. SGP.25 is the PP for eUICCs.
- **Security Target (ST)** : A vendor-specific document that instantiates the PP for a particular product, selecting and refining requirements.
- **Target of Evaluation (TOE)** : The specific product (or component) being evaluated. For SGP.25, the TOE is the eUICC software.
- **Evaluation Assurance Level (EAL)** : A scale from EAL1 (functionally tested) to EAL7 (formally verified design and tested) that dictates the rigour of the evaluation.

The CC framework is administered by national certification schemes (e.g., BSI in Germany, ANSSI in France, NIAP in the USA) operating under the Common Criteria Recognition Arrangement (CCRA), which provides mutual recognition of certificates across 31 nations.

### Why eUICCs Need a Protection Profile

An eUICC is fundamentally different from a traditional SIM card:

- It hosts **multiple operator profiles** simultaneously, with strict isolation requirements
- It supports **post-issuance remote provisioning**, meaning operators load credentials over the air onto a chip they don't physically control
- It stores **long-lived cryptographic credentials** (eUICC private keys, eSIM CA public keys) that must resist extraction over a product lifetime of 10+ years
- It is deployed in **hostile environments** : embedded in consumer phones, IoT sensors, and industrial equipment accessible to adversaries

Without independent security evaluation, there is no basis for trust between the eUICC manufacturer, the operator loading profiles onto it, and the end user.

---

## TOE Overview: What SGP.25 Evaluates

The TOE of this Protection Profile is the **embedded UICC software** that implements:

- **GSMA RSP Architecture Specification [SGP.21]** and **Technical Specification [SGP.22]** for Consumer Devices, and/or
- **GSMA eSIM IoT Architecture and Requirements [SGP.31]** and **eSIM IoT Technical Specification [SGP.32]** for IoT Devices

The TOE comprises two layers:

### Application Layer
The privileged applications providing remote provisioning and administration:

| Component | Role |
|-----------|------|
| **ISD-R** (Issuer Security Domain: Root) | Life-cycle management of profiles; includes LPA/IPA Services |
| **ECASD** (eUICC Controlling Authority Security Domain) | Secure storage of credentials; key establishment; eUICC authentication |
| **ISD-P** (Issuer Security Domain: Profile) | Secure container hosting one unique profile per ISD-P |

### Platform Layer
Support functions underpinning the Application Layer:

| Component | Role |
|-----------|------|
| **Telecom Framework** | Network authentication algorithms (3G/4G/5G) |
| **Profile Package Interpreter** | Translates Profile Package data into installed Profiles |
| **Profile Rules Enforcer** | Enforces Profile Policy Rules (PPRs), Enterprise Rules, and the Rules Authorisation Table (RAT) |

The secure IC and its embedded software (OS, Runtime Environment) are considered the **operational environment** of the eUICC TOE, covered by security objectives that must be fulfilled by a previously certified platform or translated into explicit SFRs.

---

## EAL4+: The Assurance Level

SGP.25 mandates **EAL4 augmented** : the highest practical assurance level for a commercial-grade product:

- **EAL4 base**: Methodically designed, tested, and reviewed. Requires low-level design, implementation representation (source code), functional testing, and independent testing.
- **ALC_DVS.2** (augmentation): Sufficiency of security measures in the development environment: physical, procedural, and personnel controls that protect TOE confidentiality and integrity during development.
- **AVA_VAN.5** (augmentation): Advanced methodical vulnerability analysis: penetration testing by evaluators with **elevated attack potential**, searching for vulnerabilities that could bypass TSF protections.

```
EAL4+ = EAL4 + ALC_DVS.2 + AVA_VAN.5
```

This is the same assurance level required for Java Card platforms and other smart card security products hosting sensitive applications.

---

## The Modular PP Structure

SGP.25 v2.1 employs a modular approach defined by CC:2022 Part 1, consisting of:

1. **Base-PP** (Sections 1–6) : Core eUICC security requirements, covering the ISD-R, ISD-P, ECASD, and Platform Layer regardless of where the LPA/IPA resides.

2. **LPAe PP-Module** (Section 7) : Additional requirements when the Local Profile Assistant resides *inside* the eUICC (LPAe) rather than on the Device.

3. **LPAe PP-Configuration** (Section 8) : Composite configuration combining Base-PP + LPAe PP-Module for LPAe-capable consumer eUICCs.

4. **IPAe PP-Module** (Section 9) : Additional requirements when the IoT Profile Assistant resides inside the eUICC (IPAe).

5. **IPAe PP-Configuration** (Section 10) : Composite configuration for IPAe-capable IoT eUICCs.

6. **Dual LPAe and IPAe PP-Configuration** (Section 11) : Combined configuration for eUICCs supporting both consumer and IoT provisioning.

7. **PP-Module OS Update** (Annex A) : Mandatory module if the TOE provides eUICC OS Update functionality.

---

## High-Level Threat Landscape

SGP.25 structures threats in two tiers:

### First-Level Threats
- **Unauthorised Profile / Platform management** : An off-card actor or malicious on-card application alters Profile data or manipulates Platform functions (e.g., disabling an enabled Profile)
- **Identity tampering** : Modification of eUICC identity data or actor identities, such as the eSIM CA public key or session secrets
- **eUICC cloning** : Using a legitimate Profile on an unauthorised eUICC or simulator
- **LPAd/IPAd impersonation** : Exploiting the always-present LPAd interfaces to masquerade as a legitimate LPA
- **Unauthorised access to mobile networks** : Leveraging flaws in network authentication to access keys

### Second-Level Threats
- **Logical attacks** : Unintended side-effects of legitimate functions, buffer overflows, unauthorised code execution
- **Physical attacks** : Side-channel analysis (SPA/DPA), fault injection, environmental stress, electrical probing

---

## 📋 Summary

- SGP.25 is the GSMA's Common Criteria Protection Profile for eUICC security certification at EAL4+
- The PP evaluates eUICC software (ISD-R, ECASD, ISD-P, and Platform Layer) implementing SGP.22 and/or SGP.32
- EAL4 augmented with ALC_DVS.2 and AVA_VAN.5 provides the highest practical assurance for commercial grade products
- The modular structure separates Base-PP requirements from LPAe/IPAe optional modules for consumer and IoT variants
- Certification against SGP.25 is the trust prerequisite: no production operator profiles are loaded onto an uncertified eUICC

---

<div align="center" markdown="1">

[🏠 Home]({{ site.baseurl }}/)

Next: [eUICC Security Functional Requirements]({{ site.baseurl }}/docs/articles/sgp25/23-sgp25-security-requirements) →

</div>

---

*Based on GSMA SGP.25 v2.1 (3 February 2025) : eUICC for Consumer and IoT Devices Protection Profile, Sections 1–2, conformant to Common Criteria CC:2022 release 1*


---

[Section Index](index) | Next: [eUICC Security Functional Requirements](23-sgp25-security-requirements) →


---

[Section Index](index) | Next: [eUICC Security Functional Requirements](23-sgp25-security-requirements) →
