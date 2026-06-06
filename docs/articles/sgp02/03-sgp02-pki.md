---
date: 2026-06-07
---

# M2M Certificate Hierarchy: CI, EUM, SM-DP, SM-SR, and eUICC

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > M2M Certificate Hierarchy: CI, EUM, SM-DP, SM-SR, and eUICC**

> **📚 Prerequisites:** Read the [eUICC Internals]({{ site.baseurl }}/docs/articles/sgp02/02-sgp02-euicc-internals) article to understand the ECASD and how certificates are used on-chip. The [Architecture]({{ site.baseurl }}/docs/articles/sgp02/01-sgp02-architecture) article introduced the CI and EUM roles.

> **💡 Why this matters:** The entire security of remote SIM provisioning rests on certificate-based trust. If you don't understand the certificate chain, you don't understand how the system prevents rogue servers from pushing malicious profiles to your device.

> **Key takeaways:**
> - Three-tier PKI: CI root → EUM/SM-DP/SM-SR (signed by CI) → eUICC (signed by EUM)
> - Dual certificate format: X.509 for CI/EUM, GlobalPlatform Amendment E for SM-DP/SM-SR/eUICC
> - The ECASD private key (`SK.ECASD.ECKA`) is the most sensitive secret — it never leaves the chip
> - CRL management follows an Operator informed-decision model — the eUICC doesn't manage revocation itself
> - Cryptographic baseline targets the 2030 horizon: AES-128, RSA-3072, ECC-256, SHA-256

---

## The Three-Tier PKI

SGP.02 §2.3 defines a three-tier Public Key Infrastructure. The hierarchy is:

```
         ┌──────────────────┐
         │  CI Root (self)  │  ← Self-signed, pre-loaded in ECASD
         └────────┬─────────┘
      ┌───────────┼───────────┐
      │           │           │
      ▼           ▼           ▼
 ┌─────────┐ ┌─────────┐ ┌─────────┐
 │   EUM   │ │  SM-DP  │ │  SM-SR  │  ← Signed by CI
 │  Cert   │ │  Cert   │ │  Cert   │
 └────┬────┘ └─────────┘ └─────────┘
      │
      ▼
 ┌─────────┐
 │  eUICC  │                              ← Signed by EUM
 │  Cert   │
 └─────────┘
```

**Tier 1 — CI Root Certificate**: Self-signed by the GSMA Certificate Issuer. Its public key (`PK.CI.ECDSA`) is stored in every eUICC's ECASD during manufacturing. This is the ultimate trust anchor — if you can't trace a certificate back to this key, the eUICC rejects it.

**Tier 2 — EUM, SM-DP, and SM-SR Certificates**: Signed by the CI. The EUM certificate proves a manufacturer is GSMA-accredited. The SM-DP certificate (`CERT.DP.ECDSA`) authenticates profile preparation servers. The SM-SR certificate (`CERT.SR.ECDSA`) authenticates the OTA management platform. Each contains the role-specific public key used for signature verification.

**Tier 3 — eUICC Certificate**: Signed by the EUM (not the CI). Each chip gets a unique certificate (`CERT.ECASD.ECKA`) containing its public key, EID, and a product reference that identifies the Common Criteria certification report. This is what proves "this is a genuine chip from a GSMA-accredited manufacturer."

---

## Dual Certificate Format

SGP.02 uses two different certificate formats, a consequence of the ecosystem's heritage spanning both IT infrastructure and smart card standards (SGP.02 §2.3.2):

### X.509 Format (per SGP.14)

The **CI Root Certificate** and **EUM Certificates** use **X.509** format as specified in the GSMA eUICC PKI Certificate Policy (SGP.14). This format includes standard extensions like:
- **SubjectAltName** — identifies the certificate holder
- **SubjectKeyIdentifier** — uniquely identifies the parent's signing key pair

This choice makes sense: CI and EUM certificates are processed by server-side PKI libraries that expect X.509.

### GlobalPlatform Amendment E Format

**SM-DP, SM-SR, and eUICC Certificates** use the format defined in **GlobalPlatform Card Specification Amendment E**. This is a compact, TLV-based format optimized for smart card processing. It uses:
- **Tag `42` (CA-ID)** — identifies the issuing organization
- **Tag `C9` (Authority Key Identifier)** within discretionary data (tag `73`) — identifies which parent key pair signed the certificate

