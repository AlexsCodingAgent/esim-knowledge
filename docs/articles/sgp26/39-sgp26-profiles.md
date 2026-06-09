---
title: "Certificate Profiles: What Makes a Valid Test Certificate"
description: "Walks through SGP.26 X.509 certificate profiles for each RSP role — covering key usage, certificate policies OIDs, basic constraints, and SKI/AKI chaining required for eUICC certificate validation."
date: 2026-06-06
---

# Certificate Profiles: What Makes a Valid Test Certificate

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.26 Test Certificates]({{ site.baseurl }}/docs/articles/sgp26/) > Certificate Profiles: What Makes a Valid Test Certificate**

> **💡 Why this matters:** An eUICC doesn't just verify a signature: it validates the entire certificate profile: key usage, extended key usage, certificate policies, basic constraints, subject key identifier chaining, and CRL distribution points. One wrong extension and the eUICC must reject the certificate. SGP.26 defines the exact extension profile for each certificate type so that testers know precisely what "valid" means: and what deliberate violations trigger which error codes.

> **Key takeaways:**
> - Every test certificate conforms to X.509 v3 (RFC 5280) with ECDSA signatures: the version, serial number, signature algorithm, issuer, validity, subject, and extensions are fully specified for each certificate type
> - Certificate Policies OIDs (`2.23.146.1.2.1.x`) encode the RSP role: CI, eUICC, SM-DP+ auth, SM-DP+ pb, SM-DP+ TLS, SM-DS auth, SM-DS TLS, EUM: and are checked by the eUICC during certificate validation
> - `keyUsage` is always marked Critical and uses role-specific combinations: CAs get `keyCertSign` + `cRLSign`; end-entities get `digitalSignature`; TLS certs add extended key usage for `serverAuth` + `clientAuth`
> - `basicConstraints` distinguishes CAs (`CA = true`, with optional `pathLenConstraint`) from end entities (absent or `CA = false`)
> - Subject Key Identifier (SKI) and Authority Key Identifier (AKI) create the cryptographic chain: SKI is the SHA-1 hash of the public key; AKI references the issuer's SKI
> - `nameConstraints` on the EUM certificate restricts permitted EIN prefixes to `89049032` using a GSMA-specific extension (`2.23.146.1.2.2.0`)
> - The eUICC certificate is the only end-entity certificate with a certificatePolicies extension marked Critical

The certificate profiles in SGP.26 are designed to be indistinguishable from production certificates on the wire. Every extension, every OID, every flag matches what a real GSMA CI would issue. The only differences are the placeholder subject names and the publicly-known private keys.

---

## Algorithm Requirements

SGP.26 mandates two elliptic curves:

| Curve | OpenSSL Name | Key Size | Signature Size | Use |
|---|---|---|---|---|
| **NIST P-256** | `prime256v1` | 256 bits | 64 bytes (DER-encoded) | All certificate types |
| **Brainpool P256r1** | `brainpoolP256r1` | 256 bits | 64 bytes (DER-encoded) | All certificate types |

The signature algorithm in every certificate's `signatureAlgorithm` field and the TBS certificate's `signature` field is `sha256ECDSA` : SHA-256 hash signed with ECDSA over the specified curve.

No RSA, no EdDSA, no P-384 or P-521 certificates are defined for valid test cases. The invalid test cases (Section 4) deliberately introduce P-192 and P-384 certificates to verify that the eUICC correctly rejects unsupported curves with error code `unsupportedCurve(3)`.

---

## Certificate Policies: The Role OID System

The `certificatePolicies` extension is the primary mechanism by which the eUICC determines what role a certificate is authorized to play. The GSMA-registered OID arc `2.23.146.1.2.1` (id-rspRole) defines the RSP role taxonomy:

| Certificate Type | Policy OID (Variant O) | Policy OID (Variants A/B/C) | Critical? |
|---|---|---|---|
| **CI** | `2.23.146.1.2.1.0` | `2.23.146.1.2.1.0` | No |
| **CI SubCA** | : | `2.23.146.1.2.1.0.0` | No |
| **eUICC** | `2.23.146.1.2.1.1` | `2.23.146.1.2.1.0.0.0.0.0` | **Yes** |
| **SM-DP+ Auth** | `2.23.146.1.2.1.2` | `2.23.146.1.2.1.0.0.1.2` | No |
| **SM-DP+ TLS** | `2.23.146.1.2.1.3` | `2.23.146.1.2.1.0.0.1.0` | Variant O: No; Others: **Yes** |
| **SM-DP+ PB** | `2.23.146.1.2.1.5` | `2.23.146.1.2.1.0.0.1.5` | No |
| **SM-DS Auth** | `2.23.146.1.2.1.7` | `2.23.146.1.2.1.0.0.2.1` | Variant O: **Yes**; Others: **Yes** |
| **SM-DS TLS** | `2.23.146.1.2.1.6` | `2.23.146.1.2.1.0.0.2.0` | Variant O: No; Others: **Yes** |
| **EUM** | `2.23.146.1.2.1.5` | `2.23.146.1.2.1.0.0.0.0` | No |

