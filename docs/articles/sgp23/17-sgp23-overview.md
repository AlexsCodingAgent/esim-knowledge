---
title: "SGP.23 Overview: How eSIM Interoperability Is Tested"
date: 2026-06-05
---

# SGP.23 Overview: How eSIM Interoperability Is Tested

> **💡 Why this matters:** SGP.22 defines *what* an eSIM system must do. SGP.23 defines *how to prove it works* — the 913-page test specification that every eUICC, SM-DP+, SM-DS, and LPA implementation must pass before deployment. Understanding SGP.23 reveals the compliance regime that makes multi-vendor eSIM interoperability possible.

> **Key takeaways:**
> - SGP.23 tests four Implementation Under Test (IUT) types: eUICC, LPAd/Device, SM-DP+, and SM-DS
> - Two testing scopes — interface compliance testing and system behaviour testing — cover every interaction
> - Test environments use simulators (S_SM-DP+, S_SM-DS, S_LPAd, etc.) to isolate each component under test
> - An Optional Features Table and Applicability Table let vendors declare capabilities and determine which test cases apply
> - Certification culminates in a GlobalPlatform Digital Letter of Approval (DLOA), with SAS accreditation numbers embedded in the eUICC

SGP.23 v1.16 (913 pages) is the GSMA's test specification for the consumer Remote SIM Provisioning ecosystem. Where SGP.22 defines the protocol, SGP.23 defines the test cases that prove an implementation conforms to that protocol — covering every interface, every procedure, and every corner case defined by SGP.22 v2.2 through v2.6.

---

## The Test Ecosystem

### What Gets Tested

SGP.23 defines four categories of IUT (Implementation Under Test):

- **eUICC** — the embedded chip. Tested via ISO/IEC 7816-4 contact interface (removable form factor) or USB CCID (integrated eUICC in SoC). Tests verify ATR, ISD-R selection, ES8+ end-to-end channel operations, ES10a/b/c interface functions, and ES6 OTA management.
- **LPAd / Device** — the on-device profile assistant. Tested as a complete Device Under Test with a GSMA-compliant test eUICC, exercising ES9+ (to simulated SM-DP+), ES10a/b/c (to the test eUICC), ES11 (to simulated SM-DS), and all local profile management procedures.
- **SM-DP+** — the profile delivery server. Tested across three test environments: ES12 only (TE_P1), ES9+ only (TE_P2), and ES2+ with ES9+/ES12 combined (TE_P3), using simulated Operators, LPAs, and SM-DSs.
- **SM-DS** — the discovery server. Tested as either Root SM-DS or Alternative SM-DS, across ES11 (to simulated LPA), ES12 (to simulated SM-DP+), and ES15 (between cascaded SM-DSs).

### Two Testing Scopes

**Interface Compliance Testing** (Section 4): Verifies that every API call across every interface conforms to the ASN.1 structures and procedure flows defined in SGP.22. Each test case specifies exact request/response sequences with expected DER encoding, step-by-step.

**System Behaviour Testing** (Section 5): Verifies end-to-end functional behaviour — profile download and installation, mutual authentication, profile policy rule enforcement, notification handling, retry mechanisms, and device-level procedures like Add/Enable/Disable/Delete Profile.

### Who Uses SGP.23

- **Test tool developers** — implement the simulators and test harnesses
- **Vendors** (eUICC manufacturers, device makers, SM-DP+/SM-DS providers) — validate their products
- **Operators** — ensure interoperability across their deployment scenarios

---

## The Simulator Architecture

SGP.23 defines nine simulated components that surround the IUT, implemented by test tool providers:

| Simulator | Role |
|-----------|------|
| `S_Device` | Sends ISO/IEC 7816-4 commands to the eUICC under test |
| `S_SM-DP+` | Stands in for a real SM-DP+ during testing |
| `S_SM-DS` | Stands in for a real SM-DS |
| `S_MNO` | Simulates the Operator for ES2+ profile ordering |
| `S_LPAd` | Simulates the device-side LPA |
| `S_LPAe` | Simulates the eUICC-resident LPA |
| `S_EndUser` | Simulates user interactions (person or software) |
| `S_CLIENT` | HTTPS client for TLS testing |
| `S_SERVER` | HTTPS server for TLS testing |

The pattern is: `S_ComponentName` for a simulated component, `ComponentName` for the IUT. This isolation ensures that when the SM-DP+ is under test, its behaviour can be verified without depending on a real eUICC, LPA, or Operator.

---

## Optional Features and Applicability

Not every test case applies to every implementation. SGP.23 provides two key tables:

**Optional Features Table** — The vendor declares which optional capabilities their product supports. For eUICCs, this includes cryptographic curve support (NIST P-256, brainpoolP256r1, FRP256V1), CRL support, integrated eUICC form factor, LPAe support, one-time key reuse, and more. For SM-DP+s: session key usage, ES2+ retry, brainpoolP256r1 TLS. For Devices: SM-DS support, nickname display, combined Add+Enable operations, cellular-only connectivity.

**Applicability Table** — Maps every test case to an applicability code: `M` (mandatory), `N/A` (not applicable), or `Ci` (conditional — applies only if certain optional features are supported). This produces a tailored test suite for each implementation, keyed to the SGP.22 version under test (v2.2 through v2.6).

---

## SAS and the Accreditation Number

Every eUICC eligible for production deployment must carry a **SAS Accreditation Number** (`sasAcreditationNumber`), embedded in the `EUICCInfo2` structure. This number certifies that the eUICC manufacturing site has passed the GSMA's **Security Accreditation Scheme** (SAS) audit — a mandatory requirement for commercial eSIMs.

SGP.23 test cases verify that the eUICC correctly returns this number in its `GetEUICCInfo` response, confirming traceability from the test lab back to the accredited factory.

---

## The Path to Certification

The GSMA runs regular **Test Events** where vendors bring their implementations to be tested against a standardised test harness. The workflow:

1. Vendor declares optional features and SGP.22 version support
2. Applicability Table determines which test cases must pass
3. Testing executes in the relevant test environments (TE_eUICC, TE_P1-P3, TE_S1-SR2)
4. Test results are recorded and reviewed
5. Upon successful completion, a **Digital Letter of Approval** (DLOA) is issued per the GlobalPlatform DLOA specification

The DLOA serves as a portable certificate of compliance — a product that holds a valid DLOA has been independently verified against the SGP.23 test suite.

---

## 📋 Summary

- SGP.23 is the 913-page GSMA test specification covering every SGP.22 interface and behaviour for consumer eSIM
- Four IUT types (eUICC, LPAd/Device, SM-DP+, SM-DS) are tested using isolated simulator environments
- Two testing scopes (interface compliance + system behaviour) span ES2+, ES6, ES8+, ES9+, ES10a/b/c, ES11, ES12, and ES15
- Optional Features and Applicability tables ensure each implementation is tested against relevant requirements only
- SAS accreditation numbers and the GlobalPlatform DLOA link testing to production certification

---

*Based on GSMA SGP.23 v1.16 (29 April 2025) — RSP Test Specification*
