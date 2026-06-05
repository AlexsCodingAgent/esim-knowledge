---
title: "CRL and Certificate Management in the Test Ecosystem"
date: 2026-06-06
---

# CRL and Certificate Management in the Test Ecosystem

**🏠 [eUICC.tech](/) > [SGP.26 Test Certificates](/docs/articles/sgp26/) > CRL and Certificate Management in the Test Ecosystem**

> **💡 Why this matters:** In production, CRLs are the emergency brake — when a certificate is compromised, the CRL tells every eUICC and server to stop trusting it. In testing, you need to verify that this emergency brake actually works. SGP.26 provides a complete CRL infrastructure with distribution points at every CA level, plus deliberately unusual parameters (3-year CRL validity) that ensure test suites don't break from CRL expiry mid-run.

> **Key takeaways:**
> - The SGP.26 CRL infrastructure covers four CA levels: CI root, CI SubCA, EUM, SM-DP+ SubCA, and SM-DS SubCA — each issues its own CRL
> - All CRLs currently contain empty `revokedCertificates` sequences — no certificates have been revoked (certificates with revoked entries are marked "FFS" — For Future Study)
> - CRL validity is set to 1,095 days (3 years), which SGP.26 notes is "unusual" — chosen deliberately so that no test execution risks failing because the CRL itself expired
> - CRL Distribution Points (CDPs) are embedded in every certificate, pointing to test URLs like `http://ci.test.example.com/CRL-1.crl` and `http://smdp.test.example.com/CRL.crl`
> - The `issuingDistributionPoint` extension controls scope: `onlyContainsCACerts` and `onlyContainsUserCerts` determine whether a CRL covers CAs, end-entities, or both
> - CRL numbering starts from 2024 (decimal) across all issuers — a fixed, predictable value for test reproducibility
> - Certificate expiry and rotation schedules vary dramatically: from 398 days (TLS) to 2,000,000 days (eUICC) — test suites must account for this

The CRL (Certificate Revocation List) infrastructure in SGP.26 mirrors production: every CA that can sign certificates also issues CRLs covering those certificates. The structure is defined in Section 5 of the specification.

---

## CRL Hierarchy: Who Issues What

Each CA in the certificate hierarchy issues CRLs covering certificates it has directly signed:

| CRL Issuer | Covers | Variants | Distribution Point URI |
|---|---|---|---|
| **CI Root** | Certificates signed directly by CI (EUM, SM-DP+ auth/pb/TLS, SM-DS auth/TLS in Variant O) | O, Ov3, A, B, C | `http://ci.test.example.com/CRL-1.crl` + `CRL-2.crl` |
| **CI SubCA** | Certificates signed by CI SubCA (EUM, SM-DP+, SM-DS in Variants B, C; role SubCAs in Variant C) | B, C | Same as CI Root (shares parent) |
| **EUM** | Certificates signed by EUM (eUICC certificates in Variants O, Ov3, B; EUM SubCA in Variants A, C) | All (Variant O/B) / A,C (for SubCA) | `http://eum.test.example.com/CRL.crl` |
| **SM-DP+ SubCA** | Certificates signed by DP SubCA (SM-DP+ auth, pb, TLS in Variants A, C) | A, C | `http://smdp.test.example.com/CRL.crl` |
| **SM-DS SubCA** | Certificates signed by DS SubCA (SM-DS auth, TLS in Variants A, C) | A, C | `http://smds.test.example.com/CRL.crl` |

CRLs for the CI SubCA exist only in Variants B and C (where the CI SubCA exists). CRLs for the EUM, DP SubCA, and DS SubCA exist only in Variants A and C (where those SubCAs exist). In Variant O, only the CI root issues CRLs, covering all end-entity certificates directly.

---

## CRL Structure and Contents

Every SGP.26 CRL is an X.509 v2 CRL conforming to RFC 5280. The core structure:

| Field | Value |
|---|---|
| **version** | V2 (1) — automatically set |
| **signature** | sha256ECDSA (same algorithm as certificates) |
| **issuer** | Same as the issuing CA's Subject DN |
| **thisUpdate** | Timestamp of CRL generation |
| **nextUpdate** | `thisUpdate` + 1,095 days (3 years) |
| **revokedCertificates** | Empty sequence (no revoked certificates) |
| **cRLNumber** | 2024 (decimal) |
| **authorityKeyIdentifier** | `keyId` + `issuer` — references the issuing CA |

The empty `revokedCertificates` sequence is noteworthy. The current version of SGP.26 (v3.0.2) explicitly states: *"The current version of SGP.26 only provides CRLs where no Certificate has been revoked. Test CRLs listing revoked Certificates are FFS."* This means the CRL infrastructure exists and is validatable, but the actual revocation testing — verifying that the eUICC correctly rejects a revoked certificate — is deferred to future versions.

---

## The 3-Year CRL Validity: Deliberately Unusual

