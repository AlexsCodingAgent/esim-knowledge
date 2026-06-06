---
title: "SGP.23-1 Overview: Testing the eUICC Itself"
date: 2026-06-05
---

# SGP.23-1 Overview: Testing the eUICC Itself

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.23-1 eUICC Testing]({{ site.baseurl }}/docs/articles/sgp23-1/) > SGP.23-1 Overview: Testing the eUICC Itself**

> **💡 Why this matters:** SGP.23 tests the entire eSIM ecosystem as an integrated system — but before any of that integration testing can happen, the eUICC chip itself must be proven compliant. SGP.23-1 is the 797-page test bible dedicated exclusively to the eUICC — the embedded chip at the heart of every eSIM device. If your eUICC can't pass these tests, nothing downstream works.

> **Key takeaways:**
> - SGP.23-1 is the eUICC-only companion to SGP.23, developed after SGP.23 was split into three documents (SGP.23-1, -2, -3) in 2018
> - The only Implementation Under Test (IUT) is the eUICC — all other components (SM-DP+, SM-DS, LPA, MNO) are simulated
> - Two testing scopes: interface compliance testing (Section 4) and system behaviour testing (Section 5)
> - Tests target SGP.22 V3.1 (the M2M/IoT RSP specification), covering ES6, ES8+, ES10a, ES10b, and ES10c interfaces
> - An Optional Features Table with 30+ mnemonic options lets eUICC vendors declare supported capabilities, driving conditional test applicability
> - SGP.23-1 feeds into the SAS-UP (SAS for UICC Production) certification path, with the SAS accreditation number verified in test cases

SGP.23-1 v3.1.3 (797 pages, 27 January 2025) is the GSMA's test specification for the eUICC component in isolation. Unlike the parent SGP.23 specification which tests all four IUT types together, SGP.23-1 zooms in on a single question: does this eUICC chip correctly implement every interface and behaviour defined in the RSP Technical Specification?

---

## Why SGP.23-1 Exists

The original SGP.23 (v1.0, June 2017) was a single 913-page document covering all four IUT types: eUICC, LPAd/Device, SM-DP+, and SM-DS. By 2018, the GSMA recognised that the eUICC's testing requirements were so extensive they warranted their own dedicated specification. SGP.23 was split into three documents:

- **SGP.23-1** — RSP Test Specification for the eUICC (this document)
- **SGP.23-2** — RSP Test Specification for the SM-DP+
- **SGP.23-3** — RSP Test Specification for the SM-DS and LPAd/Device

This split allowed the eUICC testing to evolve independently, targeting SGP.22 V3.1 (the M2M/IoT profile) rather than the consumer-focused SGP.22 V2.x series. SGP.23-1 now stands at v3.1.3 with multiple MEP (Multiple Enabled Profiles) test additions.

*(Note: SGP.33 is a separate family created later for IoT-specific testing — see SGP.33-3 articles.)*

---

## What Gets Tested

SGP.23-1 tests the eUICC across every interface defined for consumer/M2M Remote SIM Provisioning:

| Interface | Between | What's Tested |
|-----------|---------|---------------|
| **ES6** | Operator → eUICC | OTA management: `UpdateMetadata` for Operator services via SCP80/SCP81 |
| **ES8+** | SM-DP+ → eUICC | Secure end-to-end channel: `InitialiseSecureChannel`, `ConfigureISDP`, `StoreMetadata`, `ReplaceSessionKeys`, `LoadProfileElements` |
| **ES10a** | LDSd → eUICC | Profile discovery: `GetEuiccConfiguredAddresses`, `SetDefaultDpAddress` |
| **ES10b** | LPDd → eUICC | Profile download pipeline: `PrepareDownload`, `LoadBoundProfilePackage`, `GetEUICCChallenge`, `GetEUICCInfo`, notification management, `AuthenticateServer`, `CancelSession`, `LoadCRL`, `GetRAT`, `LoadRPMPackage` |
| **ES10c** | LUId → eUICC | Local profile management: `GetProfilesInfo`, `EnableProfile`, `DisableProfile`, `DeleteProfile`, `eUICCMemoryReset`, `GetEID`, `SetNickname` |

All commands are wrapped in STORE DATA APDUs and sent in a dedicated logical channel to the ISD-R (Issuer Security Domain - Root).

---

## The Optional Features Table

One of SGP.23-1's most important innovations is its granular Optional Features Table (Table 4). Unlike simple "supports/doesn't support" declarations, the table defines 30+ mnemonic options that drive conditional test applicability:

| Mnemonic | Feature |
|----------|---------|
| `O_E_NIST` | NIST P-256 curve for signing/verification |
| `O_E_BRP` | BrainpoolP256r1 curve |
| `O_E_FRP` | FRP256V1 (French national curve) |
| `O_E_SM2` | SM2 (Chinese national algorithm) |
| `O_E_LPAe` | eUICC-resident LPA support |
| `O_E_LPA_PROXY` | LPA Proxy support |
| `O_E_REUSE_OTPK` | One-time key pair reuse for retry |
| `O_E_2_PIR` | Two Profile Installation Results |
| `O_E_RPM` | Remote Profile Management |
| `O_E_ENTERPRISE` | Enterprise Profiles |
| `O_E_INTEGRATED` | Integrated eUICC (SoC-embedded) |
| `O_E_MEP` | Multiple Enabled Profiles |
| `O_E_DEVICE_CHANGE` | Device Change and Profile Recovery |
| `O_E_OS_UPDATE` | OS Update capability |

Each test case in the Applicability Table (Table 5) maps to conditional expressions: `M` (mandatory), `N/A` (not applicable), or `Ci` (conditional on specific option combinations). This ensures vendors are only tested against features they actually claim to support.

---

## How It Differs from SGP.23

The parent SGP.23 specification (v1.16) is a system-level test specification. Key differences:

- **SGP.23** tests four IUT types with cross-component interaction; **SGP.23-1** tests only the eUICC
- **SGP.23** targets SGP.22 V2.x (consumer); **SGP.23-1** targets SGP.22 V3.1 (M2M/IoT)
- **SGP.23** has 9 simulator types; **SGP.23-1** uses 5 simulators (S_Device, S_SM-DP+, S_SM-DS, S_MNO, S_LPAd)
- **SGP.23-1** has no VOID sections for LPAd, SM-DP+, or SM-DS testing — all those sections are explicitly VOID
- **SGP.23-1** includes Integrated eUICC testing via USB CCID (Annex J), a form factor not covered in SGP.23's consumer-focused testing

---

## Relationship with SAS-UP and SGP.25

SGP.23-1 sits in a broader certification ecosystem:

- **SAS-UP (Security Accreditation Scheme for UICC Production)**: eUICC manufacturing sites must pass SAS-UP audits. SGP.23-1 test cases verify that the `sasAcreditationNumber` is correctly embedded in `EUICCInfo2` and returned in `GetEUICCInfo` responses — linking the tested chip back to its accredited factory.
- **SGP.25**: The eUICC Security Requirements specification. SGP.23-1's security test cases (certificate validation, key operations, SCP03t channels) verify compliance with SGP.25's requirements.
- **SGP.23**: Full system testing. An eUICC that passes SGP.23-1 can then participate in SGP.23 system-level testing alongside real SM-DP+, SM-DS, and LPA components.
- **GlobalPlatform DLOA**: Upon successful completion of all applicable test cases, a Digital Letter of Approval is issued per GlobalPlatform specification [19].

---

## 📋 Summary

- SGP.23-1 is the 797-page eUICC-dedicated test specification, split from SGP.23 in 2018 to handle the eUICC's extensive testing requirements independently
- The only IUT is the eUICC; five simulators (S_Device, S_SM-DP+, S_SM-DS, S_MNO, S_LPAd) wrap it in a controlled test environment
- Interface compliance testing (Section 4) covers ES6, ES8+, ES10a/b/c — every API call with exact DER-encoded request/response verification
- System behaviour testing (Section 5) covers retry mechanisms, PPR enforcement, file structure, delete/enable/disable processes, and notifications
- A 30+ option Optional Features Table drives conditional applicability, ensuring each eUICC is tested only against its declared capabilities
- SGP.23-1 connects to SAS-UP for manufacturing certification and feeds into SGP.23 for full system-level interoperability testing

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

Next: [eUICC Test Architecture: Readers, Scripts, and GSMA Tools]({{ site.baseurl }}/docs/articles/sgp23-1/33-sgp23-1-architecture) →

</div>

---

*Based on GSMA SGP.23-1 v3.1.3 (27 January 2025) — RSP Test Specification for the eUICC, Sections 1–3*


---

[Section Index](index) | Next: [eUICC Test Architecture: Readers, Scripts, and GSMA Tools](33-sgp23-1-architecture) →


---

[Section Index](index) | Next: [eUICC Test Architecture: Readers, Scripts, and GSMA Tools](33-sgp23-1-architecture) →
