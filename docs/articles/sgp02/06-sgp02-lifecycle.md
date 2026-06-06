---
date: 2026-06-07
layout: default
title: "Profile Lifecycle: Enable, Disable, Delete, and Fall-Back"
---

# Profile Lifecycle: Enable, Disable, Delete, and Fall-Back

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > Profile Lifecycle: Enable, Disable, Delete, and Fall-Back**

> **📚 Prerequisites:** This article assumes you understand the SGP.02 architecture (roles, interfaces), the eUICC's internal security domain structure (ISD-R, ISD-P, ECASD), and how a Profile gets downloaded. Articles 1–6 cover these foundations.

> **💡 Why this matters:** After a Profile is downloaded, it lives on the eUICC for months or years. Operators need to activate, deactivate, and eventually remove Profiles — and all of this happens remotely, often to devices buried in utility closets or sealed inside engine compartments.

> **Key takeaways:**
> - Profile lifecycle operations — enable, disable, delete — can be initiated through three paths: Operator via ES4, Operator via SM-DP relay (ES2→ES3→ES5), or M2M SP via ES4
> - Every operation has a Normal Case and a Connectivity Failure Case with automatic roll-back
> - Disabling a Profile triggers automatic activation of the Fall-Back Profile
> - POL1 (on-card) and POL2 (SM-SR-side) policies are enforced at every lifecycle operation
> - The Master Delete procedure can bypass policy rules using a cryptographically authorised Delete Token

---

## Three Paths to Every Operation

SGP.02 defines three distinct initiation paths for Profile lifecycle operations, each serving a different deployment scenario:

**Path 1 — Operator via ES4 (Direct SM-SR):** The Operator calls the SM-SR directly through the ES4 interface. This is the simplest path — one function call, one entity mediating between Operator and eUICC. Use cases: operators with a direct business relationship with the SM-SR, full-service MNOs managing their own fleet.

**Path 2 — Operator via SM-DP Relay (ES2→ES3→ES5):** The Operator calls the SM-DP (ES2), which forwards the request to the SM-SR (ES3), which contacts the eUICC (ES5). This path exists because some Operators interface primarily with their SM-DP for both profile preparation and lifecycle management. The SM-DP acts as a relay and translator between the two worlds.

**Path 3 — M2M SP via ES4:** The M2M Service Provider — often a fleet management company or enterprise — calls the SM-SR directly through ES4 with prior authorisation from the Profile-owning Operator (granted via PLMA — see Article 10). This path enables the device fleet manager to manage connectivity without involving the Operator on every operation.

All three paths converge on the same on-card procedure: the ISD-R receives the command via ES5 (SMS, HTTPS, or CAT_TP), enforces POL1, performs the operation, and notifies the SM-SR.

---

## Profile Enabling: Making a Profile Active

Profile Enabling is the procedure that makes a Profile's NAA (Network Access Application) and file system selectable over the UICC-Terminal interface. Only one Profile can be enabled at a time — enabling Profile B automatically disables the currently enabled Profile A.

### Normal Case (SGP.02 §3.2.1)

The flow, whether initiated via Operator or SM-DP relay:

1. **Request:** Operator calls `ES4.EnableProfile(eid, iccid)` (or `ES2.EnableProfile` through SM-DP relay)
2. **SM-SR checks initial conditions:** The SM-SR verifies the request is acceptable — the Profile exists, is disabled, and POL2 permits enabling
3. **OTA command:** SM-SR sends an SCP80-secured `ES5.STORE DATA` command to the ISD-R via SMS (or equivalent via HTTPS/CAT_TP)
4. **POL1 enforcement:** The ISD-R checks the currently Enabled Profile's POL1 — if POL1 says "disable not allowed," the procedure fails
5. **Enable ISD-P:** The ISD-R disables the current ISD-P and enables the target ISD-P
6. **REFRESH:** The eUICC sends a UICC Reset REFRESH to the Device, forcing a new network attachment with the newly enabled Profile
7. **Notification:** The eUICC performs the Default Notification procedure (SMS or HTTPS) to inform the SM-SR of the profile change
8. **POL2 check:** After notification confirmation, the SM-SR evaluates POL2 of the now-disabled Profile. If POL2 contains "Profile deletion is mandatory when disabled," the SM-SR sends an `ES5.DELETE` command
9. **EIS update:** The SM-SR updates its EIS record to reflect the new enabled/disabled states

### Connectivity Failure Case (SGP.02 §3.2.2)

If the newly enabled Profile cannot attach to the network — or if the notification procedure fails — the eUICC automatically rolls back:

- The ISD-R re-enables the previously Enabled Profile
- A new REFRESH triggers network attachment with the roll-back Profile
- The notification procedure informs the SM-SR of the roll-back
- If the previously Enabled Profile *also* cannot provide connectivity, the eUICC activates the Fall-Back Mechanism (see Article 9)

This automatic roll-back is critical for M2M: a failed profile switch in an unreachable device could otherwise leave it permanently disconnected.

---

## Profile Disabling: Deactivate and Switch to Fall-Back

Profile Disabling (§3.4) makes a Profile unselectable while preserving it on the card. The flow mirrors enabling but with one critical difference: when a Profile is disabled, the eUICC **automatically enables the Profile with the Fall-Back Attribute set**.

This is the spec's built-in safety net. Disabling a Profile without another enabled Profile would leave the device with no network access — so SGP.02 mandates immediate failover to the Fall-Back Profile. The procedure also handles conditional deletion:

