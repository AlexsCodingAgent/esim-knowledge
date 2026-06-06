---
title: "eIM Test Architecture: Simulated eIM and Reference IPA"
date: 2026-06-05
---

# eIM Test Architecture: Simulated eIM and Reference IPA

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.33-3 eIM Testing]({{ site.baseurl }}/docs/articles/sgp33-3/) > eIM Test Architecture: Simulated eIM and Reference IPA**

> **💡 Why this matters:** Testing the eUICC IoT Manager (eIM) is architecturally unique: it's a *server* under test, not a chip or a device. Unlike eUICC testing (where a physical card sits on a reader) or LPAd testing (where a device runs test software), the eIM is a remote network service that must be tested across four different simulated counterparts simultaneously. Understanding how SGP.33-3 constructs this test environment reveals the engineering challenge of proving that an IoT remote management server works correctly before it ever touches a real IoT device.

> **Key takeaways:**
> - The eIM is the sole Implementation Under Test (IUT) : all other components (SM-DP+, SM-DS, eUICC, IPA) are simulators implemented by the test tool provider
> - Five simulator types surround the eIM: S_SM-DP+ (ES9+'), S_SM-DS (ES11'), S_eUICC (ESep), S_IPA (ESipa), and S_CLIENT/S_SERVER (TLS testing)
> - Four interfaces are in scope for eIM testing: ESep, ES9+', ES11', and ESipa: while ES2+, ES6, ES8+, ES9+, ES10a, ES10b, ES11, and ES12 are out of scope
> - The test architecture mirrors the IoT eSIM reference architecture from SGP.31/SGP.32, with the eIM positioned as the central orchestrator between the IoT Device, SM-DP+, and SM-DS
> - Test environments mirror those from SGP.23 but adapted for IoT-specific interfaces: the eIM plays the role of LPAd for ES9+' and ES11' testing
> - Test tools MUST implement all simulators; the specification provides methods (MTD_*) and procedures (PROC_*) as building blocks, but leaves implementation details to tool providers

SGP.33-3 v1.2 defines a test architecture where the eIM sits at the centre of a simulated IoT eSIM ecosystem. Every other component is a simulator: this isolation is essential because the eIM is a server, and you cannot test a server's protocol behaviour without controlled, deterministic counterparts.

---

## The General (eIM) Test Environment

The test environment (Section 3.2.3.1) places the eIM IUT at the centre of four simulated interfaces:

```
                S_SM-DP+
                   |
                 ES9+'
                   |
  S_SM-DS: ES11' : IUT (eIM) : ESep: S_eUICC
                   |
                 ESipa
                   |
                 S_IPA
```

The test environment consists of:
- **IUT**: The eUICC IoT Manager under test: the real implementation
- **S_SM-DP+**: A simulated SM-DP+ supporting ES9+' connections
- **S_SM-DS**: A simulated SM-DS supporting ES11' connections
- **S_eUICC**: A simulated eUICC supporting ESep connections
- **S_IPA**: A simulated IPA supporting ESipa connections

Implementation of all simulators is the responsibility of the test tool providers. The test tools must also implement S_CLIENT and S_SERVER simulators for TLS-level testing: these MAY be the same as S_SM-DP+ or S_SM-DS depending on which component is under test.

---

## Interfaces In Scope vs. Out of Scope

SGP.33-3 defines a clear boundary for what is tested:

### In Scope (eIM Responsibilities)

| Interface | Between | Description | Tested |
|-----------|---------|-------------|--------|
| **ESep** | eIM → eUICC | Logical end-to-end interface for eUICC Packages (Profile State Management and eIM Configuration) | ✓ |
| **ES9+'** | eIM → SM-DP+ | Secure transport for Bound Profile Package delivery, with eIM acting as LPAd | ✓ |
| **ES11'** | eIM → SM-DS | Event Record retrieval from SM-DS, with eIM acting as LPAd | ✓ |
| **ESipa** | eIM → IPA | Trigger profile download at IPA; secure transport for eUICC Package delivery; notification handling | ✓ |

### Out of Scope (Other Components' Responsibilities)

| Interface | Between | Description |
|-----------|---------|-------------|
| **ES2+** | Operator → SM-DP+ | Profile ordering |
| **ES6** | Operator → eUICC | OTA management of Operator services |
| **ES8+** | SM-DP+ → eUICC | Secure end-to-end channel for ISD-P administration |
| **ES9+** | SM-DP+ → IPA | Secure transport for Bound Profile Package (IPA-side) |
| **ES10a** | IPA → eUICC | Profile discovery |
| **ES10b** | IPA → eUICC | Transfer Bound Profile Package to eUICC |
| **ES11** | IPA → SM-DS | Event Record retrieval (IPA-side) |
| **ES12** | SM-DP+ → SM-DS | Event Registration management |

This scoping means SGP.33-3 tests the eIM as the IoT remote management orchestrator: how it talks to profile servers, discovery servers, eUICCs, and the device-side IPA.

---

## How the eIM Reuses SGP.23 Test Sequences

A distinctive feature of SGP.33-3 is its extensive reuse of SGP.23 test cases. Rather than redefining every test from scratch, SGP.33-3 frequently states: *"This test sequence is the same as SGP.23 [32] ... where the eIM plays the role of LPAd."*

This applies to:

- **ES9+' testing** (Sections 4.2.10–4.2.15): The eIM communicates with SM-DP+ using the same ES9+ interface the LPA uses in consumer eSIM, but over the IoT-specific ES9+' variant. Test cases for InitiateAuthentication, GetBoundProfilePackage, AuthenticateClient, HandleNotification, CancelSession, and HTTPS are all adapted from SGP.23's LPAd test cases.

