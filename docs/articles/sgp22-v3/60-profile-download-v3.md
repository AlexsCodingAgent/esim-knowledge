---
description: "Documents profile download in SGP.22 v3.x — the four Operator-side sub-processes from Contract Subscription through Subscription Activation and three eUICC-side sub-procedures, with v3.x additions for enterprise profiles and RPM chaining."
layout: default
title: "Profile Download & Installation in SGP.22 v3.x"
date: 2026-06-07
---

# Profile Download & Installation in SGP.22 v3.x

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.22 v3.x Unified RSP]({{ site.baseurl }}/docs/articles/sgp22-v3/) > Profile Download & Installation in SGP.22 v3.x**

> **💡 Why this matters:** Profile download is the single most important operation in the entire eSIM ecosystem: it's the moment a subscriber's mobile identity materialises on the eUICC. Every other v3.x feature: Multiple Enabled Profiles, Remote Profile Management, Device Change, enterprise controls: assumes the download and installation procedure already exists and works reliably. Understanding this flow is foundational to understanding everything else in SGP.22. The v3.x download procedure is largely evolved from v2.x, but adds critical new checks: enterprise profile validation, RPM package chaining, MEP-aware PPR enforcement, and manufacturer-authorised certificate verification.

> **Key takeaways:**
> - Profile download has four sub-processes: **Contract Subscription → Download Preparation → Contract Finalisation → Subscription Activation** (all Operator/SM-DP+ side)
> - The actual download procedure has three sub-procedures: **Authentication & eligibility → Download Confirmation → Profile Installation**
> - Three discovery paths exist: **Activation Code**, **SM-DS Event**, or **Default SM-DP+ address**
> - The eUICC generates a **one-time key pair** (otPK/otSK.EUICC.KA) used for BPP binding: ensuring only the target eUICC can decrypt the profile
> - A **Profile Installation Result** is signed by the eUICC and delivered to the SM-DP+, providing cryptographic proof of installation success or failure
> - The SM-DP+ tracks each Profile through a **lifecycle state machine** (Available → Allocated → Linked → Confirmed → Released → Downloaded → Installed/Error)
> - v3.x adds enterprise checks, RPM chaining via `rpmPending`, and MEP-aware PPR validation during download

---

## The Big Picture: Four Sub-Processes on the Operator Side

Before the end user ever sees a download prompt, the Operator and SM-DP+ execute four sub-processes (section 3.1.1):

### A. Contract Subscription Process (Informative)

The end user selects an Operator and provides billing information, optionally the target device's EID and IMEI. The Operator may verify device/eUICC compatibility at this stage. This is out of scope of SGP.22 but provides inputs for what follows.

### B. Download Preparation Process

1. The Operator calls `ES2+.DownloadOrder` on the SM-DP+, providing the EID (optional but recommended) and either a `ProfileType` or specific `ICCID`.
2. The SM-DP+ reserves the ICCID: at this point it may pick a pre-generated Protected Profile Package from inventory or generate one.
3. The SM-DP+ returns the ICCID.
4. The Operator optionally generates a MatchingID.
5. The Operator calls `ES2+.ConfirmOrder` with the ICCID, EID, MatchingID, optional Confirmation Code, SM-DS addresses, and a `releaseFlag`.
6. The SM-DP+ either acknowledges the Operator-generated MatchingID or generates one and returns it.

The `releaseFlag` is critical: when set to `true`, the profile is immediately ready for download. When `false`, the Operator must later call `ES2+.ReleaseProfile` : this decouples backend provisioning (HLR registration, etc.) from the end-user download experience.

### C. Contract Finalisation

The Operator delivers the MatchingID and SM-DP+ address to the end user: typically via an Activation Code (QR code), but this could also be through SM-DS Event delivery or simply instructing the user to trigger a Default SM-DP+ download on first boot.

### D. Subscription Activation (Optional)

If the Operator couldn't complete backend provisioning during step B, it does so now and calls `ES2+.ReleaseProfile` to unlock the download.

## The Download Procedure: Three Sub-Procedures

Once triggered by the end user, the actual download and installation procedure (section 3.1.3) runs in three phases.

### Phase 1: Authentication & Eligibility Check

The LPA discovers the SM-DP+ through one of three paths:

- **Activation Code** (option a): The LPA parses the QR code to extract the SM-DP+ address, Activation Code Token (serving as MatchingID), and optionally an SM-DP+ OID and eSIM CA RootCA Public Key indicator.
- **SM-DS Event** (option b): The LPA retrieves an Event from an SM-DS containing the SM-DP+ address and EventID.
- **Default SM-DP+** (option c): The LPA retrieves the Default SM-DP+ address from the eUICC via `ES10a.GetEuiccConfiguredData`.

The Common Mutual Authentication procedure (section 3.0.1) then establishes a secure session:

