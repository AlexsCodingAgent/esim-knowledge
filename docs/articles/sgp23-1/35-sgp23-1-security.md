---
title: "eUICC Security Testing: Certificates, Keys, and Channels"
date: 2026-06-05
---

# eUICC Security Testing: Certificates, Keys, and Channels

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.23-1 eUICC Testing]({{ site.baseurl }}/docs/articles/sgp23-1/) > eUICC Security Testing: Certificates, Keys, and Channels**

> **💡 Why this matters:** The eSIM security model is built on a chain of trust extending from the GSMA Certificate Issuer (CI) down through the eUICC manufacturer (EUM), the SM-DP+, and finally the eUICC itself. If any link in this chain fails — a certificate doesn't validate, a key operation produces wrong results, or a secure channel is established with weak parameters — the entire profile delivery system is compromised. SGP.23-1 devotes significant testing to every cryptographic operation the eUICC must perform.

> **Key takeaways:**
> - Certificate validation tests verify the eUICC can validate chains from CERT.DPauth.ECDSA → CI → root, and correctly reject expired, mis-signed, or wrong-issuer certificates
> - ECDSA operational tests cover signing and verification across four curves: NIST P-256, BrainpoolP256r1, FRP256V1, and SM2
> - ECDH key agreement testing verifies the eUICC correctly establishes shared secrets for SCP03t secure channels
> - SCP03t channel testing covers key derivation, MAC generation/verification, and encrypted command/response handling
> - CRL (Certificate Revocation List) handling tests verify the eUICC loads CRLs correctly and subsequently rejects revoked certificates
> - Key generation testing verifies one-time key pair generation for profile binding (`otPK.eUICC.ECKA` / `otSK.eUICC.ECKA`)
> - The entire test PKI (Annex A.2) is isolated from production: test certificates and keys ensure testing never touches live GSMA infrastructure

Security testing permeates nearly every test case in SGP.23-1, but several test groups focus specifically on cryptographic correctness and secure channel operations.

---

## The Test PKI: A Parallel Trust Infrastructure

SGP.23-1 defines a complete parallel PKI in Annex A.2, completely isolated from production GSMA certificates. The key principle: **test certificates and test keys ensure conformance testing never touches live GSMA infrastructure.**

The test PKI includes:

| Certificate / Key | Role |
|-------------------|------|
| `CERT_S_CI_ECDSA` | Simulated Certificate Issuer — the root of trust for testing |
| `CERT_S_EUM_ECDSA` | Simulated EUM certificate — signs the eUICC's certificates |
| `CERT_S_SM_DPauth_ECDSA` | SM-DP+ authentication certificate — used in `ES9+.InitiateAuthentication` |
| `CERT_S_SM_DPpb_ECDSA` | SM-DP+ profile binding certificate — verified during `PrepareDownload` |
| `CERT_S_SM_DP_TLS` | SM-DP+ TLS server certificate |
| `CERT_S_SM_DS_TLS` | SM-DS TLS certificate |
| `PK_EUICC_SIG` | eUICC public signature key — used to verify `euiccSignPIR` and `euiccSignRPR` |
| `SK_EUICC_SIG` | eUICC private signature key — held securely within the eUICC |

Test eUICCs are pre-loaded with the test CI's public key in their `euiccCiPKIdListForVerification` and `euiccCiPKIdListForSigning` lists. The test SM-DP+ simulator uses `SK.DPauth.SIG` and `SK.DPpb.SIG` to sign its messages, and the eUICC verifies these against the test certificates.

---

## Certificate Validation Tests

Certificate validation is tested implicitly throughout the specification but concentrated in the `AuthenticateServer` test case group (Section 4.2.18) and the Mutual Authentication procedures.

### AuthenticateServer Testing

The eUICC must validate the SM-DP+'s certificate chain during profile download. The `AuthenticateServer` test case verifies:

- **Valid certificate chain**: `CERT.DPauth.ECDSA` is signed by `CERT.CI.ECDSA` which is signed by the CI root — the eUICC must traverse this chain and accept it
- **Wrong certificates**: If the SM-DP+ presents a certificate not chaining to a known CI, the eUICC must reject the authentication
- **Expired certificates**: Certificates with `notAfter` dates in the past must be rejected
- **Mismatched matching IDs**: If the certificate's OID doesn't match the expected SM-DP+ OID for the transaction
- **Unsupported CI public key identifiers**: If `euiccCiPKIdToBeUsed` doesn't match any key in the eUICC's `euiccCiPKIdListForVerification`

The `AuthenticateServer` test case (4.2.18) spans ~51 pages (pages 162–213), making it one of the most extensively specified security test groups.

### PrepareDownload Certificate Verification

During `PrepareDownload`, the eUICC receives the SM-DP+'s profile binding certificate (`CERT.DPpb.ECDSA`). Test cases verify:
- The eUICC correctly hashes the certificate and includes the hash in its response
- That mismatched or invalid certificates are rejected
- Curve-specific certificate handling (NIST P-256, BrainpoolP256r1, FRP256V1)

---

## ECDSA Operational Testing

ECDSA signing and verification operations are tested across all supported curves:

### Curve-Specific Test Variants

| Curve | Mnemonic | Test Cases |
|-------|----------|------------|
| **NIST P-256** | `O_E_NIST` | `PrepareDownloadNIST`, `LoadBoundProfilePackageNIST`, plus NIST variants across all ES8+ and ES10b tests |
| **BrainpoolP256r1** | `O_E_BRP` | `PrepareDownloadBRP`, `LoadBoundProfilePackageBRP`, brainpool variants of all signing/verification tests |
| **FRP256V1** | `O_E_FRP` | `PrepareDownloadFRP`, `LoadBoundProfilePackageFRP` — French national curve testing |
| **SM2** | `O_E_SM2` | Chinese national algorithm — noted as "for further study" in v3.1.3 |

Every test that involves an eUICC signature — including `euiccSignPIR` in profile installation results, `euiccSignRPR` in RPM package results, and the `EUICC_SIGNATURE2` in the PrepareDownload response — must be verified against `#PK_EUICC_SIG` using the appropriate curve.

### Signature Variants

Five signing variants are tested:
- **Variant O** (`O_VAR_O`) — Standard signature format
- **Variant Ov3** (`O_VAR_OV3`) — Updated variant O for V3.x
- **Variants A, B, C** — Alternative signature formats with different data inclusion rules

---

## ECDH Key Agreement and SCP03t Channel Testing

The ES8+ secure channel between the SM-DP+ and the eUICC uses SCP03t (Secure Channel Protocol 03 with TLS-style key agreement) built on ECDH:

### Key Agreement

During `InitialiseSecureChannel`, the SM-DP+ sends its ephemeral public key (`otPK.SM-DP+.ECKA`). The eUICC:
1. Generates its own ephemeral key pair (`otPK.eUICC.ECKA` / `otSK.eUICC.ECKA`)
2. Performs ECDH key agreement to derive shared secret `ShS`
3. Derives session keys (S-ENC, S-MAC, S-RMAC) from `ShS` using KDF
4. Returns `otPK.eUICC.ECKA` and receipt confirmation

Test sequences verify:
- Correct key agreement across all supported curves
- That invalid or malformed public keys are rejected
- That session keys are unique across different sessions

### SCP03t Channel Operations

The SCP03t secure channel protects all subsequent ES8+ commands (`ConfigureISDP`, `StoreMetadata`, `LoadProfileElements`). Test cases verify:
- **MAC generation/verification**: Every command includes a MAC over the command data; every response includes a MAC over the response data
- **Encryption**: Sensitive data (profile content) is encrypted with S-ENC
- **Command chaining**: Multiple STORE DATA commands in sequence with proper chaining
- **Session key replacement**: `ReplaceSessionKeys` rotates session keys mid-session for Perfect Forward Secrecy

