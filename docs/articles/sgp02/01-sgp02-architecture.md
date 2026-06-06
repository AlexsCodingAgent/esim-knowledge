---
date: 2026-06-07
---

# M2M Ecosystem: EUM, SM-DP, SM-SR, and the Operator

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > M2M Ecosystem: EUM, SM-DP, SM-SR, and the Operator**

> **📚 Prerequisites:** Read the [SGP.02 Overview]({{ site.baseurl }}/docs/articles/sgp02/00-sgp02-overview) first. Familiarity with smart card security domains (from our [Prerequisites Guide]({{ site.baseurl }}/docs/prerequisites)) is helpful.

> **💡 Why this matters:** Every procedure in SGP.02 — profile download, enabling, SM-SR change — flows through this ecosystem of roles and interfaces. Understanding who does what is the map you'll need for every article that follows.

> **Key takeaways:**
> - Six core roles form the SGP.02 ecosystem: EUM, CI, SM-DP, SM-SR, Operator, and M2M SP
> - The SM-DP and SM-SR are separate entities, unlike consumer eSIM's combined SM-DP+
> - Nine interfaces (ES1–ES8, ESx) connect these roles, split between on-card and off-card domains
> - The SM-SR is the hub — it connects to every other role except the CI
> - This architecture was designed for an operator-driven world where the device is passive

---

## The Architecture Diagram

SGP.02 §2.1 presents Figure 1 — the complete eUICC Remote Provisioning System. It's worth studying before we meet each player:

```
       CI
        |
   +---------+     ES2     +----------+
   |  SM-DP  |-------------| Operator |
   +---------+             +----------+
        | ES3                   | ES4
        |                  +----+----+
   +---------+   ES7   +---------+  | ES4A
   |  SM-SR  |---------|  SM-SR  |  |
   +---------+         +---------+  |
    ES1|   |ES5              |ES4    |
   +----+   |           +---------+  |
   | EUM |   |           | M2M SP  |--+
   +----+   |           +---------+
            | ES8             | ES6
         +----------------+  |
         |     eUICC      |--+
         | +------+------+|
         | | ISD-R|ISD-P||
         | +------+------+|
         | |    ECASD    ||
         | +-------------+|
         +----------------+
              | ESx
         +----------+
         |  Device  |
         +----------+
```

The diagram reveals a crucial architectural insight: the **SM-SR is the hub**. It connects directly to the EUM (ES1), the SM-DP (ES3), the Operator and M2M SP (ES4/ES4A), the eUICC (ES5), and other SM-SRs (ES7). Every profile download, every enable/disable operation, every SM-SR change flows through the SM-SR.

---

## The Six Core Roles

### EUM — eUICC Manufacturer

The **EUM** builds the physical eUICC chip and loads the initial firmware and security credentials. During manufacturing, the EUM:

- Installs and personalizes the **ISD-R** (the on-card SM-SR representative) with initial SCP80/SCP81 keys
- Creates the **ECASD** (the root of trust), embedding the eUICC's unique private key (`SK.ECASD.ECKA`), its certificate (`CERT.ECASD.ECKA`), the CI's public key (`PK.CI.ECDSA`), and the EID
- May pre-load an initial Provisioning Profile with connectivity for bootstrap operations
- Generates the **EIS** (eUICC Information Set) and sends it to the first SM-SR via the ES1 interface

The EUM's certificate (`CERT.EUM.ECDSA`), signed by the CI, is the link in the trust chain that proves a chip is genuine. When an SM-DP verifies an eUICC's certificate during profile download, it's tracing back through the EUM to the CI root.

### CI — Certificate Issuer

The **CI** (Certificate Issuer) is the root of trust for the entire SGP.02 PKI. It's a GSMA-accredited authority that:

- Issues a self-signed **Root Certificate** (`CERT.CI.ECDSA`)
- Signs certificates for EUMs, SM-DPs, and SM-SRs
- Publishes Certificate Revocation Lists (CRLs) when certificates are compromised or expired

