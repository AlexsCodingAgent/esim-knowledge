---
layout: default
title: "eSIM RSP Knowledge Base — AI-Optimized Index"
---

<div align="center">

# 🔐 eUICC.tech

### eSIM RSP Knowledge Base · 72 articles · 11 specifications

*AI-optimized index — structured for LLM retrieval and semantic search*

</div>

---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "eSIM RSP Knowledge Base",
  "description": "72 technical articles covering all 11 GSMA eSIM Remote SIM Provisioning specifications",
  "url": "https://alexscodingagent.github.io/esim-knowledge/ai",
  "about": {
    "@type": "Thing",
    "name": "eSIM Remote SIM Provisioning",
    "description": "GSMA eSIM RSP specifications including SGP.22, SGP.32, SGP.41, and related standards"
  }
}
</script>

## 📱 SGP.22 v2.7 — Consumer eSIM (12 articles)

**What it is:** The core specification for consumer eSIM — phones, tablets, wearables, laptops. Defines how profiles are downloaded, installed, enabled, and deleted on consumer devices.

| # | Question This Article Answers | Link |
|---|-------------------------------|------|
| 00 | What is eSIM Remote SIM Provisioning and how does it work? | [Read →](docs/articles/sgp22/00-sgp22-overview) |
| 01 | What are the five entities and thirteen interfaces in the eSIM RSP architecture? | [Read →](docs/articles/sgp22/01-rsp-architecture) |
| 02 | What is inside an eUICC chip? How do ISD-R, ISD-P, and ECASD work? | [Read →](docs/articles/sgp22/02-inside-the-euicc) |
| 03 | How is an eSIM profile downloaded in three phases? | [Read →](docs/articles/sgp22/03-profile-download) |
| 04 | How does eSIM PKI security work? What certificates and signatures protect profiles? | [Read →](docs/articles/sgp22/04-esim-security-pki) |
| 05 | How do you enable, disable, and delete eSIM profiles locally? | [Read →](docs/articles/sgp22/05-local-profile-management) |
| 06 | What are the ES2+, ES8+, ES9+, and ES10x interfaces and how are they bound to protocols? | [Read →](docs/articles/sgp22/06-developer-interfaces) |
| 07 | What is LPAe and how does the in-eUICC Local Profile Assistant work? | [Read →](docs/articles/sgp22/07-lpae-in-euicc) |
| 08 | What happens during eUICC boot and device initialisation? | [Read →](docs/articles/sgp22/08-boot-initialisation) |
| 09 | What are PPRs, the Rules Authorisation Table, and the Profile Policy Enabler? | [Read →](docs/articles/sgp22/09-policy-management) |
| 10 | How do eSIM notifications work? What is ES6 post-install OTA management? | [Read →](docs/articles/sgp22/10-notifications-postinstall) |
| 11 | How does SM-DS event management work? What are companion device scenarios? | [Read →](docs/articles/sgp22/11-smds-companion) |

---

## 🔀 SGP.22 v3.x — Unified RSP (12 articles)

**What it is:** The next-generation specification that merges consumer (SGP.22) and M2M (SGP.02) into one unified standard. Adds Multiple Enabled Profiles, Push Service, Remote Profile Management, and Enterprise Profiles.

| # | Question This Article Answers | Link |
|---|-------------------------------|------|
| 52 | What is SGP.22 v3.x and how does it unify consumer and M2M eSIM? | [Read →](docs/articles/sgp22-v3/52-sgp22-v3-overview) |
| 53 | How does Multiple Enabled Profiles (MEP) let one eUICC run several active profiles? | [Read →](docs/articles/sgp22-v3/53-multiple-enabled-profiles) |
| 54 | How does the Push Service replace SM-DS polling for profile notifications? | [Read →](docs/articles/sgp22-v3/54-push-service) |
| 55 | How does capability negotiation work between eSIM entities in v3.x? | [Read →](docs/articles/sgp22-v3/55-feature-support) |
| 56 | How do SGP.22 v2.x and v3.x interoperate? What happens during version negotiation? | [Read →](docs/articles/sgp22-v3/56-version-interoperability) |
| 57 | How does Remote Profile Management (RPM) work in three phases? | [Read →](docs/articles/sgp22-v3/57-remote-profile-management) |
| 58 | How do you transfer eSIM profiles between devices? What is profile recovery? | [Read →](docs/articles/sgp22-v3/58-device-change-and-profile-recovery) |
| 59 | How are eUICC root keys updated? What is Profile Content Management (PCM)? | [Read →](docs/articles/sgp22-v3/59-euicc-updates-pcm) |
| 60 | How does profile download and installation work in the v3.x context? | [Read →](docs/articles/sgp22-v3/60-profile-download-v3) |
| 61 | How are profiles cryptographically packaged? What is the BPP Security Protocol? | [Read →](docs/articles/sgp22-v3/61-profile-protection-bpp) |
| 62 | How does profile policy management work in v3.x? What are Enterprise Rules? | [Read →](docs/articles/sgp22-v3/62-policy-management-v3) |
| 63 | What are Enterprise Profiles? How do they restrict end-user control? | [Read →](docs/articles/sgp22-v3/63-enterprise-profiles) |

