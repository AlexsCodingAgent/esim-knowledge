---
description: "Explains Enterprise Profiles in SGP.22 v3.x : the v3.x-only profile class with enforceable corporate restrictions including priority enforcement, installation limits, and non-deletable and non-disablable rules that survive end-user actions."
layout: default
title: "Enterprise Profiles in SGP.22 v3.x: Corporate Control of eSIMs"
date: 2026-06-07
---

# Enterprise Profiles in SGP.22 v3.x: Corporate Control of eSIMs

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.22 v3.x Unified RSP]({{ site.baseurl }}/docs/articles/sgp22-v3/) > Enterprise Profiles in SGP.22 v3.x: Corporate Control of eSIMs**

> **💡 Why this matters:** Bring-your-own-device (BYOD) programs create a fundamental tension: the employee owns the phone, but the enterprise owns the data and the mobile subscription. In SGP.22 v2.x, there's no way to express this distinction: all profiles are treated equally, and the end user can disable or delete any profile at will. Enterprise Profiles, introduced in v3.0, solve this by creating a new profile class with enforceable restrictions that survive end-user actions. An enterprise can mandate that its corporate profile cannot be disabled or deleted, that only enterprise profiles can be installed on the device, or that the enterprise profile must be the priority profile. The eUICC enforces these rules in hardware, not just in software: making enterprise profiles the foundation for corporate-managed eSIM fleets.

> **Key takeaways:**
> - Enterprise Profiles are a **v3.x-only feature** (`#SupportedForEnterpriseV3.0.0#`), distinct from Operational and Test profile classes
> - **Enterprise Rules** are encoded in the `EnterpriseConfiguration` data structure within Profile Metadata, containing: `referenceEnterpriseRule`, `priorityEnterpriseProfile`, `onlyEnterpriseProfilesCanBeInstalled`, and `numberOfNonEnterpriseProfiles`
> - An **Enterprise Capable Device** is required for Enterprise Rules to take effect: non-Enterprise Capable Devices can still install Enterprise Profiles but without rule enforcement
> - The **Reference Enterprise Rule** is the master switch: only one Enterprise Profile per eUICC can hold this flag, and its rules govern the entire device
> - Enterprise Rules coexist with Profile Policy Rules (PPRs) : they're enforced by the same Profile Rules Enforcer but operate at a different layer
> - The LPA performs **seven distinct enterprise-related checks** during profile download, each with its own cancel/error reason code
> - Enterprise Profiles can coexist with consumer profiles on the same eUICC, governed by the `numberOfNonEnterpriseProfiles` limit

---

## What Makes a Profile "Enterprise"?

An Enterprise Profile is defined not by its internal structure: it has the same file system, NAA, and applet format as any other profile: but by the presence of an **Enterprise Configuration** in its Profile Metadata (section 2.4a.1.7):

```
EnterpriseConfiguration ::= SEQUENCE {
    enterpriseOid     [0] OBJECT IDENTIFIER,
    enterpriseName    [1] UTF8String (SIZE(0..64)),
    enterpriseRules   [2] SEQUENCE {
        enterpriseRuleBits [0] BIT STRING {
            referenceEnterpriseRule              (0),
            priorityEnterpriseProfile            (1),
            onlyEnterpriseProfilesCanBeInstalled  (2)
        },
        numberOfNonEnterpriseProfiles [1] INTEGER
    } OPTIONAL
}
```

The key fields:

- **enterpriseOid**: A globally unique OID identifying the enterprise. This is **immutable** after installation: it cannot be changed via metadata update.
- **enterpriseName**: Human-readable enterprise name (up to 64 UTF-8 characters).
- **enterpriseRules**: An optional block containing the actual policy rules. When absent, the profile is an Enterprise Profile in name only: no restrictions apply.

---

## The Three Enterprise Rule Bits

The `enterpriseRuleBits` bit string contains three independent flags that control device behaviour:

### Bit 0: `referenceEnterpriseRule` : The Master Switch

This is the most critical bit. When set:

- This Enterprise Profile's rules become the **governing policy** for the entire device
- The eUICC ensures **at most one** installed Enterprise Profile has this bit set
- All Enterprise Rules only take effect on an **Enterprise Capable Device** when the Reference Enterprise Rule is present

Without a profile holding the `referenceEnterpriseRule` bit, none of the other enterprise rules are enforced: even on Enterprise Capable Devices. This design allows multiple enterprise profiles to coexist but ensures there's always one clear authority.

### Bit 1: `priorityEnterpriseProfile` : Always First

When set, the end user experiences two possible restrictions:

- **Strict interpretation**: The end user can enable *only* this Enterprise Profile (no other profiles can be enabled while this rule is active)
- **Priority interpretation**: The end user must enable *this* Enterprise Profile before being able to enable any other Profile

The exact behaviour depends on the Device implementation, but the intent is clear: the enterprise profile takes precedence over personal profiles.

### Bit 2: `onlyEnterpriseProfilesCanBeInstalled` : Corporate-Only Device

When set, the end user can install only Enterprise Profiles. Any attempt to download a non-Enterprise Profile (i.e., one without an `EnterpriseConfiguration` in its metadata) will be rejected by the LPA with reason `enterpriseProfilesOnly` and by the eUICC during installation.

This effectively converts the device into a corporate-managed asset, even if the employee owns the hardware.

### `numberOfNonEnterpriseProfiles` : The Quota

Defines the maximum number of non-Enterprise Profiles that can be **Enabled** simultaneously on the eUICC. Note:

- This counts Enabled profiles, not installed profiles: an employee could have multiple personal profiles installed but only N can be active at once
- The actual limit may be lower if the number of supported eSIM Ports (in MEP mode) is less than this value
- Combined with `priorityEnterpriseProfile`, this creates a "work-first" device model where the corporate profile is always active and personal profiles get remaining port capacity

---

## Enterprise Capable Devices vs Enterprise Owned Devices

The specification distinguishes two device categories:

### Enterprise Capable Device

A Device that supports the Enterprise Profile feature. When an Enterprise Capable Device encounters a profile with `referenceEnterpriseRule` set:

- The LPA enforces Enterprise Rules during download attempts
- The eUICC's Profile Rules Enforcer enforces Enterprise Rules at installation and at runtime
- All seven enterprise-related error checks are active

The LPA on an Enterprise Capable Device performs these checks during profile download (section 3.1.3, step 7):

| Check | Condition | Cancel Reason |
|-------|-----------|---------------|
| Enterprise Profile + existing PPR1 | Enterprise Configuration present AND existing profile has PPR1 | `enterpriseProfileNotAllowed` |
| Enterprise Rules + non-capable device | Enterprise Rules present AND Device is NOT Enterprise Capable | `enterpriseRulesNotAllowed` |
| Enterprise Rules + user rejection | End User rejects Enterprise Rules during consent | `enterpriseRulesNotAllowed` |
| Enterprise OID mismatch | Enterprise OID doesn't match existing Enterprise Profiles' OIDs | `enterpriseOidMismatch` |
| Reference Enterprise Rule error | `referenceEnterpriseRule` bit set but configuration invalid | `enterpriseRulesError` |
| Enterprise-only required | Reference Enterprise Rule requires Enterprise-only but profile isn't Enterprise | `enterpriseProfilesOnly` |
| LPR not supported | Profile contains LPR Configuration but Device/eUICC doesn't support LPR | `lprNotSupported` |

### Non-Enterprise Capable Device

A standard consumer device. It can still install Enterprise Profiles, but:

- Enterprise Rules are **not enforced** : the profile behaves like a regular Operational Profile
- The LPA may still display the enterprise name and rules to the end user for informational purposes
- The eUICC will not reject installation due to enterprise rule violations

### Enterprise Owned Device

An additional category where the device itself is owned by the enterprise. On such devices, the eUICC ensures at most one Enterprise Profile holds the `referenceEnterpriseRule` bit. The spec leaves further Enterprise Owned Device behaviour for future study.

---

## How Enterprise Profiles Coexist with Consumer Profiles

The genius of the Enterprise Profile design is that it doesn't require a separate eUICC or a separate SIM. Enterprise and consumer profiles coexist on the same eUICC, governed by clear rules:

### Scenario 1: BYOD with Corporate Profile

An employee installs a corporate Enterprise Profile alongside their personal profile:

- The Enterprise Profile may carry `priorityEnterpriseProfile` : requiring it to be enabled first or exclusively
- `numberOfNonEnterpriseProfiles` limits how many personal profiles can be active
- `onlyEnterpriseProfilesCanBeInstalled` is typically **not set** in BYOD scenarios: the employee can still install personal profiles
- The end user cannot disable or delete the Enterprise Profile if PPR1/PPR2 are set (these work the same as for any Operational Profile)

### Scenario 2: Corporate-Owned, Personally Enabled (COPE)

The enterprise issues the device with a Reference Enterprise Rule profile:

- `onlyEnterpriseProfilesCanBeInstalled` may be set: blocking personal profile installation entirely
- Or `numberOfNonEnterpriseProfiles` may allow one personal profile
- The enterprise profile is always present and may be undeletable (PPR2)
- In MEP mode, the enterprise profile occupies one eSIM Port while the personal profile (if allowed) occupies another

