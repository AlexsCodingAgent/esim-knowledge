---
description: "Details SGP.22 v3.x policy management : PPR1 and PPR2 rules extended with MEP-aware enforcement, the manufacturer-set Rules Authorisation Table, and the Profile Policy Enabler with groundwork for Enterprise Rules."
layout: default
title: "Policy Management in SGP.22 v3.x: PPR, RAT, and the Policy Enforcer"
date: 2026-06-07
---

# Policy Management in SGP.22 v3.x: PPR, RAT, and the Policy Enforcer

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.22 v3.x Unified RSP]({{ site.baseurl }}/docs/articles/sgp22-v3/) > Policy Management in SGP.22 v3.x: PPR, RAT, and the Policy Enforcer**

> **💡 Why this matters:** Without policy management, any profile on your eSIM could be disabled or deleted by anyone: the end user, a malicious app, even a different operator. Profile Policy Management gives Profile Owners (operators) the ability to enforce conditions of use: a corporate-issued profile that can't be deleted by the employee, or a subsidised-device profile that can't be disabled until the contract ends. The system is carefully balanced: the eUICC manufacturer sets the ground rules (RAT), the operator sets per-profile policies (PPRs), and the eUICC enforces them (PPE). v3.x extends this with MEP-aware enforcement and lays groundwork for Enterprise Rules.

> **Key takeaways:**
> - Three components: **Profile Policy Rules (PPRs)** set by operators, **Rules Authorisation Table (RAT)** set by the manufacturer, and **Profile Policy Enabler (PPE)** on the eUICC
> - Two PPRs defined: **PPR1** : "Disabling of this Profile is not allowed", **PPR2** : "Deletion of this Profile is not allowed"
> - The **RAT** defines which operators can use which PPRs, and whether end user consent is required: using MCC/MNC wildcards for flexible operator matching
> - Both the **LPA** (during download) and the **eUICC** (during installation and operation) independently verify PPRs against the RAT: a dual-layer enforcement model
> - **MEP changes everything for PPR1**: On MEP-capable eUICCs, PPR1 is simply not enforceable: the RAT SHALL NOT contain PPAR entries for PPR1
> - The RAT survives eUICC Memory Reset: it's a platform-level configuration set at manufacturing or initial device setup
> - v3.x introduces **Enterprise Rules** as a separate policy layer, enforced by the Profile Rules Enforcer alongside PPRs

---

## The Three Pillars of Policy Management

Profile Policy Management (section 2.9) rests on three components working together:

### Pillar 1: Profile Policy Rules (PPR) : What the Operator Wants

PPRs are the operator's expression of intent. They're set by the SM-DP+ in the Profile Metadata and travel with the profile throughout its lifecycle. Two rules are defined in v3.1 (section 2.9.1):

- **PPR1**: *"Disabling of this Profile is not allowed"* : The end user cannot disable this profile through the LUI. If it's enabled, it stays enabled.
- **PPR2**: *"Deletion of this Profile is not allowed"* : The end user cannot delete this profile. It remains on the eUICC regardless of user action.

A Profile may have zero, one, or both PPRs set. Test Profiles should not contain PPRs. PPRs may only be provided for profiles containing an EF IMSI (i.e., operational profiles).

PPRs are encoded as a bit string in the Profile Metadata:

```
PprIds ::= BIT STRING {
    pprUpdateControl(0),  -- controls PPR update mechanism via ES6
    ppr1(1),              -- 'Disabling of this Profile is not allowed'
    ppr2(2)               -- 'Deletion of this Profile is not allowed'
}
```

A bit set to `'1'` indicates the corresponding PPR is active.

### Pillar 2: Rules Authorisation Table (RAT) : What the Platform Allows

The RAT is the gatekeeper. It's defined at the **eUICC platform level** and determines which operators are allowed to use which PPRs, and under what conditions (section 2.9.2).

The RAT contains a list of **Profile Policy Authorisation Rules (PPARs)**, each specifying:

| Field | Description |
|-------|-------------|
| **PPR Identifier** | Which PPR(s) this rule applies to (PPR1, PPR2, or both) |
| **Allowed Operators** | Which operators (by MCC/MNC + optional GID1/GID2) can use this PPR. Wildcards supported. |
| **End User Consent Required** | Whether the LPA must obtain explicit end user consent before installing a profile with this PPR (true/false) |

