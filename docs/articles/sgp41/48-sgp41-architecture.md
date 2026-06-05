---
title: "The IFPP Architecture: SM-DPf, FPA, and Device Manufacturer"
date: 2026-06-06
---

# The IFPP Architecture: SM-DPf, FPA, and Device Manufacturer

> **💡 Why this matters:** SGP.41 doesn't just tweak existing eSIM components — it introduces three entirely new architectural roles and nine specialised interfaces for the factory environment. Understanding how the SM-DPf differs from a regular SM-DP+, what the FPA actually does (and doesn't do), and how the Device Manufacturer's role expands is essential for anyone designing, deploying, or certifying an IFPP solution.

> **Key takeaways:**
> - **SM-DPf** (Subscription Manager Data Preparation factory): A new SM-DP+ variant that pre-binds profiles before delivery — handles generation, protection, binding, storage, and delivery of BPPs
> - **FPA** (Factory Profile Assistant): A lightweight, factory-only conduit that pushes BPPs into the eUICC and returns results — can be hardware, a driver, or a factory-mode LPA/IPA
> - **Device Manufacturer**: Takes on profile requesting, temporary storage, and provisioning functions — with the critical ability to operate fully offline during profile loading
> - Nine interfaces: ES2f, Esbpp, Esfac, ES10f, ES8f, Esci, Eseum, Esed1, Esed2 — each with specific scope boundaries
> - The eUICC architecture is unchanged from SGP.21 — same ISD-P, ISD-R, ECASD structure — with new FPA Services and one-time key storage added
> - The EUM role gains new responsibilities: provisioning one-time keys into eUICCs during manufacturing

SGP.41 defines a factory-specific variant of the RSP architecture. While it reuses the underlying eUICC structure from SGP.21/SGP.31, it introduces three new actors — the SM-DPf, the FPA, and an expanded Device Manufacturer — connected by interfaces purpose-built for the factory environment.

---

## Architecture Diagram

The IFPP functional architecture involves six actors connected by nine interfaces:

```
eSIM CA ──Esci──▶ EUM ──Eseum──▶ eUICC
   │              │                  ▲
   │ Esci       Esed1              ES8f
   ▼              ▼                  │
SM-DPf ◀──ES2f── Operator           │
   │                                │
   │ Esbpp                          │
   ▼                                │
Device Manufacturer ──Esfac──▶ FPA ──ES10f──▶ eUICC
   ▲                                ▲
   │                                │
   └───── Esed2 ───────────────────┘
```

This is Figure 1 from the specification, showing the Consumer/IoT IFPP architecture. (The M2M variant is marked FFS.)

---

## The New Players

### SM-DPf — Subscription Manager Data Preparation Factory

The SM-DPf is the central profile preparation entity for IFPP. While conceptually similar to the consumer SM-DP+, the SM-DPf is optimised for batch, offline, and pre-provisioned operations. It provides five functions:

| Function | Description |
|----------|-------------|
| **Profile Package Generation** | Creates Profile Packages (IMSI, K, ICCID, etc.) from Profile Descriptions agreed with Operators. Can be an off-line batch or synchronous process. |
| **Profile Package Protection** | Secures each Profile Package according to the security process, creating the Protected Profile Package. |
| **Profile Package Binding** | Binds the Protected Profile Package to a target eUICC using one-time keys, creating the Bound Profile Package. |
| **Profile Package Storage** | Temporarily stores Protected or Bound Profile Packages for subsequent delivery. |
| **Profile Package Delivery for IFPP** | Transmits the BPP to the Device Manufacturer for installation onto the eUICC. |

Functionally, the SM-DPf is the only entity allowed to perform profile generation, protection, and binding (DPFF01–DPFF04). It must be SAS-accredited (DPFS01), and its private key for profile binding must be protected in an SAS-certified HSM (GENS05).

The SM-DPf also receives and verifies **Profile Loading Reports** from the Device Manufacturer, checking the integrity and authenticity of eUICC-signed Profile Installation Results before forwarding results to the Mobile Service Provider (DPFF05–DPFF07).

### FPA — Factory Profile Assistant

The FPA is the on-device (or near-device) proxy that sits between the Device Manufacturer's production system and the eUICC. Its job is simple and narrow:

1. Receive the BPP and related SM-DPf data from the Device Manufacturer's provisioning system
2. Forward it to the eUICC via the FPA Services (ES10f)
3. Return the Profile Installation Result

The FPA is deliberately underspecified — SGP.41 explicitly states that the functional split between the Device Manufacturer and the FPA is irrelevant to the specification. The FPA can be implemented as:

- A hardware solution on the production line
- A low-level driver on the device
- An LPA (Local Profile Assistant) running in factory mode
- An IPA (IoT Profile Assistant) running in factory mode

The interface between the Device Manufacturer and the FPA (`Esfac`) is out of scope — this is intentional, letting each manufacturer integrate the FPA in whatever way suits their production line.

### Device Manufacturer

The Device Manufacturer's role expands significantly in IFPP. Beyond its traditional SGP.21 role of assembling devices containing eUICCs, the Device Manufacturer now:

| Function | Description |
|----------|-------------|
| **Profile Package Requesting** | Requests BPPs from the SM-DPf (with eUICC data) and sends Profile Loading Reports back |
| **Profile Package Storage** | Temporarily stores BPPs for subsequent delivery to the eUICC |
| **Profile Provisioning** | Transmits the BPP to the FPA for installation during the Device Production Process |

