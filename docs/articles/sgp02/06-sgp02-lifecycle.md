---
description: "Covers the SGP.02 profile lifecycle — enable, disable, delete, and master delete operations across three initiation paths (Operator ES4, SM-DP relay, M2M SP), with normal-case and connectivity-failure handling patterns."
date: 2026-06-07
layout: default
title: "Profile Lifecycle: Enable, Disable, Delete, and Fall-Back"
---

# Profile Lifecycle: Enable, Disable, Delete, and Fall-Back

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > Profile Lifecycle: Enable, Disable, Delete, and Fall-Back**

You've downloaded a Profile onto an eUICC inside a sealed water meter. It's sitting there, disabled, waiting. Now the real work begins: this Profile will be enabled, disabled, maybe deleted, and possibly resurrected through Fall-Back, all over the course of a deployment that might outlast the careers of the engineers who provisioned it.

Nobody's going to unscrew that meter to swap a SIM. Every operation happens remotely, through an OTA channel the SM-SR owns. And every operation follows a pattern the spec repeats with almost obsessive consistency: Normal Case, Connectivity Failure Case, roll-back. Get used to that pattern; SGP.02 never stops thinking about what happens when things go wrong.

Before we dive in: this article assumes you understand the SGP.02 architecture (roles, interfaces), the eUICC's internal security domain structure (ISD-R, ISD-P, ECASD), and how a Profile gets downloaded. Articles 1–5 cover those foundations.

---

## Who can do what and how they reach the eUICC

Not everyone who wants to toggle a Profile has a direct line to the SM-SR. SGP.02 defines three initiation paths, and which one you use depends on who you are and what relationship you have with the infrastructure.

**Path 1: Operator via ES4 (direct SM-SR).** The Operator calls `ES4.EnableProfile` (or Disable, or Delete). The SM-SR receives it, checks its policies, and forwards the command to the eUICC over ES5. This is the straightforward case: one call, one intermediary. It's how a full-service MNO managing its own fleet typically works.

**Path 2: Operator via SM-DP relay (ES2 → ES3 → ES5).** Some Operators interact primarily with their SM-DP: the same entity that prepared the Profile in the first place. In this path, the Operator calls the SM-DP (ES2), which relays the request to the SM-SR (ES3), which then contacts the eUICC (ES5). The SM-DP acts as a translator between the profile-preparation world and the lifecycle-management world.

**Path 3: M2M SP via ES4.** Fleet managers and enterprise customers don't always want to call the Operator every time they need a profile change. With prior authorisation from the Profile-owning Operator (granted via PLMA; see Article 9), an M2M Service Provider can call the SM-SR directly through ES4. The utility company managing thousands of meters gets to drive, while the mobile operator retains veto power through policy rules.

All three paths converge at the eUICC: the ISD-R receives the command via ES5 (SMS, HTTPS, or CAT_TP), checks POL1, executes the operation, and notifies the SM-SR. The path that got the command there doesn't change what happens on the card.

| Operation | Operator (ES4) | Operator via SM-DP (ES2→ES3→ES5) | M2M SP (ES4) |
|-----------|----------------|----------------------------------|--------------|
| Enable | `ES4.EnableProfile` | `ES2.EnableProfile` → `ES3.EnableProfile` | `ES4.EnableProfile` (with PLMA) |
| Disable | `ES4.DisableProfile` | `ES2.DisableProfile` → `ES3.DisableProfile` | `ES4.DisableProfile` (with PLMA) |
| Delete | `ES4.DeleteProfile` | `ES2.DeleteProfile` → `ES3.DeleteProfile` | `ES4.DeleteProfile` (with PLMA) |
| Master Delete | Out of scope (ES4 by Initiator) | Via SM-DP authorisation | Not applicable |

---

## Enabling a Profile: "make this one the active one"

Enabling is the operation that makes a Profile's NAA (Network Access Application) and file system visible over the UICC-Terminal interface. Only one Profile can be enabled at a time; if you enable Profile B, Profile A gets automatically disabled. There's no graceful handoff and no confirmation dialog. The ISD-R just does it.

The Normal Case flow (SGP.02 §3.2.1):

1. The Operator calls `ES4.EnableProfile(eid, iccid)` (or `ES2.EnableProfile` through the SM-DP)
2. The SM-SR verifies the Profile exists, is currently disabled, and POL2 doesn't forbid enabling
3. The SM-SR sends an SCP80-secured `ES5.STORE DATA` command to the ISD-R, typically via SMS
4. The ISD-R checks the currently enabled Profile's POL1: "disable not allowed"? Then we stop right here
5. The ISD-R disables the current ISD-P and enables the target ISD-P
6. A UICC Reset REFRESH forces the Device to re-attach with the new Profile
7. The eUICC runs the Default Notification procedure (SMS or HTTPS) to tell the SM-SR what happened
8. After notification, the SM-SR evaluates POL2 of the now-disabled Profile. If POL2 says "Profile deletion is mandatory when disabled," the SM-SR immediately sends an `ES5.DELETE` command
9. The SM-SR updates its EIS record

### What if it can't connect?

This is the Connectivity Failure Case (§3.2.2), and it's where SGP.02 earns its reputation for paranoia-that-pays-off. If the newly enabled Profile can't attach to the network, or if the notification procedure fails, the eUICC doesn't just shrug and leave the device stranded:

- The ISD-R re-enables the previously enabled Profile
- A new REFRESH triggers re-attachment with the roll-back Profile
- The notification procedure tells the SM-SR "we rolled back"
- If the roll-back Profile *also* can't connect, the eUICC activates the Fall-Back Mechanism (Article 8)

A failed profile switch in a device nobody can physically reach would otherwise mean permanent disconnection. The automatic roll-back is the spec's answer to that nightmare.

