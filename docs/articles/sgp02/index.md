---
date: 2026-06-07
---

# SGP.02 M2M RSP: Article Series

**🏠 [eUICC.tech]({{ site.baseurl }}/) > SGP.02 M2M RSP**

The SGP.02 specification defines the GSMA's Remote Provisioning Architecture for Embedded UICC in machine-to-machine devices. This 12-article series covers the complete M2M eSIM "push" architecture: from the ecosystem roles through profile download, lifecycle management, and the SM-SR Change procedure.

Articles are designed as ~1,200–1,800 word reads (<10 minutes each), building progressively from foundation to advanced topics.

---

## Foundation: What SGP.02 Is and Who the Players Are

1. **[SGP.02 v4.2: The M2M eSIM Push Architecture](00-sgp02-overview)** : What is SGP.02, the push model (SM-SR decides when profiles arrive), why it existed before IoT, scope vs SGP.22 consumer. *Spec: §1.1–1.8*

2. **[M2M Ecosystem: EUM, SM-DP, SM-SR, and the Operator](01-sgp02-architecture)** : Four core roles, interface landscape (ES1–ES8), how they differ from consumer roles, the SM-SR as central hub. *Spec: §2.1*

## Internals: The Chip, the PKI, the Communication Channels

3. **[Inside the M2M eUICC: ISD-R, ISD-P, ECASD, and EID](02-sgp02-euicc-internals)** : Security domains, EID structure, profile container lifecycle, profile isolation, and hardware requirements. *Spec: §2.2*

4. **[M2M Certificate Hierarchy: CI, EUM, SM-DP, SM-SR, and eUICC](03-sgp02-pki)** : Three-tier PKI, dual certificate format (X.509 and GlobalPlatform), CRL management, algorithm requirements through 2030. *Spec: §2.3*

5. **[OTA Communication: SMS, PSK-TLS, CAT_TP, and DNS](04-sgp02-ota)** : The ES5 bearer, SMS triggering, PSK-TLS handshake, HTTP POST pattern, CAT_TP transport, DNS resolution for SM-SR addresses. *Spec: §2.4–2.8*

## Procedures: How Profiles Actually Work

6. **[Profile Download: ISD-P Creation, SCP03, and Encrypted Delivery](05-sgp02-download)** : Full download flow, ISD-P creation, Scenario#3 mutual authentication, ECKA-EG key agreement, SCP03/SCP03t encrypted delivery, error management. *Spec: §3.1*

7. **[Profile Lifecycle: Enable, Disable, Delete, and Fall-Back](06-sgp02-lifecycle)** : Three initiation paths (Operator ES4, SM-DP relay, M2M SP ES4), state machine transitions, enabling/disabling semantics, Master Delete with Delete Token. *Spec: §3.2–3.7, §3.10*

8. **[SM-SR Change: Handover, ES7 Interface, and EIS Migration](07-sgp02-sm-sr-change)** : Full 32-step handover between SM-SRs, ES7 interface functions (HandoverEUICC, AuthenticateSM-SR, CreateAdditionalKeySet), EIS migration, preventing vendor lock-in. *Spec: §3.8–3.9, §5.6*

## Advanced Topics

9. **[Resilience: Fall-Back Mechanism, Emergency Profiles, and Test Profiles](08-sgp02-resilience)** : Fall-Back Profile concept and autonomous activation, Emergency Profile for regulatory compliance, Test Profile lifecycle, local enable/disable via ESx. *Spec: §3.16, §3.22–3.31*

10. **[Policy Rules & Notifications: POL1, POL2, and the Default Notification](09-sgp02-policy-notifications)** : Dual-enforcement POL1/POL2 framework, notification types and SMS/HTTPS delivery, Default Notification procedure, ONC (Operator Notification Configuration), PLMA for M2M SP authorisation. *Spec: §3.11–3.15, §3.20–3.21*

11. **[Off-Card Interfaces: ES1–ES7 and the SOAP Binding](10-sgp02-offcard-interfaces)** : Complete function catalog for ES1–ES7, ES4A for M2M SP/ONC, SOAP/HTTPS binding with WS-Addressing and WS-Security, ASN.1 message mapping. *Spec: Chapter 5, Annex A–C*

12. **[SGP.02 vs SGP.22 vs SGP.32: Push, Pull, and the Evolution of eSIM](11-sgp02-comparison)** : Comparative analysis across all three GSMA eSIM specs, when to use which standard, M2M push vs consumer pull vs IoT pull, migration paths from legacy M2M to modern IoT. *Cross-spec comparison*

---

## Reading Order

The articles build progressively:

- **Foundation** (Articles 1–2): What SGP.02 is, who the players are
- **Internals** (Articles 3–5): The chip, the PKI, the communication channels
- **Procedures** (Articles 6–8): Profile download, lifecycle, SM-SR change
- **Advanced Topics** (Articles 9–10): Resilience, policy rules
- **Interfaces** (Article 11): The API layer
- **Context** (Article 12): Where SGP.02 sits in the eSIM universe

A reader can stop after Article 7 and have working knowledge of SGP.02. Articles 8–12 provide depth for implementation or architectural decision-making.

---

*Specification: GSMA SGP.02 v4.2 (07 July 2020) : Remote Provisioning Architecture for Embedded UICC Technical Specification, 452 pages*
