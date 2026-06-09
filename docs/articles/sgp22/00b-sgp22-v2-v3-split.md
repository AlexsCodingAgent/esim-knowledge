---
title: "SGP.22 v2.x vs v3.x: The Specification Split Explained"
description: "Explains the GSMA's bifurcation of SGP.22 into parallel v2.x and v3.x tracks — covering the v2.2.2 baseline, the v3.x unified architecture merging consumer and M2M, and what the split means for eUICC procurement and platform planning."
date: 2026-06-06
---

# SGP.22 v2.x vs v3.x: The Specification Split Explained

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.22 Consumer RSP]({{ site.baseurl }}/docs/articles/sgp22/) > SGP.22 v2.x vs v3.x: The Specification Split Explained**

> **💡 Why this matters:** If you're working with eSIM today, you need to know which version of SGP.22 your components target: v2.x or v3.x. The GSMA has bifurcated the consumer RSP specification into two parallel tracks with different architectures, capabilities, and roadmaps. Understanding the split is essential for platform planning, eUICC procurement, and long-term interoperability.

> **Key takeaways:**
> - SGP.22 v2.2.2 (June 2020) was the stable baseline for years: it defined the eSIM ecosystem as we know it
> - Around 2024, the GSMA created a **v3.x track** that merges consumer (SGP.22) and M2M (SGP.02) capabilities into a unified architecture
> - **v2.x** continues as a consumer-focused evolution track; the latest is **v2.7 (24 April 2026)**
> - **v3.x** introduces new capabilities: additional profile package versions, unified notification model, and cross-domain eUICC features
> - Both tracks are actively maintained: v2.x is not "legacy" and v3.x is not a "replacement"

---

## Background: The v2.2.2 Baseline

For nearly four years, **SGP.22 v2.2.2** (05 June 2020) was the definitive consumer RSP specification. Every eSIM-capable smartphone, tablet, and wearable shipped with an eUICC implementing v2.2.2. The architecture: five players (eUICC, SM-DP+, SM-DS, LPA, Operator) across thirteen interfaces: remained stable through this period, while the GSMA focused on building the IoT eSIM ecosystem (SGP.31/SGP.32).

---

## The Split: Why Two Tracks?

Around 2024, the GSMA recognised that the consumer (SGP.22) and M2M (SGP.02) ecosystems shared significant architectural overlap. Both needed profile download, secure channels, and lifecycle management: but they used different protocols, different actors, and different trust models.

Rather than maintaining two entirely separate specification families, the GSMA began work on a **unified specification** : a single RSP Technical Specification that could serve consumer devices, IoT devices, and M2M equipment. This became the **v3.x track**.

However, the consumer eSIM ecosystem was already deeply invested in v2.x. Billions of eUICCs, thousands of SM-DP+ deployments, and countless LPA implementations were built against v2.2.2. A forced migration would be disruptive. So the GSMA decided to maintain **both tracks in parallel**:

| Track | Focus | Latest Version | Status |
|-------|-------|---------------|--------|
| **v2.x** | Consumer RSP (original SGP.22 scope) | v2.7 (April 2026) | Active development |
| **v3.x** | Unified RSP (consumer + M2M/IoT) | v3.2 | Active development |

---

## What v2.7 Added Since v2.2.2

The v2.x track has evolved significantly since 2020. Key additions in versions v2.3 through v2.7 include:

- **Simplified End User confirmation** : streamlined the user interaction flow for profile downloads
- **Removal of mandatory RAT configuration** : the Rules Authorisation Table is now optional, reducing complexity
- **Integrated eUICC support** : mirrored from the IoT specifications (SGP.31/SGP.32), enabling single-chip solutions where the eUICC is integrated into the device SoC
- **LPA accepting TLS cert chains to Public CAs** : the LPA can now verify SM-DP+ TLS certificates signed by public Certificate Authorities (not just GSMA CI), simplifying deployment
- **Optional Brainpool and FRP for TLS** : alternative elliptic curves (Brainpool) and Forward-secure Re-keying Protocol for enhanced cryptographic flexibility
- **Profile download retry on temporary errors** : the SM-DP+ and eUICC can now resume failed downloads without restarting from scratch
- **Optional LPAd support for Profile Download with PPRs on Removable eUICCs** : extends LPAd functionality to removable eUICC form factors with policy enforcement
- **Multiple eUICC Profile support** : eUICCs can declare support for additional profile package versions (laying groundwork for v3.x coexistence)
- **SIMAlliance → TCA cleanup** : all references updated from SIMAlliance to Trusted Connectivity Alliance branding
- **ASN.1 corrections** : numerous fixes to the ASN.1 module definitions
- **Alignment with SGP.21 v2.3 and SGP.29** : cross-specification consistency improvements
- **TLS 1.3 adoption** : mandatory support for TLS 1.3 on all HTTP interfaces (CR27019)
- **eUICC OS Update capability** : new euiccInfo2 bit indicating whether the eUICC supports over-the-air OS updates
- **Bytecode Verification** : applets installed in the eUICC must pass bytecode verification for type safety
- **Test Profile safeguards** : new allow-list checks and security mechanisms to prevent test profiles from being used in production
- **euiccMinimumSecurityLevel** : standardised minimum security level value (set to 12) for cryptographic operations
- **Long-term forward compatibility with SGP.32 tags** : tag allocations aligned to prevent future conflicts with the IoT specification

