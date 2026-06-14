---
layout: default
title: "eSIM RSP Glossary: All Acronyms and Terms"
description: "Every acronym and technical term used across the eSIM knowledge base, defined in one or two sentences. Use this as a quick reference while reading the articles."
---

# 📖 eSIM RSP Glossary

Every acronym and technical term used across the eSIM knowledge base, defined in one or two sentences. Use this as a quick reference while reading the articles.

---

## Core Architecture

- **eUICC** (embedded UICC) : A tamper-resistant secure element soldered into a device that hosts multiple operator profiles. The "eSIM chip."
- **UICC** (Universal Integrated Circuit Card) : The generic smart card platform for mobile authentication. A removable SIM card is a physical UICC.
- **Profile** : One operator's complete subscription credentials stored inside an eUICC. Functionally equivalent to a single physical SIM card.
- **ISD-P** (Issuer Security Domain: Profile) : A cryptographically isolated container on the eUICC that holds exactly one Profile.
- **ISD-R** (Issuer Security Domain: Root) : The profile manager on the eUICC. Creates and destroys ISD-Ps, enforces profile policy. One per chip.
- **ECASD** (eUICC Controlling Authority Security Domain) : The factory-installed root of trust on the eUICC. Holds the chip's private key, CI public keys, and EUM certificate. Permanent and immutable.
- **MNO-SD** (Mobile Network Operator: Security Domain) : The operator's representative inside an ISD-P, holding OTA keys for post-install profile management.
- **NAA** (Network Access Application) : The on-card application (USIM, ISIM, CSIM) that performs network authentication.
- **USIM** (Universal Subscriber Identity Module) : The 3G/4G/5G network access application on a UICC/eUICC.
- **ISIM** (IP Multimedia Services Identity Module) : The application for IMS/VoLTE authentication on a UICC/eUICC.
- **CSIM** (CDMA Subscriber Identity Module) : The CDMA network access application on a UICC/eUICC.

## RSP Entities

- **SM-DP+** (Subscription Manager: Data Preparation) : The server that builds, encrypts, and delivers Profiles to eUICCs over the air.
- **SM-DS** (Subscription Manager: Discovery Server) : A notification service that tells devices when a Profile is waiting for them at an SM-DP+.
- **LPA** (Local Profile Assistant) : The on-device software that orchestrates eSIM operations: discovery, download, and user interface.
- **LDS** (Local Discovery Service) : The LPA sub-component that polls the SM-DS for pending Profiles.
- **LPD** (Local Profile Download) : The LPA sub-component that handles Profile download from SM-DP+ to eUICC.
- **LUI** (Local User Interface) : The LPA sub-component that provides the user-facing screen for profile management.
- **LPAd** (LPA in Device) : Deployment model where the LPA runs on the device's application processor (typical for smartphones).
- **LPAe** (LPA in eUICC) : Deployment model where the LPA runs on the eUICC itself (common in constrained wearable devices).
- **MNO** (Mobile Network Operator) : The carrier that provides mobile service and manages its Profiles post-install.

## IoT eSIM (SGP.32)

- **eIM** (eSIM IoT Remote Manager) : The remote entity that manages Profiles on IoT device fleets. Replaces the consumer's manual interaction.
- **IPA** (IoT Profile Assistant) : The on-device component for IoT. A stripped-down proxy that relays commands rather than making decisions.
- **IPAd** (IPA in Device) : IoT Profile Assistant running on the IoT device's processor.
- **IPAe** (IPA in eUICC) : IoT Profile Assistant running on the eUICC itself.
- **PSMO** (Profile State Management Operation) : Remote enable, disable, or delete of an IoT Profile via the eIM.
- **eCO** (eIM Configuration Operation) : Adding, updating, removing, or listing eIMs associated with an eUICC.

## In-Factory Provisioning (SGP.41)

- **IFPP** (In-Factory Profile Provisioning) : The process of pre-loading Profiles onto eUICCs during device manufacturing, offline.
- **SM-DPf** (SM-DP for Factory) : A variant SM-DP+ that pre-binds Profiles to eUICCs before the device reaches the factory.
- **FPA** (Factory Profile Assistant) : The factory-floor tool that pushes pre-bound Profile Packages into eUICCs on the production line.
- **BPP** (Bound Profile Package) : A Profile encrypted specifically for one eUICC, delivered as a static asset rather than built live.
- **UPP** (Unbound Profile Package) : A Profile that has NOT been bound to a specific eUICC (intermediate format before binding).
- **PPP** (Protected Profile Package) : A Profile that has been encrypted for transport but not yet bound to a specific eUICC.
- **SBPP** (Signed Bound Profile Package) : A BPP that additionally carries a digital signature from the SM-DPf.

## Cryptography & Security

