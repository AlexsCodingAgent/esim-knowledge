---
title: "Using Test Certificates: Developer Setup and Integration"
date: 2026-06-06
---

# Using Test Certificates: Developer Setup and Integration

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.26 Test Certificates]({{ site.baseurl }}/docs/articles/sgp26/) > Using Test Certificates: Developer Setup and Integration**

> **💡 Why this matters:** Having a specification for test certificates is one thing: getting them onto actual test hardware is another. This article covers the practical path from downloading the SGP.26 ZIP package to having a test eUICC that trusts your test SM-DP+, including OpenSSL commands, certificate provisioning, and the common mistakes that waste days in the lab.

> **Key takeaways:**
> - The SGP.26 ZIP package (`SGP.26_v3.x-YYYYMMDD_Files.ZIP`) contains all keys (PEM), certificates (DER), CRLs, and OpenSSL configuration files: it's the single source of truth for the test PKI
> - Key generation uses OpenSSL 1.1.0e's `ecparam` command for NIST P-256 and Brainpool P256r1 curves; CSRs use `openssl req -new -nodes -sha256 -config <cnf>` with template configuration files from Annex F
> - Installing test certificates on an eUICC test SIM requires provisioning CERT.CI.SIG (or equivalent self-signed CI), CERT.EUM.SIG, and CERT.EUICC.SIG: along with the eUICC's private key: into the ECASD
> - Test SM-DP+ configuration needs all three SM-DP+ certificates (auth, profile binding, TLS) plus their private keys, and must serve the test CRL at the URLs specified in the certificates
> - Self-signed test CIs (Annex C) allow RSP actors to generate their own test roots and publish them via GSMA's registry at `https://www.gsma.com/esim/gsma-root-ci/`
> - Common pitfalls: forgetting to convert DER to PEM for OpenSSL signing, using the wrong variant's certificates for your test scenario, CRL distribution point URL mismatches, and certificate expiry during long-running test suites

* TOC
{:toc}

SGP.26 is not just a reference document: it ships with an actual file package containing every key, certificate, and configuration file needed to stand up a complete test RSP environment. This article covers the end-to-end developer workflow.

---

## Obtaining the SGP.26 Package

The test certificates are distributed as a ZIP file named `SGP.26_v3.x[.y]-YYYYMMDD_Files.ZIP`, where:

- `3.x` is the minor version of the SGP.26 document
- `YYYYMMDD` is the update date
- `[.y]` is an optional sub-version for bug-fix releases

The package is updated at least every two years to prevent certificate expiry. The latest version should always be used. For SGP.26 v3.0.2 (January 2025), the package contains:

```
SK_CI_SIG_NIST.pem          # CI private key (NIST P-256)
SK_CI_SIG_BRP.pem            # CI private key (Brainpool P256r1)
CERT_CI_SIG_NIST.der         # CI certificate (DER)
CERT_CI_SIG_BRP.der
SK_EUM_SIG_NIST.pem          # EUM private key
CERT_EUM_SIG_NIST.der
SK_EUICC_SIG_NIST.pem        # eUICC private key
CERT_EUICC_SIG_NIST.der
SK_S_SM_DP1auth_SIG_NIST.pem # SM-DP+ auth private key
CERT_S_SM_DP1auth_SIG_NIST.der
SK_S_SM_DP1pb_SIG_NIST.pem   # SM-DP+ profile binding private key
CERT_S_SM_DP1pb_SIG_NIST.der
SK_S_SM_DP1_TLS_NIST.pem     # SM-DP+ TLS private key
CERT_S_SM_DP1_TLS_NIST.der
# ... plus CRLs, .cnf configuration files, and BRP equivalents
```

All private keys are unencrypted PEM files: deliberately, since these are test-only keys. In a production context, private keys would be in HSMs and never exported.

---

## The OpenSSL Toolchain

SGP.26 specifies OpenSSL 1.1.0e as the reference toolchain. The version matters: later OpenSSL versions (3.x) changed default behaviour for some extensions and may produce certificates that differ in subtle ASN.1 encoding. Tests should use the exact version specified, or at minimum verify that the generated certificates match the reference DER files byte-for-byte.

### Step 1: Generate Private Keys

