---
date: 2026-06-07
layout: default
title: "SM-SR Change: Handover, ES7 Interface, and EIS Migration"
---

# SM-SR Change: Handover, ES7 Interface, and EIS Migration

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > SM-SR Change: Handover, ES7 Interface, and EIS Migration**

> **📚 Prerequisites:** You should understand the SGP.02 ecosystem roles (SM-DP, SM-SR, Operator), the eUICC's internal architecture (ISD-R, ECASD), the PKI certificate hierarchy, and key establishment using the ECASD key pair. Articles 2, 3, and 4 cover the needed foundations.

> **💡 Why this matters:** In the M2M world, device deployments span a decade or more. The SM-SR you chose when the device shipped may not be the one you want five years later — due to M&A, pricing changes, service quality, or regulatory shifts. The SM-SR Change procedure is SGP.02's answer to vendor lock-in, enabling migration of an entire eUICC (all Profiles, all state) from one SM-SR to another without physical access.

> **Key takeaways:**
> - SM-SR Change is a 32-step protocol spanning four entities: Initiator Operator, SM-SR1 (old), SM-SR2 (new), and the eUICC
> - The eUICC uses its ECASD private key to derive a new key set (KS2) for SM-SR2 — the same mechanism used for Profile Download, now in a different context
> - The ES7 interface (SM-SR ↔ SM-SR) carries three functions: `HandoverEUICC`, `AuthenticateSM-SR`, and `CreateAdditionalKeySet`
> - All ISD-Ps, Profiles, and the eUICC's state survive the migration intact
> - The handover is atomic: once SM-SR2 verifies the receipt at step 23, it owns the eUICC — even if subsequent steps fail

---

## Why SM-SR Change Matters

The SM-SR is the single most powerful entity in the SGP.02 ecosystem. It owns the OTA channel, holds the Platform Management keys, and serves as the gatekeeper for every profile lifecycle operation. In a typical M2M deployment spanning 10–15 years, the original SM-SR selection is made by the device manufacturer or initial operator. But circumstances change:

- A fleet operator switches mobile network operators and the new MNO has an existing relationship with a different SM-SR
- Corporate mergers and acquisitions consolidate SM-SR providers
- An SM-SR goes out of business or discontinues service in a region
- Pricing or service level agreements make migration economically attractive

Without SM-SR Change, an eUICC is effectively locked to its original SM-SR for life — replacing the SM-SR would mean replacing the physical eUICC. The SM-SR Change procedure (SGP.02 §3.8) solves this by defining a complete, cryptographically secured handover protocol.

---

## The Four-Entity Dance

SM-SR Change involves four entities interacting through multiple interfaces:

| Entity | Role | Interface Used |
|--------|------|---------------|
| **Initiator Operator** | Requests and orchestrates the change | ES4 (to both SM-SRs) |
| **SM-SR1 (old)** | Current SM-SR; holds EIS and Platform Management keys | ES4, ES5, ES7 |
| **SM-SR2 (new)** | Target SM-SR; must become the new Platform Manager | ES4, ES5, ES7 |
| **eUICC** | The chip itself; must authenticate SM-SR2 and create new keys | ES5 (via SM-SR1 relay) |

The procedure is unusual in that SM-SR1 and SM-SR2 must cooperate — they communicate via ES7, a spec-defined inter-SM-SR interface that exists only for this purpose. The Initiator Operator drives the process but relies on both SM-SRs to execute correctly.

---

## The Full Handover Sequence (§3.8)

SGP.02 defines the SM-SR Change as a 32-step procedure. It can be grouped into five phases:

### Phase 1: Preparation (Steps 1–3)