The CI doesn't appear in procedure flows — it operates in the background, maintaining the trust infrastructure. Every mutual authentication in SGP.02 ultimately traces back to the CI's root public key stored in the ECASD.

### SM-DP — Subscription Manager, Data Preparation

The **SM-DP** is the profile factory. It:

- Prepares Profile Packages — complete operator subscriptions containing NAAs (USIM/ISIM), file systems, applets, and OTA keys
- Encrypts profiles for a specific eUICC (creating a Bound Profile Package)
- Establishes the SCP03 secure channel with the ISD-P on the eUICC via the ES8 interface
- Manages the profile download procedure end-to-end, working through the SM-SR as a relay

The SM-DP talks to the Operator via **ES2** (25+ functions for profile ordering, lifecycle, auditing, authorization) and to the SM-SR via **ES3** (28 functions for ISD-P creation, profile download relay, and lifecycle operations).

Critically, the SM-DP **never communicates directly with the eUICC**. All ES8 commands are tunneled through the SM-SR's ES5 channel. The SM-DP encrypts data for the ISD-P, hands it to the SM-SR via ES3, and the SM-SR relays it over ES5.

### SM-SR — Subscription Manager, Secure Routing

The **SM-SR** is the platform manager and OTA gateway. This is the role that defines SGP.02's push architecture. The SM-SR:

- **Owns the OTA channel** to the eUICC (ES5) — no other off-card entity can initiate communication
- Stores and maintains the **EIS** for every eUICC under management
- Executes Platform Management functions: ISD-P creation, profile enabling/disabling/deletion, policy rule enforcement
- Relays ES8 traffic between SM-DP and ISD-P
- Manages connectivity parameters (SMSC address, DNS servers) that the eUICC needs to stay reachable
- Coordinates SM-SR Change procedures when an operator migrates to a different SM-SR provider

The SM-SR uses **ES4** to communicate with Operators and M2M SPs (23 functions) and **ES7** to communicate with other SM-SRs during handover.

### Operator (MNO)

The **Operator** is the mobile network operator (or MVNO) that owns profiles and subscriber relationships. In SGP.02, the Operator:

- Orders profiles from the SM-DP via ES2, providing the target EID and ICCID
- Requests lifecycle operations: enable, disable, delete profiles
- Receives notifications about profile state changes via ONC (Operator Notification Configuration)
- Authorizes M2M SPs to perform lifecycle operations on its profiles via PLMA (Profile Lifecycle Management Authorization)
- Maintains its own OTA platform for post-install profile management via ES6

The Operator can connect to the SM-SR directly (ES4) or through its SM-DP (ES2→ES3→ES5 relay). The direct connection offers lower latency for lifecycle operations; the relay path is useful when the Operator has no direct business relationship with the SM-SR.

### M2M SP — M2M Service Provider

The **M2M SP** is a unique SGP.02 role absent from consumer eSIM. It represents a service provider that manages a device fleet but doesn't own the connectivity — it relies on an Operator for that. Examples:

- An automotive OEM managing telematics units across multiple countries, each using a local operator's profile
- A smart meter company that installs meters and contracts with regional operators for connectivity
- A fleet management provider tracking vehicles globally

The M2M SP connects to the SM-SR via **ES4** and can perform lifecycle operations (enable, disable, delete) on profiles it's authorized to manage. Authorization is granted by the Operator through PLMA settings. The **ES4A** interface allows the Operator to configure which M2M SPs can access which profiles.

---

## The Interface Landscape

SGP.02 defines nine interfaces, organized into two domains:

### Off-Card Interfaces (Server-to-Server)