The eUICC doesn't have an X.509 parser. It natively processes GlobalPlatform certificate formats, which is why SM-DP and SM-SR certificates must conform to Amendment E.

---

## Parent Certificate Identification

A subtle but critical detail: the CA-ID field alone isn't sufficient to identify which parent key pair signed a certificate. An organization might have multiple active key pairs — for rollover, different security levels, or different product lines. SGP.02 §2.3.2.2 addresses this:

- **SubjectKeyIdentifier** extension in parent certificates (CI and EUM, both X.509) uniquely identifies the signing key pair
- **AuthorityKeyIdentifier** in child certificates MUST match the parent's SubjectKeyIdentifier
  - For EUM certificates (X.509): standard Authority Key Identifier extension per RFC 5280
  - For eUICC, SM-DP, SM-SR certificates (GP Amendment E): tag `C9` within tag `73`

This matching ensures the eUICC can unambiguously verify that `CERT.DP.ECDSA` was signed by the specific CI key pair whose public key is stored in the ECASD — even if the CI operates multiple signing keys.

---

## Certificate Revocation Management

Certificate revocation in SGP.02 follows a distinctive philosophy: **the Operator makes the informed decision, not the eUICC** (SGP.02 §2.3.2.3).

### How Revocation Works

The CI issues Certificate Revocation Lists (CRLs) periodically or on event, following procedures defined in SGP.14. These CRLs list identifiers of revoked certificates — EUM, SM-DP, or SM-SR certificates that have been compromised or expired before their validity period ended.

The **Operator SHOULD** regularly retrieve the latest CRL and check whether any of its suppliers' certificates are listed. As a general recommendation:
- Don't download profiles to an eUICC whose EUM certificate was revoked
- Avoid managing profiles via an SM-DP or SM-SR whose certificate has been revoked

### The Informed-Decision Principle

However, SGP.02 contains a crucial override: **the SM-DP and SM-SR SHALL NOT refuse service solely because a certificate has been revoked**. They must obey the Operator's informed decision. Specifically:

- An SM-DP must not refuse to download a profile just because the EUM certificate is revoked
- An SM-DP must not refuse a profile management operation just because the SM-SR certificate is revoked
- An SM-SR must not refuse to register an eUICC (via ES1 or ES7) just because the EUM certificate is revoked
- An SM-SR must not refuse lifecycle operations just because the EUM certificate is revoked
- An SM-SR1 must not refuse to transfer an eUICC to SM-SR2 (SM-SR Change) just because SM-SR2's certificate is revoked

The note in the spec explains the reasoning: "The above ensures that the eUICC doesn't need to manage the revocation status of the SM-DP certificate or the SM-SR certificate that it receives."

This is a pragmatic design decision. The eUICC is a constrained device — managing CRLs on-chip would consume memory and require regular OTA updates. Instead, the Operator (a server-side entity with full PKI infrastructure) shoulders the revocation-checking responsibility. The eUICC simply verifies that certificates chain to the CI root — it doesn't check revocation status.

---

## The ECASD Key Pair and Its Role

The ECASD key pair is the most sensitive cryptographic material in the SGP.02 ecosystem. It consists of:

- **`SK.ECASD.ECKA`** — the private key, generated on-chip during manufacturing, **never leaves the eUICC**
- **`PK.ECASD.ECKA`** — the public key, embedded in the eUICC certificate and distributed as part of the EIS

This key pair serves dual purposes:

1. **Authentication**: The eUICC certificate, signed by the EUM, contains `PK.ECASD.ECKA`. When a server verifies the certificate chain (CERT.ECASD.ECKA → CERT.EUM.ECDSA → CI Root), it confirms the chip is genuine.

2. **Key Establishment**: During Scenario#3 mutual authentication (§3.1.2), the SM-DP generates an ephemeral key pair (`ePK.DP.ECKA` / `eSK.DP.ECKA`). The ECASD uses `SK.ECASD.ECKA` and the SM-DP's ephemeral public key to compute a shared secret (`ShS`). This shared secret is then used to derive the SCP03 session keys — all without `SK.ECASD.ECKA` ever being transmitted.

The algorithm is ECKA-EG (Elliptic Curve Key Agreement — ElGamal), as defined in GlobalPlatform Amendment E. It provides the cryptographic property that the SM-DP and eUICC can derive identical session keys without either revealing their private key.

