# SGP.02 v4.2 — M2M eSIM Architecture: 12-Article Series Plan

**Spec:** GSMA SGP.02 v4.2 — Remote Provisioning Architecture for Embedded UICC Technical Specification (452 pages, July 2020)
**Audience:** Technical professionals wanting to understand the M2M "push" eSIM provisioning model
**Article length:** ~1,200–1,800 words each, <10 minute reads

---

## Article 1: SGP.02 and the M2M Push Model — An Introduction

**Spec sections:** §1.1–1.8 (Introduction, Overview, Scope, Document Purpose, Definitions, Abbreviations)

**Description:**
The opening article sets the stage for the entire series. It explains why SGP.02 exists: the original M2M eSIM standard designed for devices that are not easily reachable — utility meters, automotive telematics, industrial sensors. It introduces the core paradigm of SGP.02: the **"push" model**, where the SM-SR initiates communication with the eUICC rather than the device "pulling" profiles. Key definitions (eUICC, Profile, SM-DP, SM-SR, M2M SP, PLMA) are introduced in context. The article also previews how SGP.02 sits alongside SGP.22 (consumer "pull") and SGP.32 (IoT "pull") in the GSMA eSIM family, establishing the "why M2M needs its own model" narrative.

**Place in the story:** The foundation — readers understand the problem SGP.02 solves and the push-model philosophy before diving into architecture.

---

## Article 2: The SGP.02 Ecosystem — Roles, Actors, and Architecture

**Spec sections:** §2.1 (General Architecture), §1.5 (Definition of Terms for roles)

**Description:**
A walkthrough of Figure 1 — the complete eUICC Remote Provisioning System diagram. Every role is introduced with its responsibilities: the **EUM** (eUICC Manufacturer) who builds the hardware and signs certificates; the **CI** (Certificate Issuer) who is the trust root; the **SM-DP** (Subscription Manager Data Preparation) who prepares and encrypts profiles; the **SM-SR** (Subscription Manager Secure Routing) who owns the OTA channel and manages platform operations; the **Operator** (MNO) who owns profiles and subscriber relationships; and the **M2M SP** (M2M Service Provider) who manages the device fleet but relies on the Operator for connectivity. The interface landscape (ES1 through ES8, ES4A, ESx) is mapped onto the roles, distinguishing off-card interfaces from on-card (eUICC) interfaces.

**Place in the story:** The map — readers learn who does what and how they connect before exploring each component.

---

## Article 3: Inside the eUICC — Security Domains and the ISD-R/ISD-P/ECASD Trio

**Spec sections:** §2.2 (eUICC Architecture), §2.2.1–2.2.8

**Description:**
A deep dive into the eUICC's internal architecture, heavily based on GlobalPlatform Card Specification. Three Security Domains form the backbone: the **ISD-R** (Issuer Security Domain - Root), the sole on-card representative of the SM-SR, responsible for Platform Management; the **ECASD** (eUICC Controlling Authority Security Domain), which holds the eUICC's private key and certificates; and multiple **ISD-P** instances (Issuer Security Domain - Profile), each representing an SM-DP and hosting exactly one Profile. This article covers EID identification, AID/TAR addressing, Profile structure (POL1 within the Profile, POL2 in the ISD-P), secure channel protocols (SCP80/SCP81 for ES5, SCP03 for ES8), the Profile hierarchy (MNO-SD, NAA, file system), Java Card support, and hardware characteristics including discrete vs. integrated eUICC.

**Place in the story:** The engine room — readers understand how the eUICC chip itself organizes and isolates multiple stakeholders.

---

## Article 4: The Certificate Hierarchy — PKI and Trust in SGP.02

**Spec sections:** §2.3 (Security Overview), §2.3.1–2.3.3

**Description:**
A comprehensive treatment of the SGP.02 Public Key Infrastructure. The article traces the three-tier certificate chain: the **CI Root Certificate** (self-signed) → **EUM, SM-DP, SM-SR Certificates** (signed by CI) → **eUICC Certificate** (signed by EUM). It explains the dual certificate format split — X.509 for CI/EUM certificates per SGP.14, and GlobalPlatform Amendment E format for SM-DP/SM-SR/eUICC certificates. Key concepts covered: SubjectKeyIdentifier/AuthorityKeyIdentifier for parent certificate identification, the ECASD key pair (PK.ECASD.ECKA / SK.ECASD.ECKA), Certificate Revocation List (CRL) management and the Operator's informed-decision principle (the SM-DP/SM-SR must not refuse service solely on revoked certificate grounds), and the cryptographic algorithm baseline (AES-128, RSA-3072, ECC-256, SHA-256 for the 2030 horizon).

**Place in the story:** The security backbone — readers understand how trust is established across the remote provisioning ecosystem.

---

## Article 5: OTA Communication — How the SM-SR Reaches the eUICC

**Spec sections:** §2.4 (OTA Communication on ES5), §2.4.1–2.4.5, §2.5, §2.6, §2.7, §2.8

