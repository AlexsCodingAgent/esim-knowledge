---
description: "Explains SGP.02 policy enforcement : the dual POL1/POL2 rule framework, PLMA for operator delegation, the Default Notification mechanism, and how the ONC keeps operators informed of profile lifecycle events."
date: 2026-06-07
layout: default
title: "Policy Rules & Notifications: POL1, POL2, and the Default Notification"
---

# Policy Rules & Notifications: POL1, POL2, and the Default Notification

**[eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > Policy Rules & Notifications: POL1, POL2, and the Default Notification**

You've seen the machinery by now. The eUICC can download Profiles, the SM-SR can push enable/disable commands, the SM-DP can relay operations, and the M2M SP can drive the whole lifecycle on behalf of an Operator. But here's the question that should be nagging at you: *who decides what's actually allowed?*

If an M2M SP sends a `DeleteProfile` command for a Profile owned by Operator A, does anything stop them? If the SM-SR itself gets compromised, can an attacker wipe every eUICC in the field? If a Profile's been disabled for six months, should the device just… hold onto it forever?

These aren't edge cases. They're the kind of conflicts that emerge the moment you hand lifecycle control to multiple parties. And SGP.02's answer is a dual-enforcement policy framework backed by mandatory notifications. It's not the flashiest part of the spec, but it's the part that keeps operators from accidentally (or maliciously) stepping on each other's Profiles.

We're drawing on §3.11–3.15 (POL1/POL2 and Default Notification), §3.20 (PLMA), §3.21 (ONC), and §3.24 (ES4A). If the lifecycle operations from Article 6 feel like second nature at this point, you're in the right place.

---

## Why two policy stores: and why both matter

SGP.02 doesn't store policy in one place. It splits it across the eUICC (POL1) and the SM-SR (POL2). If you're coming from a web-services background, your first instinct might be "that's just redundancy." It's not. The two stores protect against different attackers, and they check at different moments.

**POL1 lives on the chip.** It's stored inside the ISD-P, in the Profile's own file system, and the ISD-R enforces it right before executing any Platform Management command. This means even a fully compromised SM-SR (an attacker with every ES4 credential) can't force a delete or disable that the Profile's owner didn't permit. The last word lives inside tamper-resistant silicon.

**POL2 lives on the server.** It's stored in the SM-SR's EIS record, and the SM-SR checks it *before* constructing an OTA command. If POL2 says "disable not allowed," the request dies at the SM-SR. No OTA bandwidth wasted, no SCP80 packet crafted, no radio awake time burned on a command that was doomed from the start.

An attacker who wants to bypass policy has to own *both* the SM-SR and the eUICC. That's not impossible (nothing in security is) but it's a meaningfully higher bar than either store alone would set.

---

## POL1: The on-card enforcer

POL1 arrives with the Profile. It's part of the Profile package downloaded during installation (§3.1) and gets written during the `ES8.StoreMetadata` step. From that moment on, it lives in the ISD-P's file system, and only one entity can change it: the Operator.

The update path is narrow by design. The Operator sends an SCP80-secured SMS carrying `ES6.UpdatePOL1byMNO` to the MNO-SD inside the Profile, which forwards it to the ISD-P. That's it. No ES8 path exists for POL1 updates, the SM-DP can't touch it, the M2M SP can't touch it, and the SM-SR (the entity that enforces POL2) has no write access to POL1 whatsoever. The Operator retains exclusive control over the last line of defence.

When does the ISD-R check POL1? Not when the command arrives over ES5; but at the moment of execution, when the ISD-P operation is about to happen. This matters because commands can be relayed through multiple entities. An `EnableProfile` might originate from an Operator, pass through an SM-DP, get forwarded by the SM-SR, and arrive at the eUICC as an SCP80 command. The ISD-R doesn't care about the chain of custody. It checks POL1 at the point of impact.

There's one deliberate exception. If a Profile carries the Fall-Back Attribute *and* POL1 says "Profile deletion is mandatory when disabled," the deletion rule is ignored for the Fall-Back Profile (§3.16). You don't want your safety net destroying itself the moment it catches you.

---

## POL2: The server-side gatekeeper

POL2 sits in the SM-SR's EIS, associated with a specific Profile but living entirely server-side. The Operator updates it via `ES2.UpdatePolicyRules` (through the SM-DP, which relays to `ES3`) or directly through the ES4A path (§3.24). The M2M SP is explicitly locked out: the PLMA system says "the management of POL2 cannot be authorised to an M2M SP" (§3.20). POL2 stays under Operator control, full stop.

The spec is unusually explicit about a corner case: the Operator "SHALL be able to specify the POL2 content even if it contains no rules." An empty POL2 isn't undefined behaviour; it's a deliberate declaration that "this Profile has no server-side restrictions." Intentional emptiness is different from the absence of configuration, and the spec makes sure implementations can't conflate the two.

Because POL2 is checked before any OTA command leaves the SM-SR, it acts as an early rejection filter. If the SM-SR knows the eUICC will refuse a command anyway, why spend the airtime? POL2 catches the obvious "no" before the radio even wakes up.

---

## When the two stores disagree

POL1 and POL2 "MAY have different content": the spec's diplomatic way of saying they'll drift apart in the real world. An Operator updates POL1 over ES6 but forgets to update POL2. A relay fails. A configuration tool has a bug. When the two stores say different things:

| Scenario | What Happens |
|----------|-------------|
| POL1 allows, POL2 denies | SM-SR rejects before OTA; command never reaches eUICC |
| POL1 denies, POL2 allows | SM-SR sends command; ISD-R rejects during enforcement |
| Both allow | Command executes |
| Both deny | SM-SR rejects (POL2 checked first) |

The pattern is simple: the most restrictive combination always wins. POL2 gets checked first because it's cheaper (server-side, no OTA), but if POL2 says yes and POL1 says no, the eUICC still has the final veto.

There's an interesting edge case around post-disable deletion. Both POL1 and POL2 can independently contain "Profile deletion is mandatory when its state is changed to disabled." POL1-triggered deletion happens on the eUICC *before* the notification confirmation. POL2-triggered deletion happens *after* confirmation, initiated by the SM-SR. A Profile could get deleted twice; and the spec handles that gracefully.

---

## After every state change: the Default Notification

Every Profile state change (enable, disable, Fall-Back activation) triggers a notification from the eUICC back to the SM-SR. This isn't optional. The Default Notification Procedure (§3.15) is how the ecosystem stays synchronised, and it's one of the few procedures the eUICC initiates autonomously.

Three events fire a notification: the eUICC's first-ever network attachment (happens once, signalling deployment), a Profile being enabled (whether explicitly or by Fall-Back), and Fall-Back activation itself.

The eUICC has two transport options.

**SMS (§3.15.1).** The eUICC sends an MO-SMS containing an SCP80 Command Packet using the ISD-R's SCP80 keys. It sets the counter to `0000000000` and the SPI to "No counter available": this is a special notification-mode signal, not a normal secured command. The eUICC retries until it gets `TR=0` (successful terminal response) from the device, then waits for the SM-SR's confirmation via MT-SMS (`ES5.NotificationConfirmation`). If the confirmation doesn't arrive within a configured timeout, the eUICC retries the whole sequence. After exhausting all retries, it rolls back to the previously enabled Profile. The system would rather undo the state change than proceed without the SM-SR knowing about it.

**HTTPS (§3.15.2).** If DNS is configured, the eUICC resolves the SM-SR's FQDN, opens a BIP channel using the enabled Profile's network parameters, performs a PSK-TLS handshake with the SM-SR (using ISD-R keys), and sends an HTTP POST with `?msg=<hex-encoded notification data>`. The SM-SR responds with HTTP 200 carrying `ES5.NotificationConfirmation`. The eUICC processes the confirmation (including any follow-up activities like post-disable deletion), sends a second POST with the confirmation response, and gets an HTTP 204 acknowledgement.

The notification payload is the same regardless of transport: EID, the currently enabled Profile's ICCID, notification type (first-attach, profile-change-success, fall-back-activated), and device information.

The SM-SR's confirmation isn't just an ACK; it's an `ES5.NotificationConfirmation` command that can trigger follow-up activities on the eUICC. If a Profile was disabled and POL1 requires deletion, the ISD-R performs that deletion after receiving the confirmation, and reports the deletion status in its confirmation response. If the SM-SR receives the notification after the validity period of the original function call has expired, it does *not* send a confirmation; and the eUICC treats that as a notification failure, triggering the retry-and-rollback sequence.

---

## ONC: telling the system to pipe down

The Default Notification ensures the SM-SR always knows about Profile state changes. But not every Operator wants every notification. If you're managing 200,000 smart meters and each one fires a notification on every state transition, that's a lot of noise.

The Operator Notification Configuration (§3.21) lets Operators suppress specific notification types on a per-Profile-Type basis. It's opt-out, not opt-in; if no ONC is configured, you get everything.

An ONC entry combines an Operator identity, a Profile Type (identifying which Profiles the configuration applies to), and a list of notification types to discard. The Operator sets it via `ES4A.SetONC` (direct) or `ES2.SetONC` → SM-DP → `ES3` relay.

SM-SR support for ONC is optional. If the SM-SR doesn't support it, `SetONC` calls get rejected and all notifications flow to all Operators, the safe default.

---

## PLMA: handing the M2M SP the keys (some of them)

The Profile Lifecycle Management Authorisation (§3.20) is technically a policy mechanism, though it's distinct from POL1 and POL2. PLMA defines what an M2M SP can do on behalf of an Operator's Profiles.

A PLMA entry combines Operator identity, M2M SP identity, Profile Type, and a list of authorised actions: which lifecycle operations the M2M SP can perform and which notifications it can receive. The Operator sets it via `ES4A.SetPLMA` (§3.20.1) or via SM-DP relay (§3.20.2), and the SM-SR checks PLMA before executing any M2M SP-initiated operation.

PLMA can authorise an M2M SP to *unset* attributes (Emergency, Fall-Back) on another Operator's Profile. This is the mechanism that enables Case 2 of Emergency Profile replacement (§3.25); one of the few places in the spec where an entity other than the Profile owner can modify Profile attributes. It's a narrow, carefully gated exception, and it exists for a reason: in an emergency, you can't always reach the original Operator.

What PLMA explicitly cannot do: hand over POL2 management. That stays with the Operator, period. PLMA governs what M2M SPs can *do*; POL2 governs what *anyone* can do. Different layers, different owners.

---

## Summary

- POL1 (on-card, in ISD-P) and POL2 (server-side, in EIS) form a belt-and-suspenders policy framework: an attacker has to compromise both the SM-SR and the eUICC to bypass policy
- POL1 is updated exclusively by the Operator via ES6 OTA; POL2 is updated via ES2/ES3 relay or direct ES4A
- When POL1 and POL2 conflict, the most restrictive combination wins; POL2 gets checked first because it's cheaper
- The Default Notification fires after every Profile state change (SMS or HTTPS), and failure to confirm triggers roll-back to the previously enabled Profile
- ONC lets Operators mute specific notification types on a per-Profile-Type basis; SM-SR support is optional, and the default is "send everything"
- PLMA governs what M2M SPs can do on an Operator's behalf; POL2 management is explicitly excluded from PLMA scope

---

<div align="center">

<a href="{{ site.baseurl }}/">Home</a>

Previous: <a href="08-sgp02-resilience">Resilience: Fall-Back Mechanism, Emergency Profiles, and Test Profiles</a> →
Next: <a href="10-sgp02-offcard-interfaces">Off-Card Interfaces: ES1–ES7 and the SOAP Binding</a> →

</div>

---

*Based on GSMA SGP.02 v4.2 (07 July 2020), Remote Provisioning Architecture for Embedded UICC Technical Specification, §3.11–3.15, §3.20–3.21, §3.24*

---

← Previous: [Resilience: Fall-Back Mechanism, Emergency Profiles, and Test Profiles](08-sgp02-resilience) | [Section Index](index) | Next: [Off-Card Interfaces: ES1–ES7 and the SOAP Binding](10-sgp02-offcard-interfaces) →
