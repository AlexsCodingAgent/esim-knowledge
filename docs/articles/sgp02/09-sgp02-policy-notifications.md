---
date: 2026-06-07
layout: default
title: "Policy Rules & Notifications: POL1, POL2, and the Default Notification"
---

# Policy Rules & Notifications: POL1, POL2, and the Default Notification

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > Policy Rules & Notifications: POL1, POL2, and the Default Notification**

> **📚 Prerequisites:** This article builds on the Profile lifecycle operations (Article 7) and the eUICC's internal architecture — particularly the ISD-R's role as policy enforcer and the ISD-P as profile container. Understanding the three initiation paths (Operator, SM-DP relay, M2M SP) helps contextualise how policy rules are updated.

> **💡 Why this matters:** Policy Rules are the governance layer of SGP.02. They determine who can do what to a Profile — and they're enforced at two independent levels, creating a belt-and-suspenders security model. The notification system ensures every stakeholder knows when profile state changes.

> **Key takeaways:**
> - POL1 lives on the eUICC (in the ISD-P) and is enforced by ISD-R during Platform Management
> - POL2 lives on the SM-SR (in the EIS) and is enforced by the SM-SR before issuing commands
> - When POL1 and POL2 conflict, the most restrictive result wins — and both are independently checked
> - The Default Notification procedure uses SMS or HTTPS from the eUICC to the SM-SR after every profile state change
> - ONC (Operator Notification Configuration) lets Operators selectively suppress notifications on a per-Profile-Type basis

---

## Why Two Policy Stores?

SGP.02 splits policy enforcement across two locations — the eUICC and the SM-SR. This isn't redundancy for redundancy's sake. Each location serves a different threat model:

- **POL1 (on-card):** Protects against a compromised or misbehaving SM-SR. Even if the SM-SR issues a delete command, the ISD-R checks POL1 before executing. POL1 is the Profile owner's last line of defence — it lives inside the tamper-resistant chip
- **POL2 (server-side):** Protects against OTA command overhead and enables SM-SR-level policy decisions without contacting the eUICC. The SM-SR can reject a request before wasting OTA resources on a command the eUICC would refuse anyway

This dual enforcement means an attacker would need to compromise both the SM-SR and the eUICC to bypass policy rules — a significantly higher bar.

---

## POL1: On-Card Policy Rules

POL1 resides within the Profile itself, stored in the ISD-P's file system. The ISD-R reads POL1 when processing Platform Management commands (enable, disable, delete). Key characteristics:

**Storage:** POL1 is part of the Profile package downloaded during Profile Installation (§3.1). It's written during the `ES8.StoreMetadata` step.

**Enforcement:** The ISD-R enforces POL1 at the moment of executing each command — not when the command arrives, but when the ISD-P operation is about to occur. This means POL1 is checked even if the command was relayed through multiple entities.

**Update paths:**
- **Operator via ES6** (§3.12): The Operator sends an SCP80-secured SMS with `ES6.UpdatePOL1byMNO` to the MNO-SD within the Profile. The MNO-SD forwards the update to the ISD-P. This is the direct OTA path
- **During Profile Download:** POL1 is set as part of the profile package

