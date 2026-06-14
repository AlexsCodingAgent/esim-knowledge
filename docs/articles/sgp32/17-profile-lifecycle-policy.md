---
title: "Profile Lifecycle & Policy: Types, PPE, and Enforcement in IoT eSIM"
description: "Examines the three Profile Types : Operational, Provisioning, Test : and how the Profile Policy Enabler enforces PPR1/PPR2 rules against the Rules Authorisation Table to prevent carrier lock-in."
date: 2026-06-07
---

# Profile Lifecycle & Policy: Types, PPE, and Enforcement in IoT eSIM

**[eUICC.tech]({{ site.baseurl }}/) > [SGP.32 IoT eSIM]({{ site.baseurl }}/docs/articles/sgp32/) > Profile Lifecycle & Policy: Types, PPE, and Enforcement in IoT eSIM**

> **Why this matters:** Not all eSIM profiles are created equal. SGP.32 defines three distinct Profile Types: Operational, Provisioning, and Test: each with different lifecycles, visibility rules, and survival characteristics across memory resets. On top of that, every profile can carry Policy Rules that dictate whether it can be disabled or deleted, enforced by a dedicated eUICC component called the Profile Policy Enabler (PPE). Understanding this layered lifecycle-and-policy model is essential for designing IoT fleets that survive field failures, resets, and provider transitions.

> **Key takeaways:**
> - Three Profile Types: Operational (standard MNO profiles), Provisioning (survive resets, hidden from users), Test (lab/QA-only, weak keys)
> - Profile Class is set in metadata at manufacturing time: it determines lifecycle behaviour forever
> - PPR1 ("Disabling not allowed") and PPR2 ("Deletion not allowed") are enforced by the PPE at profile-state-change time
> - The Rules Authorisation Table (RAT) gates which Operators can use which PPRs: preventing lock-in abuse
> - In IoT, the eIM also verifies PPRs against the RAT during Indirect profile download, rejecting mismatched profiles before they touch the eUICC

* TOC
{:toc}

Every profile on an eSIM has a lifecycle: it is downloaded, enabled, disabled, and eventually deleted. But not all profiles follow the same lifecycle rules. Some survive factory resets. Some can't be deleted. Some are invisible to the end user. This article unpacks the three Profile Types and the Policy Enforcement machinery that makes all of this work.

---

## The Three Profile Types

SGP.22 (and by extension SGP.32) defines exactly three Profile Types, distinguished by the `Profile Class` field in the Profile Metadata, set at profile creation time:

| Profile Type | Profile Class | Visibility | Memory Reset | Typical Use |
|---|---|---|---|---|
| **Operational** | `operational` | Visible | Deleted | Primary MNO connectivity |
| **Provisioning** | `provisioning` | Hidden from LUI | **Survives** | Bootstrap/first-connectivity |
| **Test** | `test` | Visible only in Test Mode | Deletable (selectively) | Lab & factory QA |

### Operational Profile

This is the standard, everyday profile. It contains the Operator's MNO-SD, NAAs, applets, and file system: the full profile component set. When an Operational Profile is Enabled, the eUICC behaves exactly like a conventional UICC.

Operational Profiles are visible to the end user, selectable, and deletable through normal UI actions. They are deleted by eUICC Memory Reset. They can carry PPR1 and/or PPR2 if the Operator wishes to prevent accidental disabling or deletion.

### Provisioning Profile

A Provisioning Profile is structurally identical to an Operational Profile in every respect except two critical behavioural differences:

1. **Hidden from the LUI.** Provisioning Profiles and their metadata are never visible to the end user. They cannot be selected through any user action. This makes them invisible bootstrap profiles: the user's device connects using a provisioning profile, but the user never sees it.

2. **Survive Memory Reset.** In consumer eSIM (SGP.22), the eUICC Memory Reset function explicitly *does not delete* Provisioning Profiles. They persist through what would otherwise be a factory reset. This is intentional: a provisioning profile is the escape hatch that lets a device reconnect after a catastrophic reset.