- After disabling, POL1 is evaluated. If the disabled Profile's POL1 contains "Profile deletion is mandatory when its state is changed to disabled," the ISD-R deletes the Profile and its ISD-P
- After notification, the SM-SR separately evaluates POL2 and may also trigger deletion if POL2 contains the same rule
- The procedure explicitly notes that POL1 and POL2 "MAY have different content. As a consequence, both the eUICC and the SM-SR have to ensure the ISD-P deletion based on their respective Policy"

---

## Profile and ISD-P Deletion: Permanent Removal

Profile Deletion (§3.6, §3.7) permanently removes the ISD-P and all its contents — NAA, file system, keys, applets, and metadata. The procedure can be initiated:

- **Directly** by the Operator via `ES4.DeleteProfile`
- **Via SM-DP relay** using `ES2.DeleteProfile` → `ES3.DeleteProfile` → `ES5` commands
- **Post-disable** as a consequence of POL1/POL2 mandatory-deletion rules

The on-card flow:
1. SM-SR sends `ES5.DELETE` command to ISD-R targeting the disabled Profile's ISD-P
2. ISD-R enforces POL1 of the target Profile
3. If POL1 permits, ISD-R deletes the ISD-P and the contained Profile
4. SM-SR updates EIS to reflect the deletion

The Spec explicitly prohibits deleting the currently Enabled Profile — the Profile must be disabled first. The deletion is permanent and irreversible.

### Master Delete (§3.10)

The Master Delete procedure handles a specific edge case: **orphaned Profiles**. These are Profiles whose owning Operator is no longer available (e.g., bankruptcy, contract termination) or whose policy rules prevent normal deletion.

Master Delete uses a cryptographically authorised **Delete Token** issued by the SM-DP:

1. An Initiator (not necessarily the Operator) requests Master Delete from the SM-SR
2. SM-SR requests a Master Delete Authorisation from the SM-DP associated with the target Profile
3. SM-DP verifies the request is authenticated and authorised (including Operator authorisation — out of scope)
4. If authorised, SM-DP returns a one-time Delete Token
5. SM-SR sends `ES5.MasterDelete` with the token to the ISD-R
6. The **ISD-P itself verifies the token** (not just the ISD-R — this is a unique cryptographic check)
7. ISD-R deletes the ISD-P and Profile **regardless of POL1 or POL2**

The Master Delete cannot target the Fall-Back Profile — ensuring the device always retains at least one connectivity option.

---

## The Connectivity Failure Pattern

Every lifecycle operation — enable, disable, delete — shares a common pattern for handling connectivity failures:

- **eUICC-side timeout:** If the newly enabled Profile can't attach to the network, the eUICC detects this locally (no network registration)
- **Notification timeout:** If the eUICC cannot reach the SM-SR for notification (all retries exhausted), it considers the operation failed
- **Roll-back:** The eUICC reverts to the previously Enabled Profile (for enabling) or activates the Fall-Back Profile (for disabling)
- **Fall-Back escalation:** If roll-back also fails, the Fall-Back Mechanism is activated — this is the ultimate safety net
- **SM-SR Validity Period:** The SM-SR sets a Validity Period timer when it issues an OTA command. If the notification arrives after expiry, the SM-SR does not send a confirmation — and the eUICC treats this as a notification failure, triggering roll-back

---

## Initiation Path Summary

| Operation | Operator (ES4) | Operator via SM-DP (ES2→ES3→ES5) | M2M SP (ES4) |
|-----------|----------------|----------------------------------|--------------|
| Enable | `ES4.EnableProfile` | `ES2.EnableProfile` → `ES3.EnableProfile` | `ES4.EnableProfile` (with PLMA) |
| Disable | `ES4.DisableProfile` | `ES2.DisableProfile` → `ES3.DisableProfile` | `ES4.DisableProfile` (with PLMA) |
| Delete | `ES4.DeleteProfile` | `ES2.DeleteProfile` → `ES3.DeleteProfile` | `ES4.DeleteProfile` (with PLMA) |
| Master Delete | Out of scope (ES4 by Initiator) | Via SM-DP authorisation | Not applicable |

The three-path architecture is what makes SGP.02 flexible enough for diverse M2M deployments. A utility company acting as M2M SP can manage its meter fleet directly, while the mobile operator retains ultimate control through PLMA and POL1/POL2 policy rules.

---

## 📋 Summary

- Profile lifecycle operations have three initiation paths: Operator direct (ES4), Operator via SM-DP relay, and M2M SP via ES4 with PLMA authorisation
- Every enable/disable/delete operation follows a structured flow: SM-SR checks → OTA command → POL1 enforcement → eUICC execution → notification → POL2 check → EIS update
- Connectivity Failure Cases provide automatic roll-back — the eUICC reverts to the previously Enabled Profile or activates the Fall-Back Mechanism
- Disabling always triggers enablement of the Fall-Back Profile to maintain connectivity
- POL1 (on-card) and POL2 (server-side) are independently enforced at each lifecycle step; they may differ
- Master Delete uses a one-time Delete Token and bypasses all policy rules — but cannot target the Fall-Back Profile

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

Previous: [Profile Download: ISD-P Creation, SCP03, and Encrypted Delivery](05-sgp02-download) →
Next: [SM-SR Change: Handover, ES7 Interface, and EIS Migration](07-sgp02-sm-sr-change) →

</div>

---

*Based on GSMA SGP.02 v4.2 (07 July 2020) — Remote Provisioning Architecture for Embedded UICC Technical Specification, §3.2–3.7, §3.10*


---

← Previous: [Profile Download: ISD-P Creation, SCP03, and Encrypted Delivery](05-sgp02-download) | [Section Index](index) | Next: [SM-SR Change: Handover, ES7 Interface, and EIS Migration](07-sgp02-sm-sr-change) →
