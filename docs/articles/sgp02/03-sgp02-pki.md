---
description: "Details the SGP.02 three-tier PKI — from the GSMA CI root certificate through EUM, SM-DP, and SM-SR intermediate certificates to eUICC certificates, covering X.509, GlobalPlatform Amendment E, and CRLs."
date: 2026-06-07
---

# M2M Certificate Hierarchy: CI, EUM, SM-DP, SM-SR, and eUICC

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > M2M Certificate Hierarchy: CI, EUM, SM-DP, SM-SR, and eUICC**

If you've been following along from [the eUICC Internals article]({{ site.baseurl }}/docs/articles/sgp02/02-sgp02-euicc-internals), you already know the ECASD sits at the cryptographic center of the chip, holding certificates and a private key that never leaves the hardware. And [the Architecture piece]({{ site.baseurl }}/docs/articles/sgp02/01-sgp02-architecture) introduced the CI and EUM as the two entities that make the whole trust system work. Now we get into how those certificates actually chain together, because if you don't understand the trust model, nothing else in SGP.02 clicks.

Here's the shape of it: SGP.02 runs a three-tier PKI, with the CI root certificate at the top (self-signed, burned into every eUICC at the factory), EUM, SM-DP, and SM-SR certificates in the middle (all signed by the CI), and each chip's own eUICC certificate at the bottom (signed by its EUM (not the CI directly). Two certificate formats coexist) X.509 for the server-side pieces, and GlobalPlatform Amendment E for anything the chip itself has to parse. The CRL model follows an operator-informed-decision philosophy rather than automated on-chip revocation, and the ECASD private key (`SK.ECASD.ECKA`) is the one secret in this entire system that must never, under any circumstance, leave the hardware.

---

## The Three-Tier PKI

SGP.02 §2.3 lays out the hierarchy. Here's the chain:

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

**Tier 1, CI Root Certificate.** Self-signed by the GSMA Certificate Issuer. Its public key, `PK.CI.ECDSA` : lives in every eUICC's ECASD, written during manufacturing. This is the ultimate trust anchor. If you can't walk a certificate back to this key, the eUICC rejects it. No exceptions, no override.

**Tier 2, EUM, SM-DP, and SM-SR Certificates.** Signed by the CI. The EUM certificate tells the world "this manufacturer is GSMA-accredited." The SM-DP certificate (`CERT.DP.ECDSA`) authenticates profile preparation servers. The SM-SR certificate (`CERT.SR.ECDSA`) authenticates the OTA management platform. Each contains the role-specific public key used for signature verification downstream.

**Tier 3, eUICC Certificate.** Signed by the EUM, not the CI. Every chip gets a unique certificate (`CERT.ECASD.ECKA`) carrying its public key, its EID, and a product reference that points to the relevant Common Criteria certification report. This is what proves "this chip came from a GSMA-accredited factory."

---

## Dual Certificate Format

SGP.02 uses two certificate formats: a consequence of an ecosystem that straddles IT infrastructure and smart card standards (SGP.02 §2.3.2).

### X.509 Format (per SGP.14)

The CI Root Certificate and EUM Certificates use X.509, as specified in the GSMA eUICC PKI Certificate Policy (SGP.14). Standard extensions apply:

- **SubjectAltName** : identifies the certificate holder
- **SubjectKeyIdentifier** : uniquely identifies the parent's signing key pair

CI and EUM certificates get processed by server-side PKI libraries. Those libraries speak X.509 natively, so using anything else would just create friction.

### GlobalPlatform Amendment E Format

SM-DP, SM-SR, and eUICC Certificates use the format from GlobalPlatform Card Specification Amendment E. It's a compact, TLV-based structure optimized for smart card processing:

- **Tag `42` (CA-ID)** : identifies the issuing organization
- **Tag `C9` (Authority Key Identifier)** inside discretionary data (tag `73`) : identifies the parent key pair that signed the certificate

The eUICC doesn't carry an X.509 parser. It processes GlobalPlatform certificate formats at the hardware level. That's why SM-DP and SM-SR certificates must conform to Amendment E: the chip literally can't read them otherwise.

---

## Parent Certificate Identification

