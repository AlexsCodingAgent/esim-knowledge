---
title: "Test Certificate Hierarchy: CI, EUM, DP, DS, and eUICC"
date: 2026-06-06
---

# Test Certificate Hierarchy: CI, EUM, DP, DS, and eUICC

**🏠 [eUICC.tech](/) > [SGP.26 Test Certificates](/docs/articles/sgp26/) > Test Certificate Hierarchy: CI, EUM, DP, DS, and eUICC**

> **💡 Why this matters:** Certificate validation in eSIM is not just about checking a signature — it's about walking a chain of trust from a known root through potentially multiple intermediate CAs, verifying path length constraints, name constraints, and role-specific policy OIDs at every step. SGP.26 gives you the complete chain for every RSP entity, so you can trace exactly how trust flows from the GSMA Test CI down to an individual eUICC or SM-DP+ TLS endpoint.

> **Key takeaways:**
> - The test PKI spans up to 4 levels: Root CI → CI SubCA → Role SubCA → End Entity, depending on the variant
> - The CI root (CERT.CI.SIG) uses NIST P-256/Brainpool P256r1, signs with SHA-256, has a 35-year validity, and carries `keyCertSign` + `cRLSign` key usage
> - The EUM certificate (CERT.EUM.SIG) anchors the eUICC manufacturing trust domain — it signs the eUICC certificate and carries a `nameConstraints` extension restricting permitted EINs to `89049032`
> - SM-DP+ servers hold three certificates each: one for authentication (CERT.DPauth.SIG), one for profile binding (CERT.DPpb.SIG), and one for TLS (CERT.DP.TLS) — each with distinct key usages and policy OIDs
> - The eUICC certificate has a 2,000,000-day validity (effectively infinite), uses `digitalSignature` key usage, and carries the policy OID `2.23.146.1.2.1.0.0.0.0.0` (id-rspRole-euicc)
> - eIM certificates (signing + TLS/DTLS) chain directly to the CI root and are not scoped by variants — they have no SubCA delegates

The SGP.26 certificate hierarchy mirrors the trust relationships defined in SGP.22's PKI architecture. Every certificate is an X.509 v3 certificate conforming to RFC 5280, with ECDSA signatures over NIST P-256 or Brainpool P256r1.

---

## Level 0: The GSMA Test CI Root

The Certificate Issuer (CI) root is the ultimate trust anchor. Two distinct CI roots exist:

- **CI Root for Variant O** — Subject: `cn = Test CI, ou = TESTCERT, o = RSPTEST, c = IT`. Includes `crlDistributionPoints` extension pointing to `http://ci.test.example.com/CRL-1.crl` and `CRL-2.crl`.
- **CI Root for Variants Ov3, A, B, C** — Same subject but without the `crlDistributionPoints` extension (Variant Ov3) or with it added for other variants.

Both CI roots have:
- **Validity**: 12,783 days (35 years)
- **Key Usage**: Critical, `keyCertSign` + `cRLSign`
- **Basic Constraints**: Critical, `CA = true`
- **Certificate Policies**: `2.23.146.1.2.1.0` (id-rspRole-ci)
- **Subject Key Identifier**: SHA-1 hash of the public key
- **Subject Alternative Name**: `RID:2.999.1` (a GSMA-registered OID)
- **Serial Number**: Variant O = `0x00B874F3ABFA6C44D3`; Variants A/B/C = `0x000`

The CI root is self-signed — its Issuer field equals its Subject field.

---

## Level 1: CI SubCA (Variants B and C)

The CI SubCA (CERT.CISUBCA.SIG) is the first delegation level, present only in Variants B and C:

| Field | Value |
|---|---|
| **Subject** | `cn = Test CI SubCA, ou = TESTCERT, o = RSPTEST, c = ES` |
| **Issuer** | Same as CI Root subject |
| **Validity** | Same as CI Root (35 years) |
| **Key Usage** | Critical, `keyCertSign` + `cRLSign` |
| **Basic Constraints** | Critical, `CA = true` |
| **Certificate Policies** | `2.23.146.1.2.1.0.0` (one level below id-rspRole-ci) |
| **AKI** | keyId + issuer from CI Root |
| **CRL DPs** | Same URLs as CI root — valid because both CI and CI SubCA are signed by the same parent |

