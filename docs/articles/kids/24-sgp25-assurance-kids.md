---
description: "How eUICC chips prove they are secure at EAL4+ — the highest practical evaluation level, with six pillars of proof covering design, life-cycle controls, testing, and expert penetration attempts."
title: "Proving It's Safe: EAL4+ and the Penetration Test"
date: 2026-06-07
---

# Proving It's Safe: EAL4+ and the Penetration Test 🕵️

## Imagine...

You're the inventor of a new safe. You *say* it's unbreakable. But a real security company won't take your word for it. They send in **penetration testers** : experts whose job is to break in by any means necessary. They drill, pick locks, use stethoscopes, and try every trick in the book. If they can't get in : *then* the safe gets certified.

That's exactly what **EAL4+** means for eUICC chips. The "plus" is the penetration test. And it's the hardest part of the entire evaluation.

---

## The Six Pillars of Proof 🏛️

SGP.25's assurance requirements are divided into six classes:

| Class | What It Checks | The Question It Answers |
|-------|---------------|------------------------|
| **ADV** (Development) | Design docs, source code, architecture | "Is it well-built?" |
| **AGD** (Guidance) | User manuals, setup instructions | "Do operators know how to use it safely?" |
| **ALC** (Life-Cycle) | Development security, delivery, tools | "Was it built in a secure environment?" |
| **ASE** (Security Target) | Conformance claims, objectives | "Does the paperwork match reality?" |
| **ATE** (Tests) | Functional testing, coverage, independent tests | "Does everything work as documented?" |
| **AVA** (Vulnerability) | Penetration testing | "Can we break it?" |

Together, these six classes leave no stone unturned. Let's look at each.

---

## ADV: Show Me the Blueprints 🗺️

The Development class demands four levels of documentation:

| Component | What They Review |
|-----------|-----------------|
| **ADV_ARC.1** | Security architecture: how domains are separated, how the chip protects itself from tampering |
| **ADV_FSP.4** | Complete functional specification: every single interface documented |
| **ADV_IMP.1** | Source code: evaluators actually read the implementation |
| **ADV_TDS.3** | TOE design: modular breakdown of subsystems |

Architecture has special refinements. The design must show:
- How security domains (ISD-R, ECASD, ISD-P) stay separate
- How the chip protects itself from tampering by untrusted entities
- How security functions cannot be bypassed

If the documentation is incomplete or the design has gaps: evaluation stops right here.

---

## ALC: Was It Built Safely? 🏭

Software security starts at the keyboard. The Life-Cycle class verifies:

| Component | What It Means |
|-----------|---------------|
| **ALC_CMC.4** | Configuration management: every version tracked |
| **ALC_CMS.4** | CM covers the TOE, evidence, AND development tools |
| **ALC_DEL.1** | Secure delivery: no tampering during distribution |
| **ALC_DVS.2** | Development security: physical, procedural, personnel controls |
| **ALC_LCD.1** | Defined life-cycle with development, manufacturing, and operational phases |
| **ALC_TAT.1** | Well-defined development tools under configuration control |

**ALC_DVS.2** is one of the two augmentations that make this "EAL4+". Standard EAL4 only requires ALC_DVS.1 (security measures exist). The "+" demands **sufficiency** : the evaluator must agree the measures are actually good enough given the threat model. It's the difference between "we have a lock on the door" and "that lock is Grade 1, pick-resistant, and inspected weekly."

---

## ATE: Does It Actually Work? ✅

Testing goes beyond the vendor's own QA:

| Component | What It Requires |
|-----------|-----------------|
| **ATE_COV.2** | Rigorous analysis of test coverage against the functional spec |
| **ATE_DPT.1** | Testing based on the design: test subsystems and interfaces |
| **ATE_FUN.1** | Functional testing per the specification |
| **ATE_IND.2** | Independent testing by the evaluators using a sample of the TOE |

The evaluators don't just watch the vendor run tests: they run their **own** tests on the actual product. Independent verification, not self-assessment.

---

## 🔥 AVA_VAN.5: The Penetration Test

This is the crown jewel of EAL4+. Standard EAL4 only requires AVA_VAN.3 ("focused vulnerability analysis") : searching public sources for known vulnerabilities. AVA_VAN.5 is a different beast entirely:

### What Evaluators Do

1. **Search** public sources: vulnerability databases, academic papers, conference talks: for attack techniques relevant to the TOE
2. **Analyse** the design, source code, and architecture for potential weak spots
3. **Devise** penetration tests targeting those weak spots
4. **Execute** the attacks on the actual TOE in its operational configuration
5. **Document** everything so findings are reproducible

### Attack Techniques Used

| Category | Examples |
|----------|----------|
| **Side-Channel Analysis** | Simple Power Analysis (SPA), Differential Power Analysis (DPA), timing attacks, EM emissions analysis |
| **Fault Injection** | Voltage glitching, clock manipulation, laser fault injection, electromagnetic pulses |
| **Protocol Attacks** | Fuzzing, state machine analysis, replay attacks, man-in-the-middle |
| **Logical Attacks** | Buffer overflows, type confusion, API misuse |

### Attack Potential Required

AVA_VAN.5 requires **elevated attack potential** : evaluators must employ techniques matching attackers with:
- Significant expertise in smart card security
- Specialised equipment (oscilloscopes, glitching tools, EM probes)
- Time and resources beyond casual attackers

The GSMA specifically notes that AVA_VAN.5 *"is considered as the expected level for Java Card technology-based products hosting sensitive applications"*. This is the bar: not exceptional, but expected.

---

## How Assurance Validates Function 🔗

The assurance requirements don't exist in isolation. They prove the functional requirements actually work:

| Functional Claim | How Assurance Checks It |
|-----------------|------------------------|
| "We authenticate every actor" | ADV_FSP.4 documents every interface; ATE_COV.2 verifies all are tested; AVA_VAN.5 tries to bypass authentication |
| "Our secure channels are encrypted" | ADV_TDS.3 documents protocols; ATE_DPT.1 tests subsystems; AVA_VAN.5 tests channel tampering |
| "Profiles are isolated from each other" | ADV_ARC.1 documents separation; ATE_IND.2 independently tests isolation; AVA_VAN.5 attempts cross-domain access |
| "Keys resist extraction" | ADV_IMP.1 provides source code; AVA_VAN.5 performs SPA/DPA to extract keys |
| "We resist side channels" | FPT_EMS.1 declares the requirement; AVA_VAN.5 actively tests it |

---

## The Optional Extra: Flaw Reporting 📬

SGP.25 offers an optional component: **ALC_FLR.2** : formal flaw reporting procedures. When included:

- Security flaws discovered post-certification go through formal channels
- The vendor analyses, fixes, and distributes corrections
- Users know how to report problems
- This creates an ongoing security lifecycle, not just a one-time check

---

The "augmented" in EAL4+ comes from TWO specific additions: ALC_DVS.2 (development security sufficiency) and AVA_VAN.5 (advanced penetration testing). Both raise the bar significantly from standard EAL4. The GSMA judged standard EAL4 insufficient for chips that hold operator credentials worth millions and resist physical attacks for a decade.

---

*Kid-friendly version of GSMA SGP.25 v2.1: Assurance Requirements*

← [Back to Kids Articles](index)
