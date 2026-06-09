---
title: "Key eIM Test Cases: PSMO, Notifications, and Configuration"
description: "Covers key SGP.33-3 eIM test cases: Profile State Management Operations via ESep, eIM Configuration management, notification handling across ES9+', and ESipa profile download orchestration."
date: 2026-06-05
---

# Key eIM Test Cases: PSMO, Notifications, and Configuration

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.33-3 eIM Testing]({{ site.baseurl }}/docs/articles/sgp33-3/) > Key eIM Test Cases: PSMO, Notifications, and Configuration**

> **💡 Why this matters:** The eIM's job is to remotely manage what happens on IoT devices: enabling and disabling profiles, handling configuration changes, and processing notifications about profile state: all without any End User pressing buttons. SGP.33-3's test cases verify that the eIM correctly orchestrates these operations across four different interfaces (ESep, ES9+', ES11', ESipa) and through multiple communication patterns. If the eIM gets any of these wrong, IoT devices in the field could be left with the wrong profile enabled, missed notifications, or an unmanageable eUICC.

> **Key takeaways:**
> - Profile State Management Operations (PSMO) test cases cover five eUICC Package functions: Enable, Disable, Delete, ListProfileInfo, and GetRat: all sent via the ESep logical interface
> - eIM Configuration test cases cover four functions: AddEim, UpdateEim (including anti-replay counter updates), DeleteEim, and ListEim: managing the eIM-eUICC association itself
> - Notification handling is tested across ES9+' (eIM-to-SM-DP+) with 9 nominal test sequences covering PIR, Install, Enable, Disable, and Delete notifications with various SM-DP+ address configurations
> - The ESipa interface (eIM-to-IPA) defines 11 functions for profile download orchestration, eIM Package transfer, and notification relay: though test sequences remain FFS as of v1.2
> - The only fully-defined behaviour test case in v1.2 is Profile Enable via eIM Package Retrieval mode, with four nominal sequences and error cases for wrong EID and eIM request errors
> - Most interface test cases reference SGP.23 and substitute the eIM for the LPAd role, reusing well-proven consumer eSIM test methodology

SGP.33-3 organises its test cases into two major sections: **Interface Compliance Testing** (Section 4) and **Procedure / Behaviour Testing** (Section 5). The interface tests verify correct message formats, protocol sequences, and error handling. The behaviour tests verify end-to-end procedures.

---

## ESep: Profile State Management Operations (PSMO)

The ESep interface (eIM-to-eUICC) carries eUICC Packages containing PSMO commands. Five PSMO functions are tested:

### Enable (4.2.1)
Requests the eUICC to enable a specific Operational Profile. Tests verify correct eUICC Package construction with Enable commands, conforming to SGP.22 sections 2.11.1.1, 2.11.1.1.3, 2.11.2.1, 3.3.1, and SGP.32 section 5.13.1. **Test sequences FFS in v1.2.**

### Disable (4.2.2)
Requests the eUICC to disable a currently Enabled Profile. Conformance references: SGP.22 sections 2.11.1.1, 2.11.1.1.3, 2.11.2.1, 3.3.1, and SGP.32 section 5.13.2. **Test sequences FFS in v1.2.**

### Delete (4.2.3)
Requests the eUICC to delete an installed Profile. Conformance references: SGP.22 sections 2.11.1.1, 2.11.1.1.3, 2.11.2.1, 3.3.1, and SGP.32 section 5.13.3. **Test sequences FFS in v1.2.**

### ListProfileInfo (4.2.4)
Allows the eIM to retrieve the list of Profile information for installed Profiles, including their current state (Enabled/Disabled) and associated Profile Metadata. This is the eIM's equivalent of the LPA's GetProfilesInfo. Conformance references: SGP.22 sections 2.11.1.1, 2.11.1.1.3, 2.11.2.1, 3.3.1, and SGP.32 section 5.13.4. **Test sequences FFS in v1.2.**

### GetRat (4.2.5)
Allows the eIM to retrieve the Rules Authorisation Table (RAT) from the eUICC: essential for knowing which profile management operations are permitted. Conformance references: SGP.22 sections 2.11.1.1, 2.11.1.1.3, 2.11.2.1, 3.3.1, and SGP.32 section 5.13.5. One test sequence is defined: Test Sequence #01 Nominal Case.

---

## ESep: eIM Configuration Operations (eCO)

Four eIM Configuration functions manage the eIM-eUICC association:

### AddEim (4.2.6)
Adds an Associated eIM to the eUICC by providing its eIM Configuration Data including the eimID. This is the eIM equivalent of the initial provisioning step where a remote manager registers itself with an IoT device's eUICC. **Test sequences FFS.**

