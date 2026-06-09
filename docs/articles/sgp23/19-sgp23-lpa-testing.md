---
title: "Testing the LPA: LDS, LPD, and LUI Conformance"
description: "Walks through SGP.23's LPA conformance testing — ES10a discovery, ES10b profile download pipeline (12 functions), ES10c local management (8 functions), and LPAd interface verification across two testing chapters."
date: 2026-06-05
---

# Testing the LPA: LDS, LPD, and LUI Conformance

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.23 Test Specifications]({{ site.baseurl }}/docs/articles/sgp23/) > Testing the LPA: LDS, LPD, and LUI Conformance**

> **💡 Why this matters:** The LPA is the bridge between the user and the eUICC: and between the device and the SM-DP+/SM-DS. Get the LPA wrong, and profile downloads fail, discovery breaks, or users can't switch carriers. SGP.23 dedicates two complete testing chapters (eUICC ES10x and LPAd interfaces) to ensuring this bridge works correctly in every scenario.

> **Key takeaways:**
> - ES10a (LDS → eUICC) is tested for two functions: discovery address retrieval and default SM-DP+ configuration
> - ES10b (LPD → eUICC) covers 12 functions: the full profile download pipeline from challenge generation to CRL loading
> - ES10c (LUI → eUICC) covers 8 functions for local profile management: list, enable, disable, delete, reset, EID, nickname
> - LPAd interface testing (Section 4.4) verifies that the device-side LPA correctly relays commands and handles responses
> - ES11 (LDS → SM-DS) event retrieval is tested from both the eUICC side (Section 4.2) and the LPAd side (Section 4.4)
> - Device-level procedure testing (Section 5.4) verifies full workflows: Add Profile, Enable/Disable/Delete, Set Nickname, eUICC Memory Reset

The LPA (Local Profile Assistant) is the most interface-heavy component in the eSIM ecosystem. It has three sub-components: LDS (discovery), LPD (download), and LUI (user interface) : and touches four interfaces: ES10a, ES10b, ES10c (to the eUICC) and ES9+, ES11 (to remote servers). SGP.23 tests both the eUICC's implementation of the LPA services and the LPAd/Device's implementation as a client.

---

## ES10a: Profile Discovery Functions

The LDS sub-component uses ES10a to query the eUICC about discovery configuration. Two functions are tested:

### GetEuiccConfiguredAddresses

Returns the SM-DP+ address (if set as default) and/or the Root SM-DS address configured on the eUICC. Test cases verify:
- Correct DER encoding of the `GetEuiccConfiguredAddressesResponse`
- Proper handling when no addresses are configured
- That the SM-DS address format matches the specification

### SetDefaultDPAddress

Configures the eUICC's default SM-DP+ address: the fallback server used when no explicit SM-DP+ address is provided in an Activation Code. Test cases verify:
- Successful write and subsequent read-back via `GetEuiccConfiguredAddresses`
- Handling of invalid address formats
- Persistence across power cycles

---

## ES10b: Profile Download Pipeline

The LPD sub-component is the workhorse. Twelve ES10b functions are tested:

### GetEUICCChallenge / GetEUICCInfo

The two functions that kick off mutual authentication. `GetEUICCInfo` returns the eUICC's capabilities, supported CI public key identifiers (for signing and verification), and SAS accreditation number. `GetEUICCChallenge` generates a fresh random challenge. Test cases verify:
- Correct `EUICCInfo1` and `EUICCInfo2` structure encoding
- That `euiccCiPKIdListForSigning` and `euiccCiPKIdListForVerification` are populated correctly
- Challenge uniqueness across successive calls

### AuthenticateServer

The eUICC verifies the SM-DP+'s identity. The test tool sends a simulated `AuthenticateServerRequest` containing the SM-DP+'s certificate chain and signature. The eUICC must:
- Validate the certificate chain (`CERT.DPauth.ECDSA` → CI → root)
- Verify the SM-DP+'s signature over the transaction data
- Return the authenticated server response with its own signature

Test cases cover valid authentication, wrong certificates, expired certificates, mismatched matching IDs, and unsupported CI public key identifiers.

### PrepareDownload

The eUICC prepares to receive a profile. It verifies the SM-DP+'s profile binding certificate (`CERT.DPpb.ECDSA`) and generates a one-time key pair (`otPK.eUICC.ECKA` / `otSK.eUICC.ECKA`) for the encrypted download channel. Test cases verify:
- Hash of the profile binding certificate in the response
- That the one-time public key is correctly generated
- Handling of confirmation code requirements (when the profile requires user confirmation)

### LoadBoundProfilePackage

The critical function that delivers encrypted profile data to the eUICC. The eUICC receives the `BoundProfilePackage` (encrypted specifically for this eUICC) and processes it internally: the LPA never sees the decrypted content. Test cases verify:
- Successful profile installation
- Detection of corrupted or tampered profile packages
- Sequential delivery (the profile is delivered in chunks : `LoadBoundProfilePackage` is called repeatedly)
- Proper handling of the `StoreMetadata` step embedded within the bound package

### Notification Functions

Three functions manage the eUICC's notification queue:

- **ListNotification** : Returns pending notifications (install, enable, disable, delete) as a `NotificationMetadataList`
- **RetrieveNotificationsList** : Returns the full notification list with detailed `PendingNotification` structures
- **RemoveNotificationFromList** : Removes a specific notification by sequence number after it has been acknowledged

Test cases verify ordered delivery, sequence number management, and that notifications persist until explicitly removed.

### LoadCRL

