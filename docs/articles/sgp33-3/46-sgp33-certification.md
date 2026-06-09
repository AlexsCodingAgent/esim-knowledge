---
title: "IoT eSIM Certification Path: From Test Cases to Production"
description: "Traces the IoT eSIM certification path from SGP.33-3 conformance testing to production deployment — covering multi-vendor test ecosystems, SAS-SM accreditation for eIM platforms, and current FFS limitations."
date: 2026-06-05
---

# IoT eSIM Certification Path: From Test Cases to Production

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.33-3 eIM Testing]({{ site.baseurl }}/docs/articles/sgp33-3/) > IoT eSIM Certification Path: From Test Cases to Production**

> **💡 Why this matters:** Passing SGP.33-3 test cases in a lab is one thing: getting an eIM product certified for production deployment in the IoT eSIM ecosystem is another. The certification path for IoT eSIM components is still evolving: unlike the mature consumer eSIM certification programme (with its well-established GSMA Test Events, SAS audits, and GlobalPlatform DLOAs), IoT eSIM certification is being built incrementally. Understanding the current state and future direction of IoT eSIM certification helps eIM vendors, IoT device manufacturers, and operators plan their compliance strategies.

> **Key takeaways:**
> - IoT eSIM certification builds on the existing GSMA compliance framework but must address multi-vendor test ecosystems where the eIM, IPA, SM-DP+, SM-DS, and eUICC may all come from different vendors
> - The eIM is tested as a standalone component (per SGP.33-3), but production deployment requires end-to-end interoperability with real IPAs, eUICCs, SM-DP+s, and SM-DSs: an area still marked FFS (For Future Study) in SGP.23
> - eIM/DUT combo testing: where the eIM is tested alongside a real Device Under Test with an actual IoT eUICC and IPA: bridges the gap between isolated conformance testing and real-world deployment
> - SAS-SM (Security Accreditation Scheme for Subscription Management) applies to eIM platforms, extending the SAS framework from eUICC manufacturing to remote management servers
> - The certification workflow mirrors SGP.23: vendor readiness → Optional Features declaration → test execution → review → approval: but with IoT-specific additions for eIM Configuration Data, eIM Package Retrieval mode, and multi-interface orchestration
> - As of v1.2, many test sequences remain FFS, making the current certification path partial: practical certification for eIM products is possible but focuses on ES9+' and ES11' interfaces adapted from proven consumer eSIM testing

SGP.33-3 v1.2 is a test specification, not a certification programme document. But the two are inseparable: test cases exist to support certification, and certification programmes require test cases. This article traces the path from an eIM implementation through testing to production deployment.

---

## The Multi-Vendor IoT Test Ecosystem

### Why Multi-Vendor Matters More for IoT

Consumer eSIM certification tests individual components (eUICC, LPAd/Device, SM-DP+, SM-DS) in isolation using simulators. This works because the consumer ecosystem has a relatively simple topology: Device ⟷ SM-DP+ ⟷ SM-DS, with the LPA as the on-device orchestrator.

IoT eSIM introduces a fundamentally more complex topology:

```
                   Operator
                      │
                 ES2+ │
                      ▼
  ┌─────────┐    ┌─────────┐
  │  SM-DP+ │◄──►│  SM-DS  │
  └────┬────┘    └────┬────┘
       │ES9+'         │ES11'
       ▼              ▼
  ┌─────────────────────────┐
  │          eIM            │  ← Remote server, multi-tenant
  └────────────┬────────────┘
               │ESipa
       ┌───────┴───────┐
       ▼               ▼
  ┌─────────┐    ┌─────────┐
  │  IPA    │    │  IPA    │  ← Many IoT devices
  │ (Device │    │ (Device │
  │   1)    │    │   2)    │
  └────┬────┘    └────┬────┘
       │ES10b         │ES10b
       ▼              ▼
  ┌─────────┐    ┌─────────┐
  │ eUICC   │    │ eUICC   │
  └─────────┘    └─────────┘
```

In this topology:

- The **eIM** may manage thousands of IoT devices, each with its own IPA and eUICC
- The eIM talks to multiple **SM-DP+s** (for profile delivery from different operators) and multiple **SM-DSs** (for event discovery)
- The **IPA** on each device must interoperate with the eIM via ESipa: an interface that, as of v1.2, has no defined test sequences
- Each device's **eUICC** stores eIM Configuration Data associating it with one or more eIMs