- **ES11' testing** (Sections 4.2.16–4.2.18): The eIM communicates with SM-DS using the same patterns as the LPA's ES11 communication in consumer eSIM.

This reuse gives SGP.33-3 a foundation of proven test methodology while allowing IoT-specific additions (ESep, ESipa, eIM configuration) to be the focus of new test development.

---

## The ESipa Interface: New Test Territory

The ESipa interface (eIM-to-IPA) is the most IoT-specific interface tested in SGP.33-3. It defines 11 functions:

1. **InitiateAuthentication** (SM-DP+/SM-DS authentication via eIM)
2. **GetBoundProfilePackage** (delivery and binding of Profile Package)
3. **AuthenticateClient** (eUICC authentication by SM-DP+/SM-DS)
4. **InitiateAuthentication** (second variant)
5. **GetBoundProfilePackage** (second variant)
6. **AuthenticateClient** (second variant)
7. **TransferEimPackage** (single eIM Package to IPA)
8. **GetEIMPackage** (IPA retrieves eIM Package)
9. **ProvideEimPackageResult** (IPA delivers eIM Package Result with optional Notifications)
10. **HandleNotification** (IPA notifies eIM of profile state changes)
11. **CancelSession** (eIM cancels ongoing RSP session)

As of v1.2, the test sequences for all ESipa functions are marked **FFS (For Future Study)** : a recognition that the eIM-to-IPA interface testing methodology is still maturing. However, the behaviour testing section (Section 5) does contain a concrete test case for Profile Enable via ESipa (TC_eIM_ProfileEnable_TLS_eIM_Pkg_Retrieval).

---

## Test Methods and Procedures

SGP.33-3 defines a library of reusable test building blocks:

### Methods (Annex C.1)
- **MTD_TLS_CLIENT_HELLO** / **MTD_TLS_SERVER_HELLO_ETC** / **MTD_TLS_CLIENT_KEY_EXCH_ETC** / **MTD_TLS_SERVER_END**: TLS v1.2 handshake building blocks
- **MTD_HTTP_REQ_ESIPA** / **MTD_HTTP_RESP_ESIPA**: ESipa HTTP request/response wrappers
- **MTD_GET_EIM_PACKAGE** / **MTD_PROVIDE_EIM_PACKAGE_RESULT**: JSON-formatted ESipa messages
- **MTD_HANDLE_NOTIF** / **MTD_HANDLE_NOTIF_EIM_PACKAGE_RESULT**: Notification handling messages

### Procedures (Annex C.2)
- **PROC_TLS_INITIALIZATION_SERVER_AUTH_ESIPA**: TLS v1.2 with Server authentication on ESipa (using Variant O certificate)
- **PROC_TLS_INITIALIZATION_SERVER_AUTH**: TLS v1.2 with Server authentication on ES9+' or ES11'
- **PROC_ES9+'_HANDLE_NOTIF_EN1** / **PROC_ES9+'_HANDLE_NOTIF_DIS2**: Notification handling procedures

---

## The Test eUICC Configuration

The simulated eUICC (S_eUICC) must be pre-configured for eIM testing (Annex G):

- Configured with ISD-R AID and a test EID (#EID1)
- Contains no Profiles initially (operational profiles are loaded per test case)
- Default SM-DS address: #TEST_ROOT_DS_ADDRESS
- Default SM-DP+ address: #TEST_DP_ADDRESS1
- ECASD configured with eUICC Private Key (#SK_EUICC_ECDSA), eUICC Certificate (#CERT_EUICC_ECDSA), CI Public Key (#PK_CI_ECDSA), and EUM Certificate (#CERT_EUM_ECDSA)
- The eIM must be pre-associated to the S_eUICC with eIM Configuration Data (including eimID) before behaviour test cases

---

## 📋 Summary

- The eIM is tested in isolation as the sole IUT, surrounded by five simulator types controlled by the test tool provider
- Four interfaces are in scope (ESep, ES9+', ES11', ESipa) while eight are out of scope: focusing testing on the eIM's role as IoT remote management orchestrator
- Most ES9+' and ES11' test cases are adapted from SGP.23's LPAd test cases with the eIM playing the role of LPAd
- The ESipa interface (eIM-to-IPA) represents new test territory with 11 functions defined but test sequences still marked FFS in v1.2
- Reusable methods (MTD_*) and procedures (PROC_*) provide building blocks for test tool implementers
- The simulated eUICC must be pre-configured with keys, certificates, and eIM association data before behaviour testing

---

<div align="center">

← Previous: [SGP.33 Overview: The IoT eSIM Test Family]({{ site.baseurl }}/docs/articles/sgp33-3/42-sgp33-overview) · [🏠 Home]({{ site.baseurl }}/)

Next: [Key eIM Test Cases: PSMO, Notifications, and Configuration]({{ site.baseurl }}/docs/articles/sgp33-3/44-sgp33-eim-test-cases) →

</div>

---

*Based on GSMA SGP.33-3 v1.2 (27 January 2025) : eUICC IoT Manager Test Specification, Sections 3, Annexes A–D, G*


---

← Previous: [SGP.33 Overview: The IoT eSIM Test Family](42-sgp33-overview) | [Section Index](index) | Next: [Key eIM Test Cases: PSMO, Notifications, and Configuration](44-sgp33-eim-test-cases) →
