---
layout: default
title: "eUICC Updates and Profile Content Management: Lifecycle Beyond Download"
date: 2026-06-06
---

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.22 v3.x Unified RSP]({{ site.baseurl }}/docs/articles/sgp22-v3/) > eUICC Updates and Profile Content Management**

# eUICC Updates and Profile Content Management: Lifecycle Beyond Download

> **💡 Why this matters:** Downloading a profile is just the beginning. Over a device's 10+ year lifetime, the eUICC OS needs security patches, profiles need content updates, and operators need to manage metadata remotely — all without physical access to the chip. SGP.22 v3.x introduces three mechanisms that transform the eUICC from a static container into a living, updatable platform.

> **Key takeaways:**
> - v3.x introduces **eUICC Root Public Key Update** — the ability to rotate the chip's foundational key material without replacing the chip
> - **Profile Content Management** allows operators to update profile contents (applets, files, NAAs) post-installation
> - **Remote Management by Operator** adds Metadata Update via ES6 and Pending Operation Alerting
> - These are v3.x exclusives — none exist in v2.x

---

## The Lifecycle Problem

In v2.x, once a profile is downloaded, the operator can manage it via ES6 (Over-The-Air) — but that's limited to operator-service-level updates. The eUICC itself is frozen: its root keys (ECASD), its OS, and its installed profile contents are effectively immutable after manufacturing.

v3.x recognizes that devices live for a decade or more. Over that time:
- Cryptographic standards evolve (quantum-resistant algorithms may be needed)
- Security vulnerabilities are discovered in eUICC OS implementations
- Operators want to push new applets or update existing ones
- Users change devices and need profile portability

---

## eUICC Root Public Key Update (Section 3.10)

The eUICC's root of trust is the ECASD, which holds `PK.CI.ECDSA` — the GSMA Certificate Issuer's public key. This key verifies every entity the eUICC communicates with: SM-DP+, SM-DS, EUM certificates.

**The problem:** If the CI's key is compromised, or if the ecosystem migrates to a new CI (e.g., for post-quantum cryptography), every eUICC in the field needs its root key updated. Without a mechanism for this, all deployed chips become insecure or incompatible.

**The solution:** Section 3.10 defines a procedure where:

1. The current CI signs an update package containing the new root public key
2. The eUICC verifies the package using its existing `PK.CI.ECDSA`
3. Upon successful verification, the new key is installed alongside (or replaces) the old key
4. Multi-CI support means the eUICC can hold keys from both old and new CIs during migration

This is the cryptographic equivalent of a root certificate update in a web browser — it keeps deployed eUICCs secure across decades without physical recall.

---

## Profile Content Management (Section 3.9)

In v2.x, profile contents — applets, file systems, NAAs — are frozen after download. If an operator wants to add a new payment applet or update an ISIM configuration, they'd need to delete and re-download the entire profile.

v3.x adds **Profile Content Management (PCM)**, which allows:

| Operation | Description |
|-----------|-------------|
| **Load** | Install new executable modules (applets) into a profile |
| **Install** | Make loaded modules available for use |
| **Remove** | Uninstall specific modules without affecting the rest of the profile |
| **Update** | Replace a module with a newer version |
| **Lock/Unlock** | Temporarily disable/enable specific modules |

The LPA gains a **PCM role** — an additional LPA function that manages content operations on behalf of the operator. PCM operations are authenticated end-to-end between the operator (or SM-DP+) and the eUICC, with the LPA acting as an untrusted transport — the same security model as profile download.

---

## Remote Management by Operator (Section 3.8)

Two new capabilities extend the existing ES6 OTA channel:

### Metadata Update via ES6

Operators can now update profile metadata — the information displayed to the user (profile name, operator name, icon) — via the ES6 interface. In v2.x, this metadata was set during download and couldn't be changed.

### Pending Operation Alerting

When an operator queues a remote operation (e.g., profile enable, disable, PCM update), the eUICC can now generate a **Pending Operation Alert** that the LPA picks up and surfaces to the user or to the eIM (in IoT contexts). This solves the "silent operation" problem — users aren't surprised by profile changes they didn't initiate.

---

## Version Compatibility

All three mechanisms are **v3.x only**:

| Feature | v2.x | v3.x |
|---------|------|------|
| Root Public Key Update | ❌ | ✅ Section 3.10 |
| Profile Content Management | ❌ | ✅ Section 3.9 |
| Metadata Update via ES6 | ❌ | ✅ Section 3.8.1 |
| Pending Operation Alerting | ❌ | ✅ Section 3.8.2 |

A v2.x eUICC encountering any of these operations would reject them as unsupported. The Feature Support mechanism (see article 55) allows entities to negotiate which lifecycle features are available before attempting them.

---

## 📋 Summary

- **Root Public Key Update** allows deployed eUICCs to receive new CI keys — essential for cryptographic agility across decades-long device lifetimes
- **Profile Content Management** enables granular updates to installed profiles without full re-download
- **Metadata Update and Pending Operation Alerting** give operators and users visibility and control over ongoing profile management
- All three are v3.x exclusives, negotiated via Feature Support during session establishment

---

<div align="center">

← Previous: [Device Change and Profile Recovery: Moving eSIMs Between Devices]({{ site.baseurl }}/docs/articles/sgp22-v3/58-device-change-and-profile-recovery) · [🏠 Home]({{ site.baseurl }}/)

</div>

---

*Based on GSMA SGP.22 v3.1 (01 December 2023), Sections 3.8 — Remote Management by the Operator, 3.9 — Profile Content Management, 3.10 — eUICC Root Public Key Update*
