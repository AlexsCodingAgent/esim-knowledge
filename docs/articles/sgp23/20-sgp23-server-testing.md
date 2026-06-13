---
title: "Testing the SM-DP+ and SM-DS"
3|description: "Explores SGP.23's server-side testing : the SM-DP+ across ES2+, ES8+, and ES9+ interfaces, the SM-DS across ES12, ES11, and ES15, with independent TLS interface verification."
date: 2026-06-05
---

# Testing the SM-DP+ and SM-DS

**[eUICC.tech]({{ site.baseurl }}/) > [SGP.23 Test Specifications]({{ site.baseurl }}/docs/articles/sgp23/) > Testing the SM-DP+ and SM-DS**

> **Why this matters:** The SM-DP+ is the profile factory and the SM-DS is the notification backbone. Together they form the server-side of every eSIM deployment. SGP.23 tests these components across six interfaces (ES2+, ES8+, ES9+, ES12, ES11, TLS) with strict requirements for cryptographic correctness, error handling, and inter-component coordination.

> **Key takeaways:**
> - SM-DP+ is tested across three interfaces: ES2+ (Operator-facing, 6 functions), ES8+ (eUICC-facing, 5 functions), and ES9+ (LPA-facing, 5 functions)
> - ES2+ testing uses a simulated MNO to verify profile ordering, confirmation, cancellation, release, and progress tracking
> - ES8+ testing verifies the end-to-end secure channel: InitialiseSecureChannel, ConfigureISDP, StoreMetadata, LoadProfileElements, ReplaceSessionKeys
> - ES9+ testing verifies mutual authentication, bound profile package delivery, client authentication, and notification handling
> - SM-DS is tested across ES12 (event registration/deletion from SM-DP+), ES11 (event retrieval by LPA), and ES15 (inter-SM-DS cascading)
> - TLS interface testing (Section 4.6) independently verifies mutual authentication, server authentication, and cipher suite compliance

Where SGP.22 defines the server interfaces, SGP.23 defines the test cases that prove a server implementation is correct. This article covers the SM-DP+ and SM-DS testing defined in Sections 4.3, 4.5, and 4.6 of the specification.

---

## SM-DP+ Testing: Three Interfaces, Three Test Environments

The SM-DP+ is tested in up to three configurations:

| Environment | Interfaces Active | Simulated Counterparts |
|-------------|-------------------|----------------------|
| TE_P1 | ES12 only | S_SM-DS |
| TE_P2 | ES9+ only | S_LPAd |
| TE_P3 | ES2+ + ES9+ + ES12 | S_MNO + S_LPAd + S_SM-DS |

Test data is provided in JSON format. The SM-DP+ IUT is tested as both a TLS server (for ES9+ and ES2+ connections) and a TLS client (for ES12 connections to the SM-DS).

---

## ES2+ : Operator to SM-DP+ Interface

ES2+ is how an operator orders profiles. Six functions are tested:

### DownloadOrder

The operator reserves an ICCID from the SM-DP+'s pool before confirming the order. Test cases verify:
- Successful ICCID reservation
- Rejection when the requested profile type is unavailable
- Proper handling of the response structure

### ConfirmOrder

The operator provides the target EID, triggering the SM-DP+ to prepare a profile bound to that specific eUICC. Test cases verify:
- Successful confirmation with valid EID
- Rejection with invalid or malformed EIDs
- That the SM-DP+ can handle ES2+ retry (identical `ConfirmOrder` called twice: optional feature `O_P_ES2+_RETRY`)
- Correct encoding of the `ConfirmOrderResponse`

### CancelOrder / ReleaseProfile

- **CancelOrder** : Aborts a pending order before profile delivery. Test cases verify that the ICCID returns to the available pool.
- **ReleaseProfile** : Releases a profile that has been delivered but is no longer needed. Test cases verify proper lifecycle management.

### HandleDownloadProgressInfo