### InitialiseSecureChannel Error Handling

The test specification explicitly verifies that the eUICC rejects:
- Invalid Remote Operation IDs in the `InitialiseSecureChannel` request
- Invalid SM-DP+ signatures over the channel parameters
- Invalid Transaction Identifiers that don't match the session
- Invalid CRT (Control Reference Template) values
- A second `InitialiseSecureChannel` request while a secure session is already active

---

## CRL Handling Tests

The `LoadCRL` test case (4.2.17) verifies Certificate Revocation List processing:

- **Loading a valid CRL**: The eUICC must correctly parse the CRL ASN.1 structure and store the revocation information
- **Rejecting revoked certificates**: After loading a CRL, subsequent `AuthenticateServer` calls with certificates listed in that CRL must be rejected
- **CRL format validation**: Malformed CRLs must be rejected with appropriate error codes

CRL support is conditional — not all eUICCs are required to support it, but those that do must handle it correctly.

---

## Key Generation Testing

The eUICC generates several types of keys that are verified during testing:

### One-Time Key Pairs (Profile Binding)

During `PrepareDownload`, the eUICC generates `otPK.eUICC.ECKA` / `otSK.eUICC.ECKA` — the ephemeral key pair used to establish the encrypted download channel. Tests verify:
- Fresh key generation for each `PrepareDownload` call
- That the public key is correctly formatted for the selected curve
- Key reuse behaviour: when `O_E_REUSE_OTPK` is supported, the eUICC reuses the previous key pair for retry attempts after a failed download

### ECASD Operations

The eUICC's ECASD (eUICC Controlling Authority Security Domain) holds the eUICC's long-term identity keys. While not a separate test group, ECASD operations are verified implicitly:
- The eUICC's certificate (`CERT.EUICC.ECDSA`) must be accessible and verifiable
- The private key (`SK.EUICC.ECDSA`) must correctly sign challenges and responses
- The EUM certificate chain must be complete and verifiable

---

## Physical Interface and Transport Security

For Integrated eUICCs using USB CCID (Annex J), the test interface specification includes security requirements:

- **Data integrity**: The test interface must maintain the integrity and order of data between the integrated eUICC and the test system
- **No interference**: The manufacturer must ensure no other SoC subsystems interfere during testing
- **Reliable channel**: Any physical or logical interface is acceptable as long as a USB CCID interface is provided and the channel is reliable

---

## 📋 Summary

- A complete parallel test PKI (Annex A.2) isolates conformance testing from production GSMA certificates and keys
- Certificate validation tests verify the eUICC correctly traverses the CI → EUM → SM-DP+ chain and rejects invalid, expired, or mismatched certificates
- ECDSA operations are tested across four curves (NIST P-256, BrainpoolP256r1, FRP256V1, SM2) with five signature variants
- SCP03t channel testing covers ECDH key agreement, session key derivation, MAC generation/verification, encryption, and session key rotation
- CRL handling tests verify correct loading and subsequent rejection of revoked certificates
- One-time key pair generation is tested for fresh generation and (optionally) retry reuse
- Every eUICC signature (`euiccSignPIR`, `euiccSignRPR`, `EUICC_SIGNATURE2`) is verified against the known test public key `#PK_EUICC_SIG`

---

<div align="center">

← Previous: [Key eUICC Test Cases: ISD-R, ECASD, and Profile Lifecycle]({{ site.baseurl }}/docs/articles/sgp23-1/34-sgp23-1-test-cases) · [🏠 Home]({{ site.baseurl }}/)

Next: [eUICC Certification: From SGP.23-1 Tests to SAS-UP Approval]({{ site.baseurl }}/docs/articles/sgp23-1/36-sgp23-1-certification) →

</div>

---

*Based on GSMA SGP.23-1 v3.1.3 (27 January 2025) — RSP Test Specification for the eUICC, Sections 4.2.3, 4.2.10, 4.2.17, 4.2.18, Annexes A.2, J*