1. The LPA sends `ES9+.InitiateAuthentication` with the eUICC's challenge and supported eSIM CA RootCA PKIDs.
2. The SM-DP+ authenticates to the eUICC via its certificate chain.
3. The eUICC authenticates to the SM-DP+.
4. The LPA calls `ES9+.AuthenticateClient` with the MatchingID, Device Info, and operation type.

At this point the SM-DP+ performs critical verifications:

- **Pending order exists** for the provided MatchingID
- **EID matches** (if the order was linked to an EID)
- **Profile is in Released state** (or Downloaded state for a retry)
- **Download attempt count** hasn't exceeded the limit
- **Eligibility checks** pass

The SM-DP+ returns `smdpSigned2` containing the TransactionID, a Confirmation Code Required flag, and optionally a `bppEuiccOtpk` (for retry scenarios) and `rpmPending` (if an RPM Package is also waiting).

### The LPA's Pre-Download Validation (v3.x Specific)

Before proceeding, the LPA checks if the profile can be installed. This is where v3.x adds significant new logic:

- **PPR check against RAT**: The LPA retrieves the Rules Authorisation Table (`ES10b.GetRAT`) and verifies that all PPRs in the Profile Metadata are allowed for this Profile Owner.
- **Enterprise Profile checks**: If the Profile Metadata contains an Enterprise Configuration, the LPA validates:
  - No conflict with an existing PPR1 profile (`enterpriseProfileNotAllowed`)
  - Device is Enterprise Capable if Enterprise Rules are present (`enterpriseRulesNotAllowed`)
  - Enterprise OID matches any already-installed Enterprise Profile (`enterpriseOidMismatch`)
  - Reference Enterprise Rule validity (`enterpriseRulesError`)
  - If Reference Enterprise Rule requires Enterprise-only profiles, the new profile must be Enterprise (`enterpriseProfilesOnly`)
- **MEP-aware PPR1 check**: On an eUICC supporting MEP, PPR1 profiles are not rejected: the restriction only applies to single-enabled-profile (SEP) eUICCs.

If any of these checks fail, the LPA cancels the session with the appropriate reason code.

### Phase 2: Download Confirmation

With all checks passed, the LPA requests end user consent:

1. **Confirmation Code** (if required): The end user enters the code provided separately by the Operator. The LPA hashes it as `SHA256(SHA256(code) | TransactionID)`.
2. **PPR/Enterprise Rule consent**: If the RAT requires end user consent for certain PPRs, or if an Enterprise Profile requires immediate enabling, the LPA displays a clear message and requests Strong Confirmation.
3. **Simple Confirmation**: If no special rules apply, a simple yes/no prompt suffices.

If the end user agrees, the LPA calls `ES10b.PrepareDownload`:

- The eUICC verifies the SM-DP+ signatures (CERT.DPpb.SIG, smdpSignature2)
- The eUICC generates a one-time key pair (otPK.EUICC.KA, otSK.EUICC.KA) : unless the SM-DP+ specified a reusable `bppEuiccOtpk` from a previous attempt
- The eUICC returns `euiccSigned2` containing the TransactionID and the one-time public key

The LPA then calls `ES9+.GetBoundProfilePackage` with the eUICC's signed data. The SM-DP+:

1. Verifies `euiccSignature2`
2. Verifies the Confirmation Code hash (if required)
3. Generates the **Bound Profile Package** : either creating a new BPP, reusing an existing one, or rebinding a previously generated BPP
4. Optionally notifies the Operator via `ES2+.HandleNotification`
5. Returns the BPP and sets the Profile state to 'Downloaded'

The LPA performs a final metadata consistency check: the PPRs and Enterprise Configuration in the BPP must match what was returned earlier in `AuthenticateClient`. If anything changed, the session is cancelled with `metadataMismatch`.

### Phase 3: Profile Installation

The LPA segments the BPP into APDU-sized chunks (the **Segmented Bound Profile Package**, see section 2.5.5) and feeds them to the eUICC via repeated `ES10b.LoadBoundProfilePackage` calls. The installation sequence is:

1. **InitialiseSecureChannel**: Key agreement: the eUICC generates session keys (S-ENC, S-MAC) using the one-time keys
2. **ConfigureISDP**: Creates the ISD-P (Issuer Security Domain: Profile) on the eUICC
3. **StoreMetadata**: Writes Profile Metadata including PPRs: the eUICC's Profile Policy Enabler verifies each PPR against the RAT
4. **ReplaceSessionKeys** (optional): If the profile was protected with separate Profile Protection Keys (PPK-ENC, PPK-MAC), the session keys are replaced
5. **LoadProfileElements**: The actual profile content: NAA keys, file system, applets: is loaded and installed

After successful installation, the eUICC generates a signed **Profile Installation Result** containing:

- Notification Metadata (sequence number, operation type, recipient address, ICCID)
- Transaction ID
- Final result (success or error with reason code)
- SM-DP+ OID
- eUICC signature for non-repudiation

