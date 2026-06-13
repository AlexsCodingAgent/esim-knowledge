---
description: "The physical test setup for eUICC chips: card readers, USB probes, five simulators, and a two-channel system that keeps profile management commands separate from normal phone operation."
title: "The Chip Test Lab: Readers, Probes, and Poking Tools"
date: 2026-06-07
---

# The Chip Test Lab: Readers, Probes, and Poking Tools 🔬🔌

## Imagine...

You're testing a tiny computer chip the size of a grain of rice. You can't plug a keyboard into it. You can't connect a monitor. All you have are five tiny metal contact pads: and a very precise testing machine that sends electrical signals and measures the responses.

This is the world of **eUICC test architecture** : where special card readers, USB probes, and five different simulator programs work together to poke and prod every corner of the chip.

---

## Two Ways to Connect 🔌

The chip can be tested in two physical forms:

| Test Setup | How It Connects | Used For |
|---|---|---|
| **TE_eUICC** | Metal contacts via a PC/SC card reader | Standard removable chips (like Java Cards) |
| **TE_Integrated eUICC** | USB CCID test cable in "card reader mode" | Chips buried inside phone processors |

For the integrated chips, it's actually clever: the chip pretends to be a smart card reader over USB! The test tool plugs in and talks to it as if it were a card reader with a chip inserted.

---

## The Five Simulators 🤖

Since ONLY the chip is real, five different simulator programs pretend to be everyone else:

| Simulator | Role | What It Sends |
|---|---|---|
| **S_Device** | Phone/modem | ISO 7816-4 APDU commands: the same electrical signals a real phone sends |
| **S_LPAd** | Phone Assistant | ES10 commands wrapped in STORE DATA envelopes, sent on a special channel |
| **S_SM-DP+** | Key Maker | Bound Profile Packages, certificate chains, authentication challenges |
| **S_SM-DS** | Post Office | Event records for discovery testing |
| **S_MNO** | Mobile company | Over-the-air commands for ES6 testing |

---

## The Secret Channel System 🚪

The chip uses a clever two-channel system, like a hotel with a front desk and a VIP entrance:

- **Basic Logical Channel** : For normal phone commands: "Hello, are you there?", "What are your capabilities?", "Reset yourself"
- **Dedicated Logical Channel** : Opened by the LPA simulator specifically for ES10 profile commands: "Get profiles list!", "Download this key!", "Enable that profile!"

This separation means the profile management commands can't accidentally interfere with normal phone operation: and vice versa.

---

## How a Test Actually Runs ⚙️

Every test case follows the same recipe:

1. **Set initial conditions** : The chip must start in a known state (certain profiles loaded, certain certificates present, certain mode enabled)
2. **Follow the numbered steps** : Each step says exactly who sends what command and what response to expect
3. **Check the results** : Every response must match the expected data, down to the status word (`SW=0x9000` means success!)

The test scripts use a three-tier notation system:

- `#CONSTANTS` : Fixed values like `#ISD_R_AID` (the chip manager's ID)
- `<VARIABLES>` : Dynamic values like `<EUICC_CHALLENGE>` (a fresh random number)
- `#IUT_SETTINGS` : Vendor-specific details like `#IUT_MEP_LSI_OPTIONS`

---

## The Known Starting State 📍

Before testing begins, the chip must arrive in a carefully prepared state:

- Test certificates and keys are pre-loaded (NOT real GSMA certificates!)
- PROFILE_OPERATIONAL1 is installed (usually disabled)
- The Rules Authorisation Table is configured for the right mode
- A clean-up procedure can reset everything between test runs

This means every test starts from the same known point: like resetting a video game to level 1 before each new player tries.

---

For MEP (Multiple Enabled Profiles) testing, the Device Simulator has to support two different ways of telling the chip "now talk on this line" : either through MANAGE LSI commands or through a special byte in the T=1 protocol. The chip maker declares which method their chip uses, and the test adapts!

---

*Kid-friendly version of GSMA SGP.23-1, Section 3, Annexes A, E, F, G, J*

← [Back to Kids Articles](index)