SGP.26 sets CRL `nextUpdate` to `thisUpdate` + 1,095 days (3 years). The specification includes an explicit note:

> *"A duration of 3 years for a CRL is unusual. This setting is chosen so that no execution of tests during the validity period of an SGP.26 Server Certificate risks failing because the corresponding CRL is itself expired."*

In production, CRLs typically have much shorter validity — often 24 hours to 7 days for high-security environments. A 3-year CRL would be unacceptable in production because a revoked certificate would remain trusted for up to 3 years on any system that caches CRLs. But in testing, the priority is different: the test suite must run without CRL-expiry interruptions, even for long-duration tests that span months.

The trade-off is understood and accepted within the test context.

---

## CRL Distribution Points (CDPs) in Certificates

Every SGP.26 certificate (except the CI root in variants without CDPs) carries one or more `crlDistributionPoints` in its extensions:

### CI-Issued Certificates (Variant O and CI-issued chains)

```
[1] CRL Distribution Point
    Distribution Point Name:
        Full Name: URL=http://ci.test.example.com/CRL-1.crl

[2] CRL Distribution Point
    Distribution Point Name:
        Full Name: URL=http://ci.test.example.com/CRL-2.crl
```

The dual distribution points provide redundancy. Both point to the same CI root — the CI and CI SubCA share CDP URLs because both are signed by the CI parent, which is valid per RFC 5280.

### Role-Specific SubCA Certificates

SM-DP+ SubCA certificates use:
```
http://smdp.test.example.com/CRL.crl
```

SM-DS SubCA certificates use:
```
http://smds.test.example.com/CRL.crl
```

EUM certificates use:
```
http://eum.test.example.com/CRL.crl
```

### End-Entity Certificates

End-entity certificates inherit CDPs from their issuer. For example, an SM-DP+ auth certificate in Variant A carries the same CDP URLs as the DP SubCA that signed it: `http://smdp.test.example.com/CRL.crl`. In Variant O, it carries the CI root's CDPs: `http://ci.test.example.com/CRL-1.crl` and `CRL-2.crl`.

---

## CRL Extensions: Controlling Scope

### authorityKeyIdentifier

Every CRL includes the issuing CA's key identifier through the AKI extension. This allows a validator to match the CRL to the correct CA certificate — critical when multiple CAs exist in the chain.

### cRLNumber

All SGP.26 CRLs use `cRLNumber = 2024` (decimal). This is a fixed, predictable value that makes CRL identification deterministic in test scenarios. In production, the CRL number monotonically increases with each CRL issuance. In testing, a fixed number simplifies validation — test cases can hardcode the expected value.

### issuingDistributionPoint

The IDP extension controls which certificates the CRL covers:

| CRL Issuer | `onlyContainsCACerts` | `onlyContainsUserCerts` | Scope |
|---|---|---|---|
| **CI Root** | `false` | `false` | Covers both CA and end-entity certificates |
| **CI SubCA** | `false` | `false` | Covers both |
| **EUM** | `true` | — | Covers only CA certificates (EUM SubCA) |
| **SM-DP+ SubCA** | — | `true` | Covers only end-entity certificates (SM-DP+ auth/pb/TLS) |
| **SM-DS SubCA** | — | `true` | Covers only end-entity certificates (SM-DS auth/TLS) |

The EUM's CRL has `onlyContainsCACerts = true` because, in Variants A and C, the EUM signs the EUM SubCA (a CA certificate). In Variants O and B, the EUM signs only eUICC end-entity certificates — but the CRL IDP is still set to `onlyContainsCACerts`, which means an eUICC certificate revocation would need to come from a different mechanism (or the IDP flag would need to change).

The DP SubCA and DS SubCA CRLs have `onlyContainsUserCerts = true` because those SubCAs only sign end-entity server certificates.

---

## Certificate Expiry and Rotation

### Expiry Schedule by Certificate Type

| Certificate Type | Validity | Effective Lifetime |
|---|---|---|
| **CI Root** | 12,783 days (35 years) | Longest — anchors everything |
| **CI SubCA** | Same as CI Root | Same |
| **eUICC** | 2,000,000 days | Effectively permanent |
| **eIM Signing** | 2,555 days (7 years) | Long-lived IoT |
| **EUM** | 1,095 days (3 years) | Matches CRL validity |
| **EUM SubCA** | 1,095 days | Same |
| **SM-DP+ Auth/PB** | 1,095 days | Same |
| **SM-DP+ SubCA** | 1,095 days | Same |
| **SM-DS Auth** | 1,095 days | Same |
| **SM-DS SubCA** | 1,095 days | Same |
| **SM-DP+ TLS** | 398 days | Shortest — mirrors CA/B Forum limits |
| **SM-DS TLS** | 398 days | Same |
| **eIM TLS/DTLS** | 398 days | Same |

### Rotation Implications

