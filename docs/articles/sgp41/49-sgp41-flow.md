---
title: "IFPP Flow: Manufacturing Step to Configuration Step"
date: 2026-06-06
---

# IFPP Flow: Manufacturing Step to Configuration Step

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.41 IFPP]({{ site.baseurl }}/docs/articles/sgp41/) > IFPP Flow: Manufacturing Step to Configuration Step**

> **💡 Why this matters:** The IFPP flow is SGP.41's beating heart — 16 steps spanning profile preparation, eUICC key delivery, BPP creation, factory-floor loading, and post-production reporting. Understanding this flow reveals why IFPP works where SGP.22 fails: the heavy cryptographic lifting (binding, encryption) happens *before* the profile reaches the production line, and the factory itself does nothing more complex than pushing pre-packaged data. The two-phase split between the Manufacturing Step and the Configuration Step is what enables the flexible inventory management and region-specific provisioning that consumer RSP cannot offer.

> **Key takeaways:**
> - 16 sequential steps grouped into four phases: Profile Preparation (step 1), eUICC Delivery (steps 2–4), Profile Delivery (steps 5–7), and Profile Loading + Reporting (steps 8–16)
> - The flow is a **two-phase process**: a Manufacturing Step (build generic hardware, place in stock) followed by a Configuration Step (add customer/region-specific profiles before shipping)
> - Profile Loading (steps 8–12) can happen **completely offline** — no internet, no external connectivity required
> - The number of profiles requested at step 5 may be a *subset* of those prepared at step 1, enabling bulk generation with just-in-time binding
> - A Profile Loading Report aggregates eUICC-signed Installation Results and FPA-reported errors into a single file for the SM-DPf
> - The flow is designed for **multiple profiles per eUICC** from **multiple SM-DPfs** — repeat the procedure for each profile-MNO combination
> - All pre-step-8 steps can be reordered as long as preconditions are met — e.g., eUICC delivery (step 2) can happen after profile delivery (step 7)

The IFPP procedure in SGP.41 Section 5.1 defines a complete end-to-end flow from profile ordering through post-production reporting. While shown for a single profile from a single SM-DPf, it is designed to be repeated for multiple profiles from multiple operators.

---

## The 16-Step Flow

### Phase 1: Profile Preparation

```
MSP ──[1] prepare Profiles request──▶ SM-DPf
```

**Step 1**: The Mobile Service Provider (Operator) requests the SM-DPf to prepare Profiles. This is the batch trigger — the Operator says "I need N profiles for devices from Manufacturer X." The SM-DPf may generate all N profiles at once (bulk generation) and bind them individually as needed (just-in-time binding).

---

### Phase 2: eUICC Delivery and Key Distribution

```
EUM ──[2] eUICCs──▶ Device Manufacturer
```

**Step 2**: The EUM delivers IFPP-capable eUICCs (with pre-loaded one-time keys) to the Device Manufacturer. These eUICCs have already been personalised with EIDs, certificates, and an agreed number of private one-time keys during the Two-Step Personalisation Process (GSMA FS.18).

Then, one of two paths for eUICC data:

```
Path A:  EUM ──[3] eUICC data (keys, certs)──▶ SM-DPf
Path B:  EUM ──[4] eUICC data (keys, certs)──▶ Device Manufacturer
```

**Step 3 (Path A)**: The EUM sends eUICC data directly to the SM-DPf via `Esed1`. The data includes one-time public keys, eUICC certificates, eUICC Info 2, and the EUM certificate chain — packaged in an interoperable data structure.

**Step 4 (Path B)**: Alternatively, the EUM sends the same data to the Device Manufacturer via `Esed2`, who will later forward it to the SM-DPf when requesting profiles. This path gives the Device Manufacturer more control over which SM-DPf receives which eUICC's data.

---

### Phase 3: Profile Delivery — Binding Before Delivery

