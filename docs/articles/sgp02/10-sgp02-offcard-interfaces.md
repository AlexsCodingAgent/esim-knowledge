---
description: "Documents all seven SGP.02 off-card interfaces — ES1 through ES7 — covering their functions, message flows, ASN.1 definitions, and the SOAP/HTTP binding for server-to-server communication in the M2M RSP ecosystem."
date: 2026-06-07
layout: default
title: "Off-Card Interfaces: ES1–ES7 and the SOAP Binding"
---

# Off-Card Interfaces: ES1–ES7 and the SOAP Binding

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > Off-Card Interfaces: ES1–ES7 and the SOAP Binding**

If you're implementing an SM-DP, integrating with an SM-SR, or debugging a profile operation that's failing somewhere in the chain, this is the article you'll keep coming back to. The off-card interfaces (ES1 through ES7) are the communication fabric that connects every server-side entity in the SGP.02 ecosystem. Together they carry somewhere north of ninety defined functions, and understanding which entity calls which function on which interface is table stakes for any serious implementation work.

The previous articles have used these interfaces constantly (every Profile Download, every lifecyle command, every notification) but always from the perspective of the procedure. Here we flip the lens: what does each interface look like on its own terms, what's on it, and what's the thinking behind each one?

Chapter 5 of the spec (§5.1–5.7) is the source material, with ASN.1 definitions in Annex A and the SOAP binding in Annex B. The on-card interfaces (ES5, ES6, ES8, ESx) live in Chapter 4 and aren't covered here.

---

## The landscape: six interfaces at a glance

Before diving into function tables, here's the bird's-eye view. Six off-card interfaces, each connecting a specific pair of entities:

| Interface | Between | Purpose | Function Count |
|-----------|---------|---------|---------------|
| **ES1** | EUM → SM-SR | eUICC registration and EIS management | 2 |
| **ES2** | Operator → SM-DP | Profile ordering, lifecycle, audit, PLMA, ONC | 25 |
| **ES3** | SM-DP → SM-SR | Profile operations relay, ISD-P management | 28 |
| **ES4** | Operator/M2M SP → SM-SR | Direct profile lifecycle, SM-SR change, audit | 23 |
| **ES4A** | Operator → SM-SR | M2M SP authorisation (PLMA) and ONC | 4 |
| **ES7** | SM-SR → SM-SR | SM-SR Change handover | 3 |

The SM-SR is the hub: it participates in four of the six interfaces (ES1, ES3, ES4, ES7, plus ES4A). The SM-DP participates in two (ES2, ES3). The Operator touches ES2, ES4, and ES4A. Most functions appear on at least two interfaces; once on ES2 for the SM-DP relay path, and once on ES4 for the direct path. This isn't duplication for its own sake; it's the spec accommodating two different deployment topologies.

---

## Common patterns: what every function call looks like

Every off-card function, regardless of interface, follows one of two communication patterns from §5.1.

### Request-response (§5.1.2)

The caller sends a request and blocks until the response arrives. Used for operations where the caller can't proceed without knowing the outcome: `EnableProfile`, `DeleteProfile`, `DownloadProfile`, and most management functions. The request carries input parameters; the response carries an execution status and output data.

### Notification handler (§5.1.3)

A one-way asynchronous message. The sender fires it off and doesn't wait for a response beyond transport-level acknowledgement. Used for event notifications: `HandleProfileEnabledNotification`, `HandleSMSRChangeNotification`, and the like. In practice, these often trigger cascading updates: the SM-SR receives a notification from the eUICC and fans it out to every interested Operator and M2M SP.

### The message envelope

Every message shares the same structural skeleton, regardless of which function it carries:

- **Header:** Function identifier, caller/sender identification, EID (so the receiver knows which eUICC we're talking about), execution parameters (validity period, retry policy), and correlation IDs for matching responses to requests
- **Body:** Function-specific payload, structured ASN.1 types defined in Annex A
- **Status codes:** Standardised values including `Executed-Success`, `Executed-WithWarning`, `Failed`, and function-specific error codes

If you've ever worked with SOAP or gRPC, this pattern will feel familiar. The header handles routing and correlation; the body carries the domain logic.

---

## ES1: EUM → SM-SR (§5.2)

The simplest interface: two functions, used exactly once per eUICC at manufacturing time and occasionally for metadata updates:

| Function | Direction | Purpose |
|----------|-----------|---------|
| `RegisterEIS` | EUM → SM-SR | Register a new eUICC by submitting its EIS (signed by EUM) |
| `UpdateEISAdditionalProperties` | EUM → SM-SR | Update additional properties in an existing EIS |

ES1 is the eUICC's entry into the ecosystem. The EUM, having manufactured the chip, submits a signed EIS containing the ECASD certificate, ISD-R configuration, and initial metadata. The SM-SR verifies the EUM signature before accepting the record. If this registration fails, the eUICC doesn't exist as far as the RSP infrastructure is concerned: no profiles, no OTA commands, nothing. Two functions, but the whole system depends on them.

---

## ES2: Operator → SM-DP (§5.3)

The Operator's primary workhorse. Twenty-five functions covering the full Profile lifecycle, all routed through the SM-DP:

| Function | Pattern | Purpose |
|----------|---------|---------|
| `GetEUICCInfo` | Request-Response | Retrieve eUICC information from SM-DP records |
| `DownloadProfile` | Request-Response | Order and download a Profile to an eUICC |
| `UpdatePolicyRules` | Request-Response | Update POL2 for a Profile |
| `UpdateEUICCInfo` | Request-Response | Update eUICC information at SM-DP |
| `EnableProfile` | Request-Response | Enable a Profile via SM-DP relay |
| `DisableProfile` | Request-Response | Disable a Profile via SM-DP relay |
| `DeleteProfile` | Request-Response | Delete a Profile via SM-DP relay |
| `HandleProfileDisabledNotification` | Notification | Receive notification of profile disabling |
| `HandleProfileEnabledNotification` | Notification | Receive notification of profile enabling |
| `HandleSMSRChangeNotification` | Notification | Receive notification of SM-SR change |
| `HandleProfileDeletedNotification` | Notification | Receive notification of profile deletion |
| `AuditEUICCInfo` | Request-Response | Audit eUICC information |
| `SetAuthorisationsOfM2MSP` | Request-Response | Set PLMA via SM-DP relay |
| `GetAuthorisationsOfM2MSP` | Request-Response | Retrieve PLMA via SM-DP relay |
| `HandleProfileDownloadedNotification` | Notification | Receive notification of profile download completion |
| `HandleProfilePOL2UpdatedNotification` | Notification | Receive notification of POL2 changes |
| `HandlePLMASettingNotification` | Notification | Receive notification of PLMA changes |
| `SetONC` | Request-Response | Set Operator Notification Configuration |
| `GetONC` | Request-Response | Retrieve Operator Notification Configuration |
| `SetEmergencyProfileAttribute` | Request-Response | Set Emergency Profile Attribute via SM-DP |
| `HandleEmergencyProfileAttributeSetNotification` | Notification | Receive notification of Emergency attribute set |
| `HandleEmergencyProfileAttributeUnsetNotification` | Notification | Receive notification of Emergency attribute unset |
| `SetFallBackAttribute` | Request-Response | Set Fall-Back Attribute via SM-DP |
| `HandleFallBackAttributeSetNotification` | Notification | Receive notification of Fall-Back attribute set |
| `HandleFallBackAttributeUnsetNotification` | Notification | Receive notification of Fall-Back attribute unset |

Notice the split: roughly half are request-response (the Operator wants something done), and half are notification handlers (the Operator wants to know when something happened). The notification handlers are how the Operator stays aware of events it didn't directly trigger: a Profile being disabled by an M2M SP, an SM-SR change completed by a different Operator, a Fall-Back attribute being unset by an emergency procedure.

Profile ordering and Master Delete functions are considered out of scope for ES2; they use pre-existing Operator processes rather than standardised RSP interfaces.

---

## ES3: SM-DP → SM-SR (§5.4)

ES3 is the busiest interface in the spec: 28 functions, and it earns every one of them. It's the SM-DP's channel into the SM-SR for everything Profile-related. Many ES2 functions have a corresponding ES3 function: when the Operator calls `ES2.EnableProfile`, the SM-DP calls `ES3.EnableProfile` on the SM-SR. ES3 isn't a simple pass-through, though; the SM-DP adds cryptographic work (Profile preparation, key establishment) that doesn't exist on the ES2 side.

| Function | Purpose |
|----------|---------|
| `GetEIS` | Retrieve the EIS for an eUICC |
| `CreateISDP` | Request creation of a new ISD-P on the eUICC |
| `EstablishISDPKeySet` | Key establishment for Profile Download |
| `DownloadProfile` | Relay the encrypted profile package |
| `EnableProfile` | Enable a Profile on an eUICC |
| `DisableProfile` | Disable a Profile on an eUICC |
| `DeleteProfile` | Delete a Profile and its ISD-P |
| `UpdatePolicyRules` | Update POL2 for a Profile |
| `UpdateConnectivityParameters` | Update Connectivity Parameters using SCP03 |
| `HandleProfileDisabledNotification` | Forward profile disabled notification to Operator |
| `HandleProfileEnabledNotification` | Forward profile enabled notification to Operator |
| `HandleSMSRChangeNotification` | Forward SM-SR change notification to Operator |
| `HandleProfileDeletedNotification` | Forward profile deleted notification to Operator |
| `HandleProfileDownloadedNotification` | Forward profile downloaded notification |
| `HandleProfilePOL2UpdatedNotification` | Forward POL2 update notification |
| `HandlePLMASettingNotification` | Forward PLMA setting notification |
| `SetEmergencyProfileAttribute` | Relay Emergency attribute set command |
| `HandleEmergencyProfileAttributeSetNotification` | Forward Emergency attribute set notification |
| `HandleEmergencyProfileAttributeUnsetNotification` | Forward Emergency attribute unset notification |
| `SetFallBackAttribute` | Relay Fall-Back attribute set command |
| `HandleFallBackAttributeSetNotification` | Forward Fall-Back attribute set notification |
| `HandleFallBackAttributeUnsetNotification` | Forward Fall-Back attribute unset notification |

Plus ISD-P lifecycle and authorisation management functions rounding out the 28.

If you're building an SM-DP, ES3 is where most of your integration complexity lives. You're not just proxying Operator commands; you're managing ISD-P creation, key establishment, and Profile encryption, all through this single interface.

---

## ES4: Operator/M2M SP → SM-SR (§5.5)

The direct channel. When the Operator has a relationship with the SM-SR (rather than going through an SM-DP), ES4 is the interface they use. Twenty-three functions, and the list mirrors ES2 almost exactly: same operations, different routing:

| Function | Purpose |
|----------|---------|
| `GetEUICCInfo` | Retrieve eUICC information from SM-SR |
| `UpdatePolicyRules` | Update POL2 (ES4A alternative) |
| `UpdateEUICCInfo` | Update eUICC information at SM-SR |
| `AuditEUICCInfo` | Audit eUICC information |
| `EnableProfile` | Direct profile enabling |
| `DisableProfile` | Direct profile disabling |
| `DeleteProfile` | Direct profile deletion |
| `PrepareSMSRChange` | Prepare for SM-SR change (to SM-SR2) |
| `SMSRChange` | Execute SM-SR change (to SM-SR1) |
| `HandleProfileDisabledNotification` | Receive profile disabled notification |
| `HandleProfileEnabledNotification` | Receive profile enabled notification |
| `HandleSMSRChangeNotification` | Receive SM-SR change notification |
| `HandleProfileDeletedNotification` | Receive profile deleted notification |
| `HandleProfileDownloadedNotification` | Receive profile downloaded notification |
| `HandleProfilePOL2UpdatedNotification` | Receive POL2 update notification |
| `HandlePLMASettingNotification` | Receive PLMA setting notification |
| `GetAuthorisationsOfM2MSP` | Retrieve M2M SP authorisations |
| `SetEmergencyProfileAttribute` | Set Emergency Profile Attribute |
| `HandleEmergencyProfileAttributeSetNotification` | Receive Emergency attribute set notification |
| `HandleEmergencyProfileAttributeUnsetNotification` | Receive Emergency attribute unset notification |
| `SetFallBackAttribute` | Set Fall-Back Attribute |
| `HandleFallBackAttributeSetNotification` | Receive Fall-Back attribute set notification |
| `HandleFallBackAttributeUnsetNotification` | Receive Fall-Back attribute unset notification |

The parallel between ES2 and ES4 is deliberate: they support the exact same operations, just through different routing. An Operator with an SM-DP relationship uses ES2; an Operator with a direct SM-SR relationship uses ES4. The functions themselves stay consistent. The two extra functions on ES4 that don't appear on ES2 (`PrepareSMSRChange` and `SMSRChange`) are the SM-SR Change operations. Those can't go through an SM-DP because the SM-DP isn't involved in SM-SR handover.

---

## ES4A: Operator → SM-SR: PLMA and ONC (§5.7)

ES4A is a focused subset of ES4, carved out for two specific concerns:

| Function | Purpose |
|----------|---------|
| `SetPLMA` | Set Profile Lifecycle Management Authorisation |
| `GetPLMA` | Retrieve PLMA configuration |
| `SetONC` | Set Operator Notification Configuration |
| `GetONC` | Retrieve Operator Notification Configuration |

Four functions, two pairs of get/set. PLMA and ONC can also be managed through the ES2+ES3 relay path, but ES4A gives Operators with a direct SM-SR connection a dedicated administrative channel. If you're wondering why this needs its own interface rather than just being part of ES4, the spec separates them because PLMA and ONC are configuration operations, not lifecycle operations. They change policy, not Profile state. Different concern, different interface.

---

## ES7: SM-SR → SM-SR: the handover interface (§5.6)

The smallest interface by function count. The most architecturally significant. ES7 exists for exactly one purpose: SM-SR Change. Three functions, all critical to avoiding vendor lock-in:

| Function | Direction | Purpose |
|----------|-----------|---------|
| `HandoverEUICC` | SM-SR1 → SM-SR2 | Transfer the EIS to the new SM-SR |
| `AuthenticateSM-SR` | SM-SR2 → SM-SR1 | Provide SM-SR2's certificate for eUICC authentication |
| `CreateAdditionalKeySet` | SM-SR2 → SM-SR1 | Provide ephemeral key and signature for KS2 creation |

ES7 is the only inter-SM-SR interface in the spec. Without it, migrating an eUICC between SM-SRs would be impossible; you'd be locked into your original SM-SR vendor for the lifetime of every device. The full change procedure that uses these three functions is covered in Article 7.

---

## Annex B: The SOAP/HTTPS binding

Annex A defines the messages in ASN.1. Annex B defines how they travel over the wire. The binding is normative (implementations must support it for interoperability) though the spec acknowledges that proprietary bindings exist for specific deployment scenarios.

The stack is SOAP v1.2 over HTTPS with mutual TLS authentication. Each function call maps to a SOAP message: the common header elements (function caller, sender ID, EID, validity period) go into the SOAP header, and the function-specific data structures go into the SOAP body. WS-Security provides message-level signing and encryption on top of the transport-level TLS.

Message Exchange Patterns map cleanly: request-response functions use synchronous SOAP request-response MEPs, and notification handlers use one-way MEPs. WS-Addressing headers (`MessageID`, `RelatesTo`, `To`, `From`) handle message routing and correlation: every message gets a unique ID, and responses reference the request they're answering.

The URI structure follows a predictable pattern: `https://<host>/<interface>/<function>`. ES4's `EnableProfile` might resolve to `https://smsr.example.com/es4/EnableProfile`. If you're building a client, the URI convention is stable enough to generate programmatically.

---

## Which interface carries which procedure?

A cross-reference mapping the procedure catalog back to the interfaces that carry them:

| Procedure | Initiation Path | Interfaces Used |
|-----------|----------------|-----------------|
| Profile Download | Operator → SM-DP → SM-SR → eUICC | ES2, ES3, ES5, ES8 |
| Profile Enable (direct) | Operator → SM-SR → eUICC | ES4, ES5 |
| Profile Enable (relay) | Operator → SM-DP → SM-SR → eUICC | ES2, ES3, ES5 |
| Profile Disable | Operator → SM-SR → eUICC | ES4, ES5 |
| Profile Delete | Operator → SM-SR → eUICC | ES4, ES5 |
| SM-SR Change | Operator → SM-SR1/SM-SR2 → eUICC | ES4 (×2), ES7 (×3), ES5 |
| Fall-Back Activation | eUICC autonomous + notification | ES5 (notification only) |
| Emergency/Test Local Enable | Device → eUICC | ESx |
| POL1 Update | Operator → eUICC | ES6 |
| POL2 Update | Operator → SM-DP → SM-SR | ES2, ES3 |

Every on-card operation flows through ES5. Every server-side operation flows through one of the off-card interfaces above. The two domains meet at the SM-SR, which holds keys for both.

---

## 📋 Summary

- Six off-card interfaces carry roughly 90+ defined functions, with the SM-SR at the centre of most of them
- ES3 is the busiest (28 functions); it's where the SM-DP and SM-SR do the real work of Profile management
- ES2 and ES4 provide parallel function sets for the same operations through different routing: relay (via SM-DP) or direct (to SM-SR)
- Every function is either request-response (synchronous, caller blocks) or notification handler (asynchronous, fire-and-forget), sharing a common header+body envelope
- The SOAP/HTTPS binding (Annex B) is the normative transport, with ASN.1 payloads in SOAP bodies, WS-Addressing for correlation, and mutual TLS
- ES7 is the only inter-SM-SR interface: three functions, but they're the only thing standing between you and vendor lock-in
- ES4A carves out PLMA and ONC into their own interface because they're configuration operations, not lifecycle operations

---

<div align="center">

<a href="{{ site.baseurl }}/">🏠 Home</a>

Previous: <a href="09-sgp02-policy-notifications">Policy Rules & Notifications: POL1, POL2, and the Default Notification</a> →
Next: <a href="11-sgp02-comparison">SGP.02 vs SGP.22 vs SGP.32: Push, Pull, and the Evolution of eSIM</a> →

</div>

---

*Based on GSMA SGP.02 v4.2 (07 July 2020), Remote Provisioning Architecture for Embedded UICC Technical Specification, Chapter 5 (§5.1–5.7), Annex A–C*

---

← Previous: [Policy Rules & Notifications: POL1, POL2, and the Default Notification](09-sgp02-policy-notifications) | [Section Index](index) | Next: [SGP.02 vs SGP.22 vs SGP.32: Push, Pull, and the Evolution of eSIM](11-sgp02-comparison) →