Additionally, Provisioning Profiles have a special override on PPR1: if a Provisioning Profile needs to be enabled, the eUICC will *implicitly disable* the currently enabled Operational Profile, even if that Operational Profile has PPR1 ("Disabling not allowed") set. A Provisioning Profile can always be enabled: it is, by design, the profile of last resort.

In SGP.32 IoT context, the Memory Reset function (`ES10b.eUICCMemoryReset`) presents a **parameterised deletion model**: the caller selects which subsets of profiles to delete (Operational, field-loaded Test, pre-loaded Test, Provisioning). This gives IoT fleet managers finer control, but also means a badly-constructed reset command *could* delete provisioning profiles: unlike consumer eSIM where they're unconditionally protected.

### Test Profile

Test Profiles exist for laboratory, certification, and factory QA use. Their key characteristic: they use deliberately weak, well-known authentication keys (all-zeroes, or the 3GPP test USIM default `00 01 02 03 … 0F`). No live commercial network would accept these keys.

Test Profiles are hidden from normal LUI view and only become visible when the device enters **Device Test Mode** : triggered by enabling a Test Profile for the first time. While in Test Mode, the regular Profile Policy Rules enforcement is relaxed: even if an Operational Profile has PPR1 set, enabling a Test Profile will implicitly disable it. This prevents test workflows from triggering spurious policy errors.

When the Test Profile is disabled, the eUICC re-enables whichever Operational Profile was active before Test Mode was entered. No notifications are generated for enabling or disabling Test Profiles.

---

## The Profile Policy Enabler (PPE)

The PPE is an on-eUICC component (part of the broader **Profile Rules Enforcer**, or PRE) with two jobs:

1. **At install time:** Verify that any PPRs a new profile carries are authorised by the Rules Authorisation Table (RAT).
2. **At runtime:** Enforce the PPRs whenever a Local Profile Management operation (enable, disable, delete) is attempted.

If a profile contains a PPR not authorised by the RAT, the PPE rejects the installation entirely: the profile never lands on the eUICC.

### The Two Policy Rules

SGP.22 v3.1 defines exactly two Profile Policy Rules:

| Rule | Bit | Meaning |
|---|---|---|
| **PPR1** | `ppr1(1)` | Disabling of this Profile is not allowed |
| **PPR2** | `ppr2(2)` | Deletion of this Profile is not allowed |

PPRs are flagged in the `profilePolicyRules` bit string (ASN.1 type `PprIds`) within the Profile Metadata. A profile can carry zero, one, or both rules.

**PPR1 enforcement:** If a profile has PPR1 set and is currently Enabled, any attempt to disable it (whether locally or via PSMO) is rejected. The only exception: enabling a Provisioning Profile or Test Profile overrides PPR1 check.

**PPR2 enforcement:** If a profile has PPR2 set, any attempt to delete it is rejected regardless of whether it is enabled or disabled. Even a Memory Reset would need to respect PPR2: though in SGP.32, the parameterised reset can specify profile subsets explicitly.

---

## The Rules Authorisation Table (RAT)

Not every Operator is allowed to set every PPR. The **Rules Authorisation Table** (RAT) is an eUICC-platform-level table initialised at manufacturing time: or at initial device setup (provided no Operational Profile is installed yet) : that controls *which Operators* may use *which PPRs* on *this specific eUICC*.

The RAT contains a list of **Profile Policy Authorisation Rules (PPARs)**, each specifying:

- **PPR Identifier:** Which PPR(s) this entry applies to
- **Allowed Operators:** A list of Operator identifiers (MCC-MNC + optional GID1/GID2), with wildcard support (`EEEEEE` means "any operator", empty GID means "match absent")
- **End User Consent Required:** Whether the LPA must obtain user consent before installing a profile with this PPR

PPARs are evaluated in order. The first matching PPAR for a given PPR + Operator combination wins. Critically: if *no* PPAR is defined for a particular PPR, that PPR is **forbidden** for *all* Operators.

