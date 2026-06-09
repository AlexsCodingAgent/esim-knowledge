---
description: "Explains the SGP.02 SM-SR Change protocol — a 32-step cryptographic handover that migrates an eUICC's platform management keys and EIS from one SM-SR to another over the ES7 interface, preventing vendor lock-in."
date: 2026-06-07
layout: default
title: "SM-SR Change: Handover, ES7 Interface, and EIS Migration"
---

# SM-SR Change: Handover, ES7 Interface, and EIS Migration

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.02 M2M RSP]({{ site.baseurl }}/docs/articles/sgp02/) > SM-SR Change: Handover, ES7 Interface, and EIS Migration**

Picture an eUICC shipped in 2024, soldered into a smart meter, deployed in a suburban utility closet. The manufacturer chose SM-SR1 because they had a good deal at the time. Five years later, the utility company switches mobile operators. The new MNO works exclusively with SM-SR2. Now what?

Without SM-SR Change, the answer is: you're stuck. The SM-SR owns the OTA channel, holds the Platform Management keys, and gates every profile operation. Replacing it would mean physically replacing the eUICC; and nobody's sending a technician to 50,000 utility closets because of a backend vendor switch.

SGP.02 §3.8 defines the escape hatch: a 32-step, four-entity, cryptographically sealed protocol for migrating an eUICC (all its Profiles, all its state, all its keys) from one SM-SR to another, over the air. It's the spec's answer to vendor lock-in, and it's one of the more remarkable pieces of protocol engineering in the entire GSMA RSP ecosystem.

Before we get into the handshake: you'll want to understand the SGP.02 roles (SM-DP, SM-SR, Operator), the eUICC's internal architecture (ISD-R, ECASD), the PKI certificate hierarchy, and key establishment using the ECASD key pair. Articles 2, 3, and 4 lay that groundwork.

---

## The players

Four entities, three interfaces, one goal:

| Entity | Role | Interface Used |
|--------|------|---------------|
| **Initiator Operator** | Requests and orchestrates the change | ES4 (to both SM-SRs) |
| **SM-SR1 (old)** | Current SM-SR; holds EIS and Platform Management keys | ES4, ES5, ES7 |
| **SM-SR2 (new)** | Target SM-SR; must become the new Platform Manager | ES4, ES5, ES7 |
| **eUICC** | The chip itself; authenticates SM-SR2 and creates new keys | ES5 (via SM-SR1 relay) |

SM-SR1 and SM-SR2 talk to each other over ES7, an interface that exists for exactly this purpose and nothing else. The Initiator Operator drives the whole thing, but can't do any of the cryptographic heavy lifting. That's all between the eUICC and SM-SR2, with SM-SR1 playing courier.

---

## The handover, step by step

SGP.02 breaks the 32-step procedure into five phases. What follows is the full sequence, told as a story rather than a reference table. (If you need the reference-level detail, §3.8 has every ASN.1 message and timer value.)

### Phase 1: "Are you willing to take this eUICC?" (Steps 1–3)

The Initiator Operator calls `ES4.PrepareSMSRChange` on SM-SR2, passing the EID. SM-SR2 runs a quick sanity check: can I manage this eUICC? Do I have capacity? Does this chip's capabilities match what I support? Is my CI-signed certificate valid?

If SM-SR2 says yes, nothing has actually changed yet. No state modified, no keys moved. This is a handshake before the handshake, confirming both parties are willing before anything irreversible happens.

### Phase 2: "Here's everything I know about this chip" (Steps 4–6)

Now the Operator calls `ES4.SMSRChange` on SM-SR1, providing SM-SR2's identity and a Validity Period (the deadline for this whole procedure). SM-SR1 responds by:

- Checking there are no pending operations for this eUICC
- Locking the eUICC; no new management requests accepted during the handover
- Calling `ES7.HandoverEUICC(eis)` on SM-SR2

That last call transmits the entire EIS, the eUICC Information Set. ECASD certificate, ISD-R metadata, every ISD-P and its Profile state, all policy rules, the Fall-Back and Emergency attributes. SM-SR2 receives it and immediately validates the ECASD certificate against the EUM certificate and the CI root. If the chain doesn't check out, the procedure stops here.

### Phase 3: "Prove you are who you say you are" (Steps 7–13)

SM-SR2 has the EIS, but the eUICC doesn't know SM-SR2 from any other server on the internet. This phase is SM-SR2 introducing itself to the chip, and the chip verifying that introduction cryptographically.