The RAT is initialised at eUICC manufacturing time or during initial device setup (before any operational profile is installed). The Device manufacturer or EUM is responsible for its content. Critically, the RAT **survives** `ES10c.eUICCMemoryReset` : it's a permanent platform policy.

**Wildcard matching** is flexible:

- Any MCC/MNC digit can be wildcarded by setting the nibble to `'E'` (e.g., `'EEEEEE'` matches all operators)
- GID1/GID2 can be wildcarded by setting an empty value (length zero)
- An omitted GID1/GID2 matches only an operator ID where the corresponding field is absent

**PPAR ordering matters**: When a Profile Owner matches multiple PPARs for the same PPR, the **first matching PPAR** determines whether end user consent is required.

**Example RAT configuration:**

| PPR | Allowed Operators | End User Consent |
|-----|-------------------|-----------------|
| PPR1 | OP-A | false |
| PPR2 | OP-B | false |
| PPR1, PPR2 | * (all operators) | true |

With this configuration:
- **OP-A**: Can use PPR1 without consent, PPR2 with consent
- **OP-B**: Can use PPR1 with consent, PPR2 without consent
- **Any other operator**: Can use PPR1 and PPR2, but only with end user consent

**Notable preset configurations** (section 2.9.2.2):

- **"All PPRs allowed for all operators, consent required"**: Single PPAR with PPR1+PPR2, wildcard operator, consent=true. This is the most permissive: any operator can use any PPR, but the user always gets a say.
- **"All PPRs forbidden"**: Empty RAT (no PPARs). No operator can use any PPR. Profiles containing PPRs will be rejected at installation.

### Pillar 3: Profile Policy Enabler (PPE) : The Enforcer

The PPE lives on the eUICC and has two jobs (section 2.9.3):

1. **Verification at installation time**: Before accepting a profile, the PPE verifies each PPR against the RAT
2. **Runtime enforcement**: When a local profile management operation (enable, disable, delete) is requested, the PPE enforces the PPRs of the affected profiles

---

## Dual-Layer Verification: LPA + eUICC

One of the most important design features of SGP.22 policy management is that **both the LPA and the eUICC independently verify PPRs**. This provides defence in depth:

### Layer 1: LPA Verification (During Download)

During the Profile Download and Installation procedure (section 3.1.3, step 7), the LPA retrieves the RAT via `ES10b.GetRAT` and the list of installed profiles via `ES10c.GetProfilesInfo`. It then checks:

1. Each PPR in the incoming profile's metadata is checked against the RAT
2. If any PPR is not allowed, the LPA cancels with `pprNotAllowed`
3. If PPR1 is set and an operational profile is already installed (SEP mode only), the LPA cancels with `pprNotAllowed`
4. If end user consent is required, the LPA prompts the user with a descriptive message

The LPA also verifies PPRs a second time after BPP download (step 12) : checking that the metadata in the bound package hasn't changed from what was received earlier.

### Layer 2: eUICC Verification (During Installation)

During `ES8+.StoreMetadata` processing (section 3.1.3.3, step 4a), the PPE on the eUICC performs its own independent PPR verification:

- Same RAT-based check as the LPA, but without considering the "End User Consent Required" field: the PPE cannot enforce that the LPA obtained consent; that's the LPA's responsibility
- If the Enterprise Configuration requires Enterprise-Only profiles, the PPE verifies the incoming profile is indeed an Enterprise Profile
- If verification fails, installation is rejected and a signed Profile Installation Result with the appropriate error reason is generated

This dual-layer approach means that even if a compromised LPA tried to install a profile with unauthorised PPRs, the eUICC's PPE would reject it independently.

### PPR Update After Installation

A PPR can be **unset** after installation via `ES6.UpdateMetadata` (by the Profile Owner) or via the RPM `UpdateMetadata` command. Setting a PPR after installation is "for further study" : the spec currently only defines removal, not addition.

---

## MEP and PPR1: The Fundamental Conflict

