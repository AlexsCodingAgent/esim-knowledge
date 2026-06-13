---
description: "Explains capability negotiation in SGP.22 v3.x : the tagged-acronym Feature Support system that lets eUICCs, LPAs, and SM-DP+ servers declare supported features and conditionally include or omit version-specific data elements."
layout: default
title: "Feature Support: Capability Negotiation in v3.x"
date: 2026-06-06
---

# Feature Support: Capability Negotiation in v3.x

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.22 v3.x Unified RSP]({{ site.baseurl }}/docs/articles/sgp22-v3/) > Feature Support: Capability Negotiation in v3.x**

> **💡 Why this matters:** When two parties communicate in the eSIM ecosystem: a device and a server, or two servers: they may implement different versions of SGP.22 with different capabilities. How does an SM-DP+ know whether an eUICC supports Remote Profile Management? How does an LPA know whether to include Push Service data in a request? Without a capability negotiation mechanism, either data gets sent that the receiver doesn't understand (causing errors), or features go unused because the sender doesn't dare try. The Feature Support system in v3.x solves this with a tag-based model that lets every party declare exactly what it supports: and limits messages accordingly.

> **Key takeaways:**
> - Feature Support uses **tagged acronyms** (e.g., `#SupportedFromV3.X.Y#`, `#SupportedForRpmV3.X.Y#`) throughout the specification
> - Each tag marks data elements that were introduced in a specific version, so senders can **conditionally include or omit** them
> - The system covers: version-gated features (`#SupportedFromV3.X.Y#`), version-deprecated features (`#SupportedOnlyBeforeV3.X.Y#`), optional features (RPM, Enterprise, LPA Proxy, Device Change, Event Checking, Push Service, MEP), and mandatory-from features (`#MandatoryFromV3.X.Y#`)
> - At runtime, capability is exchanged via **RSP capability** fields (`EuiccRspCapability`, `lpaRspCapability`, `rspCapability`) during Common Mutual Authentication
> - The absence of `rspCapability` from a party indicates a pre-v3 implementation
> - For server-to-server communication, SVN is indicated via the `X-Admin-Protocol` HTTP header

---

## The Problem: Version Heterogeneity

The eSIM ecosystem contains devices, eUICCs, LPAs, SM-DP+s, and SM-DSs running different versions of SGP.22. An SM-DP+ might be v3.1 while the device's eUICC is v2.7. An LPA might be v3.1 while the SM-DS is v2.2.2. Without a way to discover what each party supports, these mismatches lead to:

- **Errors**: A v3.x SM-DP+ sends an RPM Package to a v2.x eUICC that doesn't understand RPM Commands
- **Wasted bandwidth**: Data elements for unsupported features are transmitted unnecessarily
- **Missed opportunities**: An SM-DP+ avoids using Device Change because it doesn't know whether the eUICC supports it

The Feature Support system addresses all three problems.

---

## The Tag System: Feature Acronyms in the Spec

SGP.22 v3.1 annotates data elements throughout the specification with tags encapsulated in hash symbols. These tags tell implementers (and protocol engines) when a data element applies. Section 1.9 defines the following tag categories:

### Version-Gated Tags

| Tag | Meaning |
|-----|---------|
| `#SupportedFromV2.X.Y#` | Data element introduced in v2.X.Y: available in that version and later |
| `#SupportedOnlyBeforeV3.X.Y#` | Data element used in pre-v3.X.Y versions: SHALL NOT be sent to a receiver indicating v3.X.Y or higher |
| `#SupportedFromV3.X.Y#` | Data element introduced in v3.X.Y: SHALL NOT be sent to a receiver indicating a version lower than v3.X.Y |
| `#MandatoryFromV3.X.Y#` | Data element was optional or undefined pre-v3.X.Y and SHALL always be provided in v3.X.Y or higher |

### Feature-Specific Tags

| Tag | Feature | Description |
|-----|---------|-------------|
| `#SupportedForRpmV3.X.Y#` | Remote Profile Management | RPM commands, RPM Package, RPM result structures |
| `#SupportedForEnterpriseV3.X.Y#` | Enterprise Profiles | Enterprise-specific profile data and rules |
| `#SupportedForLpaProxyV3.X.Y#` | LPA Proxy / Profile Content Management | LPRd, PCMP, PCM session data |
| `#SupportedForDcV3.X.Y#` | Device Change | Device Change configuration, procedures, and data |
| `#SupportedForEventCheckingV3.X.Y#` | Event Checking | Event checking (verifying Event List integrity) |
| `#SupportedForPushServiceV3.X.Y#` | Push Service | Push Token, push registration data |
| `#SupportedForMEPV3.X.Y#` | Multiple Enabled Profiles | MEP mode configuration, eSIM Port data |

### Example: How Tags Work in Practice

In the ASN.1 definitions, you'll see annotations like:

```
RpmPackage ::= SEQUENCE OF RpmCommand -- #SupportedForRpmV3.0.0#
```

