---
title: "The 32-Digit Fingerprint: Every Chip's Secret Name"
date: 2026-06-07
---

# The 32-Digit Fingerprint: Every Chip's Secret Name 🔢🆔

## Imagine...

Every dollar bill in your wallet has a unique serial number. No two bills share the same one. If you could look up that number, you'd know exactly which printing press made it and when. That's what the **EID** is for eSIM chips — a 32-digit fingerprint for every eSIM chip, like a serial number on a dollar bill.

The **EID** (eUICC Identifier) is a globally unique 32-digit number burned into every eSIM chip on the planet. It's the chip's secret name — and SGP.29 is the rulebook that says how these names are created, who hands them out, and how they stay unique.

---

## Why Did EIDs Need Their Own Rulebook? 📖

Before SGP.29, EIDs were a bit of a mess. They used a system designed for credit-card-style SIM cards (called ICCID), managed by different national authorities with different rules. Three big problems:

| Problem | What Went Wrong |
|---|---|
| **Wrong tool for the job** | EIDs identify chips, not payment accounts — forcing them into a billing-number system was a mismatch |
| **Too many bosses** | Different countries had different rules. Some manufacturers couldn't get EIDs at all! |
| **No central referee** | Without one authority, nobody could guarantee names were truly unique worldwide |

In 2019, the eSIM industry said: "Enough!" They asked the GSMA (the global mobile industry association) to become the central librarian for all EIDs. SGP.29 v1.0 was born on 31 July 2020.

---

## What the EID Is (and What It Definitely Isn't) 🎯

SGP.29 sets six golden rules for EIDs. Here are the most important ones:

| Rule | Meaning |
|---|---|
| **EID.P02** | An EID's one job: uniquely identify one eSIM chip — period |
| **EID.P03** | The EID is NOT a payment account number — you can't charge money to it! |
| **EID.P04** | The EID is NOT for billing phone calls |
| **EID.P05** | EID assignment is completely separate from old SIM card numbering |
| **EID.P06** | EIDs don't have to start with "89" (unlike old SIM cards) |

This is crucial: the EID says "I am Chip #12345..." — it does NOT say "I belong to Alex" or "charge this account." The EID identifies hardware, not people.

---

## The EID at Work: Where You'd Spot It 🔍

The EID isn't just a label — it's used actively throughout the eSIM world:

| Where It's Used | What the EID Does |
|---|---|
| **SM-DS (Discovery Service)** | Matches waiting profiles to the right chip — "Is there a key for EID 12345...?" |
| **ES11 Polling** | The helper app asks: "Any pending downloads for my EID?" |
| **ES8+ Profile Download** | The Key Maker locks the profile to one specific EID so nobody else can use it |
| **Event Registration** | Subscribes a specific chip to notifications: "Tell EID 12345... when its key is ready" |

Without a globally unique EID, the eSIM Key Maker couldn't tell your chip apart from anyone else's!

---

## The GSMA: Head Librarian 📚

SGP.29 puts the GSMA in charge as the **First Level EIN Assignment Authority**. Think of them as the head librarian who hands out blocks of book ISBNs:

- They assign **ERHI1** (EID Range Holder Identifier Level 1) to manufacturers, device makers, and national authorities
- They keep a master registry of every ERHI1 ever assigned
- They run yearly audits to make sure everything is in order
- Cancelled ERHI1s are **never reassigned** — that number is retired forever

But don't worry — EIDs issued under the old system still work! SGP.29 creates a new, cleaner path forward without breaking anything that already exists.

---

## 🧠 Did You Know?

There are enough possible 32-digit EIDs to give a unique name to every grain of sand on Earth — billions of times over! The numbering space is deliberately enormous so we'll never, ever run out.

---

*Kid-friendly version of GSMA SGP.29 v1.1 — EID Definition and Assignment Process*

← [Back to Kids Articles](index)
