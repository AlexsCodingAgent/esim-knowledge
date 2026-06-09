---
description: "Explains Multiple Enabled Profiles in SGP.22 v3.x — how several profiles run simultaneously, each bound to a distinct eSIM Port as a logical SE interface, enabling true multi-SIM eSIM devices with per-port policy enforcement."
layout: default
title: "Multiple Enabled Profiles: Running Several eSIMs at Once"
date: 2026-06-06
---

# Multiple Enabled Profiles: Running Several eSIMs at Once

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.22 v3.x Unified RSP]({{ site.baseurl }}/docs/articles/sgp22-v3/) > Multiple Enabled Profiles: Running Several eSIMs at Once**

> **💡 Why this matters:** In SGP.22 v2.x, only one profile can be **Enabled** at a time. If you have a personal profile and a work profile, you must disable one to use the other. If your device has dual SIM hardware, only one eSIM can be active. Multiple Enabled Profiles (MEP) changes everything: it allows multiple profiles to be Enabled simultaneously, each bound to a separate eSIM Port, enabling true multi-SIM eSIM devices just like physical dual-SIM phones. This is the single most impactful consumer-facing feature in v3.x.

> **Key takeaways:**
> - MEP allows **several Profiles in Enabled state simultaneously**, each assigned to a distinct eSIM Port
> - eSIM Ports are logical SE interfaces (LSIs per ETSI TS 102 221), identified by consecutive numbers starting from 0
> - Each eSIM Port can have at most one Enabled Profile; each Profile can be assigned to at most one eSIM Port
> - Three MEP modes: **MEP-A1** (LPA assigns ports), **MEP-A2** (eUICC assigns ports), **MEP-B** (ISD-R selectable on any port)
> - MEP is only defined for **non-removable eUICCs**; still, an optional setup mechanism allows devices and eUICCs to negotiate modes
> - APDU multiplexing uses standard ETSI TS 102 221 mechanisms such as MANAGE LSI or NAD byte selection
> - In v2.x, profile switching (Enable/Disable) requires either a REFRESH proactive command or none; MEP extends these options for multi-port operation

---

## The v2.x Limitation: One Profile at a Time

In SGP.22 v2.x, the eUICC maintains state for one Enabled Profile. When you want to switch from Profile A to Profile B, the LPA must:

1. Disable Profile A (sending a REFRESH to reset the UICC interface)
2. Enable Profile B

During the switch, the device loses connectivity. Even on a dual-SIM device with two physical basebands, v2.x cannot expose two active eSIM profiles simultaneously: there's a single logical channel.

MEP removes this limitation. The eUICC presents multiple **eSIM Ports**, each of which can host a different Enabled Profile. A device with two basebands can connect one to each port, giving the user two active mobile subscriptions at once: just like a dual physical SIM phone.

---

## How MEP Works: eSIM Ports

The core concept of MEP is the **eSIM Port** : what ETSI TS 102 221 calls a Logical SE Interface (LSI). Ports are identified by consecutive numbers starting from zero:

- **eSIM Port 0** : typically the "primary" port, where the ISD-R may be selectable (depending on the MEP mode)
- **eSIM Port 1, Port 2, ...** : additional ports that can host Enabled Profiles

The multiplexing of APDU streams to different Profiles on a single physical interface uses standard mechanisms defined in ETSI TS 102 221:

- **APDU MANAGE LSI (select LSI)** : when transmission protocol T=0 or T=1 is used, the device selects which eSIM Port an APDU targets
- **NAD byte** : when T=1 is used, the Node Address byte identifies the target port

The key constraint: **each eSIM Port SHALL be assigned to at most one Enabled Profile, and each Profile SHALL be assigned to at most one eSIM Port**. Profile Enabling assigns a Profile to a port; Profile Disabling releases the assignment. A Disabled Profile is not assigned to any port.

---

## The Three MEP Modes

The specification defines three options for how ISD-R selection and port assignments work. An eUICC MAY implement any combination of these modes; the OEM and EUM can pre-agree on which modes to use.

### MEP-A1: LPA-Assigned Ports

In MEP-A1:
- The **ISD-R is selected only on eSIM Port 0** (the Command Port)
- **Profiles are selected on eSIM Ports 1 and higher** (the Target Ports)
- The LPA assigns which Profile goes to which port: so the Command Port and Target Port are **always different**

This is the simplest model for the LPA: it controls port assignment directly.

### MEP-A2: eUICC-Assigned Ports

In MEP-A2:
- The **ISD-R is selected only on eSIM Port 0** (the Command Port)
- **Profiles are selected on eSIM Ports 1 and higher** (the Target Ports)
- The **eUICC assigns** which Profile goes to which port: Command Port and Target Port are always different

