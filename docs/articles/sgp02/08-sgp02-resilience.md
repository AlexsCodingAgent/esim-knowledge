---
description: "Covers SGP.02 resilience mechanisms — the Fall-Back protocol for connectivity loss, Emergency Profiles for life-critical access, and Test Profiles for manufacturing validation — that enable 15-year M2M field deployments."
date: 2026-06-07
layout: default
title: "Resilience: Fall-Back Mechanism, Emergency Profiles, and Test Profiles"
---

# Resilience: Fall-Back Mechanism, Emergency Profiles, and Test Profiles

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > Resilience: Fall-Back Mechanism, Emergency Profiles, and Test Profiles**

A gas meter in a basement. An eCall module in a crashed car. A weather station on a mountain. A water quality sensor in a reservoir. None of these devices will ever see a technician. And all of them need to stay connected for a decade or more, through operator changes, network outages, and hardware degradation.

SGP.02 knew this from the start. The spec bakes in three separate resilience mechanisms, each designed for a different kind of failure. One handles routine connectivity loss. One handles life-or-death emergency access. One handles the entirely mundane problem of testing a device without burning an operational subscription. Together they form the safety net that makes 15-year M2M deployments viable.

This article assumes you understand the Profile lifecycle (Article 6), the ISD-R's role as Platform Manager, and the OTA communication paths over ES5. We'll reference notification procedures and POL1/POL2 rules; Article 9 covers those in full.

---

## "The network is down.": Fall-Back Mechanism

Let's start with the most common failure: the enabled Profile can't connect anymore. Maybe the operator's network went down. Maybe the subscription expired. Maybe a policy rule on the other side of the world flipped a switch the device didn't expect.

Consumer devices solve this with a human. You notice the "No Service" icon, you open Settings, you tap a different eSIM. M2M devices don't have you. They need the eUICC to figure it out on its own.

### The Fall-Back Attribute

At any time, exactly one Profile on the eUICC carries the **Fall-Back Attribute**. It sits there disabled, waiting, usually a minimal, low-cost subscription from a different operator than the primary Profile. Network diversity is the whole point. If Operator A goes down, Operator B probably hasn't.

Setting the Fall-Back Attribute works like any other management operation:
- Operator calls `ES4.SetFallBackAttribute` (§3.27)
- Operator via SM-DP relay: `ES2.SetFallBackAttribute` → `ES3` → `ES5` (§3.28)
- M2M SP via `ES4.SetFallBackAttribute` with PLMA authorisation (§3.29)

When you set it on Profile B, it's automatically unset from Profile A. There's no "unset Fall-Back" function: it's always a transfer, never a removal. Some Profile somewhere always carries the flag.

### What happens when it triggers

The Fall-Back Mechanism is autonomous. No server, no OTA command, no human approval:

1. The ISD-R detects the enabled Profile has lost connectivity. The spec doesn't mandate how; implementations might watch for network registration timeout, repeated attach failure, or a window without successful data transfer
2. The ISD-R disables the failing Profile, **ignoring POL1**. "Disable not allowed"? Doesn't matter. Fall-Back overrides it
3. The ISD-R enables the Profile with the Fall-Back Attribute
4. A UICC Reset REFRESH triggers network attachment with the Fall-Back Profile
5. The eUICC performs the Default Notification procedure, telling the SM-SR what happened
6. The SM-SR updates the EIS and notifies affected Operators

The device is back online before the SM-SR even knows there was a problem. That's the key design choice: switch first, notify second. Don't wait for permission when connectivity is at stake.

### The rules that keep Fall-Back sane

A mechanism this aggressive needs guardrails:

- **Don't override Emergency or Test.** If the currently enabled Profile is the Emergency Profile or a Test Profile, Fall-Back stays quiet until `LocalDisable` is called. You don't want automatic failover pulling a device out of an eCall session or a factory test.
- **POL1 "disable not allowed" creates a pin.** If the previously enabled Profile has this rule, the eUICC can only switch back to *that* Profile, nothing else. The Fall-Back Attribute can't be set on any Profile while this rule is active. Only Master Delete can clear it.
- **No automatic deletion during Fall-Back.** Even if POL1 says "Profile deletion is mandatory when disabled," the eUICC doesn't delete during Fall-Back activation. The spec explicitly prohibits it. Automatic deletion during an emergency switch would be chaos.
- **Optional cancellation.** The spec reserves a notification path for the eUICC to switch back to the previously enabled Profile once connectivity returns. The technical details are out of scope, but the hook is there.

---

## "Someone needs to call 112.": Emergency Profiles

The European Union's eCall regulation changed automotive electronics forever. Every new car sold in the EU must be able to place an emergency call to 112, even without an active commercial subscription. If the primary Profile is disabled, expired, or belongs to an operator with no coverage where the crash happened, the emergency call still has to go through. No exceptions.

Emergency Profiles (§3.25, §3.26) are SGP.02's answer. They provide:

- Emergency calling capability: network access limited to emergency numbers (112, 911, etc.)
- No dependency on an ongoing commercial operator relationship
- Regulatory compliance that survives operator changes, subscription lapses, and SM-SR migrations

### The Emergency Profile Attribute

Like Fall-Back, exactly one Profile can hold the **Emergency Profile Attribute**. Setting it on Profile B unsets it on Profile A. The three-path management pattern applies:

- Operator via `ES4.SetEmergencyProfileAttribute` → `ES5` (§3.25)
- Operator via SM-DP relay: `ES2.SetEmergencyProfileAttribute` → `ES3` → `ES5`
- M2M SP via `ES4.SetEmergencyProfileAttribute` with PLMA authorisation (§3.26)

### Replacing an Emergency Profile isn't free

The spec distinguishes two cases:

**Case 1: First Emergency Profile.** No Emergency Profile exists yet. The Operator sets the attribute on the target Profile. Simple.

**Case 2: Replacement.** An Emergency Profile already exists, owned by Operator1. Operator2 wants to set the attribute on its own Profile. Operator1 has to grant Operator2 PLMA authorisation to unset the attribute from Operator1's Profile. You can't just overwrite someone else's emergency capability.

### Constraints

- A Profile can't hold both Fall-Back and Emergency attributes. Mutually exclusive; they solve different problems and shouldn't be conflated.
- The Emergency Profile Attribute must be set on a Profile that's present and disabled. You enable it when you need it.

---

## "Does this thing even work?": Test Profiles

Not every resilience problem is a crisis. Sometimes you just need to test a device on the factory floor without consuming a production subscription. Test Profiles (§3.22, §3.23) are built for manufacturing, lab validation, and field diagnostics.

