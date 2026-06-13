---
title: "Key eUICC Test Cases: ISD-R, ECASD, and Profile Lifecycle"
description: "Examines key SGP.23-1 test cases : ISD-R selection across nine sequences, ES8+ secure channel testing, ES10b profile download pipeline, ES10c local management, and MEP multi-profile handling."
date: 2026-06-05
---

# Key eUICC Test Cases: ISD-R, ECASD, and Profile Lifecycle

**[eUICC.tech]({{ site.baseurl }}/) > [SGP.23-1 eUICC Testing]({{ site.baseurl }}/docs/articles/sgp23-1/) > Key eUICC Test Cases: ISD-R, ECASD, and Profile Lifecycle**

> **Why this matters:** Before any profile can be downloaded, before any carrier switch can happen, the eUICC must correctly handle the fundamental lifecycle of its secure domains and profiles. SGP.23-1's 27 interface test groups and 8 behaviour test groups verify every state transition: from the first ATR byte through ISD-R selection, secure channel establishment, profile installation, enablement, and deletion. These are the tests that catch the bugs which would otherwise surface as "inexplicable" field failures.

> **Key takeaways:**
> - ISD-R selection is tested across 9 sequences covering nominal cases, enabled/disabled profiles, LPAe support, and MEP configurations (A1, A2, B)
> - ES8+ secure channel testing covers `InitialiseSecureChannel` (5 error sequences), `ConfigureISDP`, `StoreMetadata` (11+ sequences), and `LoadProfileElements` (12 sequences)
> - ES10b profile download pipeline tests span `PrepareDownload` (curve-specific + error), `LoadBoundProfilePackage`, `GetEUICCChallenge`, and `AuthenticateServer`
> - ES10c local profile management tests `GetProfilesInfo`, `EnableProfile`, `DisableProfile`, `DeleteProfile`, and `eUICCMemoryReset` : the most heavily tested interface with hundreds of pages
> - Behaviour testing covers retry mechanisms (Confirmation Code, one-time key reuse), forbidden PPRs, file structure validation, and notification handling
> - MEP (Multiple Enabled Profiles) adds extensive test sequences for multi-profile management across LSI multiplexing

* TOC
{:toc}

SGP.23-1's test cases are organised into two major chapters: Section 4 (Interface Compliance Testing, pages 37–595) and Section 5 (Procedure - Behaviour Testing, pages 595–611). Together they cover 27 interface-level test groups and 8 behaviour-level test groups, each containing multiple test sequences.

---

## ISD-R Selection and ATR Testing

The very first thing tested is whether the eUICC powers up correctly and allows the LPA to select its ISD-R:

**TC_eUICC_ATR_And_ISDR_Selection** covers 9 test sequences:

| # | Scenario | Key Verification |
|---|----------|-----------------|
| 1 | Nominal: ATR + Select ISD-R | ATR contains tBi with b2=1; FCP Template present; ISD-R selection returns proprietary data with `#R_ISDR_SELECTION` |
| 2 | With Enabled Profile | Same ISD-R selection but response includes `#R_ISDR_SELECTION_EN_PROF` : different proprietary data when a profile is enabled |
| 3 | LPAe Supported | ISD-R selection response includes `#R_ISDR_SELECTION_LPAE` : the eUICC advertises its LPAe capability |
| 4 | MEP-A1 | LSI Support present in ATR; `MEP_MODE = '01'`; configures 2 LSIs with IDs "010203" |
| 5 | MEP-A2 | Similar to A1 but with `MEP_MODE = '10'` |
| 6 | MEP-B | `MEP_MODE = '11'`; configures for MEP-B with possible auto-deselection behaviour |
| 7-9 | Additional MEP variants | Various LSI multiplexing and auto-deselection configurations |

The test verifies that the eUICC correctly advertises its capabilities through the ATR historical bytes and ISD-R selection response: the first trust boundary between the device and the eUICC.

---

## ES8+ Secure Channel: Profile Delivery

The ES8+ interface is the secure tunnel through which profiles arrive from the SM-DP+. Four test case groups verify it:

### InitialiseSecureChannel (4.2.3)

Five error sequences ensure the eUICC rejects malformed channel initiation:
- Invalid Remote Operation ID
- Invalid SM-DP+ Signature (the euiccSignPIR must be verified with `#PK_EUICC_SIG`)
- Invalid Transaction Identifier
- Invalid CRT (Control Reference Template) Values
- Rejecting a second `InitialiseSecureChannel` while a secure session is already ongoing

### ConfigureISDP (4.2.4)

Mandatory test case verifying that the eUICC correctly processes ISD-P configuration commands: allocating memory, setting up the security domain, and preparing for profile content.

### StoreMetadata (4.2.5)

The most sequence-heavy ES8+ test group with 11+ test sequences covering:
- Nominal metadata storage for operational profiles
- Service-specific data handling
- Enterprise profile metadata (conditional on `O_E_ENTERPRISE`)
- V3 notification configuration
- RPM (Remote Profile Management) metadata
- HRI Server Address storage (conditional on `O_E_HRI_ADDRESS_IN_PM`)
- LPR Configuration (Local Profile Replacement)
- Device Change metadata

### LoadProfileElements (4.2.7)

Delivers the actual profile content. 12 test sequences cover:
- Nominal profile loading across NIST P-256, BrainpoolP256r1, and FRP256V1 curves
- Error cases: invalid element IDs, wrong sequence ordering, truncated data
- The eUICC must return the correct Profile Installation Result (PIR) with a verifiable `euiccSignPIR`

---

## ES10b: The Profile Download Pipeline

The ES10b interface is where the LPA orchestrates profile downloads. Key test groups:

### PrepareDownload (4.2.10)

Four test case groups: three curve-specific (NIST, BRP, FRP) and one for error handling. Each verifies:
- Correct generation of the one-time key pair (`otPK.eUICC.ECKA` / `otSK.eUICC.ECKA`)
- Proper hash of the SM-DP+ profile binding certificate
- Confirmation Code handling when `#PREP_DOWNLOAD_WITH_CC` is used
- That error cases (wrong matching ID, unsupported CI public key identifier) are correctly rejected

### GetEUICCChallenge / GetEUICCInfo (4.2.12–13)

- `GetEUICCChallenge` verifies fresh challenge generation on every call
- `GetEUICCInfo1` has 6 test sequences covering different `EUICCInfo1` response structures
- `GetEUICCInfo2` has 5 variants: V2.1 (N/A for SGP.23-1), V2.2.x (mandatory), V3.x (mandatory), and Integrated eUICC variant
- The `sasAcreditationNumber` field is verified in the `EUICCInfo2` response

### LoadBoundProfilePackage (4.2.11)

The critical delivery function. Curve-specific tests (NIST, BRP, FRP) plus error cases verify:
- Successful profile decryption and installation
- Sequential chunk delivery handling
- Detection of tampered or malformed Bound Profile Packages

### Notification Management (4.2.14–16)

Three test groups covering the notification lifecycle:
- **ListNotification** : Returns pending notifications; test sequence #5 covers RPM-specific notifications
- **RetrieveNotificationsList** : Full notification details with sequence number tracking
- **RemoveNotificationFromList** : Removal by sequence number; verifications that the correct notification is removed

### RPM Package Loading (4.2.28)

`LoadRPMPackage` (conditional on `O_E_RPM`) tests the Remote Profile Management capability: updating profile metadata, policy rules, or content on an already-installed profile without full re-download.

---

## ES10c: Local Profile Management

The ES10c interface is where the user-facing profile operations happen. This is SGP.23-1's most heavily tested interface:

### GetProfilesInfo (4.2.20)

Returns information about all installed profiles. Test sequences verify:
- Correct `ProfileInfoListResponse` encoding with `profileInfoListOk`
- Enabled vs Disabled state indication
- Nickname, Service Provider Name, Profile Name, and Profile Class fields
- PPR (Profile Policy Rule) reporting
- Estimated profile size when `O_E_PROFILE_SIZE_IN_PROFILE_INFO` is supported