### UpdateEim (4.2.7)
Updates eIM Configuration Data: specifically the public key or Certificate and the related **anti-replay counter value** of an Associated eIM with a given eimID, while keeping the same eimID. This function is critical for key rotation and security maintenance: when an eIM updates its credentials, it must increment the anti-replay counter to prevent replay attacks. **Test sequences FFS.**

### DeleteEim (4.2.8)
Deletes an Associated eIM identified by its eimID from the eUICC. If the successfully deleted Associated eIM was the last available Associated eIM, the eUICC SHALL allow ES10b.AddInitialEim again: enabling a fresh association to be established. **Test sequences FFS.**

### ListEim (4.2.9)
Requests the eUICC to provide a list of all currently configured Associated eIMs. This is an audit function allowing the eIM (or a new eIM) to discover what remote managers are currently associated with a given device. **Test sequences FFS** (one error case sequence defined but not detailed).

---

## ES9+': eIM-to-SM-DP+ Testing

The ES9+' interface is the eIM's channel to the SM-DP+ for profile delivery. All test cases reuse SGP.23 LPAd test sequences with the eIM playing the LPAd role:

### InitiateAuthentication (4.2.10)
- **Nominal**: Initiate Authentication (1 sequence, from SGP.23 §4.4.21.2.1)
- **Error Cases** (9 sequences): Invalid SM-DP+ Address, Unsupported Security Configuration, Unsupported SVN, Unavailable SM-DP+ Certificate, Invalid SM-DP+ Certificate, Invalid SM-DP+ Signature, Invalid SM-DP+ Address sent by SM-DP+, Unsupported CI Key ID, Invalid SM-DP+ OID

### GetBoundProfilePackage (4.2.11)
- **Nominal** (4 sequences): Get BPP using S-ENC/S-MAC (with/without Confirmation Code), Get BPP using PPK-ENC/PPK-MAC (with/without Confirmation Code)
- **Retry** (1 sequence): Get BPP Retry after incorrect Confirmation Code
- **Error Cases** (7 sequences): Wrong eUICC Signature, BPP Not Available, Unknown TransactionID, Missing Confirmation Code, Download Order Expired, Wrong Confirmation Code, Max Confirmation Code retries exceeded

### AuthenticateClient (4.2.12)
- **Nominal** (3 sequences): Authenticate without Confirmation Code, with Confirmation Code, with Confirmation Code Retry
- **Error Cases** (18 sequences): Invalid/Expired EUM Certificate, Invalid/Expired eUICC Certificate, Invalid eUICC Signature or serverChallenge, Insufficient Memory, Unknown CI Root Key, Profile not Allowed (Not in 'released' State), Unknown TransactionID, Refused MatchingID, Refused EID, No Eligible Profile, Expired Download Order, Max Retries Exceeded, Invalid SM-DP+(pb) certificate, Different OID for SM-DP+ Certificates, Invalid SM-DP+ signature (smdpSignature2), Invalid TransactionID sent by SM-DP+

### HandleNotification (4.2.13)
- **Nominal** (9 sequences): Covers all notification combinations:
  - Successful PIR and Install Notifications to Same SM-DP+ Address
  - Successful PIR and Enable Notifications to Same SM-DP+ Address
  - Disable and Delete Notifications to Same SM-DP+ Address
  - Enable and Disable Notifications with Different SM-DP+ Addresses
  - Different SM-DP+ Addresses in PIR and Install Notifications
  - Profile Download with PIR Failed
  - Successful PIR and Install Notifications after Connectivity Interruption (FFS)
  - No Acknowledge for Successful PIR results in No Further Notifications
  - Disable and Delete Notifications using Delete Operation

### CancelSession (4.2.14)
- **Nominal** (3 sequences): PPR1 not allowed (Operational Profile already present), Load BPP Error, Load BPP Error due to unknown TAG
- **EndUserPostponed** (VOID), **Error** (VOID), **PPRs** (VOID)

### HTTPS (4.2.15)
- **Nominal** (2 sequences): HTTPS Session Establishment, non-reuse of session keys
- **Error Cases** (2 defined + VOID): Invalid (SM-DP+) TLS Certificate signature, Expired TLS Certificate, Invalid TLS Certificate based on Invalid CI (Invalid Curve)

---

## ES11': eIM-to-SM-DS Testing

### InitiateAuthentication (4.2.16)
- **Nominal**: Initiate Authentication (1 sequence)
- **Error Cases** (8 sequences): Invalid SM-DS Address, Unsupported Security Configuration, Unsupported SVN, Unavailable SM-DS Certificate, Invalid SM-DS Certificate, Invalid SM-DS Signature, Invalid SM-DS Address sent by SM-DS, Unsupported CI Key ID

### AuthenticateClient (4.2.17)
- **Nominal** (2 sequences): Authenticate with empty MatchingID, Authenticate with MatchingID set to EventID
- **Error Cases** (7 sequences): Invalid/Expired EUM Certificate, Invalid/Expired eUICC Certificate, Invalid eUICC signature or serverChallenge, Unknown TransactionID, Unknown Event Record