Here the eUICC makes the assignment decision, which may be useful when the eUICC has knowledge about port capabilities that the LPA lacks.

### MEP-B: ISD-R on Any Port

In MEP-B:
- **Profiles can be selected on eSIM Ports 0 and higher**
- The **ISD-R can be selected on any eSIM Port**
- `ES10c.EnableProfile` and (when CAT is initialised on the Target Port) `ES10c.DisableProfile` are always sent **on the Target Port** : so Command Port and Target Port are identical
- If CAT is not initialised on the Target Port, `ES10c.DisableProfile` can be sent on any eSIM Port where CAT is initialised
- Other ES10 commands can be sent on any eSIM Port where CAT is initialised

MEP-B is the most flexible mode, allowing any port to serve as both command and target port.

---

## Profile Switching with MEP

v2.x defines two options for profile switching: with or without a REFRESH proactive command. MEP extends these for multi-port scenarios:

- **With REFRESH**: After enabling/disabling a Profile, the ISD-R sends a REFRESH proactive command (SEP mode) or an LSI COMMAND with "UICC Platform Reset" (MEP mode)
- **Without REFRESH**: The profile switch completes without any proactive command

In MEP mode, instead of a REFRESH command that resets the entire UICC, the eUICC can send an **LSI COMMAND proactive command** with "UICC Platform Reset" : targeting only the affected port rather than resetting the entire eUICC. This means enabling a profile on Port 1 doesn't disrupt the active session on Port 0.

---

## Comparison: v2.x (SEP) vs v3.x (MEP)

| Aspect | v2.x (SEP: Single Enabled Profile) | v3.x (MEP: Multiple Enabled Profiles) |
|--------|-------------------------------------|----------------------------------------|
| Profiles Enabled at once | 1 | Multiple (one per eSIM Port) |
| Port model | Single logical interface | Multiple eSIM Ports (LSIs) |
| ISD-R location | One location | Mode-dependent (Port 0 only or any port) |
| Profile switching | Disable old → REFRESH → Enable new | Enable on target port without disrupting others |
| Proactive reset | REFRESH (UICC Reset) | LSI COMMAND (UICC Platform Reset) per port |
| APDU multiplexing | Not needed | MANAGE LSI or NAD byte |
| eUICC type | All | Non-removable only |
| Mode negotiation | N/A | Optional setup mechanism (section 3.4.1) |

---

## The Optional Setup Mechanism

Although MEP modes are typically pre-agreed between the OEM and EUM at manufacturing time, the specification defines an optional setup mechanism (section 3.4.1) that allows Devices and eUICCs to support several MEP modes. This mechanism enables:

- Discovery of which MEP modes the eUICC supports
- Negotiation of the mode to use
- Fallback to SEP if MEP modes don't match

This flexibility is valuable for device manufacturers who want a single LPA implementation to work across different eUICC hardware that may implement different MEP modes.

---

## MEP and Profile Policy Rules

The v3.x Profile Rules Enforcer (section 2.4.12) must handle the multi-port scenario. When a profile is Enabled on a port, Profile Policy Rules (PPRs) related to that profile: such as restrictions on disabling or deletion: still apply. The ISD-R enforces these rules regardless of which port the profile occupies.

For profile switching in MEP mode, the same PPR logic applies as in v2.x: a profile configured with a "disabling not allowed" rule cannot be disabled, even if another profile is being enabled on the same port.

---

## Summary

- Multiple Enabled Profiles (MEP) is a v3.x-only feature that allows several profiles to be Enabled simultaneously
- Each Enabled Profile is assigned to a distinct eSIM Port (numbered from 0)
- Three modes exist: MEP-A1 (LPA assigns), MEP-A2 (eUICC assigns), MEP-B (any port for ISD-R)
- APDU multiplexing uses standard ETSI TS 102 221 mechanisms
- MEP is limited to non-removable eUICCs; OEMs and EUMs pre-agree on supported modes
- Profile switching in MEP can use per-port resets rather than full UICC resets

---

<div align="center" markdown="1">

← Previous: [SGP.22 v3.x Overview: The Unified eSIM Specification]({{ site.baseurl }}/docs/articles/sgp22-v3/52-sgp22-v3-overview)

Next: [Push Service: How eSIMs Get Notified Without Polling]({{ site.baseurl }}/docs/articles/sgp22-v3/54-push-service) →

</div>

---

*Based on GSMA SGP.22 v3.1 (01 December 2023), Section 2.12: Multiple Enabled Profiles, and ETSI TS 102 221 [6]*


---

← Previous: [SGP.22 v3.x Overview: The Unified eSIM Specification](52-sgp22-v3-overview) | [Section Index](index) | Next: [Push Service: How eSIMs Get Notified Without Polling](54-push-service) →
