---
title: "Crash-Testing eSIMs Before They Go on Sale"
date: 2026-06-07
---

# Crash-Testing eSIMs Before They Go on Sale 🏭🔬

## Imagine...

You're a car manufacturer. Before you can sell your new car, it has to pass hundreds of safety tests. Crash-test dummies get thrown into walls. Brakes get stomped a thousand times. Airbags get popped in empty parking lots. Only cars that pass every single test get to wear the "APPROVED" sticker and go on sale.

eSIMs go through exactly the same thing — but instead of crash-test dummies, there are simulator programs, test chips, and digital inspection checklists. The rulebook for all of this is called **SGP.23** — a 913-page document that says: *"Here is exactly how to prove every piece of the eSIM puzzle works."*

---

## What Gets Tested? 🔍

Four different pieces of the eSIM world get put through their paces:

- **The Vault chip itself** (eUICC) — tested with special card readers that send it commands and check its responses
- **The Phone's Assistant app** (LPA) — tested to make sure it knows how to download, switch, and delete profiles correctly
- **The Key Maker server** (SM-DP+) — tested to make sure it builds keys correctly and delivers them safely
- **The Post Office server** (SM-DS) — tested to make sure it can tell phones "you have a delivery waiting!"

---

## Two Kinds of Tests 📋

| Test Type | What It Checks | Real-World Analogy |
|---|---|---|
| **Interface Testing** | Does every button and command work properly? | Checking every knob, switch, and pedal in the car |
| **Behaviour Testing** | Does the whole system work together end-to-end? | Taking the car for a test drive on a real road |

The interface tests check every single command — hundreds of them — one by one. The behaviour tests put them all together and say: "Okay, now download a profile from start to finish. Does it work?"

---

## It's All Fake (On Purpose!) 🎭

Nobody uses real customer profiles or real servers during testing. Instead, the test lab creates a complete **simulated world**:

- **S_SM-DP+** — a pretend Key Maker server
- **S_SM-DS** — a pretend Post Office
- **S_LPAd** — a pretend Phone Assistant
- **S_MNO** — a pretend mobile company

This way, when they're testing the real eUICC chip, all the other pieces are carefully controlled simulators — so if something goes wrong, they know exactly which piece is to blame.

---

## The Path to the Gold Star ⭐

Every eSIM component that wants to be sold in real phones goes through this journey:

1. **Declare what you can do** — "I support this encryption type, these features..."
2. **Figure out which tests apply** — not every test is needed for every chip
3. **Run the tests** — at an official GSMA Test Event
4. **Pass them all** — every mandatory test, every conditional test
5. **Get your DLOA** — the Digital Letter of Approval, like a gold star sticker that says "CERTIFIED!"

---

## 🧠 Did You Know?

The SGP.23 test specification is 913 pages long — longer than most fantasy novels! It covers over 800 test cases that four different types of eSIM components must pass before they can be used in real phones.

---

*Kid-friendly version of GSMA SGP.23 — RSP Test Specification*

← [Back to Kids Articles](index)