This means: the `RpmPackage` data structure only exists when RPM is supported. A sender should only include `RpmPackage` in a message destined for a receiver that has declared RPM support.

For `#MandatoryFromV3.X.Y#`, a field that was optional in v2.x becomes mandatory in v3.x: the receiver can rely on it always being present.

---

## Runtime Capability Exchange

The tag system provides the *static* definition of what features exist. The *runtime* mechanism for discovering capabilities is integrated into the Common Mutual Authentication procedure (section 3.0.1).

### RSP Capability Fields

Three capability fields are exchanged:

| Field | Sent By | Contains |
|-------|---------|----------|
| `EuiccRspCapability` | eUICC (via LPA) | eUICC's supported features: RPM, Enterprise, LPA Proxy, Device Change, Event Checking, Push Service, MEP |
| `lpaRspCapability` | LPAd (to Server) | LPAd's SVN and supported features |
| `rspCapability` | RSP Server (SM-DP+/SM-DS) | Server's SVN, supported features, and optional `supportedPushServices` |

### How Capability Discovered

During Common Mutual Authentication:

1. The eUICC provides its `EuiccRspCapability` in the challenge/authentication flow (via the LPA as intermediary)
2. The RSP Server provides its `rspCapability` in the authentication response
3. The LPAd provides its `lpaRspCapability` in subsequent requests

**Critical rule**: When `rspCapability` is absent from a server, it indicates a party implementing a version **prior to v3.0**. The LPA knows to limit its requests to v2.x-compatible data elements only. Conversely, a v3.x server that doesn't receive `lpaRspCapability` from the LPA treats the device as v2.x.

### For Server-to-Server Communication

On ES2+, ES12, and ES15 interfaces (server-to-server), the RSP Server acting as client indicates its SVN using the HTTP header `X-Admin-Protocol` (section 6.2).

---

## Feature Support in eUICC Info

The eUICC declares its supported features through `euiccInfo2`, which includes bit flags for:

- **rpmSupport** : whether the eUICC supports Remote Profile Management
- **lpaProxySupport** : whether the eUICC supports LPA Proxy
- **enterpriseSupport** : whether the eUICC supports Enterprise Profiles
- **deviceChangeSupport** : whether the eUICC supports Device Change and Profile Recovery
- **pushServiceV3Support** : whether the eUICC supports Push Service

Additionally, `euiccInfo2.additionalProfilePackageVersions` allows an eUICC to declare support for profile package versions beyond the baseline (e.g., v3.2 or higher).

---

## Comparison: v2.x vs v3.x Capability Handling

| Aspect | v2.x | v3.x |
|--------|------|------|
| Version discovery | SVN in HTTP headers | SVN + `rspCapability` in authentication |
| Feature discovery | Implicit (presence of fields) | Explicit (tagged features + capability bits) |
| Conditional data inclusion | Manual implementation | Tags guide conditional serialisation |
| Backward compatibility | Trial and error (errors on unknown fields) | Graceful degradation via capability absence |
| Server-to-server | `X-Admin-Protocol` header | `X-Admin-Protocol` header (unchanged) |
| Feature-specific support bits | None | RPM, Enterprise, LPA Proxy, DC, Event Checking, Push, MEP |

---

## Practical Example: SM-DP+ Deciding What to Send

An SM-DP+ communicating with an eUICC:

1. Receives `EuiccRspCapability` indicating: `rpmSupport=true`, `deviceChangeSupport=false`, no `pushServiceV3Support`
2. Knows it can include RPM Commands in the profile download response
3. Knows it should NOT attempt Device Change operations for this eUICC
4. Knows it should NOT advertise Push Service support (the eUICC can't use it)
5. For any data tagged `#SupportedForRpmV3.0.0#`, it includes them in the message
6. For data tagged `#SupportedForDcV3.0.0#`, it omits them

This prevents errors and keeps messages lean.

---

## Summary

- The Feature Support system uses hash-tagged acronyms to mark version and feature dependencies on data elements
- Seven feature-specific tags cover RPM, Enterprise, LPA Proxy, Device Change, Event Checking, Push Service, and MEP
- Runtime capability is exchanged via `rspCapability` / `EuiccRspCapability` / `lpaRspCapability` during Common Mutual Authentication
- Absence of `rspCapability` from a server means "pre-v3" : limit to v2.x data elements
- Server-to-server communication uses `X-Admin-Protocol` HTTP header for SVN indication
- eUICC capability bits declare feature support explicitly

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp22-v3/54-push-service">Push Service: How eSIMs Get Notified Without Polling</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp22-v3/56-version-interoperability">Version Interoperability: How v2.x and v3.x Coexist</a> →

</div>

---

*Based on GSMA SGP.22 v3.1 (01 December 2023), Section 1.9: Feature Support, Section 3.0.1: Common Mutual Authentication Procedure, and Section 4.3: eUICC Information*


---

← Previous: [Push Service: How eSIMs Get Notified Without Polling](54-push-service) | [Section Index](index) | Next: [Version Interoperability: How v2.x and v3.x Coexist](56-version-interoperability) →
