---
title: "SGP.26 Overview: The GSMA RSP Test Certificate Infrastructure"
description: "Covers GSMA SGP.26's publicly documented test certificate infrastructure: a complete PKI with known private keys enabling RSP interoperability testing of eUICCs, SM-DP+, and SM-DS components."
date: 2026-06-06
---

# SGP.26 Overview: The GSMA RSP Test Certificate Infrastructure

**[eUICC.tech]({{ site.baseurl }}/) > [SGP.26 Test Certificates]({{ site.baseurl }}/docs/articles/sgp26/) > SGP.26 Overview: The GSMA RSP Test Certificate Infrastructure**

> **Why this matters:** Every eSIM test runs on certificates: but production certificates are tightly guarded secrets. SGP.26 defines a complete, publicly documented test PKI with known private keys so that eUICC manufacturers, SM-DP+ providers, and device testers can all interoperate without risking real credentials. Without SGP.26, there is no common language for eSIM testing.

> **Key takeaways:**
> - SGP.26 defines the test certificates used by SGP.23 (RSP Test Specification) : not production, not staging, but true *test-only* certificates with openly published private keys
> - All test certificates use NIST P-256 and/or Brainpool P256r1 elliptic curves with SHA-256 signatures
> - The test PKI includes a GSMA Test CI root, plus certificates for every RSP role: EUM, eUICC, SM-DP+ (authentication, profile binding, TLS), SM-DS (authentication, TLS), and eIM (signing, TLS/DTLS)
> - Five certificate chain variants (O, Ov3, A, B, C) reflect real-world deployment patterns: Variant O chains directly to the CI, while variants A/B/C introduce intermediate SubCAs mirroring production hierarchies
> - Test certificates SHALL NOT be present in any commercial RSP product in its operational lifecycle: the GSMA CI's test private key is publicly known
> - The accompanying ZIP package (`SGP.26_v3.x-YYYYMMDD_Files.ZIP`) contains all keys, certificates, CRLs, and OpenSSL configuration files needed to regenerate or extend the test PKI

SGP.26 v3.0.2 (66 pages, 27 January 2025) is the GSMA's normative definition of every X.509 certificate used during RSP interoperability testing. Rather than describing *how* to test, it defines *what* certificates exist, *how* they chain, and *how* to generate them: using OpenSSL 1.1.0e as the reference toolchain.

---

## What Test Certificates Are

In the eSIM ecosystem, certificates are the trust anchors. The eUICC uses its pre-provisioned CI public key to verify that an SM-DP+ is authorised to deliver a profile. The SM-DP+ uses its certificate to sign bound profile packages. The SM-DS uses its certificate to sign discovery responses. Every handshake depends on certificate validation.

Production certificates are generated and guarded by GSMA-accredited Certificate Issuers (CIs). Their private keys never leave Hardware Security Modules. Nobody outside the CI operator ever sees them, which makes them impossible to use in a test lab.

SGP.26 solves this by defining a complete, parallel test PKI:

| Certificate | Role | Count per Curve |
|---|---|---|
| CERT.CI.SIG | Test CI root | 1 |
| CERT.CISUBCA.SIG | CI SubCA (variants B, C) | 1 |
| CERT.EUM.SIG | eUICC Manufacturer | 1 |
| CERT.EUMSUBCA.SIG | EUM SubCA (variants A, C) | 1 |
| CERT.EUICC.SIG | eUICC | 1 |
| CERT.DPauth.SIG | SM-DP+ Authentication | 2 |
| CERT.DPpb.SIG | SM-DP+ Profile Binding | 2 |
| CERT.DP.TLS | SM-DP+ TLS | 4 |
| CERT.DPSubCA.SIG | SM-DP+ SubCA (variants A, C) | 1 |
| CERT.DSauth.SIG | SM-DS Authentication | 1 |
| CERT.DS.TLS | SM-DS TLS | 2 |
| CERT.DSSubCA.SIG | SM-DS SubCA (variants A, C) | 1 |
| CERT.EIM.ECDSA | eIM Signing | 1 |
| CERT.EIM.TLS | eIM TLS/DTLS | 1 |

All private keys are included in the ZIP package. Testers can inspect, regenerate, or extend any certificate in the chain.

---

## How the Test PKI Differs from Production

The structural differences between test and production PKI are minimal: and that's by design. The certificates use the same X.509 profiles, the same elliptic curves, the same key usages, and the same RSP role OIDs. The differences are operational:

| Aspect | Production | SGP.26 Test |
|---|---|---|
| **CI Private Key** | Stored in HSM, never disclosed | Published in PEM file alongside the spec |
| **Certificate Subject** | Real company names, real C= codes | Placeholder subjects: `cn = Test CI`, `o = RSPTEST`, `c = IT` |
| **Validity Period** | Typically 15–25 years for root | 35 years (CI root: 12,783 days) |
| **CRL Distribution Points** | Real, monitored URLs | Test URLs: `http://ci.test.example.com/CRL-1.crl` |
| **eUICC Certificate** | Contains real EID, signed by real EUM | 2,000,000-day validity with test EID `89049032123451234512345678901235` |
| **Certificate Policies OID** | `2.23.146.1.2.1.x` (id-rspRole) | Same OID arc: indistinguishable from production on the wire |

