---
title: "Shields Up! Stopping Drills, Spies, and Hackers"
date: 2026-06-07
---

# Shields Up! Stopping Drills, Spies, and Hackers 🛡️

## Imagine...

Someone wants to break into a bank vault. They could try picking the lock (that's a logical attack). Or they could get clever: drill through the wall, listen to the tumblers with a stethoscope, or blast it with heat to weaken the steel. These are **physical attacks** — they don't trick the lock, they attack the vault itself.

eUICC chips face the same threat. An attacker who holds the device can probe the chip, measure its power consumption, blast it with lasers, or yank the power at just the wrong moment. SGP.25 has specific requirements to stop all of these.

---

## The Physical Attack Threat: T.PHYSICAL-ATTACK ⚡

SGP.25 defines physical attacks as a "second-level" threat — they bypass all the normal logical protections entirely:

| Attack Category | How It Works | What They're After |
|----------------|-------------|-------------------|
| **Side-Channel Analysis** | Measure power usage or EM emissions during crypto operations | Secret keys, session keys |
| **Fault Injection** | Flip bits with voltage spikes, lasers, or EM pulses | Bypass security checks |
| **Electrical Probing** | Touch probes to internal bus lines | Sniff data in transit |
| **Environmental Stress** | Heat, cold, voltage manipulation | Cause unexpected behaviour |
| **Unexpected Tearing** | Cut power during sensitive operations | Leave the chip in an inconsistent state |
| **IC Failure Analysis** | Decapsulate the chip, reverse-engineer layers | Extract TSF code, keys |

All of these target the physical reality of the chip — not bugs in code, but the fact that computation consumes power, takes time, and can be disrupted.

---

## FPT_EMS.1: The Side-Channel Shield 🔇

The main SFR fighting physical attacks is **FPT_EMS.1/Base** — TOE Emanation Control. In plain language:

> "The chip must not leak secrets through its physical emanations."

What are "emanations"? Things an attacker can observe from outside:

| Observable Phenomenon | Attack Type | What It Reveals |
|----------------------|-------------|-----------------|
| **Power consumption** over time | SPA / DPA | Individual bits of secret keys |
| **Execution time** variations | Timing attacks | Whether a key bit is 0 or 1 |
| **Electromagnetic radiation** | EM analysis | Internal data processing |
| **Radio emissions** | RF analysis | Internal operation patterns |

The chip must resist **state-of-the-art attacks** against all of these. Not just the attacks known when the chip was designed — the requirement is forward-looking.

### What's Protected?

- 🔑 **D.SK.EUICC.ECDSA** — The chip's private key (the most valuable asset)
- 🔐 **D.SECRETS** — One-time keys, shared secrets, session keys
- 📦 **D.MNO_KEYS** — Operator keys within profiles
- 📡 **D.PROFILE_NAA_PARAMS** — Network authentication parameters

---

## The Hardware Shield: The Secure IC 💪

SGP.25 delegates physical defence to the underlying **Secure IC** (the chip hardware itself). The IC must be independently certified under its own Protection Profile:

- **[PP0084]** — Security IC Platform Protection Profile
- **[PP0117]** — Security IC Platform for SoC subsystems

The IC must provide four essential capabilities:

### 1. Non-Bypassability and Non-Alterability
> The hardware must prevent TSF functions from being bypassed or altered through low-level access.

This means: even if you have physical probes on the chip's buses, you can't skip the security checks.

### 2. Secure Cryptographic Processing
> The IC must provide secure cryptographic primitives — key generation, signing, verification — that resist physical observation.

### 3. Structured Memory with Access Controls
> Memory must be structured with segmentation fault detection. Transient objects never stored in non-volatile memory.

This prevents buffer overflow attacks and memory-based exploits at the hardware level.

### 4. Atomic Memory Operations
> Memory operations (especially during state transitions) must be atomic — all or nothing.

---

## Power Loss Recovery: OE.IC.RECOVERY 🔌

What if an attacker pulls the power at exactly the wrong moment? This is called **unexpected tearing**. SGP.25 requires:

> "If power is lost during an operation, the IC must allow the TOE to eventually complete the interrupted operation successfully, or recover to a consistent and secure state."

No half-installed profiles. No partially generated keys. No "confused" chip state that an attacker could exploit. Every operation is either complete or safely rolled back.

---

## Three Layers of Side-Channel Defence 🏰

Physical security isn't just the hardware's job. SGP.25 distributes it across three layers:

### Layer 1: Secure IC (Hardware)
- Power consumption smoothing
- Clock randomisation
- Shielded buses and metal layers
- Physical sensors (light, temperature, voltage)

### Layer 2: Runtime Environment (Software Platform)
- The RE must protect confidentiality of all TOE data it processes
- Security architecture must explicitly address side-channel coverage
- Java Card implementations must incorporate countermeasures

### Layer 3: TOE Software (eUICC Application)
- FPT_EMS.1 requires side-channel resistance from the TOE itself
- Secret data transmitted between ECASD and ISD-R/ISD-P must be protected
- Profile Rules Enforcer and Profile Package Interpreter must protect processed data

Defence in depth: if the attacker beats one layer, the next one still stands.

---

## The Chain of Trust: Secure Manufacturing 🏭

Security begins before the chip is even finished. SGP.25 defines a five-phase life-cycle:

| Phase | Activity | Security Requirement |
|-------|----------|---------------------|
| **Phase a** | Software development | ALC_DVS.2-protected environment |
| **Phase b** | IC manufacturing & packaging | SAS-accredited facility |
| **Phase c** | Software embedding onto IC | Secure site (may combine with Phase d) |
| **Phase d** | eUICC personalisation (key injection) | **GSMA SAS-accredited site** |
| **Phase e** | Operational deployment | In the field |

The critical moment is **Phase d** — that's when the chip's private key and eSIM CA public key are injected. This MUST happen at a SAS-accredited facility with audited physical security, access controls, and key management procedures.

If an attacker compromises the personalisation process, they don't need to break the chip — they can inject their own keys from the start.

---

## Tamper Evidence and Self-Protection 🚨

The ADV_ARC.1 requirement adds another layer:

> "The TSF must protect itself from tampering by untrusted active entities."

The security architecture must demonstrate:
- Even if one component is compromised, others remain protected
- The domain separation (ISD-R, ECASD, ISD-P isolation) provides structural defence
- Tampering attempts are detectable

This is like having a vault where each safe deposit box has its own independent lock — breaking into one doesn't give access to the rest.

---

## 🧠 Did You Know?

Side-channel attacks are remarkably powerful. Differential Power Analysis (DPA) can extract a 256-bit encryption key by measuring the chip's power consumption across thousands of operations and looking for tiny statistical correlations. Countermeasures like constant-time code, power smoothing, and random delays make this practically impossible on a certified eUICC.

---

*Kid-friendly version of GSMA SGP.25 v2.1 — Physical Security*

← [Back to Kids Articles](index)
