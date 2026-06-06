---
title: "SGP.41 Overview: In-Factory Profile Provisioning"
date: 2026-06-06
---

# SGP.41 Overview: In-Factory Profile Provisioning

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.41 IFPP]({{ site.baseurl }}/docs/articles/sgp41/) > SGP.41 Overview: In-Factory Profile Provisioning**

> **💡 Why this matters:** Traditional eSIM profile provisioning (SGP.22) requires the device to be online: connecting to an SM-DP+ server over the internet for live profile download. But factory floors are often air-gapped, production lines run at blistering speed, and manufacturers don't want to install SAS-certified HSMs just to load a profile. SGP.41 solves all three at once: pre-bound, pre-encrypted profiles that install offline in milliseconds, with no internet, no HSM, and no End User interaction required. This is the specification that makes eSIM work at manufacturing scale.

> **Key takeaways:**
> - SGP.41 defines In-Factory Profile Provisioning (IFPP): loading profiles onto eUICCs during manufacturing, before the device ever reaches an End User
> - The core innovation is the **Bound Profile Package (BPP)** : a profile pre-bound to a specific eUICC at the SM-DPf, delivered to the factory in advance, and installed locally without any network connection
> - Three new architectural elements: **SM-DPf** (Factory SM-DP+), **FPA** (Factory Profile Assistant), and an expanded **Device Manufacturer** role
> - The spec applies equally to Consumer Devices (SGP.21) and IoT Devices (SGP.31) : M2M (SGP.01) is marked FFS (For Future Study)
> - Production lines run offline; security is maintained through one-time keys, pre-encrypted BPPs, and eUICC-resident key material: no HSM needed at the factory
> - SGP.41 v1.0 was published on 28 February 2025, and reuses proven security from SGP.21/SGP.31 wherever possible

The GSMA's SGP.41 specification introduces a new provisioning paradigm: instead of downloading profiles over the air during device setup, profiles are installed right on the factory floor: inside the Device Production Process: before the device is ever boxed, shipped, or powered on by a consumer.

---

## The Problem: Why SGP.22 Doesn't Work in a Factory

SGP.22 (consumer RSP) assumes the device has an internet connection during profile download. The LPA talks to the SM-DP+ over HTTPS, exchanges several round-trips of mutual authentication and key agreement, and finally downloads the Bound Profile Package. This works beautifully for a consumer scanning a QR code on their smartphone: but it fails completely on a factory floor:

- **No internet**: Many factories are intentionally air-gapped for security and intellectual property protection. The production line has no path to the outside world.
- **Latency kills throughput**: SGP.22's multiple round-trips (PrepareDownload, GetEUICCChallenge, AuthenticateServer, LoadBoundProfilePackage) take seconds per device. At 1 million devices per month, that's unacceptable.
- **Security burden**: SGP.22 requires the LPA to manage TLS sessions and authentication. Factory equipment operators don't want to become PKI administrators.
- **No End User to confirm**: SGP.22's User Intent, Confirmation Requests, and Confirmation Code entries are meaningless on an assembly line.

SGP.41 addresses all of these by moving the profile binding and encryption to the SM-DPf *before* the profile ever reaches the factory.

---

## The Core Innovation: Pre-Bound Profiles

The fundamental shift in SGP.41 is the **Bound Profile Package (BPP)**. In SGP.22, the BPP is created dynamically during an online session between the device and SM-DP+. In SGP.41, the BPP is created in advance by the SM-DPf and shipped to the factory as a static asset:

| Aspect | SGP.22 (Consumer) | SGP.41 (IFPP) |
|--------|-------------------|---------------|
| Profile binding | Live, during download | Pre-bound at SM-DPf |
| Network required | Yes (HTTPS to SM-DP+) | No: offline loading |
| Round-trips | Multiple (PrepareDownload, Auth, Load) | Single push through FPA |
| End User involved | Yes (Confirmation Code, User Intent) | No |
| HSM at production site | Not required (LPA manages TLS) | Not required: GENS02 explicitly allows no HSM |
| Factory SAS accreditation | N/A | Optional: GENS01 provides an option without SAS |

