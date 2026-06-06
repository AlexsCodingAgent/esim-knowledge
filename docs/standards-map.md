---
layout: default
title: "GSMA eSIM Standards Map: eUICC.tech"
---

# 🗺️ GSMA eSIM Standards Map

*The complete GSMA SGP specification landscape: what each spec does, how they relate, and when they were published.*

---

## Timeline

```
2007 ─ SGP.01    eSIM Architecture Overview (foundational concepts)
  │
2010 ─ SGP.02    M2M RSP Architecture (original push-based M2M spec)
  │
2014 ─ SGP.21    RSP Architecture (underpins SGP.22)
2015 ─ SGP.22    RSP Technical Specification v1.0 (Consumer eSIM)
  │
2016 ─ SGP.23    RSP Test Specification (Consumer compliance)
2017 ─ SGP.24    eUICC Compliance Process
2018 ─ SGP.25    eUICC Protection Profile v1.0
  │    SGP.26    RSP Test Certificates Definition
  │
2019 ─ SGP.22    v2.0: major rewrite
2020 ─ SGP.22    v2.2 (current baseline for most deployments)
  │    SGP.27    IoT eSIM Feasibility Study
  │    SGP.28    IoT eSIM Requirements
  │
2021 ─ SGP.29    EID Definition and Assignment Process
2022 ─ SGP.31    eSIM IoT Architecture & Requirements v1.0
  │    SGP.32    eSIM IoT Technical Specification v1.0
  │
2023 ─ SGP.22    v2.5: LPAd/LPAe refinements
  │    SGP.23-1  RSP Test Specification for the eUICC v3.0
  │    SGP.33    IoT Test Spec family (33-1 LPA, 33-2 SM-DP+, 33-3 eIM)
  │
2024 ─ SGP.25    v2.0: Protection Profile for Consumer + IoT unified
  │    SGP.29    v1.1: EID refinements
  │
2025 ─ SGP.23    v1.16: latest consumer test spec
  │    SGP.23-1  v3.1.3: latest eUICC test spec
  │    SGP.25    v2.1: Protection Profile
  │    SGP.26    v3.0.2: Test Certificates
  │    SGP.33-3  v1.2: eIM Test Spec
  │    SGP.41    v1.0: IFPP
  │
2026 ─ SGP.22    v2.7 (April 2026) : LATEST consumer spec  │ SGP.22 v3.2: unified consumer+M2M spec (parallel track)
  │    SGP.31    v1.3 (May 2026) : LATEST IoT architecture
  │    SGP.32    v1.3 (May 2026) : LATEST IoT technical spec
```

---

## Specification Dependency Map

```
                    ┌─────────────────────────────────┐
                    │     SGP.01: Architecture       │
                    │     (foundational concepts)      │
                    └───────────┬─────────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│   SGP.02      │     │   SGP.21      │     │   SGP.31      │
│  M2M RSP      │     │ RSP Arch      │     │ IoT Arch      │
│  (push model) │     │ (consumer)    │     │ (IoT)         │
└───────┬───────┘     └───────┬───────┘     └───────┬───────┘
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│   (legacy)    │     │   SGP.22      │     │   SGP.32      │
│               │     │ RSP Tech Spec │     │ IoT Tech Spec │
│               │     │ (consumer)    │     │ (IoT)         │
│               │     └───────┬───────┘     └───────┬───────┘
│               │             │                     │
│               │     ┌───────┴───────┐     ┌───────┴───────┐
│               │     │   SGP.23      │     │   SGP.33-3    │
│               │     │ Test Spec     │     │ eIM Test Spec │
│               │     │ (consumer)    │     │ (IoT)         │
│               │     └───────────────┘     └───────────────┘
│               │
│               │     ┌───────────────┐
│               │     │  SGP.23-1     │
│               │     │ eUICC Test    │
│               │     └───────────────┘
│               │
│               ├─────┤
│                     │
│       SHARED        │
│       ACROSS        │
│       ALL           │
│                     │
│  ┌───────────────┐  │
│  │   SGP.24      │  │
│  │ Compliance    │  │
│  │ Process       │  │
│  └───────────────┘  │
│  ┌───────────────┐  │
│  │   SGP.25      │  │
│  │ eUICC PP      │  │
│  │ (security)    │  │
│  └───────────────┘  │
│  ┌───────────────┐  │
│  │   SGP.26      │  │
│  │ Test Certs    │  │
│  └───────────────┘  │
│  ┌───────────────┐  │
│  │   SGP.29      │  │
│  │ EID Standard  │  │
│  └───────────────┘  │
│                     │
│       NEW:          │
│  ┌───────────────┐  │
│  │   SGP.41      │  │
│  │ IFPP (in-     │  │
│  │ factory)      │  │
│  └───────────────┘  │
```

