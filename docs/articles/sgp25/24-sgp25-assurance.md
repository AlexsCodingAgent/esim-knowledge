---
title: "eUICC Assurance Requirements: EAL4+ and Penetration Testing"
3|description: "Explains the SGP.25 EAL4+ assurance package : six evaluated assurance classes, AVA_VAN.5 advanced penetration testing with elevated attack potential, and why EAL4 is the highest practical level for commercial secure elements."
date: 2026-06-05
---

# eUICC Assurance Requirements: EAL4+ and Penetration Testing

**[eUICC.tech]({{ site.baseurl }}/) > [SGP.25 eUICC Security]({{ site.baseurl }}/docs/articles/sgp25/) > eUICC Assurance Requirements: EAL4+ and Penetration Testing**

> **Why this matters:** Security Functional Requirements define *what* the eUICC must do. Assurance Requirements define *how thoroughly we verify* it actually does those things: and at what level of rigour. For an eUICC that will store operator credentials worth millions and resist attackers with physical access to the device, "we tested the happy path" is not enough. EAL4+ with AVA_VAN.5 penetration testing means evaluators actively try to break the TOE using state-of-the-art attack techniques.

> **Key takeaways:**
> - SGP.25 mandates EAL4 augmented with ALC_DVS.2 (development security) and AVA_VAN.5 (advanced penetration testing)
> - EAL4 is the highest practical assurance level for commercial products: it requires low-level design, source code, independent testing, and vulnerability analysis
> - AVA_VAN.5 "Advanced methodical vulnerability analysis" subjects the TOE to penetration testing by evaluators with elevated attack potential, commensurate with Java Card products hosting sensitive applications
> - Six assurance classes are evaluated: Development (ADV), Guidance Documents (AGD), Life-Cycle Support (ALC), Security Target (ASE), Tests (ATE), and Vulnerability Assessment (AVA)
> - The optional ALC_FLR.2 component adds formal flaw reporting and remediation procedures
> - Architectural design refinements specifically require security domain separation and self-protection against tampering

Assurance is the confidence that the security functions work as specified: and that they cannot be bypassed, tampered with, or defeated. The EAL4+ package in SGP.25 represents the intersection of practical commercial development processes with the rigour needed for a security component that will be deployed in the field for a decade or more.

---

## Why EAL4?

SGP.25's security rationale explicitly justifies EAL4:

> "EAL4 is required for this type of TOE and product since it is intended to defend against sophisticated attacks. This evaluation assurance level allows a developer to gain maximum assurance from positive security engineering based on good practices. EAL4 represents the highest practical level of assurance expected for a commercial grade product."

Key reasons:

1. **Sophisticated attackers** : eUICCs face adversaries with physical access, specialised equipment, and strong motivation (cloning for fraud, network access theft)

2. **Long-lived credentials** : eUICC private keys and certificates must resist extraction for the product's entire operational life (10+ years)

3. **Multi-stakeholder trust** : Operators loading profiles, device manufacturers embedding chips, and end users all need confidence that the platform hasn't been compromised

4. **Source code access for evaluators** : EAL4 is the lowest level at which evaluators must review implementation representation (ADV_IMP.1) and TOE design (ADV_TDS.3), enabling meaningful vulnerability discovery

---

## The Six Assurance Classes

### Class ADV: Development

| Component | Name | What It Requires |
|-----------|------|-----------------|
| **ADV_ARC.1** | Architectural design | Security architecture description showing domains, self-protection, and non-bypassability |
| **ADV_FSP.4** | Functional specification | Complete functional specification of all TSF interfaces at the lowest level of abstraction |
| **ADV_IMP.1** | Implementation representation | Implementation representation for the entire TSF: source code available to evaluators |
| **ADV_TDS.3** | TOE design | Basic modular design describing the TSF architecture and subsystems |

**Architecture refinements** (Section 6.2.1): ADV_ARC.1 is refined with additional requirements beyond standard CC. The security architecture must describe security domains consistent with SFRs, demonstrate that the TSF protects itself from tampering by untrusted active entities, and demonstrate non-bypassability of SFR-enforcing functionality. The domain separation rules (A.APPLICATIONS) must be sufficient to maintain security for all applications loaded on the eUICC.