The BPP is created when the Device Manufacturer sends eUICC data (certificates, one-time public keys) to the SM-DPf via the `Esbpp` interface. The SM-DPf performs the binding (encrypting the profile to that specific eUICC's one-time key) and returns the BPP. The factory then simply pushes the BPP through the FPA into the eUICC: a single, fast, offline operation.

---

## What SGP.41 Covers (and What It Doesn't)

**In scope** (Section 1.2):

- Reuse of SGP.21, SGP.31, and SGP.01 architectures with minimal impact
- Reuse of established security from those specifications
- Consumer Devices and IoT Devices
- Both Discrete and Integrated eUICCs
- Loading of the first Profile Package onto a fully personalised eUICC

**Out of scope**:

- Loading of the eUICC operating system and individual data (EID, certificates, keys) : that's the Two-Step Personalisation Process (GSMA FS.18) and happens before IFPP
- M2M Devices (SGP.01) : marked FFS
- The internal structure of the Device Manufacturer's factory systems
- The transport between Device Manufacturer and FPA (the `Esfac` interface)

---

## Relationship to SGP.22

SGP.41 is not a replacement for SGP.22: it's a complementary specification for a different phase of the device lifecycle:

- **SGP.22** handles profile provisioning *after* the device has left the factory (in the field, consumer-initiated)
- **SGP.41** handles profile provisioning *during* the Device Production Process (in-factory, manufacturer-initiated)

Both specifications share the same eUICC architecture (ISD-P, ISD-R, ECASD, MNO-SD, CASD), the same profile package format (TCA eUICC Profile Package specification [6]), and the same end-to-end secure channel concept (ES8+ in SGP.22, ES8f in SGP.41). The differences are in *who requests the profile*, *when binding happens*, and *what network connectivity is required*.

---

## Why This Matters for the eSIM Industry

SGP.41 unlocks use cases that SGP.22 alone cannot address:

1. **PC OEMs**: Laptops with eSIM shipped from the factory with a pre-installed bootstrap profile: the user powers on, clicks "Connect," and is immediately online without scanning any QR code.
2. **Automotive**: Cars with eSIM pre-provisioned during assembly. The connectivity works the moment the car rolls off the line: critical for telematics, emergency calling, and over-the-air updates.
3. **IoT at scale**: Millions of smart meters, sensors, and trackers pre-loaded with connectivity before deployment. No field provisioning truck rolls required.
4. **Region-specific configuration**: A two-stage manufacturing process where generic device hardware is built first (manufacturing step), then region-specific profiles are loaded just before shipping (configuration step).

---

## 📋 Summary

- SGP.41 defines In-Factory Profile Provisioning: loading eSIM profiles during manufacturing without internet connectivity, End User interaction, or HSMs at the factory
- The core innovation is pre-bound BPPs created at the SM-DPf and shipped to the factory for offline, single-push installation
- Three new architectural roles: SM-DPf (factory SM-DP+), FPA (Factory Profile Assistant), and Device Manufacturer with expanded profile handling functions
- Applies to Consumer and IoT Devices; M2M is FFS
- Complements SGP.22: SGP.41 for manufacturing, SGP.22 for field provisioning
- Published v1.0, 28 February 2025, reusing security and architecture from SGP.21/SGP.31

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

Next: [The IFPP Architecture: SM-DPf, FPA, and Device Manufacturer]({{ site.baseurl }}/docs/articles/sgp41/48-sgp41-architecture) →

</div>

---

*Based on GSMA SGP.41 v1.0 (28 February 2025) : eSIM In-Factory Profile Provisioning Architecture and Requirements, Sections 1–3*


---

[Section Index](index) | Next: [The IFPP Architecture: SM-DPf, FPA, and Device Manufacturer](48-sgp41-architecture) →


---

[Section Index](index) | Next: [The IFPP Architecture: SM-DPf, FPA, and Device Manufacturer](48-sgp41-architecture) →