Here's a detail that trips people up: the CA-ID field alone doesn't identify which parent key pair signed a certificate. An organization might run multiple active key pairs, for rollover, different security levels, different product lines. SGP.02 §2.3.2.2 addresses this:

- The **SubjectKeyIdentifier** extension in parent certificates (CI and EUM, both X.509) uniquely identifies the signing key pair
- The **AuthorityKeyIdentifier** in child certificates must match that parent's SubjectKeyIdentifier
  - For EUM certificates (X.509): the standard Authority Key Identifier extension per RFC 5280
  - For eUICC, SM-DP, SM-SR certificates (GP Amendment E): tag `C9` inside tag `73`

This matching lets the eUICC unambiguously verify that `CERT.DP.ECDSA` was signed by the specific CI key whose public key is stored in the ECASD, even if the CI operates a dozen different signing keys.

---

## Certificate Revocation Management

Certificate revocation in SGP.02 works differently than what you'd expect from a web PKI. The eUICC doesn't check revocation at all. The Operator does, and then makes a conscious choice about what to do with that information (SGP.02 §2.3.2.3).

### How Revocation Works

The CI issues Certificate Revocation Lists periodically or on event, following procedures from SGP.14. These CRLs list revoked certificates, EUM, SM-DP, or SM-SR certificates that have been compromised or expired prematurely.

The Operator **SHOULD** retrieve the latest CRL and check whether any of its suppliers' certificates appear. The general recommendations are straightforward: don't download profiles to an eUICC whose EUM certificate got revoked, and avoid managing profiles through an SM-DP or SM-SR whose certificate has been pulled.

### The Informed-Decision Principle

But here's where SGP.02 gets interesting. The SM-DP and SM-SR **SHALL NOT refuse service solely because a certificate has been revoked**. They must follow the Operator's informed decision. Specifically:

- An SM-DP must not refuse to download a profile just because the EUM certificate is revoked
- An SM-DP must not refuse a profile management operation just because the SM-SR certificate is revoked
- An SM-SR must not refuse to register an eUICC (via ES1 or ES7) just because the EUM certificate is revoked
- An SM-SR must not refuse lifecycle operations just because the EUM certificate is revoked
- An SM-SR1 must not refuse to transfer an eUICC to SM-SR2 (SM-SR Change) just because SM-SR2's certificate is revoked

The spec's own note explains the reasoning: "The above ensures that the eUICC doesn't need to manage the revocation status of the SM-DP certificate or the SM-SR certificate that it receives."

This is a design choice born from hardware constraints. The eUICC is a constrained device, storing CRLs on-chip would burn memory and demand regular OTA updates. Instead, the Operator (a server-side entity with full PKI infrastructure) shoulders the revocation-checking burden. The eUICC's job is simpler: verify that certificates chain to the CI root and stop there. It never asks "has this certificate been revoked?"

---

## The ECASD Key Pair and Its Role

The ECASD key pair is the most sensitive cryptographic material in SGP.02. Two components:

- **`SK.ECASD.ECKA`** : the private key, generated on-chip during manufacturing. Never leaves the eUICC.
- **`PK.ECASD.ECKA`** : the public key, embedded in the eUICC certificate and distributed as part of the EIS.

This single key pair does two jobs:

**1. Authentication.** The eUICC certificate (signed by the EUM) contains `PK.ECASD.ECKA`. When a server walks the chain (CERT.ECASD.ECKA → CERT.EUM.ECDSA → CI Root) it confirms the chip is genuine.

**2. Key Establishment.** During Scenario#3 mutual authentication (§3.1.2), the SM-DP generates an ephemeral key pair (`ePK.DP.ECKA` / `eSK.DP.ECKA`). The ECASD uses `SK.ECASD.ECKA` and the SM-DP's ephemeral public key to compute a shared secret (`ShS`). That shared secret then feeds into the SCP03 session key derivation, and at no point does `SK.ECASD.ECKA` ever get transmitted.

The algorithm is ECKA-EG (Elliptic Curve Key Agreement, ElGamal), defined in GlobalPlatform Amendment E. The property that matters: the SM-DP and eUICC derive identical session keys without either side revealing its private key.

---

## Algorithm and Key Length Requirements

SGP.02 §2.3.3 sets the cryptographic baseline out to 2030, aligned with NIST SP 800-57 and BSI TR-02102 recommendations:

| Algorithm | Minimum Key Length | Usage |
|-----------|-------------------|-------|
| Symmetric (AES) | 128 bits, 128-bit block | SCP03/SCP80 session encryption, profile package encryption |
| Asymmetric (RSA) | 3072 bits | Certificate signatures (legacy) |
| Elliptic Curve (ECC) | 256 bits | Certificate signatures (ECDSA), key agreement (ECKA-EG) |
| Hashing (signatures) | SHA-256 | Digital signatures on certificates and challenges |
| Hashing (HMAC, KDF, RNG) | SHA-256 | Key derivation, message authentication, random number generation |

Most modern SGP.02 deployments run ECC-256 with ECDSA signatures and ECKA-EG key agreement. RSA-3072 hangs around for backward compatibility but you'll rarely see it in a new deployment. AES-128 paired with SHA-256 handles all the symmetric work, session encryption, HMAC, and key derivation.

---

## Certificate Storage on the eUICC

The eUICC keeps a deliberately minimal certificate store (SGP.02 §2.3.2.1):

**Verified but not stored:**
- SM-SR Certificate, verified during SM-SR Change, then discarded
- SM-DP Certificate, verified during Profile Download, then discarded

**Stored persistently in ECASD:**
- eUICC Certificate (`CERT.ECASD.ECKA`)
- CI Root Certificate (specifically `PK.CI.ECDSA`, the public key portion)

The eUICC certificate also appears in the **EIS** (eUICC Information Set) stored at the SM-SR. The EIS bundles additional metadata, EID, product reference, platform version, remaining memory, and the ISD-R's SCP80/SCP81 key sets.

---

## How This Differs from Consumer eSIM PKI

SGP.02 and SGP.22 share the same CI root concept and three-tier structure, but the details diverge:

- **SGP.02** separates SM-DP and SM-SR certificates (two distinct certificate types signed by the CI) because the roles are split. **SGP.22** uses a single SM-DP+ certificate since those roles are combined into one entity.

- **SGP.02** involves the EUM certificate in the eUICC authentication chain (CERT.ECASD.ECKA → CERT.EUM.ECDSA → CI). **SGP.22** keeps the same chain but also introduced EUM-signed eUICC certificates specifically for consumer devices.

- Both specs avoid requiring the eUICC to manage CRLs, but SGP.02 explicitly places the revocation decision in the Operator's hands. SGP.22's model leans more on the SM-DP+ handling revocation checking server-side.

- Certificate operational periods and key usage periods live in SGP.14 §8.2 for both specifications.

---

## Summary

- SGP.02 runs a three-tier PKI: CI root (self-signed, in the ECASD) → EUM/SM-DP/SM-SR certificates (CI-signed) → eUICC certificate (EUM-signed)
- Two formats coexist: X.509 for CI and EUM certificates (server-side), GlobalPlatform Amendment E for SM-DP, SM-SR, and eUICC certificates (on-chip)
- SubjectKeyIdentifier/AuthorityKeyIdentifier matching tells the eUICC exactly which parent key signed a given certificate, critical when an organization runs multiple signing keys
- CRL management follows the operator-informed-decision model: the eUICC doesn't check revocation, the Operator does, and can choose to proceed despite a revoked certificate
- `SK.ECASD.ECKA` is the crown jewel: a chip-unique private key that handles both identity proof and session key derivation without ever leaving the hardware
- Cryptographic baseline targets 2030: ECC-256 for asymmetric, AES-128 for symmetric, SHA-256 for hashing

---

<div align="center">

<a href="{{ site.baseurl }}/">🏠 Home</a>

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp02/02-sgp02-euicc-internals">Inside the M2M eUICC</a> | Next: <a href="{{ site.baseurl }}/docs/articles/sgp02/04-sgp02-ota">OTA Communication</a> →

</div>

---

*Based on GSMA SGP.02 v4.2 §2.3, Security Overview*


---

← Previous: [Inside the M2M eUICC: ISD-R, ISD-P, ECASD, and EID](02-sgp02-euicc-internals) | [Section Index](index) | Next: [OTA Communication: SMS, PSK-TLS, CAT_TP, and DNS](04-sgp02-ota) →
