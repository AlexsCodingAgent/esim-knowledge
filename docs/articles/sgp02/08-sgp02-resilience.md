---
date: 2026-06-07
layout: default
title: "Resilience: Fall-Back Mechanism, Emergency Profiles, and Test Profiles"
---

# Resilience: Fall-Back Mechanism, Emergency Profiles, and Test Profiles

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > Resilience: Fall-Back Mechanism, Emergency Profiles, and Test Profiles**

> **📚 Prerequisites:** You should understand the Profile lifecycle (enable, disable, delete) from Article 7, the eUICC's ISD-R role as Platform Manager, and the OTA communication paths (ES5). The notification procedures and POL1/POL2 policy rules are also referenced — see Article 10 for full treatment.

> **💡 Why this matters:** M2M devices operate in the real world — not a data centre. Network coverage fails. SIM profiles get corrupted. Devices deploy in areas where no technician will ever visit. SGP.02's resilience mechanisms ensure a utility meter in a basement doesn't become e-waste just because one operator's network went down.

> **Key takeaways:**
> - The Fall-Back Mechanism automatically switches to a backup Profile when the enabled Profile loses connectivity — no server involvement required
> - Emergency Profiles satisfy regulatory requirements (e.g., eCall in vehicles) for emergency calling capability regardless of the enabled Profile's state
> - Test Profiles support manufacturing and testing without consuming operational subscriptions
> - Local Enable/Disable (ESx) allows the Device to activate Test and Emergency Profiles without network interaction
> - Fall-Back and Emergency attributes are mutually exclusive on the same Profile; only one Profile can hold each at a time

---

## Why M2M Needs Its Own Resilience Architecture

Consumer eSIM devices (SGP.22) have a human in the loop. If a profile fails, you notice, you go to Settings, you tap to switch. M2M devices have no human. A connected gas meter installed in 2024 might be expected to operate until 2039 — through multiple operator contracts, network technology upgrades, and inevitable service disruptions.

SGP.02 addresses this with three distinct resilience mechanisms, each serving a different failure scenario:

1. **Fall-Back Profile** — automatic connectivity recovery when the active Profile fails
2. **Emergency Profile** — regulatory-mandated emergency access independent of commercial service
3. **Test Profile** — manufacturing and field-test capabilities without impacting operational profiles

---

## Fall-Back Mechanism: The Automatic Safety Net

The Fall-Back Mechanism (§3.16) is the cornerstone of SGP.02 resilience. It answers a simple question: **what happens when the currently enabled Profile can no longer connect?**

### The Fall-Back Attribute

At any given time, exactly one Profile on the eUICC can have the **Fall-Back Attribute** set. This Profile serves as the backup — it's kept in disabled state, ready to be activated when needed. The Fall-Back Profile typically contains a minimal, low-cost subscription from a different operator than the primary Profile(s), ensuring network diversity.

Setting the Fall-Back Attribute is a management operation that can be initiated:
- Directly by the Operator via `ES4.SetFallBackAttribute` (§3.27)
- Via SM-DP relay using `ES2.SetFallBackAttribute` → `ES3` → `ES5` (§3.28)
- By the M2M SP via `ES4.SetFallBackAttribute` with PLMA authorisation (§3.29)

When the Fall-Back Attribute is set on Profile B, it is automatically unset from Profile A (the previous holder). There is no explicit "unset Fall-Back" function — it's always a transfer.

### Activation Procedure

When the Fall-Back Mechanism triggers, the ISD-R acts autonomously:

1. **Trigger:** The currently enabled Profile loses network connectivity. The spec doesn't define the exact detection mechanism — implementations may use network registration timeout, repeated attach failure, or a period without successful data transfer
2. **Override POL1:** The ISD-R disables the currently enabled Profile, **ignoring POL1**. Even if POL1 says "disable not allowed," the ISD-R proceeds
3. **Enable Fall-Back:** The ISD-R enables the Profile with the Fall-Back Attribute set
4. **REFRESH:** A UICC Reset triggers network attachment with the Fall-Back Profile
5. **Notification:** The eUICC performs the Default Notification procedure to inform the SM-SR of the switch
6. **EIS Update:** The SM-SR updates the EIS to reflect the new enabled/disabled states and notifies affected Operators