```bash
# NIST P-256
openssl ecparam -name prime256v1 -genkey -out sk_euicc_nist.pem

# Brainpool P256r1
openssl ecparam -name brainpoolP256r1 -genkey -out sk_euicc_brp.pem
```

### Step 2: Generate the Public Key

```bash
openssl ec -in sk_euicc_nist.pem -pubout -out pk_euicc_nist.pem
```

### Step 3: Generate a Certificate Signing Request (CSR)

CSRs use configuration files defined in Annex F of SGP.26. For the eUICC:

```bash
openssl req -new -nodes -sha256 \
  -config EUICC-csr.cnf \
  -key sk_euicc_nist.pem \
  -out euicc_nist.csr
```

The `EUICC-csr.cnf` file specifies the subject DN:
```
prompt = no
distinguished_name = dn-param
[dn-param]
cn = Test eUICC
serialNumber = 89049032123451234512345678901235
o = RSPTEST
c = ES
```

### Step 4: Sign the Certificate

```bash
# Convert CA cert from DER to PEM if needed
openssl x509 -inform der -in CERT_EUM_SIG_NIST.der -out CERT_EUM_SIG_NIST.pem

# Sign the CSR
openssl x509 -req -in euicc_nist.csr \
  -CA CERT_EUM_SIG_NIST.pem \
  -CAkey SK_EUM_SIG_NIST.pem \
  -set_serial 0x020000000000000001 \
  -days 2000000 \
  -extfile EUICC-ext.cnf \
  -out CERT_EUICC_SIG_NIST.pem

# Convert to DER
openssl x509 -in CERT_EUICC_SIG_NIST.pem -outform DER -out CERT_EUICC_SIG_NIST.der
```

### Step 5: Verify the Certificate

```bash
openssl x509 -in CERT_EUICC_SIG_NIST.der -inform der -text -noout
```

This displays the full certificate content: verify that all extensions match the expected profile.

### CI Root Certificate Generation (Self-Signed)

The CI root is self-signed, using `openssl req -x509`:

```bash
openssl req -config CI-csr.cnf \
  -key SK_CI_SIG_NIST.pem \
  -new -x509 \
  -days 12783 \
  -sha256 \
  -set_serial 0x00B874F3ABFA6C44D3 \
  -extensions extend \
  -out CERT_CI_SIG_NIST.pem

openssl x509 -in CERT_CI_SIG_NIST.pem -outform DER -out CERT_CI_SIG_NIST.der
```

---

## Installing Certificates on Test eUICC SIMs

A test eUICC needs three certificates in its ECASD (eUICC Controlling Authority Security Domain):

| Certificate | Purpose | File |
|---|---|---|
| **CI Root** | Trust anchor for SM-DP+ validation | `CERT_CI_SIG_<curve>.der` |
| **EUM Certificate** | Attests that the EUM authorized this eUICC | `CERT_EUM_SIG_<curve>.der` |
| **eUICC Certificate** | The eUICC's own identity | `CERT_EUICC_SIG_<curve>.der` |
| **eUICC Private Key** | Used to sign PIRs and authenticate | `SK_EUICC_SIG_<curve>.pem` |

The exact provisioning mechanism depends on the eUICC vendor. Common approaches:

- **GSMA SAS-UP certified test SIMs**: Many eUICC vendors offer pre-provisioned test SIMs loaded with SGP.26 certificates. These are profile-ready out of the box.
- **GlobalPlatform-compliant personalization**: Use the vendor's personalization tools to load certificates during the manufacturing equivalent phase.
- **SCP03t script loading**: Some test eUICCs support certificate injection via SCP03t secure channel scripts: query the vendor's test documentation.
- **RSP Test Platform provisioning**: Some eUICC test platforms (e.g., COMPRION, FIME) support loading SGP.26 certificates through their management interfaces.

The CI root public key (or its Subject Key Identifier) must also be configured in `euiccCiPKIdListForVerification` or the equivalent list that the eUICC uses to determine which CIs it trusts. For SGP.23 testing, this list is typically set to include the SGP.26 test CI.

---

## Configuring a Test SM-DP+

A test SM-DP+ server needs three certificates per curve plus their private keys:

