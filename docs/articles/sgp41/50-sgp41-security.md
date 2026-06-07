---
title: "IFPP Security: Factory Trust Models and Certificate Chains"
description: "Explains SGP.41's factory trust model: one-time keys, perfect forward secrecy, SAS-certified HSM protection, and pre-encrypted BPPs that treat the factory as a courier rather than a custodian of profile secrets."
date: 2026-06-06
---

# IFPP Security: Factory Trust Models and Certificate Chains

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.41 IFPP]({{ site.baseurl }}/docs/articles/sgp41/) > IFPP Security: Factory Trust Models and Certificate Chains**

> **💡 Why this matters:** Factory floors are untrusted environments. The Device Manufacturer and FPA handle profile packages but must never see them in plaintext. One-time keys, forward secrecy, and pre-encryption create a security model where the factory is a courier, not a custodian: the profile's confidentiality and integrity are preserved end-to-end from the SAS-certified SM-DPf to the eUICC, regardless of what happens on the production line.

> **Key takeaways:**
> - SGP.41 implements **defence in depth** for the factory: the Device Manufacturer never has access to clear-text private/secret keys used for binding (GENS10), and clear-text profiles only exist inside the eUICC (GENS09)
> - **One-time keys** are the cryptographic linchpin: randomly generated (GENS07), single-use (GENS08), SAS-UP generated and loaded (GENS14), and tied to a specific eUICC (GENS12)
> - **Perfect Forward Secrecy (PFS)** is required for every profile binding (GENS06) : compromise of the SM-DPf's long-term key does not expose previously bound profiles
> - The SM-DPf's private key MUST be protected in an SAS-certified HSM (GENS05); the EUM MUST be SAS-accredited (EUMS01); the SM-DPf MUST be SAS-accredited (DPFS01)
> - **Two explicit security options** reduce factory burden: Option 1 allows no SAS accreditation for the Device Manufacturer (GENS01); Option 2 allows no HSM at the Device Manufacturer (GENS02)
> - Anti-cloning is built in: a profile can only be loaded to one eUICC (GENS04), enforced by the one-time key binding
> - FPA Services are only available during the Device Production Process (GENS13) : they cannot be invoked in the field

SGP.41's security model starts from a blunt premise: **the factory is not trusted with profile secrets.** Every security decision flows from this premise. The Device Manufacturer and FPA handle Bound Profile Packages but can never decrypt them. The SM-DPf does all cryptographic operations in a SAS-certified HSM before the profile reaches the factory. The result is a model where even a fully compromised factory cannot extract profile keys or clone profiles.

---

## The Security Architecture

### End-to-End Protection Chain

```
SM-DPf HSM                     Factory (untrusted)                eUICC
─────────                      ──────────────────                ─────
[Profile]                       [BPP in transit]                 [Profile]
   │                                 │                              ▲
   ├─ encrypt to eUICC's            ├─ push through FPA            │
   │  one-time public key           │  (cannot decrypt)            │
   │                                 │                              │
   ├─ sign with SM-DPf              ├─ store temporarily           ├─ decrypt with
   │  private key                   │  (cannot decrypt)            │  one-time private key
   │                                 │                              │
   └─ include SM-DPf cert           └─ load onto eUICC             ├─ verify SM-DPf sig
      chain                                                         │
                                                                    └─ verify cert chain
```

The profile exists in plaintext at exactly two points: inside the SM-DPf's SAS-certified HSM during generation and binding, and inside the eUICC after decryption and installation. At every point in between: in transit over Esbpp, in storage at the Device Manufacturer, during Esfac transfer, during ES10f forwarding: it is a cryptographically bound and encrypted BPP that no factory entity can read.

---

## One-Time Keys: The Cryptographic Anchor

One-time keys are the foundation of IFPP security. Here's how they work:

### Key Generation and Loading

