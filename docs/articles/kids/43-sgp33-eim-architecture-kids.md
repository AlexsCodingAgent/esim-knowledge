---
description: "How SGP.33-3 builds a complete simulated IoT world — five pretend characters surround the real eIM, testing it across four channels without needing a single physical robot."
title: "Practice Drills: Fake Mission Control and Test Robots"
date: 2026-06-07
---

# Practice Drills: Fake Mission Control and Test Robots 🎭

## Imagine...

Before astronauts go to space, they spend months in simulators: fake cockpits, pretend emergencies, practice missions. The real rocket only launches after every drill is perfect. Testing the eIM works exactly the same way: build a **fake Mission Control setup**, surround it with pretend robots and servers, and run through every possible scenario.

This is the **test architecture** of SGP.33-3: a complete simulated IoT eSIM world built just to test one piece: the eIM.

---

## The Star of the Show: The eIM (IUT) 🌟

In testing language, the thing being tested is called the **IUT** : Implementation Under Test. For SGP.33-3, the IUT is:

> **The real eIM** : the actual Mission Control server that the vendor built. Everything else around it is fake.

Why test just one piece? Because if you test everything at once and something breaks, you don't know whose fault it is! By isolating the eIM, testers can prove: "Mission Control itself works correctly."

---

## The Cast of Pretend Characters 🎪

Five simulator types surround the eIM, playing different roles:

| Simulator | Real-World Role | What It Pretends to Be |
|-----------|----------------|----------------------|
| **S_SM-DP+** | Key Maker server | "I'll deliver bound profiles on demand" |
| **S_SM-DS** | Post Office server | "I have event messages waiting for you" |
| **S_eUICC** | Robot's security vault | "I receive eIM Packages and execute orders" |
| **S_IPA** | Robot's on-board translator | "I relay orders and send reports back" |
| **S_CLIENT / S_SERVER** | TLS security testers | "Let's check your encryption is solid" |

The simulator names follow a pattern: `S_` means "Simulated." So `S_eUICC` is "Simulated eUICC" : a pretend vault that follows orders perfectly.

---

## The Test Stage: Four Channels 🎬

Picture the eIM sitting in the centre, with four different radio channels active:

```
         S_SM-DP+ (Fake Key Maker)
              │
            ES9+'    ← "Send me a profile!"
              │
S_SM-DS: ES11' : IUT (eIM) : ESep: S_eUICC (Fake Vault)
              │
            ESipa     ← "Robot, download this!"
              │
           S_IPA (Fake Translator)
```

Each channel tests a different responsibility:

- **ES9+'** : Can the eIM request profiles from a key maker?
- **ES11'** : Can the eIM check for messages at the post office?
- **ESep** : Can the eIM send signed commands to a robot's vault?
- **ESipa** : Can the eIM coordinate with the robot's on-board helper?

---

## What's Inside vs. Outside Scope 🎯

Not everything gets tested by SGP.33-3. Here's the breakdown:

### ✅ In Scope (eIM's Job)

- Talking to Key Makers (ES9+')
- Checking the Post Office (ES11')
- Sending orders to robot vaults (ESep)
- Coordinating with robot translators (ESipa)

### ❌ Out of Scope (Someone Else's Job)

- How operators order profiles (ES2+)
- How the key maker talks to the vault directly (ES8+)
- What the robot's translator does locally (ES10a, ES10b)
- How the post office registers events (ES12)

This keeps testing focused. SGP.33-1 tests the IPA side. SGP.33-2 tests the SM-DP+ side. SGP.33-3 tests the eIM side.

---

## Borrowing from the Experts 📚

Here's a clever trick: many eIM tests are **reused from SGP.23** (consumer eSIM testing)! When the eIM talks to the Key Maker (ES9+'), it acts just like a phone's LPA would. So testers adapted those proven test cases: replacing "LPAd" with "eIM" in the instructions.

This means the IoT testing family didn't have to start from scratch. The well-tested consumer foundation gives IoT testing a head start.

---

The test tools that create all these simulators are built by specialised testing companies: not by the eIM vendor. This independence means the testers have no incentive to go easy on the eIM. It's like having an outside referee instead of letting the home team call their own fouls!

---

*Kid-friendly version of GSMA SGP.33-3: eUICC IoT Manager Test Specification, Test Architecture*

← [Back to Kids Articles](index)