A RAT that is empty (no entries) means: "all PPRs forbidden for all Operators." A RAT with a wildcard entry like `PPR1, PPR2 → * → true` means: "any Operator can use any PPR, but End User consent is required."

The RAT survives eUICC Memory Reset: it's platform-level, not profile-level.

### RAT Verification in IoT

In the IoT SGP.32 world, the RAT check happens at two points:

1. **LPA/IPA side:** During the Cancel Session flow (if the profile's PPRs don't pass the RAT check, the reason `pprNotAllowed` is sent)
2. **eIM side:** During Indirect profile download, the eIM receives the Profile Metadata from the SM-DP+ via `ES9+'` and verifies PPRs against the RAT *before* forwarding the Bound Profile Package to the IPA

This server-side pre-check is an IoT-specific enhancement: it prevents the IPA from even receiving a profile that would later be rejected by the eUICC's PPE, saving bandwidth and processing on constrained devices.

---

## Where PPE Fits in the eUICC Architecture

The PPE sits alongside ISD-R, ISD-P, ECASD, and the Telecom Framework in the eUICC's internal architecture. In the SGP.32 diagram (Figure 4), the PPE and Profile Package Interpreter are shown as co-located services on the eUICC OS, with the ISD-R acting as the gateway for all profile state changes:

```
eUICC OS
 ├── ECASD (keys, certs)
 ├── ISD-R (profile lifecycle manager)
 ├── ISD-P / ISD-P (profile containers)
 ├── Profile Policy Enabler (PPR verification + enforcement)
 ├── Profile Package Interpreter (decodes Profile Package)
 └── Telecom Framework (NAA algorithms)
```

When a PSMO arrives via eUICC Package:
1. ISD-R receives the signed package
2. ISD-R identifies the target profile
3. PPE checks: does this operation violate any PPR on the target profile?
4. Only if PPE grants clearance does ISD-R proceed with the REFRESH cycle

---

## Lifecycle Summary: Which Profile Survives What

| Event | Operational | Provisioning | Test |
|---|---|---|---|
| Enable/Disable (PSMO) | (if PPR1 allows) | (overrides PPR1) | (overrides PPR1) |
| Delete (PSMO) | (if PPR2 allows) | (if PPR2 allows) | |
| Consumer Memory Reset | **Deleted** | **Survives** | **Deleted** (field-loaded only by default) |
| SGP.32 IoT Memory Reset | Deleted if selected | Deleted if selected | Deleted if selected |
| Visible in LUI | | | (Test Mode only) |
| Can carry PPRs | | (but PPR1 overridden) | (SHOULD NOT) |

---

## Summary

- Three Profile Types serve three distinct lifecycle roles: Operational (standard), Provisioning (bootstrap, reset-surviving), and Test (lab-only with weak keys)
- The Profile Policy Enabler gates every profile state change against PPR1 and PPR2
- The Rules Authorisation Table restricts which Operators may set which PPRs: preventing lock-in abuse
- In IoT, the eIM adds a server-side PPR verification layer during Indirect Download
- Provisioning Profiles are the escape hatch: they survive consumer Memory Reset and override PPR1 blocking

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp32/16-iot-functions-reference">IoT eSIM Functions Reference: ESipa, ES9+', ES11', ESep</a> · <a href="{{ site.baseurl }}/">Home</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp32/18-advanced-security-lifecycle">Advanced IoT Security & Lifecycle</a> →

</div>

---

*Based on GSMA SGP.22 v3.1, Sections 2.4.5, 2.9; GSMA SGP.32 v1.3, Sections 2.4.5, 2.4.12, 2.8, 5.9.5*


---

← Previous: [IoT eSIM Functions Reference: ESipa, ES9+', ES11', ESep](16-iot-functions-reference) | [Section Index](index) | Next: [Advanced IoT Security & Lifecycle: Mutual Auth, OS Update, Emergency Profiles, and ECASD](18-advanced-security-lifecycle) →