1. SM-SR2 calls `ES7.AuthenticateSM-SR`, sending its certificate `CERT.SR.ECDSA`
2. SM-SR1 relays this to the eUICC as `ES5.EstablishISDRKeySet(CERT.SR.ECDSA)`
3. The ISD-R confirms this is an SM-SR certificate (not a DP certificate, different OID), then passes it to the ECASD
4. The ECASD validates `CERT.SR.ECDSA` against `PK.CI.ECDSA`, the CI root public key burned in at manufacture
5. The ECASD extracts and stores `PK.SR.ECDSA` from the certificate
6. The ECASD generates a Random Challenge: 16 or 32 bytes of fresh randomness; and hands it to the ISD-R
7. The Random Challenge flows back through SM-SR1 to SM-SR2

The certificate is trusted. Now SM-SR2 has to prove it holds the matching private key.

### Phase 4: "Let's make some keys together" (Steps 14–23)

This is where the cryptographic heavy lifting happens. The mechanism should look familiar; it's the same ECKA-EG key agreement used during Profile Download (Scenario#3), but repurposed here to create keys for the ISD-R (Platform Management) instead of an ISD-P (Profile Management).

1. SM-SR2 generates an ephemeral ECKA key pair (`eSK.SR.ECKA`, `ePK.SR.ECKA`) and signs the Random Challenge plus `ePK.SR.ECKA` with its private key `SK.SR.ECDSA`
2. SM-SR2 calls `ES7.CreateAdditionalKeySet` with the ephemeral public key and the signature
3. SM-SR1 relays this as `ES5.EstablishISDRKeySet(ePK.SR.ECKA, signature)` to the eUICC
4. The ECASD verifies the signature using `PK.SR.ECDSA`, the key it extracted in Phase 3
5. The ECASD computes the shared secret `ShS` from `ePK.SR.ECKA` and its own private key `SK.ECASD.ECKA`. Standard ECKA-EG key agreement
6. The ISD-R generates an optional Diversification Random (DR), derives the new key set KS2 from ShS (and DR if present), and calculates a receipt
7. The receipt flows back to SM-SR2, which independently computes ShS from its ephemeral private key and `PK.ECASD.ECKA`, derives KS2, and verifies the receipt

**Step 23 is the atomic commit point.** The spec is unambiguous: "As soon as SM-SR2 has verified the receipt (step 23 above), the management of the eUICC is ensured by the new SM-SR2." SM-SR2 now owns this eUICC. Even if every subsequent step fails, SM-SR2 is the Platform Manager. SM-SR1 will delete its EIS regardless of what happens next.

### Phase 5: "Clean up and tell everyone" (Steps 24–32)

The new keys exist, but SM-SR1's old keys are still sitting in the ISD-R. Time to clean house:

1. SM-SR2 opens a secure channel to the eUICC using the freshly-minted KS2 key set
2. `ES5.FinaliseISDRhandover` deletes SM-SR1's keys from the ISD-R
3. Optionally, SM-SR2 reconfigures ISD-R parameters: HTTPS endpoints, DNS settings, SM-SR addressing, additional key sets for different SCP protocols
4. SM-SR2 updates the EIS to show itself as owner
5. SM-SR2 returns `HandoverEUICC` success to SM-SR1
6. SM-SR1 deletes its EIS for this eUICC
7. SM-SR1 tells the Initiator Operator: `SMSRChange` succeeded
8. SM-SR2 notifies every Operator with a Profile on this eUICC via `ES4.HandleSMSRChangeNotification`. If an Operator doesn't have a direct connection to SM-SR2, the notification routes through the SM-DP (ES3 → ES2)

The eUICC has a new Platform Manager. All its Profiles survived. Not a single byte lost.

---

## The ES7 interface: purpose-built for handover

ES7 (SGP.02 §5.6) is the only interface in the spec that exists for a single procedure. Three functions, all carrying sensitive material between SM-SRs:

| Function | Direction | Purpose |
|----------|-----------|---------|
| `HandoverEUICC` | SM-SR1 → SM-SR2 | Transmits the EIS to the new SM-SR |
| `AuthenticateSM-SR` | SM-SR2 → SM-SR1 | SM-SR2 provides its certificate for eUICC authentication |
| `CreateAdditionalKeySet` | SM-SR2 → SM-SR1 | SM-SR2 provides ephemeral key and signature for KS2 creation |

ES7 uses the same SOAP/HTTPS binding as the other off-card interfaces (Annex B), with messages defined in ASN.1 (Annex A). It carries the EIS (ECASD certificate, ISD-R metadata, all Profile information), so TLS and mutual authentication aren't optional. Nobody wants an EIS interceptable in transit.

---

## What moves, what stays behind

The EIS (defined in Annex E) is the SM-SR's complete database record for an eUICC. During SM-SR Change, it migrates from SM-SR1 to SM-SR2. Here's what's in it:

- **EID** : unique eUICC identifier
- **ECASD Certificate** (`CERT.ECASD.ECKA`) : needed for all future key establishment
- **ISD-R configuration** : AID, TAR, supported SCP protocols, addressing parameters
- **All ISD-P metadata** : AIDs, TARs, associated SM-DP identities, Profile states (enabled/disabled)
- **Profile identifiers** : ICCIDs, Profile Types, Operator identities
- **Policy Rules** : POL2 for each Profile
- **Connectivity Parameters** : SM-DP addressing, notification addresses
- **Additional Properties** : Emergency Profile attribute, Fall-Back attribute, Test Profile flags

What doesn't migrate: SM-SR1's Platform Management keys (deleted at step 25 and replaced by KS2). SM-SR1's billing records, audit logs, and internal administrative data are out of scope; only the operational data needed to manage the eUICC gets handed over.

---

## When things go sideways

A 32-step protocol with four entities and cryptographic key agreement has plenty of failure modes. SGP.02 addresses the most important ones:

**Validity Period expiry.** Both SM-SRs enforce timeouts. If SM-SR1 doesn't receive step 7 or step 15 within the window, it aborts and returns "Failed" to the Initiator. Clean, unambiguous, no orphaned state.

**Verification failures.** Certificate invalid? Signature doesn't verify? The ECASD says no, and the procedure stops immediately. SM-SR2 deletes its local EIS copy.

**Failures after the commit point.** Step 23 passed, SM-SR2 owns the eUICC, then something breaks during finalisation. SM-SR2 still returns "Executed-Success" or "Executed-WithWarning" : never "Failed." SM-SR1 deletes its EIS regardless. Ownership is unambiguous.

**Retry with partial completion.** Imagine SM-SR1's timer expires after step 22, but SM-SR2 actually completed step 23 on the first attempt. On retry, the whole handshake (steps 7–23) gets skipped: the eUICC already has the new keys. SM-SR2 signals "eUICC already managed," SM-SR1 returns "Success_WithWarning," and finalisation proceeds directly.

**Can't delete old keys?** If step 25 fails (SM-SR1's keys won't delete from the ISD-R), SM-SR2 is still responsible for management. It returns a warning but continues. The old keys become a cleanup problem, not a blocking error.

---

## Why this defeated vendor lock-in

SM-SR Change is SGP.02's most politically significant design choice. The architecture was built from the ground up so that no single entity could hold an eUICC hostage:

- **SM-SR1 can't block authentication.** The eUICC authenticates SM-SR2 through the CI root (burned into the ECASD at manufacture) not through SM-SR1. SM-SR1 relays messages but can't forge or suppress the cryptographic handshake.
- **The eUICC is the ultimate authority.** The ECASD private key (`SK.ECASD.ECKA`) never leaves the chip. SM-SR2 has to prove its identity to the eUICC directly.
- **The protocol works even with a reluctant SM-SR1.** As long as SM-SR1 relays messages correctly (which it's contractually obligated to do) the handover succeeds. The spec mandates SM-SR1 support for the procedure.
- **Nothing gets lost.** All Profiles, their states, and their policy rules survive the migration intact. The Operator's relationship with each Profile is preserved. Only the backend Platform Management provider changes.

In an industry where 15-year device lifecycles are routine and vendor relationships rarely last that long, SM-SR Change isn't a nice-to-have. It's load-bearing architecture.

---

### In one breath

- SM-SR Change is a 32-step, four-entity protocol for migrating eUICC management between SM-SRs
- It reuses the ECKA-EG key establishment mechanism from Profile Download: same math, different target (ISD-R keys instead of ISD-P keys)
- ES7 carries three functions: `HandoverEUICC` (EIS transfer), `AuthenticateSM-SR` (certificate provisioning), `CreateAdditionalKeySet` (key agreement)
- Step 23 is the atomic commit point, receipt verified, SM-SR2 is now Platform Manager
- All Profiles, ISD-Ps, and eUICC state survive intact; only the Platform Management keys change
- Error handling supports retry, partial completion, and graceful degradation without ambiguous ownership

---

<div align="center">

<a href="{{ site.baseurl }}/">🏠 Home</a>

Previous: <a href="06-sgp02-lifecycle">Profile Lifecycle: Enable, Disable, Delete, and Fall-Back</a> →
Next: <a href="08-sgp02-resilience">Resilience: Fall-Back Mechanism, Emergency Profiles, and Test Profiles</a> →

</div>

---

*Based on GSMA SGP.02 v4.2 (07 July 2020) : Remote Provisioning Architecture for Embedded UICC Technical Specification, §3.8–3.9, §5.6*


---

← Previous: [Profile Lifecycle: Enable, Disable, Delete, and Fall-Back](06-sgp02-lifecycle) | [Section Index](index) | Next: [Resilience: Fall-Back Mechanism, Emergency Profiles, and Test Profiles](08-sgp02-resilience) →
