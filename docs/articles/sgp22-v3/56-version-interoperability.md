---
layout: default
title: "Version Interoperability: How v2.x and v3.x Coexist"
date: 2026-06-06
---

# Version Interoperability: How v2.x and v3.x Coexist

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.22 v3.x Unified RSP]({{ site.baseurl }}/docs/articles/sgp22-v3/) > Version Interoperability: How v2.x and v3.x Coexist**

> **💡 Why this matters:** The eSIM ecosystem won't flip from v2.x to v3.x overnight. Billions of deployed v2.x eUICCs, thousands of v2.x SM-DP+ servers, and countless v2.x LPA implementations will remain in the field for years. A v3.x device must be able to talk to a v2.x SM-DP+ and SM-DS. A v3.x SM-DP+ must serve both v2.x and v3.x eUICCs. Version interoperability is not an optional feature — it's the foundation that allows the whole ecosystem to evolve without breaking. SGP.22 v3.x bakes this in from day one with explicit version discovery, capability negotiation, and backward-compatible protocol design.

> **Key takeaways:**
> - Version interoperability uses **RSP capability** fields exchanged during Common Mutual Authentication (for device↔server) and **X-Admin-Protocol** HTTP header (for server↔server)
> - The absence of `rspCapability` from a server indicates a **pre-v3 implementation** — the LPA limits itself to v2.x data
> - The eUICC declares its `highestSvn` and `additionalProfilePackageVersions`, allowing the SM-DP+ to select the right profile package version
> - v3.x servers and devices **MUST** handle absent capability fields gracefully — this is the core backward-compatibility contract
> - ES6 (Operator → eUICC) uses protocol/functions corresponding to the eUICC's capabilities as declared in `EUICCInfo2`
> - EShri (HRI Server) has no SVN negotiation — the HRI Server versions its services using different URLs
> - v2.x devices and v3.x devices can coexist on the same SM-DP+ and SM-DS infrastructure

---

## The Interoperability Mechanism

Section 2.11 of SGP.22 v3.1 defines the version interoperability framework. It distinguishes three communication patterns, each with its own negotiation mechanism:

### Device ↔ RSP Server (ES8+, ES9+, ES10a, ES10b, ES11)

For LPA/eUICC to RSP Server communication, the specification provides a **built-in capability indication** mechanism within Common Mutual Authentication (section 3.0.1):

- Each party compliant with **version 3 or higher** includes its `rspCapability` / `lpaRspCapability` / `EuiccRspCapability`
- When `rspCapability` is **absent** from a server, it indicates a party implementing a version **prior to version 3**
- The LPA uses this information to restrict its subsequent ES10 function calls and parameters to what the eUICC and server support

### RSP Server ↔ RSP Server (ES2+, ES12, ES15)

For server-to-server communication, the RSP Server acting as client indicates its **SVN** (Specification Version Number) using the HTTP header `X-Admin-Protocol` (section 6.2). This is the same mechanism used in v2.x — the receiving server checks the SVN and adapts its processing accordingly.

### Device ↔ eUICC (ES10x)

The LPAd determines the eUICC's `highestSvn` using `ES10b.GetEUICCInfo` (section 5.7.8). The LPAd then uses ES10 functions and associated parameters in line with `EuiccRspCapability` for further communication with the eUICC. The eUICC doesn't need to know the LPAd's SVN — it simply operates according to the LPAd's requests.

---

## How a v3.x LPA Talks to a v2.x SM-DP+

This is the most common backward-compatibility scenario: a new v3.x device connecting to an existing v2.x SM-DP+:

1. The LPA initiates Common Mutual Authentication with the SM-DP+
2. The SM-DP+ (v2.x) responds but does **not** include `rspCapability` in its response — because v2.x servers don't know about this field
3. The LPA interprets the **absence** of `rspCapability` as meaning "this is a pre-v3 server"
4. The LPA:
   - Does NOT attempt Push Service registration
   - Does NOT include v3.x-only data elements (tagged `#SupportedFromV3.X.Y#`)
   - Does NOT attempt RPM, Device Change, or any v3.x feature
   - Falls back to v2.x-compatible profile download and event retrieval
5. The LPA still provides `lpaRspCapability` in its requests (the server ignores unknown fields per HTTP/JSON conventions)

The result: the v3.x device operates exactly like a v2.x device when talking to a v2.x server.

---

## How a v3.x SM-DP+ Serves a v2.x eUICC