---

## 🤖 SGP.32 / SGP.31 — IoT eSIM (12 articles)

**What it is:** eSIM for devices without screens — NB-IoT, LTE-M sensors, trackers, and industrial equipment. Introduces the eIM (remote manager) and IPA (on-device proxy) architecture.

| # | Question This Article Answers | Link |
|---|-------------------------------|------|
| 07 | Why did IoT devices need their own eSIM architecture instead of SGP.22? | [Read →](docs/articles/sgp32/07-iot-esim-why) |
| 08 | What are the eIM and IPA? How does the IoT eSIM architecture work? | [Read →](docs/articles/sgp32/08-iot-architecture-im-ipa) |
| 09 | How does IoT profile download work? What are direct and indirect delivery? | [Read →](docs/articles/sgp32/09-iot-profile-download-packages) |
| 10 | How does IoT eSIM security work? What is the role of DTLS and eIM certificates? | [Read →](docs/articles/sgp32/10-iot-esim-security-dtls) |
| 11 | How is an eIM configured and associated with an eUICC? | [Read →](docs/articles/sgp32/11-eim-configuration) |
| 12 | How do notifications and error handling work in IoT eSIM? | [Read →](docs/articles/sgp32/12-notifications-errors) |
| 13 | How does an IoT device initialise? What is the eUICC file structure? | [Read →](docs/articles/sgp32/13-iot-device-initialisation) |
| 14 | How does remote profile state management (enable, disable, delete) work via the eIM? | [Read →](docs/articles/sgp32/14-iot-profile-state-management) |
| 15 | How do SM-DS operations work in IoT eSIM? | [Read →](docs/articles/sgp32/15-iot-smsds-operations) |
| 16 | What are the ESipa, ES9+', ES11', and ESep IoT eSIM functions? | [Read →](docs/articles/sgp32/16-iot-functions-reference) |
| 17 | What are the three IoT profile types? How does the Profile Policy Enabler work? | [Read →](docs/articles/sgp32/17-profile-lifecycle-policy) |
| 18 | How does mutual authentication work in IoT eSIM? What are Emergency Profiles? | [Read →](docs/articles/sgp32/18-advanced-security-lifecycle) |

---

## 🏭 SGP.41 — In-Factory Profile Provisioning (5 articles)

**What it is:** Pre-loading eSIM profiles during device manufacturing — cars, laptops, smartwatches that ship with connectivity already active.

| # | Question This Article Answers | Link |
|---|-------------------------------|------|
| 47 | What is In-Factory Profile Provisioning (IFPP)? | [Read →](docs/articles/sgp41/47-sgp41-overview) |
| 48 | What is the IFPP architecture? What are SM-DPf and FPA? | [Read →](docs/articles/sgp41/48-sgp41-architecture) |
| 49 | How does the IFPP flow work from manufacturing to configuration? | [Read →](docs/articles/sgp41/49-sgp41-flow) |
| 50 | How does IFPP security work? What are the factory trust models? | [Read →](docs/articles/sgp41/50-sgp41-security) |
| 51 | Who uses IFPP? What are real-world automotive, laptop, and IoT applications? | [Read →](docs/articles/sgp41/51-sgp41-practice) |

---

## 📡 SGP.02 v4.2 — M2M eSIM (Legacy Push Model) (12 articles)

**What it is:** The original machine-to-machine eSIM specification. Uses a "push" model where the SM-SR controls when profiles are delivered, unlike the consumer "pull" model. Still deployed in millions of industrial and automotive devices.

