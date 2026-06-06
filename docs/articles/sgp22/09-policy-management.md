---
title: "SGP.22 v2.7 — Profile Policy Management: PPRs, RAT, and Profile Policy Enabler"
date: 2026-06-07
---

# SGP.22 v2.7 — Profile Policy Management: PPRs, RAT, and Profile Policy Enabler

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.22 Consumer RSP]({{ site.baseurl }}/docs/articles/sgp22/) > Profile Policy Management: PPRs, RAT, and Profile Policy Enabler**

> **💡 Why this matters:** Profile Policy Management is the mechanism that lets enterprises lock down corporate eSIMs, prevents users from accidentally deleting their primary carrier profile, and gives operators fine-grained control over what can and can't happen to their profiles. If you've ever wondered why you can't delete a carrier profile on your phone, this is why.

> **Key takeaways:**
> - Only two Profile Policy Rules exist in v2.7: **PPR1** ("Disabling not allowed") and **PPR2** ("Deletion not allowed")
> - The **Rules Authorisation Table (RAT)** is set at manufacturing time and controls *which operators* can set *which PPRs* and whether *End User consent* is required
> - Each RAT entry is a **PPAR** (Profile Policy Authorisation Rule) combining: PPR identifier, Allowed Operators list, and Consent Required flag
> - The **Profile Policy Enabler** verifies PPRs at installation time, during post-install updates, and enforces them during runtime
> - PPRs can override user intent — but a Provisioning Profile always takes priority (it can implicitly disable an Operational Profile even if PPR1 is set)
> - There are two notable RAT configurations: "all PPRs allowed with consent" (consumer-friendly) and "all PPRs forbidden" (fully open device)

---

Profile Policy Management (section 2.9) is SGP.22's answer to a fundamental tension: the eUICC is owned by the end user, but the profiles on it are owned by operators. Who gets to decide what happens to a profile? Can the user delete it? Can the operator lock it in place? The answer is a three-layer system of rules (PPRs), authorisation tables (RAT), and enforcement (PPE).

---

## Layer 1: Profile Policy Rules (PPRs)

PPRs (section 2.9.1) are flags set by the Profile Owner (the operator) in the Profile Metadata. They travel with the profile and are enforced by the eUICC. SGP.22 v2.7 defines exactly two:

| PPR | Name | Effect |
|---|---|---|
| **PPR1** | Disabling of this Profile is not allowed | The ISD-R SHALL reject any attempt to disable this profile. The user cannot switch away from it. |
| **PPR2** | Deletion of this Profile is not allowed | The ISD-R SHALL reject any attempt to delete this profile. It's permanent until a memory reset. |

These are encoded as bits in the `PprIds` ASN.1 BIT STRING (section 2.4a.1.1):
- Bit 0 set = PPR1 active
- Bit 1 set = PPR2 active

A profile MAY have zero, one, or both PPRs. Test Profiles SHOULD NOT contain any PPRs. PPRs MAY only be provided for a Profile that contains an EF-IMSI (i.e., a profile that actually provides network access).

**Important nuance:** PPR1 only prevents *explicit* disabling. If a Provisioning Profile needs to be enabled, the eUICC SHALL implicitly disable the currently enabled Operational Profile *regardless of PPR1* (section 2.4.5.2). This is the one exception — provisioning always takes priority.

---

## Layer 2: Rules Authorisation Table (RAT)

The RAT (section 2.9.2) answers the question: *which operators are allowed to set which PPRs?* It's defined at the eUICC platform level and is set at manufacturing time or during initial device setup (provided no Operational Profile is yet installed). The OEM or EUM is responsible for its content.

The RAT is persistent — it survives eUICC Memory Reset (ES10b.eUICCMemoryReset does not affect it). This means the device manufacturer's policy decisions are baked into the chip permanently.

### Profile Policy Authorisation Rules (PPAR)

Each entry in the RAT is a **PPAR** (section 2.9.2.1) containing three fields:

| Field | Description |
|---|---|
| **PPR Identifier** | Which PPR(s) this rule applies to (can be PPR1, PPR2, or both, encoded as a `PprIds` bitmask) |
| **Allowed Operators** | List of Profile Owners allowed to use this PPR. Supports wildcards at MCC/MNC and GID level |
| **End User Consent Required** | Boolean: must the LPA get explicit user consent before installing a profile with this PPR? |

### Operator Matching with Wildcards

The `Allowed Operators` field uses the `OperatorId` type (section 2.4a.1.2), which contains MCC+MNC and optional GID1/GID2. Wildcarding works as follows:

- **MCC/MNC digits**: Any nibble set to `E` acts as a wildcard. Setting all to `EEEEEE` means "any operator."
- **GID1/GID2**: An empty value (length zero) acts as a wildcard. An omitted value only matches when the corresponding field in the profile's `profileOwner` is also absent.

This allows granular rules: "Only Vodafone UK (234-15) can set PPR1" or "Any operator can set PPR2, but only with user consent."

### Multiple PPARs and Priority

When multiple PPARs apply to the same PPR, the first matching PPAR (in order) wins. The RAT order is significant. Here's the example from the spec:

```
PPR1, OP-A, consent=false
PPR2, OP-B, consent=false
PPR1+PPR2, *, consent=true
```