### Critical Rules

- **Emergency/Test Profile exception:** If the currently enabled Profile is the Emergency Profile or Test Profile, the Fall-Back Mechanism does NOT activate until the `LocalDisable` command is called. This prevents automated roll-back from regulatory or testing states
- **POL1 "disable not allowed":** If the previously enabled Profile has this rule, the eUICC can only switch back to this Profile — no other Profile can be enabled in its place. The Fall-Back Attribute cannot be set on any Profile while this rule is active on the disabled Profile. Only Master Delete can remove it
- **Mandatory deletion rule:** If the previously enabled Profile has "Profile deletion is mandatory when disabled" in POL1, the eUICC does NOT automatically delete it during Fall-Back activation — this is explicitly prohibited by the spec
- **Cancellation (optional):** A mechanism MAY allow the eUICC to switch back to the previously enabled Profile once network connectivity is restored. The technical solution for this is out of scope, but the spec reserves the notification path for it

---

## Emergency Profiles: Regulatory Compliance

Emergency Profiles (§3.25, §3.26) exist to satisfy regulatory requirements — most notably the European Union's eCall regulation, which mandates that vehicles must be able to place emergency calls (to 112) even without an active commercial subscription. An Emergency Profile provides:

- Emergency calling capability (network access limited to emergency numbers)
- No dependency on a commercial operator's ongoing service
- Regulatory compliance independent of the device's primary operator relationship

### Emergency Profile Attribute

Like Fall-Back, exactly one Profile on the eUICC can hold the **Emergency Profile Attribute** at a time. Setting it on Profile B automatically unsets it on Profile A. The attribute is set through:

- Operator via `ES4.SetEmergencyProfileAttribute` → `ES5` (§3.25)
- Operator via SM-DP relay: `ES2.SetEmergencyProfileAttribute` → `ES3` → `ES5`
- M2M SP via `ES4.SetEmergencyProfileAttribute` with PLMA authorisation (§3.26)

### Case 1 vs Case 2

The spec distinguishes two scenarios for setting the Emergency Profile Attribute:

- **Case 1 (First Emergency Profile):** No Emergency Profile exists on the eUICC. The operator simply sets the attribute on the target Profile
- **Case 2 (Replacement):** An Emergency Profile already exists (owned by Operator1). Operator2 wants to set the attribute on its own Profile. This requires Operator1 to grant Operator2 authorisation via PLMA to unset the attribute from Operator1's Profile

### Constraints

- A Profile with the Fall-Back Attribute set **cannot also have** the Emergency Profile Attribute set — these are mutually exclusive
- The Emergency Profile Attribute must be set on a Profile that is present and disabled on the eUICC

---

## Test Profiles: Manufacturing and Lab Use