| Certificate | Purpose | Configure in |
|---|---|---|
| **CERT.DPauth.SIG** | ES9+ mutual authentication | SM-DP+ auth service |
| **CERT.DPpb.SIG** | ES8+ profile binding signature | SM-DP+ profile delivery service |
| **CERT.DP.TLS** | ES9+ HTTPS TLS | Web server / reverse proxy |

Additionally:

1. **Serve the CRL**: The SM-DP+ must make the relevant CRL available at the URL specified in the certificates' `crlDistributionPoints` extension. For Variant O, this is:
   - `http://ci.test.example.com/CRL-1.crl`
   - `http://ci.test.example.com/CRL-2.crl`

   These are test-only URLs on `example.com`. In a local test setup, configure DNS or `/etc/hosts` to point `ci.test.example.com` to your CRL server. The CRL files are included in the SGP.26 ZIP package.

2. **Configure the CI chain**: The SM-DP+ must present the full certificate chain during TLS handshakes: end-entity → SubCA (if applicable) → CI root.

3. **Host the Test Profile**: Per Annex D, the test SM-DP+ must provide a URL to an application that allows testers to trigger profile downloads. This is typically a web interface where the tester submits an EID, Confirmation Code (if required), and receives a Matching ID.

4. **Support at least one download mechanism**: Per SGP.22, options include:
   - Default SM-DP+ address in the eUICC
   - SM-DS event registration and discovery
   - Activation Code (QR code containing SM-DP+ address and Matching ID)

---

## Test SM-DS Configuration

A test SM-DS server needs:

| Certificate | Purpose |
|---|---|
| **CERT.DSauth.SIG** | Signing discovery responses |
| **CERT.DS.TLS** | HTTPS TLS for event registration and discovery |

The SM-DS must serve its CRL at the URLs in its certificates' `crlDistributionPoints`. For Variant A and C, this uses SM-DS-specific URLs like `http://smds.test.example.com/CRL.crl`.

---

## Self-Signed Test CIs: Annex C

Not everyone needs to use the centralized GSMA test CI. Annex C of SGP.26 describes how RSP actors can generate their own self-signed test CI certificates:

1. **Generate a key pair** for NIST P-256 or Brainpool P256r1 using `openssl ecparam`
2. **Create a self-signed CI certificate** using `openssl req -x509` with the CI configuration template
3. **Sign downstream certificates** using the self-signed CI's private key: EUM certs, eUICC certs, SM-DP+ certs, SM-DS certs
4. **Publish the self-signed CI** via GSMA's test certificate registry

The recommended minimum profile for a self-signed test CI (Table 50):

| Field | Value |
|---|---|
| **version** | V3 (2) |
| **serialNumber** | Vendor-specific |
| **signature** | sha256ECDSA |
| **Issuer** | Same as Subject |
| **Validity** | Vendor-specific |
| **keyUsage** | Certificate Signing, CRL Signing |
| **certificatePolicies** | `2.23.146.1.2.1.0` (id-rspRole-ci) |
| **basicConstraints** | CA = true |

This allows, for example, an SM-DP+ vendor to set up a complete test environment with their own test root and distribute compatible test eUICCs to their customers: without depending on the GSMA test CI.

---

## Publishing Test Certificates: Annex D

GSMA maintains a public registry at `https://www.gsma.com/esim/gsma-root-ci/` that lists:

- Providers that support the test root certificate operated by GSMA CI
- Alternative self-signed root test certificate issuers

To register, RSP actors submit to `testCICertificates@gsma.com` using the Test Certificate Submission Form:

**For GSMA CI test root support (D.1):**
- Company name
- Confirmation of Test Profile support per SGP.22
- List of test root certificates used (as EUM, SM-DP+ provider, and/or SM-DS provider), each identified by Subject Key Identifier
- URL to the profile download trigger application

**For self-signed root test CI (D.2):**
- Company name + Test Profile support confirmation
- URL hosting the self-signed test CI certificate in PEM format
- Optionally: URL of the test CI private key, signed client EUM/SM-DP+ certificates
- URL to the profile download trigger application
- Information is published with publication date and certificate expiry date

---

## Common Pitfalls

### 1. DER vs PEM Confusion

