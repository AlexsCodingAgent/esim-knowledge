---
description: "Inside the eSIM testing lab — nine different simulators pretend to be every part of the ecosystem so that the one real component under test can be checked in perfect isolation."
title: "The Testing Lab: Crash-Test Dummies and Safety Inspectors"
date: 2026-06-07
---

# The Testing Lab: Crash-Test Dummies and Safety Inspectors 🏗️🧪

## Imagine...

You want to test a brand-new car. You can't just drive it on public roads: you need a special testing lab with crash barriers, rolling roads, and crash-test dummies that measure impact forces. You also need fake cars for the real car to crash into, fake pedestrians to detect, and controlled conditions so every test is exactly the same every time.

That's what SGP.23's test infrastructure does for eSIMs. Instead of roads and dummies, it uses **test certificates, test profiles, and nine different simulators** : all designed to create a perfect testing bubble where nothing from the real world can interfere.

---

## The Pretend World 🌍

Everything in the test lab is fake, on purpose:

| Real-World Thing | Test Lab Equivalent |
|---|---|
| Real GSMA certificates | Test certificates (marked with "S_") |
| A real customer's profile | A test profile with a known fake ICCID |
| A real phone | S_Device simulator sending commands |
| A real Key Maker server | S_SM-DP+ simulator |
| A real Post Office | S_SM-DS simulator |
| A real mobile company | S_MNO simulator |
| A real person tapping the screen | S_EndUser simulator |

The rule is simple: **only the thing being tested is real.** Everything around it is a carefully controlled fake. This is called *isolation testing* : and it's the only way to know for sure whether a bug is the chip's fault or the server's fault.

---

## The Nine Simulators 🤖

The test lab has nine different simulator types, each pretending to be one part of the eSIM world:

| Simulator | Pretends to Be... | Why It's Needed |
|---|---|---|
| S_Device | A phone/modem | Sends the exact electrical signals a phone would send |
| S_SM-DP+ | The Key Maker | Generates test profiles with known keys |
| S_SM-DS | The Post Office | Stores and delivers fake event notifications |
| S_MNO | A mobile company | Orders profiles like a real operator would |
| S_LPAd | The Phone Assistant app | Sends the commands an LPA would normally send |
| S_LPAe | The in-chip Assistant | For chips that have the assistant built right in |
| S_EndUser | A human tapping the screen | Simulates someone pressing buttons |
| S_CLIENT | An HTTPS client | Tests the secure internet connection from the client side |
| S_SERVER | An HTTPS server | Tests the secure internet connection from the server side |

---

## Different Labs for Different Tests 🏢

You don't test a chip the same way you test a server:

- **TE_eUICC** : For testing the chip: a card reader connects to the chip's metal contacts and sends APDU commands (tiny electrical messages)
- **TE_Integrated eUICC** : For chips buried inside phone processors: uses a USB test cable instead of physical contacts
- **TE_P1/P2/P3** : For testing the Key Maker server: three different setups depending on which interface is being tested
- **TE_S1-SR2** : For testing the Post Office: seven different setups covering all the ways the SM-DS is used

---

## The Secret Recipe Books 📖

The test lab uses standardised recipes so every test is repeatable:

- **Test profiles** have known fake ICCIDs like `89019990001234567893` : every tester knows what's inside
- **Test certificates** create a parallel PKI (public key infrastructure) completely separate from the real GSMA
- **Constants and variables** like `#MATCHING_ID_1` and `<EUICC_CHALLENGE>` let test scripts refer to values without hard-coding them

---

Integrated eUICCs: chips buried deep inside phone processors with no exposed metal contacts: use a special **USB CCID test interface** that makes the chip pretend to be a smart card reader! It's like a secret test hatch built into the chip just for the testing lab.

---

*Kid-friendly version of GSMA SGP.23, Section 3 and Annexes A, E, F, G, J*

← [Back to Kids Articles](index)
