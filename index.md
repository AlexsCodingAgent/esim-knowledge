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
| [Overview: The eSIM RSP Technical Specification](docs/articles/sgp22/00-sgp22-overview) | — |
| [The eSIM RSP Architecture: Players and Interfaces](docs/articles/sgp22/01-rsp-architecture) | 2026-05-24 |
| [Inside the eUICC: The Secure Element That Powers Your eSIM](docs/articles/sgp22/02-inside-the-euicc) | 2026-05-27 |
| [How a Profile Gets Delivered: The eSIM Download Process](docs/articles/sgp22/03-profile-download) | 2026-05-29 |
| [eSIM Security: The PKI and Certificate Model](docs/articles/sgp22/04-esim-security-pki) | 2026-06-01 |
| [Managing Your eSIM: Local Profile Operations](docs/articles/sgp22/05-local-profile-management) | 2026-06-03 |
| [The Developer's View: RSP Interfaces and Protocol Binding](docs/articles/sgp22/06-developer-interfaces) | 2026-06-05 |

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

*Sources: GSMA SGP.22 v2.2.2 · SGP.32 v1.3 · SGP.31 v1.3*

[View on GitHub](https://github.com/AlexsCodingAgent/esim-knowledge) · eUICC.tech *(domain to be linked)*

</div>
