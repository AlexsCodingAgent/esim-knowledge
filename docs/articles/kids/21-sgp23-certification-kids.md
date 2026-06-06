---
title: "Getting the Gold Star: The GSMA Stamp of Approval"
date: 2026-06-07
---

# Getting the Gold Star: The GSMA Stamp of Approval ⭐🏆

## Imagine...

You've built something amazing: maybe a new bicycle helmet, a toy for toddlers, or a kitchen gadget. Before you can sell it in stores, an independent testing lab has to verify that it's safe, it works as advertised, and it won't break on day one. When you pass, you get a certification mark: a little symbol that tells customers *"This product has been checked. You can trust it."*

In the eSIM world, that certification mark is called a **DLOA** : a Digital Letter of Approval. And getting one is a journey.

---

## The Five-Stage Journey 🗺️

| Stage | What Happens | Real-Life Analogy |
|---|---|---|
| 1. Get Ready | Implement the spec, fill out capability forms | Preparing your car for the safety test |
| 2. Attend the Test Event | Bring your product to an official GSMA testing session | Driving to the testing facility |
| 3. Run the Tests | Execute all applicable test cases | The crash-test dummies go to work |
| 4. Get Reviewed | Results are checked, failures get fixed and retested | The inspector reviews the report |
| 5. Receive the DLOA | The Digital Letter of Approval is issued | You get the gold star sticker! |

---

## The GSMA Certification Ecosystem 🌐

Four different organisations work together:

- **GSMA** : Writes the rules (SGP.23) and organises the Test Events
- **Test Tool Providers** : Build the simulators and test harnesses
- **Test Laboratories** : Run the tests and produce the reports
- **GlobalPlatform** : Issues the actual DLOA certificate

---

## What Each Component Gets Certified For 🏅

Every piece of the eSIM puzzle can earn its own certification:

- **eUICC Chip** : "I correctly handle every interface command, I verify certificates properly, and I carry a valid SAS accreditation number from my factory"
- **LPA / Device** : "My phone's assistant correctly finds, downloads, and manages profiles"
- **SM-DP+ Server** : "My Key Maker correctly takes orders, builds keys, and delivers them securely"
- **SM-DS Server** : "My Post Office correctly registers, stores, and delivers event notifications"

---

## The SAS Accreditation Number 🏭

Every eUICC chip destined for real phones must carry a **SAS Accreditation Number** : proof that the factory where it was made has passed a GSMA security audit. This matters because:

- A secure chip made in a non-secure factory is NOT a secure chip
- SAS-UP (the audit programme) checks physical security, key handling procedures, and access controls
- The test cases actually verify this number is present in the chip's response: linking the tested chip back to its certified birthplace

It's like a signed certificate hanging on the factory wall, and every chip carries a reference to it.

---

## The DLOA: Your Portable Proof 📜

The Digital Letter of Approval is:

- **Digital** : It's a machine-verifiable certificate, not a paper document
- **Portable** : You can show it to any mobile operator anywhere in the world
- **Specific** : It lists exactly which SGP.22 version was tested, which optional features are supported, and which test lab verified it
- **Managed** : It lives on a DLOA Registrar (a secure database) with a discovery URL

When a mobile operator says "prove your chip is certified," you point them to your DLOA.

---

## What's NOT Tested (Yet) ⏳

SGP.23 is honest about its limits:

- **End-to-end testing** : Testing ALL components together at once (chip + server + phone + post office) is marked "For Future Study"
- **Provisioning profiles** : Test profiles for factory bootstrap are out of scope (only normal operational profiles are tested)
- **Cellular-only devices** : Devices that can only connect via mobile networks (no Wi-Fi) aren't yet covered

---

SGP.23 supports testing against SGP.22 versions v2.2 through v2.6: and the Applicability Table has version-specific columns so a product certifying against v2.3 is only tested against v2.3 test cases. It's like having different driving tests for cars, trucks, and motorcycles: each gets tested against what's relevant!

---

*Kid-friendly version of GSMA SGP.23, Sections 1-3, Annex F, GlobalPlatform DLOA specification*

← [Back to Kids Articles](index)
