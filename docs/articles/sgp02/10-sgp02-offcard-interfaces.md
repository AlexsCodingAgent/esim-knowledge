---
date: 2026-06-07
layout: default
title: "Off-Card Interfaces: ES1–ES7 and the SOAP Binding"
---

# Off-Card Interfaces: ES1–ES7 and the SOAP Binding

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > Off-Card Interfaces: ES1–ES7 and the SOAP Binding**

> **📚 Prerequisites:** This is a reference-level article. You should understand the SGP.02 roles (EUM, SM-DP, SM-SR, Operator, M2M SP) from Article 2 and the distinction between off-card and on-card interfaces. All previous articles use these interfaces — this article maps the complete function catalog.

> **💡 Why this matters:** The off-card interfaces are the communication fabric that connects every entity in the SGP.02 ecosystem. Understanding which entity calls which function on which interface is essential for implementation, integration testing, and architectural decision-making.

> **Key takeaways:**
> - Six off-card interfaces (ES1–ES4, ES4A, ES7) carry ~90+ defined functions using shared request-response and notification-handler patterns
> - ES3 (SM-DP ↔ SM-SR) is the busiest interface with 28 functions; ES2 (Operator ↔ SM-DP) follows with 25 functions
> - All off-card messages share a common structure: header (function identifier, caller/sender identification, execution parameters) + body (function-specific data)
> - The SOAP/HTTPS binding (Annex B) maps ASN.1-defined messages (Annex A) to web services transport
> - ES4A is a subset of ES4 dedicated to M2M SP authorisation and Operator Notification Configuration
> - ES7 exists solely for SM-SR Change — only three functions, but among the most security-critical in the spec

---

## The Interface Landscape

SGP.02 Chapter 5 defines the off-card interfaces — the machine-to-machine APIs between server-side entities. These are distinct from the on-card (eUICC) interfaces (ES5, ES6, ES8, ESx) described in Chapter 4.

| Interface | Between | Purpose | Function Count |
|-----------|---------|---------|---------------|
| **ES1** | EUM → SM-SR | eUICC registration and EIS management | 2 |
| **ES2** | Operator → SM-DP | Profile ordering, lifecycle, audit, PLMA, ONC | 25 |
| **ES3** | SM-DP → SM-SR | Profile operations relay, ISD-P management | 28 |
| **ES4** | Operator/M2M SP → SM-SR | Direct profile lifecycle, SM-SR change, audit | 23 |
| **ES4A** | Operator → SM-SR | M2M SP authorisation (PLMA) and ONC | 4 |
| **ES7** | SM-SR → SM-SR | SM-SR Change handover | 3 |

The interfaces form a hub-and-spoke pattern around the SM-SR, which participates in four of the six interfaces (ES1, ES3, ES4, ES7, plus ES4A). The SM-DP participates in two (ES2, ES3). The Operator participates in two (ES2, ES4) plus ES4A.

---

## Common Function Patterns (§5.1)

All off-card functions follow one of two communication patterns:

### Request-Response (§5.1.2)

A synchronous call where the caller sends a request and blocks until receiving a response. Used for operations that must complete before the caller proceeds (e.g., `EnableProfile`, `DeleteProfile`). The request includes input parameters; the response includes an execution status and output data.

### Notification Handler (§5.1.3)

An asynchronous one-way message where the sender informs the receiver of an event. Notifications do not expect a response (beyond transport-level acknowledgement). Used for status change notifications (e.g., `HandleProfileEnabledNotification`, `HandleSMSRChangeNotification`).

### Common Message Structure

Every message, regardless of function, shares the same envelope structure:

- **Header:** Function identifier, caller/sender identification, eUICC identification (EID), execution parameters (validity period, retry policy), and message correlation identifiers
- **Body:** Function-specific input data — structured data types defined in ASN.1 notation (Annex A)
- **Status codes:** Execution status values including `Executed-Success`, `Executed-WithWarning`, `Failed`, and function-specific error codes

---

## ES1: EUM to SM-SR (§5.2)

The simplest interface — only two functions, used during manufacturing and initial provisioning:

| Function | Direction | Purpose |
|----------|-----------|---------|
| `RegisterEIS` | EUM → SM-SR | Register a new eUICC by submitting its EIS (signed by EUM) |
| `UpdateEISAdditionalProperties` | EUM → SM-SR | Update additional properties in an existing EIS |

The EIS registration is the first step in an eUICC's lifecycle. The EUM, having manufactured the chip, submits the signed EIS containing the ECASD certificate, ISD-R configuration, and initial metadata. The SM-SR verifies the EUM signature before accepting.

---

## ES2: Operator to SM-DP (§5.3)

The Operator's primary interface for profile management through the SM-DP. With 25 functions, it covers the full lifecycle:

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

Profile ordering and Master Delete functions on ES2 are considered out of scope — they use pre-existing Operator processes.

---

## ES3: SM-DP to SM-SR (§5.4)

The busiest interface, carrying 28 functions. ES3 serves as the SM-DP's channel to the SM-SR for all Profile and ISD-P operations. Many ES2 functions have a corresponding ES3 function that the SM-DP calls on the SM-SR:

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