The operator can query the status of a profile download in progress. Test cases verify that the SM-DP+ correctly reports download states.

### TLS, Mutual Authentication, Server Session Establishment

The ES2+ connection itself is tested: the SM-DP+ must present a valid TLS server certificate and optionally perform mutual TLS authentication with the operator.

---

## ES8+ : SM-DP+ to eUICC (End-to-End Secure Channel)

ES8+ is tunnelled through the LPA: the SM-DP+ sends commands that the LPA relays to the eUICC without seeing the payload. Five functions are tested:

### InitialiseSecureChannel

Establishes the end-to-end encrypted channel between the SM-DP+ and the eUICC's target ISD-P. The SM-DP+ sends SCP03t (Secure Channel Protocol 03: tunnelled) TLVs containing:
- Key agreement parameters for deriving session keys `<S-ENC>` and `<S-MAC>`
- The initialisation data for the secure channel

Test cases verify that the SM-DP+ generates correct SCP03t structures, uses the eUICC's one-time public key (`otPK.eUICC.ECKA`) from `PrepareDownload`, and derives session keys correctly.

### ConfigureISDP

Creates and configures the ISD-P container. The SM-DP+ specifies:
- The ISD-P's security domain parameters
- Key sets, privileges, and lifecycle state

Test cases verify correct ISD-P creation and that the SM-DP+ can configure the ISD-P to the expected state before profile loading begins.

### StoreMetadata

Writes the profile's metadata into the ISD-P: ICCID, Service Provider Name, Profile Name, Profile Class, Profile Policy Rules, notification addresses. Test cases verify:
- Correct encoding of the metadata ASN.1 structure
- That all mandatory fields are present
- Proper handling of optional metadata extensions

### LoadProfileElements

The profile package is streamed in chunks. This function is called repeatedly, each time delivering a portion of the bound profile package. Test cases verify:
- Correct chunking (the SM-DP+ must split the profile package into valid elements)
- That the eUICC's Profile Package Interpreter can decode each element
- Error recovery if a chunk fails

### ReplaceSessionKeys

Optionally replaces the session keys mid-download for enhanced security. When session keys are used (`O_P_SESSION_KEYS`), test cases verify that the SM-DP+ correctly transitions to new keys without breaking the secure channel.

---

## ES9+ : SM-DP+ to LPA Interface

ES9+ is the HTTPS interface between the SM-DP+ and the device's LPA (LPD component). Five functions are tested:

### InitiateAuthentication

