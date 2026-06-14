---
title: "Physical Security: Side-Channel and Fault Injection Defences"
description: "Examines SGP.25's physical security requirements : resistance to side-channel analysis, fault injection, and tampering : plus the secure IC platform certification and trusted manufacturing lifecycle phases."
date: 2026-06-05
---

# Physical Security: Side-Channel and Fault Injection Defences

**[eUICC.tech]({{ site.baseurl }}/) > [SGP.25 eUICC Security]({{ site.baseurl }}/docs/articles/sgp25/) > Physical Security: Side-Channel and Fault Injection Defences**

> **Why this matters:** An eUICC doesn't just face network-based attacks: it sits inside a device that an adversary can physically hold, probe, and manipulate. Side-channel analysis can extract cryptographic keys from power consumption patterns. Fault injection can flip bits during critical operations. Physical tampering can expose internal buses and memory. SGP.25 explicitly addresses these threats, requiring the TOE and its underlying platform to resist attackers with oscilloscopes, glitching tools, and lab benches.

> **Key takeaways:**
> - T.PHYSICAL-ATTACK is a "second-level" threat covering environmental stress, electrical probing, side channels, fault injection, and physical tampering
> - FPT_EMS.1/Base requires the TOE to resist emissions-based attacks: SPA, DPA, timing analysis, and electromagnetic radiation analysis
> - The secure IC (operational environment) must be certified against [PP0084] or [PP0117], providing hardware-level physical defenses
> - OE.IC.SUPPORT requires atomic memory operations, segmentation fault detection, and secure low-level cryptographic processing
> - O.DATA-CONFIDENTIALITY and O.DATA-INTEGRITY objectives apply to both the TOE and Runtime Environment, including explicit side-channel resistance
> - Secure manufacturing processes (life-cycle phases a–e) create a chain of trust from IC fabrication through personalisation to operational deployment

* TOC
{:toc}

Physical attacks represent a qualitatively different threat than logical attacks. They don't exploit bugs in software: they exploit the physical reality that every computation consumes power, takes time, emits radiation, and can be disrupted. SGP.25's treatment of physical security spans the TOE's own SFRs, the objectives placed on the operational environment (IC, Runtime Environment), and the life-cycle controls on manufacturing.

---

## The Threat: T.PHYSICAL-ATTACK

SGP.25 defines physical attacks as a distinct "second-level" threat that bypasses all first-level protections:

> "The off-card actor discloses or modifies the design of the TOE, its sensitive data or application code by physical (as opposed to logical) tampering means."

The formal threat definition encompasses:

| Attack Category | Examples | Assets Threatened |
|----------------|----------|-------------------|
| **Environmental stress** | Temperature extremes, voltage manipulation, clock glitching | All assets |
| **IC failure analysis** | Decapsulation, micro-probing, reverse engineering | D.TSF_CODE, keys |
| **Electrical probing** | Monitoring bus lines, memory bus sniffing | D.SECRETS, D.SK.EUICC.ECDSA |
| **Side channels** | SPA, DPA, electromagnetic analysis, timing attacks | Secret keys, session keys |
| **Fault injection** | Voltage glitching, laser fault injection, EM pulses | Execution integrity |
| **Unexpected tearing** | Power removal during sensitive operations | Atomicity of state transitions |
| **Instruction manipulation** | Altering execution order through physical means | TSF code integrity |

All assets of the TOE are directly threatened: from private keys and session secrets to TSF code and Profile data. A successful physical attack could clone the eUICC, extract operator credentials, or bypass profile policy enforcement entirely.

---

## FPT_EMS.1/Base: TOE Emanation Control

The primary SFR directly addressing physical attacks is FPT_EMS.1/Base:

```
FPT_EMS.1.1/Base
The TSF shall ensure that the TOE does not emit emissions over its attack
surface in such amount that these emissions enable access to TSF data
and user data as specified.
```

### Protected Assets

The assets explicitly protected from emanation-based disclosure:

- **TSF data**: D.SECRETS (one-time keys, shared secrets, session keys), D.SK.EUICC.ECDSA (eUICC private keys)
- **User data**: Secret keys within D.MNO_KEYS and D.PROFILE_NAA_PARAMS

### Attack Techniques Covered