Loads a Certificate Revocation List onto the eUICC. Test cases verify correct parsing of the CRL ASN.1 structure and that subsequent authentications reject certificates listed in the CRL.

### CancelSession / GetRAT

- **CancelSession** : Allows the LPA to abort an in-progress profile download or authentication session. Test cases verify clean session teardown.
- **GetRAT** : Returns the eUICC's Rules Authorisation Table: the policy that governs which profile operations the user can perform. Used by the LPA to enforce Profile Policy Rules (PPRs).

---

## ES10c: Local Profile Management

The LUI sub-component uses ES10c for all user-facing profile operations:

### GetProfilesInfo

Returns information about all installed profiles: ICCID, ISD-P AID, profile state (Enabled/Disabled), profile nickname, Service Provider Name, Profile Name, Profile Class, and PPRs. Test cases verify:
- Correct encoding of `ProfileInfoListResponse`
- Proper indication of enabled vs. disabled states
- That only one profile is reported as enabled at a time
- That PPRs are correctly reported for each profile

### EnableProfile / DisableProfile

Enable makes a profile the active subscription (deactivating the previously enabled one). Disable makes it dormant while keeping it installed. Test cases verify:
- `RefreshFlag` behaviour (whether the eUICC sends a REFRESH proactive command in "UICC Reset" mode)
- Error handling when trying to enable an already-enabled profile
- Error handling when trying to disable an already-disabled profile
- PPR enforcement: the eUICC refuses operations that violate the enabled profile's policy rules

### DeleteProfile

Permanently removes an ISD-P and all its contents. Test cases verify:
- Successful deletion and ISD-P removal
- That deleted profiles no longer appear in `GetProfilesInfo`
- Error handling for non-existent ICCIDs
- PPR enforcement (e.g., PPR2 may require the profile to be disabled first)

### eUICCMemoryReset / GetEID / SetNickname

- **eUICCMemoryReset** : Factory-resets the entire eUICC, deleting all profiles and ISD-Ps. Test cases verify complete erasure.
- **GetEID** : Returns the eUICC's unique 32-digit EID.
- **SetNickname** : Assigns a user-friendly label to a profile. Test cases verify persistence and proper UTF-8 handling.

---

## LPAd Interface Testing (Section 4.4)

When testing the LPAd (device-side LPA), the perspective flips: the test tool simulates the eUICC and remote servers, and the Device Under Test exercises the ES10x, ES9+, and ES11 interfaces:

- **ES10a** : The device must correctly call `GetEuiccConfiguredAddresses` and `SetDefaultDPAddress` and handle the eUICC's responses
- **ES10b** : The device must orchestrate the full profile download pipeline in the correct sequence without race conditions or missing steps
- **ES10c** : The device's LUI must offer all required operations and pass user intent/confirmation correctly to the eUICC
- **ES9+** : The device must correctly call `InitiateAuthentication`, `GetBoundProfilePackage`, and `AuthenticateClient` on the simulated SM-DP+
- **ES11** : The device must poll the simulated SM-DS using `ES11.GetEvents` and handle event records

The S_EndUser simulator (person or software) drives all user interactions, following the vendor's documented confirmation mechanisms (`#IUT_LPAd_Confirmation`).

---

## Device-Level Procedure Testing (Section 5.4)

Beyond interface-level testing, Section 5.4 tests complete workflows:

- **Add Profile** : Full flow from Activation Code entry through download and installation
- **List Profiles** : Display of installed profiles with correct states
- **Set Nickname** : End-to-end nickname assignment and display
- **Delete / Enable / Disable Profile** : Complete procedures including any required confirmations
- **Retrieve EID** : Displaying the EID to the user
- **eUICC Memory Reset** : Full factory reset procedure
- **eUICC Test Memory Reset** : Device Test Mode operation
- **Set/Edit Default SM-DP+ Address** : Configuring the fallback server
- **Device Power-On Profile Discovery** : Automatic SM-DS polling at boot

---

## 📋 Summary

- ES10a (2 functions), ES10b (12 functions), and ES10c (8 functions) are tested from both the eUICC perspective (Section 4.2) and the LPAd perspective (Section 4.4)
- The profile download pipeline (GetEUICCChallenge → AuthenticateServer → PrepareDownload → LoadBoundProfilePackage) is the most heavily tested sequence
- Notification management (List, Retrieve, Remove) ensures pending operations are tracked and acknowledged
- Device-level procedure testing validates complete user workflows, including combined operations (Add+Enable, Disable+Delete)
- PPR enforcement is tested at both the interface level (eUICC rejects invalid operations) and the procedure level (LUI respects policy rules)

---

<div align="center" markdown="1">

← Previous: [The GSMA eSIM Test Infrastructure]({{ site.baseurl }}/docs/articles/sgp23/18-sgp23-test-infrastructure) · [🏠 Home]({{ site.baseurl }}/)

Next: [Testing the SM-DP+ and SM-DS]({{ site.baseurl }}/docs/articles/sgp23/20-sgp23-server-testing) →

</div>

---

*Based on GSMA SGP.23 v1.16 (29 April 2025) : RSP Test Specification, Sections 4.2 (eUICC Interfaces), 4.4 (LPAd Interfaces), 5.2 (eUICC Behaviour), 5.4 (Device Procedures)*


---

← Previous: [The GSMA eSIM Test Infrastructure](18-sgp23-test-infrastructure) | [Section Index](index) | Next: [Testing the SM-DP+ and SM-DS](20-sgp23-server-testing) →