Test Profiles (§3.22, §3.23) are designed for device manufacturing, testing, and development. They contain known keys and may connect to test networks rather than live production networks. A Test Profile is identified by a special flag and test NAA keys (as defined in SGP.01's EUICC23 requirements).

Test Profiles are not managed through the normal Profile lifecycle — they're activated and deactivated locally through the **ESx interface**, which is the direct Device-to-eUICC interface.

---

## Local Enable/Disable via ESx

The ESx interface (§3.22, §3.23, §3.30, §3.31) enables the Device (the host hardware — the modem, MCU, or application processor) to locally switch to and from Test and Emergency Profiles without any network involvement. This is the only Profile management path that doesn't go through the SM-SR.

### Local Enable for Test Profile (§3.22)

The Device calls `ESx.LocalEnableTestProfile`. The eUICC verifies:
- The Test Profile exists (with valid flag and NAA keys)
- The currently enabled Profile is NOT the Emergency Profile (you can't override emergency calling)
- The Test Profile is not already enabled

If checks pass, the eUICC ignores POL1 of the currently enabled Profile, disables it, enables the Test Profile, sends a REFRESH, and the device attaches. Critically, the spec notes: "Whether the Test Profile provides connectivity to a test network or not, the eUICC will not attempt to enable automatically the previously Enabled Profile. This is in contrast to the remote enable procedures."

### Local Disable for Test Profile (§3.23)

`ESx.LocalDisableTestProfile` verifies the currently enabled Profile is indeed the Test Profile, then disables the Test Profile and re-enables the previously Enabled Profile (the one that was active before the test session).

### Local Enable for Emergency Profile (§3.30)

`ESx.LocalEnableEmergencyProfile` follows the same pattern: verify the Emergency Profile exists, verify it's not already enabled, then override POL1 and switch to it. This is how a vehicle's crash detection system activates eCall without waiting for an OTA command.

### Local Disable for Emergency Profile (§3.31)

`ESx.LocalDisableEmergencyProfile` reverts from the Emergency Profile back to the previously Enabled Profile.

---

## Attribute Management Architecture

Both Fall-Back and Emergency attributes follow a common management pattern across three initiation paths:

| Operation | Operator (ES4) | Via SM-DP | M2M SP (ES4) |
|-----------|----------------|-----------|--------------|
| Set Emergency Attribute | §3.25 | §3.25 (via SM-DP) | §3.26 |
| Set Fall-Back Attribute | §3.27 | §3.28 | §3.29 |
| Local Enable Test | N/A (ESx) | N/A | N/A |
| Local Disable Test | N/A (ESx) | N/A | N/A |
| Local Enable Emergency | N/A (ESx) | N/A | N/A |
| Local Disable Emergency | N/A (ESx) | N/A | N/A |

The pattern is always the same: the requester calls the appropriate function, the SM-SR relays the command to the eUICC via ES5 (for remote operations) or the Device calls directly via ESx (for local operations), the eUICC performs the attribute change, notifications propagate to affected parties, and the EIS is updated.

---

## Interaction Between Resilience Mechanisms

These mechanisms don't operate in isolation — they interact in specific ways defined by the spec:

- **Fall-Back and Emergency are mutually exclusive** on the same Profile
- **Fall-Back doesn't activate when Emergency or Test Profile is enabled** — deliberate local activation takes priority over automatic fall-back
- **A disabled Profile with "disable not allowed" in POL1 forces the Fall-Back Mechanism to switch back only to that Profile** — it's effectively pinned
- **Local Enable/Disable overrides POL1** — the eUICC "SHALL NOT enforce POL1 of the currently Enabled Profile" during local switches
- **The Fall-Back Mechanism overrides POL1** for the Profile being disabled (but not for the Profile being enabled — that would be the Fall-Back Profile)

---

## 📋 Summary

- SGP.02 provides three resilience mechanisms: Fall-Back Profile (automatic connectivity recovery), Emergency Profile (regulatory emergency access), and Test Profile (manufacturing/testing)
- The Fall-Back Mechanism is fully autonomous — the eUICC detects loss of connectivity and switches profiles without server involvement, then notifies the SM-SR afterwards
- Emergency and Fall-Back attributes are managed through the same three-path pattern as lifecycle operations (ES4 direct, SM-DP relay, M2M SP)
- Local Enable/Disable via ESx allows the Device to switch to Test or Emergency Profiles without network interaction, overriding POL1
- Exactly one Profile can hold each attribute (Fall-Back, Emergency); setting one on a new Profile implicitly unsets it on the previous holder
- The mechanisms are designed for a 10–15 year deployment horizon — no physical access, no human intervention

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

Previous: [SM-SR Change: Handover, ES7 Interface, and EIS Migration](07-sgp02-sm-sr-change) →
Next: [Policy Rules & Notifications: POL1, POL2, and the Default Notification](09-sgp02-policy-notifications) →

</div>

---

*Based on GSMA SGP.02 v4.2 (07 July 2020) — Remote Provisioning Architecture for Embedded UICC Technical Specification, §3.16, §3.22–3.31*


---

← Previous: [SM-SR Change: Handover, ES7 Interface, and EIS Migration](07-sgp02-sm-sr-change) | [Section Index](index) | Next: [Policy Rules & Notifications: POL1, POL2, and the Default Notification](09-sgp02-policy-notifications) →
