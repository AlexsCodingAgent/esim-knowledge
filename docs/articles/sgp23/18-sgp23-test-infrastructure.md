---
title: "The GSMA eSIM Test Infrastructure"
3|description: "Details the GSMA eSIM conformance test infrastructure : a parallel PKI of test certificates and keys, six test profiles, nine simulator types, and numbered test environments that isolate each IUT."
date: 2026-06-05
---

# The GSMA eSIM Test Infrastructure

**[eUICC.tech]({{ site.baseurl }}/) > [SGP.23 Test Specifications]({{ site.baseurl }}/docs/articles/sgp23/) > The GSMA eSIM Test Infrastructure**

> **Why this matters:** You can't test an eSIM ecosystem with production SIMs and live servers: you need a parallel universe of test certificates, test keys, test profiles, and simulated servers. SGP.23's Annexes (A through K) define this entire parallel infrastructure, enabling deterministic, repeatable conformance testing without touching a live operator network.

> **Key takeaways:**
> - Test certificates and test keys (defined in Annex A.2) create a parallel PKI isolated from production GSMA certificates
> - Six test profiles (operational, provisioning) with known ICCIDs and metadata enable repeatable test scenarios
> - Nine simulator types (S_Device through S_SERVER) wrap each IUT in a fully controlled test environment
> - Test environments are numbered (TE_eUICC, TE_P1-P3, TE_S1-SR2) and map to specific IUT types
> - Test tools must implement DER encoding/decoding, APDU handling, TLS session management, and profile package generation
> - Integrated eUICCs (SoC-embedded) use USB CCID test interfaces per Annex J

Every SGP.23 test case executes within a controlled test environment: a carefully specified arrangement of the Implementation Under Test (IUT) and the simulators that surround it. This article unpacks the infrastructure that makes eSIM conformance testing possible.

---

## Test Certificates and Test Keys

SGP.23 defines a complete parallel PKI hierarchy, completely isolated from production certificates. Annex A.2 specifies:

- **CERT_S_SM_DPauth_ECDSA** : SM-DP+ authentication certificate (for `ES9+.InitiateAuthentication` mutual auth)
- **CERT_S_SM_DPpb_ECDSA** : SM-DP+ profile binding certificate (for `ES10b.PrepareDownload`)
- **CERT_S_SM_DP_TLS** : SM-DP+ TLS server certificate
- **CERT_S_SM_DS_TLS** : SM-DS TLS certificate
- **CERT_S_EUM_ECDSA** : Simulated EUM certificate
- **CERT_S_CI_ECDSA** : Simulated Certificate Issuer (root of trust for test)

Test eUICCs are pre-loaded with test certificates and keys, and pre-configured with the test CI's public key in their `euiccCiPKIdListForVerification` and `euiccCiPKIdListForSigning` lists. This means test setups don't touch the GSMA production CI: everything runs in a sandbox.

---

## Test Profiles

Annex E defines the profiles used in test cases. Each has a known ICCID, known metadata, and a known profile package (per the eUICC Profile Package Specification). References follow the pattern:

- `PROFILE_OPERATIONAL1`, `PROFILE_OPERATIONAL2`, … : normal consumer profiles
- `PROFILE_PROVISIONING1` : bootstrap/connectivity profiles (out of scope in SGP.23 v1.16)
- `PROFILE_TEST1` : profiles with known OTA keys for Device Test Mode (out of scope)

Each profile's metadata specifies: ICCID, Service Provider Name, Profile Name, Profile Class, Profile Policy Rules (PPRs), and notification addresses. By using standardised profiles, test cases can verify that an eUICC correctly parses metadata, enforces PPRs, and sends notifications to the expected addresses.

---

## The Nine Simulators

Test environments replace every real-world counterpart of the IUT with a simulator controlled by the test tool:

| Simulator | What It Replaces | When Used |
|-----------|-----------------|-----------|
| `S_Device` | Phone/modem | eUICC testing: sends APDUs over ISO 7816-4 |
| `S_SM-DP+` | Profile factory server | eUICC, LPAd, SM-DS testing |
| `S_SM-DS` | Discovery server | eUICC, LPAd, SM-DP+ testing |
| `S_MNO` | Mobile network operator | SM-DP+ ES2+ testing |
| `S_LPAd` | Device-side LPA | eUICC, SM-DP+, SM-DS testing |
| `S_LPAe` | eUICC-resident LPA | eUICC testing |
| `S_EndUser` | Human user | Device/LPAd testing (person or software) |
| `S_CLIENT` | HTTPS client | TLS testing on SM-DP+/SM-DS |
| `S_SERVER` | HTTPS server | TLS testing on SM-DP+/SM-DS |

Each simulator is the responsibility of test tool providers. They must handle DER encoding/decoding of ASN.1 structures, APDU command/response parsing, TLS session establishment, and profile package generation.

---

