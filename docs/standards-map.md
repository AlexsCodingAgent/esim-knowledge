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
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 555" style="width:100%;max-width:960px;height:auto">
  <defs>
    <marker id="a-g" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#34d399"/>
    </marker>
    <marker id="a-b" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#5dade2"/>
    </marker>
    <marker id="a-a" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#fbbf24"/>
    </marker>
    <marker id="a-x" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
    <linearGradient id="sg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1b3a5c" stop-opacity="0.15"/>
      <stop offset="50%" stop-color="#1b3a5c" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#1b3a5c" stop-opacity="0.15"/>
    </linearGradient>
  </defs>

  <rect width="960" height="555" fill="#0a1628" rx="8"/>

  <!-- ═══ ROW 0: SGP.01 ROOT ═══ -->
  <rect x="330" y="16" width="300" height="48" rx="8" fill="rgba(167,139,250,0.1)" stroke="#a78bfa" stroke-width="1.8"/>
  <text x="480" y="37" fill="#a78bfa" font-family="system-ui,sans-serif" font-size="12.5" font-weight="700" text-anchor="middle">SGP.01</text>
  <text x="480" y="53" fill="#c8d6e5" font-family="system-ui,sans-serif" font-size="9" text-anchor="middle">eSIM Architecture Overview · 2007</text>

  <!-- Tree: SGP.01 → 3 branches -->
  <line x1="480" y1="64" x2="480" y2="78" stroke="#64748b" stroke-width="1.2"/>
  <line x1="168" y1="78" x2="792" y2="78" stroke="#64748b" stroke-width="1.2"/>
  <line x1="168" y1="78" x2="168" y2="93" stroke="#64748b" stroke-width="1.2" marker-end="url(#a-x)"/>
  <line x1="480" y1="78" x2="480" y2="93" stroke="#64748b" stroke-width="1.2" marker-end="url(#a-x)"/>
  <line x1="792" y1="78" x2="792" y2="93" stroke="#64748b" stroke-width="1.2" marker-end="url(#a-x)"/>

  <!-- ═══ COLUMNS ═══
       M2M (amber):     col x=26,  w=284, ctr=168, box x=38
       Consumer (green): col x=338, w=284, ctr=480, box x=350
       IoT (blue):      col x=650, w=284, ctr=792, box x=662
       Box width: 260  -->

  <!-- Category labels above columns -->
  <text x="168" y="93" fill="#fbbf24" font-family="system-ui,sans-serif" font-size="7.5" font-weight="600" text-anchor="middle" opacity="0.7">M2M RSP — Push</text>
  <text x="480" y="93" fill="#34d399" font-family="system-ui,sans-serif" font-size="7.5" font-weight="600" text-anchor="middle" opacity="0.7">Consumer RSP — Pull</text>
  <text x="792" y="93" fill="#5dade2" font-family="system-ui,sans-serif" font-size="7.5" font-weight="600" text-anchor="middle" opacity="0.7">IoT RSP — Proxy</text>

  <!-- ═══ ROW 1: COLUMN HEADERS ═══ -->
  <!-- M2M -->
  <rect x="38" y="98" width="260" height="46" rx="7" fill="rgba(251,191,36,0.08)" stroke="#fbbf24" stroke-width="1.5"/>
  <text x="168" y="119" fill="#fbbf24" font-family="system-ui,sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">SGP.02</text>
  <text x="168" y="135" fill="#7a8ba0" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">M2M RSP Architecture · Push model · 2010</text>

  <!-- Consumer -->
  <rect x="350" y="98" width="260" height="46" rx="7" fill="rgba(52,211,153,0.08)" stroke="#34d399" stroke-width="1.5"/>
  <text x="480" y="119" fill="#34d399" font-family="system-ui,sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">SGP.21</text>
  <text x="480" y="135" fill="#7a8ba0" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">RSP Architecture · 2014</text>

  <!-- IoT -->
  <rect x="662" y="98" width="260" height="46" rx="7" fill="rgba(93,173,226,0.1)" stroke="#5dade2" stroke-width="1.5"/>
  <text x="792" y="119" fill="#5dade2" font-family="system-ui,sans-serif" font-size="11.5" font-weight="700" text-anchor="middle">SGP.27 / SGP.28</text>
  <text x="792" y="135" fill="#7a8ba0" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">IoT Feasibility &amp; Requirements · 2019–20</text>

  <!-- M2M internal arrows (dashed — one spec, internal detail) -->
  <line x1="168" y1="144" x2="168" y2="157" stroke="#fbbf24" stroke-width="0.8" stroke-dasharray="3,3" marker-end="url(#a-a)"/>

  <!-- Consumer arrows -->
  <line x1="480" y1="144" x2="480" y2="157" stroke="#34d399" stroke-width="1" marker-end="url(#a-g)"/>

  <!-- IoT arrows -->
  <line x1="792" y1="144" x2="792" y2="157" stroke="#5dade2" stroke-width="1" marker-end="url(#a-b)"/>

  <!-- ═══ ROW 2 ═══ -->
  <!-- M2M: internal detail (dashed, lighter) -->
  <rect x="38" y="160" width="260" height="46" rx="6" fill="rgba(251,191,36,0.03)" stroke="#fbbf24" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="168" y="179" fill="#fbbf24" font-family="system-ui,sans-serif" font-size="10" font-weight="600" text-anchor="middle">Push-based provisioning</text>
  <text x="168" y="195" fill="#5a6d80" font-family="system-ui,sans-serif" font-size="7.5" text-anchor="middle">Network-driven · no LPA · ES1–ES5</text>

  <!-- Consumer -->
  <rect x="350" y="160" width="260" height="46" rx="6" fill="rgba(52,211,153,0.06)" stroke="#34d399" stroke-width="1.2"/>
  <text x="480" y="179" fill="#34d399" font-family="system-ui,sans-serif" font-size="11" font-weight="600" text-anchor="middle">SGP.22 v2.7</text>
  <text x="480" y="196" fill="#7a8ba0" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">RSP Technical Specification · 2015</text>

  <!-- IoT -->
  <rect x="662" y="160" width="260" height="46" rx="6" fill="rgba(93,173,226,0.08)" stroke="#5dade2" stroke-width="1.2"/>
  <text x="792" y="179" fill="#5dade2" font-family="system-ui,sans-serif" font-size="11" font-weight="600" text-anchor="middle">SGP.31 v1.3</text>
  <text x="792" y="196" fill="#7a8ba0" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">IoT Architecture &amp; Requirements · 2022</text>

  <!-- Arrows row 2→3 -->
  <line x1="168" y1="206" x2="168" y2="219" stroke="#fbbf24" stroke-width="0.8" stroke-dasharray="3,3" marker-end="url(#a-a)"/>
  <line x1="480" y1="206" x2="480" y2="219" stroke="#34d399" stroke-width="1" marker-end="url(#a-g)"/>
  <line x1="792" y1="206" x2="792" y2="219" stroke="#5dade2" stroke-width="1" marker-end="url(#a-b)"/>

  <!-- ═══ ROW 3 ═══ -->
  <!-- M2M -->
  <rect x="38" y="222" width="260" height="46" rx="6" fill="rgba(251,191,36,0.03)" stroke="#fbbf24" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="168" y="241" fill="#fbbf24" font-family="system-ui,sans-serif" font-size="10" font-weight="600" text-anchor="middle">ES1–ES8 interface family</text>
  <text x="168" y="257" fill="#5a6d80" font-family="system-ui,sans-serif" font-size="7.5" text-anchor="middle">ES1 (EUM) · ES2/ES3 (DP) · ES4–ES8 (SR+eUICC)</text>

  <!-- Consumer -->
  <rect x="350" y="222" width="260" height="46" rx="6" fill="rgba(52,211,153,0.06)" stroke="#34d399" stroke-width="1.2"/>
  <text x="480" y="241" fill="#34d399" font-family="system-ui,sans-serif" font-size="11" font-weight="600" text-anchor="middle">SGP.23 v1.16</text>
  <text x="480" y="258" fill="#7a8ba0" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">RSP Test Specification · 2016</text>

  <!-- IoT -->
  <rect x="662" y="222" width="260" height="46" rx="6" fill="rgba(93,173,226,0.08)" stroke="#5dade2" stroke-width="1.2"/>
  <text x="792" y="241" fill="#5dade2" font-family="system-ui,sans-serif" font-size="11" font-weight="600" text-anchor="middle">SGP.32 v1.3</text>
  <text x="792" y="258" fill="#7a8ba0" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">IoT Technical Specification · 2022</text>

  <!-- Arrows row 3→4 -->
  <line x1="168" y1="268" x2="168" y2="281" stroke="#fbbf24" stroke-width="0.8" stroke-dasharray="3,3" marker-end="url(#a-a)"/>
  <line x1="480" y1="268" x2="480" y2="281" stroke="#34d399" stroke-width="1" marker-end="url(#a-g)"/>
  <line x1="792" y1="268" x2="792" y2="281" stroke="#5dade2" stroke-width="1" marker-end="url(#a-b)"/>

  <!-- ═══ ROW 4 ═══ -->
  <!-- M2M -->
  <rect x="38" y="284" width="260" height="46" rx="6" fill="rgba(251,191,36,0.03)" stroke="#fbbf24" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="168" y="303" fill="#fbbf24" font-family="system-ui,sans-serif" font-size="10" font-weight="600" text-anchor="middle">Legacy status</text>
  <text x="168" y="319" fill="#5a6d80" font-family="system-ui,sans-serif" font-size="7.5" text-anchor="middle">SGP.02 stable · M2M+Consumer unified in SGP.22 v3.2</text>

  <!-- Consumer -->
  <rect x="350" y="284" width="260" height="46" rx="6" fill="rgba(52,211,153,0.06)" stroke="#34d399" stroke-width="1.2"/>
  <text x="480" y="303" fill="#34d399" font-family="system-ui,sans-serif" font-size="11" font-weight="600" text-anchor="middle">SGP.23-1 v3.1.3</text>
  <text x="480" y="320" fill="#7a8ba0" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">eUICC Test Specification · 2023</text>

  <!-- IoT -->
  <rect x="662" y="284" width="260" height="46" rx="6" fill="rgba(93,173,226,0.08)" stroke="#5dade2" stroke-width="1.2"/>
  <text x="792" y="302" fill="#5dade2" font-family="system-ui,sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">SGP.33 Family</text>
  <text x="792" y="318" fill="#7a8ba0" font-family="system-ui,sans-serif" font-size="8" text-anchor="middle">33-1 (IPA) · 33-2 (SM-DP+) · 33-3 (eIM) · 2023</text>

  <!-- Interface labels -->
  <text x="168" y="350" fill="#3a4d62" font-family="system-ui,sans-serif" font-size="7" text-anchor="middle">ES1 · ES2 · ES3 · ES4 · ES5 · ES8</text>
  <text x="480" y="350" fill="#3a4d62" font-family="system-ui,sans-serif" font-size="7" text-anchor="middle">ES2+ · ES8+ · ES9+ · ES10a/b/c · ES11</text>
  <text x="792" y="350" fill="#3a4d62" font-family="system-ui,sans-serif" font-size="7" text-anchor="middle">ESipa · ESeim · ESim</text>

  <!-- ═══ SHARED SPECS ═══ -->
  <rect x="25" y="372" width="910" height="22" rx="4" fill="url(#sg)"/>
  <text x="480" y="387" fill="#64748b" font-family="system-ui,sans-serif" font-size="9" font-weight="600" text-anchor="middle" letter-spacing="1.5">SHARED ACROSS ALL SPECIFICATIONS</text>

  <!-- 5 × 170w + 4 × 12g = 898, start=31 -->
  <rect x="31" y="404" width="170" height="44" rx="5" fill="rgba(148,163,184,0.05)" stroke="#64748b" stroke-width="1"/>
  <text x="116" y="425" fill="#94a3b8" font-family="system-ui,sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">SGP.24</text>
  <text x="116" y="439" fill="#64748b" font-family="system-ui,sans-serif" font-size="7.5" text-anchor="middle">Compliance Process</text>

  <rect x="213" y="404" width="170" height="44" rx="5" fill="rgba(251,113,133,0.06)" stroke="#fb7185" stroke-width="1"/>
  <text x="298" y="425" fill="#fb7185" font-family="system-ui,sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">SGP.25 v2.1</text>
  <text x="298" y="439" fill="#fb7185" font-family="system-ui,sans-serif" font-size="7.5" text-anchor="middle">Security Protection Profile</text>

  <rect x="395" y="404" width="170" height="44" rx="5" fill="rgba(148,163,184,0.05)" stroke="#64748b" stroke-width="1"/>
  <text x="480" y="425" fill="#94a3b8" font-family="system-ui,sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">SGP.26 v3.0.2</text>
  <text x="480" y="439" fill="#64748b" font-family="system-ui,sans-serif" font-size="7.5" text-anchor="middle">Test Certificates</text>

  <rect x="577" y="404" width="170" height="44" rx="5" fill="rgba(148,163,184,0.05)" stroke="#64748b" stroke-width="1"/>
  <text x="662" y="425" fill="#94a3b8" font-family="system-ui,sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">SGP.29 v1.1</text>
  <text x="662" y="439" fill="#64748b" font-family="system-ui,sans-serif" font-size="7.5" text-anchor="middle">EID Definition &amp; Assignment</text>

  <rect x="759" y="404" width="170" height="44" rx="5" fill="rgba(167,139,250,0.07)" stroke="#a78bfa" stroke-width="1"/>
  <text x="844" y="425" fill="#a78bfa" font-family="system-ui,sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">SGP.41 v1.0</text>
  <text x="844" y="439" fill="#a78bfa" font-family="system-ui,sans-serif" font-size="7.5" text-anchor="middle">IFPP Factory Provisioning</text>

  <!-- ═══ LEGEND ═══ -->
  <line x1="31" y1="468" x2="929" y2="468" stroke="#1b3a5c" stroke-width="1"/>

  <rect x="36" y="480" width="11" height="11" rx="2" fill="rgba(167,139,250,0.25)" stroke="#a78bfa" stroke-width="1"/>
  <text x="52" y="490" fill="#64748b" font-family="system-ui,sans-serif" font-size="8">Foundational</text>

  <rect x="175" y="480" width="11" height="11" rx="2" fill="rgba(52,211,153,0.18)" stroke="#34d399" stroke-width="1"/>
  <text x="191" y="490" fill="#64748b" font-family="system-ui,sans-serif" font-size="8">Consumer RSP (SGP.21–23-1)</text>

  <rect x="345" y="480" width="11" height="11" rx="2" fill="rgba(93,173,226,0.18)" stroke="#5dade2" stroke-width="1"/>
  <text x="361" y="490" fill="#64748b" font-family="system-ui,sans-serif" font-size="8">IoT RSP (SGP.27–33)</text>

  <rect x="485" y="480" width="11" height="11" rx="2" fill="rgba(251,191,36,0.18)" stroke="#fbbf24" stroke-width="1"/>
  <text x="501" y="490" fill="#64748b" font-family="system-ui,sans-serif" font-size="8">M2M Legacy</text>

  <rect x="590" y="480" width="11" height="11" rx="2" fill="rgba(251,113,133,0.15)" stroke="#fb7185" stroke-width="1"/>
  <text x="606" y="490" fill="#64748b" font-family="system-ui,sans-serif" font-size="8">Security</text>

  <rect x="675" y="480" width="11" height="11" rx="2" fill="rgba(148,163,184,0.12)" stroke="#64748b" stroke-width="1"/>
  <text x="691" y="490" fill="#64748b" font-family="system-ui,sans-serif" font-size="8">Shared / Supporting</text>

  <rect x="820" y="480" width="11" height="11" rx="2" fill="none" stroke="#64748b" stroke-width="1" stroke-dasharray="2,2"/>
  <text x="836" y="490" fill="#64748b" font-family="system-ui,sans-serif" font-size="8">Dashed = internal</text>
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
