---
title: "Passing the Ultimate Security Audit: SAS-UP"
date: 2026-06-07
---

# Passing the Ultimate Security Audit: SAS-UP 🏅

## Imagine...

Your new safe has passed every test. The design is solid. The penetration testers gave up. But there's one more step before banks will trust it: a **site audit**. Inspectors visit the factory, check the security cameras, interview the workers, and verify that every safe leaves the factory without being tampered with.

For eUICC chips, this is **SAS-UP** — the GSMA Security Accreditation Scheme for UICC Production. It's the final seal of approval that says: "This chip was built right, in a secure facility, by trusted people."

---

## The Certification Ecosystem: Who's Who 🎭

Getting an eUICC certified involves many players:

| Actor | Role |
|-------|------|
| **GSMA** | Rulebook author — owns SGP.25 and runs the SAS programme |
| **eSIM CA** | Trust anchor — issues certificates to everyone else |
| **EUM** (eUICC Manufacturer) | Chip maker — develops the eUICC, hires the lab |
| **Accredited Lab** | Evaluator — runs all EAL4+ tests including AVA_VAN.5 |
| **Certification Body** | Issuer — reviews the lab's report and grants the certificate |
| **SAS Auditors** | Site inspectors — verify physical and procedural security |

The eSIM CA (Certificate Authority) plays a special role — it's the **root of trust** for the entire public key infrastructure. Its public key is stored in every eUICC's ECASD. If the eSIM CA were compromised, every chip that trusts it would be at risk.

---

## Three Ways to Get Evaluated 🛤️

Not every chip manufacturer starts from the same place. SGP.25 offers three evaluation models:

### Model 1: Composite (Platform Pre-Certified) — The Common Path

```
┌─────────────────┐
│ Certified IC     │ ← Already has [PP0084] certificate
├─────────────────┤
│ Certified OS     │ ← Already has platform certificate
├─────────────────┤
│ Certified RE     │ ← Already has [PP-JCS] certificate
├─────────────────┤
│ eUICC Software   │ ← NEW: evaluated against SGP.25 on top
└─────────────────┘
```

The Security Target references existing certificates for the lower layers. Only the eUICC-specific software is evaluated. This is the most common path — most manufacturers use certified Java Card platforms on certified secure ICs.

### Model 2: Unified (Everything Together)

```
┌─────────────────┐
│ IC + OS + RE +   │ ← ONE big evaluation
│ eUICC Software   │     from hardware to app
└─────────────────┘
```

Everything is evaluated at once. Larger scope, no dependencies on third-party certificates. Used by vertically integrated manufacturers or novel architectures.

### Model 3: Hybrid (IC Only Certified)

```
┌─────────────────┐
│ Certified IC     │ ← Already certified
├─────────────────┤
│ OS + RE +        │ ← NEW: composite evaluation
│ eUICC Software   │     of software on certified IC
└─────────────────┘
```

The IC is pre-certified; everything above is evaluated as a composite product.

---

## The Evaluation Workflow: Step by Step 📋

### Step 1: Build Your Security Target

The vendor writes a **Security Target** (ST) — a document that instantiates SGP.25 for their specific product:

- Which SGP.22 / SGP.32 versions are supported
- Embedded or removable form factor
- Single or Multiple Enabled Profiles (SEP/MEP)
- Cryptographic algorithm selections
- Random number generator class
- Delivery life-cycle (at which phase the TOE leaves the trusted environment)
- Which evaluation model is used

### Step 2: Engage the Lab

The vendor hires a CC-accredited lab. The lab reviews:

- **Security Target** — Is it complete? Does it conform to SGP.25?
- **Development Evidence** — Design docs, source code, architecture
- **Configuration Management** — Version tracking, build processes
- **Development Security** — ALC_DVS.2 audit of the development environment
- **Guidance Documents** — Operator manuals, installation guides
- **Functional Tests** — Vendor's own test suite (coverage analysis by lab)
- **Independent Tests** — Lab runs its own tests on actual TOE samples

### Step 3: The Penetration Test (AVA_VAN.5)

The lab's penetration testers go to work:

- Analyse design and source code for vulnerabilities
- Research public attack techniques applicable to this TOE
- Attempt side-channel extraction (SPA/DPA/EM)
- Attempt fault injection (voltage glitching, laser, EM pulses)
- Test security domain isolation
- Attempt protocol-level bypasses

**If they find a way in — you fail.** Back to engineering. Fix it. Try again.

### Step 4: Certification

The lab produces an **Evaluation Technical Report** (ETR). The national certification body (e.g., BSI in Germany, ANSSI in France) reviews the ETR and issues:

- A **Common Criteria Certificate** — internationally recognised under CCRA
- A **Certification Report** — publicly available summary

31 countries recognise this certificate. One evaluation, global trust.

---

## SAS-UP: The Factory Inspection 🏭

While SGP.25 certifies the **product**, SAS-UP certifies the **factory**:

| SAS-UP Audits | What It Checks |
|---------------|---------------|
| **Physical security** | Perimeter fencing, CCTV, access control, secure areas |
| **Personnel security** | Background checks, training, segregation of duties |
| **Key management** | Generation, injection, storage, destruction procedures |
| **Production segregation** | Separation between phases, clean rooms, anti-contamination |
| **Audit logging** | Who did what, when, where — with tamper-proof records |
| **Secure transport** | How products move between facilities and phases |

The personalisation phase (Phase d) — where the eUICC's private key is injected — MUST occur at a SAS-accredited site. This is non-negotiable.

---

## Two Certifications, One Goal 🎯

SGP.25 and SGP.23-1 work together:

| Aspect | SGP.23-1 (Testing) | SGP.25 (Security) |
|--------|-------------------|-------------------|
| **What it proves** | The chip speaks the protocol correctly | The chip resists attacks |
| **Methodology** | Scripted test cases with known answers | Independent vulnerability analysis |
| **Attacker model** | Protocol misbehaviour | Sophisticated attacker with physical access |
| **Output** | Digital Letter of Approval (DLOA) | Common Criteria Certificate |
| **Governance** | GSMA Test Events + GlobalPlatform | National CC scheme + CCRA |

Both are **required** for production deployment. Protocol conformance without security is useless. Security without protocol conformance is also useless. You need both.

---

## After Certification: The Ongoing Story 📖

Certification isn't "one and done":

- **ALC_FLR.2** (optional) creates a formal flaw reporting channel — security bugs get fixed
- **Assurance continuity** allows incremental updates without full re-evaluation
- **Major changes** (new crypto, new features) may trigger re-evaluation
- **The PP evolves** — SGP.25 v2.1 replaced earlier versions; future versions will add requirements

---

## 🧠 Did You Know?

The SAS accreditation number for the factory is actually embedded in the eUICC's data structure (`EUICCInfo2`). This means any operator receiving a profile notification can trace the chip back to the specific SAS-accredited facility that personalised it. Full traceability from deployment to factory floor — that's trust you can verify!

---

*Kid-friendly version of GSMA SGP.25 v2.1 — Certification and SAS-UP*

← [Back to Kids Articles](index)