| Interface | Between | Purpose |
|-----------|---------|---------|
| **ES1** | EUM → SM-SR | Register EIS at manufacturing, update properties |
| **ES2** | Operator → SM-DP | Profile ordering, lifecycle, auditing, PLMA/ONC management (25 functions) |
| **ES3** | SM-DP → SM-SR | ISD-P creation, profile download relay, lifecycle relay (28 functions) |
| **ES4** | Operator/M2M SP → SM-SR | Direct lifecycle operations, EIS retrieval, SM-SR change (23 functions) |
| **ES4A** | Operator → SM-SR | M2M SP authorization configuration |
| **ES7** | SM-SR → SM-SR | Handover during SM-SR change (CreateAdditionalKeySet, HandoverEUICC) |

### On-Card Interfaces (eUICC-Bound)

| Interface | Between | Purpose |
|-----------|---------|---------|
| **ES5** | SM-SR → eUICC (ISD-R) | Platform management commands, OTA channel (SMS, HTTPS, CAT_TP) |
| **ES6** | Operator → eUICC (MNO-SD) | Post-install OTA profile management |
| **ES8** | SM-DP → eUICC (ISD-P) | Profile management — SCP03/SCP03t tunneled through ES5 |
| **ESx** | Device → eUICC | Local enable/disable for emergency and test profiles (optional) |

The ES8 interface deserves special attention. It's not a physical interface — it's a **tunneled secure channel**. SM-DP commands are wrapped in SCP03/SCP03t encryption, transported over the ES3 link to the SM-SR, then relayed inside the SCP80/SCP81-protected ES5 channel to the ISD-R, which forwards them to the target ISD-P. The SM-SR never sees the plaintext — it's an encrypted relay.

---

## How This Differs from Consumer eSIM

If you're coming from SGP.22, the organizational differences are stark:

**SGP.22 (Consumer)**:
- SM-DP+ handles both profile preparation AND secure routing
- Device-initiated pull model via LPA
- SM-DS provides discovery (push notification alternative)
- ES9+ carries the HTTPS transport from LPA to SM-DP+
- User-facing: QR codes, LUI, activation codes

**SGP.02 (M2M)**:
- SM-DP and SM-SR are separate commercial entities with distinct responsibilities
- Server-initiated push model — the SM-SR calls the shots
- No LPA, no SM-DS, no QR codes
- ES5 is the OTA bearer (SMS/HTTPS/CAT_TP); ES8 is tunneled through it
- Operator-facing: the device is invisible to the end user

This separation has real commercial consequences. An operator can change SM-SR providers without touching its SM-DP relationship — the SM-SR Change procedure (SGP.02 §3.8) handles the migration. Similarly, an operator can use multiple SM-DPs for different profile types while maintaining a single SM-SR for OTA control.

---

## 📋 Summary

- The SGP.02 ecosystem has six roles: CI (trust root), EUM (chip manufacturer), SM-DP (profile factory), SM-SR (OTA gateway and platform manager), Operator (profile owner), and M2M SP (fleet manager)
- The SM-SR is the central hub, connected to every other role — it's the cornerstone of the push model
- Nine interfaces partition the system: off-card (ES1–ES4, ES7) handle business logic and server-to-server communication; on-card (ES5, ES6, ES8, ESx) handle chip-level operations
- The split SM-DP/SM-SR architecture provides commercial flexibility and vendor independence
- ES8 is not a physical interface — it's an encrypted tunnel through ES3 and ES5, ensuring the SM-SR never sees profile plaintext

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

← Previous: [SGP.02 Overview]({{ site.baseurl }}/docs/articles/sgp02/00-sgp02-overview) | Next: [Inside the M2M eUICC]({{ site.baseurl }}/docs/articles/sgp02/02-sgp02-euicc-internals) →

</div>

---

*Based on GSMA SGP.02 v4.2 §2.1 — General Architecture*


---

← Previous: [SGP.02 v4.2: The M2M eSIM Push Architecture](00-sgp02-overview) | [Section Index](index) | Next: [Inside the M2M eUICC: ISD-R, ISD-P, ECASD, and EID](02-sgp02-euicc-internals) →
