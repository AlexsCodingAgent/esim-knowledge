---
title: "eUICC Certification: From SGP.23-1 Tests to SAS-UP Approval"
description: "Traces the eUICC certification path — from declaring optional features and IUT settings through the Applicability Table to SAS-UP accreditation, DLOA issuance, and GSMA Test Event participation."
date: 2026-06-05
---

# eUICC Certification: From SGP.23-1 Tests to SAS-UP Approval

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.23-1 eUICC Testing]({{ site.baseurl }}/docs/articles/sgp23-1/) > eUICC Certification: From SGP.23-1 Tests to SAS-UP Approval**

> **💡 Why this matters:** Passing SGP.23-1's 797 pages of test cases isn't just an engineering milestone: it's a regulatory and commercial gateway. An eUICC that can't produce a valid DLOA (Digital Letter of Approval) backed by SAS-UP accreditation cannot be deployed in production devices. Understanding the certification workflow: from declaring optional features through test execution to final approval: reveals what separates a prototype eUICC from a production-ready one.

> **Key takeaways:**
> - Certification begins with the vendor declaring optional features and providing IUT settings (Annex F) : this determines the exact test suite
> - The Applicability Table (Table 5) maps every test case to M (mandatory), N/A (not applicable), or Ci (conditional) based on the vendor's declarations
> - A test execution passes only if the entire test procedure is carried out successfully; inconclusive results occur when setup issues prevent proper evaluation
> - The SAS accreditation number embedded in `EUICCInfo2` links tested eUICCs back to SAS-UP audited manufacturing sites
> - The final deliverable is a GlobalPlatform Digital Letter of Approval (DLOA), referenced in SGP.23-1 via GPC_SPE_095
> - SGP.23-1 certification feeds into SGP.23 system-level testing, where the certified eUICC participates as a known-good component
> - The GSMA runs regular Test Events where vendors bring implementations for formal conformance assessment

The certification path for an eUICC is a multi-stage process that transforms SGP.23-1's test cases from a specification document into a commercial credential. This article traces the journey from a vendor's first declaration through to the DLOA that unlocks production deployment.

---

## Stage 1: Declaration: The Optional Features and IUT Settings

Before a single test case executes, the eUICC vendor must declare what their product supports. This declaration has two parts:

### Optional Features Table (Table 4)

The vendor fills out a comprehensive capabilities declaration across 30+ options:

| Category | Example Options |
|----------|----------------|
| **Cryptographic Curves** | NIST P-256, BrainpoolP256r1, FRP256V1, SM2 |
| **LPA Features** | LPAe support, LPA Proxy |
| **Profile Management** | RPM, Enterprise Profiles, Device Change, OS Update |
| **MEP** | MEP-A1, MEP-A2, MEP-B, MEP-B without Refresh |
| **Form Factor** | Integrated eUICC (SoC-embedded) |
| **Unique Behaviours** | One-time key reuse for retry, catBusy error handling, 2 PIR support |

Each option is declared as `true` or `false`. A vendor may declare both values for the same option: but must provide separate samples configured for each value.

### IUT Settings (Annex F)

Vendor-specific implementation details that the test tool needs:

- `#IUT_RSP_VERSION` : Which SGP.22 version the eUICC implements
- `#IUT_LPAd_Confirmation` : How the device-side LPA confirms user operations
- `#IUT_MEP_LSI_OPTIONS` : LSI indication method (MANAGE LSI or T=1 NAD byte)
- `#IUT_EUICC_MULTIPLEXING_LSI_INDICATION` : MEP multiplexing configuration
- Java Card version, supported radio access technologies, and DLOA URLs

These settings ensure the test tool correctly configures its simulators to match the eUICC's expected interface.

---

## Stage 2: Applicability: Determining What to Test

The Applicability Table (Table 5, spanning pages 11–21) maps every test case to an applicability code based on the vendor's declarations:

| Code | Meaning | Example |
|------|---------|---------|
| **M** | Mandatory: must pass regardless of options | `TC_eUICC_ES8+.InitialiseSecureChannel` : every eUICC must handle secure channel setup |
| **N/A** | Not applicable: impossible in this context | `TC_eUICC_ES10b.GetEUICCInfo2_RSP_V2.1` : SGP.23-1 targets V3.1, so V2.1 is N/A |
| **Ci** | Conditional: applies only if specific options are set | `C001` = IF `O_E_NIST` THEN apply NIST-specific `PrepareDownload` tests |

Conditional codes use Boolean expressions with nesting: `IF ... THEN (IF ... THEN ... ELSE ...) ELSE ...`. This produces a tailored test suite: an eUICC supporting only NIST P-256 gets a different set of applicable tests than one also supporting Brainpool, MEP, and RPM.

**Critical rule**: If the vendor declares both `true` and `false` for an option (providing multiple samples), the test tool must run all applicable tests for each sample independently.

---

## Stage 3: Execution: Running the Test Suite

### Pre-Conditions

The eUICC must arrive at the test lab in a defined initial state (Annex G.2):
- Test certificates and keys pre-loaded
- `PROFILE_OPERATIONAL1` installed (usually in Disabled state)
- RAT configured for SEP or MEP as applicable
- Known file system structure (EF_UST, EF_DIR, EF_ICCID, etc.)

A clean-up procedure (Annex G.2.6) allows resetting the eUICC to its initial state between test runs.

### Pass Criteria (Section 2.2.5)

SGP.23-1 defines three outcomes for every test execution:

- **Pass** : The test procedure was fully carried out successfully; all expected results matched
- **Fail** : The tested feature provided unexpected behaviour at any step
- **Inconclusive** : Pass criteria cannot be evaluated due to issues during setup of initial conditions (including ICx steps) or during steps where no requirement is referenced

This three-state model prevents false negatives: if the test infrastructure has a problem, the eUICC isn't penalised.

### Test Environments

All eUICC tests run in one of two environments:
- **TE_eUICC** : Removable eUICC with PC/SC reader or custom hardware
- **TE_Integrated eUICC** : SoC-embedded eUICC with USB CCID test interface

---

## Stage 4: Results: The Test Report Structure

While SGP.23-1 doesn't prescribe a specific test report format, the structure is implicit in the specification:

1. **Declaration Summary** : The vendor's Optional Features Table and IUT Settings
2. **Applicability Matrix** : Which tests were applicable and why (M, N/A, or Ci with condition)
3. **Test Execution Log** : Per test sequence: initial conditions verified, steps executed, expected vs. actual results
4. **Signature Verifications** : Every eUICC-generated signature (`euiccSignPIR`, `euiccSignRPR`) was verified against `#PK_EUICC_SIG`
5. **Overall Result** : Pass (all applicable tests passed), Fail (one or more failures), or Inconclusive (setup issues prevented completion)

The report serves as evidence for the DLOA application and may be reviewed during SAS-UP audits.

---

## Stage 5: SAS-UP Integration

The SAS accreditation number (`sasAcreditationNumber`) is the critical link between SGP.23-1 testing and SAS-UP manufacturing certification:

### What SAS-UP Certifies

SAS-UP (Security Accreditation Scheme for UICC Production) audits the **eUICC manufacturing site** : not the eUICC design. It verifies:
- Physical security of the production facility
- Secure handling of eUICC cryptographic material during manufacturing
- Access controls, key injection procedures, and audit trails
- That the production process matches the certified design

### How SGP.23-1 Verifies the Link

SGP.23-1 test cases verify that:
- The eUICC correctly returns `sasAcreditationNumber` in `EUICCInfo2` responses
- The number matches the expected format and the accredited production site
- This confirms the eUICC was manufactured at a SAS-UP certified facility

Without this verification, an eUICC cannot be deployed commercially: the `sasAcreditationNumber` is checked during SGP.23 system testing and by operators during profile provisioning.

---

## Stage 6: The Digital Letter of Approval (DLOA)

Upon successful completion of all applicable test cases, a **Digital Letter of Approval** (DLOA) is issued per GlobalPlatform specification GPC_SPE_095 [19]. The DLOA:

- Is a portable, machine-verifiable certificate of compliance
- Contains the product identification, tested SGP.22 version, and applicable options
- Is issued by a recognised test laboratory
- Serves as evidence for GSMA certification and operator acceptance

The DLOA Registrar and Management System are referenced in SGP.23-1's architecture diagram (Section 3.1), connected via the `ESdloa` interface: though this interface is out of scope for SGP.23-1 testing.

---

## Integration with SGP.23 System Testing

An eUICC certified through SGP.23-1 becomes a "known-good" component for SGP.23 system-level testing:

1. **SGP.23-1 certification** : Proves the eUICC itself is compliant
2. **SGP.23 system testing** : The certified eUICC is used as a trusted component while testing SM-DP+, SM-DS, LPAd/Device implementations
3. **Full system certification** : When all components pass their respective test specifications, the complete eSIM ecosystem is certified

This layered approach means an SM-DP+ vendor testing under SGP.23 doesn't need to worry about eUICC bugs: they're using a pre-certified eUICC.

---

## The GSMA Test Event Cycle

The GSMA organises regular Test Events where vendors bring implementations for formal assessment:

- **Pre-event preparation**: Vendors run self-tests against the specification
- **Test event**: Formal execution of applicable test cases using standardised test tools
- **Issue resolution**: Failures are documented and may require specification clarification or implementation fixes
- **Re-testing**: Failed test cases are re-executed after fixes
- **Certification**: Successful completion leads to DLOA issuance

SGP.23-1's document history (Annex L) shows a steady stream of CRs (Change Requests) arising from Test Events: each one clarifying a test procedure that proved ambiguous during real-world testing. The document evolved from v2.0 Draft 0 (April 2018) through v3.1.3 (October 2023) with contributions from STMicroelectronics, FIME, and the eSIMWG3 working group.

---

## 📋 Summary

- Certification begins with the vendor's Optional Features declaration, which drives the Applicability Table to produce a tailored test suite
- Test execution uses strict pass/fail/inconclusive criteria, with inconclusive protecting against infrastructure issues
- The SAS accreditation number (`sasAcreditationNumber`) in `EUICCInfo2` connects SGP.23-1 compliance testing to SAS-UP manufacturing site certification
- A GlobalPlatform Digital Letter of Approval (DLOA) is the final deliverable: a portable, verifiable compliance certificate
- SGP.23-1 certification feeds into SGP.23 system testing, where the certified eUICC serves as a trusted component
- GSMA Test Events provide the formal venue for conformance assessment, with iterative CRs refining the specification based on real-world testing experience

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp23-1/35-sgp23-1-security">eUICC Security Testing: Certificates, Keys, and Channels</a> · <a href="{{ site.baseurl }}/">🏠 Home</a>

</div>

---

*Based on GSMA SGP.23-1 v3.1.3 (27 January 2025) : RSP Test Specification for the eUICC, Sections 2.1, 2.2, 3, Annexes F, G, L; GlobalPlatform GPC_SPE_095*


---

← Previous: [eUICC Security Testing: Certificates, Keys, and Channels](35-sgp23-1-security) | [Section Index](index)
