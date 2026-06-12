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

<div class="spec-diagram">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 620" style="width:100%;max-width:720px;height:auto">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#5a6d80"/>
    </marker>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#5dade2"/>
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#34d399"/>
    </marker>
    <marker id="arrow-amber" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#fbbf24"/>
    </marker>
    <linearGradient id="shared-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1b3a5c" stop-opacity="0.3"/>
      <stop offset="50%" stop-color="#1b3a5c" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#1b3a5c" stop-opacity="0.3"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="720" height="620" fill="#0a1628" rx="8"/>

  <!-- Row 0: SGP.01 -->
  <rect x="260" y="20" width="200" height="48" rx="6" fill="rgba(167,139,250,0.12)" stroke="#a78bfa" stroke-width="1.5"/>
  <text x="360" y="40" fill="#a78bfa" font-family="system-ui,sans-serif" font-size="12" font-weight="700" text-anchor="middle">SGP.01</text>
  <text x="360" y="55" fill="#c8d6e5" font-family="system-ui,sans-serif" font-size="10" text-anchor="middle">Architecture Overview</text>

  <!-- Arrows: SGP.01 → 3 branches -->
  <line x1="310" y1="68" x2="130" y2="115" stroke="#5a6d80" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="360" y1="68" x2="360" y2="115" stroke="#5a6d80" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="410" y1="68" x2="590" y2="115" stroke="#5a6d80" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Row 1: Architecture specs -->
  <rect x="40" y="120" width="180" height="48" rx="6" fill="rgba(251,191,36,0.08)" stroke="#fbbf24" stroke-width="1.5"/>
  <text x="130" y="140" fill="#fbbf24" font-family="system-ui,sans-serif" font-size="11" font-weight="700" text-anchor="middle">SGP.02</text>
  <text x="130" y="156" fill="#c8d6e5" font-family="system-ui,sans-serif" font-size="9" text-anchor="middle">M2M RSP Architecture</text>
  <text x="130" y="170" fill="#5a6d80" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">Push model · legacy</text>

  <rect x="270" y="120" width="180" height="48" rx="6" fill="rgba(52,211,153,0.08)" stroke="#34d399" stroke-width="1.5"/>
  <text x="360" y="140" fill="#34d399" font-family="system-ui,sans-serif" font-size="11" font-weight="700" text-anchor="middle">SGP.21</text>
  <text x="360" y="156" fill="#c8d6e5" font-family="system-ui,sans-serif" font-size="9" text-anchor="middle">RSP Architecture</text>
  <text x="360" y="170" fill="#5a6d80" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">Consumer RSP foundation</text>

  <rect x="500" y="120" width="180" height="48" rx="6" fill="rgba(93,173,226,0.1)" stroke="#5dade2" stroke-width="1.5"/>
  <text x="590" y="140" fill="#5dade2" font-family="system-ui,sans-serif" font-size="11" font-weight="700" text-anchor="middle">SGP.31</text>
  <text x="590" y="156" fill="#c8d6e5" font-family="system-ui,sans-serif" font-size="9" text-anchor="middle">IoT Architecture</text>
  <text x="590" y="170" fill="#5a6d80" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">Headless devices</text>

  <!-- Arrows: Row 1 → Row 2 -->
  <line x1="360" y1="168" x2="360" y2="200" stroke="#34d399" stroke-width="1.2" marker-end="url(#arrow-green)"/>
  <line x1="590" y1="168" x2="590" y2="200" stroke="#5dade2" stroke-width="1.2" marker-end="url(#arrow-blue)"/>

  <!-- Row 2: Technical specs -->
  <rect x="260" y="205" width="200" height="48" rx="6" fill="rgba(52,211,153,0.1)" stroke="#34d399" stroke-width="1.5"/>
  <text x="360" y="224" fill="#34d399" font-family="system-ui,sans-serif" font-size="11" font-weight="700" text-anchor="middle">SGP.22 v2.7 / v3.2</text>
  <text x="360" y="240" fill="#c8d6e5" font-family="system-ui,sans-serif" font-size="9" text-anchor="middle">RSP Technical Specification</text>

  <rect x="490" y="205" width="200" height="48" rx="6" fill="rgba(93,173,226,0.12)" stroke="#5dade2" stroke-width="1.5"/>
  <text x="590" y="224" fill="#5dade2" font-family="system-ui,sans-serif" font-size="11" font-weight="700" text-anchor="middle">SGP.32 v1.3</text>
  <text x="590" y="240" fill="#c8d6e5" font-family="system-ui,sans-serif" font-size="9" text-anchor="middle">IoT Technical Specification</text>

  <!-- Arrows: Row 2 → Row 3 -->
  <line x1="310" y1="253" x2="240" y2="290" stroke="#34d399" stroke-width="1.2" marker-end="url(#arrow-green)"/>
  <line x1="410" y1="253" x2="480" y2="290" stroke="#34d399" stroke-width="1.2" marker-end="url(#arrow-green)"/>
  <line x1="590" y1="253" x2="590" y2="290" stroke="#5dade2" stroke-width="1.2" marker-end="url(#arrow-blue)"/>

  <!-- Row 3: Test specs -->
  <rect x="160" y="295" width="160" height="45" rx="6" fill="rgba(52,211,153,0.06)" stroke="#34d399" stroke-width="1.2"/>
  <text x="240" y="313" fill="#34d399" font-family="system-ui,sans-serif" font-size="10" font-weight="700" text-anchor="middle">SGP.23 v1.16</text>
  <text x="240" y="328" fill="#c8d6e5" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">Consumer Test Spec</text>

  <rect x="400" y="295" width="160" height="45" rx="6" fill="rgba(52,211,153,0.06)" stroke="#34d399" stroke-width="1.5"/>
  <text x="480" y="313" fill="#34d399" font-family="system-ui,sans-serif" font-size="10" font-weight="700" text-anchor="middle">SGP.23-1 v3.1.3</text>
  <text x="480" y="328" fill="#c8d6e5" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">eUICC Test Spec</text>

  <rect x="530" y="295" width="160" height="45" rx="6" fill="rgba(93,173,226,0.08)" stroke="#5dade2" stroke-width="1.2"/>
  <text x="610" y="313" fill="#5dade2" font-family="system-ui,sans-serif" font-size="10" font-weight="700" text-anchor="middle">SGP.33-3 v1.2</text>
  <text x="610" y="328" fill="#c8d6e5" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">eIM Test Spec</text>

  <!-- Shared specs divider -->
  <rect x="30" y="370" width="660" height="28" rx="4" fill="url(#shared-grad)"/>
  <text x="360" y="389" fill="#5a6d80" font-family="system-ui,sans-serif" font-size="10" font-weight="600" text-anchor="middle" letter-spacing="2">SHARED ACROSS ALL SPECIFICATIONS</text>

  <!-- Row 4: Shared specs -->
  <rect x="30" y="410" width="118" height="48" rx="5" fill="rgba(148,163,184,0.06)" stroke="#64748b" stroke-width="1"/>
  <text x="89" y="430" fill="#94a3b8" font-family="system-ui,sans-serif" font-size="10" font-weight="700" text-anchor="middle">SGP.24</text>
  <text x="89" y="444" fill="#94a3b8" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">Compliance</text>

  <rect x="158" y="410" width="118" height="48" rx="5" fill="rgba(251,113,133,0.06)" stroke="#fb7185" stroke-width="1"/>
  <text x="217" y="430" fill="#fb7185" font-family="system-ui,sans-serif" font-size="10" font-weight="700" text-anchor="middle">SGP.25 v2.1</text>
  <text x="217" y="444" fill="#fb7185" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">Security PP</text>

  <rect x="286" y="410" width="118" height="48" rx="5" fill="rgba(148,163,184,0.06)" stroke="#64748b" stroke-width="1"/>
  <text x="345" y="430" fill="#94a3b8" font-family="system-ui,sans-serif" font-size="10" font-weight="700" text-anchor="middle">SGP.26 v3.0.2</text>
  <text x="345" y="444" fill="#94a3b8" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">Test Certs</text>

  <rect x="414" y="410" width="118" height="48" rx="5" fill="rgba(148,163,184,0.06)" stroke="#64748b" stroke-width="1"/>
  <text x="473" y="430" fill="#94a3b8" font-family="system-ui,sans-serif" font-size="10" font-weight="700" text-anchor="middle">SGP.29 v1.1</text>
  <text x="473" y="444" fill="#94a3b8" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">EID Standard</text>

  <rect x="542" y="410" width="148" height="48" rx="5" fill="rgba(167,139,250,0.08)" stroke="#a78bfa" stroke-width="1"/>
  <text x="616" y="430" fill="#a78bfa" font-family="system-ui,sans-serif" font-size="10" font-weight="700" text-anchor="middle">SGP.41 v1.0</text>
  <text x="616" y="444" fill="#a78bfa" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">IFPP Factory</text>

  <!-- Legend -->
  <line x1="30" y1="490" x2="690" y2="490" stroke="#1b3a5c" stroke-width="1"/>
  <rect x="40" y="502" width="10" height="10" rx="2" fill="rgba(167,139,250,0.3)" stroke="#a78bfa" stroke-width="1"/>
  <text x="55" y="511" fill="#5a6d80" font-family="system-ui,sans-serif" font-size="9">Foundational</text>
  <rect x="150" y="502" width="10" height="10" rx="2" fill="rgba(52,211,153,0.2)" stroke="#34d399" stroke-width="1"/>
  <text x="165" y="511" fill="#5a6d80" font-family="system-ui,sans-serif" font-size="9">Consumer RSP</text>
  <rect x="275" y="502" width="10" height="10" rx="2" fill="rgba(93,173,226,0.2)" stroke="#5dade2" stroke-width="1"/>
  <text x="290" y="511" fill="#5a6d80" font-family="system-ui,sans-serif" font-size="9">IoT</text>
  <rect x="340" y="502" width="10" height="10" rx="2" fill="rgba(251,191,36,0.2)" stroke="#fbbf24" stroke-width="1"/>
  <text x="355" y="511" fill="#5a6d80" font-family="system-ui,sans-serif" font-size="9">M2M Legacy</text>
  <rect x="460" y="502" width="10" height="10" rx="2" fill="rgba(251,113,133,0.15)" stroke="#fb7185" stroke-width="1"/>
  <text x="475" y="511" fill="#5a6d80" font-family="system-ui,sans-serif" font-size="9">Security</text>
  <rect x="550" y="502" width="10" height="10" rx="2" fill="rgba(148,163,184,0.15)" stroke="#64748b" stroke-width="1"/>
  <text x="565" y="511" fill="#5a6d80" font-family="system-ui,sans-serif" font-size="9">Shared/Supporting</text>
</svg>
</div>

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