```
Dev Mfr ──[5] request for BPPs [with eUICC data]──▶ SM-DPf
         [6] create BPPs (inside SM-DPf)
Dev Mfr ◀──[7] send BPPs── SM-DPf
```

**Step 5**: The Device Manufacturer requests BPPs from the SM-DPf over `Esbpp`. If the eUICC data followed Path B (step 4), the request includes one one-time public key and eUICC certificate(s) per profile requested. eUICC Info 2 and the EUM certificate chain only need to be provided once per batch.

The spec notes an important optimisation: *"The number of Profiles requested at step 5 may be a part or the totality of the Profiles requested at step 1."* This enables:
- The SM-DPf to generate profiles in large quantities (efficient batch processing)
- The Device Manufacturer to bind in smaller quantities (flexible inventory management)
- On-demand binding without re-generating the entire batch

**Step 6**: The SM-DPf creates the Bound Profile Packages. This is where the heavy lifting happens:
1. The SM-DPf performs an **eUICC eligibility check** as instructed by the Profile Owner (DPFF09)
2. It verifies the integrity and authenticity of the eUICC data (DPFF10)
3. It binds the Protected Profile Package to the target eUICC using the one-time public key — encrypting the profile such that only that specific eUICC can decrypt it
4. The binding incorporates **Perfect Forward Secrecy (PFS)** (GENS06)

**Step 7**: The BPPs and related SM-DPf data (e.g., SM-DPf certificate chain) are forwarded to the Device Manufacturer. At this point, the Device Manufacturer now holds BPPs that can be installed offline at any time.

---

### Phase 4: Profile Loading — The Factory Floor

Steps 8–12 happen *during the Device Production Process*. These are the only steps that touch the physical production line — and they require no internet connectivity.

```
Dev Mfr ──[8] BPP──▶ FPA ──[9] BPP──▶ eUICC
                   [10] Profile installation (inside eUICC)
Dev Mfr ◀──[12] Profile Installation Result── FPA ◀──[11] Profile Installation Result── eUICC
```

**Step 8**: The Device Manufacturer's in-factory provisioning system sends the BPP together with related SM-DPf data (certificate chain) to the FPA over `Esfac`.

**Step 9**: The FPA transmits the BPP and SM-DPf data to the eUICC via the FPA Services (`ES10f`). This encapsulates ES8f messages inside ES10f commands.

**Step 10**: The eUICC loads and installs the Profile. It:
- Verifies the SM-DPf certificate chain
- Decrypts the BPP using its one-time private key
- Installs the profile into an ISD-P
- Marks the one-time key as consumed (it cannot be reused — GENS08)

**Step 11**: The eUICC returns the **Profile Installation Result** — a signed data structure confirming success or detailing the failure reason.

**Step 12**: The FPA forwards the Profile Installation Result to the Device Manufacturer's provisioning system.

---

### Phase 5: Post-Production Reporting (Optional)

Steps 13–16 handle reporting. Alternatively, the device may defer notification to after first power-up in the field:

```
[13] Generate Profile Loading Report (inside Dev Mfr)
Dev Mfr ──[14] Profile Loading Report──▶ SM-DPf
         [15] Verify Profile Installation Results (inside SM-DPf)
SM-DPf ──[16] Report──▶ MSP
```

**Step 13**: The Device Manufacturer generates a **Profile Loading Report**. This aggregates:
- One or more eUICC-generated Profile Installation Results (cryptographically signed)
- Reports for profiles that did *not* generate Installation Results — e.g., due to an unreachable or physically damaged eUICC, or FPA execution errors

**Step 14**: The Profile Loading Report is forwarded to the SM-DPf via `Esbpp`.

**Step 15**: The SM-DPf checks the integrity and authenticity of the Profile Installation Results. It verifies signatures against the eUICC certificates received earlier.

**Step 16**: The SM-DPf delivers reports to the Mobile Service Provider, giving them full information on which of their profiles are loaded into which eUICCs after manufacturing.