---

## Coverage Status

| Spec | Title | Version | Pages | Covered? | Articles Planned |
|------|-------|---------|-------|----------|------------------|
| SGP.01 | Architecture Overview | : | : | ❌ | 0 (foundational: referenced) |
| SGP.02 | M2M RSP Architecture | : | : | ❌ | 0 (mentioned in IoT article) |
| SGP.21 | RSP Architecture | : | : | ❌ | 0 (content absorbed into SGP.22) |
| **SGP.22** | **RSP Technical Spec** | **v2.7** | **~300** | **✅ 8 articles** | **Update to v2.7 + v2/v3 split** |
| **SGP.22 v3.2** | **Unified RSP Tech Spec** | **v3.2** | **TBD** | **❌** | **0 (parallel track: v2.x/v3.x article covers it)** |
| **SGP.23** | **RSP Test Spec** | **v1.16** | **913** | **❌ NEW** | **5 articles** |
| **SGP.23-1** | **eUICC Test Spec** | **v3.1.3** | **797** | **❌ NEW** | **5 articles** |
| SGP.24 | Compliance Process | : | : | ❌ | 0 (referenced) |
| **SGP.25** | **eUICC Protection Profile** | **v2.1** | **172** | **❌ NEW** | **5 articles** |
| **SGP.26** | **Test Certificates** | **v3.0.2** | **66** | **❌ NEW** | **5 articles** |
| **SGP.29** | **EID Standard** | **v1.1** | **13** | **❌ NEW** | **5 articles** |
| **SGP.31** | **IoT Architecture** | **v1.3** | **62** | **✅** | **(part of SGP.32 series)** |
| **SGP.32** | **IoT Technical Spec** | **v1.3** | **231** | **✅ 10 articles** | **Update to v1.3** |
| **SGP.33-3** | **eIM Test Spec** | **v1.2** | **74** | **❌ NEW** | **5 articles** |
| **SGP.41** | **IFPP Architecture** | **v1.0** | **~26** | **❌ NEW** | **5 articles** |

**Total: 18 existing articles + 35 new = 53 articles across 9 specs**

---

## Article Plans by Specification

### SGP.22 v2.7: RSP Technical Specification (UPDATE existing)
> *Current articles cite v2.2.2. All updated to reference v2.7. Added 00b explaining the v2.x/v3.x specification split.*

### SGP.22 v3.2: Unified RSP Technical Specification (NEW parallel track)
> *Unified consumer+M2M specification. Covered in the v2.x/v3.x split article (00b). Full deep-dive articles planned once a stable v3.x CR is available.*

### SGP.23 v1.16: RSP Test Specification (NEW)
1. **SGP.23 Overview: How eSIM Interoperability Is Tested** : The test ecosystem: GSMA test events, SAS certification, DLOA process. Why testing matters.
2. **The GSMA eSIM Test Infrastructure** : Test SIMs, test certificates, simulated SM-DP+/SM-DS, reference LPA implementations, lab requirements.
3. **Testing the LPA: LDS, LPD, and LUI Conformance** : Key test cases for each LPA component. ES10a/b/c, ES11 validation.
4. **Testing the SM-DP+ and SM-DS** : ES2+, ES8+, ES9+, ES12 test cases. Profile ordering, delivery, notifications.
5. **SGP.23 Certification: From Test Cases to DLOA** : The certification workflow, test report structure, Digital Letter of Approval.