---

## Key Differences: v2.x vs v3.x

The v2.7 specification itself contains forward-looking references to v3.x that reveal the architectural differences:

### Profile Package Versions

v3.x eUICCs support an `additionalProfilePackageVersions` field in `euiccInfo2`. An eUICC can declare support for profile package versions higher than 2.x: specifically **version 3.1 or higher, and SHOULD contain version 3.2 or higher**. This enables:

- v2.x eUICCs: `profileVersion` = 2.x (e.g., 2.1, 2.7)
- v3.x eUICCs: `profileVersion` = 2.x (backward compatible) PLUS `additionalProfilePackageVersions` = [3.2, ...]

The SM-DP+ selects the appropriate version based on what the eUICC declares.

### Notification Model

v3.2 introduces a `HandleNotification` function with notification check points. Notably, **check point '17' is explicitly aligned between v2.7 and v3.2** : both specifications use the same value for this notification point. This ensures that an SM-DP+ or operator system handling notifications doesn't need to implement completely separate notification handling for v2.x and v3.x profiles.

### Provisioning Profiles

v2.7 contains a forward-looking note: *"Use of Provisioning Profiles for other system services in version 3 of this specification may require modifications of this definition."* This suggests that v3.x will expand the role of Provisioning Profiles beyond bootstrap connectivity: potentially for device management, firmware updates, or other system-level services.

### eUICC Capabilities

v3.2 expects eUICCs that support "version 3.2 or higher" for:
- `ts102241Version` : the ETSI TS 102 241 (Java Card) version supported
- Profile package handling: the uiccCapability field is imported from the TCA specification based on the highest supported version

Several bits in the eUICC capabilities field are **reserved for SGP.22 v3.x** (bits 6-18 and 20-25), indicating planned v3.x-only features that v2.x eUICCs will not implement.

### Scope and Architecture

The fundamental difference is scope:

- **v2.x** targets consumer devices only. The five-player model (eUICC, SM-DP+, SM-DS, LPA, Operator) remains unchanged. The LPA is always present, and the end user is always in the loop.
- **v3.x** unifies consumer and M2M architectures. It incorporates the IoT eSIM model (eIM instead of LPA for some deployments, IPA for IoT Profile Assistant) alongside the consumer LPA model. A single specification covers both push-based (M2M) and pull-based (consumer) provisioning.

---

## Which Track Should You Target?

### Choose v2.x if:
- You're building or maintaining a consumer eSIM device (smartphone, tablet, wearable, laptop)
- Your eUICC vendor ships v2.x firmware
- You need compatibility with the existing global SM-DP+ ecosystem
- You don't need M2M-style push provisioning

### Choose v3.x if:
- You need a single eUICC platform for both consumer and IoT/M2M use cases
- You're deploying managed IoT fleets with eIM-based provisioning
- You need the highest profile package version features
- You want Multiple Enabled Profiles, Push Service, or Device Change

**📂 [Read the full SGP.22 v3.x article series →]({{ site.baseurl }}/docs/articles/sgp22-v3/52-sgp22-v3-overview)** : 8 deep-dive articles covering all v3.x features
- You're future-proofing a new platform that won't ship for 18+ months

### Both tracks in parallel:
- SM-DP+ platforms should plan to support both v2.x and v3.x eUICCs, negotiating the profile package version during mutual authentication
- eUICC manufacturers may offer v2.x-only, v3.x-only, or dual-mode chips
- LPA implementations targeting v2.x will continue to work indefinitely: v2.x is not being deprecated

---

## 📋 Summary

- SGP.22 v2.2.2 (2020) was the stable baseline; the GSMA has since split the specification into parallel v2.x (consumer) and v3.x (unified) tracks
- v2.7 (April 2026) adds significant features: integrated eUICC support, TLS 1.3, profile download retry, multiple profile package versions, bytecode verification, and enhanced test profile security
- v3.x merges consumer and M2M architectures, introduces additional profile package versions, unifies the notification model, and reserves capability bits for future cross-domain features
- Both tracks are actively maintained: choose based on your deployment requirements, not on perceived "freshness"
- The v2.x and v3.x ecosystems will coexist for years; SM-DP+ and eUICC platforms should plan for dual-version support

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp22/00-sgp22-overview">eSIM Remote SIM Provisioning (RSP) : How It Works</a> · <a href="{{ site.baseurl }}/">🏠 Home</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp22/01-rsp-architecture">The eSIM RSP Architecture: Players and Interfaces</a> →

</div>

---

*Based on GSMA SGP.22 v2.7 (24 April 2026), Annex M: Document History, Section 2.2.3: eUICC Capabilities, and cross-references to SGP.22 v3.2*