- **PKI** (Public Key Infrastructure) : The system of certificates, CAs, and revocation lists that underpins eSIM trust.
- **CI** (Certificate Issuer) : The GSMA-operated root Certificate Authority at the top of the eSIM trust chain.
- **EUM** (eUICC Manufacturer) : The company that fabricates eUICCs and installs the initial root of trust (ECASD) in a SAS-UP-certified facility.
- **ECDSA** (Elliptic Curve Digital Signature Algorithm) : The signature algorithm used for mutual authentication in eSIM. NIST P-256 curve.
- **ECDH** (Elliptic Curve Diffie-Hellman) : Ephemeral key agreement protocol providing Perfect Forward Secrecy for session encryption.
- **ECC** (Elliptic Curve Cryptography) : The class of public-key algorithms (including ECDSA and ECDH) used throughout eSIM security.
- **PFS** (Perfect Forward Secrecy) : Security property ensuring session keys are ephemeral; compromising a long-term key won't expose past sessions.
- **CRL** (Certificate Revocation List) : A list of certificates that have been invalidated before their natural expiry date.
- **OCSP** (Online Certificate Status Protocol) : An alternative to CRLs for real-time certificate revocation checking.
- **HSM** (Hardware Security Module) : A tamper-resistant device used by SM-DP+ operators and EUMs to protect private keys and perform cryptographic operations.
- **TOE** (Target of Evaluation) : In Common Criteria certification, the specific product or system being evaluated for security (e.g., an eUICC chip).
- **SCP03t** (Secure Channel Protocol 03, tweaked) : The GlobalPlatform protocol for establishing encrypted, authenticated channels to on-card security domains. Used for `ES8+`.

## Smart Card Concepts

- **APDU** (Application Protocol Data Unit) : The command-response messaging protocol used to communicate with smart cards and eUICCs.
- **TLV** (Tag-Length-Value) : An encoding format where each data element is tagged (type), followed by its length, then its value. Ubiquitous in smart card data.
- **ASN.1** (Abstract Syntax Notation One) : A standardized data description language used to define the structure of eSIM messages and certificates.
- **GlobalPlatform** : The industry standard defining security domain architecture, key management, and secure channel protocols for smart cards.
- **TAR** (Toolkit Application Reference) : An identifier used in OTA messaging to route commands to the correct application on the UICC/eUICC.
- **AID** (Application Identifier) : A unique identifier for an application on a smart card (e.g., USIM, ISIM, SD).
- **ADF** (Application Dedicated File) : A directory in the UICC file system that contains an application and its data files.
- **MF** (Master File) : The root directory of the UICC file system.
- **DF** (Dedicated File) : A subdirectory in the UICC file system, containing child files and/or further DFs.
- **EF** (Elementary File) : A data file in the UICC file system (e.g., IMSI, phonebook, SMS storage).
- **SD** (Security Domain) : An on-card entity with its own cryptographic keys, providing secure channel establishment and application management.

## Identifiers

- **ICCID** (Integrated Circuit Card Identifier) : The unique serial number of a Profile (equivalent to the number printed on a physical SIM).
- **IMSI** (International Mobile Subscriber Identity) : The unique identifier that authenticates a subscriber to the mobile network.
- **EID** (eUICC Identifier) : A 32-digit unique number identifying a specific eUICC chip, used for Profile ordering and discovery.
- **ERHI1** (eUICC Random Host Identifier 1) : A privacy-preserving identifier derived from the EID, used in SM-DS event registration to prevent tracking.

## Network & IoT Technologies

- **OTA** (Over-The-Air) : Remote management of Profiles and applets via SMS, HTTPS, or CoAP. Used for post-install updates.
- **CoAP** (Constrained Application Protocol) : A lightweight HTTP-like protocol over UDP, used in IoT eSIM for low-power, lossy networks.
- **DTLS** (Datagram Transport Layer Security) : TLS for UDP. Provides encryption and authentication for CoAP-based eSIM IoT communications.
- **LwM2M** (Lightweight Machine-to-Machine) : An IoT device management protocol from OMA SpecWorks that commonly transports eSIM operations over CoAP/DTLS.
- **NB-IoT** (Narrowband IoT) : A 3GPP LPWA radio technology for low-bandwidth IoT devices that may lack SMS and TCP/IP.
- **LTE-M** (LTE Machine Type Communication) : A 3GPP LPWA technology offering higher bandwidth than NB-IoT but still constrained vs. full LTE.
- **LPWA** (Low Power Wide Area) : A category of network technologies (NB-IoT, LTE-M, LoRaWAN) designed for battery-powered IoT devices.
- **eDRX** (Extended Discontinuous Reception) : A power-saving feature where IoT devices sleep for extended periods and only wake to check for network messages.
- **PSM** (Power Saving Mode) : A deeper sleep state than eDRX where the device is completely unreachable for hours or days.

## Certification & Testing

- **SAS-UP** (Security Accreditation Scheme: UICC Production) : GSMA certification for eUICC manufacturing facilities, ensuring secure production environments.
- **SAS-SM** (Security Accreditation Scheme: Subscription Management) : GSMA certification for SM-DP+ and SM-DS operational sites.
- **DLOA** (Declaration of Live Operation Approval) : The formal document confirming a product has passed GSMA conformance testing and is approved for production.
- **GSMA** (GSM Association) : The industry body representing mobile operators worldwide, publisher of all SGP specifications.

## Profile Types

- **Operational Profile** : A standard consumer or IoT subscription profile, visible to the user/eIM.
- **Provisioning Profile** : A bootstrap profile providing initial connectivity before the main operational profile is downloaded. Hidden from the end user.
- **Test Profile** : A profile with known keys used for lab development and conformance testing. Only loadable in Device Test Mode.

---

*This glossary covers terms from GSMA SGP.22, SGP.31, SGP.32, SGP.41, SGP.25, SGP.26, SGP.29, SGP.23, SGP.23-1, and SGP.33-3.*

*Looking for the [🏠 Home]({{ site.baseurl }}/)  ·  [📚 Prerequisites]({{ site.baseurl }}/docs/prerequisites)  ·  [🧒 Kid-Friendly Versions]({{ site.baseurl }}/docs/articles/kids/)*