### SGP.23-1 v3.1.3: eUICC Test Specification (NEW)
1. **SGP.23-1 Overview: Testing the eUICC Itself** : The 797-page test bible. What's tested, test architecture, how it differs from SGP.23.
2. **eUICC Test Architecture** : Test readers, GSMA reference eUICC implementation, test script execution, logging.
3. **Key eUICC Test Cases** : ISD-R lifecycle, ECASD operations, profile installation/management, memory management.
4. **eUICC Security Testing** : Certificate validation, ECDSA/ECDH operations, SCP03t channel testing, CRL handling.
5. **eUICC Certification and SAS-UP** : The path from test results to SAS-UP certification. Relationship with SGP.25.

### SGP.25 v2.1: eUICC Protection Profile (NEW)
1. **SGP.25 Overview: The Common Criteria Protection Profile** : What a Protection Profile is, CC EAL levels, why eUICCs need one.
2. **Security Functional Requirements** : Cryptographic support, user data protection, identification & authentication, security management.
3. **Assurance Requirements and Penetration Testing** : EAL4+ augmented, AVA_VAN.5, penetration testing scope.
4. **Physical Security: Side-Channel and Fault Injection** : DPA/SPA countermeasures, fault injection resistance, tamper evidence.
5. **SGP.25 Certification and SAS-UP** : Evaluation process, accredited labs, certificate maintenance.

### SGP.26 v3.0.2: Test Certificates Definition (NEW)
1. **SGP.26 Overview: The RSP Test PKI** : Why test certificates exist, how they differ from production, the test CI.
2. **Test Certificate Hierarchy** : CI root → test EUM, test SM-DP+, test SM-DS, test eUICC certificates.
3. **Certificate Profiles and Key Sizes** : Algorithm requirements, key usages, extensions specific to testing.
4. **Using Test Certificates in Development** : How to obtain, install, and use test certificates. Common pitfalls.
5. **CRL and Certificate Management for Test** : Test CRL distribution, certificate expiry, rotation in test environments.

### SGP.29 v1.1: EID Definition and Assignment (NEW)
1. **SGP.29 Overview: The eUICC Identifier (EID)** : What EID is, why it's critical, the GSMA assignment process.
2. **EID Format Decoded** : The 32-digit structure: issuer ID, individual ID, check digits. Worked examples.
3. **EID Assignment Process** : How manufacturers request EID ranges. The ERHI1 assignment flow. GSMA DAG governance.
4. **EID in RSP Protocols** : How EID is used in SM-DS discovery, profile matching, and event registration.
5. **EID Security and Privacy** : Tracking risks, EID rotation, GSMA privacy controls.

### SGP.33-3 v1.2: eIM Test Specification (NEW)
1. **SGP.33 Overview: The IoT Test Family** : SGP.33-1 (IPA), SGP.33-2 (SM-DP+), SGP.33-3 (eIM). Test coverage for IoT.
2. **eIM Test Architecture** : Simulated eIM, reference IPA implementation, test harness setup.
3. **Key eIM Test Cases** : Profile state management (PSMO), notifications, eIM configuration, IPA-eIM communication.
4. **eIM Security Testing** : DTLS validation, certificate checking, signed package verification, replay protection.
5. **IoT eSIM Certification Path** : From SGP.33-3 tests to production deployment. The multi-vendor test ecosystem.

### SGP.41 v1.0: In-Factory Profile Provisioning (NEW)
1. **SGP.41 Overview: In-Factory Profile Provisioning** : What IFPP is, why it exists, the 16-step provisioning flow.
2. **The IFPP Architecture** : SM-DPf (Factory SM-DP+), FPA (Factory Profile Assistant), Device Manufacturer, EUM roles.
3. **IFPP Flow: Manufacturing to Activation** : The two phases: manufacturing step and configuration step. Profile loading report.
4. **IFPP Security Model** : Factory trust, certificate chains, BPP encryption, profile installation verification.
5. **IFPP in Practice** : PC OEM eSIM provisioning (Windows), automotive manufacturing, IoT device factories.

---

<div align="center">

*Last updated: 2026-06-06 · Sources: GSMA SGP specifications v2.7, v3.2, v1.3, v1.16, v3.1.3, v2.1, v3.0.2, v1.1, v1.2, v1.0*

[🏠 eUICC.tech Home]({{ site.baseurl }}/)

</div>