Critically, the Device Manufacturer's interfaces fall into two categories: **external** interfaces (Esed2, Esbpp) that communicate with the EUM and SM-DPf outside the factory, and **internal** interfaces (Esfac) that operate on the production floor, potentially fully disconnected from the outside world.

---

## The EUM and One-Time Keys

The eUICC Manufacturer (EUM) gains a new responsibility in SGP.41: provisioning **one-time keys** into the eUICC during manufacturing. These keys are:

- Generated during the Two-Step Personalisation Process (GSMA FS.18), which happens *before* IFPP
- Created and loaded only in a SAS-UP accredited environment (GENS14)
- Randomly generated (GENS07)
- Each used to load only **one** Profile (GENS08)

The EUM sends these eUICC data (certificates, one-time public keys, eUICC Info 2, capabilities) to either:
- The SM-DPf directly via `Esed1`, or
- The Device Manufacturer via `Esed2` (who then forwards them to the SM-DPf)

---

## The Nine Interfaces

SGP.41 defines nine interfaces, several of which are deliberately left out of scope:

| Interface | Between | Purpose | Scope |
|-----------|---------|---------|-------|
| **ES2f** | Operator ↔ SM-DPf | Profile ordering and notification of provisioning results | In scope (similar to ES2+) |
| **Esbpp** | SM-DPf ↔ Device Manufacturer | BPP delivery, eUICC data submission, Profile Loading Reports | In scope — data structures specified; at least one transport mechanism required |
| **Esfac** | Device Manufacturer ↔ FPA | BPP forwarding and result retrieval on the production line | **Out of scope** — implementation-specific |
| **ES10f** | FPA ↔ eUICC (FPA Services) | Transfer of BPP to eUICC and retrieval of Profile Installation Results | In scope — may reuse ES10 functions from SGP.21 |
| **ES8f** | SM-DPf ↔ eUICC | Secure end-to-end channel for ISD-P administration during download/install | In scope — may reuse ES8+ functions from SGP.21 |
| **Esci** | eSIM CA ↔ EUM / SM-DPf | Certificate issuance and revocation status | Out of scope |
| **Eseum** | EUM ↔ eUICC | One-time key provisioning during eUICC manufacturing | Out of scope |
| **Esed1** | EUM ↔ SM-DPf | eUICC data (certs, keys, capabilities) to SM-DPf | Data structure in scope; transport out of scope |
| **Esed2** | EUM ↔ Device Manufacturer | Alternative path for eUICC data to Device Manufacturer | Data structure in scope; transport out of scope |

### Key Interface Details

**Esbpp** is the workhorse for profile delivery. It carries three data structures:
- **BPP delivery** (ESBPP01): One or more Bound Profile Packages from SM-DPf to Device Manufacturer
- **eUICC data request** (ESBPP02): eUICC certificates, keys, and capabilities from Device Manufacturer to SM-DPf when requesting profiles
- **Profile Loading Report** (ESBPP03): Aggregated results including eUICC-generated Profile Installation Results and FPA-reported errors (e.g., unreachable or damaged eUICCs)

At least one transport mechanism must be specified for Esbpp (ESBPP04) — the spec itself doesn't mandate a particular transport, leaving it to be defined elsewhere or by bilateral agreement.

**ES8f** is the analogue of SGP.22's ES8+. It provides the same secure end-to-end channel between the SM-DPf and the eUICC, tunnelled through the FPA via ES10f. The eUICC verifies the SM-DPf's certificates and the BPP's integrity using the same cryptographic mechanisms proven in SGP.21.

**ES10f** encapsulates the FPA-to-eUICC commands. It may directly reuse functions already defined for ES10 (LPA-to-eUICC) in SGP.21, but adds factory-specific operations like authorising the FPA Services and deleting one-time keys after use.

---

## The eUICC: What's Different

The eUICC architecture in SGP.41 is fundamentally the same as SGP.21's — same ISD-P, ISD-R, ECASD, MNO-SD, CASD, NAAs, SSD, and Profile Package Interpreter. The differences are:

1. **FPA Services**: A new service access point for the FPA to communicate with the eUICC during factory provisioning. These services are only available during the Device Production Process (GENS13).

2. **One-time Key Storage**: The eUICC must be able to store one or multiple pre-provisioned one-time keys (EUICCF01), one per profile to be loaded. The Device Manufacturer can delete all remaining unused one-time keys before the end of production (EUICCF03).

3. **Gating of LPA/IPA Services**: The eUICC only authorises LPA Services (SGP.21) or IPA Services (SGP.31) if there are no remaining one-time keys (EUICCF04). This prevents field-side profile management from interfering with factory-provisioned profiles, and vice versa.

4. **Optional Connectivity Test**: The eUICC MAY provide a mechanism for the Device Manufacturer to test a profile's connectivity during the Device Production Process (EUICCF05).

---

## 📋 Summary

- Three new roles: SM-DPf (batch profile binding), FPA (factory conduit), and Device Manufacturer (profile handling and offline provisioning)
- The FPA is deliberately flexible — hardware, driver, or factory-mode LPA/IPA — with its interface to the Device Manufacturer left out of scope
- Nine interfaces connect the ecosystem, with Esbpp (BPP delivery/reporting) and ES8f (secure end-to-end channel) as the most critical
- The eUICC architecture remains the same as SGP.21, with FPA Services, one-time key storage, and service gating added
- The EUM provisions one-time keys during eUICC manufacturing in a SAS-UP environment — one key per profile to be loaded

---

*Based on GSMA SGP.41 v1.0 (28 February 2025) — eSIM In-Factory Profile Provisioning Architecture and Requirements, Sections 2–3*
