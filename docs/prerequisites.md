---
layout: default
title: "Prerequisites: What You Should Know Before Reading"
description: "This knowledge base dives deep into the GSMA eSIM Remote SIM Provisioning (RSP) ecosystem. The articles assume a working familiarity with a few foundational…"
---

# 📚 Prerequisites: What You Should Know Before Reading

This knowledge base dives deep into the GSMA eSIM Remote SIM Provisioning (RSP) ecosystem. The articles assume a working familiarity with a few foundational topics. If you're new to telecom, smart cards, or public-key cryptography, this page will help you get oriented.

Each section below covers the essentials you'll need, with links to external resources if you want to go deeper.

---

## 1. Basic Networking Concepts

The eSIM ecosystem operates over standard internet and mobile network protocols. You should be comfortable with:

- **TCP/IP** : how devices connect and communicate over the internet. Articles assume you know what an IP address, a port, and a client-server connection are.
- **TLS (Transport Layer Security)** : encrypts communication between two endpoints (e.g., your phone and an SM-DP+ server). eSIM uses TLS extensively, and the security articles discuss certificate-based authentication within TLS sessions.
- **DNS (Domain Name System)** : resolves domain names (like `smdp.example.com`) to IP addresses. The SM-DP+ and SM-DS addresses are DNS names.