**Description:**
The SM-SR is the only entity that can initiate Over-The-Air communication with the eUICC — that's the essence of the push model. This article details the three transport options on the ES5 interface: **SMS** (including SMS-based HTTPS/CAT_TP session triggering), **HTTPS** (with PSK-TLS authentication, HTTP POST from ISD-R to SM-SR), and **CAT_TP** (Card Application Toolkit Transport Protocol). It covers the PSK-TLS key derivation from the SCP80/SCP81 secure channel, the DNS resolution flow (when the eUICC needs to resolve the SM-SR's FQDN to IP), and how these transports differ in latency, reliability, and power consumption. Brief mention of ES8 (SM-DP↔eUICC, always SCP03-protected), ES6 (Operator OTA platform), ES3 (SM-DP↔SM-SR link establishment), and ES1 (EUM↔SM-SR EIS registration).

**Place in the story:** The plumbing — readers understand the physical communication paths that make remote provisioning possible.

---

## Article 6: Profile Download and Installation — The Heart of Remote Provisioning

**Spec sections:** §3.1 (Profile Download and Installation), §3.1.1–3.1.5

**Description:**
The most critical procedure in SGP.02, broken into its four constituent steps. **Step 1 — ISD-P Creation:** The SM-DP requests the SM-SR (via ES3) to create a new ISD-P on the eUICC, establishing the initial secure channel. **Step 2 — Key Establishment:** The SM-DP and eUICC perform Scenario#3 mutual authentication using the ECASD key pair, establishing SCP03 security with full entity authentication — the SM-DP authenticates via CERT.DP.ECDSA verified against the CI root, and the eUICC authenticates via CERT.ECASD.ECKA verified against the EUM certificate chain. **Step 3 — Profile Download:** The encrypted Profile package (PE) is transported through the SM-SR relay to the ISD-P, decrypted, and installed. **Step 4 — Error Management and Cleanup:** Sub-routines handle failures gracefully, rolling back ISD-P creation when download fails.

**Place in the story:** The main event — readers see how a Profile actually gets onto the chip.

---

## Article 7: Profile Lifecycle — Enabling, Disabling, and Deletion

**Spec sections:** §3.2–3.7, §3.10 (Master Delete)

**Description:**
Once a Profile is downloaded, it enters a lifecycle managed by Platform Management functions. This article covers three core operations with both their Normal Case and Connectivity Failure Case variants: **Enabling** a Profile (making its NAA and files selectable over the UICC-Terminal interface), **Disabling** a Profile (making it unselectable while preserved on-card), and **Deleting** a Profile along with its ISD-P. Each operation can be initiated through three paths: directly by the Operator via ES4, by the Operator via SM-DP (ES2→ES3→ES5 relay), or by the M2M SP via ES4. The article explains the Connectivity Failure Case — what happens when the eUICC can't be reached during the procedure, including the retry and fallback semantics. It also covers the **Master Delete** procedure for complete eUICC wipe.

**Place in the story:** The operational layer — readers learn how Profiles are managed day-to-day after initial provisioning.

---

## Article 8: The SM-SR Change — Migrating Between Subscription Managers

**Spec sections:** §3.8 (SM-SR Change), §3.9 (eUICC Registration), §5.6 (ES7 Interface), §5.6.1–5.6.3

**Description:**
In the M2M world, an Operator or enterprise may need to switch SM-SR providers — e.g., due to contract changes, M&A, or service quality. The SM-SR Change procedure is one of SGP.02's most architecturally significant flows. This article walks through the full handover: the Operator initiates via ES4 (Prepare SM-SR Change, then SM-SR Change); the old SM-SR (SM-SR1) coordinates with the new SM-SR (SM-SR2) via the ES7 interface to create additional key sets and hand over the eUICC Information Set (EIS); the eUICC receives new Platform Management credentials; and all ISD-Ps, Profiles, and state information migrate intact. The article covers the ES7 interface functions: CreateAdditionalKeySet, HandoverEUICC, and AuthenticateSM-SR, as well as the eUICC Registration at the new SM-SR.

**Place in the story:** The escape hatch — readers understand how the ecosystem avoids vendor lock-in.

---

## Article 9: Resilience — Fall-Back Mechanism, Emergency Profiles, and Test Profiles

**Spec sections:** §3.16 (Fall-Back Activation), §3.22–3.31 (Emergency Profile, Test Profile, Fall-Back Attribute Management), §3.30–3.31 (Local Enable/Disable for Emergency)

**Description:**
M2M devices operate in harsh conditions where network connectivity is never guaranteed. SGP.02 provides multiple resilience mechanisms. The **Fall-Back Mechanism** activates automatically when the enabled Profile loses connectivity: the eUICC detects the failure and switches to the Profile with the Fall-Back Attribute set, ensuring the device can reconnect. **Emergency Profiles** comply with regulatory requirements (e.g., eCall in vehicles), providing only emergency calling capability. **Test Profiles** support device manufacturing and testing without consuming operational subscriptions. This article covers the full management cycle for all three: setting/unsetting the Fall-Back and Emergency Profile Attributes via Operator, SM-DP, or M2M SP; the automatic fall-back activation procedure (the eUICC monitoring connectivity and switching); and local enable/disable (ESx interface) that allows the Device to activate emergency or test profiles without network involvement.

