---
layout: default
title: eUICC.tech — eSIM RSP Knowledge Base
---

<div align="center">

# 🔐 eUICC.tech

### Deep Dives Into GSMA eSIM Remote SIM Provisioning

*Built from primary source specifications SGP.22, SGP.31, and SGP.32*

</div>

---

## 🚀 Start Here

New to eSIM? Read these in order — each builds on the last.

| # | Article | What You'll Learn |
|---|---------|-------------------|
| 1 | [Overview: The eSIM RSP Technical Specification](docs/articles/sgp22/00-sgp22-overview) | The big picture — what RSP is, who the players are, how the interfaces connect |
| 2 | [The eSIM RSP Architecture: Players and Interfaces](docs/articles/sgp22/01-rsp-architecture) | Deep dive into all 5 entities and 13 interfaces, trust flows, deployment models |
| 3 | [Inside the eUICC: The Secure Element That Powers Your eSIM](docs/articles/sgp22/02-inside-the-euicc) | ISD-R, ISD-P, ECASD, Profile Policy Enabler — the chip's internal architecture |
| 4 | [How a Profile Gets Delivered: The eSIM Download Process](docs/articles/sgp22/03-profile-download) | The full 3-phase download: initiation, authentication, installation — step by step |
| 5 | [eSIM Security: The PKI and Certificate Model](docs/articles/sgp22/04-esim-security-pki) | ECDSA, ECDH, certificate chains, revocation — how eSIM prevents man-in-the-middle |
| 6 | [Managing Your eSIM: Local Profile Operations](docs/articles/sgp22/05-local-profile-management) | Enable, disable, delete, rename — what the LPA does after profiles are installed |
| 7 | [The Developer's View: RSP Interfaces and Protocol Binding](docs/articles/sgp22/06-developer-interfaces) | ASN.1 structures, HTTPS/ES8+/ES9+ bindings, the developer-facing side |

---

## 📱 SGP.22 — Consumer eSIM RSP

*Phones, tablets, wearables, laptops — the eSIM you use every day.*

| Article | Date |
|---------|------|
| [Overview](docs/articles/sgp22/00-sgp22-overview) | — |
| [Architecture](docs/articles/sgp22/01-rsp-architecture) | 2026-05-24 |
| [Inside the eUICC](docs/articles/sgp22/02-inside-the-euicc) | 2026-05-27 |
| [Profile Download](docs/articles/sgp22/03-profile-download) | 2026-05-29 |
| [Security & PKI](docs/articles/sgp22/04-esim-security-pki) | 2026-06-01 |
| [Profile Management](docs/articles/sgp22/05-local-profile-management) | 2026-06-03 |
| [Developer Interfaces](docs/articles/sgp22/06-developer-interfaces) | 2026-06-05 |

---

## 🤖 SGP.32 / SGP.31 — IoT eSIM RSP

*NB-IoT, LTE-M, sensors, trackers — eSIM for things that have no screen.*

| Article | Date |
|---------|------|
| [eSIM for IoT: Why It Needed Its Own Architecture](docs/articles/sgp32/07-iot-esim-why) | 2026-05-22 |
| [The eSIM IoT Architecture: eIM, IPA, and New Interfaces](docs/articles/sgp32/08-iot-architecture-im-ipa) | 2026-05-26 |
| [IoT Profile Download: Direct, Indirect, and eIM Package Handling](docs/articles/sgp32/09-iot-profile-download-packages) | 2026-05-29 |
| [IoT eSIM Security: eIM Certificates, DTLS, and Device Trust](docs/articles/sgp32/10-iot-esim-security-dtls) | 2026-06-01 |
| [eIM Configuration: Associating Remote Managers with Your eUICC](docs/articles/sgp32/11-eim-configuration) | 2026-06-02 |
| [Notifications and Error Handling in IoT eSIM](docs/articles/sgp32/12-notifications-errors) | 2026-06-03 |
| [IoT Device Initialisation and the eUICC File Structure](docs/articles/sgp32/13-iot-device-initialisation) | 2026-06-04 |
| [Profile State Management via the eIM](docs/articles/sgp32/14-iot-profile-state-management) | 2026-06-05 |
| [SM-DS Operations in IoT eSIM](docs/articles/sgp32/15-iot-smsds-operations) | 2026-06-06 |
| [IoT eSIM Functions Reference: ESipa, ES9+', ES11', ESep](docs/articles/sgp32/16-iot-functions-reference) | 2026-06-07 |

---

## 🎨 Architecture Diagrams

*Dark-themed SVG diagrams — open in any browser.*

| Diagram | What It Shows |
|---------|---------------|
| [RSP Architecture Overview](docs/diagrams/01-rsp-architecture.html) | All 5 entities, 13 interfaces, trust relationships |
| [eUICC Internal Architecture](docs/diagrams/02-euicc-internals.html) | ISD-R, ISD-P, ECASD, security domains, profile isolation |
| [PKI Trust Chain](docs/diagrams/03-pki-trust-chain.html) | CI → EUM → eUICC certificate hierarchy |
| [IoT Architecture — eIM + IPA](docs/diagrams/04-iot-architecture.html) | The SGP.32 ecosystem: eIM, IPA, SM-DP+, new interfaces |
| [Profile Download Sequence](docs/diagrams/05-profile-download-sequence.html) | Full message flow: activation → auth → install |
| [Profile Package Stages](docs/diagrams/06-profile-package-stages.html) | How a profile moves from operator → SM-DP+ → eUICC |

---

## 📚 Key Concepts

| Concept | Quick Explanation |
|---------|-------------------|
| **eUICC** | The tamper-resistant chip that holds profiles — not just storage, a full Java Card OS |
| **Profile** | One operator's credentials inside an eUICC — equivalent to one physical SIM |
| **ISD-P** | Issuer Security Domain — Profile — the container for each profile inside the eUICC |
| **ISD-R** | Issuer Security Domain — Root — the profile manager on the chip |
| **ECASD** | eUICC Controlling Authority Security Domain — the root of trust, holds CI public keys |
| **SM-DP+** | Subscription Manager Data Preparation — builds and encrypts profiles |
| **SM-DS** | Subscription Manager Discovery Server — notifies devices of pending profiles |
| **LPA** | Local Profile Assistant — the on-device software that orchestrates downloads |
| **eIM** | eSIM IoT Remote Manager — the remote entity that manages IoT device profiles |
| **IPA** | IoT Profile Assistant — the stripped‑down on‑device proxy for IoT devices |
| **PSMO** | Profile State Management Operation — remote enable/disable/delete (IoT only) |
| **ECDSA** | Elliptic Curve Digital Signature Algorithm — P‑256, used for mutual authentication |
| **ECDH** | Elliptic Curve Diffie‑Hellman — ephemeral key exchange for Perfect Forward Secrecy |
| **CRL** | Certificate Revocation List — how compromised certificates are invalidated |

---

<div align="center">

---

## 🧪 SGP.23 / SGP.23-1 — RSP Test Specifications

*How eSIM interoperability is tested and certified.*

| Article | Date |
|---------|------|
| [SGP.23 Overview: How eSIM Interoperability Is Tested](docs/articles/sgp23/17-sgp23-overview) | 2026-06-05 |
| [The GSMA eSIM Test Infrastructure](docs/articles/sgp23/18-sgp23-test-infrastructure) | 2026-06-05 |
| [Testing the LPA: LDS, LPD, and LUI Conformance](docs/articles/sgp23/19-sgp23-lpa-testing) | 2026-06-05 |
| [Testing the SM-DP+ and SM-DS](docs/articles/sgp23/20-sgp23-server-testing) | 2026-06-05 |
| [SGP.23 Certification: From Test Cases to DLOA](docs/articles/sgp23/21-sgp23-certification) | 2026-06-05 |
| [SGP.23-1 Overview: Testing the eUICC Itself](docs/articles/sgp23-1/32-sgp23-1-overview) | 2026-06-05 |
| [eUICC Test Architecture: Readers, Scripts, and GSMA Tools](docs/articles/sgp23-1/33-sgp23-1-architecture) | 2026-06-05 |
| [Key eUICC Test Cases: ISD-R, ECASD, and Profile Lifecycle](docs/articles/sgp23-1/34-sgp23-1-test-cases) | 2026-06-05 |
| [eUICC Security Testing: Certificates, Keys, and Channels](docs/articles/sgp23-1/35-sgp23-1-security) | 2026-06-05 |
| [eUICC Certification: From Tests to SAS-UP Approval](docs/articles/sgp23-1/36-sgp23-1-certification) | 2026-06-05 |

---

## 🔒 SGP.25 — eUICC Protection Profile

*Common Criteria security certification for eUICC hardware.*

| Article | Date |
|---------|------|
| [SGP.25 Overview: The eUICC Common Criteria Protection Profile](docs/articles/sgp25/22-sgp25-overview) | 2026-06-05 |
| [eUICC Security Functional Requirements](docs/articles/sgp25/23-sgp25-security-requirements) | 2026-06-05 |
| [eUICC Assurance Requirements: EAL4+ and Penetration Testing](docs/articles/sgp25/24-sgp25-assurance) | 2026-06-05 |
| [Physical Security: Side-Channel and Fault Injection Defenses](docs/articles/sgp25/25-sgp25-physical-security) | 2026-06-05 |
| [SGP.25 Certification: SAS-UP and the Evaluation Process](docs/articles/sgp25/26-sgp25-certification) | 2026-06-05 |

---

## 📜 SGP.26 — RSP Test Certificates Definition

*The PKI for eSIM development and testing.*

| Article | Date |
|---------|------|
| [SGP.26 Overview: The GSMA RSP Test Certificate Infrastructure](docs/articles/sgp26/37-sgp26-overview) | 2026-06-05 |
| [Test Certificate Hierarchy: CI, EUM, DP, DS, and eUICC](docs/articles/sgp26/38-sgp26-hierarchy) | 2026-06-05 |
| [Certificate Profiles: What Makes a Valid Test Certificate](docs/articles/sgp26/39-sgp26-profiles) | 2026-06-05 |
| [Using Test Certificates: Developer Setup and Integration](docs/articles/sgp26/40-sgp26-development) | 2026-06-05 |
| [CRL and Certificate Management in the Test Ecosystem](docs/articles/sgp26/41-sgp26-crl) | 2026-06-05 |

---

## 🆔 SGP.29 — EID Definition and Assignment

*The 32-digit eUICC Identifier — format, assignment, and governance.*

| Article | Date |
|---------|------|
| [SGP.29 Overview: The eUICC Identifier (EID)](docs/articles/sgp29/27-sgp29-overview) | 2026-06-05 |
| [EID Format Decoded: The 32-Digit Structure](docs/articles/sgp29/28-sgp29-eid-format) | 2026-06-05 |
| [EID Assignment: How Manufacturers Get Their Allocations](docs/articles/sgp29/29-sgp29-assignment) | 2026-06-05 |
| [EID in RSP Protocols: Discovery, Matching, and Events](docs/articles/sgp29/30-sgp29-in-protocols) | 2026-06-05 |
| [EID Security: Privacy, Tracking, and GSMA Governance](docs/articles/sgp29/31-sgp29-security) | 2026-06-05 |

---

## 🤖 SGP.33-3 — eIM Test Specification

*Testing the eSIM IoT Manager for SGP.32 deployments.*

| Article | Date |
|---------|------|
| [SGP.33 Overview: The IoT eSIM Test Family](docs/articles/sgp33-3/42-sgp33-overview) | 2026-06-05 |
| [eIM Test Architecture: Simulated eIM and Reference IPA](docs/articles/sgp33-3/43-sgp33-eim-architecture) | 2026-06-05 |
| [Key eIM Test Cases: PSMO, Notifications, and Configuration](docs/articles/sgp33-3/44-sgp33-eim-test-cases) | 2026-06-05 |
| [eIM Security Testing: DTLS, Certificates, and Signed Packages](docs/articles/sgp33-3/45-sgp33-eim-security) | 2026-06-05 |
| [IoT eSIM Certification Path: From Test Cases to Production](docs/articles/sgp33-3/46-sgp33-certification) | 2026-06-05 |

---

## 🏭 SGP.41 — In-Factory Profile Provisioning (IFPP)

*Pre-loading eSIM profiles during device manufacturing.*

| Article | Date |
|---------|------|
| [SGP.41 Overview: In-Factory Profile Provisioning](docs/articles/sgp41/47-sgp41-overview) | 2026-06-05 |
| [The IFPP Architecture: SM-DPf, FPA, and Device Manufacturer](docs/articles/sgp41/48-sgp41-architecture) | 2026-06-05 |
| [IFPP Flow: Manufacturing Step to Configuration Step](docs/articles/sgp41/49-sgp41-flow) | 2026-06-05 |
| [IFPP Security: Factory Trust Models and Certificate Chains](docs/articles/sgp41/50-sgp41-security) | 2026-06-05 |
| [IFPP in Practice: PC OEMs, Automotive, and IoT Manufacturing](docs/articles/sgp41/51-sgp41-practice) | 2026-06-05 |

---

## 🗺️ Standards Map

[📊 Complete GSMA SGP Standards Map and Timeline →](docs/standards-map)

---

*Sources: GSMA SGP.22 v2.7 · SGP.23 v1.16 · SGP.23-1 v3.1.3 · SGP.25 v2.1 · SGP.26 v3.0.2 · SGP.29 v1.1 · SGP.31 v1.3 · SGP.32 v1.3 · SGP.33-3 v1.2 · SGP.41 v1.0*

[View on GitHub](https://github.com/AlexsCodingAgent/esim-knowledge) · eUICC.tech *(domain to be linked)* · [📖 Glossary](docs/glossary) · [📚 Prerequisites](docs/prerequisites) · [🧒 Kid-Friendly Versions](docs/articles/kids/) · [🗺️ Standards Map](docs/standards-map)

</div>
