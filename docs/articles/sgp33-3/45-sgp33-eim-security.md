---
title: "eIM Security Testing: DTLS, Certificates, and Signed Packages"
date: 2026-06-05
---

# eIM Security Testing: DTLS, Certificates, and Signed Packages

**🏠 [eUICC.tech](/) > [SGP.33-3 eIM Testing](/docs/articles/sgp33-3/) > eIM Security Testing: DTLS, Certificates, and Signed Packages**

> **💡 Why this matters:** The eUICC IoT Manager (eIM) remotely controls profile state and configuration on IoT devices — often devices deployed in the field for years without physical access. A compromised eIM could enable rogue profiles, disable critical connectivity, or hijack device management. SGP.33-3's security test cases verify the cryptographic foundations that make remote IoT management trustworthy: TLS channel establishment, certificate chain validation, signed package integrity, anti-replay protection, and server authentication. These tests ensure that only authorised eIMs can issue commands, and that those commands cannot be replayed, modified, or forged in transit.

> **Key takeaways:**
> - All eIM-to-server communication uses TLS v1.2 in **Server Authentication mode** (the eIM authenticates the server, not vice versa), with mandatory cipher suites: TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 (preferred) or TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256
> - HTTPS test cases verify TLS certificate validation across ES9+' and ES11' — including invalid certificate signatures, expired certificates, unsupported CI curves, and invalid server signatures
> - The ESipa interface uses Server Authentication with **Variant O certificate** — the eIM acts as the TLS server and the IPA as client
> - eUICC Packages on ESep are signed by the eIM (`eimSignature`) and include an anti-replay **counterValue** that increments with each package — the eUICC verifies both
> - Certificate validation is based on SGP.26 test certificates (X.509 format, ECDSA on NIST P-256 or brainpoolP256r1), with CI root keys pre-loaded in the eUICC's ECASD
> - eIM Configuration updates (UpdateEim) specifically update the public key/certificate and anti-replay counter — making key rotation testable
> - Notifications are cryptographically signed by the eUICC (`euiccNotificationSignature`) and include the full certificate chain (eUICC Certificate + EUM Certificate) for verification

SGP.33-3 embeds security testing throughout its interface compliance and behaviour test cases. Unlike some specifications that isolate security in a dedicated section, SGP.33-3 weaves TLS, certificate, and signature verification into the normal flow of every interface test.

---

## TLS Channel Validation

### Server Authentication Mode

All eIM-to-server communications use TLS v1.2 in Server Authentication mode — the server presents a certificate, and the eIM (acting as client) verifies it. This is the same model used by the consumer LPA. The test specification references SGP.22 section 2.6.6 for HTTPS security requirements.

### Cipher Suite Requirements

The test tools enforce a specific cipher suite preference:

- **Preferred**: `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`
- **Fallback**: `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`

The simulated server selects the preferred cipher suite if present in the client's offered cipher suite list, otherwise falls back to the CBC variant. Client Hello must include `supported_signature_algorithms` extension with at minimum `sha256` + `ecdsa`.

### TLS Test Procedures

Three TLS handshake procedures are defined:

- **PROC_TLS_INITIALIZATION_SERVER_AUTH_ESIPA**: Establishes TLS v1.2 between S_IPAd (client) and EIM (server) on ESipa, with the server using its Variant O certificate (#CERT_EIM_TLS). The EIM server sends ServerHello, Certificate, ServerKeyExchange, and ServerHelloDone.

- **PROC_TLS_INITIALIZATION_SERVER_AUTH**: Establishes TLS v1.2 between EIM (client) and S_SERVER (SM-DP+ or SM-DS simulator) on ES9+' or ES11'. The EIM client sends ClientHello; the simulated server responds with ServerHello + Certificate + ServerKeyExchange + ServerHelloDone.

### HTTPS Test Cases

**ES9+' HTTPS (4.2.15)** — eIM talking to SM-DP+:
- TC_eIM_HTTPS_Nominal:
  - Sequence #01: HTTPS Session Establishment — verifies successful TLS handshake and session creation
  - Sequence #02: Non-reuse of session keys — verifies the eIM uses fresh ephemeral keys for each session, preventing session key reuse attacks
- TC_eIM_HTTPS_ErrorCases:
  - Sequence #01: Invalid (SM-DP+) TLS Certificate signature — verifies the eIM detects and rejects a tampered server certificate
  - Sequence #02: Expired TLS Certificate — verifies the eIM checks certificate validity period
  - Sequence #07: Invalid TLS Certificate based on Invalid CI (Invalid Curve) — verifies the eIM validates the certificate chain's cryptographic algorithm

**ES11' HTTPS (4.2.18)** — eIM talking to SM-DS:
- TC_eIM_ES11'_HTTPS_Nominal:
  - Sequence #01: HTTPS Session Establishment
  - Sequence #02: Non-reuse of session keys
- TC_EIM_ES11'_HTTPS_Error:
  - Sequence #01: Invalid (SM-DS) TLS Certificate signature
  - Sequence #02: Expired TLS Certificate
  - Sequence #07: Invalid TLS Certificate based on Invalid CI (Invalid Curve)

---

## Certificate Checking

### Certificate Types in the Test Ecosystem

SGP.33-3 defines a certificate hierarchy based on SGP.26 test certificates, all using ECDSA on NIST P-256, brainpoolP256r1, or FRP256V1 curves:

| Certificate | Description | Used By |
|-------------|-------------|---------|
| `CERT_EUICC_ECDSA` | eUICC's public key certificate, signed by EUM | eUICC authentication, notification signing |
| `CERT_EUM_ECDSA` | EUM's public key certificate, signed by CI | eUICC certificate chain validation |
| `CERT_CI_ECDSA` | Certificate Issuer root public key | Trust anchor for all certificate verification |
| `CERT_EIM_TLS` | eIM's TLS server certificate (Variant O) | ESipa TLS server authentication |
| `CERT_S_SM_DP_TLS` | Simulated SM-DP+ TLS certificate | ES9+' TLS server authentication |
| `CERT_S_SM_DS_TLS` | Simulated SM-DS TLS certificate | ES11' TLS server authentication |

### Certificate Validation in Test Cases

Certificate validation is tested implicitly throughout the interface test cases. For ES9+' InitiateAuthentication:

- **Error Sequence #04**: Unavailable SM-DP+ Certificate — the simulated server provides no certificate
- **Error Sequence #05**: Invalid SM-DP+ Certificate — the simulated server provides a structurally invalid certificate
- **Error Sequence #06**: Invalid SM-DP+ Signature — the server's signed response has a bad signature
- **Error Sequence #08**: Unsupported CI Key ID — the server uses a certificate chaining to a CI the eIM doesn't trust

For AuthenticateClient (both ES9+' and ES11'):

- **Error Sequences #01–#02**: Invalid/Expired EUM Certificate — tests that the eIM validates the EUM certificate in the eUICC's certificate chain
- **Error Sequences #03–#04**: Invalid/Expired eUICC Certificate — tests eUICC certificate validation
- **Error Sequence #15**: Invalid SM-DP+(pb) certificate — the profile-binding certificate fails validation
- **Error Sequence #16**: Different OID for SM-DP+ Certificates — CERT.DPpb.ECDSA and CERT.DPauth.ECDSA don't belong to the same entity

### Initial State Certificate Configuration

The test environment pre-loads the eIM and simulated eUICC with specific certificate configurations (Annex G):

- **eIM**: Configured with #CERT_EIM_TLS for NIST (and optionally BRP) — ensures the eIM can act as a TLS server on ESipa
- **Test eUICC (ECASD)**: Contains the eUICC Private Key (#SK_EUICC_ECDSA), eUICC Certificate (#CERT_EUICC_ECDSA), CI Public Key (#PK_CI_ECDSA for verifying off-card entity certificates), and EUM Certificate (#CERT_EUM_ECDSA)
- No CRLs are loaded on the test eUICC — CRL testing is deferred
- The CI identified as highest priority in `euiccCiPKIdListForSigning` must also be selectable in `euiccCiPKIdListForVerification`

---

## Signed Package Verification

### eIM Package Signatures

Every eUICC Package Request sent by the eIM over ESep is cryptographically signed. The ASN.1 structure reveals the security wrapping:

```
EuiccPackageRequest ::= {
    euiccPackageSigned {
        eimId            #EIM_ID,
        eidValue         #EID1,
        counterValue     <COUNTER_EIM>,
        eimTransactionId <EIM_TRANSACTION_ID>,    -- optional (O_S_TRID)
        euiccPackage     psmoList : { enable { iccid #ICCID_OP_PROF1 } }
    },
    eimSignature <EIM_SIGNATURE>
}
```

The `eimSignature` covers the entire `euiccPackageSigned` structure, ensuring integrity and authenticity of the PSMO/eCO command. The eUICC verifies this signature using the eIM's public key or certificate stored in its eIM Configuration Data.

### eUICC Package Result Signatures

Results flow back with equivalent protection:

```
ProvideEimPackageResult ::= {
    eidValue         #EID1,
    eimPackageResult euiccPackageResult : euiccPackageResultSigned : {
        euiccPackageResultDataSigned {
            eimId        #EIM_ID1,
            counterValue <COUNTER_EIM>,
            eimTransactionId <EIM_TRANSACTION_ID>,
            seqNumber    <SEQ_NUMBER>,
            euiccResult  { EnableProfileResult : ok }
        },
        euiccSignEPR <EUICC_SIGN_EPR_EPR>
    }
}
```

The `euiccSignEPR` is the eUICC's ECDSA signature over `euiccPackageResultDataSigned` — providing non-repudiation that the eUICC actually executed the requested operation.

### Notification Signatures

Profile state change notifications are also cryptographically signed:

```
PendingNotification ::= otherSignedNotification : {
    tbsOtherNotification {
        seqNumber                  <SEQ_NUMBER>,
        profileManagementOperation { notificationEnable },
        notificationAddress        #TEST_DP_ADDRESS1,
        iccid                      #ICCID_OP_PROF1
    },
    euiccNotificationSignature <TBS_EUICC_NOTIF_SIG>,
    euiccCertificate           #CERT_EUICC_ECDSA,
    eumCertificate             #CERT_EUM_ECDSA
}
```

Notifications include the full certificate chain (eUICC + EUM certificates) alongside the signature, enabling the SM-DP+ to verify the notification without needing pre-loaded eUICC certificates.

---

## Anti-Replay Protection

### CounterValue Mechanism

The `counterValue` field in eUICC Packages is the primary anti-replay mechanism. Defined in Annex B:

> *COUNTER_EIM: Integer value coded maximum on two bytes. Incremented each time the IUT (EIM) generates an eUICC Package Request.*

The eUICC tracks the counter value for each Associated eIM and rejects packages with counter values less than or equal to the last seen value. This prevents:

- **Replay attacks**: An attacker cannot capture and resend a previous eUICC Package because the counter wouldn't advance
- **Out-of-order execution**: Packages must be processed in the order the eIM intended

### UpdateEim and Counter Reset

The UpdateEim function (4.2.7) is specifically designed to update *"the public key or Certificate and the related anti-replay counter value"*. When an eIM rotates its keys, the anti-replay counter is also updated — preventing an attacker from replaying old packages signed with the old key after a key rotation event.

### TransactionID as Additional Correlation

The optional `eimTransactionId` (controlled by O_S_TRID) provides session-level correlation across multiple ESxx interfaces. While not strictly an anti-replay mechanism, it helps detect mismatched or misrouted packages by allowing the eIM and eUICC to verify that messages across ESep, ESipa, ES9+', and ES11' all belong to the same RSP session.

---

## eIM Authentication

### How the eUICC Authenticates the eIM

The eUICC authenticates eIM commands through two mechanisms:

1. **eIM Signature Verification**: Every eUICC Package includes an `eimSignature` over the package contents. The eUICC verifies this signature using the eIM's public key or certificate stored in its eIM Configuration Data (established during AddEim or UpdateEim).

2. **CounterValue Check**: The eUICC verifies the counter value is greater than the last seen value from that eIM, preventing replay.

### ESipa Server Authentication

On the ESipa interface, the eIM acts as the TLS server. The IPA (simulated by S_IPA in testing) authenticates the eIM by verifying its TLS certificate (#CERT_EIM_TLS) during the TLS handshake. This is Server Authentication mode — the IPA authenticates the eIM, not vice versa.

### ES9+' / ES11' Client Authentication

When the eIM communicates with SM-DP+ (ES9+') or SM-DS (ES11'), the eIM acts as the TLS client and authenticates the server. The eIM does not present a client certificate — Server Authentication mode only. The SM-DP+/SM-DS authenticates the eIM indirectly through the eUICC's signatures in AuthenticateClient calls, not through TLS mutual authentication.

---

## Test Certificate Infrastructure

All test certificates are based on SGP.26 (RSP Test Certificates Definition v3.0.2), which provides:

- Valid test keys and certificates for ECDSA on NIST P-256, brainpoolP256r1, and FRP256V1 curves
- Instructions for generating invalid certificates — essential for error case testing (invalid signatures, expired certificates, unsupported curves)
- X.509 format certificate chains (CI → EUM → eUICC) for certificate validation testing

The specification notes that *"SGP.26 [25] contains test keys, valid test certificates and instructions for how to generate invalid certificates"* — test tool providers use SGP.26 as their certificate generation toolkit.

---

## 📋 Summary

- TLS v1.2 in Server Authentication mode is mandatory on all eIM interfaces, with ECDHE_ECDSA cipher suites on NIST P-256 or brainpoolP256r1
- HTTPS test cases validate certificate chain checking (invalid signatures, expired certs, unsupported CI curves) and session key non-reuse
- eUICC Packages are signed by the eIM (`eimSignature`) and verified by the eUICC; results are signed by the eUICC (`euiccSignEPR`)
- Anti-replay protection uses a monotonically increasing `counterValue` per eIM — updated during key rotation via UpdateEim
- Notifications include the full eUICC + EUM certificate chain alongside an eUICC signature for independent verification
- ESipa uses Variant O certificate for eIM server authentication; ES9+' and ES11' use Server Authentication with simulated server certificates
- SGP.26 provides the test certificate infrastructure — valid certificates for positive testing and instructions for generating invalid certificates for error case testing

---

<div align="center">

← Previous: [Key eIM Test Cases: PSMO, Notifications, and Configuration](/docs/articles/sgp33-3/44-sgp33-eim-test-cases) · [🏠 Home](/)

Next: [IoT eSIM Certification Path: From Test Cases to Production](/docs/articles/sgp33-3/46-sgp33-certification) →

</div>

---

*Based on GSMA SGP.33-3 v1.2 (27 January 2025) — eUICC IoT Manager Test Specification, Sections 4.2.10–4.2.18 (TLS/HTTPS testing), Annexes A–B (Constants, Dynamic Content), Annex G (Initial States)*
