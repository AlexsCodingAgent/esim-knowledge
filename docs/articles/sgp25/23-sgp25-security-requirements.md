---
title: "eUICC Security Functional Requirements"
date: 2026-06-05
---

# eUICC Security Functional Requirements

> **💡 Why this matters:** The heart of any Protection Profile is its Security Functional Requirements (SFRs). These are the precise, testable statements that define what the eUICC must *do* to be considered secure — from authenticating remote actors and isolating Profiles to protecting cryptographic keys and enforcing policy rules. Understanding the SFRs reveals exactly what security properties a certified eUICC guarantees.

> **Key takeaways:**
> - SGP.25 defines four Security Function Policies (SFPs): Secure Channel Protocol, Platform Services, ISD-R Content Access Control, and ECASD Access Control
> - Identification & Authentication SFRs (FIA_*) ensure every remote and local actor is identified and authenticated before accessing TOE services
> - Communication SFRs (FTP_ITC.1, FDP_UCT.1, FDP_UIT.1) protect all data transmitted through ES6, ES8+, and other interfaces
> - Security Domain SFRs (FDP_ACC.1, FDP_ACF.1) enforce strict isolation between ISD-R, ISD-P, and ECASD based on AID and ISD-P state attributes
> - Security management SFRs (FMT_*) control who may modify security attributes like Profile Policy Rules, keys, and the Rules Authorisation Table
> - The TOE scope explicitly excludes MNO-SD, Profiles, and the Runtime Environment from the PP's SFR coverage

The Security Functional Requirements in SGP.25 are drawn from Common Criteria Part 2, with refinements (adding detail), selections (choosing from CC options), assignments (specifying parameter values), and iterations (repeating components for different contexts). This article unpacks the SFR structure and explains what each group of requirements means in practice.

---

## Security Function Policies (SFPs)

SGP.25 defines four SFPs that collectively govern all access to and protection of eUICC assets:

### 1. Secure Channel Protocol Information Flow Control SFP

This policy governs communication between remote actors (SM-DP+, MNO OTA Platform) and their on-card counterparts (ISD-R, ISD-P, MNO-SD). The TOE must support three secure channel protocols:

| Protocol | Used By | Interface |
|----------|---------|-----------|
| **SCP-SGP22** | SM-DP+ ↔ ISD-R / ISD-P | ES8+ |
| **SCP80** | MNO OTA Platform ↔ MNO-SD | ES6 |
| **SCP81** | MNO OTA Platform ↔ MNO-SD (HTTP-based) | ES6 |

These secure channels are built upon security attributes — keysets (D.MNO_KEYS, D.SECRETS) — that bind user identities to the appropriate subjects on the eUICC.

### 2. Platform Services Information Flow Control SFP

Controls access by the Application Layer (ISD-R, ISD-P, ECASD) to Platform services (Profile Package Interpreter, Profile Rules Enforcer, Telecom Framework). This ensures that:

- Profile packages are only interpreted through the authorised PPI interface
- Profile Policy Rules are only enforced through the PRE
- Network authentication algorithms in the Telecom Framework are only accessible to the currently enabled Profile's NAA

### 3. ISD-R Content Access Control SFP

Governs which operations may be performed on the ISD-R and its data. The ISD-R is the single most privileged component on the eUICC — it creates ISD-Ps, manages their life-cycle, and accesses ECASD functions. This SFP ensures only authenticated remote actors (via secure channels) can trigger ISD-R operations.

### 4. ECASD Access Control SFP

The ECASD holds the eUICC's most sensitive assets — private keys, certificates, eSIM CA public keys, and secrets. This SFP restricts local access to ECASD functions to:

- **S.ECASD itself** — for self-contained cryptographic operations
- **S.ISD-R** — for key establishment and eUICC authentication operations, based on AID

Additional subjects may be granted local access in the Security Target for optional key renewal functionality.

---

## Identification and Authentication (FIA_*)

Every actor interacting with the TOE must be identified and authenticated before any other SFR-enforcing actions occur.

### Remote Actor Authentication

Remote users (U.SM-DP+, U.MNO-OTA, U.EIM) are authenticated via the FIA hierarchy:

| SFR | Purpose |
|-----|---------|
| **FIA_UID.1/EXT** | Timing of identification — remote users must be identified before any other TSF-mediated action except those listed in the allowance clause |
| **FIA_UAU.1/EXT** | Timing of authentication — authentication must succeed before any TSF-mediated action beyond identification |
| **FIA_USB.1/EXT** | User-subject binding — associates remote user security attributes (CERT.DPauth.ECDSA, CERT.DPpb.ECDSA, SM-DP+ OID, MNO OID) with corresponding subjects (S.ISD-R, S.ISD-P, SO.ISD-P) |
| **FIA_UAU.4/EXT** | Single-use authentication mechanisms — prevents reuse of authentication data related to one-time keys (otSK/otPK) and shared secrets |
| **FIA_API.1** | Authentication Proof of Identity — the TOE provides a cryptographic authentication mechanism to prove the eUICC's identity to remote actors |

### Local Actor Authentication

The only local user is the MNO-SD (an on-card application within a Profile, not part of the TOE):

| SFR | Purpose |
|-----|---------|
| **FIA_UID.1/MNO-SD** | MNO-SD must be identified before any TSF-mediated action |
| **FIA_USB.1/MNO-SD** | Associates MNO-SD security attributes (MNO OID, keysets) with SO.ISD-P |

### Security Attribute Definitions

FIA_ATD.1/Base defines the full list of security attributes maintained by the TSF for each user, including: AID, ISD-P state, PPR, Reference Enterprise Rule, Enterprise Rule, RAT, keysets/session keys, certificates (CERT.DPauth.ECDSA, CERT.DPpb.ECDSA), and OIDs.

---

## Communication Protection

The Secure Channel Protocol SFP is enforced through interconnected SFRs that protect data in transit:

```text
FTP_ITC.1/SCP  ──► Trusted channel establishment (ES8+, ES6)
FDP_IFC.1/SCP  ──► Information flow control policy definition
FDP_IFF.1/SCP  ──► Simple security attribute-based flow rules
FDP_UCT.1/SCP  ──► Confidentiality of transmitted user data
FDP_UIT.1/SCP  ──► Integrity of transmitted user data
FDP_ITC.2/SCP  ──► Import of user data with security attributes
FPT_TDC.1/SCP  ──► Consistent interpretation of TSF data between TOE and external entities
```

Key management for these channels is handled by:

- **FCS_CKM.1/SCP-SM** — Cryptographic key generation for SM-DP+ ↔ TOE channels
- **FCS_CKM.2/SCP-MNO** — Cryptographic key distribution for MNO-SD keys (D.MNO_KEYS)
- **FCS_CKM.6/SCP-SM and FCS_CKM.6/SCP-MNO** — Cryptographic key destruction

---

## Security Domain Isolation

The access control SFRs enforce the strict separation between Security Domains:

### ISD-R Access Control
```
FDP_ACC.1/ISDR  ──► Defines which subjects/objects are covered
FDP_ACF.1/ISDR  ──► Defines the access control rules
```
Operations governed by ISD-R state include: profile download and installation, ISD-P creation/deletion, ISD-P state transitions (INSTALLED → SELECTABLE → ENABLED → DISABLED), PPR enforcement, and Enterprise Rule evaluation.

### ECASD Access Control
```
FDP_ACC.1/ECASD ──► Defines ECASD subjects and objects
FDP_ACF.1/ECASD ──► Defines access rules based on AID
```
ECASD operations include: key generation, shared secret computation, signature creation, certificate verification, and EID retrieval.

### ISD-P Isolation

The ISD-P structure ensures that:
1. Each ISD-P hosts exactly one unique Profile
2. Profile components have no visibility of or access to components outside their ISD-P
3. ISD-Ps have no visibility of or access to other ISD-Ps
4. Profile deletion removes the containing ISD-P and all Profile components

---

## Security Management (FMT_*)

Security management SFRs control who may modify which security attributes:

| SFR | Coverage |
|-----|----------|
| **FMT_SMF.1/Base** | Specification of management functions — defines the complete list of management operations (create, delete, enable, disable ISD-P; install, enable, disable, delete Profile; configure ISD-P; update ISD-P metadata) |
| **FMT_SMR.1/Base** | Security management roles — defines roles authorised to perform management functions (S.ISD-R, U.SM-DP+, U.MNO-OTA, LPAd/IPAd, End User via LUId) |
| **FMT_MSA.1/PLATFORM_DATA** | Management of Platform data security attributes — restricts state transitions for ISD-P state (ENABLED/DISABLED/INSTALLED/SELECTABLE) |
| **FMT_MSA.1/RULES** | Management of PPRs and Reference Enterprise Rules — restricts modification and deletion to authorised actors |
| **FMT_MSA.1/RAT** | Management of Rules Authorisation Table — restricts RAT modification to manufacturing or initial Device setup |
| **FMT_MSA.1/CERT_KEYS** | Management of certificate and key attributes — restricts modification of eSIM CA keys and CRLs |
| **FMT_MSA.3** | Static attribute initialisation — defines restrictive default values for all security attributes |

---

## Platform and Internal Protection

### Secure Failure Modes
```
FPT_FLS.1/Base              — Failure with preservation of secure state
FPT_FLS.1/Platform_services — Platform services failure handling
```
These ensure that failures (including memory reset and test memory reset) do not compromise security. The Memory Reset function may override PPRs (disabling/deleting profiles even when PPRs prohibit it), which is an explicit documented exception.

### Internal Communications and Side Channels
```
FPT_EMS.1/Base  — TOE Emanation of TSF and User data
```
Ensures that secret data stored or transmitted within the TOE (shared secrets between ECASD and ISD-R/ISD-P, private keys, session keys) shall not be disclosed through side-channel emissions. This includes resistance to SPA, DPA, timing attacks, and electromagnetic radiation analysis.

```
FDP_SDI.1/Base  — Stored data integrity monitoring
FDP_RIP.1/Base  — Residual information protection
```
FDP_SDI.1 ensures integrity monitoring of all integrity-sensitive data (keys, Profile data, management data, identity data). FDP_RIP.1 ensures that deallocated resources do not leak residual confidential data.

### Random Number Generation
```
FCS_RNG.1/Base  — Random number generation
```
The ST author must select RNG classes (NTRG, DRG.2, DRG.3, DRG.4, PTG.2, PTG.3) as defined in AIS 20/31. This underpins all key generation, challenge-response protocols, and session key derivation.

---

## TOE Scope and Boundaries

What SGP.25 SFRs explicitly do **NOT** cover:

- **MNO-SD and Profiles** — These are user data under the control of the ISD-P, not part of the TOE. The MNO OTA Platform manages them through ES6, which the TOE enforces as a secure channel.
- **Runtime Environment** — The RE (e.g., Java Card System) provides the Application Firewall, secure communications, and code execution controls. It is expected to be certified under its own PP (e.g., [PP-JCS]) or translated into SFRs by the ST author.
- **Secure IC hardware** — The underlying chip's physical security is covered by OE.IC.* objectives, fulfilled by a separate hardware certification (e.g., [PP0084] for secure IC platforms).
- **LPAd/IPAd** — The device-side LPA is a non-TOE component assumed to provide trusted paths (ES10a/b/c) and end-user authentication.

---

## 📋 Summary

- SGP.25 defines four SFPs controlling secure channels, platform services, ISD-R content, and ECASD access
- FIA_* SFRs ensure every actor (remote SM-DP+, MNO-OTA, local MNO-SD) is identified and authenticated before any TSF-mediated action
- Communication SFRs protect confidentiality and integrity of all data exchanged over ES6, ES8+, ES9+, and ES11
- Security Domain access control SFRs enforce strict isolation between ISD-R, ISD-P, and ECASD based on AID and state attributes
- Management SFRs (FMT_*) define who can modify Profile Policy Rules, RAT, keys, and certificates — and what default values apply
- Internal protection SFRs cover side-channel resistance (FPT_EMS.1), integrity monitoring (FDP_SDI.1), and secure failure (FPT_FLS.1)

---

*Based on GSMA SGP.25 v2.1 (3 February 2025) — eUICC for Consumer and IoT Devices Protection Profile, Sections 3 (Security Problem Definition), 4 (Security Objectives), and 6 (Security Requirements including SFR definitions)*