The CI SubCA can sign EUM, EUM SubCA, SM-DP+, SM-DP+ SubCA, SM-DS, and SM-DS SubCA certificates — essentially all downstream entities except the CI root itself.

For Variant C, the CI SubCA also signs the role-specific SubCAs (EUM SubCA, DP SubCA, DS SubCA), which then sign end-entity certificates.

---

## Level 2: Role-Specific SubCAs (Variants A and C)

### EUM SubCA (CERT.EUMSUBCA.SIG) — Variants A, C

The EUM SubCA delegates the eUICC manufacturer's signing authority. Its `pathLenConstraint = 0` means it can sign end-entity certificates (eUICCs) but not further SubCAs:

| Field | Value |
|---|---|
| **Subject** | `cn = Test EUM SubCA, ou = TESTCERT, o = RSPTEST, c = ES` |
| **Key Usage** | Critical, `keyCertSign` + `cRLSign` |
| **Basic Constraints** | Critical, `CA = true, pathLenConstraint = 0` |
| **Certificate Policies** | `2.23.146.1.2.1.5` (id-rspRole-eum) |
| **Validity** | 1,095 days (3 years) |

### SM-DP+ SubCA (CERT.DPSubCA.SIG) — Variants A, C

Delegates SM-DP+ server certificate signing. Also `pathLenConstraint = 0`:

| Field | Value |
|---|---|
| **Subject** | `cn = Test CI SM_DPSubCA, ou = TESTCERT, o = RSPTEST, c = ES` |
| **Key Usage** | Critical, `keyCertSign` + `cRLSign` |
| **Basic Constraints** | Critical, `CA = true, pathLenConstraint = 0` |
| **Certificate Policies** | `2.23.146.1.2.1.0.0.1` |
| **Validity** | 1,095 days (3 years) |

### SM-DS SubCA (CERT.DSSubCA.SIG) — Variants A, C

Delegates SM-DS server certificate signing:

| Field | Value |
|---|---|
| **Subject** | `cn = Test CI SM_DSSubCA, ou = TESTCERT, o = RSPTEST, c = ES` |
| **Key Usage** | Critical, `keyCertSign` + `cRLSign` |
| **Basic Constraints** | Critical, `CA = true, pathLenConstraint = 0` |
| **Certificate Policies** | `2.23.146.1.2.1.0.0.2` |
| **Validity** | 1,095 days (3 years) |

For Variant A, all three SubCAs are signed by the CI root. For Variant C, the CI root signs the CI SubCA, which signs the role SubCAs, which sign end-entity certificates.

---

## Level 3: End-Entity Certificates

### EUM Certificate (CERT.EUM.SIG)

The eUICC Manufacturer certificate is a CA certificate (it signs eUICC certificates) and exists in all variants:

| Field | Value |
|---|---|
| **Subject** | `cn = Test EUM, ou = TESTCERT, o = RSPTEST, c = ES` |
| **Issuer** | Variant O: CI root; Variant B: CI SubCA; Variants A, C: EUM SubCA |
| **Validity** | 1,095 days (3 years) |
| **Key Usage** | Critical, `keyCertSign` + `cRLSign` |
| **Basic Constraints** | Critical, `CA = true, pathLenConstraint = 0` |
| **Certificate Policies** | Variant O: `2.23.146.1.2.1.5`; Variants A/B/C: `2.23.146.1.2.1.0.0.0.0` |
| **Name Constraints** | Critical. Permitted EINs: `89049032` (GSMA-specific extension `2.23.146.1.2.2.0`) |
| **SAN** | Variant O: `RID:2.999.5`; Variants A/B/C: `RID:2.999.101` |