---

## Algorithm and Key Length Requirements

SGP.02 §2.3.3 defines the cryptographic baseline to ensure security through the year 2030. These requirements align with recommendations from NIST (SP 800-57) and BSI (TR-02102):

| Algorithm | Minimum Key Length | Usage |
|-----------|-------------------|-------|
| Symmetric (AES) | 128 bits, 128-bit block | SCP03/SCP80 session encryption, profile package encryption |
| Asymmetric (RSA) | 3072 bits | Certificate signatures (legacy) |
| Elliptic Curve (ECC) | 256 bits | Certificate signatures (ECDSA), key agreement (ECKA-EG) |
| Hashing (signatures) | SHA-256 | Digital signatures on certificates and challenges |
| Hashing (HMAC, KDF, RNG) | SHA-256 | Key derivation, message authentication, random number generation |

In practice, modern SGP.02 deployments overwhelmingly use ECC-256 with ECDSA signatures and ECKA-EG key agreement. RSA-3072 is included for backward compatibility but is rarely seen in new deployments. AES-128 with SHA-256 provides the symmetric and hashing backbone for all session protection.

---

## Certificate Storage on the eUICC

The eUICC stores a minimal set of certificates (SGP.02 §2.3.2.1):

**Checked (verified, not stored permanently):**
- SM-SR Certificate — verified during SM-SR Change
- SM-DP Certificate — verified during Profile Download

**Stored persistently in ECASD:**
- eUICC Certificate (`CERT.ECASD.ECKA`)
- CI Root Certificate (specifically `PK.CI.ECDSA`, the public key)

The eUICC certificate is also part of the **EIS** (eUICC Information Set) stored at the SM-SR. The EIS contains additional metadata — the EID, product reference, platform version, remaining memory, and the ISD-R's SCP80/SCP81 key sets.

---

## How This Differs from Consumer eSIM PKI

The SGP.02 and SGP.22 PKIs share the same CI root concept and three-tier structure, but differ in important details:

- **SGP.02** separates SM-DP and SM-SR certificates (two distinct certificate types signed by the CI) because the roles are split. **SGP.22** has a single SM-DP+ certificate since the roles are combined.

- **SGP.02** involves the EUM certificate in the eUICC authentication chain (CERT.ECASD.ECKA → CERT.EUM.ECDSA → CI). **SGP.22** has the same chain, but SGP.22 also introduced EUM-signed eUICC certificates specifically for consumer devices.

- **SGP.02's** CRL model delegates revocation decisions to the Operator. **SGP.22** similarly doesn't require the eUICC to manage CRLs, but the consumer ecosystem's SM-DP+ typically handles revocation checking server-side.

- Certificate operational periods and key usage periods are defined in SGP.14 §8.2 for both specifications.

---

## 📋 Summary

- SGP.02 uses a three-tier PKI: CI root (self-signed, stored in ECASD) → EUM/SM-DP/SM-SR certificates (CI-signed) → eUICC certificate (EUM-signed)
- Dual format: X.509 for CI and EUM certificates (server-side processing), GlobalPlatform Amendment E for SM-DP, SM-SR, and eUICC certificates (on-chip processing)
- SubjectKeyIdentifier/AuthorityKeyIdentifier matching unambiguously identifies which parent key pair signed each certificate
- CRL management follows the Operator informed-decision model — the eUICC doesn't check revocation; the Operator does, and can choose to proceed despite revocation at its own risk
- `SK.ECASD.ECKA` is the crown jewel — a chip-unique private key that never leaves the hardware, used for both identity proof and session key derivation
- Cryptographic baseline targets 2030: ECC-256 for asymmetric, AES-128 for symmetric, SHA-256 for hashing

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

← Previous: [Inside the M2M eUICC]({{ site.baseurl }}/docs/articles/sgp02/02-sgp02-euicc-internals) | Next: [OTA Communication]({{ site.baseurl }}/docs/articles/sgp02/04-sgp02-ota) →

</div>

---

*Based on GSMA SGP.02 v4.2 §2.3 — Security Overview*


---

← Previous: [Inside the M2M eUICC: ISD-R, ISD-P, ECASD, and EID](02-sgp02-euicc-internals) | [Section Index](index) | Next: [OTA Communication: SMS, PSK-TLS, CAT_TP, and DNS](04-sgp02-ota) →
