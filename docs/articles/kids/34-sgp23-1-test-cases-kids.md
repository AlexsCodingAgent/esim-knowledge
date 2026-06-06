---
title: "What They Test: Room Manager, Key Storage, and Key Lifecycle"
date: 2026-06-07
---

# What They Test: Room Manager, Key Storage, and Key Lifecycle 🗂️🔑

## Imagine...

Your vault has a manager — a tiny computer programme that decides who can enter, which room a new key goes into, and what to do when a key is no longer needed. The manager also keeps a list of every key, knows which one is currently in use, and enforces the rules: "You can't throw away a key while it's still in the door!"

SGP.23-1 tests this manager inside and out. It checks the ISD-R (the vault's security director), the ECASD (the vault's identity vault), and every stage of a profile's life — from birth to death.

---

## The First Handshake: ISD-R Selection 🤝

Before anything else can happen, the LPA must find and talk to the chip's **ISD-R** — the Issuer Security Domain Root. It's like finding the building manager's office:

| Test Scenario | What It Checks |
|---|---|
| Basic power-on (ATR) | The chip wakes up, sends its "Hello, I'm a chip!" bytes |
| Select ISD-R | The chip responds with its manager's ID and capabilities |
| With enabled profile | The manager's response changes when a profile is active |
| LPAe support | The chip advertises if it has a built-in assistant |
| MEP-A1, MEP-A2, MEP-B | Multiple-profile modes are correctly declared |

9 test sequences verify this first handshake — because if the manager can't be found, nothing else works.

---

## The Secure Delivery: ES8+ Channel 🔒

ES8+ is how profiles arrive through an encrypted tunnel. Four test groups verify it:

| Test Group | What It Verifies | Edge Cases |
|---|---|---|
| **InitialiseSecureChannel** | The encrypted pipe is built correctly | Wrong signatures, double initiation, invalid parameters are ALL rejected |
| **ConfigureISDP** | A new locked room is created inside the vault | Correct security domain parameters |
| **StoreMetadata** | The room's label is written (carrier name, rules, notification addresses) | 11+ sequences including enterprise profiles, RPM metadata, device change info |
| **LoadProfileElements** | The actual key data arrives in chunks | 12 sequences across three encryption curves plus error cases |

---

## The Download Pipeline: ES10b ⬇️

12 function groups test the complete download chain:

- **PrepareDownload** — Four test groups (one per encryption curve + errors). The chip generates a fresh one-time key pair each time.
- **GetEUICCChallenge / GetEUICCInfo** — The chip produces fresh random challenges (no repeats!) and reports its capabilities, including the crucial `sasAcreditationNumber`
- **AuthenticateServer** — 51 pages of testing! The chip must validate the Key Maker's certificate chain AND reject wrong, expired, or mis-signed certificates
- **LoadBoundProfilePackage** — The encrypted key is delivered. The chip decrypts it and installs the profile — the LPA never sees the contents
- **Notification Management** — Three functions track what happened: list pending notifications, get details, remove acknowledged ones

---

## The Keychain Manager: ES10c 👆

The most heavily tested interface — EnableProfile alone spans 117 pages!

| Function | Pages of Tests | Why So Heavy |
|---|---|---|
| GetProfilesInfo | Moderate | Must correctly list all profiles with states, nicknames, and policy rules |
| EnableProfile | ~117 pages | Normal enable, MEP variants, errors, refresh flags, catBusy handling |
| DisableProfile | ~106 pages | Normal disable, MEP variants, "can't disable the only profile if rules forbid it" |
| DeleteProfile | Moderate | Must verify profile is gone after deletion, enforce policy rules |
| eUICCMemoryReset | Moderate | Complete factory wipe — nothing left behind |

---

## Beyond the Interface: Behaviour Testing 🧪

Section 5 goes beyond individual commands to test real-world behaviour:

- **Retry mechanisms** — If a download fails, can the chip reuse its key pair and try again?
- **Forbidden PPRs** — Does the chip refuse operations that the profile's policy rules forbid?
- **File structure** — Is the chip's internal file system (EF_UST, EF_DIR, EF_ICCID) correctly organised?
- **State transitions** — Does enabling Profile A correctly disable Profile B? Are notifications generated?

---

## 🧠 Did You Know?

The AuthenticateServer test case alone takes up ~51 pages in the specification — making it one of the most extensively specified groups. This is because certificate validation is the security foundation: if the chip accepts a fake certificate, an attacker could deliver a malicious profile!

---

*Kid-friendly version of GSMA SGP.23-1, Sections 4.2 and 5.2*

← [Back to Kids Articles](index)