### EnableProfile (4.2.21)

The most complex test case group: spanning ~117 pages (from page 238 to 355). It covers:
- **Nominal enablement** with RefreshFlag behaviour
- **MEP-A1/A2/B** variants: Multiple Enabled Profiles add significant complexity
- **Error cases**: enabling an already-enabled profile, "catBusy" when a proactive session is ongoing, PPR violations
- **Refresh flag variants**: with and without refresh flag set, different MEP modes

### DisableProfile (4.2.22)

Spans ~106 pages, covering:
- Nominal disablement, MEP variants
- Error cases: disabling the only enabled profile when PPRs forbid it, disabling an already-disabled profile
- "catBusy" error handling when proactive sessions are in progress
- Auto-deselection behaviour for MEP-B

### DeleteProfile (4.2.23)

Covers permanent ISD-P removal:
- Successful deletion and verification the profile no longer appears in `GetProfilesInfo`
- PPR enforcement (PPR2 may require disablement before deletion)
- Memory reclamation after deletion
- Error handling for non-existent ICCIDs

### eUICCMemoryReset (4.2.24)

Factory-resets the entire eUICC: all profiles and ISD-Ps deleted. Tests verify:
- Complete erasure of all profile data
- "catBusy" handling when proactive sessions are active
- That `GetProfilesInfo` returns empty after reset

---

## Behaviour Testing: End-to-End eUICC Behaviour

Section 5 verifies functional behaviour beyond individual interface calls:

### Retry Mechanism (5.2.1)

Tests the eUICC's ability to handle failed downloads gracefully:
- **Confirmation Code retry** : When the user enters a wrong confirmation code, the eUICC reuses the previous one-time key pair for the retry attempt (conditional on `O_E_REUSE_OTPK`)
- **Download retry** : Full retry of a failed `LoadBoundProfilePackage` sequence

### Forbidden PPRs (5.2.2)

Verifies that the eUICC refuses operations that violate Profile Policy Rules: the enforcement mechanism that prevents users (or malware) from performing disallowed profile operations.

### eUICC File Structure (5.2.4)

Validates the eUICC's internal file system: that EF_UST, EF_DIR, EF_ICCID, and EF_ARR are correctly structured and accessible through standard UICC file selection commands.

### Delete/Enable/Disable Process Behaviour (5.2.5–7)

Beyond interface compliance, these behaviour tests verify the full process lifecycle:
- Notification generation for each operation
- Correct state transitions (Enabled ↔ Disabled ↔ Deleted)
- Interaction with the REFRESH proactive command
- MEP-specific process flows

---

## Summary

- ISD-R selection (9 sequences) verifies the very first handshake: ATR, logical channel management, and capability advertisement
- ES8+ testing (4 groups) validates the secure channel for profile delivery: initialisation, ISD-P configuration, metadata storage, and profile element loading
- ES10b (12 function groups) covers the complete profile download pipeline from challenge generation through bound package loading to notification management
- ES10c (8 function groups) is the most heavily tested interface, with EnableProfile alone spanning ~117 pages of test sequences
- System behaviour testing (Section 5) goes beyond interface compliance to verify retry mechanisms, PPR enforcement, file structure integrity, and state transitions
- MEP (Multiple Enabled Profiles) adds extensive test variants across ISD-R selection, EnableProfile, DisableProfile, and DeleteProfile

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp23-1/33-sgp23-1-architecture">eUICC Test Architecture: Readers, Scripts, and GSMA Tools</a> · <a href="{{ site.baseurl }}/"> Home</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp23-1/35-sgp23-1-security">eUICC Security Testing: Certificates, Keys, and Channels</a> →

</div>

---

*Based on GSMA SGP.23-1 v3.1.3 (27 January 2025) : RSP Test Specification for the eUICC, Sections 4.2, 5.2*


---

← Previous: [eUICC Test Architecture: Readers, Scripts, and GSMA Tools](33-sgp23-1-architecture) | [Section Index](index) | Next: [eUICC Security Testing: Certificates, Keys, and Channels](35-sgp23-1-security) →