A Test Profile carries a special flag and test NAA keys (defined in SGP.01's EUICC23 requirements). It connects to test networks, not production networks. It's not managed through the normal lifecycle path: no SM-SR, no ES4, no OTA. Instead, the Device talks directly to the eUICC over the ESx interface.

---

## The local control channel: ESx

ESx is the direct Device-to-eUICC interface, and it's the only Profile management path that bypasses the SM-SR entirely. The Device (the modem, MCU, or application processor that hosts the eUICC) can switch to Test and Emergency Profiles without touching the network.

### Switching to a Test Profile (§3.22)

The Device calls `ESx.LocalEnableTestProfile`. The eUICC checks:

- The Test Profile exists (valid flag, valid NAA keys)
- The currently enabled Profile is *not* the Emergency Profile (you don't override emergency calling)
- The Test Profile isn't already enabled

Checks pass? The eUICC ignores POL1 of the currently enabled Profile, disables it, enables the Test Profile, fires a REFRESH, and the device attaches. The spec is explicit about what happens next: "Whether the Test Profile provides connectivity to a test network or not, the eUICC will not attempt to enable automatically the previously Enabled Profile." Local enable has no automatic roll-back. You're in test mode until you explicitly leave it.

Switching back is `ESx.LocalDisableTestProfile` (§3.23). The eUICC confirms the Test Profile is enabled, then disables it and re-enables whatever Profile was active before.

### Switching to an Emergency Profile (§3.30)

`ESx.LocalEnableEmergencyProfile` follows the same pattern: verify the Emergency Profile exists and isn't already enabled, override POL1, switch. This is how a vehicle's crash detection system activates eCall without waiting for an OTA command that might never arrive.

Reverting is `ESx.LocalDisableEmergencyProfile` (§3.31), back to the previously enabled Profile.

---

## Managing attributes: the common pattern

Both Fall-Back and Emergency attributes follow the same three-path management pattern as lifecycle operations:

| Operation | Operator (ES4) | Via SM-DP | M2M SP (ES4) |
|-----------|----------------|-----------|--------------|
| Set Emergency Attribute | §3.25 | §3.25 (via SM-DP) | §3.26 |
| Set Fall-Back Attribute | §3.27 | §3.28 | §3.29 |
| Local Enable Test | N/A (ESx) | N/A | N/A |
| Local Disable Test | N/A (ESx) | N/A | N/A |
| Local Enable Emergency | N/A (ESx) | N/A | N/A |
| Local Disable Emergency | N/A (ESx) | N/A | N/A |

For remote operations: requester calls the function, SM-SR relays to eUICC via ES5, eUICC executes, notifications propagate, EIS updates. For local operations: Device calls ESx directly, eUICC executes, no server involvement needed.

---

## How the mechanisms interact

These three systems aren't silos. They overlap in ways the spec carefully defines:

- **Fall-Back and Emergency are mutually exclusive** on the same Profile. Pick one.
- **Fall-Back doesn't activate when Emergency or Test is enabled.** Deliberate local activation always beats automatic failover.
- **"Disable not allowed" in POL1 pins the Fall-Back Mechanism** to only switch back to that specific Profile. It's a one-way door until someone clears the rule.
- **Local Enable/Disable overrides POL1.** The spec says the eUICC "SHALL NOT enforce POL1 of the currently Enabled Profile" during local switches. Local control trumps server-side policy.
- **The Fall-Back Mechanism overrides POL1** for the Profile it's disabling, but not for the Fall-Back Profile it's enabling.

The design philosophy is consistent: the more local and immediate the need, the more the spec allows it to override remote policy. A crashed car needs eCall more than it needs to respect a "disable not allowed" flag.

---

These three mechanisms (Fall-Back, Emergency, and Test) are what make the "embedded" in eUICC mean something. They don't assume network availability. They don't assume a human is nearby. They don't assume the original Operator is still in business. They're designed for a world where the device is on its own, and they give it the tools to stay connected anyway.

### The short version

- SGP.02 provides three resilience mechanisms: Fall-Back Profile (automatic connectivity recovery), Emergency Profile (regulatory emergency access), and Test Profile (manufacturing/testing)
- The Fall-Back Mechanism is fully autonomous: the eUICC detects loss of connectivity, switches profiles without server involvement, and notifies afterwards
- Emergency and Fall-Back attributes use the same three-path management pattern as lifecycle operations (ES4 direct, SM-DP relay, M2M SP)
- Local Enable/Disable via ESx lets the Device switch to Test or Emergency Profiles without network interaction, overriding POL1
- Exactly one Profile can hold each attribute at a time; setting on a new Profile implicitly unsets the previous holder
- The mechanisms are designed for a 10–15 year deployment horizon: no physical access, no human intervention, no single point of failure

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

Previous: [SM-SR Change: Handover, ES7 Interface, and EIS Migration](07-sgp02-sm-sr-change) →
Next: [Policy Rules & Notifications: POL1, POL2, and the Default Notification](09-sgp02-policy-notifications) →

</div>

---

*Based on GSMA SGP.02 v4.2 (07 July 2020), Remote Provisioning Architecture for Embedded UICC Technical Specification, §3.16, §3.22–3.31*


---

← Previous: [SM-SR Change: Handover, ES7 Interface, and EIS Migration](07-sgp02-sm-sr-change) | [Section Index](index) | Next: [Policy Rules & Notifications: POL1, POL2, and the Default Notification](09-sgp02-policy-notifications) →