> **Want deeper background?**
> - [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/) : friendly introduction to TCP/IP and sockets
> - [How TLS Works](https://tls13.xargs.org/) : animated explanation of every byte in a TLS 1.3 handshake
> - [How DNS Works](https://howdns.works/) : comic-style DNS walkthrough

---

## 2. SIM Cards and UICC

The **UICC (Universal Integrated Circuit Card)** is the smart card that authenticates you to a mobile network. The physical SIM card you slide into a phone is a removable UICC. An **eUICC** (embedded UICC) is the same thing soldered onto a circuit board: the "eSIM chip."

Key concepts:
- A UICC stores your **IMSI** (International Mobile Subscriber Identity) and cryptographic keys that prove you're a paying subscriber.
- The UICC runs a **USIM** (Universal Subscriber Identity Module) application that handles authentication with 4G/5G networks. Older networks used **SIM** (2G) or **CSIM** (CDMA).
- A single UICC can hold multiple operator credentials when it supports Remote SIM Provisioning: that's what "multiple profiles" means.

> **Want deeper background?**
> - [Wikipedia: SIM card](https://en.wikipedia.org/wiki/SIM_card) : covers UICC, USIM, and the evolution of the SIM
> - [GlobalPlatform: What is a Secure Element?](https://globalplatform.org/secure-element/) : overview of tamper-resistant chip technology

---

## 3. Public-Key Cryptography Basics

eSIM security is built on public-key cryptography. You'll encounter these concepts constantly:

- **Key Pairs** : a private key (kept secret, never leaves the chip) and a public key (shared openly). Anything encrypted with the public key can only be decrypted with the private key, and vice versa.
- **Digital Signatures** : cryptographically proving that a message came from a specific entity and hasn't been tampered with. The sender signs with their private key; anyone can verify with the sender's public key.
- **Digital Certificates** : a document that binds a public key to an identity (e.g., "this is the SM-DP+ server operated by Carrier X"). Certificates are signed by a trusted **Certificate Authority (CA)** : in eSIM, that's the **GSMA Certificate Issuer (CI)**.
- **PKI (Public Key Infrastructure)** : the system of CAs, certificates, and revocation lists that makes large-scale trust possible.
- **ECDSA** : Elliptic Curve Digital Signature Algorithm. The specific algorithm used in eSIM (NIST P-256 curve).
- **ECDH** : Elliptic Curve Diffie-Hellman. Key agreement protocol that lets two parties agree on a shared secret over a public channel.
- **Perfect Forward Secrecy (PFS)** : a property where session keys are ephemeral, so compromising a long-term key doesn't expose past sessions.
- **CRL (Certificate Revocation List)** : a list of certificates that have been revoked before their expiry date (e.g., because the private key was compromised).

> **Want deeper background?**
> - [A Gentle Introduction to Public-Key Cryptography](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/) : Cloudflare's accessible explainer
> - [Elliptic Curve Cryptography: A Basic Introduction](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/) : why ECC is used instead of RSA
> - [How Certificate Chains Work](https://letsencrypt.org/how-it-works/) : Let's Encrypt's explanation of certificate hierarchies

---

## 4. Smart Card and Java Card Basics

eUICCs are **Java Card** secure elements. Understanding the smart card model is essential:

- **APDU (Application Protocol Data Unit)** : the command-response protocol used to communicate with smart cards. Every operation on an eUICC: authenticate, store data, delete a profile: happens via APDU commands and responses.
- **Security Domain** : an on-card container with its own keys and access controls. In eSIM, profiles live in **ISD-Ps** (Issuer Security Domains: Profile) and the profile manager is the **ISD-R** (Issuer Security Domain: Root).
- **GlobalPlatform** : the industry standard that defines how security domains, key management, and secure channels work on smart cards. The eUICC operating system follows GlobalPlatform architecture.
- **TLV (Tag-Length-Value)** : the encoding format used extensively in smart card communications. Each data element is tagged with its type, followed by its length, followed by the value itself.
- **SCP03t** : Secure Channel Protocol 03 (tweaked). A GlobalPlatform protocol for establishing encrypted, authenticated channels between an off-card entity and an on-card security domain. Used in `ES8+` between SM-DP+ and ISD-P.

> **Want deeper background?**
> - [GlobalPlatform Card Specification](https://globalplatform.org/specs-library/card-specification/) : the foundational standard for secure chip technology
> - [Java Card Platform Specification](https://www.oracle.com/java/technologies/java-card-tech.html) : how Java runs on smart cards
> - [Smart Card Basics](https://www.smartcardbasics.com/) : introductions to APDUs, file systems, and security

---

## 5. GSMA and the Standards Ecosystem

The eSIM specifications are published by the **GSMA** (GSM Association) : the industry body that represents mobile operators worldwide. eSIM lives within a family of documents called **SGP** (SIM Group Publications):

| Spec | Coverage |
|------|----------|
| **SGP.22** | Consumer eSIM RSP (phones, tablets, wearables) |
| **SGP.31 / SGP.32** | IoT eSIM RSP (sensors, trackers, industrial devices) |
| **SGP.41** | In-Factory Profile Provisioning (pre-loading profiles during manufacturing) |
| **SGP.25** | eUICC Protection Profile (Common Criteria security certification) |
| **SGP.26** | Test Certificates (PKI for development and lab testing) |
| **SGP.29** | EID Definition (the 32-digit eUICC identifier format) |

Key ecosystem terms:
- **SAS (Security Accreditation Scheme)** : GSMA's certification program for secure production facilities. **SAS-UP** certifies eUICC manufacturing sites; **SAS-SM** certifies SM-DP+ and SM-DS operators. Products from non-SAS-certified facilities cannot participate in the production eSIM ecosystem.
- **DLOA (Declaration of Live Operation Approval)** : the formal document issued after a product passes GSMA testing, authorising it for production use.
- **EUM (eUICC Manufacturer)** : the company that fabricates the eUICC chip and installs the initial root of trust (ECASD).
- **CI (Certificate Issuer)** : the GSMA-operated root Certificate Authority that anchors the entire eSIM trust model.

> **Want deeper background?**
> - [GSMA: eSIM](https://www.gsma.com/esim/) : GSMA's official eSIM portal
> - [GSMA SAS Overview](https://www.gsma.com/security/security-accreditation-scheme/) : how the Security Accreditation Scheme works
> - [GSMA SGP Specifications](https://www.gsma.com/esim/specifications/) : the source documents (free with registration)

---

## Still Confused?

Start with the [🧒 Kid-Friendly Versions](/docs/articles/kids/) : they explain every concept with stories, analogies, and zero jargon. Then come back to the main articles.

Check the [Glossary]({{ site.baseurl }}/docs/glossary) for quick definitions of every acronym used in this knowledge base.

---
