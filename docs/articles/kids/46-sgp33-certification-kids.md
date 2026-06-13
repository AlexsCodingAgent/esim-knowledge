---
description: "Why IoT eIM certification matters in a multi-vendor world: how passing SGP.33-3 tests transforms a lab prototype into a trusted remote management server ready for real robot fleets."
title: "From Practice Drills to Real Missions: Getting Certified"
date: 2026-06-07
---

# From Practice Drills to Real Missions: Getting Certified 🏆

## Imagine...

You've built Mission Control. It works in the simulator. But before you can command a real robot fleet, you need a **license**. You go to an independent testing agency, they run every drill in the book, and if you pass: you get certified. Now operators trust you with their robots.

That's the certification journey for an eIM product. Passing SGP.33-3 test cases is the gateway from a lab prototype to a production-ready remote management server.

---

## Why Certification Matters 🎯

IoT eSIM isn't a single-vendor world. A real deployment might have:

- An **eIM** from Company A
- **eUICCs** from Company B  
- **IPAs** from Company C
- **SM-DP+** servers from Company D
- **SM-DS** servers from Company E

All these pieces come from different companies, but they must work together **flawlessly**. Certification gives everyone confidence that each piece holds up its end of the bargain.

---

## The Multi-Vendor Puzzle 🧩

Here's what a real IoT eSIM deployment looks like: way more complex than consumer eSIM:

```
        Operator (mobile company)
            │
            ▼
    ┌──────────┐    ┌──────────┐
    │  SM-DP+  │◄──►│  SM-DS   │
    │(Key Maker)│    │(Post Office)│
    └────┬─────┘    └────┬─────┘
         │ES9+'          │ES11'
         ▼               ▼
    ┌─────────────────────────┐
    │         eIM             │  ← THIS is what SGP.33-3 certifies
    │   (Mission Control)     │
    └────────────┬────────────┘
                 │ESipa
         ┌───────┴───────┐
         ▼               ▼
    ┌─────────┐    ┌─────────┐
    │  IPA    │    │  IPA    │  ← Many robot devices
    │(Device 1)│    │(Device 2)│
    └────┬────┘    └────┬────┘
         │               │
         ▼               ▼
    ┌─────────┐    ┌─────────┐
    │ eUICC   │    │ eUICC   │
    └─────────┘    └─────────┘
```

One eIM might manage **thousands** of robots, each with different eUICCs and IPAs from different vendors. That's why certification is non-negotiable.

---

## The Certification Workflow 📝

### Step 1: Vendor Readiness

Before testing begins, the eIM vendor prepares:

- The eIM implementation itself
- An **Optional Features Declaration** : what the eIM does and doesn't support:

| Feature | Question |
|---------|----------|
| O_S_TRID | Does the eIM send Transaction IDs with packages? |
| O_S_PKG_RETRIEVAL | Does the eIM support Package Retrieval mode? |
| O_S_ESIPA_HTTPS | Does the eIM use TLS on ESipa? |

- **IUT Settings** : the eIM's address, ID, supported RSP version

### Step 2: Test Execution

The accredited lab sets up the General Test Environment with all four simulators and runs every applicable test:

- ✅ Interface compliance tests (every API call)
- ✅ System behaviour tests (end-to-end procedures)
- ✅ Security tests (TLS, certificates, signatures)

### Step 3: Results and Approval

Each test gets a verdict: Pass, Fail, or Inconclusive. Failed tests can be retried after fixes. Once all mandatory and applicable conditional tests pass, the product proceeds to certification.

---

## SAS-SM: The Security Audit for Servers 🔐

Testing protocol behaviour is one thing. But the **GSMA Security Accreditation Scheme** (SAS) goes further:

- **SAS-UP** audits eUICC manufacturing sites (chip factories)
- **SAS-SM** audits subscription management platforms: and that now includes **eIM platforms**

An eIM must prove:

- 🔑 Secure key storage (the eIM's private signing keys)
- 📋 Access controls and audit logging
- 🌐 Network security and TLS configuration
- 📜 Operational security procedures

SGP.33-3 test cases indirectly verify SAS-relevant properties: TLS configuration, certificate validation, anti-replay mechanisms: but the full SAS audit is a separate process run by GSMA-accredited auditors.

---

## What's Certifiable Today 📊

Not everything is ready for certification yet:

| Interface | Status | Certification Ready? |
|-----------|--------|---------------------|
| **ES9+'** (eIM→SM-DP+) | Fully defined ✅ | Ready: adapted from proven consumer tests |
| **ES11'** (eIM→SM-DS) | Fully defined ✅ | Ready: adapted from proven consumer tests |
| **ESep** (eIM→eUICC) | Partially defined ⚠️ | Limited: most PSMO sequences still FFS |
| **ESipa** (eIM→IPA) | Requirements only ⚠️ | Not certifiable: all sequences FFS |
| **Behaviour** (Profile Enable) | One test case ⚠️ | Conditional only |

For today's eIM vendors, the practical strategy is: certify ES9+' and ES11' first, conduct bilateral interoperability testing for ESipa/ESep, and track the specification as it evolves.

---

## Beyond Isolated Testing 🔭

SGP.33-3 tests the eIM in isolation. But production deployment needs **end-to-end testing** with real eUICCs, IPAs, and servers: an area still marked "For Future Study" in the broader GSMA testing framework.

For now, vendors fill this gap with:
- Bilateral testing with partner companies
- Consortium test events
- Real-world field trials

The certification path is still being paved: but the foundation (ES9+' and ES11' testing) is solid.

---

SGP.33-3 connects to at least five other GSMA documents: SGP.33-1 (IPA testing), SGP.33-2 (SM-DP+ testing), SGP.23 (consumer testing), SGP.26 (test certificates), and the GlobalPlatform DLOA framework. No specification is an island!

---

*Kid-friendly version of GSMA SGP.33-3: eUICC IoT Manager Test Specification, Certification Path*

← [Back to Kids Articles](index)