### Class AGD: Guidance Documents

| Component | Name | What It Requires |
|-----------|------|-----------------|
| **AGD_OPE.1** | Operational user guidance | Guidance for secure operation of the TOE |
| **AGD_PRE.1** | Preparative user guidance | Guidance for secure preparation and installation |

### Class ALC: Life-Cycle Support

| Component | Name | What It Requires |
|-----------|------|-----------------|
| **ALC_CMC.4** | CM capabilities | Production support, acceptance procedures, and configuration management |
| **ALC_CMS.4** | CM scope | Configuration management covering the TOE, evaluation evidence, and development tools |
| **ALC_DEL.1** | Delivery | Secure delivery procedures to prevent tampering during distribution |
| **ALC_DVS.2** | Development security | Sufficiency of physical, procedural, personnel, and technical security measures |
| **ALC_LCD.1** | Life-cycle definition | Defined life-cycle model with development, manufacturing, and operational phases |
| **ALC_TAT.1** | Tools and techniques | Well-defined development tools with configuration control |

#### ALC_DVS.2: Why the Augmentation?

The standard ALC_DVS.1 mandated by EAL4 is explicitly judged insufficient for an eUICC. The nature of the TOE: software that will protect operator credentials and enable network authentication: requires justification of the **sufficiency** of development security procedures to protect both confidentiality and integrity of the TOE and embedding product. This means the evaluator verifies not just that security measures exist, but that they are adequate given the threat model.

#### Optional ALC_FLR.2: Flaw Reporting Procedures

SGP.25 lists ALC_FLR.2 as an optional augmentation. When included, the developer must:

1. Establish formal flaw reporting procedures that track all reported security flaws in each TOE release
2. Act appropriately upon security flaw reports: analysing, fixing, and distributing corrections
3. Provide flaw remediation guidance so TOE users know how to submit reports
4. Know to whom to send corrective fixes

If selected, it must be added to the "Assurance Level" line of the PP identification.

### Class ASE: Security Target Evaluation

| Component | Name | What It Requires |
|-----------|------|-----------------|
| **ASE_CCL.1** | Conformance claims | Valid conformance claims to the PP and CC |
| **ASE_ECD.1** | Extended components | Definition and justification of any extended SFR/SAR components |
| **ASE_INT.1** | ST introduction | Complete ST introduction including TOE reference, overview, and description |
| **ASE_OBJ.2** | Security objectives | Complete mapping of security objectives to threats, OSPs, and assumptions |
| **ASE_REQ.2** | Derived security requirements | Complete mapping of SFRs to objectives with rationale |
| **ASE_SPD.1** | Security problem definition | Complete definition of threats, OSPs, and assumptions |
| **ASE_TSS.1** | TOE summary specification | How the TOE meets each SFR |

### Class ATE: Tests

| Component | Name | What It Requires |
|-----------|------|-----------------|
| **ATE_COV.2** | Coverage | Rigorous analysis of test coverage against functional specification |
| **ATE_DPT.1** | Depth | Testing based on the TOE design: test subsystems and interfaces |
| **ATE_FUN.1** | Functional tests | Functional testing per the functional specification |
| **ATE_IND.2** | Independent testing | Independent evaluator testing using a sample of the TOE |

### Class AVA: Vulnerability Assessment

| Component | Name | What It Requires |
|-----------|------|-----------------|
| **AVA_VAN.5** | Vulnerability analysis | Advanced methodical vulnerability analysis |

---

## AVA_VAN.5: Advanced Methodical Vulnerability Analysis

This is the most significant augmentation — and the most demanding. Standard EAL4 only requires AVA_VAN.3 ("Focused vulnerability analysis"), which involves searching public domain sources for potential vulnerabilities and conducting independent testing based on those findings.

AVA_VAN.5 raises the bar dramatically:

### What It Means