- Generated during the Two-Step Personalisation Process (GSMA FS.18) : before IFPP begins
- **Must be randomly generated** (GENS07)
- **Must be created and loaded only in a SAS-UP environment** (GENS14)
- The private key stays in the eUICC, never leaves
- The public key is exported via Esed1 or Esed2 to the SM-DPf

### Key Usage

- **Each one-time key binds exactly one profile** (GENS08)
- After use, the key is consumed: it cannot be used again
- The Device Manufacturer **SHOULD delete all remaining unused one-time keys** before the end of the Device Production Process (DMF03)
- The eUICC provides a secure mechanism for the Device Manufacturer to delete all unused one-time keys (EUICCF03)

### Why One-Time Keys?

One-time keys solve several problems simultaneously:

1. **Anti-cloning**: A BPP encrypted to eUICC-A's one-time key cannot be installed on eUICC-B: only eUICC-A has the corresponding private key (GENS04).

2. **Offline binding**: The SM-DPf can bind a profile to an eUICC without any real-time communication. It only needs the public key, which it receives in advance.

3. **No long-term correlation**: Because each key is used once, an attacker who compromises one BPP learns nothing about other BPPs bound to the same eUICC.

4. **Factory-side simplicity**: The Device Manufacturer never touches private keys: it only passes through encrypted BPPs.

---

## Certificate Chains and Trust

### The Certificate Hierarchy

IFPP reuses the PKI infrastructure from SGP.21/SGP.31:

- **eSIM CA** (Certificate Authority): Issues certificates to EUMs and SM-DPfs via the `Esci` interface (out of scope for SGP.41)
- **EUM Certificate**: Issued to the eUICC Manufacturer, used to sign eUICC certificates
- **eUICC Certificate**: Unique per eUICC, stored in ECASD during manufacturing, used to authenticate the eUICC to the SM-DPf
- **SM-DPf Certificate**: Used for profile binding and signing, validated by the eUICC during installation

### Certificate Validation During Profile Installation

When the eUICC receives a BPP (step 10 of the IFPP flow), it verifies:

1. The SM-DPf certificate chain (included with the BPP) chains back to a trusted eSIM CA root
2. The BPP's cryptographic signature matches the SM-DPf's certificate
3. The BPP is encrypted to the eUICC's own one-time public key (verified by successful decryption with the private key)

### Certificate Revocation

The SM-DPf retrieves certificate revocation status from the eSIM CA via the `Esci` interface. The eUICC is expected to have mechanisms for certificate validation consistent with SGP.21/SGP.25 requirements: though CRL loading during IFPP itself is not detailed in the v1.0 specification.

---

## What the Factory Does NOT Need

SGP.41 explicitly defines two options that reduce the security burden on the manufacturing environment:

### Option 1: No SAS Accreditation for the Factory (GENS01)

> *"There SHALL be an option where Profile provisioning related security accreditation (e.g., GSMA SAS) is not required for the Device Manufacturer."*

This is a critical design choice. Traditional eSIM profile handling (SM-DP+ operations) requires SAS accreditation. By shifting all security-sensitive operations to the SM-DPf (which MUST be SAS-accredited: DPFS01), SGP.41 lets factories operate without SAS certification. This is explicitly called out in the IoT use case (Annex A.2): *"CheapDevice does not want its production facility constrained by strong additional security requirements, e.g., get a SAS certification for its production facility."*

### Option 2: No HSM at the Factory (GENS02)

> *"There SHALL be an option where an HSM at the Device Manufacturer is not required."*

The Device Manufacturer never holds plaintext profile keys or performs cryptographic operations on profile material. An HSM would protect nothing of value. SGP.41 eliminates this cost and complexity.

---

## GENS09 and GENS10: The Hard Security Boundaries

Two requirements define the absolute security boundaries:

**GENS09**: *"At the Device Manufacturer, the clear-text Profile Package SHALL only exist inside the eUICC."*

The Device Manufacturer handles BPPs (encrypted), stores BPPs (encrypted), transports BPPs (encrypted), and pushes BPPs through the FPA (encrypted). At no point does the Device Manufacturer's infrastructure see or touch a plaintext profile.

