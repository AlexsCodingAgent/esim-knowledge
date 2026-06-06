---
title: "Testing the Magic Vault Itself"
date: 2026-06-07
---

# Testing the Magic Vault Itself 🔒🧪

## Imagine...

You buy a safe to protect your valuables. But before you trust it with your passport and jewellery, you want to know: Can someone pick the lock? Will it survive a drill attack? Does the combination mechanism work every single time: even after a thousand uses?

You're not testing the keys. You're not testing the person who delivers the keys. You're testing **the vault itself** : the box, the lock, the hinges.

That's what **SGP.23-1** does for eSIMs. It's the 797-page test bible that asks one question and one question only: *Does this eUICC chip work correctly?*

---

## One Question, One Target 🎯

SGP.23-1 is different from the regular SGP.23 testing. Here's how:

| Aspect | SGP.23 (System Testing) | SGP.23-1 (Chip-Only Testing) |
|---|---|---|
| What's tested | Four components at once | ONLY the eUICC chip |
| Everything else | Mixed: some real, some simulated | EVERYTHING else is simulated |
| Target spec | SGP.22 V2.x (consumer phones) | SGP.22 V3.1 (M2M/IoT) |
| Simulators needed | 9 different types | 5 types |
| Length | 913 pages | 797 pages |

The original SGP.23 tested everything together: chips, servers, phones, post offices. But in 2018, the GSMA realised the chip's testing was so massive it needed its own book. So they split SGP.23 into three: SGP.23-1 (the chip), SGP.23-2 (the Key Maker), and SGP.23-3 (the Post Office and Phone Assistant).

---

## Every Interface, Every Command 🔌

The chip is tested across five different interfaces:

| Interface | Connects To | What Gets Verified |
|---|---|---|
| ES6 | Mobile company → Chip | Over-the-air metadata updates |
| ES8+ | Key Maker → Chip | The encrypted delivery tube for profiles |
| ES10a | Assistant → Chip | Finding discovery addresses |
| ES10b | Assistant → Chip | The complete profile download pipeline |
| ES10c | Assistant → Chip | Managing profiles: enable, disable, delete |

---

## The Optional Features Table 📋

Not every chip supports every feature. A chip in a smartwatch might need different things than a chip in a car. So SGP.23-1 has a brilliant system: **30+ optional feature checkboxes** that the chip maker fills out:

| Feature | What It Means |
|---|---|
| O_E_NIST | Supports NIST P-256 encryption curve |
| O_E_BRP | Supports BrainpoolP256r1 curve |
| O_E_MEP | Supports Multiple Enabled Profiles |
| O_E_RPM | Supports Remote Profile Management |
| O_E_ENTERPRISE | Supports Enterprise (work) profiles |
| O_E_INTEGRATED | Chip is buried inside a processor, not a removable card |

Each checkbox decides which test cases apply. A chip supporting only basic features gets a smaller test suite; a chip packed with every feature gets everything.

---

## From Test to Trust 🤝

SGP.23-1 feeds into a bigger chain of trust:

1. **SAS-UP** : The factory audit that checks how chips are made
2. **SGP.23-1** : Proves this specific chip design works correctly
3. **SGP.23** : The certified chip becomes a "known-good" component for full system testing
4. **DLOA** : The final Digital Letter of Approval

Every production eUICC carries its `sasAcreditationNumber` inside its `EUICCInfo2` structure: and SGP.23-1 test cases verify it's there!

---

SGP.23-1 has been evolving for over 6 years: from v2.0 in April 2018 through v3.1.3 in 2025: with Change Requests coming from real Test Events. Every time a tester found an ambiguity, the specification got clearer. It's a living document shaped by actual testing experience!

---

*Kid-friendly version of GSMA SGP.23-1 v3.1.3: RSP Test Specification for the eUICC*

← [Back to Kids Articles](index)