Multiple Enabled Profiles (MEP) creates an inherent conflict with PPR1. If PPR1 means "this profile cannot be disabled", what happens when the user wants to enable a different profile but the eUICC supports multiple enabled profiles?

The specification resolves this cleanly (section 2.9.2.1):

> *The RAT of an eUICC supporting MEP SHALL NOT contain any PPAR for PPR1.*

In other words, **PPR1 is incompatible with MEP**. On a MEP-capable eUICC, no operator can set PPR1: profiles with PPR1 set will be rejected during installation by both the LPA and the eUICC. This makes sense: with MEP, enabling a new profile doesn't require disabling the current one, so the "disabling not allowed" restriction loses its meaning.

This also means that device manufacturers choosing to support MEP must accept that PPR1-based business models (e.g., permanently locked subsidised-device profiles) won't work on their platform. Operators who rely on PPR1 must target SEP-only devices.

---

## PPR Enforcement at Runtime

When the end user (or the LPA on their behalf) attempts a local profile management operation, the PPE checks the relevant PPRs (section 2.9.3.3):

- **Disable attempt on a PPR1 profile**: Rejected. The PPE SHALL NOT allow the profile to be disabled.
- **Delete attempt on a PPR2 profile**: Rejected. The PPE SHALL NOT allow the profile to be deleted.

**Exception: Test Profiles** (section 2.9.3.3.2): When a Test Profile needs to be enabled while the currently enabled profile has PPR1 set, the PPE does **not** enforce PPR1. This allows device testing without being locked out by production profiles. The eUICC implicitly disables the operational profile to enable the test profile, and re-enables the operational profile when the test profile is disabled: maintaining the spirit of PPR1 while permitting test operations.

**Exception: Provisioning Profiles**: The LPA can enable a Provisioning Profile even when the currently enabled operational profile has PPR1 set. The eUICC implicitly disables the operational profile for the duration of provisioning.

---

## v3.x Extensions: Enterprise Rules and RPM

v3.x extends the policy framework in two important ways:

### Enterprise Rules

The Profile Rules Enforcer (section 2.4.12) now enforces not just PPRs but also **Enterprise Rules** : a separate policy layer for enterprise-owned devices. Enterprise Rules can:

- Require that only enterprise profiles can be installed (`onlyEnterpriseProfilesCanBeInstalled`)
- Define a priority enterprise profile that must be enabled first (`priorityEnterpriseProfile`)
- Limit the number of non-enterprise profiles that can be enabled (`numberOfNonEnterpriseProfiles`)

Enterprise Rules are enforced by the eUICC independently of PPRs, creating a multi-layer policy stack.

### RPM and Policy

Remote Profile Management (RPM) commands must respect PPRs: an RPM Disable command targeting a profile with PPR1 set will be rejected, and an RPM Delete targeting a PPR2 profile will be rejected. RPM Commands targeting Test Profiles are always rejected: RPM is for Operational Profiles only.

---

## Summary

- Profile Policy Management uses three components: PPRs (operator's intent), RAT (platform's authorisation), and PPE (eUICC enforcement)
- Two PPRs exist: PPR1 (disable not allowed) and PPR2 (delete not allowed)
- The RAT uses flexible wildcard matching to define which operators can use which PPRs, with optional end user consent requirements
- Both LPA and eUICC independently verify PPRs: a dual-layer security model
- MEP and PPR1 are mutually exclusive: MEP-capable eUICCs must not allow PPR1
- The RAT survives memory resets and is set at the platform level by the manufacturer
- v3.x adds Enterprise Rules as an additional policy layer enforced alongside PPRs

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp22-v3/61-profile-protection-bpp">Profile Protection & BPP Security</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp22-v3/63-enterprise-profiles">Enterprise Profiles in SGP.22 v3.x</a> →

</div>

---

*Based on GSMA SGP.22 v3.1 (01 December 2023), Section 2.9: Profile Policy Management, and related sections on Profile Rules Enforcer (2.4.12) and Enterprise Configuration (2.4a.1.7)*


---

← Previous: [Profile Protection & BPP Security: How eSIM Profiles Stay Secret](61-profile-protection-bpp) | [Section Index](index) | Next: [Enterprise Profiles in SGP.22 v3.x: Corporate Control of eSIMs](63-enterprise-profiles) →