The Application Note provides a detailed catalogue of the attack classes that must be resisted:

> "The TOE shall prevent attacks against the secret data of the TOE where the attack is based on external observable physical phenomena of the TOE. Such attacks may be observable at the interfaces of the TOE or may originate from internal operation of the TOE or may originate from an attacker that varies the physical environment under which the TOE operates."

| Attack | Description | Observable Phenomenon |
|--------|-------------|---------------------|
| **Simple Power Analysis (SPA)** | Direct interpretation of power consumption traces during cryptographic operations | Power consumption over time |
| **Differential Power Analysis (DPA)** | Statistical correlation between power consumption and processed data across many operations | Aggregated power traces |
| **Timing attacks** | Measuring execution time variations that depend on secret data | Transition timing of internal states |
| **Electromagnetic radiation analysis** | Capturing and analysing EM emissions from the chip during computation | Electromagnetic radiation |
| **Radio emission analysis** | Detecting radio-frequency emissions from internal operation | Radio emissions |

The evaluator is expected to assess resistance against **state-of-the-art attacks applicable to the technologies employed by the TOE** : a forward-looking requirement that keeps pace with advancing attack techniques.

---

## The Secure IC: Hardware-Level Defences

SGP.25 explicitly delegates first-line physical defense to the underlying secure IC. The IC is not part of the TOE but is a required component of the operational environment:

### Required IC Certification

The secure IC must be certified according to:

- **[PP0084]** : Security IC Platform Protection Profile with Augmentation Packages, version 1.0 (BSI-CC-PP-0084-2014), or
- **[PP0117]** : Security IC Platform Protection Profile for a secure subsystem integrated in a SoC

This is a mandatory requirement: the IC's hardware security features are independently evaluated before the eUICC software evaluation begins.

### What the IC Must Provide

OE.IC.SUPPORT specifies four essential capabilities:

```
(1) Non-bypassability and non-alterability of TSF:
 The IC must not allow TSF functions to be bypassed or altered, and
 must not allow access to low-level functions beyond those exposed
 through the API.
 → Includes protection of private data and code against disclosure
 or modification at the hardware level.

(2) Secure low-level cryptographic processing:
 The IC must provide secure cryptographic primitives to the Profile
 Rules Enforcer, Profile Package Interpreter, and Telecom Framework.

(3) Structured memory with access controls:
 Memory model must be structured and allow low-level control
 accesses (segmentation fault detection).
 → Transient objects must not be stored in non-volatile memory.
 → Prevents memory-based attacks (buffer overflows, stack smashing).

(4) Atomic memory operations:
 The IC must provide a means to perform memory operations atomically.
 → Critical for resisting fault injection during state transitions.
```

### Power Loss Recovery

OE.IC.RECOVERY addresses unexpected tearing (power removal during operations):

> "If there is a loss of power while an operation is in progress, the underlying IC must allow the TOE to eventually complete the interrupted operation successfully, or recover to a consistent and secure state."

This prevents attackers from manipulating eUICC state by precisely timing power removal during profile installation, key generation, or state transitions.

### Unique Identification

OE.IC.PROOF_OF_IDENTITY requires the underlying IC to be uniquely identified: a hardware root of trust that anchors the eUICC's identity and prevents chip-swapping attacks.

---

## Side-Channel Resistance Throughout the Stack

Physical security is not just an IC problem. SGP.25 distributes side-channel resistance requirements across three layers:

### Layer 1: Secure IC (OE.IC.SUPPORT)
Hardware countermeasures: power consumption smoothing, clock randomisation, shielded buses, metal layers, sensors

### Layer 2: Runtime Environment (OE.RE.DATA-CONFIDENTIALITY)
> "The Runtime Environment shall provide a means to protect at all times the confidentiality of the TOE sensitive data it processes."

The Application Note explicitly requires:
> "refining the ADV_ARC 'non-bypassability' requirements to explicit the coverage of side channel attacks by the security architecture of the ST TOE."

For Java Card implementations, this means the Java Card System's own security architecture must incorporate side-channel resistance: not just pass through to the hardware.