The LPA sends the eUICC's challenge and device info, and the SM-DP+ responds with its own challenge, certificate chain, and transaction ID. Test cases verify:
- Correct response structure (`InitiateAuthenticationResponse`)
- Proper selection of the CI public key identifier for signing (based on the eUICC's `euiccCiPKIdListForSigning`)
- Certificate chain validation (`CERT.DPauth.ECDSA` must chain to the selected CI)
- Handling of optional fields (matching ID, device info, Event ID, IMEI)

### AuthenticateClient

The LPA forwards the eUICC's signed challenge, and the SM-DP+ verifies the eUICC is genuine. Test cases verify:
- Successful client authentication with valid eUICC signature
- Rejection of tampered or invalid client responses
- Proper profile metadata delivery in the response

### GetBoundProfilePackage

The LPA requests the encrypted profile package. The SM-DP+ delivers the `BoundProfilePackage`, encrypted specifically for the target eUICC. Test cases verify:
- Successful delivery of the bound package
- That the package is correctly encrypted (the test tool can decrypt it with known test keys to verify)
- Handling when the transaction ID is invalid or expired

### HandleNotification

The LPA sends profile operation notifications (install result, enable, disable, delete) to the SM-DP+. Test cases verify:
- Correct parsing of `HandleNotificationRequest`
- Proper acknowledgment
- Handling of duplicate notifications

### CancelSession / TLS

- **CancelSession** : The LPA can abort a transaction. Test cases verify proper cleanup.
- **TLS, Server Authentication, Session Establishment** : The SM-DP+ must present a valid TLS server certificate with the correct OID (e.g., `2.999.10` for SM-DP+) and support the required cipher suite (`TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`).

---

## SM-DS Testing: Discovery Server

The SM-DS is tested across three interfaces, with seven test environments depending on whether it is a Root SM-DS or an Alternative SM-DS:

### ES12: SM-DP+ to SM-DS (Event Registration)

The SM-DP+ registers an Event on the SM-DS when a profile is ready for a specific eUICC. Two functions:

- **RegisterEvent** : Creates an Event with the EID and the SM-DP+'s address. Test cases verify correct registration and duplicate handling.
- **DeleteEvent** : Removes an Event after the profile has been downloaded or expired. Test cases verify proper deletion.

TLS mutual authentication is required: the SM-DS must verify the SM-DP+'s client certificate.

### ES11: LPA to SM-DS (Event Retrieval)

The device's LDS polls the SM-DS for pending Events. Test cases verify:
- Correct response when Events are pending (returns Event Records with SM-DP+ addresses)
- Correct response when no Events are pending (empty list)
- Proper handling of the eUICC's EID in the request

### ES15: SM-DS to SM-DS (Cascading)

In cascaded SM-DS deployments, Alternative SM-DSs forward Events to a Root SM-DS. Test cases verify:
- Correct forwarding of Event Registrations from Alternative to Root
- Proper propagation of Event Deletions
- That the Root SM-DS correctly aggregates Events from multiple Alternative SM-DSs

---

## TLS Interface Testing (Section 4.6)

TLS is tested independently because both SM-DP+ and SM-DS act as TLS servers and TLS clients in different contexts:

- **TLS, Mutual Authentication, Client** : When the SM-DP+ or SM-DS acts as a TLS client (e.g., SM-DP+ connecting to SM-DS on ES12), it must present a valid client certificate and verify the server's certificate.
- **TLS, Mutual Authentication, Server** : When acting as a TLS server, the component must present a valid server certificate, optionally request a client certificate, and verify it.
- **TLS, Server Authentication** : Server-only authentication scenarios (e.g., ES9+ from LPA to SM-DP+) where the server authenticates to the client.

Test cases verify: supported cipher suites, certificate chain validation, OID matching (SM-DP+ OID: `2.999.10`, SM-DS OID: `2.999.15`), supported signature algorithms (ECDSA with SHA-256), and proper handling of TLS session IDs.

---

## Summary

- SM-DP+ testing spans ES2+ (6 functions, profile ordering), ES8+ (5 functions, eUICC secure channel), and ES9+ (5 functions, LPA-facing download orchestration)
- SM-DS testing spans ES12 (event registration/deletion), ES11 (event retrieval), and ES15 (cascading), with separate environments for Root SM-DS and Alternative SM-DS
- TLS is tested independently across mutual authentication, server authentication, and client authentication scenarios
- All server-side testing uses JSON input data and simulated counterparts (S_MNO, S_LPAd, S_SM-DS, etc.)
- Each test case references specific SGP.22 requirements by their identifiers (RQxx_xxx format), providing full traceability

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp23/19-sgp23-lpa-testing">Testing the LPA: LDS, LPD, and LUI Conformance</a> · <a href="{{ site.baseurl }}/"> Home</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp23/21-sgp23-certification">SGP.23 Certification: From Test Cases to DLOA</a> →

</div>

---

*Based on GSMA SGP.23 v1.16 (29 April 2025) : RSP Test Specification, Sections 4.3 (SM-DP+ Interfaces), 4.5 (SM-DS Interfaces), 4.6 (TLS Interfaces), 3.2.2 (SM-DP+ and SM-DS Test Environment)*


---

← Previous: [Testing the LPA: LDS, LPD, and LUI Conformance](19-sgp23-lpa-testing) | [Section Index](index) | Next: [SGP.23 Certification: From Test Cases to DLOA](21-sgp23-certification) →