> "AVA_VAN.5 'Advanced methodical vulnerability analysis' is considered as the expected level for Java Card technology-based products hosting sensitive applications."

The evaluator:

1. **Searches** public domain sources (vulnerability databases, academic literature, conference proceedings) for potential vulnerabilities applicable to the TOE
2. **Analyses** the TOE's design, implementation, and guidance to identify potential vulnerabilities: this includes source code review, design analysis, and architectural assessment
3. **Devises penetration tests** based on the identified potential vulnerabilities: tests that actively attempt to compromise the TOE's security functions
4. **Executes** those penetration tests on the TOE in its operational configuration
5. **Documents** all findings with sufficient detail to enable reproducibility

### Attack Potential

The attack potential required for AVA_VAN.5 is **elevated** : evaluators must employ techniques commensurate with attackers who have:

- **Significant expertise** in smart card and embedded systems security
- **Specialised equipment** for side-channel analysis, fault injection, and protocol manipulation
- **Time and resources** beyond casual attackers

This includes, but is not limited to:
- Simple Power Analysis (SPA) and Differential Power Analysis (DPA)
- Electromagnetic emanation analysis
- Timing attacks against cryptographic operations
- Fault injection (voltage glitching, clock manipulation, electromagnetic pulses)
- Protocol fuzzing and state machine analysis

### Dependencies and Coverage

AVA_VAN.5 has dependencies on: ADV_ARC.1, ADV_FSP.1, ADV_TDS.3, ADV_IMP.1, AGD_PRE.1, and AGD_OPE.1. All of these are satisfied by EAL4. The architectural design documentation is particularly critical: the evaluator must understand the security domains and TSF self-protection mechanisms to design effective penetration tests.

---

## How Assurance and Functional Requirements Interlock

The assurance requirements validate the functional requirements by proving:

| Functional Area | How Assurance Validates It |
|----------------|---------------------------|
| Identification & Authentication | ADV_FSP.4 documents every interface; ATE_COV.2 ensures all are tested; AVA_VAN.5 attempts to bypass authentication |
| Secure Channels | ADV_TDS.3 documents channel protocols; ATE_DPT.1 tests subsystems; AVA_VAN.5 tests channel tampering |
| Security Domains | ADV_ARC.1 documents domain separation; ATE_IND.2 independently tests isolation; AVA_VAN.5 attempts cross-domain access |
| Side-Channel Resistance | FPT_EMS.1 declares the requirement; AVA_VAN.5 actively tests it through SPA/DPA |
| Key Management | ADV_IMP.1 provides source code; AVA_VAN.5 searches for key extraction vulnerabilities |

---

## Summary

- SGP.25 mandates EAL4 (highest practical commercial assurance) augmented with ALC_DVS.2 and AVA_VAN.5
- Six assurance classes cover Development, Guidance, Life-Cycle, Security Target, Tests, and Vulnerability Assessment
- AVA_VAN.5 requires penetration testing by evaluators with elevated attack potential: SPA/DPA, fault injection, protocol attacks
- ALC_DVS.2 requires demonstrably sufficient development security measures, beyond the standard EAL4 requirement
- Architectural design refinements specifically mandate domain separation and tamper self-protection
- The optional ALC_FLR.2 adds formal flaw reporting, creating an ongoing security lifecycle beyond initial certification

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp25/23-sgp25-security-requirements">eUICC Security Functional Requirements</a> · <a href="{{ site.baseurl }}/">Home</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp25/25-sgp25-physical-security">Physical Security: Side-Channel and Fault Injection Defences</a> →

</div>

---

*Based on GSMA SGP.25 v2.1 (3 February 2025) : eUICC for Consumer and IoT Devices Protection Profile, Sections 6.2 (Security Assurance Rationale) and 6.3.4 (Rationale for the Security Assurance Requirements), conformant to CC Part 3 [39]*


---

← Previous: [eUICC Security Functional Requirements](23-sgp25-security-requirements) | [Section Index](index) | Next: [Physical Security: Side-Channel and Fault Injection Defences](25-sgp25-physical-security) →
