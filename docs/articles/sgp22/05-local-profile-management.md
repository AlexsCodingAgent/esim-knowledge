---
title: "Managing Your eSIM: Local Profile Operations"
date: 2026-06-03
---

# Managing Your eSIM: Local Profile Operations

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.22 Consumer RSP]({{ site.baseurl }}/docs/articles/sgp22/) > Managing Your eSIM: Local Profile Operations**

> **💡 Why this matters:** This is the user-facing half of eSIM — everything you actually do on your device: switching carriers, deleting old plans, and naming profiles. The UI is simple, but the underlying protocol is precise and policy-enforced.

> **Key takeaways:**
> - All local profile operations go through `ES10c` (LPA → eUICC) and are gated by the `ISD-R`
> - Profiles have exactly two states: Enabled (active) or Disabled (dormant)
> - **Profile Policy Rules** (`ppr1`, `ppr2`, `ppr3`) can override user intent — critical for corporate-managed devices
> - Profile switching involves careful application session termination and baseband REFRESH signalling
> - Device Test Mode and Provisioning Profiles add special lifecycle behaviours for development and bootstrap scenarios

---

Once profiles are installed on your eUICC, you need to manage them — switch between them, delete old ones, check what's installed, and occasionally factory-reset the whole chip. SGP.22 defines a complete set of local profile management operations through the `ES10c` interface (LPA → eUICC).

Every operation goes through the `ISD-R`, which enforces Profile Policy Rules and ensures operations are valid before executing them.

---

## Profile States

A Profile can be in one of two states:

| State | Behaviour |
|-------|-----------|
| **Enabled** | The Profile's file system and NAAs are selectable by the device. The modem sees this Profile. Only one Profile can be Enabled at a time. |
| **Disabled** | The Profile is installed but dormant. Its file system is invisible to the device. Its applications cannot be selected, triggered, or individually deleted. Remote management via `ES6` is blocked. |

When you switch profiles, the disabled one doesn't need to be re-downloaded — it stays on the chip, ready to be enabled again instantly.

---

## Enable Profile

Switching to a different profile involves two critical actions: disabling the current one and enabling the target.

**Start conditions:**
- For Operational Profiles: End User intent must be verified (as defined in SGP.21)
- For Test Profiles: The device must be in Device Test Mode
- For Provisioning Profiles: An operation requiring connectivity (like a profile download) must have completed

**Procedure:**

```
1. LPA → eUICC: ES10c.EnableProfile(ISD-P AID or ICCID, refreshFlag)

2. ISD-R verifies:
   - Target Profile is in Disabled state
   - Profile Policy Rules allow enabling
   - Error returned if either check fails

3. Application session termination on currently Enabled Profile:
   - Run application session termination per ETSI TS 102 221
   - Close all logical channels
   - Terminate any ongoing proactive command session

4. ISD-R enables the target Profile

5. If refreshFlag is set:
   - ISD-R sends REFRESH proactive command to baseband
   - Baseband responds with Terminal Response or RESET

6. Device discards all state from previously Enabled Profile:
   - Cached file content (including EF_ICCID and EF_DIR)
   - PIN state
   - Proactive command sessions
   - Logical channel assignments

7. Baseband executes network attach with the newly Enabled Profile
```

**Critical detail:** If the target is a Provisioning Profile and an Operational Profile was previously enabled, the Operational Profile is implicitly disabled (regardless of any "Disabling not allowed" policy rule — this is the one exception). Similarly, Test Profile transitions have special re-enable behaviour: if an Operational Profile was enabled before entering Test Mode and wasn't deleted, it's automatically re-enabled when leaving Test Mode.

---

## Disable Profile

Removing a profile from active use without deleting it:

```
1. Device runs application session termination on currently Enabled Profile
   (if refreshFlag is not set)

2. LPA → eUICC: ES10c.DisableProfile(ISD-P AID or ICCID, refreshFlag)

3. ISD-R verifies:
   - Target Profile is in Enabled state
   - Profile Policy Rules allow disabling (ppr1 check)

4. If refreshFlag is set: REFRESH → Terminal Response → disable
   If refreshFlag is not set: immediate disable

5. Auto re-enable logic for Test/Operational transitions
```

Profile Policy Rule **`ppr1`** ("Disabling not allowed") can prevent this operation entirely. This is commonly used on corporate-managed devices where the IT department's profile must always remain active.

---

## Delete Profile

Permanently removes a Profile and its containing ISD-P:

```
1. LPA → eUICC: ES10c.DeleteProfile(ISD-P AID or ICCID)

2. ISD-R verifies:
   - Profile Policy Rules allow deletion (ppr2 check)
   - If the Profile is Enabled, ppr1 also checked (must allow disabling)

3. ISD-R deletes the ISD-P:
   - All Profile Components destroyed (MNO-SD, NAAs, file system, applets)
   - ISD-P removed from eUICC

4. If deleted Profile was the currently Enabled one:
   - No profile is enabled
   - Device signals baseband: no Enabled Profile
```

**Profile Policy Rule `ppr3`** ("Delete after disable") triggers automatic deletion when a profile is disabled — useful for one-time provisioning profiles that shouldn't persist.

---

## List Profiles

Retrieving what's installed:

```
1. LPA → eUICC: ES10c.GetProfilesInfo()

2. eUICC returns per-profile:
   - ICCID
   - ISD-P AID
   - Profile state (Enabled/Disabled)
   - Profile nickname (if set)
   - Profile class (Operational/Provisioning/Test)
   - Operator name
   - Profile name
   - Icon (optional)
   - Profile Policy Rules
```

Provisioning Profiles and their metadata are **not visible to the End User in the LUI** — they exist only for machine-to-machine use. The LPA filters them from display.

---

## eUICC Memory Reset

Factory-resets the entire chip:

```
1. LPA → eUICC: ES10c.eUICCMemoryReset()

2. ISD-R:
   - Deletes all Operational and Test Profiles
   - Keeps Provisioning Profiles (by spec: "not deletable through End User action")
   - Returns eUICC to a state equivalent to post-manufacturing
```

**eUICC Test Memory Reset** is a lighter variant that only deletes post-issuance Test Profiles — useful for development and testing without affecting production profiles.

---

## Set Nickname

Assigns a user-friendly label:

```
1. LPA → eUICC: ES10c.SetNickname(ICCID, nickname)

2. ISD-R stores the nickname in Profile Metadata

3. Nickname is UTF-8, max 64 characters
```

The nickname is displayed in the LUI alongside the operator name, helping users distinguish "Work" from "Personal" from "Travel Japan."

---

## Profile Policy Rules

The **Rules Authorisation Table (RAT)** defines what operations are permitted on each profile:

| Rule | Code | Effect |
|------|------|--------|
| Disabling not allowed | `ppr1` | Enable → Disable transition blocked |
| Deletion not allowed | `ppr2` | Delete operation blocked |
| Delete after disable | `ppr3` | Auto-delete when profile is disabled |

Rules are stored per-profile in Profile Metadata and enforced by the **Profile Policy Enabler** within the `ISD-R`. The LPA may read rules to provide appropriate warnings (e.g., "Disabling this profile will automatically delete it").

---

## eUICC Memory Management

The eUICC has finite storage for multiple Profiles. SGP.22 requires the eUICC to:

- Report available memory to the LPA for display
- Return `installFailedDueToInsufficientMemoryForProfile(10)` if a new profile doesn't fit
- Support deletion of unused profiles to reclaim space
- Preserve Provisioning Profiles across Memory Reset (they persist for device recovery)

---

## Device Test Mode

For development and testing, SGP.22 defines a **Device Test Mode** — a hidden mode that grants access to Test Profiles:

- Test Profiles use predetermined test authentication keys: all bits set to zero, or the 3GPP TS 34.108 test USIM K value
- Test Profiles are only selectable when Device Test Mode is active
- The LUI hides Test Profiles from the normal user interface
- Test Profile NAA keys must comply with specific validation rules to prevent them being used as operational profiles

---

## 📋 Summary

- All local management flows through `ES10c` to the `ISD-R`, which enforces Profile Policy Rules before any state change
- Profiles toggle between Enabled (active, modem-visible) and Disabled (dormant, fully installed); switching triggers careful session termination and baseband signalling
- Three policy rules (`ppr1`, `ppr2`, `ppr3`) provide hard enforcement for enterprise and lifecycle scenarios — even the end user can't override them
- Device Test Mode and Provisioning Profiles enable development, testing, and bootstrap connectivity with special lifecycle handling and UI filtering
- Memory management, nicknames, and the Rules Authorisation Table round out a complete local management surface

---

<div align="center">

← Previous: [eSIM Security: The PKI and Certificate Model]({{ site.baseurl }}/docs/articles/sgp22/04-esim-security-pki) · [🏠 Home]({{ site.baseurl }}/)

Next: [The Developer's View: RSP Interfaces and Protocol Binding]({{ site.baseurl }}/docs/articles/sgp22/06-developer-interfaces) →

</div>

---

*Based on GSMA SGP.22 v2.7 (24 April 2026), Sections 3.2, 3.3, and 5.7 — Local Profile Management, Local eUICC Management, and ES10x Functions*