## Test Environments by IUT Type

### TE_eUICC: eUICC Test Environment

A removable eUICC (Java Card, one of the form factors from ETSI TS 102 221) connected to a PC/SC reader or custom hardware. The test system implements `S_Device`, `S_LPAd`, `S_MNO`, `S_SM-DP+`, and `S_SM-DS`. The eUICC is tested over its contact interface (ISO/IEC 7816-4), with ES6, ES8+, and ES10x commands tunnelled through APDUs.

The eUICC manufacturer must provide products compliant with Annex G.2 (eUICC Initial States), ensuring a known starting configuration before each test run.

### TE_Integrated eUICC: Integrated eUICC Testing

For eUICCs embedded in SoCs (System-on-Chip), where there is no physical UICC terminal interface, Annex J specifies a **USB CCID test interface**. The integrated eUICC must operate in card reader mode and support standard PC/SC messages (`PC_to_RDR_IccPowerOn`, `PC_to_RDR_XfrBlock`, `PC_to_RDR_T0APDU`, etc.). If USB is unavailable, an adapter (e.g., Bluetooth-to-USB) must be provided.

The manufacturer must ensure no other SoC subsystems interfere during testing.

### TE_P1/P2/P3: SM-DP+ Test Environments

- **TE_P1**: SM-DP+ tested over ES12 only: a simulated SM-DS on one side
- **TE_P2**: SM-DP+ tested over ES9+ only: a simulated LPAd on the other side
- **TE_P3**: Full SM-DP+ testing: simulated MNO on ES2+, simulated LPAd on ES9+, and simulated SM-DS on ES12 simultaneously

JSON input data is used for all SM-DP+ and SM-DS testing (ASN.1 format is out of scope for these components). TLS parameters and configurations can be defined per test case.

### TE_S1/S2/S3/SA1/SA2/SR1/SR2: SM-DS Test Environments

SM-DS testing is the most complex, with seven environments covering:

- **TE_S1**: SM-DS on ES11 (simulated LPA queries events)
- **TE_S2**: SM-DS on ES12 (simulated SM-DP+ registers/deletes events)
- **TE_S3**: Combined ES12 + ES11 testing
- **TE_SA1/SA2**: Alternative SM-DS testing, including ES15 cascading to Root SM-DS
- **TE_SR1/SR2**: Root SM-DS testing, receiving cascaded events via ES15 and serving ES11 queries

### Device/LPAd Test Environment

A complete Device Under Test containing a GSMA-compliant test eUICC (removable or soldered, not removed during testing). The test eUICC is pre-loaded with test certificates and is not itself under test. Simulated SM-DP+ and SM-DS servers are deployed on the network, with the test root certificate configured in the device for TLS trust.

---

## Dynamic Content, Constants, and IUT Settings

SGP.23 uses a notation system heavily:

- **`#NAME_OF_CONSTANT`** : Fixed values defined in Annex A (e.g., `#TEST_DP_ADDRESS1`, `#MATCHING_ID_1`, `#ACTIVATION_CODE_1`)
- **`<NAME_OF_VARIABLE>`** : Dynamic values generated by the IUT or test tool (e.g., `<EUICC_CI_PK_ID_TO_BE_USED>`, `<S_ENC>`, `<S_MAC>`)
- **`#IUT_NAME_OF_SETTING`** : Vendor-provided implementation details (e.g., `#IUT_RSP_VERSION`, `#IUT_LPAd_Confirmation`, `#IUT_SM_DP_ADDRESS`)

IUT settings (Annex F) cover product-specific information that test tool providers need: supported Java Card version, LPAd confirmation mechanisms, supported radio access technologies, and DLOA URLs.

---

## Summary

- A parallel PKI of test certificates and test keys isolates conformance testing from production GSMA infrastructure
- Six standardised test profiles with known ICCIDs and metadata enable repeatable scenarios
- Nine simulator types replace all real-world counterparts of the IUT
- Twelve+ numbered test environments map simulators to specific IUT types and interfaces
- Integrated eUICCs use USB CCID test interfaces (Annex J) instead of physical UICC contacts
- The constant/variable/IUT-setting notation system connects test case steps to concrete test data

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp23/17-sgp23-overview">SGP.23 Overview: How eSIM Interoperability Is Tested</a> · <a href="{{ site.baseurl }}/"> Home</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp23/19-sgp23-lpa-testing">Testing the LPA: LDS, LPD, and LUI Conformance</a> →

</div>

---

*Based on GSMA SGP.23 v1.16 (29 April 2025) : RSP Test Specification, Sections 3, Annexes A, B, E, F, G, J*


---

← Previous: [SGP.23 Overview: How eSIM Interoperability Is Tested](17-sgp23-overview) | [Section Index](index) | Next: [Testing the LPA: LDS, LPD, and LUI Conformance](19-sgp23-lpa-testing) →