With this configuration:
- **OP-A**: can use PPR1 without consent; PPR2 requires consent (third row wildcard match)
- **OP-B**: can use PPR2 without consent; PPR1 requires consent (third row wildcard match)
- **Any other operator**: can use both PPR1 and PPR2, but always requires consent

If no PPAR exists for a given PPR, that PPR is **forbidden** for all operators.

---

## Notable RAT Configurations (2.9.2.2)

The spec defines two canonical RAT setups:

### Consumer-Friendly: "All PPRs Allowed, Consent Required"

```
PPR1+PPR2, *, consent=true
```

This is the most common consumer device configuration. Any operator can set PPR1 or PPR2, but the user must explicitly consent during profile installation. The LPA SHALL present a clear explanation of what the PPRs mean before asking for consent.

This is what you typically see on iPhones and Android devices — the carrier can lock a profile, but only after you've agreed to it during installation.

### Fully Open: "All PPRs Forbidden"

```
<no entries in RAT>
```

No PPARs means no PPRs can ever be set. This is the configuration for devices where the end user has complete control — they can always delete or disable any profile. This might be appropriate for developer devices, test platforms, or markets where regulators require full user control.

---

## Layer 3: Profile Policy Enabler (PPE)

The Profile Policy Enabler (section 2.9.3) is the runtime enforcement component. It operates at three distinct moments:

### 3a. PPR Verification at Installation Time (2.9.3.1)

When a profile is being installed and its metadata contains PPRs, the eUICC SHALL verify each PPR against the RAT:

1. For each PPR in the profile metadata:
   - Is the PPR known? (PPR1 or PPR2 — any other value is rejected)
   - Is the PPR allowed for this Profile Owner? (check RAT for a matching PPAR)
   - If no matching PPAR: **reject the installation**
   - If PPAR requires End User consent: LPA must obtain consent before proceeding

If the eUICC determines that a PPR is not allowed, it returns `pprNotAllowed(15)` in the Profile Installation Result and the installation fails.

The LPA also performs a parallel check (section 2.9.2.4) before even sending the profile to the eUICC, using the RAT retrieved via ES10b.GetRAT. This is a performance optimisation — it's faster to reject at the LPA level than to send a multi-kilobyte BPP to the eUICC only to have it rejected.

### 3b. PPR Verification During Post-Install Update (2.9.3.2)

PPRs can be updated after installation via **ES6.UpdateMetadata** (section 5.4.1). When an operator pushes new PPRs remotely, the same verification happens:

- The eUICC checks the new PPRs against the RAT
- If the update would result in a PPR that wasn't previously allowed, it's rejected
- The PPR update is atomic — if any PPR fails verification, none are applied

This prevents operators from escalating their privileges post-install. An operator who installed a profile without PPR1 cannot later add it via OTA update unless the RAT allows it.

### 3c. PPR Enforcement at Runtime (2.9.3.3)

During normal operation, when the LPA (or LPAe) requests a profile operation, the ISD-R checks the active PPRs:

- **EnableProfile** on a different profile → ISD-R checks if current profile has PPR1. If yes, reject (unless the target is a Provisioning Profile).
- **DisableProfile** on current profile → ISD-R checks PPR1. If set, reject.
- **DeleteProfile** → ISD-R checks PPR2. If set, reject.
- **eUICC Memory Reset** → This bypasses PPR2. It's the nuclear option that wipes everything.

---

## The PPR Lifecycle

```
Manufacturing          Profile Install        Post-Install          Runtime
     │                      │                      │                   │
     ▼                      ▼                      ▼                   ▼
 RAT burned            SM-DP+ sets           ES6.UpdateMetadata   ISD-R checks
 into eUICC            PPRs in metadata      can modify PPRs      PPRs on every
 by OEM/EUM            ──────────────────    ──────────────────   ES10c operation
                        eUICC verifies        eUICC re-verifies    ──────────────────
                        against RAT           against RAT          Enable/Disable/
                        ──────────────────    ──────────────────   Delete gated
                        User consent          Update atomic        by PPR flags
                        if required
```

---

## Practical Implications

**For device manufacturers:** Your RAT configuration is a product decision. A consumer-friendly RAT (all PPRs allowed with consent) maximises carrier flexibility. A fully open RAT (no PPRs) gives users total control but may make carriers reluctant to support your device.

**For operators:** PPRs are your lock-in mechanism, but they're constrained by the RAT and require user consent in most configurations. Design your profile metadata carefully — adding PPR1 without consent won't work if the RAT requires it.

**For enterprise IT:** PPR1 is the enterprise eSIM control. Deploy profiles with PPR1 set, and employees can't switch away from the corporate plan. Combine with a locked RAT on corporate-issued devices for maximum control.

**For developers:** Always test with a RAT that either forbids all PPRs or allows them with consent. The `pprNotAllowed(15)` error during installation is easy to misdiagnose if you don't know to check the RAT.

---

Profile Policy Management is the bridge between user freedom and operator control. It's a carefully balanced system where the device manufacturer sets the ground rules (RAT), the operator declares its intent (PPRs), and the eUICC enforces everything neutrally. In the next article, we'll look at how the eUICC reports back to the ecosystem — the notification framework that keeps operators informed about what's happening on the device.