The LPA delivers this result to the SM-DP+ via `ES9+.HandleNotification`, which then terminates the download order and notifies the Operator. The eUICC stores the result until the LPA explicitly deletes it via `ES10b.RemoveNotificationFromList`.

---

## Error Handling During Download

The specification defines careful error handling at multiple layers (section 3.1.5):

### SM-DP+ Side: Attempt Limits

The SM-DP+ maintains two counters per Profile:

- **Download attempt counter**: Limits how many times the end user can attempt the download procedure
- **Confirmation Code attempt counter**: Limits incorrect Confirmation Code entries

When either limit is exceeded, the Profile transitions to 'Error' state and the Operator is notified.

### eUICC Side: Temporary vs Permanent Errors

Error reasons are classified as either:

- **Temporary** (retry allowed): `installFailedDueToInsufficientMemoryForProfile(10)`, `installFailedDueToInterruption(11)`
- **Permanent** (no retry): All other error reasons

During Profile Installation, the eUICC may encounter unexpected TLVs. The spec allows three behaviours:

- Process `GetEUICCChallenge` (new session) or `CancelSession` (termination) normally
- Optionally process other ES10 commands
- Reject everything else with status words '69 85' or '6A 88'

The eUICC does **not** discard session state for rejected TLVs, allowing the LPA to potentially recover.

### Session State and Interruptions

If the eUICC loses power or the LPA changes eSIM Ports (in MEP-B mode) mid-session, the eUICC discards session state. The Profile Installation Result is written to non-volatile memory before being delivered, so installation outcome is always known even after a power loss.

---

## Profile Lifecycle at the SM-DP+

The SM-DP+ tracks each Profile through a well-defined state machine (section 3.1.6):

| State | Meaning |
|-------|---------|
| **Available** | Profile exists in SM-DP+ inventory, not yet reserved |
| **Allocated** | Reserved for download, not yet linked to an EID |
| **Linked** | Reserved and linked to a specific EID |
| **Confirmed** | MatchingID and optional Confirmation Code assigned |
| **Released** | Ready for download: network provisioning complete |
| **Downloaded** | BPP has been delivered to the LPA |
| **Installed** | Profile successfully installed on the eUICC |
| **Error** | Download failed: CC retry exceeded, download retry exceeded, end user rejection, or permanent error |
| **Unavailable** | Profile cannot be reused |

Additionally, an SM-DP+ that receives eUICC Notifications may track runtime states: **Enabled**, **Disabled**, and **Deleted**.

---

## How v3.x Extends the Download Procedure

While the core download flow is inherited from v2.x, v3.1 adds several important extensions:

- **Enterprise Profile validation**: Seven new cancel/error reason codes for enterprise-specific conditions
- **RPM chaining via `rpmPending`**: After installation, the LPA is directed to start a new RSP Session for RPM command execution
- **V3-specific FQDN for TLS**: The LPA prepends "rsp3-" to the SM-DP+ FQDN, allowing the server to select a Public CA TLS certificate for v3 devices
- **MEP-aware PPR handling**: PPR1 is not enforced during download on MEP-capable eUICCs
- **Manufacturer-authorised certificates**: The LPA can restrict allowed eSIM CA RootCA PKIDs based on the Activation Code or Default SM-DP+ configuration
- **Service Provider messages**: The SM-DP+ can include localised text messages for display to the end user during consent prompts

---

## Summary

- Profile download is the core provisioning flow: Operator prepares a profile, end user triggers download, SM-DP+ binds it to the eUICC, and the LPA installs it
- The process has three phases: authentication & eligibility, download confirmation, and installation
- Three discovery paths: Activation Code, SM-DS Event, or Default SM-DP+
- The eUICC's one-time key pair ensures cryptographic binding: only the target eUICC can decrypt the bound profile
- v3.x adds enterprise checks, RPM chaining, MEP-aware PPR validation, and manufacturer-authorised certificate restrictions
- The SM-DP+ lifecycle state machine tracks each profile from Available through to Installed or Error
- Error handling distinguishes temporary errors (retry allowed) from permanent errors (profile moves to Error state)

---

<div align="center" markdown="1">

← Previous: [eUICC Updates and Profile Content Management]({{ site.baseurl }}/docs/articles/sgp22-v3/59-euicc-updates-pcm)

Next: [Profile Protection & BPP Security]({{ site.baseurl }}/docs/articles/sgp22-v3/61-profile-protection-bpp) →

</div>

---

*Based on GSMA SGP.22 v3.1 (01 December 2023), Sections 3.1.1: Profile Download Initiation, 3.1.3: Profile Download and Installation, 3.1.4: Limitation for Profile Installation, 3.1.5: Error Handling Within the Profile Download and Installation Procedure, and 3.1.6: Profile Lifecycle at SM-DP+*


---

← Previous: [eUICC Updates and Profile Content Management: Lifecycle Beyond Download](59-euicc-updates-pcm) | [Section Index](index) | Next: [Profile Protection & BPP Security: How eSIM Profiles Stay Secret](61-profile-protection-bpp) →