---

## Disabling: deactivate, but don't destroy

Disabling (§3.4) makes a Profile unselectable while leaving it intact on the card. The flow mirrors enabling: SM-SR checks, OTA command, ISD-R executes, notification, EIS update; but with one difference that changes everything:

When you disable a Profile, **the eUICC automatically enables the Fall-Back Profile.**

Think about why. If you disable the only enabled Profile and don't turn anything else on, the device goes dark. No connectivity. No OTA channel. Your only option is a truck roll; and for devices in basements, engine compartments, or remote weather stations, that might not even be practical. So SGP.02 mandates immediate failover to whatever Profile carries the Fall-Back Attribute.

Two more things happen during disable:

- After disabling, POL1 is evaluated. If the disabled Profile's POL1 says "Profile deletion is mandatory when its state is changed to disabled," the ISD-R deletes the Profile and its ISD-P right there on the card.
- After notification, the SM-SR separately evaluates POL2 and may also trigger deletion.

The spec explicitly notes that POL1 and POL2 "MAY have different content. As a consequence, both the eUICC and the SM-SR have to ensure the ISD-P deletion based on their respective Policy." One side might delete while the other doesn't. That's not a bug; it's intentional redundancy.

---

## Deleting: gone forever

Profile Deletion (§3.6, §3.7) permanently removes the ISD-P and everything inside it: NAA, file system, keys, applets, metadata. It can be triggered three ways:

- Directly, via `ES4.DeleteProfile`
- Through the SM-DP relay chain: `ES2.DeleteProfile` → `ES3.DeleteProfile` → `ES5` commands
- Automatically after disabling, when POL1 or POL2 demands it

The on-card flow is simple: SM-SR sends `ES5.DELETE` targeting the disabled Profile's ISD-P. ISD-R checks POL1. If it permits, the ISD-P gets wiped. SM-SR updates the EIS. You can't delete the currently enabled Profile; disable it first. The deletion is permanent and irreversible. No undo.

### Master Delete: when the rules are the problem

Sometimes a Profile needs to go but the rules say it can't. The owning Operator went bankrupt. The policy was set too restrictively. Nobody with authority is reachable to change it. These are orphaned Profiles, and they'd permanently consume space on the eUICC if SGP.02 hadn't thought ahead.

The Master Delete procedure (§3.10) solves this with a cryptographically authorised **Delete Token** issued by the SM-DP:

1. An Initiator (not necessarily the Operator) requests Master Delete from the SM-SR
2. The SM-SR asks the SM-DP associated with the target Profile for a Master Delete Authorisation
3. The SM-DP verifies the request is authenticated and authorised (Operator authorisation details are out of scope)
4. If authorised, the SM-DP issues a one-time Delete Token
5. The SM-SR sends `ES5.MasterDelete` with the token to the ISD-R
6. The ISD-P itself (not just the ISD-R) verifies the token cryptographically
7. The ISD-R deletes the ISD-P and Profile **regardless of POL1 or POL2**

One hard limit: you can't Master Delete the Fall-Back Profile. The device always keeps at least one path back to connectivity.

---

## The failure pattern that runs through everything

Once you've read a few SGP.02 procedures, you start to notice the same failure-handling skeleton underneath all of them. Enable, disable, delete; they all share it:

- **eUICC-side timeout:** If the newly enabled Profile can't register on the network, the eUICC notices locally
- **Notification timeout:** If the eUICC exhausts all retries trying to reach the SM-SR for notification, it treats the operation as failed
- **Roll-back:** Enable reverts to the previously enabled Profile. Disable activates the Fall-Back Profile
- **Fall-Back escalation:** If roll-back also fails, the Fall-Back Mechanism kicks in, the ultimate safety net
- **SM-SR Validity Period:** The SM-SR sets a timer when it issues an OTA command. If the notification arrives after the timer expires, the SM-SR doesn't send a confirmation, and the eUICC treats that as a notification failure, triggering roll-back

This pattern is what makes remote management of inaccessible devices viable. Every operation has a built-in escape hatch.

---

The three-path architecture is what makes SGP.02 flexible enough for diverse M2M deployments. A utility company acting as its own M2M SP can manage its meter fleet directly. The mobile operator retains ultimate control through PLMA and POL1/POL2 policy rules. And every operation, no matter who initiated it or through which path, converges on the same on-card procedure with the same failure handling.

### The short version

- Enable, disable, and delete each have three initiation paths: Operator direct (ES4), Operator via SM-DP relay, and M2M SP via ES4 with PLMA
- Every operation follows: SM-SR checks → OTA command → POL1 enforcement → eUICC execution → notification → POL2 check → EIS update
- Connectivity Failure Cases mean the eUICC automatically rolls back, reverting to the previous Profile or activating Fall-Back
- Disabling always switches to the Fall-Back Profile to keep the device online
- POL1 (on-card) and POL2 (server-side) are enforced independently and may differ
- Master Delete bypasses all policy rules with a one-time cryptographic token, but can't touch the Fall-Back Profile

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

Previous: [Profile Download: ISD-P Creation, SCP03, and Encrypted Delivery](05-sgp02-download) →
Next: [SM-SR Change: Handover, ES7 Interface, and EIS Migration](07-sgp02-sm-sr-change) →

</div>

---

*Based on GSMA SGP.02 v4.2 (07 July 2020): Remote Provisioning Architecture for Embedded UICC Technical Specification, §3.2–3.7, §3.10*


---

← Previous: [Profile Download: ISD-P Creation, SCP03, and Encrypted Delivery](05-sgp02-download) | [Section Index](index) | Next: [SM-SR Change: Handover, ES7 Interface, and EIS Migration](07-sgp02-sm-sr-change) →
