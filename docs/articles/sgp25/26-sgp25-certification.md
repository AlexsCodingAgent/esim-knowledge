---
title: "SGP.25 Certification: SAS-UP and the Evaluation Process"
description: "Traces SGP.25's certification process — Common Criteria evaluation through accredited labs, GSMA SAS-UP site audits, three evaluation models (composite/unified/hybrid), and the Security Target for product-specific assessment."
date: 2026-06-05
---

# SGP.25 Certification: SAS-UP and the Evaluation Process

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.25 eUICC Security]({{ site.baseurl }}/docs/articles/sgp25/) > SGP.25 Certification: SAS-UP and the Evaluation Process**

> **💡 Why this matters:** A Protection Profile is only as valuable as the certification process behind it. SGP.25 certification doesn't happen in a vacuum: it's embedded in a broader ecosystem of GSMA security accreditation (SAS), Common Criteria evaluation schemes, accredited laboratories, and the interoperability testing regime defined by SGP.23-1. Understanding the end-to-end certification journey reveals how an eUICC goes from a design document to a trusted component in live operator networks.

> **Key takeaways:**
> - SGP.25 certification follows Common Criteria evaluation workflows through nationally accredited laboratories under the CCRA mutual recognition framework
> - The GSMA Security Accreditation Scheme (SAS) provides the mandatory site audit layer: eUICC manufacturing and personalisation sites must hold SAS accreditation
> - Three evaluation models exist: composite evaluation (certified platform + eUICC on top), unified evaluation (whole product at once), and hybrid (certified IC + uncertified OS/RE)
> - SGP.23-1 testing and SGP.25 evaluation are complementary: SGP.23-1 verifies protocol conformance, while SGP.25 verifies security properties
> - A Security Target (ST) instantiates SGP.25 for a specific product, with the ST writer declaring SGP.22/SGP.32 version support, optional features, and delivery life-cycle
> - The certification ecosystem includes eSIM CA, EUM, accredited labs, certification bodies, and the GSMA SAS programme: each playing a defined trust role

SGP.25 certification is the gatekeeper for commercial eUICC deployment. Without a valid certificate, an eUICC cannot be trusted to host production operator profiles. This article traces the certification journey from PP conformance claims through laboratory evaluation to final certification: and situates SGP.25 within the broader GSMA security accreditation landscape.

---

## The Certification Ecosystem

### Actors and Their Roles

| Actor | Role in Certification |
|-------|----------------------|
| **GSMA** | PP author and maintainer; operates SAS programme; defines the overall security framework |
| **eSIM CA** | Trusted third-party issuing certificates to EUM, SM-DP+, and SM-DS; must ensure security of its own private keys |
| **EUM (eUICC Manufacturer)** | Develops the eUICC; engages an accredited lab; produces the Security Target and evaluation evidence |
| **Accredited Laboratory** | Conducts the CC evaluation: executes all EAL4+ assurance activities including AVA_VAN.5 penetration testing |
| **Certification Body** | National scheme operator (e.g., BSI, ANSSI) that reviews the Evaluation Technical Report and issues the certificate |
| **GSMA SAS Programme** | Audits and accredits eUICC manufacturing and personalisation sites for physical and procedural security |

### The eSIM CA Trust Anchor

The eSIM Certificate Authority (eSIM CA) is the root of trust for the entire public key infrastructure. SGP.25 places an objective on the operational environment:

> **OE.CI**: The eSIM CA is a trusted third-party for the purpose of authentication of the entities of the system. The eSIM CA provides certificates for the EUM, SM-DS and SM-DP+. The eSIM CA must ensure the security of its own private keys.

The eUICC stores the eSIM CA public key (D.PK.CI.ECDSA) in the ECASD: protected from unauthorised modification by the ECASD Access Control SFP. This public key is the ultimate verification anchor: it validates EUM certificates, which in turn validate individual eUICC certificates, which in turn authenticate the eUICC to SM-DP+ and SM-DS.

---

## The Three Evaluation Models

SGP.25's Protection Profile Usage section (1.2.5) defines three distinct paths for evaluation, depending on what is already certified:

### Model 1: Composite Evaluation (Platform Pre-Certified)

```
┌──────────────────────┐
│  Certified IC        │ ← Already holds [PP0084]/[PP0117] certificate
├──────────────────────┤
│  Certified OS        │ ← Already holds platform certificate
├──────────────────────┤
│  Certified RE (JCS)  │ ← Already holds [PP-JCS] certificate
├──────────────────────┤
│  eUICC Software      │ ← NEW evaluation against SGP.25 on top
└──────────────────────┘
```