The critical rule: **"Test Certificates SHALL NOT be present in any commercial RSP products in their operational lifecycle."** A production eUICC provisioned with the test CI public key would accept profiles from anyone possessing the publicly-known test CI private key.

---

## The Five Certificate Chain Variants

SGP.26 defines five variants (O, Ov3, A, B, C) that mirror different production deployment models:

**Variant O** : The simplest hierarchy. All certificates chain directly to CERT.CI.SIG. No intermediate SubCAs. The eUICC trusts the CI root directly, and every server certificate is signed by that same root. This variant has its own distinct GSMA Test CI, separate from variants Ov3/A/B/C: useful for SGP.23 testing to distinguish certificates via `euiccCiPKIdListForVerification`.

**Variant B** : Introduces a CI SubCA (CERT.CISUBCA.SIG) between the CI root and end-entity certificates. Mirrors production CIs that delegate signing authority to a subordinate CA. The CI root signs the CI SubCA; the CI SubCA signs all downstream certificates.

**Variant A** : Adds role-specific SubCAs: EUM SubCA (CERT.EUMSUBCA.SIG), SM-DP+ SubCA (CERT.DPSubCA.SIG), and SM-DS SubCA (CERT.DSSubCA.SIG). Each SubCA is signed directly by the CI root. This mirrors production environments where each RSP role operates its own intermediate CA.

**Variant C** : The deepest hierarchy. The CI root signs a CI SubCA, which in turn signs role-specific SubCAs (EUM SubCA, DP SubCA, DS SubCA), which then sign end-entity certificates. Three levels of delegation.

**Variant Ov3** : Same CI root as A/B/C but uses a certificate profile compatible with SGP.22 V3.x series specifications, with the CI certificate containing no CRL Distribution Points extension.

All variants produce cryptographically valid chains that SGP.23 test cases can validate: but each exercises different certificate path-building and validation logic.

---

## The SGP.26→SGP.23 Connection

SGP.26 exists to serve SGP.23. Every certificate defined in SGP.26 is referenced by SGP.23 test cases:

- **SGP.23 eUICC tests**: use CERT.EUICC.SIG to verify the eUICC's certificate validation against CERT.DPauth.SIG and CERT.DPpb.SIG
- **SGP.23 SM-DP+ tests**: use CERT.DPauth.SIG for mutual authentication, CERT.DPpb.SIG for profile binding signatures
- **SGP.23 SM-DS tests**: use CERT.DSauth.SIG for discovery response signatures
- **SGP.23 invalid case tests**: SGP.26 Section 4 defines certificates with deliberately broken signatures, wrong curves (NIST P-192, P-384), wrong key usages, expired validity, missing critical extensions, and incorrect certificate policies: all to test that the eUICC correctly *rejects* them

The invalid test cases are particularly valuable. SGP.26 provides certificates where:
- The last 10 bytes of the DER signature are replaced with zeros (NIST) or the last 8 bytes with `0x11` (Brainpool)
- The curve is switched to NIST P-192 or Brainpool P192r1 (triggering `unsupportedCurve(3)`)
- The `extendedKeyUsage` is set to `clientAuth` only (missing `serverAuth`)
- The `keyUsage` is set to `keyAgreement` instead of `digitalSignature`
- The `certificatePolicies` OID points to the wrong RSP role
- The certificate is expired (validity set to 1 day)

---

## Summary

- SGP.26 defines the complete test certificate infrastructure used by SGP.23 RSP testing : ~40 certificates across 13 certificate types per elliptic curve
- The test PKI is a parallel universe to production: same X.509 profiles, same curves, same OIDs: but with publicly known private keys and placeholder identities
- Five certificate chain variants (O, Ov3, A, B, C) test every delegation depth from direct-CI to three-level SubCA hierarchies
- The accompanying ZIP package contains all keys in PEM format, certificates in DER format, CRLs, and OpenSSL `.cnf` configuration files for regeneration
- Section 4 defines deliberately invalid certificates for negative testing: corrupted signatures, wrong curves, missing extensions, expired certs
- All test certificates are governed by the absolute rule: never deploy to production

---

<div align="center">

<a href="{{ site.baseurl }}/"> Home</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp26/38-sgp26-hierarchy">Test Certificate Hierarchy: CI, EUM, DP, DS, and eUICC</a> →

</div>

---

*Based on GSMA SGP.26 v3.0.2 (27 January 2025) : RSP Test Certificates Definition, Sections 1, 2, and Annex A*


---

[Section Index](index) | Next: [Test Certificate Hierarchy: CI, EUM, DP, DS, and eUICC](38-sgp26-hierarchy) →
