---
title: "The eSIM RSP Architecture: Players and Interfaces"
date: 2026-05-24
---

# The eSIM RSP Architecture: Players and Interfaces

## What Makes eSIM Different

A physical SIM card is straightforward — the operator programs a chip, you insert it, done. The GSMA's **Remote SIM Provisioning (RSP)** specification for consumer devices (SGP.22) replaces that physical step with a cryptographic protocol that delivers operator credentials over the internet into a chip that was manufactured months earlier, by a different company, in a different country.

The architecture defines five key roles and thirteen interfaces between them. Understanding who does what — and who trusts whom — is the foundation for understanding the entire system.

## The Five Players

### eUICC (embedded UICC)

The chip itself. A tamper-resistant secure element running a Java Card operating system, soldered into the device (or removable in some implementations). It hosts multiple isolated Profiles — each one the equivalent of a physical SIM card. The eUICC is manufactured and personalised by the **EUM** (eUICC Manufacturer) in a GSMA-certified secure facility.

### SM-DP+ (Subscription Manager — Data Preparation)

The profile factory. This server builds, encrypts, and delivers Profiles to eUICCs. It generates the cryptographic binding that ties a specific Profile to a specific chip, ensuring a Profile downloaded from the SM-DP+ is useless on any other eUICC. Operators either run their own SM-DP+ or use a third-party provider.

### SM-DS (Subscription Manager — Discovery Server)

The notification service. When an SM-DP+ has a Profile waiting for a specific eUICC, it registers an "Event" on the SM-DS. The device polls the SM-DS periodically to discover pending downloads. Crucially, the SM-DS only stores pointers (Event ID, EID, SM-DP+ address) — never the Profile itself. Multiple SM-DS instances can be cascaded for global scale.

### LPA (Local Profile Assistant)

The on-device orchestrator. This is the software that runs on your phone or device, managing everything eSIM-related. It has three sub-components:

- **LDS** (Local Discovery Service) — polls the SM-DS for pending Profiles
- **LPD** (Local Profile Download) — handles download from SM-DP+ and delivery to eUICC
- **LUI** (Local User Interface) — the screen the user sees to switch, add, or delete Profiles

The LPA can run either in the Device (**LPAd**) or inside the eUICC itself (**LPAe**) — both architectures are valid under SGP.22.

### Operator (MNO)

The mobile network operator. Orders Profiles from the SM-DP+, manages them post-install via OTA (Over-The-Air) through the ES6 interface, and handles the business relationship with the end user.

## The Thirteen Interfaces

| Interface | Between | Purpose |
|-----------|---------|---------|
| **ES2+** | Operator → SM-DP+ | Profile ordering, confirmation, cancellation |
| **ES6** | Operator → eUICC | Post-install OTA management of Operator services |
| **ES8+** | SM-DP+ ↔ eUICC (via LPA) | Secure end-to-end channel for profile installation (Perfect Forward Secrecy) |
| **ES9+** | SM-DP+ → LPA (LPD) | Secure transport for the Bound Profile Package |
| **ES10a** | LPA (LDS) → eUICC | eUICC info retrieval, SM-DS/DP address config, and discovery queries |
| **ES10b** | LPA (LPD) → eUICC | Profile transfer, authentication, challenge generation |
| **ES10c** | LPA (LUI) → eUICC | Local profile management: enable, disable, delete, rename |
| **ES11** | LPA (LDS) → SM-DS | Event retrieval for the respective eUICC |
| **ES12** | SM-DP+ → SM-DS | Event registration and deletion |
| **ES15** | SM-DS → SM-DS | Cascading between discovery servers |
| **ESop** | Operator → End User | Business interface (out of scope for SGP.22) |
| **ESeu** | End User → LUI | User-initiated local profile management (out of scope) |
| **ESci** | CI → SM-DP+/SM-DS/EUM | Certificate issuance and CRL retrieval |

## Trust Flows

The architecture establishes clear trust boundaries:

1. **The eUICC trusts the GSMA CI** (Certificate Issuer) — the root of the PKI. The CI's public keys are burned into the ECASD during manufacturing.
2. **The SM-DP+ proves its identity** to the eUICC by presenting a certificate signed by the CI.
3. **The eUICC proves its identity** to the SM-DP+ using its own certificate, signed by the EUM, whose certificate is also signed by the CI.
4. **The LPA is not cryptographically trusted** — it merely transports messages between the SM-DP+ and the eUICC. The ES8+ channel provides end-to-end encryption that the LPA cannot decrypt.
5. **The SM-DS is trusted for availability**, not confidentiality. It stores non-sensitive pointers, not profile data.

## Two Deployment Models

SGP.22 supports two architectural models for where the LPA lives:

**LPAd (LPA in Device):** The LPA runs as software on the device's application processor. This is how smartphones, tablets, and laptops implement eSIM today. The device handles all user interaction and profile management.

**LPAe (LPA in eUICC):** The LPA runs inside the eUICC itself, using either CAT (Card Application Toolkit) or SCWS (Smart Card Web Server). This model is used in constrained devices where the host device has limited capability — think IoT sensors, automotive modules, or wearables.

A device that supports a non-removable eUICC without an LPAe must provide an LPAd. An eUICC compliant with this specification must implement the LPA Services and may optionally implement the LPAe.

---

*Based on GSMA SGP.22 v2.2.2, Section 2 — General Architecture*