The reverse scenario: a v3.x SM-DP+ must serve a v2.x eUICC:

1. During Common Mutual Authentication, the eUICC (via the LPA) does not provide `EuiccRspCapability` — v2.x eUICCs don't know about this field
2. The SM-DP+ interprets this as "v2.x eUICC" and:
   - Selects a v2.x-compatible profile package version (e.g., 2.1 or 2.7)
   - Does NOT include RPM Commands in the bound profile package
   - Does NOT attempt Device Change or Profile Recovery operations
   - Does NOT advertise Push Service support (the eUICC can't use it)
3. The SM-DP+ includes `rspCapability=v3.1` in its response, but the v2.x LPA ignores the unknown field

The result: the v3.x SM-DP+ degrades gracefully to v2.x behavior.

---

## Profile Package Version Selection

A v3.x eUICC declares `profileVersion` (the baseline, typically 2.x for backward compatibility) plus `additionalProfilePackageVersions` (e.g., [3.2]). The SM-DP+ selects:

- If the eUICC supports a v3.x package version **and** the profile was built for v3.x → use v3.x package
- If the eUICC only supports v2.x → use the highest common v2.x version
- If there's no overlap → error

This allows eUICC manufacturers to ship chips that support both v2.x and v3.x profile packages, with the SM-DP+ selecting the appropriate version at download time.

---

## ES6: Operator to eUICC

For post-install communication over ES6, the Operator SHALL use the protocol and functions corresponding to the capabilities communicated by the eUICC in `EUICCInfo2` during Profile Download and Installation. This means:

- If the eUICC declared RPM support, the Operator can use RPM-related functions
- If the eUICC did NOT declare RPM support, the Operator must use traditional OTA mechanisms

---

## EShri: The Human-Readable Interface

The EShri interface (to the HRI Server) has **no SVN negotiation**. Instead, the HRI Server versions its services using **different URLs**. This is a pragmatic approach — the HRI Server's web interface can evolve independently, and the Activation Code format determines which URL version the LPA accesses.

---

## What v3.x Servers MUST Support

v3.x servers (SM-DP+, SM-DS) are required to:

- **Include `rspCapability`** in their Common Mutual Authentication responses
- **Gracefully handle the absence** of `EuiccRspCapability` and `lpaRspCapability` from v2.x clients
- **Not reject requests** containing unknown JSON fields (standard HTTP/JSON robustness principle)
- **Select appropriate profile package versions** based on what the eUICC declares

---

## Practical Implications for Deployment

| Scenario | Behaviour |
|----------|-----------|
| v2.x Device + v2.x Server | Standard v2.x operation (no change) |
| v3.x Device + v2.x Server | v3.x device operates in v2.x-compatible mode — no v3 features used |
| v2.x Device + v3.x Server | v3.x server degrades to v2.x compatible responses |
| v3.x Device + v3.x Server | Full v3.x feature set available, negotiated via capability exchange |
| v2.x eUICC + v3.x SM-DP+ downloading profile | SM-DP+ selects v2.x profile package; no RPM commands included |
| v3.x eUICC + v2.x SM-DP+ downloading profile | SM-DP+ selects v2.x profile package (only version it knows) |

---

## Summary

- Version interoperability is built into Common Mutual Authentication via RSP capability fields
- The absence of `rspCapability` means "pre-v3" — both sides adapt accordingly
- Server-to-server uses `X-Admin-Protocol` HTTP header for SVN
- eUICC declares `highestSvn` and `additionalProfilePackageVersions` for profile package selection
- v3.x servers MUST handle absent capability fields gracefully
- The model ensures that v2.x and v3.x devices, eUICCs, and servers coexist without modification

---

<div align="center">

← Previous: [Feature Support: Capability Negotiation in v3.x]({{ site.baseurl }}/docs/articles/sgp22-v3/55-feature-support)

Next: [Remote Profile Management: RPM Initiation, Download, and Execution]({{ site.baseurl }}/docs/articles/sgp22-v3/57-remote-profile-management) →

</div>

---

*Based on GSMA SGP.22 v3.1 (01 December 2023), Section 2.11 — Overview of Version Interoperability, Section 3.0.1 — Common Mutual Authentication Procedure, and Section 6.2 — HTTP Header Fields*


---

← Previous: [Feature Support: Capability Negotiation in v3.x](55-feature-support) | [Section Index](index) | Next: [Remote Profile Management: RPM Initiation, Download, and Execution](57-remote-profile-management) →