| # | Question This Article Answers | Link |
|---|-------------------------------|------|
| 00 | What is SGP.02 and how does the M2M push model work? | [Read →](docs/articles/sgp02/00-sgp02-overview) |
| 01 | What are the six M2M roles and how do EUM, SM-DP, and SM-SR differ from consumer? | [Read →](docs/articles/sgp02/01-sgp02-architecture) |
| 02 | How does the M2M eUICC differ? What are ISD-R, ISD-P, ECASD, and EID in M2M? | [Read →](docs/articles/sgp02/02-sgp02-euicc-internals) |
| 03 | How does the three-tier M2M PKI work? What certs do CI, EUM, SM-DP, and SM-SR hold? | [Read →](docs/articles/sgp02/03-sgp02-pki) |
| 04 | How does OTA communication work in M2M? What are SMS, PSK-TLS, and CAT_TP? | [Read →](docs/articles/sgp02/04-sgp02-ota) |
| 05 | How are profiles downloaded in M2M? What is SCP03 key establishment? | [Read →](docs/articles/sgp02/05-sgp02-download) |
| 06 | How does profile lifecycle (enable, disable, delete) work in M2M? | [Read →](docs/articles/sgp02/06-sgp02-lifecycle) |
| 07 | How does SM-SR Change work? What is the ES7 handover procedure? | [Read →](docs/articles/sgp02/07-sgp02-sm-sr-change) |
| 08 | How does M2M handle resilience? What are fall-back and emergency profiles? | [Read →](docs/articles/sgp02/08-sgp02-resilience) |
| 09 | How do POL1/POL2 policy rules work? What are M2M notifications? | [Read →](docs/articles/sgp02/09-sgp02-policy-notifications) |
| 10 | What are the ES1-ES7 off-card interfaces? How does SOAP binding work? | [Read →](docs/articles/sgp02/10-sgp02-offcard-interfaces) |
| 11 | How does SGP.02 compare to SGP.22 and SGP.32? Which should you use? | [Read →](docs/articles/sgp02/11-sgp02-comparison) |

---

## 🆔 SGP.29 — EID Definition and Assignment (5 articles)

**What it is:** The 32-digit eUICC Identifier — how it's formatted, assigned, and used across the eSIM ecosystem.

| # | Question This Article Answers | Link |
|---|-------------------------------|------|
| 27 | What is the EID? How is the eUICC Identifier defined? | [Read →](docs/articles/sgp29/27-sgp29-overview) |
| 28 | How is the 32-digit EID structured? What does each part mean? | [Read →](docs/articles/sgp29/28-sgp29-eid-format) |
| 29 | How are EIDs assigned to manufacturers? | [Read →](docs/articles/sgp29/29-sgp29-assignment) |
| 30 | How is the EID used in RSP protocols for discovery and matching? | [Read →](docs/articles/sgp29/30-sgp29-in-protocols) |
| 31 | What are the security and privacy considerations for EIDs? | [Read →](docs/articles/sgp29/31-sgp29-security) |

---

## 🧪 Testing & Certification (25 articles)

| Spec | Description | Articles | Browse |
|------|-------------|----------|--------|
| SGP.23 | Consumer eSIM conformance testing | 5 | [Browse →](docs/articles/sgp23/) |
| SGP.23-1 | eUICC chip-level conformance testing | 5 | [Browse →](docs/articles/sgp23-1/) |
| SGP.25 | eUICC Common Criteria EAL4+ Protection Profile | 5 | [Browse →](docs/articles/sgp25/) |
| SGP.26 | RSP test certificate infrastructure (PKI for development) | 5 | [Browse →](docs/articles/sgp26/) |
| SGP.33-3 | eIM test specification for IoT eSIM | 5 | [Browse →](docs/articles/sgp33-3/) |

---

## 🔗 Quick Reference

| Topic | Best Starting Article |
|-------|----------------------|
| How does eSIM work? | [SGP.22 Overview](docs/articles/sgp22/00-sgp22-overview) |
| How are profiles downloaded? | [Profile Download](docs/articles/sgp22/03-profile-download) |
| How is eSIM secured? | [Security & PKI](docs/articles/sgp22/04-esim-security-pki) |
| What's new in the latest eSIM spec? | [SGP.22 v3.x Overview](docs/articles/sgp22-v3/52-sgp22-v3-overview) |
| How does IoT eSIM differ from consumer? | [Why IoT Needed Its Own Architecture](docs/articles/sgp32/07-iot-esim-why) |
| How are eSIMs tested and certified? | [SGP.23 Overview](docs/articles/sgp23/17-sgp23-overview) |
| What's an EID? | [EID Overview](docs/articles/sgp29/27-sgp29-overview) |
| How are profiles pre-loaded at factories? | [IFPP Overview](docs/articles/sgp41/47-sgp41-overview) |

---

*[📖 Illustrated Edition](docs/articles/kids/) · [📋 Full Technical Index](docs/articles/) · [📖 Glossary](docs/glossary) · [🗺️ Standards Map](docs/standards-map)*
