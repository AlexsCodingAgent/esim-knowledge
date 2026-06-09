---
title: "SGP.23 Certification: From Test Cases to DLOA"
description: "Traces the SGP.23 certification workflow — from vendor readiness through GSMA Test Events and SAS-accredited labs to the GlobalPlatform Digital Letter of Approval for production eSIM deployment."
date: 2026-06-05
---

# SGP.23 Certification: From Test Cases to DLOA

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.23 Test Specifications]({{ site.baseurl }}/docs/articles/sgp23/) > SGP.23 Certification: From Test Cases to DLOA**

> **💡 Why this matters:** Passing 800+ pages of test cases is only the beginning. The journey from a compliant implementation to a certified product involves GSMA Test Events, SAS-accredited labs, mandatory certification audits, and ultimately a GlobalPlatform Digital Letter of Approval (DLOA) : the portable certificate that gatekeeps access to production eSIM deployments.

> **Key takeaways:**
> - Certification follows a structured workflow: vendor readiness → GSMA Test Event → test execution → report → DLOA
> - GSMA Test Events are organised periodic sessions where vendors test against standardised GSMA test tools
> - SAS (Security Accreditation Scheme) certification is mandatory for eUICC production sites and is verified by SGP.23 test cases
> - The DLOA is a GlobalPlatform-specified digital certificate managed by a DLOA Registrar with a discovery base URL
> - SGP.23 Annex F defines `IUT_DLOA_URL` as the Discovery Base URL of the SE default DLOA Registrar
> - The specification supports SGP.22 versions v2.2 through v2.6, with version-specific applicability so products can certify against their target version (Note: SGP.22 v2.7, published April 2026, post-dates SGP.23 v1.16 and is not yet covered.)

SGP.23 is not just a test specification: it is the technical foundation of the GSMA's eSIM certification programme. This article traces the path from a vendor's implementation to a certified product that can be deployed in production networks.

---

## The GSMA Certification Ecosystem

The GSMA operates a multi-layered certification framework for consumer eSIM:

- **SGP.23 Test Specification** : The technical test cases (what gets tested)
- **GSMA Test Tools** : The official test harness and simulators (how testing is executed)
- **GSMA Test Events** : Periodic face-to-face sessions where vendors test their products
- **SAS (Security Accreditation Scheme)** : Mandatory site audits for eUICC manufacturing
- **GlobalPlatform DLOA** : The digital certificate issued upon successful completion

### What Gets Certified

Each of the four IUT types can earn certification independently:

- **eUICC Certification** : Confirms the chip correctly implements all mandatory ES8+, ES10a/b/c, and ES6 functions, returns valid EUICCInfo structures with the SAS accreditation number, and handles profiles per the specification
- **LPAd/Device Certification** : Confirms the device's LPA correctly orchestrates profile discovery, download, and local management
- **SM-DP+ Certification** : Confirms the server correctly handles profile ordering (ES2+), secure channel establishment (ES8+), LPA interaction (ES9+), and SM-DS integration (ES12)
- **SM-DS Certification** : Confirms the discovery server correctly manages events across ES11, ES12, and ES15

---

## The Certification Workflow

### Step 1: Vendor Readiness

Before a Test Event, the vendor:

1. Implements SGP.22 per the target version (v2.2 through v2.6) (Note: SGP.22 v2.7, published April 2026, post-dates SGP.23 v1.16 and is not yet covered.)
2. Completes the **Optional Features Table** : declaring which optional capabilities their product supports
3. Determines the applicable test cases using the **Applicability Table** (mandatory, conditional, or not applicable based on declared features)
4. Provides **IUT Settings** (Annex F) : product-specific details needed by the test tools:
   - `#IUT_RSP_VERSION` : Which SGP.22 version is implemented
   - `#IUT_SM_DP_ADDRESS` / `#IUT_SM_DS_ADDRESS_ES11` : Server addresses
   - `#IUT_LPAd_Confirmation` : How user confirmations are performed
   - `#IUT_DLOA_URL` : Discovery Base URL of the DLOA Registrar
   - `#SAS_ACREDITATION_NUMBER` : For eUICCs, the GSMA-issued SAS number

### Step 2: GSMA Test Event

Test Events are organised GSMA sessions where vendors connect their implementations to the official test tools. Key characteristics:

- Test environments are set up per SGP.23 Section 3: the appropriate simulators surround each IUT
- Test cases execute in a predefined order, building from basic interface checks to complex multi-step procedures
- Test results are recorded step-by-step with pass/fail criteria (explicit expected results per SGP.23 Section 2.2.5)
- The test tool generates a **test report** documenting every executed case and its outcome