The Initiator Operator calls `ES4.PrepareSMSRChange` on SM-SR2 with the EID. SM-SR2 verifies it can manage this eUICC (has sufficient capacity, supports the eUICC's capabilities, has a valid CI-signed certificate). If successful, SM-SR2 confirms readiness. This is a lightweight check — no state is modified yet.

### Phase 2: EIS Handover (Steps 4–6)

The Operator calls `ES4.SMSRChange` on SM-SR1 with the target SM-SR2 identity and a Validity Period. SM-SR1:
- Verifies there are no pending actions for the target eUICC
- Rejects any new management requests for the target eUICC during the procedure (locks the eUICC)
- Calls `ES7.HandoverEUICC(eis)` on SM-SR2, transmitting the complete EIS (eUICC Information Set)

SM-SR2 receives the EIS containing ECASD certificate, ISD-R information, all ISD-P metadata, Profile states, and policy rules. SM-SR2 verifies the ECASD certificate against the EUM certificate and CI root — the same chain validation used in Profile Download.

### Phase 3: SM-SR2 Authentication to eUICC (Steps 7–13)

This is where the cryptography gets interesting. SM-SR2 must prove its identity to the eUICC's ECASD:

1. **SM-SR2 calls `ES7.AuthenticateSM-SR`** providing its certificate `CERT.SR.ECDSA`
2. **SM-SR1 relays to eUICC** via `ES5.EstablishISDRKeySet(CERT.SR.ECDSA)`
3. **ISD-R verifies** it's an SM-SR certificate (not a DP certificate), then forwards to ECASD
4. **ECASD verifies** `CERT.SR.ECDSA` using `PK.CI.ECDSA` (the CI root public key)
5. **ECASD extracts and stores** `PK.SR.ECDSA` from the certificate
6. **ECASD generates** a Random Challenge (RC) — 16 or 32 bytes — and returns it to ISD-R
7. **RC flows back** through SM-SR1 to SM-SR2

At this point, the eUICC trusts SM-SR2's certificate chain. Now SM-SR2 must prove possession of the corresponding private key.

### Phase 4: Key Set Creation (Steps 14–23)

This phase mirrors the key establishment used during Profile Download (Scenario#3), but with an important difference: the key set being created is for the ISD-R (Platform Management), not an ISD-P (Profile Management).

1. **SM-SR2 generates an ephemeral ECKA key pair** (`eSK.SR.ECKA`, `ePK.SR.ECKA`) and signs RC + `ePK.SR.ECKA` with its private key `SK.SR.ECDSA`
2. **SM-SR2 calls `ES7.CreateAdditionalKeySet`** with the ephemeral public key and signature
3. **SM-SR1 relays** `ES5.EstablishISDRKeySet(ePK.SR.ECKA, signature)` to the eUICC
4. **ECASD verifies** the signature using `PK.SR.ECDSA` (extracted in phase 3)
5. **ECASD computes the shared secret** `ShS` from `ePK.SR.ECKA` and its own private key `SK.ECASD.ECKA` — this is the standard ECKA-EG key agreement
6. **ISD-R generates an optional DR** (Diversification Random), derives key set KS2 from ShS (and DR if present), and calculates a receipt
7. **Receipt flows back** to SM-SR2, which independently computes ShS from its ephemeral private key and `PK.ECASD.ECKA`, derives KS2, and verifies the receipt

**The critical checkpoint:** Once SM-SR2 verifies the receipt at step 23, it is now the Platform Manager. Even if everything after this fails, SM-SR2 owns the eUICC. The spec states: "As soon as SM-SR2 has verified the receipt (step 23 above), the management of the eUICC is ensured by the new SM-SR2."

### Phase 5: Finalisation and Notification (Steps 24–32)

1. **SM-SR2 opens a secure channel** to the eUICC using the newly created KS2 key set
2. **`ES5.FinaliseISDRhandover`** deletes SM-SR1's keys from the ISD-R
3. **Optional ISD-R reconfiguration:** SM-SR2 may update HTTPS parameters, DNS settings, SM-SR addressing parameters, and personalise additional key sets (e.g., for different SCP protocols)
4. **SM-SR2 updates the EIS** to reflect its new ownership
5. **SM-SR2 returns `HandoverEUICC` success** to SM-SR1
6. **SM-SR1 deletes its EIS** for the target eUICC
7. **SM-SR1 returns `SMSRChange` success** to the Initiator Operator
8. **SM-SR2 notifies all affected Operators** via `ES4.HandleSMSRChangeNotification` — Operators owning Profiles on the eUICC are informed of the new SM-SR. If an Operator has no direct connection to SM-SR2, the notification routes through the SM-DP (ES3→ES2)

---

## The ES7 Interface: SM-SR to SM-SR Communication

The ES7 interface (SGP.02 §5.6) is defined exclusively for SM-SR Change and contains three functions:

| Function | Direction | Purpose |
|----------|-----------|---------|
| `HandoverEUICC` | SM-SR1 → SM-SR2 | Transmits the EIS to the new SM-SR |
| `AuthenticateSM-SR` | SM-SR2 → SM-SR1 | SM-SR2 provides its certificate for eUICC authentication |
| `CreateAdditionalKeySet` | SM-SR2 → SM-SR1 | SM-SR2 provides ephemeral key and signature for KS2 creation |

ES7 uses the same SOAP/HTTPS binding as other off-card interfaces (Annex B), with messages defined in ASN.1 notation (Annex A). The interface carries sensitive data — the EIS contains the ECASD certificate, ISD-R metadata, and all Profile information — so transport-level security (TLS) and mutual authentication are essential.

---

## EIS Migration: What Moves, What Stays

The EIS (eUICC Information Set) is the SM-SR's database record for a specific eUICC. During SM-SR Change, the EIS migrates from SM-SR1 to SM-SR2. The EIS includes (SGP.02 Annex E):

- **EID** — the unique eUICC identifier
- **ECASD Certificate** (`CERT.ECASD.ECKA`) — for future key establishment
- **ISD-R configuration** — AID, TAR, supported SCP protocols, addressing parameters
- **All ISD-P metadata** — AIDs, TARs, associated SM-DP identities, Profile states (enabled/disabled)
- **Profile identifiers** — ICCIDs, Profile Types, Operator identities
- **Policy Rules** — POL2 for each Profile
- **Connectivity Parameters** — SM-DP addressing, notification addresses
- **Additional Properties** — Emergency Profile attribute, Fall-Back attribute, Test Profile flags

What does NOT migrate: SM-SR1's Platform Management keys in the ISD-R are deleted (step 25) and replaced by KS2. SM-SR1's administrative records (billing, logs, audit trails) are out of scope — only the data needed for operational management is handed over.

---

## Error Handling and Atomicity

SGP.02 defines careful error handling for the SM-SR Change:

- **Validity Period expiry:** Both SM-SR1 and SM-SR2 enforce timeouts. If SM-SR1 doesn't receive step 7 or step 15 before expiry, it aborts and returns "Failed" to the Initiator Operator
- **Verification failures:** If the ECASD rejects SM-SR2's certificate or signature, the procedure stops immediately. SM-SR2 deletes its EIS copy
- **Post-receipt failures:** After step 23 (receipt verified), SM-SR2 always returns "Executed-Success" or "Executed-WithWarning" — never "Failed." SM-SR1 always deletes its EIS after receiving the response, even with a warning
- **Retry logic:** If the procedure expires on SM-SR1's side after step 22 but SM-SR2 completed step 23 during the first attempt, a retry skips steps 7–23 (the eUICC already has the new keys) and proceeds directly to finalisation. SM-SR2 indicates "eUICC already managed" and SM-SR1 returns "Success_WithWarning"
- **Expired ISD-R keys:** If deletion of SM-SR1's keys fails (step 25), SM-SR2 is still responsible for management — it returns a warning but proceeds

---

## Preventing Vendor Lock-In

The SM-SR Change is SGP.02's single most important architectural feature for preventing vendor lock-in. The design ensures:

- **No SM-SR1 cooperation needed for the cryptographic binding:** The eUICC authenticates SM-SR2 through the CI root (stored in ECASD at manufacture), not through SM-SR1. SM-SR1 relays messages but cannot forge or block authentication
- **The eUICC holds the ultimate authority:** The ECASD private key (`SK.ECASD.ECKA`) never leaves the chip. SM-SR2 must prove its identity to the eUICC, not just to SM-SR1
- **The procedure works even with an uncooperative SM-SR1:** As long as SM-SR1 relays messages correctly (which it is contractually obligated to do), the handover succeeds. The spec requires SM-SR1 to support the procedure
- **No data loss:** All Profiles, states, and policy rules survive the migration. The Operator's relationship with the Profiles is preserved — only the Platform Management provider changes

---

## 📋 Summary

- SM-SR Change is a 32-step, four-entity protocol for migrating eUICC management from one SM-SR to another
- The procedure uses the same ECKA-EG key establishment mechanism as Profile Download, repurposed for ISD-R (Platform Management) key creation
- The ES7 interface carries three functions: `HandoverEUICC` (EIS transfer), `AuthenticateSM-SR` (certificate provisioning), and `CreateAdditionalKeySet` (key agreement)
- Step 23 (receipt verification) is the atomic commit point — once passed, SM-SR2 owns the eUICC
- All Profiles, ISD-Ps, and eUICC state survive intact; only the Platform Management keys change
- Error handling supports retry, partial completion, and graceful degradation while maintaining unambiguous ownership

---

<div align="center">

[🏠 Home]({{ site.baseurl }}/)

Previous: [Profile Lifecycle: Enable, Disable, Delete, and Fall-Back](06-sgp02-lifecycle) →
Next: [Resilience: Fall-Back Mechanism, Emergency Profiles, and Test Profiles](08-sgp02-resilience) →

</div>

---

*Based on GSMA SGP.02 v4.2 (07 July 2020) — Remote Provisioning Architecture for Embedded UICC Technical Specification, §3.8–3.9, §5.6*


---

← Previous: [Profile Lifecycle: Enable, Disable, Delete, and Fall-Back](06-sgp02-lifecycle) | [Section Index](index) | Next: [Resilience: Fall-Back Mechanism, Emergency Profiles, and Test Profiles](08-sgp02-resilience) →