The Security Target refers to the existing IC, OS, and RE Security Targets to fulfil the corresponding security objectives (OE.IC.*, OE.RE.*). The evaluation scope is limited to the eUICC-specific TOE: ISD-R, ISD-P, ECASD, and Platform Layer components.

This is the most common path for established eUICC manufacturers using certified Java Card platforms on certified secure ICs.

### Model 2: Unified Evaluation (Everything Evaluated Together)

```
┌──────────────────────┐
│  IC + OS + RE +      │ ← Single evaluation covering everything
│  eUICC Software      │     from hardware to application layer
└──────────────────────┘
```

The Security Target defines SFRs for the IC, OS, and RE in addition to those specified in SGP.25. This is a larger evaluation scope but avoids dependency on third-party certificates. It may be appropriate for vertically integrated manufacturers or novel platform architectures.

### Model 3: Hybrid (IC Certified + OS/RE Uncrtified)

```
┌──────────────────────┐
│  Certified IC        │ ← Already holds certificate
├──────────────────────┤
│  OS + RE +           │ ← NEW: composite evaluation of software
│  eUICC Software      │     on top of certified IC
└──────────────────────┘
```

The ST refers to the IC Security Target for hardware objectives and introduces SFRs for the OS and RE. This is a composite evaluation in the sense of [14] (Composite Product Evaluation), where the system composed of eUICC software + JCS + OS is evaluated on top of a certified IC.

---

## The Evaluation Workflow

### Step 1: Security Target Development

The vendor (EUM) develops a Security Target that:

1. **Declares conformance** to SGP.25 Base-PP (mandatory) and optionally to LPAe/IPAe PP-Modules
2. **Specifies the TOE** : which SGP.22/SGP.32 versions are implemented, which form factor (embedded/removable), SEP or MEP support
3. **Completes all assignments and selections** : filling in the italicised parameters left open by the PP (cryptographic algorithms, RNG classes, emission types, key destruction methods)
4. **Describes the life-cycle** : at which phase the self-protected TOE is delivered, which delivery activities are required
5. **Maps environmental objectives** : either by referencing existing certificates or by defining new SFRs
6. **Adds FCS_COP.1 requirements** : for all cryptographic operations mandated by SGP.22 (SCP03t key derivation, signature verification, shared secret computation) and network authentication algorithms

### Step 2: Laboratory Engagement

The vendor engages a CC-accredited evaluation laboratory (recognised under the national scheme where certification will be sought). The lab:

1. Reviews the Security Target for completeness and conformance (ASE_* assurance activities)
2. Examines the development evidence: functional specification (ADV_FSP.4), TOE design (ADV_TDS.3), implementation representation: source code (ADV_IMP.1), and security architecture (ADV_ARC.1)
3. Verifies configuration management (ALC_CMC.4, ALC_CMS.4), delivery procedures (ALC_DEL.1), development security (ALC_DVS.2), and life-cycle definition (ALC_LCD.1)
4. Reviews guidance documents (AGD_OPE.1, AGD_PRE.1)
5. Conducts or witnesses functional testing (ATE_FUN.1, ATE_COV.2, ATE_DPT.1)
6. Performs independent testing (ATE_IND.2)
7. Executes vulnerability analysis and penetration testing (AVA_VAN.5)

### Step 3: AVA_VAN.5 Execution

The penetration testing phase is the most intensive. Evaluators with elevated attack potential:

- Analyse the TOE design and implementation for potential vulnerabilities
- Search public sources for applicable attack techniques
- Devise and execute penetration tests targeting potential bypasses of SFRs
- Attempt side-channel attacks against FPT_EMS.1 claims
- Attempt fault injection against FPT_FLS.1 protections
- Test security domain isolation
- Attempt to extract or modify protected assets

### Step 4: Certification Report and Certificate Issuance

The lab produces an **Evaluation Technical Report** (ETR) documenting all findings. The national certification body reviews the ETR and, if satisfied, issues a **Common Criteria Certificate** and a **Certification Report**. Under the CCRA, this certificate is recognised by all 31 signatory nations.

---

## GSMA SAS-UP: The Site Accreditation Layer

While SGP.25 certifies the **product** (the eUICC software), the GSMA Security Accreditation Scheme (SAS) certifies the **site** where manufacturing and personalisation occur.

### What SAS Covers

SGP.25 explicitly references GSMA SAS in its life-cycle model:

> "Phase d: eUICC personalization covers the ECASD/ISD-R keys and optionally the addition of provisioning Profiles and Operational Profiles onto the eUICC."

The life-cycle notes specify that if Phases c and d are performed at the same **GSMA SAS-accredited** secure site, the eUICC Manufacturer is considered a trusted administrator, enabling TOE self-protection before the end of Phase d.

