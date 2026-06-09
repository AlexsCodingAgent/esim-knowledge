---
title: "M2M Ecosystem: EUM, SM-DP, SM-SR, and the Operator"
description: "Explains the SGP.02 M2M ecosystem — the five entity roles (EUM, SM-DP, SM-SR, Operator, M2M SP), their ES1–ES8 interfaces, and how push provisioning distributes trust across the system."
date: 2026-06-07
---

# M2M Ecosystem: EUM, SM-DP, SM-SR, and the Operator

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > M2M Ecosystem: EUM, SM-DP, SM-SR, and the Operator**

If you're coming from consumer eSIM, your first look at the SGP.02 architecture diagram is going to feel... off. Where's the SM-DP+? Why are there two server roles where consumer eSIM has one? And who's this M2M SP character that doesn't exist in SGP.22 at all?

Here's the diagram from SGP.02 §2.1. Take a minute with it, every procedure in the spec flows through these boxes and lines.

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

The thing that jumps out: the SM-SR touches almost everything. EUM, SM-DP, Operator, M2M SP, other SM-SRs, and (critically) the eUICC itself. It's the hub. Every profile download, every enable/disable, every handover between SM-SR providers runs through it.

The other thing: there's no LPA. No device-side agent. The Device box at the bottom connects only through ESx: a minimal local interface for emergency operations. That's it.

## Meet the players

Six roles, each with a specific job. If you're skimming, the names are the important part: the rest is detail you can come back to.

### EUM: the factory

The eUICC Manufacturer builds the physical chip. During manufacturing, the EUM does three things that matter for the rest of the ecosystem's life:

1. Installs and personalizes the **ISD-R** (the on-card piece of the SM-SR) with initial SCP80/SCP81 keys
2. Creates the **ECASD** : the chip's immutable root of trust, embedding the eUICC's unique private key (`SK.ECASD.ECKA`), its certificate (`CERT.ECASD.ECKA`), the CI's public key (`PK.CI.ECDSA`), and the EID
3. Generates the **EIS** (eUICC Information Set) and ships it to the first SM-SR through ES1

The EUM's certificate (`CERT.EUM.ECDSA`) is signed by the CI and sits in the trust chain: CI → EUM → eUICC. When an SM-DP authenticates a chip during profile download, it's verifying that chain.

It may also pre-load a Provisioning Profile: a bootstrap subscription that gives the device enough connectivity to receive its first "real" profile over the air.

### CI: the trust anchor, mostly invisible

The Certificate Issuer is a GSMA-accredited authority. It generates a self-signed root certificate, signs certificates for EUMs, SM-DPs, and SM-SRs, and publishes CRLs when things go wrong.

You won't see the CI in procedure flows. It sits in the background, holding the trust infrastructure together. Every mutual authentication in SGP.02 traces back to the CI's root public key burned into the ECASD at manufacturing time.

### SM-DP: the profile factory

The Subscription Manager for Data Preparation builds profiles. Full operator subscriptions: NAAs (USIM/ISIM), file systems, applets, OTA keys. It encrypts each one for a specific eUICC (creating what the spec calls a Bound Profile Package) and establishes the SCP03 secure channel with the ISD-P on the chip.

The SM-DP talks to the Operator over **ES2** (25+ functions: profile ordering, lifecycle, auditing, authorization) and to the SM-SR over **ES3** (28 functions: ISD-P creation, profile download relay, lifecycle relay).

Here's what trips people up: **the SM-DP never talks directly to the eUICC.** Every command it sends to an ISD-P is wrapped in SCP03/SCT03t encryption and tunneled through the SM-SR. The SM-DP encrypts, hands the blob to the SM-SR via ES3, and the SM-SR pushes it down ES5 to the chip. The SM-SR is a courier, it can't read the package.

### SM-SR: the gatekeeper

This is the role that defines SGP.02. The Subscription Manager for Secure Routing owns the OTA channel to the eUICC. No other off-card entity can initiate contact with the chip: the SM-SR is the sole entry point.

It stores the EIS for every eUICC under management (addressing info, key sets, profile state). It creates ISD-Ps on the chip, enables and disables profiles, enforces policy rules, and manages connectivity parameters so the device stays reachable. When an operator wants to switch SM-SR providers, the SM-SR coordinates the handover procedure.

The SM-SR uses **ES4** (23 functions) to talk to Operators and M2M SPs, and **ES7** for SM-SR-to-SM-SR communication during handovers.

### Operator, owns the subscriber, calls the shots