Plus ISD-P lifecycle and authorisation management functions.

---

## ES4: Operator/M2M SP to SM-SR (§5.5)

The direct channel to the SM-SR, carrying 23 functions. This is the interface used when the Operator has a direct relationship with the SM-SR (rather than going through an SM-DP):

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

The parallel between ES2 (via SM-DP) and ES4 (direct) function sets is deliberate — they support the same operations through different routing.

---

## ES4A: Operator to SM-SR — PLMA and ONC (§5.7)

ES4A is a subset of ES4 dedicated to two specific concerns:

| Function | Purpose |
|----------|---------|
| `SetPLMA` | Set Profile Lifecycle Management Authorisation |
| `GetPLMA` | Retrieve PLMA configuration |
| `SetONC` | Set Operator Notification Configuration |
| `GetONC` | Retrieve Operator Notification Configuration |

The interface functionally overlaps with ES4 in some areas (PLMA and ONC can also be managed via ES2+ES3 relay), but ES4A provides the dedicated path for Operators with a direct SM-SR relationship.

---

## ES7: SM-SR to SM-SR — The Handover Interface (§5.6)

The smallest interface by function count but arguably the most architecturally significant. ES7 exists exclusively for SM-SR Change, carrying three functions:

| Function | Direction | Purpose |
|----------|-----------|---------|
| `HandoverEUICC` | SM-SR1 → SM-SR2 | Transfer the EIS to the new SM-SR |
| `AuthenticateSM-SR` | SM-SR2 → SM-SR1 | Provide SM-SR2's certificate for eUICC authentication |
| `CreateAdditionalKeySet` | SM-SR2 → SM-SR1 | Provide ephemeral key and signature for KS2 creation |

See Article 8 for the complete SM-SR Change procedure that uses these functions.

---

## Annex B: The SOAP/HTTPS Binding

SGP.02 Annex B defines how the ASN.1 messages from Annex A are transported over SOAP web services. Key points:

- **Transport:** SOAP v1.2 over HTTPS with mutual TLS authentication
- **Message structure:** Each function call maps to a SOAP message with a header (containing function identifier, caller identity, correlation data) and a body (containing the function-specific payload)
- **Header mapping:** The common message header elements (function caller, sender ID, EID, validity period) map into the SOAP header
- **Body mapping:** The function-specific data structures map into the SOAP body
- **Security:** Web Services Security (WS-Security) provides message-level signing and encryption; TLS provides transport-level security
- **MEPs (Message Exchange Patterns):** Request-response functions use a synchronous SOAP request-response MEP; notification handlers use a one-way MEP

The binding is normative — implementations MUST support it for interoperability, though the spec acknowledges proprietary bindings for specific deployment scenarios.

### WS-Addressing

Every SOAP message includes WS-Addressing headers for message routing and correlation:
- `MessageID` uniquely identifies each message
- `RelatesTo` correlates responses to requests
- `To` / `From` identify endpoints

### URI Structure

Each function has a defined URI endpoint following the pattern: `https://<host>/<interface>/<function>`. For example, ES4's `EnableProfile` might map to `https://smsr.example.com/es4/EnableProfile`.

---

## Interface Usage by Procedure

Mapping the full procedure catalog (Articles 6–9) to the interfaces that carry them:

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

---

## 📋 Summary

- Six off-card interfaces carry ~90+ defined functions: ES1 (EUM registration), ES2 (Operator→SM-DP, 25 functions), ES3 (SM-DP→SM-SR, 28 functions), ES4 (Operator/M2M SP→SM-SR, 23 functions), ES4A (PLMA + ONC), and ES7 (SM-SR handover, 3 functions)
- All functions follow one of two patterns: synchronous request-response or asynchronous one-way notification handler
- Common message structure: header (function ID, caller, EID, execution params) + body (function-specific data) + status codes
- ES2 and ES4 provide parallel function sets for the same operations through different routing (via SM-DP relay or direct)
- The SOAP/HTTPS binding (Annex B) maps ASN.1 messages (Annex A) to web services with WS-Addressing, WS-Security, and mutual TLS
- ES7 is the only inter-SM-SR interface — minimal (3 functions) but critical for avoiding vendor lock-in

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

Previous: [Policy Rules & Notifications: POL1, POL2, and the Default Notification](09-sgp02-policy-notifications) →
Next: [SGP.02 vs SGP.22 vs SGP.32: Push, Pull, and the Evolution of eSIM](11-sgp02-comparison) →

</div>

---

*Based on GSMA SGP.02 v4.2 (07 July 2020) — Remote Provisioning Architecture for Embedded UICC Technical Specification, Chapter 5 (§5.1–5.7), Annex A–C*


---

← Previous: [Policy Rules & Notifications: POL1, POL2, and the Default Notification](09-sgp02-policy-notifications) | [Section Index](index) | Next: [SGP.02 vs SGP.22 vs SGP.32: Push, Pull, and the Evolution of eSIM](11-sgp02-comparison) →