The Variant O OID scheme is flat: each role gets a distinct final integer. The Variant A/B/C scheme is hierarchical: the CI root is `...0`, the CI SubCA is `...0.0`, and end-entity certificates add more levels.

The `certificatePolicies` extension is marked Critical on the eUICC certificate (both variants) and on SM-DS Auth (both), SM-DP+ TLS (A/B/C), and SM-DS TLS (A/B/C). When Critical, a validator MUST recognize and accept the policy: an eUICC that doesn't understand the policy OID must reject the certificate.

Invalid test cases in Section 4 deliberately set the wrong policy OID: e.g., an SM-DP+ TLS certificate with the SM-DP+ auth policy OID (`...2` or `...1.2`) to verify rejection.

---

## Key Usage and Extended Key Usage

### CA Certificates (CI, CI SubCA, EUM, EUM SubCA, DP SubCA, DS SubCA)

All CA certificates carry:
- **keyUsage**: Critical, `keyCertSign` + `cRLSign`
- **basicConstraints**: Critical, `CA = true`, optionally `pathLenConstraint = 0`

The `keyCertSign` usage authorizes the CA to sign subordinate certificates. The `cRLSign` usage authorizes CRL issuance. Both are always present together: SGP.26 does not define separate CRL signers.

The `pathLenConstraint = 0` on EUM, EUM SubCA, DP SubCA, and DS SubCA certificates means they can only sign end-entity certificates: they cannot delegate further. The CI root and CI SubCA have no `pathLenConstraint`, allowing them to sign SubCAs.

### End-Entity Certificates (eUICC, SM-DP+ auth, SM-DP+ pb)

These certificates carry:
- **keyUsage**: Critical, `digitalSignature`
- **basicConstraints**: Absent (no CA flag)

The `digitalSignature` key usage is sufficient for the signature verification these certificates perform during mutual authentication and profile binding. They do not need `keyEncipherment` or `keyAgreement` : key agreement for ES8+ secure channels uses ephemeral ECDH keys, not the certificate key.

### TLS Certificates (SM-DP+ TLS, SM-DS TLS, eIM TLS/DTLS)

TLS certificates carry:
- **keyUsage**: Critical, `digitalSignature`
- **extendedKeyUsage**: Critical, `serverAuth` + `clientAuth`

The dual `serverAuth` + `clientAuth` EKU is deliberate. In the eSIM ecosystem, SM-DP+ and SM-DS servers act as TLS servers when the LPA connects to them, but they may also act as TLS clients when connecting to each other (e.g., SM-DP+ pushing event registrations to SM-DS). The eIM's TLS/DTLS certificate similarly needs both roles for SGP.32's IoT connectivity.

Invalid test cases provide certificates where:
- `extendedKeyUsage` is set to `clientAuth` only (missing `serverAuth`)
- `extendedKeyUsage` is completely absent (missing critical extension)
- `keyUsage` is set to `keyAgreement` instead of `digitalSignature`

---

## Subject Key Identifier and Authority Key Identifier

SKI and AKI form the cryptographic chain that binds certificates to their issuers:

- **Subject Key Identifier (SKI)**: Always present. Computed as the SHA-1 hash of the subject's DER-encoded public key (the `hash` method in OpenSSL). Same computation as RFC 5280 method (1).
- **Authority Key Identifier (AKI)**: Present on all non-root certificates. Contains both `keyIdentifier` (the issuer's SKI hash) and `authorityCertIssuer` (the issuer's Subject DN). This dual identification allows path-building even when multiple CAs share the same name pattern.

The CI root certificate is the only certificate without an AKI: it is self-signed, so its Issuer equals its Subject, and referencing its own key identifier would be redundant (though RFC 5280 permits it).

---

## Basic Constraints and Path Length

The `basicConstraints` extension is Critical on all CA certificates and absent on end-entity certificates:

| Certificate | CA | pathLenConstraint | Meaning |
|---|---|---|---|
| **CI Root** | true | absent | Unlimited delegation depth |
| **CI SubCA** | true | absent | Can sign SubCAs + end-entities |
| **EUM** | true | 0 | Can only sign eUICC certificates |
| **EUM SubCA** | true | 0 | Can only sign EUM certificates |
| **DP SubCA** | true | 0 | Can only sign SM-DP+ certificates |
| **DS SubCA** | true | 0 | Can only sign SM-DS certificates |
| **All end-entities** | absent | : | Not a CA |

The `pathLenConstraint = 0` enforcement is critical for test scenarios. When the eUICC validates a certificate chain, it must verify that no CA exceeded its path length: a chain of CI → CI SubCA → DP SubCA → SM-DP+ auth has 2 intermediate CAs, which is valid because the CI SubCA has no constraint and the DP SubCA has `pathLenConstraint = 0` (it is the last CA, directly signing the end-entity).

---

## Name Constraints: EIN Restriction

The EUM certificate carries a Critical `nameConstraints` extension using the GSMA-specific extension OID `2.23.146.1.2.2.0`. The constraint specifies:

```
permittedSubtrees:
  ein = 89049032
```

This means the EUM may only sign eUICC certificates whose EID begins with `89049032`. The `ein` name form is defined within the GSMA extension: it is not a standard X.509 `directoryName`, `dNSName`, or `rfc822Name`. The constraint is encoded as an ASN.1 SEQUENCE:

```
2.23.146.1.2.2.0 = ASN1:SEQUENCE:permittedEins
[permittedEins]
ein1 = 89049032
```

During certificate validation, the eUICC checks that its own EID falls within the permitted EIN subtree. A test eUICC with EID `89049032123451234512345678901235` passes this check. An eUICC with an EID starting with `89049033` would fail and the certificate must be rejected.

---

## Subject Alternative Name

The `subjectAltName` extension carries GSMA-registered OIDs that identify RSP entities:

| Certificate Type | SAN (Variant O) | SAN (Variants A/B/C) |
|---|---|---|
| **CI Root / CI SubCA** | `RID:2.999.1` | `RID:2.999.1` |
| **EUM / EUM SubCA** | `RID:2.999.5` | `RID:2.999.101` |
| **SM-DP+ Auth/PB (server 1)** | `RID:2.999.10` | `RID:2.999.231` |
| **SM-DP+ Auth/PB (server 2)** | `RID:2.999.12` | `RID:2.999.232` |
| **SM-DP+ TLS (server 1)** | `RID:2.999.10` + `DNS:testsmdpplus1.example.com` | `RID:2.999.251` + `DNS:testsmdpplus1.example.com` |
| **SM-DS Auth** | `RID:2.999.15` | `RID:2.999.331` |
| **SM-DS TLS (server 1)** | `RID:2.999.15` + `DNS:testrootsmds.example.com` | `RID:2.999.251` + `DNS:testrootsmds.example.com` |
| **eIM TLS/DTLS** | `RID:2.999.20` + `DNS:eim.example.com` | Same |

The `RID` (Registered ID) form uses OIDs under the `2.999` arc, which belongs to a GSMA-assigned private enterprise number. These OIDs are not globally unique identifiers like domain names: they serve as test identifiers that SGP.23 test cases can reference.

TLS certificates add DNS SAN entries because TLS clients validate the server's hostname against the SAN. SM-DP+ TLS certificates carry their operational DNS name (e.g., `testsmdpplus1.example.com`).

---

## CRL Distribution Points

The `crlDistributionPoints` extension provides URLs where CRLs can be fetched:

- **CI root (Variant O)**: Two distribution points : `http://ci.test.example.com/CRL-1.crl` and `http://ci.test.example.com/CRL-2.crl`
- **CI SubCA (Variants B, C)**: Same URLs as CI root (valid because both are signed by the same parent)
- **EUM**: `http://ci.test.example.com/CRL-1.crl` (Variant O) or equivalent
- **SM-DP+ SubCA**: `http://smdp.test.example.com/CRL.crl`
- **SM-DS SubCA**: `http://smds.test.example.com/CRL.crl`
- **TLS and end-entity certificates**: Inherit CRL DPs from their issuer

The dual distribution points on CI-issued certificates provide redundancy. The test URLs use `example.com` : these are non-routable placeholder domains. In a real test setup, testers configure DNS or host files to resolve these to their own CRL distribution servers.

---

## Validity Periods

SGP.26 uses deliberately long validity periods to avoid certificate expiry during testing:

| Certificate | Validity | Rationale |
|---|---|---|
| **CI Root** | 12,783 days (35 years) | Must outlast all subordinate certificates |
| **CI SubCA** | Same as CI Root | Same rationale |
| **EUM** | 1,095 days (3 years) | Reasonable rotation period |
| **EUM SubCA** | 1,095 days | Same as EUM |
| **DP SubCA** | 1,095 days | Reasonable rotation |
| **DS SubCA** | 1,095 days | Reasonable rotation |
| **eUICC** | 2,000,000 days (≈5,479 years) | Must never expire during chip lifetime |
| **SM-DP+ Auth/PB** | 1,095 days | Reasonable rotation |
| **SM-DP+ TLS** | 398 days | Mirrors CA/Browser Forum TLS certificate limits |
| **SM-DS Auth** | 1,095 days | Reasonable rotation |
| **SM-DS TLS** | 398 days | Mirrors CA/Browser Forum limits |
| **eIM Signing** | 2,555 days (7 years) | Long-lived IoT deployments |
| **eIM TLS/DTLS** | 398 days | Standard TLS validity |

The eUICC certificate's 2,000,000-day validity is a pragmatic approximation of "never expires." OpenSSL does not support truly infinite-duration certificates, so the maximum practical value is used. In production, eUICC certificates are similarly long-lived because replacing them requires physical access to the chip.

---

## The Invalid Certificate Profiles (Section 4)

SGP.26 Section 4 defines deliberately invalid certificate variations for negative testing:

| Invalid Case | What's Wrong | Expected Error |
|---|---|---|
| **Invalid Signature** | Last 10 bytes (NIST) / 8 bytes (BRP) of DER replaced with zeros / `0x11` | Signature verification failure |
| **Invalid Curve (P-192)** | Certificate uses NIST P-192 or Brainpool P192r1 | `unsupportedCurve(3)` |
| **Invalid Curve (P-384)** | TLS certificate uses NIST P-384 | `unsupportedCurve(3)` |
| **Invalid Certificate Policy** | Policy OID points to wrong role (e.g., auth OID on TLS cert) | Policy validation failure |
| **Missing Critical Extension** | `extendedKeyUsage` absent from TLS cert | Extension validation failure |
| **Invalid Extended Key Usage** | EKU set to `clientAuth` only (TLS cert missing `serverAuth`) | EKU validation failure |
| **Invalid Key Usage** | `keyUsage` set to `keyAgreement` instead of `digitalSignature` | Key usage validation failure |
| **Expired Certificate** | Validity set to 1 day | Certificate expired error |

These invalid certificates are generated from the same templates as valid certificates, with specific fields modified after generation (for signatures) or configuration changes (for extensions). They exist for SM-DP+ auth, SM-DP+ pb, SM-DP+ TLS, SM-DS auth, and SM-DS TLS certificates.

---

## 📋 Summary

- Certificate Policies OIDs encode the RSP role and are marked Critical on the eUICC, SM-DP+ TLS, SM-DS Auth, and SM-DS TLS certificates
- CAs use `keyCertSign` + `cRLSign`; end-entities use `digitalSignature`; TLS certs add `serverAuth` + `clientAuth` through extended key usage
- `basicConstraints` with `pathLenConstraint = 0` on SubCAs enforces that they can only sign end-entities: no further delegation
- The EUM certificate's `nameConstraints` extension restricts permitted EINs to `89049032` using the GSMA-specific extension `2.23.146.1.2.2.0`
- SKI = SHA-1 of public key; AKI = issuer's SKI + issuer DN: present on all non-root certificates
- Validity periods range from 398 days (TLS) to 2,000,000 days (eUICC) to accommodate different lifecycle requirements
- Section 4's invalid certificates provide 32+ defective variants for negative testing across SM-DP+ and SM-DS

---

<div align="center" markdown="1">

← Previous: [Test Certificate Hierarchy: CI, EUM, DP, DS, and eUICC]({{ site.baseurl }}/docs/articles/sgp26/38-sgp26-hierarchy) · [🏠 Home]({{ site.baseurl }}/)

Next: [Using Test Certificates: Developer Setup and Integration]({{ site.baseurl }}/docs/articles/sgp26/40-sgp26-development) →

</div>

---

*Based on GSMA SGP.26 v3.0.2 (27 January 2025) : RSP Test Certificates Definition, Sections 3, 4, and Annex E*


---

← Previous: [Test Certificate Hierarchy: CI, EUM, DP, DS, and eUICC](38-sgp26-hierarchy) | [Section Index](index) | Next: [Using Test Certificates: Developer Setup and Integration](40-sgp26-development) →