### HTTPS (4.2.18)
- **Nominal** (2 sequences): HTTPS Session Establishment, non-reuse of session keys
- **Error Cases** (2 defined + VOID): Invalid (SM-DS) TLS Certificate signature, Expired TLS Certificate, Invalid TLS Certificate based on Invalid CI (Invalid Curve)

---

## ESipa: eIM-to-IPA Testing (FFS)

All 11 ESipa interface functions have test sequences marked FFS in v1.2, though the conformance requirements are documented:

- **InitiateAuthentication** (4.2.19, 4.2.22): Requests SM-DP+/SM-DS authentication via the eIM. Additional error codes: `smdpAddressMismatch` and `smdpOidMismatch`
- **GetBoundProfilePackage** (4.2.20, 4.2.23): Requests delivery and binding of a Profile Package
- **AuthenticateClient** (4.2.21, 4.2.24): Requests authentication of the eUICC by SM-DP+/SM-DS
- **TransferEimPackage** (4.2.25): eIM transfers single eIM Package to IPA
- **GetEIMPackage** (4.2.26): IPA retrieves an eIM Package
- **ProvideEimPackageResult** (4.2.27): IPA delivers eIM Package Result optionally including Notifications
- **HandleNotification** (4.2.28): IPA notifies eIM and/or SM-DP+ about profile state changes
- **CancelSession** (4.2.29): eIM requests cancellation of ongoing RSP session

---

## Behaviour Testing: Profile Enable via eIM Package Retrieval

The only fully-defined behaviour test case in v1.2 is **TC_eIM_ProfileEnable_TLS_eIM_Pkg_Retrieval** (Section 5.2.1). It tests the end-to-end flow where:

1. The IPA establishes a TLS connection to the eIM (PROC_TLS_INITIALIZATION_SERVER_AUTH_ESIPA)
2. The IPA sends a **GetEimPackage** request to the eIM
3. The eIM responds with the pending **eUICC Package Request** (containing the Enable PSMO)
4. The IPA delivers the result via **ProvideEimPackageResult** (or HandleNotification)
5. The eIM forwards notifications to the SM-DP+ via ES9+' HandleNotification

Four nominal sequences are defined:
- **Sequence #01**: Enable with ProvideEimPackageResult: no enabled profile
- **Sequence #02**: Enable with HandleNotification: no enabled profile
- **Sequence #03**: Enable with implicit disabling of formerly enabled profile, via ProvideEimPackageResult
- **Sequence #04**: Enable with implicit disabling of formerly enabled profile, via HandleNotification

Error case sequences cover:
- **Wrong EID**: IPA provides an eimPackageResult with wrong EID → eIM responds with `eidNotFound`
- **eIM Request Error cases**: Additional undefined error conditions

Each sequence includes conditional branching on `O_S_TRID` (whether a TransactionId is sent with eUICC Package Requests) : demonstrating how optional features drive test behaviour.

---

## 📋 Summary

- ESep interface tests cover 5 PSMO functions (Enable, Disable, Delete, ListProfileInfo, GetRat) and 4 eIM Configuration functions (AddEim, UpdateEim, DeleteEim, ListEim) : most test sequences remain FFS
- ES9+' testing includes 6 interface functions with extensive nominal, retry, and error case coverage adapted from SGP.23 LPAd tests
- ES11' testing covers 3 interface functions (InitiateAuthentication, AuthenticateClient, HTTPS) with 17 test sequences total
- ESipa defines 11 interface functions but all test sequences are FFS: the eIM-to-IPA interface testing methodology is still maturing
- The only fully-defined behaviour test is Profile Enable via eIM Package Retrieval, with 4 nominal sequences and error cases, conditionally applicable based on optional features O_S_PKG_RETRIEVAL and O_S_ESIPA_HTTPS
- Most ES9+' and ES11' test sequences reference SGP.23 and substitute the eIM for LPAd, providing a foundation of proven test methodology

---

<div align="center" markdown="1">

← Previous: [eIM Test Architecture: Simulated eIM and Reference IPA]({{ site.baseurl }}/docs/articles/sgp33-3/43-sgp33-eim-architecture) · [🏠 Home]({{ site.baseurl }}/)

Next: [eIM Security Testing: DTLS, Certificates, and Signed Packages]({{ site.baseurl }}/docs/articles/sgp33-3/45-sgp33-eim-security) →

</div>

---

*Based on GSMA SGP.33-3 v1.2 (27 January 2025) : eUICC IoT Manager Test Specification, Sections 4–5*


---

← Previous: [eIM Test Architecture: Simulated eIM and Reference IPA](43-sgp33-eim-architecture) | [Section Index](index) | Next: [eIM Security Testing: DTLS, Certificates, and Signed Packages](45-sgp33-eim-security) →