The reference certificates in the ZIP package are in DER format. OpenSSL's signing commands (`openssl x509 -req -CA`) expect the CA certificate in PEM format. Always convert:

```bash
openssl x509 -inform der -in CERT_CI_SIG_NIST.der -out CERT_CI_SIG_NIST.pem
```

### 2. Variant Mismatch

Not all certificates work with all variants. An eUICC provisioned with Variant O certificates (trusting the Variant O CI root directly) will reject a Variant A SM-DP+ certificate that chains through a DP SubCA the eUICC doesn't know about. Ensure the entire chain: from the eUICC's CI trust anchor to the SM-DP+'s leaf certificate: uses the same variant.

### 3. CRL Distribution Point Unreachable

The eUICC may attempt to fetch CRLs during certificate validation. If `ci.test.example.com` doesn't resolve in your test network, the validation will fail. Options:

- Configure `/etc/hosts` or local DNS to resolve the test URLs
- Configure the eUICC to skip CRL checking (if supported and appropriate for the test scenario)
- Serve the CRL from a local HTTP server with the correct path

### 4. Certificate Expiry in Long-Running Tests

TLS certificates expire after 398 days. SM-DP+ auth/pb certificates expire after 1,095 days (3 years). For CI/CD pipelines that run continuously, check certificate expiry dates and plan for rotation. The SGP.26 ZIP package is updated at least every two years: download the latest version.

### 5. Using Production Crypto on Test Hardware

Some test SIMs ship with a production CI trust anchor pre-provisioned. If you try to use SGP.26 test certificates against a production CI root, signature verification will fail because the public key doesn't match. Always provision the test CI root before testing.

### 6. Brainpool vs NIST Curve Confusion

The eUICC and SM-DP+ must agree on which curve to use. If the eUICC only supports NIST P-256 but the SM-DP+ presents a Brainpool certificate chain, the eUICC returns `unsupportedCurve(3)`. Check which curves your test eUICC supports (via the Optional Features Table in SGP.23-1) and select the matching certificate set.

### 7. Certificate Policy Mismatch

The eUICC checks the `certificatePolicies` extension. If an SM-DP+ presents a TLS certificate for authentication (wrong policy OID), the eUICC must reject it. Always use the correct certificate type for each purpose:
- Auth operations → CERT.DPauth.SIG
- Profile binding → CERT.DPpb.SIG
- TLS connections → CERT.DP.TLS

---

## 📋 Summary

- The SGP.26 ZIP package is the single source of truth: download the latest version at least every two years to avoid expiry
- The OpenSSL toolchain generates keys with `ecparam`, CSRs with `req`, and certificates with `x509 -req` : always use `-sha256` and the correct configuration files from Annex F
- Installing test certificates on an eUICC requires four elements: CI root, EUM cert, eUICC cert, and eUICC private key: plus configuring the eUICC's trust list
- Test SM-DP+ configuration needs all three certificate types (auth, pb, TLS) deployed to the correct services, plus a CRL distribution endpoint
- Self-signed test CIs (Annex C) let vendors create independent test PKIs and publish them via GSMA's test certificate registry
- Avoid the seven common pitfalls: DER/PEM confusion, variant mismatch, unreachable CRL DPs, expiry, production trust anchors, curve mismatch, and policy mismatch
- The GSMA public registry at `https://www.gsma.com/esim/gsma-root-ci/` lists test SM-DP+ servers that are publicly accessible for interoperability testing

---

<div align="center">

← Previous: [Certificate Profiles: What Makes a Valid Test Certificate]({{ site.baseurl }}/docs/articles/sgp26/39-sgp26-profiles) · [🏠 Home]({{ site.baseurl }}/)

Next: [CRL and Certificate Management in the Test Ecosystem]({{ site.baseurl }}/docs/articles/sgp26/41-sgp26-crl) →

</div>

---

*Based on GSMA SGP.26 v3.0.2 (27 January 2025) : RSP Test Certificates Definition, Sections 2, Annexes A, B, C, D, and F*


---

← Previous: [Certificate Profiles: What Makes a Valid Test Certificate](39-sgp26-profiles) | [Section Index](index) | Next: [CRL and Certificate Management in the Test Ecosystem](41-sgp26-crl) →