The mobile network operator (or MVNO) owns the profiles. It orders them from the SM-DP (providing EID and ICCID), requests lifecycle operations through the SM-SR (or relayed through the SM-DP), and receives notifications about profile state changes. It can also authorize M2M SPs to manage its profiles, more on that below.

After a profile is installed, the Operator manages it directly through the ES6 OTA channel to the MNO-SD inside the profile's ISD-P. That channel bypasses the SM-DP and SM-SR entirely.

### M2M SP: the fleet manager who doesn't own connectivity

This role doesn't exist in consumer eSIM, and it's uniquely SGP.02. An M2M Service Provider manages a fleet of devices but contracts with operators for connectivity. Think:

- A car manufacturer running telematics across 40 countries, each using a local operator's profile
- A smart meter company that installs hardware and partners with regional MNOs
- A logistics provider tracking shipping containers worldwide

The M2M SP connects to the SM-SR over ES4 and can enable, disable, or delete profiles, but only ones it's been authorized to touch. Authorization comes from the Operator through PLMA settings, configured via the ES4A interface.

## Nine interfaces, two worlds

SGP.02 splits its interfaces cleanly: the ones that live on the chip and the ones that run between servers.

### Off-card (server-to-server)

| Interface | Between | What it does |
|-----------|---------|--------------|
| **ES1** | EUM → SM-SR | Register EIS at manufacturing, update properties |
| **ES2** | Operator → SM-DP | Profile ordering, lifecycle, auditing, PLMA/ONC (25 functions) |
| **ES3** | SM-DP → SM-SR | ISD-P creation, profile download relay, lifecycle relay (28 functions) |
| **ES4** | Operator/M2M SP → SM-SR | Direct lifecycle ops, EIS retrieval, SM-SR change (23 functions) |
| **ES4A** | Operator → SM-SR | Configure which M2M SPs can access which profiles |
| **ES7** | SM-SR → SM-SR | Handover during SM-SR change (CreateAdditionalKeySet, HandoverEUICC) |

### On-card (touching the eUICC)

| Interface | Between | What it does |
|-----------|---------|--------------|
| **ES5** | SM-SR → ISD-R | Platform management, OTA transport (SMS, HTTPS, CAT_TP) |
| **ES6** | Operator → MNO-SD | Post-install OTA profile management |
| **ES8** | SM-DP → ISD-P | Profile management tunneled through ES5 (SCP03/SCP03t) |
| **ESx** | Device → eUICC | Local enable/disable for emergency/test profiles |

ES8 deserves a closer look because it's not a physical interface, it's a tunnel. SM-DP commands get wrapped in SCP03/SCT03t encryption, sent to the SM-SR over ES3, then relayed inside the SCP80/SCP81-protected ES5 channel to the ISD-R, which forwards them to the right ISD-P. The SM-SR transports the encrypted payload but never sees the plaintext. It's an encrypted relay through an encrypted channel.

## Why the split architecture matters

Consumer eSIM collapses profile preparation and secure routing into one entity: the SM-DP+. SGP.02 keeps them separate. This isn't an accident, it's a commercial decision.

An operator can use one company for profile generation and a different one for OTA management. It can switch SM-SR providers without rebuilding its profiles (the SM-SR Change procedure in §3.8 handles migration). It can run multiple SM-DPs for different profile types (test profiles from one vendor, production from another) all through a single SM-SR.

The separation also means the SM-SR doesn't need to understand profile contents. It transports encrypted blobs. The SM-DP doesn't need to maintain OTA channels to thousands of devices. Each role does one thing, and the spec draws clean lines between them.

---

The SGP.02 ecosystem is built around the SM-SR: the hub that connects every other role. Six players, nine interfaces, one push architecture. If you understand who talks to whom and which interfaces carry the encrypted payloads, you've got the map for everything that follows.

---

<div align="center">

<a href="{{ site.baseurl }}/">🏠 Home</a>

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp02/00-sgp02-overview">SGP.02 Overview</a> | Next: <a href="{{ site.baseurl }}/docs/articles/sgp02/02-sgp02-euicc-internals">Inside the M2M eUICC</a> →

</div>

---

*Based on GSMA SGP.02 v4.2 §2.1, General Architecture*


---

← Previous: [SGP.02 v4.2: The M2M eSIM Push Architecture](00-sgp02-overview) | [Section Index](index) | Next: [Inside the M2M eUICC: ISD-R, ISD-P, ECASD, and EID](02-sgp02-euicc-internals) →