### Scenario 3: Multiple Enterprises

A contractor or consultant might need profiles from multiple enterprises:

- Multiple Enterprise Profiles can be installed, each with its own `EnterpriseConfiguration`
- Only one can hold the `referenceEnterpriseRule` bit
- All installed Enterprise Profiles must share the same `enterpriseOid` : the LPA rejects mismatched OIDs with `enterpriseOidMismatch`
- This restriction prevents conflicting enterprise policies from different organisations

---

## Enterprise Rules vs Profile Policy Rules

Enterprise Rules and PPRs operate at different layers and serve different purposes:

| Aspect | Profile Policy Rules (PPRs) | Enterprise Rules |
|--------|----------------------------|-----------------|
| **Scope** | Per-profile | Device-wide (via Reference Enterprise Rule) |
| **Set by** | Any Operator (subject to RAT) | Enterprise (via SM-DP+) |
| **Enforced by** | Profile Policy Enabler | Profile Rules Enforcer |
| **Authorised by** | RAT (platform-level, set by manufacturer) | Enterprise OID (immutable after install) |
| **Affects** | This profile only (disable/delete restrictions) | All profiles on the device (installation restrictions, enable priority, quota) |
| **Can be changed** | Unset via ES6/RPM (setting is for further study) | Cannot be changed after install (enterpriseOid immutable) |

They can be combined: an Enterprise Profile can have PPR2 set ("deletion not allowed") AND carry Enterprise Rules that restrict what other profiles can be installed. The Profile Rules Enforcer (section 2.4.12) handles both, applying PPR checks and Enterprise Rule checks independently.

---

## Enterprise Profiles and Local Profile Management

When the end user attempts local profile management operations (enable, disable, delete), the Enterprise Rules affect behaviour:

- **Disabling**: If `priorityEnterpriseProfile` is set and the user tries to disable the Enterprise Profile to enable a personal one, the operation may be blocked: the enterprise profile must stay enabled
- **Deleting**: An Enterprise Profile with PPR2 set cannot be deleted by the end user. The Enterprise Profile's deletion is entirely under enterprise control
- **Enabling**: If `priorityEnterpriseProfile` is set, attempting to enable a personal profile without first enabling the enterprise profile may be blocked

These enforcements happen at the eUICC level: they cannot be bypassed by a modified LPA or a rooted device.

---

## Enterprise Profiles and RPM

Remote Profile Management works with Enterprise Profiles, with important caveats:

- An RPM `Disable` command targeting an Enterprise Profile that must stay enabled (priority rule) will be rejected
- An RPM `Delete` command targeting a profile with PPR2 set will be rejected
- The `UpdateMetadata` RPM command cannot modify the `enterpriseOid` : it's immutable after installation

This means enterprises can use RPM for fleet management operations (enable, disable, update metadata) on their corporate profiles, but the fundamental enterprise policy cannot be removed remotely: providing protection against unauthorised changes even by the enterprise's own SM-DP+ administrators.

---

## Summary

- Enterprise Profiles are a v3.x feature providing corporate governance of eSIM profiles, tagged `#SupportedForEnterpriseV3.0.0#` in the spec
- The `EnterpriseConfiguration` contains an immutable enterprise OID, a name, and optional Enterprise Rules
- Three rule bits control behaviour: `referenceEnterpriseRule` (master switch), `priorityEnterpriseProfile` (enable priority), `onlyEnterpriseProfilesCanBeInstalled` (corporate-only), plus a non-enterprise profile quota
- An Enterprise Capable Device is required for rule enforcement; non-capable devices can still install Enterprise Profiles without restrictions
- Enterprise Rules coexist with PPRs and are enforced by the same Profile Rules Enforcer
- Seven enterprise-specific checks are performed by the LPA during download, each with its own error reason code
- Enterprise and consumer profiles coexist on the same eUICC, governed by clear precedence and quota rules

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp22-v3/62-policy-management-v3">Policy Management in SGP.22 v3.x</a>

</div>

---

*Based on GSMA SGP.22 v3.1 (01 December 2023), Sections 2.4.5: Profile, 2.4a.1.7: Data type: EnterpriseConfiguration, 2.4.12: Profile Rules Enforcer, and 3.1.3: Profile Download and Installation (enterprise-related checks)*


---

← Previous: [Policy Management in SGP.22 v3.x: PPR, RAT, and the Policy Enforcer](62-policy-management-v3) | [Section Index](index)