SAS also applies to ecosystem actors beyond the eUICC:

| Actor | SAS Requirement |
|-------|----------------|
| **SM-DP+** | "The SM-DP+ site must be accredited following GSMA SAS" (OE.SM-DP+) |
| **SM-DS** | "The SM-DS site must be accredited following GSMA SAS" (OE.SM-DS) |
| **eUICC Manufacturer** | SAS accreditation required for Phase d (personalisation) |

### SAS-UP: The eUICC Production Standard

SAS-UP (SAS for UICC Production) is the specific SAS scheme applicable to eUICC manufacturing and personalisation. It audits:

- Physical security of the production facility
- Access controls and personnel security
- Key management procedures (generation, injection, storage, destruction)
- Production process segregation
- Audit logging and incident response
- Secure transportation of products between phases

The SAS accreditation number embedded in the eUICC's `EUICCInfo2` structure (verified by SGP.23 test cases) provides traceability from the deployed product back to the accredited facility.

---

## Relationship with SGP.23-1 Testing

SGP.25 evaluation and SGP.23-1 testing are complementary but distinct:

| Aspect | SGP.23-1 (Test Specification) | SGP.25 (Protection Profile) |
|--------|------------------------------|----------------------------|
| **What it verifies** | Protocol conformance: does the eUICC implement SGP.22/SGP.32 correctly? | Security properties: does the eUICC resist defined threats? |
| **Methodology** | Scripted test cases with known expected results | Independent vulnerability analysis and penetration testing |
| **Attacker model** | Protocol-level misbehaviour | Sophisticated attacker with physical access, side-channel equipment |
| **Certification output** | Digital Letter of Approval (DLOA) | Common Criteria Certificate + Certification Report |
| **Governance** | GSMA Test Events + GlobalPlatform DLOA | National CC scheme + CCRA mutual recognition |

Both are required for a production-deployable eUICC:
- **SGP.23-1** proves it speaks the protocol correctly
- **SGP.25** proves it cannot be compromised while doing so

---

## Certificate Lifecycle

### Initial Certification

A certificate is valid for the specific TOE version evaluated, under the specific Security Target. Any change to security-relevant functionality requires either:

- **Re-evaluation** : for significant changes affecting SFRs or the TOE design
- **Assurance continuity** : for incremental changes that can be assessed against the existing certificate (impact analysis, delta evaluation)

### Maintenance and Recertification

The optional ALC_FLR.2 component ensures ongoing security:

1. Security flaws discovered post-certification are reported through formal channels
2. The developer analyses, fixes, and distributes corrections
3. Major fixes may trigger re-evaluation
4. The PP itself evolves: SGP.25 v2.1 replaced earlier versions, and future versions may add requirements

### Composite Certification for Applications

A secure application embedded into a certified eUICC can itself be certified in composition at a maximum assurance level of EAL4+ (the EAL of the base PP). If the application pursues higher assurance, it must do so outside composition: the additional evidence reinforces trust in the application but does not raise the platform's EAL.

---

## 📋 Summary

- SGP.25 certification follows CC evaluation through accredited labs under national schemes, with CCRA mutual recognition across 31 nations
- Three evaluation models accommodate different starting points: composite (pre-certified platform), unified (all at once), and hybrid (certified IC only)
- The Security Target is the vendor's instantiation of SGP.25: specifying TOE scope, cryptographic algorithms, delivery life-cycle, and platform dependencies
- GSMA SAS (specifically SAS-UP) provides the mandatory site accreditation layer, auditing manufacturing and personalisation facilities
- SGP.23-1 protocol testing and SGP.25 security evaluation are complementary: both are required for production deployment
- The certificate lifecycle extends beyond initial issuance through flaw reporting (ALC_FLR.2), assurance continuity, and composite certification for eUICC-resident applications

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp25/25-sgp25-physical-security">Physical Security: Side-Channel and Fault Injection Defenses</a> · <a href="{{ site.baseurl }}/">🏠 Home</a>

</div>

---

*Based on GSMA SGP.25 v2.1 (3 February 2025) : eUICC for Consumer and IoT Devices Protection Profile, Sections 1.2.3 (TOE life-cycle), 1.2.5 (Protection Profile Usage), 2 (Conformance Claims), 4.2 (Security Objectives for the Operational Environment: OE.CI, OE.SM-DP+, OE.SM-DS), 6.2 (Security Assurance Rationale), 6.3.4 (Rationale for the Security Assurance Requirements); GSMA SAS Programme; GlobalPlatform DLOA Specification [19]; SGP.23-1 RSP Test Specification*


---

← Previous: [Physical Security: Side-Channel and Fault Injection Defenses](25-sgp25-physical-security) | [Section Index](index)