**POL1 cannot be updated by:**
- The SM-DP (no ES8 path for POL1 update exists)
- The M2M SP (POL1 is exclusively the Operator's domain)
- The SM-SR (SM-SR only enforces POL2)

**Special case:** If a Profile has the Fall-Back Attribute set AND POL1 contains "Profile deletion is mandatory when disabled," the POL1 deletion rule is ignored for the Fall-Back Profile (SGP.02 §3.16). This prevents the safety net from being automatically destroyed.

---

## POL2: Server-Side Policy Rules

POL2 is stored in the SM-SR's EIS (eUICC Information Set) record, associated with a specific Profile but residing server-side. Key characteristics:

**Enforcement:** The SM-SR checks POL2 before issuing OTA commands. If POL2 says "disable not allowed," the SM-SR rejects the `ES4.DisableProfile` call before any OTA communication occurs — saving bandwidth, power, and time.

**Update paths:**
- **Operator via SM-DP** (§3.11): `ES2.UpdatePolicyRules(POL2)` → SM-DP forwards to SM-SR via `ES3.UpdatePolicyRules`
- **Direct ES4A path** (§3.24): A dedicated POL2 update via ES4A interface (for Operators with direct SM-SR connections)

**POL2 is specified by the Operator even if empty:** The spec states the Operator "SHALL be able to specify the POL2 content even if it contains no rules." This ensures explicit intent — an empty POL2 means "no restrictions," not "undefined behaviour."

**M2M SP and POL2:** The PLMA system explicitly excludes POL2 management — "The management of POL2 cannot be authorised to a M2M SP" (SGP.02 §3.20). POL2 remains exclusively under Operator control.

---

## POL1 vs POL2: The Dual Enforcement Model

The spec explicitly acknowledges that POL1 and POL2 "MAY have different content." When this happens:

| Scenario | What Happens |
|----------|-------------|
| POL1 allows, POL2 denies | SM-SR rejects before OTA — command never reaches eUICC |
| POL1 denies, POL2 allows | SM-SR sends command; ISD-R rejects during enforcement |
| Both allow | Command executes |
| Both deny | SM-SR rejects (POL2 check first) |

The practical result: the most restrictive combination always wins. The SM-SR can't force an operation the eUICC's POL1 prohibits, and the eUICC can't execute an operation the SM-SR's POL2 already blocked.

After disabling, both POL1 and POL2 can independently trigger Profile deletion (if they contain "Profile deletion is mandatory when its state is changed to disabled"). POL1-triggered deletion happens on the eUICC before the notification confirmation. POL2-triggered deletion happens after the notification confirmation, initiated by the SM-SR. This means the same Profile could be deleted twice — and the spec handles this gracefully.

---

## The Default Notification Procedure

Every profile state change — enable, disable, Fall-Back activation — must be communicated back to the SM-SR. The Default Notification Procedure (§3.15) is how the eUICC reports these changes.

### When Notifications Fire

The eUICC sends a notification after:
- **First network attachment** — happens exactly once in the eUICC's lifetime, signalling deployment
- **Profile enabling** (explicit or Fall-Back triggered) — after network attachment with the new Profile
- **Fall-Back Mechanism activation** — confirming the automatic switch

### SMS Notification (§3.15.1)

1. The eUICC detects a profile change or first power-on
2. Sends an MO-SMS containing an SCP80 Command Packet (with cryptographic checksum, no ciphering) using the ISD-R's SCP80 keys
3. Sets counter to `0000000000` and SPI to "No counter available" — this is a special notification mode, not a normal secured command
4. Retries until getting `TR=0` (successful terminal response) from the device
5. Waits for SM-SR confirmation (`ES5.NotificationConfirmation` via MT-SMS)
6. If no confirmation arrives within a configured timeout, retries the entire sequence
7. After exhausting all retries, the eUICC rolls back to the previously Enabled Profile

### HTTPS Notification (§3.15.2)

1. If DNS is configured, the eUICC resolves the SM-SR's FQDN to an IP address
2. Opens a BIP channel using the Enabled Profile's network parameters
3. Performs PSK-TLS handshake with the SM-SR (using ISD-R keys)
4. Sends HTTP POST with `?msg=<hex-encoded notification data>` query parameter
5. SM-SR responds with HTTP 200 containing `ES5.NotificationConfirmation`
6. eUICC processes confirmation (including any follow-up activities like post-disable deletion)
7. Sends a second HTTP POST with the confirmation response
8. SM-SR acknowledges with HTTP 204

### Notification Content

The notification carries: eUICC identification (EID), the currently enabled Profile's ICCID, notification type (first-attach, profile-change-success, fall-back-activated), and device information. The content is identical regardless of transport protocol.

### Notification Confirmation and Follow-Up

The SM-SR's confirmation is not just an ACK — it carries the `ES5.NotificationConfirmation` command, which can trigger follow-up activities on the eUICC. For example, if a Profile was disabled and POL1 requires deletion, the ISD-R performs the deletion after receiving the confirmation, and the eUICC reports the deletion status in its confirmation response.

If the SM-SR receives the notification after the Validity Period of the original function call has expired, it does NOT send a confirmation — and the eUICC treats this as a notification failure.

---

## Operator Notification Configuration (ONC)

The Default Notification ensures the SM-SR always knows about profile state changes. But not every Operator wants every notification. The **Operator Notification Configuration** (ONC, §3.21) lets Operators selectively suppress notifications.

### How ONC Works

An ONC is a combination of:
- **Identifiers:** Operator identity + Profile Type (identifying which Profiles the configuration applies to)
- **Discarded notifications:** A list of notification types the Operator does NOT want to receive

The Operator sets ONC via:
- `ES4A.SetONC` (direct Operator → SM-SR, §3.21.1)
- `ES2.SetONC` → SM-DP → `ES3` relay (§3.21.2)

### Default Behaviour

If no ONC is configured for a given Profile Type, the Operator receives **all notifications** for status changes on its Profiles. ONC is an opt-out system, not an opt-in.

### SM-SR Support is Optional

The SM-SR's support for ONC is optional:
- If supported: SM-SR implements `SetONC`/`GetONC` functions exactly as specified
- If not supported: SM-SR rejects `SetONC` calls and sends all notifications to all Operators (the default behaviour)

---

## PLMA: Authorising the M2M SP

The **Profile Lifecycle Management Authorisation** (PLMA, §3.20) is technically a policy mechanism, though it's not POL1/POL2. PLMA defines what operations an M2M SP can perform and what notifications it can receive on behalf of an Operator's Profiles.

A PLMA is a combination of:
- **Identifiers:** Operator, M2M SP, and Profile Type
- **Authorised actions:** List of operations (enable, disable, delete) and notifications the M2M SP can perform/receive

PLMA is set by the Operator via `ES4A.SetPLMA` (§3.20.1) or via SM-DP relay (§3.20.2). The SM-SR checks PLMA before executing any M2M SP-initiated operation.

Importantly, PLMA can authorise an M2M SP to **unset** attributes (Emergency, Fall-Back) on another Operator's Profile — this is the mechanism that enables Case 2 of Emergency Profile replacement (§3.25).

---

## 📋 Summary

- POL1 (on-card, in ISD-P) and POL2 (server-side, in EIS) form a dual-enforcement policy framework — both must permit an operation for it to succeed
- POL1 is updated exclusively by the Operator via ES6 OTA; POL2 is updated via ES2/ES3 relay
- The most restrictive combination of POL1 + POL2 always wins, with POL2 checked first (saving OTA resources)
- The Default Notification procedure fires after every profile state change using SMS or HTTPS, with SM-SR confirmation required; failure to confirm triggers roll-back
- ONC lets Operators suppress specific notifications on a per-Profile-Type basis — optional SM-SR support
- PLMA governs what M2M SPs can do; POL2 management is explicitly excluded from PLMA scope

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

Previous: [Resilience: Fall-Back Mechanism, Emergency Profiles, and Test Profiles](08-sgp02-resilience) →
Next: [Off-Card Interfaces: ES1–ES7 and the SOAP Binding](10-sgp02-offcard-interfaces) →

</div>

---

*Based on GSMA SGP.02 v4.2 (07 July 2020) — Remote Provisioning Architecture for Embedded UICC Technical Specification, §3.11–3.15, §3.20–3.21, §3.24*


---

← Previous: [Resilience: Fall-Back Mechanism, Emergency Profiles, and Test Profiles](08-sgp02-resilience) | [Section Index](index) | Next: [Off-Card Interfaces: ES1–ES7 and the SOAP Binding](10-sgp02-offcard-interfaces) →