**GENS10**: *"The Device Manufacturer SHALL never have access to the clear-text private/secret keys used for binding of Profile Packages."*

The one-time private keys stay in the eUICC. The SM-DPf's private key stays in its SAS-certified HSM. The Device Manufacturer may handle public keys and eUICC certificates: but never private key material.

---

## Perfect Forward Secrecy (GENS06)

SGP.41 requires that each profile binding incorporate Perfect Forward Secrecy: *"Each Profile binding SHALL incorporate Perfect Forward Secrecy (PFS)."*

This means:
- Even if the SM-DPf's long-term private key is compromised in the future, previously bound BPPs cannot be decrypted
- Each binding uses ephemeral key material that is discarded after use
- Combined with one-time keys, this creates a "double forward secrecy" : neither the SM-DPf's long-term key nor one eUICC's one-time key can compromise other bindings

---

## FPA Service Gating (GENS13)

A subtle but important security control: the FPA Services on the eUICC are only available during the Device Production Process:

> *"The FPA Services SHALL only be available during the Device Production Process."*

How this is enforced is Device Manufacturer and/or EUM specific (the spec notes this is implementation-dependent). Once the device leaves the factory, the FPA Services are locked: preventing any post-production attempt to use the factory provisioning path for malicious profile loading.

Additionally, the eUICC gates LPA/IPA Services: *"The eUICC SHALL only authorise the use of the LPA Services... or the IPA Services... if there is no One-time Key"* (EUICCF04). This means while one-time keys remain on the eUICC (indicating the factory phase is still active), the field-side profile management interfaces are blocked: and vice versa.

---

## Threat Model (Annex B)

SGP.41 Annex B identifies four categories of threats:

### Malicious or Compromised IFPP Entity

- **MCE01**: A malicious IFPP entity uses privileged access to push unsolicited profiles → Mitigated by one-time key binding: only profiles bound to the correct eUICC key will install
- **MCE02**: Tampering with Esbpp communications or eUICC data → Mitigated by eUICC certificate verification and BPP integrity checks

### Cryptographic Related Risks

- Key loss or theft (INO1), inability to revoke certificates (INO2), accidental revocation causing DoS (INO5), and temporary/generic key material creating single points of failure (INO6)
- These are standard PKI risks managed through the existing eSIM CA infrastructure and SAS requirements

---

## 📋 Summary

- Security is built on the premise that the factory is untrusted: clear-text profiles exist only in the SM-DPf HSM and inside the eUICC
- One-time keys provide anti-cloning, offline binding capability, and forward secrecy: each key binds exactly one profile to exactly one eUICC
- Perfect Forward Secrecy (GENS06) protects past bindings even if the SM-DPf's long-term key is compromised
- Two explicit factory-side security reductions: no SAS accreditation required (GENS01), no HSM required (GENS02)
- FPA Services are gated to the Device Production Process only; LPA/IPA Services are blocked while factory one-time keys exist
- The SM-DPf and EUM MUST be SAS-accredited; the Device Manufacturer may operate without SAS (Option 1)

---

<div align="center">

← Previous: [IFPP Flow: Manufacturing Step to Configuration Step]({{ site.baseurl }}/docs/articles/sgp41/49-sgp41-flow) · [🏠 Home]({{ site.baseurl }}/)

Next: [IFPP in Practice: PC OEMs, Automotive, and IoT Manufacturing]({{ site.baseurl }}/docs/articles/sgp41/51-sgp41-practice) →

</div>

---

*Based on GSMA SGP.41 v1.0 (28 February 2025) : eSIM In-Factory Profile Provisioning Architecture and Requirements, Sections 4.2 and Annex B*


---

← Previous: [IFPP Flow: Manufacturing Step to Configuration Step](49-sgp41-flow) | [Section Index](index) | Next: [IFPP in Practice: PC OEMs, Automotive, and IoT Manufacturing](51-sgp41-practice) →
