---
description: "Explains Device Change and Profile Recovery in SGP.22 v3.x — the standardised GSMA procedure for transferring subscriptions between devices with the SM-DP+ orchestrating the flow and Profile Recovery restoring profiles on the old device on failure."
layout: default
title: "Device Change and Profile Recovery: Moving eSIMs Between Devices"
date: 2026-06-06
---

# Device Change and Profile Recovery: Moving eSIMs Between Devices

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.22 v3.x Unified RSP]({{ site.baseurl }}/docs/articles/sgp22-v3/) > Device Change and Profile Recovery: Moving eSIMs Between Devices**

> **💡 Why this matters:** In v2.x, there is no standard way to transfer an eSIM profile from one device to another. If you buy a new phone, you must either contact your operator for a new eSIM activation code or use proprietary "eSIM Quick Transfer" features that each manufacturer implements differently. Device Change in v3.x provides a standardised, GSMA-specified procedure: the end user initiates the transfer on the old device, the SM-DP+ orchestrates everything, and a new profile lands on the new device. If something goes wrong (e.g., the new device can't install the profile), Profile Recovery lets you restore the profile on the old device: so you're never left without service.

> **Key takeaways:**
> - Device Change and Profile Recovery are **v3.x-only features** (`#SupportedForDcV3.X.Y#`)
> - Device Change allows an end user to transfer a subscription from an **old Device** to a **new Device**, with the SM-DP+ orchestrating the entire flow
> - Two modes: **requestToDp** (SM-DP+ manages the transfer, optionally issuing a new profile) and **usingStoredAc** (the profile stores a pre-generated Activation Code for the new device)
> - The Device Change Configuration stored in Profile Metadata controls which mode is used, which SM-DP+ to contact, and what information (EID, TAC) is required from the new device
> - **Profile Recovery** lets the end user recover a deleted profile on the old device if the new device's profile installation fails with a permanent error
> - The Service Provider is deeply involved: it receives `HandleDeviceChangeRequest` and `HandleNotification` calls, can provide `newProfileIccid`, a Service Provider Message, and a Confirmation Code

---

## The Problem: eSIM Portability

Physical SIM cards are inherently portable: pop the SIM out of one phone and into another. eSIMs, by design, are bound to a specific eUICC. The cryptographic binding between a profile and its eUICC means you can't simply "move" the profile file from one chip to another.

Before v3.x, transferring an eSIM between devices required one of:
- Contacting the operator for a new QR code / Activation Code (manual, slow)
- Using a manufacturer-specific transfer feature (proprietary, inconsistent across OEMs)
- Deleting the profile on the old device and downloading fresh on the new device (requires operator interaction)

Device Change in v3.x standardises this flow.

---

## Device Change: The Two Modes

Every Profile that supports Device Change contains a **DeviceChangeConfiguration** in its Profile Metadata (set by the Service Provider via the SM-DP+). This configuration determines which of two modes the procedure uses:

### Mode 1: `requestToDp` (Server-Orchestrated)

This is the full, SM-DP+-mediated flow:

1. **End User initiates** Device Change on the old device and selects the Profile to transfer
2. **LPAd retrieves** `DeviceChangeConfiguration` and finds `requestToDp`
3. **LPAd identifies the SM-DP+ address** from `smdpAddressForDc` in the configuration
4. **Optionally retrieves new device info** (EID, TAC) if the configuration requires it: the LPAd guides the end user to obtain this from the new device (e.g., scanning a QR code of the new device's EID)
5. **Common Mutual Authentication** with the SM-DP+
6. **LPAd sends `ES9+.AuthenticateClient`** with `ctxParamsForDeviceChange` containing the ICCID and optionally the new device's EID and/or TAC
7. **SM-DP+ optionally calls `ES2+.HandleDeviceChangeRequest`** to the Service Provider, which may provide:
   - `newProfileIccid` : a new profile to download on the new device (if the operator issues a fresh one)
   - `Service Provider Message` : text to display to the end user
   - `Confirmation Code` : if the end user must enter a code
8. **SM-DP+ notifies the Service Provider** via `ES2+.HandleNotification` (Device Change Request)
9. **Profile preparation**: If a new profile is needed, the Service Provider runs the Download Preparation Process: this can happen in parallel
10. **SM-DP+ returns `smdpSigned4`** with the transaction ID and optional Service Provider Message
11. **LPAd asks for Strong Confirmation** : the end user must explicitly confirm the transfer
12. **LPAd calls `ES10b.PrepareDeviceChange`** on the old eUICC with the signed data and hashed Confirmation Code
13. **LPAd calls `ES9+.ConfirmDeviceChange`** : the SM-DP+ processes the confirmation
14. **SM-DP+ returns `smdpSigned5`** : the LPAd calls `ES10b.VerifyDeviceChange`
15. **Old eUICC deletes the profile** and creates necessary Notifications
16. **LPAd generates an Activation Code** containing the Delete Notification for Device Change
17. **LPAd provides the Activation Code to the new device** (e.g., via LUI display, QR code)
18. **New device performs standard Profile Download and Installation** using the Activation Code

The Service Provider is notified at multiple points: when the Device Change is requested, when it's confirmed, and if it fails.

### Mode 2: `usingStoredAc` (Pre-Generated Activation Code)

A simpler mode where the profile already contains a stored Activation Code:

1. **LPAd retrieves** `DeviceChangeConfiguration` and finds `usingStoredAc`
2. If `deleteOldProfile` is set:
   - If the profile is Enabled, the LPAd disables it and sends notifications
   - The LPAd deletes the profile from the old device
3. **LPAd provides the stored Activation Code** to the new device
4. **New device performs standard Profile Download and Installation**

This is simpler but requires the Service Provider to have pre-generated the Activation Code and embedded it in the profile's metadata.

---

## Profile Recovery: The Safety Net (Section 3.11.2)

Device Change transfers delete the profile from the old device. What if the profile installation on the new device fails with a **permanent error**? The end user would lose the profile entirely.

Profile Recovery solves this:

**Start Conditions:**
- The LPAd of the old device has deleted the profile as instructed during Device Change
- The SM-DP+ indicated support for recovery in the Device Change Response
- The recovery information (ICCID, SM-DP+ address, allowed CI public key identifier) was stored by the LPAd
- The recovery validity period has not expired
- The profile installation on the new device failed permanently
- The new device's LPAd has delivered the Profile Installation Result to the SM-DP+ via `ES9+.HandleNotification`

**Recovery Procedure:**

1. **End User initiates** Profile Recovery on the old device, selecting the deleted profile
2. **LPAd retrieves** the stored SM-DP+ address (and optional allowed eSIM CA RootCA Public Key identifier)
3. **Common Mutual Authentication** with the SM-DP+
4. **LPAd sends `ES9+.AuthenticateClient`** with `ctxParamsForProfileRecovery`
5. **SM-DP+ verifies** that the profile installation on the new device indeed failed (checks `ProfileInstallationResult`)
6. **SM-DP+ prepares a new Profile Download and Activation Code**
7. **SM-DP+ returns `smdpSigned4`** in the AuthenticateClient response
8. **If the eUICC supports Device Change**: LPAd calls `ES10b.VerifyProfileRecovery` to verify the signed recovery data
9. **LPAd performs standard Profile Download and Installation** : the profile is restored on the old device

The recovery validity period is implementation-defined: after it expires, the LPAd discards the recovery information and recovery is no longer possible.

---

## The Complete Device Change Call Flow

The Device Change procedure involves both devices, the SM-DP+, and the Service Provider. Here's the end-to-end flow for the `requestToDp` mode:

| Step | Actor | Action |
|------|-------|--------|
| 1 | End User | Initiates Device Change on old device |
| 2 | LPAd (old) | Gets Profile Metadata, checks DeviceChangeConfiguration |
| 3 | LPAd (old) | Identifies SM-DP+ address |
| 4 | LPAd (old ← new) | Retrieves EID/TAC from new device if required |
| 5 | LPAd (old) → SM-DP+ | Common Mutual Authentication |
| 5a | LPAd (old) → SM-DP+ | `ES9+.AuthenticateClient` (ctxParamsForDeviceChange) |
| 6 | SM-DP+ → Service Provider | `ES2+.HandleDeviceChangeRequest` (ICCID, [EID], [TAC]) |
| 6 | Service Provider → SM-DP+ | OK, [newProfileIccid], [message], [Confirmation Code] |
| 7 | SM-DP+ → LPAd (old) | Error if not supported/not allowed; else continue |
| 8 | SM-DP+ → Service Provider | `ES2+.HandleNotification` (Device Change Request) |
| 9 | Service Provider → SM-DP+ | Profile Download preparation (if new profile needed) |
| 10 | SM-DP+ → LPAd (old) | `smdpSigned4`, `smdpSignature4`, [Service Provider message] |
| 11 | LPAd (old) | Strong Confirmation + optional Confirmation Code entry |
| 12 | LPAd (old) → eUICC (old) | `ES10b.PrepareDeviceChange` |
| 13 | LPAd (old) → SM-DP+ | `ES9+.ConfirmDeviceChange` |
| 14 | SM-DP+ → Service Provider | `ES2+.HandleNotification` (confirmation/failure) |
| 15 | SM-DP+ | Prepares profile if newProfileIccid not provided |
| 16 | SM-DP+ → LPAd (old) | `smdpSigned5`, `smdpSignature5` |
| 17 | LPAd (old) → eUICC (old) | `ES10b.VerifyDeviceChange` : decrypt DC data, delete profile, create notifications |
| 18 | LPAd (old) | Handle Delete Notifications; generate Activation Code |
| 19 | LPAd (old → new) | Provide Activation Code |
| 20 | LPAd (new) → SM-DP+ → eUICC (new) | Standard Profile Download and Installation |

---

## Comparison: Device Change vs Manual Transfer

| Aspect | Manual Transfer (v2.x) | Device Change (v3.x) |
|--------|------------------------|----------------------|
| Standardisation | None (proprietary per OEM) | GSMA standard (SGP.22 v3.x) |
| Operator involvement | Manual (call/website for new eSIM) | Automated via ES2+ interface |
| New profile needed | Usually yes | Optional: can reuse existing profile |
| New device info | N/A | EID, TAC optionally required |
| End user steps | Multiple manual actions | Guided flow with Strong Confirmation |
| Rollback on failure | No standard recovery | Profile Recovery restores old profile |
| Service Provider message | N/A | Displayed to end user during confirmation |
| Confirmation Code | Not used in manual flow | Can be required by Service Provider |

---

## Summary

- Device Change standardises eSIM transfer between devices: a v3.x-only feature
- Two modes: `requestToDp` (SM-DP+ orchestrates) and `usingStoredAc` (pre-generated Activation Code)
- The Service Provider is involved throughout via `HandleDeviceChangeRequest` and `HandleNotification`
- New profile issuance is optional; the SM-DP+ can prepare a fresh profile or reuse the existing subscription
- Profile Recovery provides a safety net: if the new device fails to install, the old device can restore the profile
- Recovery validity period is implementation-defined; once expired, recovery is no longer possible
- End user consent (Strong Confirmation) is required before the old profile is deleted

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp22-v3/57-remote-profile-management">Remote Profile Management: RPM Initiation, Download, and Execution</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp22-v3/59-euicc-updates-pcm">eUICC Updates and Profile Content Management: Lifecycle Beyond Download</a> →

</div>

---

*Based on GSMA SGP.22 v3.1 (01 December 2023), Section 3.11: Device Change and Profile Recovery, Section 5.6.6: ConfirmDeviceChange, and Annex O: Device Change Configuration*


---

← Previous: [Remote Profile Management: RPM Initiation, Download, and Execution](57-remote-profile-management) | [Section Index](index) | Next: [eUICC Updates and Profile Content Management: Lifecycle Beyond Download](59-euicc-updates-pcm) →