---

## The Two-Phase Manufacturing Model

Annex A.3 describes a particularly powerful pattern: the **Manufacturing Step / Configuration Step** split:

### Manufacturing Step
The device hardware is built and placed into stock — for example, a PC motherboard or a smart meter without a specific operator assigned. At this stage, the eUICC may or may not have profiles loaded. The device is generic, without customer, region, or operator specificity.

### Configuration Step
When a customer order arrives, the device is pulled from stock and configured — including loading the appropriate profile from the Mobile Service Provider for the customer's region. A modem with eUICC is added to the PC motherboard, and a profile is downloaded to it. Or a smart meter receives a profile based on its shipping destination.

This two-phase model is only possible because of IFPP's pre-binding: the profiles can be ordered, bound, and delivered in advance, stored at the factory, and loaded just-in-time during the configuration step — without requiring network connectivity at either step.

---

## Flexibility and Optimisation

The IFPP flow is designed for real manufacturing environments with several practical flexibilities:

- **Step reordering**: Steps 1–7 can be performed in any order as long as preconditions are met. For example, eUICCs can arrive (step 2) after profiles are already delivered (step 7).
- **Batch optimisation**: The SM-DPf can generate profiles in bulk (step 1) but bind them in smaller quantities (step 6), enabling efficient large-scale generation with flexible, just-in-time binding.
- **Multiple profiles per eUICC**: The entire procedure can be repeated to load several profiles from one or several SM-DPfs onto the same eUICC.
- **Multiple SM-DPfs per Device Manufacturer**: A single Device Manufacturer can work with multiple Operators, each with their own SM-DPf — profiles for different markets or MVNOs are loaded during the same Production Process.

---

## Start and End Conditions

**Start Conditions** (Section 5.1):

- The fully personalised eUICC is prepared for profile loading by the EUM, with relevant key material (one-time keys) pre-loaded
- The Device Manufacturer has ordered eUICCs from the EUM
- Optionally, the Device Manufacturer has indicated an SM-DPf as the recipient for eUICC data
- The Device Manufacturer has ordered Profiles from the Mobile Service Provider

**End Conditions**:

- The eUICCs are provisioned with Profiles at the end of the Device Production Process
- If the reporting option is chosen, the Mobile Service Provider has full information on which Profiles are loaded in which eUICCs

---

## 📋 Summary

- 16 steps across five phases: Profile Preparation → eUICC Delivery → Profile Delivery → Profile Loading → Post-Production Reporting
- The factory-floor loading phase (steps 8–12) operates **fully offline** — BPPs are pre-bound and encrypted before ever reaching the production line
- A two-phase Manufacturing Step / Configuration Step model enables flexible inventory management and region-specific provisioning
- Profile generation and binding can be decoupled: bulk generate, just-in-time bind
- Profile Loading Reports aggregate eUICC-signed results and FPA error reports for delivery to the SM-DPf and ultimately the Operator
- The entire flow repeats cleanly for multiple profiles from multiple operators on a single eUICC

---

<div align="center">

← Previous: [The IFPP Architecture: SM-DPf, FPA, and Device Manufacturer]({{ site.baseurl }}/docs/articles/sgp41/48-sgp41-architecture) · [🏠 Home]({{ site.baseurl }}/)

Next: [IFPP Security: Factory Trust Models and Certificate Chains]({{ site.baseurl }}/docs/articles/sgp41/50-sgp41-security) →

</div>

---

*Based on GSMA SGP.41 v1.0 (28 February 2025) — eSIM In-Factory Profile Provisioning Architecture and Requirements, Section 5.1 and Annexes A, C*


---

← Previous: [The IFPP Architecture: SM-DPf, FPA, and Device Manufacturer](48-sgp41-architecture) | [Section Index](index) | Next: [IFPP Security: Factory Trust Models and Certificate Chains](50-sgp41-security) →