### Layer 3: TOE Software (FPT_EMS.1/Base, O.DATA-CONFIDENTIALITY)
The TOE itself must ensure that:
- Shared secrets transmitted between ECASD and ISD-R/ISD-P are not disclosed through side channels
- Profile Rules Enforcer, Profile Package Interpreter, and Telecom Framework protect the confidentiality of data they process
- Secret data stored or transmitted within the TOE resists side-channel disclosure

---

## Secure Manufacturing: The Life-Cycle Chain of Trust

Physical security begins long before the eUICC is deployed. SGP.25's life-cycle model (Section 1.2.3) defines a chain of trusted phases:

| Phase | Activity | Security Relevance |
|-------|----------|-------------------|
| **Phase a** | eUICC Platform Development | IC and embedded software development: must occur in ALC_DVS.2-protected environment |
| **Phase b** | IC Manufacturing and Packaging | IC fabrication, pre-personalisation, test: SAS-accredited site |
| **Phase c** | eUICC Platform Storage, Pre-Personalisation, Test | Software embedding onto the IC: may be combined with Phase d if at same secure site |
| **Phase d** | eUICC Personalisation | ECASD/ISD-R key injection, optional provisioning Profile loading : **GSMA SAS-accredited** |
| **Phase e** | Operational Usage | Integration onto Device, SM-DS registration, post-issuance provisioning |

### TOE Delivery Points

The TOE may be delivered (i.e., leave the trusted environment) at three possible stages:

1. **After Phase b** : If the TOE is already self-protected (unusual)
2. **After Phase c** : If the TOE is self-protected, unless Phase c and d occur at the same SAS-accredited site (in which case the eUICC Manufacturer is a trusted administrator)
3. **After Phase d** : The latest delivery point, when the eUICC goes to the customer of the eUICC manufacturer

The ST writer must describe which delivery activities are required in their specific life-cycle model and at which phase the self-protected TOE is delivered.

---

## Tamper Evidence and Resistance

The ADV_ARC.1 architectural design requirement explicitly addresses tampering:

```
ADV_ARC.1.2D: The developer shall design and implement the TSF so that
it is able to protect itself from tampering by untrusted active entities.

ADV_ARC.1.4C: The security architecture description shall demonstrate
that the TSF protects itself from tampering.
```

This means the eUICC software architecture must include self-protection mechanisms that detect and respond to tampering attempts: not just rely on the hardware. The security domain model (ISD-R, ECASD, ISD-P isolation) is the primary architectural mechanism: even if one component is compromised, others remain protected.

---

## Summary

- T.PHYSICAL-ATTACK covers side-channel analysis (SPA/DPA), fault injection, environmental stress, electrical probing, and physical tampering
- FPT_EMS.1/Base requires the TOE to resist emanation-based attacks, with explicit coverage of SPA, DPA, timing attacks, and EM analysis
- The secure IC must be independently certified (PP0084/PP0117) and provides hardware-level defenses: atomic operations, memory protection, and cryptographic processing
- Side-channel resistance is a multi-layer requirement spanning IC, Runtime Environment, and TOE software
- The eUICC life-cycle (Phases a–e) creates a chain of trust from development through manufacturing, personalisation, and deployment
- TOE delivery points define when the product leaves trusted environments, with SAS accreditation required for the personalisation phase

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp25/24-sgp25-assurance">eUICC Assurance Requirements: EAL4+ and Penetration Testing</a> · <a href="{{ site.baseurl }}/">Home</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp25/26-sgp25-certification">SGP.25 Certification: SAS-UP and the Evaluation Process</a> →

</div>

---

*Based on GSMA SGP.25 v2.1 (3 February 2025) : eUICC for Consumer and IoT Devices Protection Profile, Sections 1.2.3 (TOE life-cycle), 3.3.6 (Second-level threats: T.PHYSICAL-ATTACK), 4.1 (Security objectives for the TOE: O.DATA-CONFIDENTIALITY), 4.2.2 (Platform objectives: OE.IC.SUPPORT, OE.IC.RECOVERY), and 6.1 (SFRs: FPT_EMS.1/Base)*


---

← Previous: [eUICC Assurance Requirements: EAL4+ and Penetration Testing](24-sgp25-assurance) | [Section Index](index) | Next: [SGP.25 Certification: SAS-UP and the Evaluation Process](26-sgp25-certification) →