The name constraints extension is critical — it restricts which EINs (eUICC Identifier namespace prefixes) the EUM is authorized to sign for. In the test PKI, only EINs beginning with `89049032` are permitted. A production EUM would have its own assigned EIN prefix.

### eUICC Certificate (CERT.EUICC.SIG)

The leaf certificate on every test eUICC:

| Field | Value |
|---|---|
| **Subject** | `cn = Test eUICC, serialNumber = 89049032123451234512345678901235, o = <same as EUM>, c = ES` |
| **Issuer** | Variants O, Ov3, B: EUM; Variants A, C: EUM SubCA |
| **Validity** | 2,000,000 days (≈5,479 years — effectively infinite) |
| **Key Usage** | Critical, `digitalSignature` |
| **Certificate Policies** | Critical. Variant O: `2.23.146.1.2.1.1`; Variants A/B/C: `2.23.146.1.2.1.0.0.0.0.0` (id-rspRole-euicc) |
| **Serial Number** | Variant O: EID string; Variants A/B/C: EID value from Annex E.1 |

The eUICC certificate's `serialNumber` in the Subject DN contains the eUICC's EID — the unique identifier that binds the certificate to a specific chip. The 2,000,000-day validity reflects the reality that eUICC certificates must never expire during the chip's operational life.

---

### SM-DP+ Certificates

Every test SM-DP+ server holds three certificates with distinct purposes:

| Certificate | Key Usage | Certificate Policies OID (Variant O) | Subject Example | Validity |
|---|---|---|---|---|
| **CERT.DPauth.SIG** | Critical, `digitalSignature` | `2.23.146.1.2.1.2` (id-rspRole-dp-auth) | `cn = TEST SM-DP+ 1, o = ACME` | 1,095 days |
| **CERT.DPpb.SIG** | Critical, `digitalSignature` | `2.23.146.1.2.1.5` (id-rspRole-dp-pb) | `cn = TEST SM-DP+ 1, o = ACME` | 1,095 days |
| **CERT.DP.TLS** | Critical, `digitalSignature` | `2.23.146.1.2.1.3` (id-rspRole-dp-tls) | `cn = testsmdpplus1.example.com, o = ACME` | 398 days |

The TLS certificate additionally carries:
- **Extended Key Usage**: Critical, `serverAuth` + `clientAuth`
- **Subject Alternative Name**: DNS name (`testsmdpplus1.example.com`) + RID OID (`RID:2.999.10`)

SGP.26 provides TLS certificates for four SM-DP+ instances (servers 1, 2, 4, 8) to support multi-server test scenarios.

The auth certificate is presented during ES9+ mutual authentication. The pb certificate signs Bound Profile Packages during ES8+ download. The TLS certificate secures the ES9+ HTTPS connection. These three roles are deliberately separated into distinct certificates — a production SM-DP+ would do the same to limit the blast radius of a key compromise.

---

### SM-DS Certificates

SM-DS servers hold two certificates:

| Certificate | Key Usage | Certificate Policies OID (Variant O) | Subject Example | Validity |
|---|---|---|---|---|
| **CERT.DSauth.SIG** | Critical, `digitalSignature` | `2.23.146.1.2.1.7` (id-rspRole-ds-auth) | `cn = TEST SM-DS 1, o = ACME` | 1,095 days |
| **CERT.DS.TLS** | Critical, `digitalSignature` | `2.23.146.1.2.1.6` (id-rspRole-ds-tls) | `cn = testrootsmds.example.com, o = RSPTEST` | 398 days |

SM-DS TLS certificates carry `serverAuth` + `clientAuth` extended key usage and a DNS SAN. Two SM-DS TLS certificates are provided per curve (servers 1 and 2).

---

### eIM Certificates

The eIM (eSIM IoT Manager) signs eUICC package requests in SGP.32 IoT environments:

| Certificate | Key Usage | Issuer | Subject | Validity |
|---|---|---|---|---|
| **CERT.EIM.ECDSA** | Critical, `digitalSignature` | CI root | `cn = eim.example.com, c = DE` | 2,555 days (7 years) |
| **CERT.EIM.TLS** | Critical, `digitalSignature`; EKU: `serverAuth` + `clientAuth` | CI root | `cn = eim.example.com, c = DE` | 398 days |

eIM certificates chain directly to the CI root — they are not scoped by variants and have no SubCA delegates.

---

## Trust Relationships Across Variants

```
Variant O:          CI ─┬── EUM ── eUICC
                        ├── SM-DP+ (auth, pb, TLS)
                        ├── SM-DS (auth, TLS)
                        └── eIM (sign, TLS)

Variant B:          CI ── CISubCA ──┬── EUM ── eUICC
                                   ├── SM-DP+ (auth, pb, TLS)
                                   └── SM-DS (auth, TLS)

Variant A:          CI ──┬── EUM SubCA ── EUM ── eUICC
                        ├── DP SubCA ── SM-DP+ (auth, pb, TLS)
                        └── DS SubCA ── SM-DS (auth, TLS)

Variant C:          CI ── CISubCA ──┬── EUM SubCA ── EUM ── eUICC
                                   ├── DP SubCA ── SM-DP+ (auth, pb, TLS)
                                   └── DS SubCA ── SM-DS (auth, TLS)
```

These variants are not arbitrary — they reflect real-world deployment patterns. Variant O represents a legacy model where the CI signs everything directly. Variant B represents a CI that delegates to a single SubCA. Variant A represents a CI that uses role-specific SubCAs. Variant C represents the fully-delegated model with both a CI SubCA and role-specific SubCAs — the deepest hierarchy, exercising the most complex certificate path validation.

---

## Key Sizes and Algorithm Requirements

All SGP.26 certificates use ECDSA with one of two curves:

- **NIST P-256** (prime256v1) — 256-bit elliptic curve, 32-byte private keys
- **Brainpool P256r1** — 256-bit Brainpool curve, 32-byte private keys

The signature algorithm is always `sha256ECDSA`. No RSA certificates are defined. Key generation uses OpenSSL's `ecparam` command:

```bash
# NIST P-256
openssl ecparam -name prime256v1 -genkey -out sk_file.pem

# Brainpool P256r1
openssl ecparam -name brainpoolP256r1 -genkey -out sk_file.pem
```

Both curves produce 64-byte signatures (two 32-byte integers, r and s, DER-encoded). The Subject Key Identifier is always the SHA-1 hash of the DER-encoded public key, matching RFC 5280 conventions.

---

## 📋 Summary

- The CI root is self-signed, valid for 35 years, carrying `keyCertSign` + `cRLSign` and the `id-rspRole-ci` policy OID
- Five variants exercise different delegation depths: direct-CI (O), single SubCA (B), role SubCAs (A), and full delegation (C)
- The EUM certificate carries a critical `nameConstraints` extension restricting permitted EINs to `89049032` — exactly as a production EUM would
- SM-DP+ servers hold three separate certificates (auth, profile binding, TLS) with distinct policy OIDs — mirroring real key separation
- The eUICC certificate has effectively infinite validity (2,000,000 days) and carries the EID in its Subject DN's `serialNumber` field
- eIM certificates chain directly to the CI root and are not variant-scoped — reflecting their independent role in the SGP.32 IoT architecture
- All certificates use ECDSA over NIST P-256 or Brainpool P256r1 with SHA-256 — no RSA anywhere in the test PKI

---

<div align="center">

← Previous: [SGP.26 Overview: The GSMA RSP Test Certificate Infrastructure](/docs/articles/sgp26/37-sgp26-overview) · [🏠 Home](/)

Next: [Certificate Profiles: What Makes a Valid Test Certificate](/docs/articles/sgp26/39-sgp26-profiles) →

</div>

---

*Based on GSMA SGP.26 v3.0.2 (27 January 2025) — RSP Test Certificates Definition, Sections 3.1–3.6*