### Step 3: SAS Accreditation (eUICC-Specific)

Every eUICC intended for production must carry a **SAS Accreditation Number** : proof that the manufacturing site has passed the GSMA's Security Accreditation Scheme audit. SGP.23 embeds this verification directly into test cases:

- `EUICCInfo2` must include `sasAcreditationNumber` with the correct value
- Test cases in Section 4.2 explicitly verify the presence and format of this field
- The SAS number provides end-to-end traceability from production to deployment

### Step 4: Test Report and Review

After test execution:

- Each test case receives a pass/fail verdict against its expected results
- Failed test cases may be re-executed after fixes (within the Test Event window or at a subsequent event)
- The test lab produces a formal test report documenting all results
- The report is reviewed for completeness and accuracy

### Step 5: Digital Letter of Approval (DLOA)

Upon successful completion of all mandatory and applicable conditional test cases:

- A **Digital Letter of Approval** is issued per the GlobalPlatform DLOA specification [19]
- The DLOA is a signed digital certificate stored on a DLOA Registrar, accessible via a Discovery Base URL
- The `IUT_DLOA_URL` setting in SGP.23 Annex F explicitly references this Discovery Base URL: confirming that SGP.23 testing feeds directly into the DLOA issuance pipeline
- The `Platform_Label` (as defined in the GlobalPlatform DLOA specification) identifies the certified product

The DLOA is portable: it can be presented to any operator or GSMA member as proof that the implementation has been independently verified against the SGP.23 test suite.

---

## Version Coverage and Evolution

SGP.23 v1.16 supports testing against multiple SGP.22 versions:

| SGP.22 Version | SGP.23 Reference | Status |
|---------------|-----------------|--------|
| v2.2 | Ref [2b] | Legacy, maintained for backward compatibility |
| v2.2.x (x≥1) | Ref [2c] | Minor revision testing |
| v2.3 | Ref [2d] | Adds DeviceInfo extensibility |
| v2.4 | Ref [2e] | Service-specific data, non-IMSI SUPI |
| v2.5 | Ref [2f] | Additional features |
| v2.6 | Ref [2] | Current primary reference |

(Note: SGP.22 v2.7, published April 2026, post-dates SGP.23 v1.16 and is not yet covered.)

The Applicability Table includes version-specific columns so that a product certifying against SGP.22 v2.3 is only tested against test cases relevant to v2.3. The `#IUT_RSP_VERSION` setting selects which column applies.

SGP.23 itself has evolved through 16 minor versions since v1.0 (June 2017), reflecting the continuous expansion of the eSIM ecosystem.

---

## What's Not (Yet) Tested

SGP.23 explicitly marks certain areas as **FFS (For Future Study)** or out of scope:

- **End-to-End Testing** (Section 7) : Testing the complete RSP ecosystem with all real components (eUICC + SM-DP+ + SM-DS + Device) is defined as FFS. Current testing isolates each component individually.
- **Test Profiles and Provisioning Profiles** : Out of scope for SGP.23 v1.16. Only Operational Profiles are tested.
- **Operator Component** : The Operator is out of scope for direct testing. It only appears as a simulator (`S_MNO`) for SM-DP+ ES2+ testing.
- **Device with cellular-only connectivity** : Out of scope for LPAd/Device testing (the device must support a non-cellular connection method to reach simulated servers).

---

## 📋 Summary

- Certification is a structured workflow: implement → declare features → attend Test Event → pass test cases → receive DLOA
- GSMA Test Events provide standardised, tool-driven validation against SGP.23 test cases
- SAS accreditation is mandatory for eUICC manufacturing and is verified within SGP.23 test cases
- The GlobalPlatform DLOA is the portable digital certificate of compliance, managed via a DLOA Registrar
- SGP.23 supports certification against SGP.22 v2.2 through v2.6 with version-specific applicability (Note: SGP.22 v2.7, published April 2026, post-dates SGP.23 v1.16 and is not yet covered.)
- End-to-end testing remains FFS, limiting current certification to per-component conformance

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp23/20-sgp23-server-testing">Testing the SM-DP+ and SM-DS</a> · <a href="{{ site.baseurl }}/">🏠 Home</a>

</div>

---

*Based on GSMA SGP.23 v1.16 (29 April 2025) : RSP Test Specification, Sections 1-3, Annex F (IUT Settings), GlobalPlatform DLOA specification [19], GSMA SAS programme*


---

← Previous: [Testing the SM-DP+ and SM-DS](20-sgp23-server-testing) | [Section Index](index)
