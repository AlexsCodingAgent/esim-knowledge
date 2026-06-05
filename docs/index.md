---
title: eSIM RSP Knowledge Base
layout: default
---

# eUICC.tech — GSMA eSIM RSP Deep Dives

In-depth technical articles on GSMA eSIM Remote SIM Provisioning, built from primary source specifications SGP.22, SGP.31, and SGP.32.

---

## SGP.22 — Consumer eSIM RSP

| Article | Date |
|---------|------|
| [Overview: The eSIM RSP Technical Specification](articles/00-sgp22-overview) | — |
| [The eSIM RSP Architecture: Players and Interfaces](articles/01-rsp-architecture) | 2026-05-24 |
| [Inside the eUICC: The Secure Element That Powers Your eSIM](articles/02-inside-the-euicc) | 2026-05-27 |
| [How a Profile Gets Delivered: The eSIM Download Process](articles/03-profile-download) | 2026-05-29 |
| [eSIM Security: The PKI and Certificate Model](articles/04-esim-security-pki) | 2026-06-01 |
| [Managing Your eSIM: Local Profile Operations](articles/05-local-profile-management) | 2026-06-03 |
| [The Developer's View: RSP Interfaces and Protocol Binding](articles/06-developer-interfaces) | 2026-06-05 |

## SGP.32 / SGP.31 — IoT eSIM RSP

| Article | Date |
|---------|------|
| [eSIM for IoT: Why It Needed Its Own Architecture](articles/07-iot-esim-why) | 2026-05-22 |
| [The eSIM IoT Architecture: eIM, IPA, and New Interfaces](articles/08-iot-architecture-im-ipa) | 2026-05-26 |
| [IoT Profile Download: Direct, Indirect, and eIM Package Handling](articles/09-iot-profile-download-packages) | 2026-05-29 |
| [IoT eSIM Security: eIM Certificates, DTLS, and Device Trust](articles/10-iot-esim-security-dtls) | 2026-06-01 |
| [eIM Configuration: Associating Remote Managers with Your eUICC](articles/11-eim-configuration) | 2026-06-02 |
| [Notifications and Error Handling in IoT eSIM](articles/12-notifications-errors) | 2026-06-03 |
| [IoT Device Initialisation and the eUICC File Structure](articles/13-iot-device-initialisation) | 2026-06-04 |
| [Profile State Management via the eIM](articles/14-iot-profile-state-management) | 2026-06-05 |
| [SM-DS Operations in IoT eSIM](articles/15-iot-smsds-operations) | 2026-06-06 |
| [IoT eSIM Functions Reference: ESipa, ES9+', ES11', ESep](articles/16-iot-functions-reference) | 2026-06-07 |

## Architecture Diagrams

- [RSP Architecture Overview](diagrams/01-rsp-architecture.html)
- [eUICC Internal Architecture](diagrams/02-euicc-internals.html)
- [PKI Trust Chain](diagrams/03-pki-trust-chain.html)
- [IoT Architecture — eIM + IPA](diagrams/04-iot-architecture.html)
- [Profile Download Sequence](diagrams/05-profile-download-sequence.html)
- [Profile Package Stages](diagrams/06-profile-package-stages.html)

---

*Sources: GSMA SGP.22 v2.2.2, SGP.32 v1.3, SGP.31 v1.3*