**Place in the story:** The safety net — readers understand how M2M devices stay connected in adverse conditions.

---

## Article 10: Policy Rules, POL1/POL2, and Operator Notification Configuration

**Spec sections:** §3.11–3.14 (POL1/POL2 Updates), §3.15 (Default Notification Procedure), §3.21 (ONC), §2.2.4 (Profile Structure — POL1/POL2)

**Description:**
Policy Rules govern what operations are permitted on a Profile and under what conditions. SGP.02 defines two policy storage locations: **POL1** — policy rules embedded within the Profile itself (stored in the ISD-P's file system, read by ISD-R during Platform Management); and **POL2** — policy rules associated with a Profile but stored in the ISD-R for faster access. This article explains the structure of Policy Rules, the distinction between POL1 and POL2, how each is updated (POL1 by Operator via ES4/ES5, POL2 via SM-DP or direct OTA), and the Priority Rules when POL1 and POL2 conflict. The second half covers two notification systems: the **Default Notification Procedure** (SMS and HTTPS variants for notifying the SM-SR of profile state changes) and the **Operator Notification Configuration (ONC)** — a richer, operator-specific notification system that lets MNOs subscribe to status-change events for their profiles (download, enable, disable, delete, PLMA settings).

**Place in the story:** The rulebook — readers understand the governance layer controlling who can do what to a Profile.

---

## Article 11: Off-Card Interfaces — ES1 Through ES7 and the SOAP Binding

**Spec sections:** Chapter 5 (§5.1–5.7), Annex A (Message Mapping), Annex B (SOAP Binding), Annex C (GlobalPlatform Privileges)

**Description:**
This article covers the external communication fabric of the SGP.02 ecosystem — the interfaces between off-card entities. It begins with the **common function patterns** (request-response and notification handler), the shared message structure (header, request/response body, status codes), and common data types. Then each interface is surveyed: **ES1** (EUM↔SM-SR: register EIS, update properties); **ES2** (Operator↔SM-DP: profile ordering, download, enabling, disabling, deletion, auditing, PLMA and ONC management — 25 functions); **ES3** (SM-DP↔SM-SR: the busiest interface — 28 functions for ISD-P creation, profile download relay, enabling, disabling, deletion, connectivity updates, and notification forwarding); **ES4** (Operator/M2M SP↔SM-SR: 23 functions for getting/auditing eUICC information, profile lifecycle, SM-SR change); **ES4A** (Operator↔SM-SR: M2M SP authorisation and ONC); **ES7** (SM-SR↔SM-SR: handover functions). The article also covers the SOAP/HTTPS binding (Annex B) and how GlobalPlatform privileges map to the security domains (Annex C).

**Place in the story:** The API reference — readers get a complete map of every function call in the ecosystem.

---

## Article 12: SGP.02 in Context — Comparing M2M Push, Consumer Pull, and IoT eSIM

**Spec sections:** Cross-document comparison; SGP.02 §1.1–1.3 (scope/purpose), §2.1 (architecture); draws on SGP.22 and SGP.32 external knowledge

**Description:**
The capstone article places SGP.02 in the broader GSMA eSIM landscape. It compares the three architectures across key dimensions:

- **SGP.02 (M2M Push):** SM-SR controls OTA channel; profiles pushed to device; operator-driven model; suitable for unreachable/headless devices; complex ecosystem with separate SM-DP and SM-SR roles.
- **SGP.22 (Consumer Pull):** Device/user initiates profile download via LPA (Local Profile Assistant); SM-DP+ (combined DP+SR); QR-code activation; suitable for smartphones and consumer devices; user-facing.
- **SGP.32 (IoT Pull):** Newer standard bringing the pull model to IoT; IPA (IoT Profile Assistant) replaces LPA for constrained devices; eIM (eSIM IoT Manager) for fleet orchestration; addresses M2M use cases that were previously SGP.02 territory.

The article analyzes the evolution: why SGP.02 was first (M2M was the earliest eSIM use case), why SGP.22 took a different path (consumer UX requirements), and why SGP.32 now offers a modern alternative for many M2M scenarios while SGP.02 remains relevant for deeply embedded, truly unreachable deployments. It concludes with guidance on when to use each standard.

**Place in the story:** The big picture — readers understand where SGP.02 fits, when to use it, and how it shaped the eSIM standards that followed.

---

## Reading Order Recommendation

The articles build progressively:

1. **Foundation:** Articles 1–2 (What SGP.02 is, who the players are)
2. **Internals:** Articles 3–5 (The chip, the PKI, the communication channels)
3. **Procedures:** Articles 6–8 (Profile download, lifecycle, SM-SR change)
4. **Advanced Topics:** Articles 9–10 (Resilience, policy rules)
5. **Interfaces:** Article 11 (The API layer)
6. **Context:** Article 12 (Where SGP.02 sits in the eSIM universe)

A reader can stop after Article 7 and have working knowledge of SGP.02. Articles 8–12 provide the depth needed for implementation or architectural decision-making.