Multi-vendor interoperability is not just desirable: it's the core value proposition of the GSMA eSIM ecosystem.

---

## eIM/DUT Combo Testing

### Beyond Isolated Component Testing

SGP.33-3 tests the eIM in isolation using simulators. But production deployment requires the eIM to work with:

- **Real eUICCs** : not simulated ones. The eUICC must correctly verify eIM signatures, process PSMO/eCO commands, manage eIM Configuration Data, and generate properly signed notifications.
- **Real IPAs** : the device-side software that orchestrates profile downloads. The IPA must correctly implement ESipa functions: retrieving eIM Packages, delivering results, and forwarding notifications.
- **Real SM-DP+s and SM-DSs** : production servers that may have different TLS configurations, certificate chains, and behaviour than simulators.

### The FFS Gap

SGP.23 Section 7 ("End-to-End Testing") is explicitly marked **FFS (For Future Study)**. This means:

- There is currently **no standardised test methodology** for testing a complete IoT eSIM deployment with all real components
- Simulator-based testing can verify protocol compliance but cannot verify real-world interoperability
- Vendors must rely on bilateral interoperability testing or consortium test events to validate multi-vendor combinations

This gap is particularly significant for IoT because the eIM-to-IPA interface (ESipa) : the critical bridge between the remote management server and the device: has no standardised test cases at all as of v1.2.

---

## The Certification Workflow

### Adapting the SGP.23 Model

The IoT eSIM certification workflow follows the same general pattern as consumer eSIM (SGP.23), adapted for IoT-specific concerns:

#### Step 1: Vendor Readiness

The eIM vendor prepares:

1. **Implementation**: An eIM conforming to SGP.31/SGP.32 requirements
2. **Optional Features Declaration** (Table 4):
   - Does the eIM send TransactionId with eUICC Packages? (O_S_TRID)
   - Does the eIM support eIM Package Retrieval mode? (O_S_PKG_RETRIEVAL)
   - Does the eIM use TLS over ESipa? (O_S_ESIPA_HTTPS)
3. **IUT Settings** (Annex F):
   - `#IUT_RSP_VERSION` : SGP.22 version supported
   - `#IUT_EIM_ADDRESS` : FQDN of the eIM
   - `#IUT_EIM_ID` : Unique identifier (OID, FQDN, or proprietary)
   - `#IUT_TLS_VERSION` : Highest TLS version supported (at least v1.2)

#### Step 2: Test Execution

Tests execute in the General (eIM) Test Environment:

- Interface compliance testing (Section 4): Verify every API call across ESep, ES9+', ES11', and ESipa
- System behaviour testing (Section 5): Verify end-to-end procedures like Profile Enable via eIM Package Retrieval
- The Applicability Table (Table 5) determines which tests apply based on declared optional features

#### Step 3: Results and Approval

- Each test case receives a pass/fail/inconclusive verdict
- Failed tests may be re-executed after fixes
- Upon successful completion of all mandatory and applicable conditional tests, the product may proceed to certification

---

## SAS-SM Integration

### Extending SAS to Remote Management

The GSMA's **Security Accreditation Scheme** (SAS) has historically focused on:

- **SAS-UP** (UICC Production): eUICC manufacturing site security
- **SAS-SM** (Subscription Management): SM-DP+ and SM-DS platform security

With IoT eSIM, **SAS-SM applies to eIM platforms** as well. The eIM is a subscription management server: it remotely controls profile state, manages eIM configuration, and orchestrates profile downloads. As such, eIM platforms must meet the same security standards as SM-DP+ and SM-DS platforms:

- Secure key storage and management (eIM private keys for package signing)
- Access control and audit logging
- Network security and TLS configuration
- Operational security procedures

### How SGP.33-3 Connects to SAS

While SGP.33-3 doesn't directly reference SAS audit requirements, the test cases implicitly verify SAS-relevant security properties:

- **TLS configuration**: HTTPS test cases verify correct TLS v1.2 with approved cipher suites: matching SAS network security requirements
- **Certificate management**: Error cases for invalid/expired certificates verify the eIM implements proper certificate validation
- **Key usage**: The eIM must correctly sign eUICC Packages (`eimSignature`) and present valid TLS certificates on ESipa
- **Anti-replay**: The counterValue mechanism ensures commands cannot be replayed, supporting audit trail integrity

---

## The State of IoT eSIM Certification: Present and Future

### What's Testable Today (v1.2)