**TLS certificates (398 days)**: These are the most frequently rotated. Test suites that run for more than a year must be prepared to update TLS certificates. The SGP.26 ZIP package is updated at least every two years, but TLS certificates may expire before the package is refreshed. Testers should either regenerate TLS certificates with fresh validity periods using the provided configuration templates, or download updated packages when available.

**Server certificates (1,095 days)**: SM-DP+ auth/pb and SM-DS auth certificates have 3-year validity, matching the CRL validity. This coordination is intentional — the CRL remains valid for as long as the certificates it covers.

**CI root (35 years)**: In practice, the CI root validity exceeds any conceivable test suite duration. However, it still has a finite expiry date. Very long-running test infrastructure (e.g., permanent CI/CD pipelines) should note the root expiry date.

**eUICC (2,000,000 days)**: Effectively never expires. This is consistent with production eUICCs, where replacing an expired chip certificate is economically infeasible.

---

## Handling CRLs in Test Environments

### Local CRL Serving

In a typical test setup, the URLs in certificate CDP extensions (`ci.test.example.com`, `smdp.test.example.com`, etc.) do not resolve to real servers. Testers have several options:

1. **Local HTTP Server**: Run a lightweight HTTP server (e.g., Python's `http.server`) serving the CRL files from the SGP.26 ZIP package with the correct URL paths. Configure `/etc/hosts` to point the test domains to `127.0.0.1`.

2. **DNS Configuration**: Configure the test network's DNS server to resolve `*.test.example.com` to a local CRL distribution server.

3. **CRL Preloading**: Some eUICC test platforms support preloading CRLs directly, bypassing HTTP distribution. Consult the vendor's documentation.

4. **CRL Validation Disabling**: For tests that don't specifically test CRL behaviour, some eUICC configurations allow disabling CRL checks. This is appropriate when the test focus is elsewhere (profile download, state transitions) but must be clearly documented.

### CRL File Paths

The CRL files must be served at the exact paths specified in the certificates:

| CDP URL | CRL File |
|---|---|
| `http://ci.test.example.com/CRL-1.crl` | CRL from the CI root |
| `http://ci.test.example.com/CRL-2.crl` | Same CRL file (redundant distribution point) |
| `http://eum.test.example.com/CRL.crl` | CRL from the EUM |
| `http://smdp.test.example.com/CRL.crl` | CRL from the SM-DP+ SubCA |
| `http://smds.test.example.com/CRL.crl` | CRL from the SM-DS SubCA |

### CRL Content-Type

CRLs are served with MIME type `application/pkix-crl`. Ensure your HTTP server is configured to return this Content-Type header — some validators check it.

### CRL and OCSP

SGP.26 does not define OCSP (Online Certificate Status Protocol) responders. The test PKI relies exclusively on CRLs for revocation status. This is consistent with the embedded nature of eUICCs — an eUICC in the field may not have continuous IP connectivity to query an OCSP responder, so CRLs (which can be preloaded and cached) are the preferred revocation mechanism in the RSP ecosystem.

---

## Future: Revocation Testing (FFS)

The specification explicitly marks "Test CRLs listing revoked Certificates" as FFS (For Future Study). When this is implemented, future versions of SGP.26 will provide:

- CRLs with one or more entries in the `revokedCertificates` sequence
- Each entry containing the certificate's serial number, revocation date, and optionally a CRL entry extension indicating the revocation reason
- Corresponding certificates that are valid except for their presence on the CRL
- Test cases in SGP.23 that verify the eUICC correctly rejects certificates listed on the CRL

Until then, the CRL infrastructure exists for structural validation — verifying that CDP URLs resolve, that CRL signatures verify, and that the `nextUpdate` field is checked — but the actual revocation logic is tested indirectly.

---

## 📋 Summary

- The SGP.26 CRL hierarchy has up to five CRL issuers: CI root, CI SubCA, EUM, DP SubCA, and DS SubCA — each covering the certificates they directly sign
- All CRLs currently have empty `revokedCertificates` — revocation testing is deferred ("FFS") to future SGP.26 versions
- CRL validity of 1,095 days (3 years) is deliberately long to prevent CRL-expiry failures during extended test runs
- CRL Distribution Points use test URLs under `test.example.com` — testers must configure local DNS/hosts and HTTP servers to resolve them
- The `issuingDistributionPoint` extension controls CRL scope: EUM CRL covers only CA certs; DP/DS SubCA CRLs cover only end-entity certs; CI CRLs cover both
- Certificate expiry varies from 398 days (TLS) to 2,000,000 days (eUICC) — rotation planning is essential for long-running test infrastructure
- SGP.26 uses CRLs exclusively (no OCSP), consistent with the embedded eUICC environment where continuous connectivity cannot be assumed

---

<div align="center">

← Previous: [Using Test Certificates: Developer Setup and Integration](/docs/articles/sgp26/40-sgp26-development) · [🏠 Home](/)

</div>

---

*Based on GSMA SGP.26 v3.0.2 (27 January 2025) — RSP Test Certificates Definition, Sections 5, Annexes A and E*