| Interface | Test Status | Certification Readiness |
|-----------|-------------|------------------------|
| **ES9+'** (eIM→SM-DP+) | Fully defined | Ready: adapted from proven SGP.23 LPAd tests |
| **ES11'** (eIM→SM-DS) | Fully defined | Ready: adapted from proven SGP.23 LPAd tests |
| **ESep** (eIM→eUICC) | Partially defined (FFS) | Limited: 9 functions defined but most test sequences FFS |
| **ESipa** (eIM→IPA) | Requirements only (FFS) | Not certifiable: all 11 function test sequences FFS |
| **Behaviour** (Profile Enable) | One test case defined | Conditional: only for eIMs with O_S_PKG_RETRIEVAL + O_S_ESIPA_HTTPS |

### What's Coming

The "For Future Study" annotations throughout SGP.33-3 indicate active development areas:

- **ESipa test sequences**: The 11 ESipa functions need detailed test cases covering nominal, retry, and error scenarios
- **ESep PSMO test sequences**: Enable, Disable, Delete, ListProfileInfo, and GetRat need completed test sequences
- **eIM Configuration test sequences**: AddEim, UpdateEim, DeleteEim, and ListEim need completed test cases
- **End-to-end testing**: Multi-component testing with real eUICCs, IPAs, and servers
- **Additional behaviour tests**: Disable, Delete, and error recovery procedures
- **Test Profiles and Provisioning Profiles**: Currently out of scope for v1.2

### Practical Certification Strategy

For eIM vendors seeking certification today, the pragmatic path is:

1. **Certify ES9+' and ES11' interfaces first** : these are the most mature, with complete test coverage adapted from SGP.23
2. **Conduct bilateral interoperability testing** for ESipa and ESep with partner IPA and eUICC implementations
3. **Prepare for SAS-SM audit** with appropriate key management and operational security
4. **Track SGP.33-3 evolution** : as FFS sections are filled in, expand certification scope

---

## Relationship to the Broader GSMA Certification Framework

SGP.33-3 does not exist in isolation. It connects to:

- **SGP.23** (RSP Test Specification): Provides the LPAd test cases that SGP.33-3 adapts for eIM testing. SGP.33-3 explicitly references SGP.23 section numbers for reused test sequences.
- **SGP.33-1** (IPA Test Specification): Tests the device-side IPA that the eIM communicates with via ESipa. Coordinated certification of IPA and eIM ensures end-to-end ESipa interoperability.
- **SGP.33-2** (SM-DP+ Test Specification): Tests the SM-DP+ that the eIM communicates with via ES9+'. Coordinated certification ensures profile delivery works end-to-end.
- **SGP.26** (RSP Test Certificates): Provides the test certificate infrastructure used throughout SGP.33-3 testing.
- **GlobalPlatform DLOA**: The Digital Letter of Approval framework applies to IoT components as it does to consumer eSIM components.

---

## 📋 Summary

- IoT eSIM certification requires multi-vendor testing across eIM, IPA, eUICC, SM-DP+, and SM-DS: a more complex ecosystem than consumer eSIM
- eIM/DUT combo testing bridges isolated conformance testing and real-world deployment, though end-to-end testing remains FFS in SGP.23
- The certification workflow follows the SGP.23 model: vendor readiness → Optional Features declaration → test execution → approval, with IoT-specific IUT settings
- SAS-SM extends to eIM platforms, requiring secure key management, TLS configuration, and operational security for remote management servers
- ES9+' and ES11' testing is certification-ready (adapted from SGP.23); ESep and ESipa testing is still maturing (FFS in v1.2)
- Practical certification today focuses on ES9+'/ES11' interfaces with bilateral interoperability testing filling the ESipa/ESep gap
- The specification connects to SGP.33-1, SGP.33-2, SGP.23, SGP.26, and the GlobalPlatform DLOA framework

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp33-3/45-sgp33-eim-security">eIM Security Testing: DTLS, Certificates, and Signed Packages</a> · <a href="{{ site.baseurl }}/">🏠 Home</a>

</div>

---

*Based on GSMA SGP.33-3 v1.2 (27 January 2025) : eUICC IoT Manager Test Specification, Sections 1–5, Annexes F–G; GSMA SGP.23 certification framework; GSMA SAS programme*


---

← Previous: [eIM Security Testing: DTLS, Certificates, and Signed Packages](45-sgp33-eim-security) | [Section Index](index)
