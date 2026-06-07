---
description: "A tour through SGP.33-3's actual test cases — sending profile orders to robots, managing fleet membership, handling errors, and verifying that Mission Control talks to every helper correctly."
title: "What They Test: Sending Orders, Getting Reports, Setting Up"
date: 2026-06-07
---

# What They Test: Sending Orders, Getting Reports, Setting Up 📋

## Imagine...

You're training to be Mission Control for a robot fleet. Before you get the real job, you have to prove you can:

- Send the right orders to the right robots
- Switch their network connections on and off
- Get status reports back from every robot
- Handle errors without panicking
- Set up new robots when they join the fleet

SGP.33-3 has test cases for **all of these**. Let's look at what they actually test.

---

## Profile Commands: The Five Basic Orders 📡

The eIM sends special packages called **eUICC Packages** to each robot's vault. Inside are Profile State Management Operations (PSMO for short):

| Order | What It Does | Real-Life Analogy |
|-------|-------------|-------------------|
| **Enable** | Turn on a mobile profile | "Switch to Plan B now!" |
| **Disable** | Turn off a mobile profile | "Stop using Plan A." |
| **Delete** | Remove a profile forever | "Throw away the old plan." |
| **ListProfileInfo** | Ask what profiles exist | "Show me all your plans." |
| **GetRat** | Check what's allowed | "Show me the rulebook." |

The **GetRat** command is especially important: it retrieves the Rules Authorisation Table (RAT), which tells Mission Control what operations are permitted. You wouldn't want to try enabling a profile that the rules say must stay disabled!

---

## Setting Up and Managing the Fleet 🏗️

Beyond day-to-day commands, the eIM also manages its relationship with each robot through **eIM Configuration Operations**:

| Operation | What It Does | When It's Used |
|-----------|-------------|----------------|
| **AddEim** | Register Mission Control with a robot | "Hello robot, I'm your new commander!" |
| **UpdateEim** | Rotate security keys and counters | "Here's my new ID badge." |
| **DeleteEim** | Remove Mission Control's access | "I'm no longer your commander." |
| **ListEim** | Ask who's registered as commander | "Who else can give you orders?" |

Think of this like a security guard's keycard system. A new guard gets a card (AddEim). Every few months they get a new card with updated codes (UpdateEim). When they leave, their card is deactivated (DeleteEim).

---

## Talking to Key Makers and Post Offices 🏭📮

The eIM doesn't work alone. Test cases also check how it talks to other services:

### ES9+' Tests (Talking to the Key Maker)

- **InitiateAuthentication** : "Let me prove I'm legit."
- **GetBoundProfilePackage** : "Send me that digital key!"
- **AuthenticateClient** : "Here's the robot's ID for you to verify."
- **HandleNotification** : "The robot says the profile is installed."
- **CancelSession** : "Abort! Something went wrong."
- **HTTPS** : "Is our encrypted tunnel working?"

### ES11' Tests (Checking the Post Office)

- **InitiateAuthentication** : Prove identity to the message service
- **AuthenticateClient** : Verify with robot credentials
- **HTTPS** : Encrypted connection check

---

## The Only Full Behaviour Test (So Far) 🧪

As of the current version, only one end-to-end behaviour test is fully defined: **Profile Enable via eIM Package Retrieval**. Here's the flow:

1. The robot's translator (IPA) connects securely to Mission Control
2. The translator asks: "Any orders for me?"
3. Mission Control responds: "Yes: enable Profile X!"
4. The translator delivers the result: "Done! Here's proof."
5. Mission Control tells the Key Maker: "The profile is active now."

Four different sequences test variations: with different notification methods and with/without previously enabled profiles. If Mission Control gets any step wrong, the test fails.

---

## What's Still "For Future Study" 🔮

Not everything is testable yet! Many test sequences are marked **FFS** (For Future Study):

- Most ESep PSMO test sequences (Enable, Disable, Delete, ListProfileInfo)
- All eIM Configuration test sequences (AddEim, UpdateEim, DeleteEim, ListEim)
- All 11 ESipa interface test sequences
- Additional behaviour tests (Disable, Delete, error recovery)

The IoT testing world is still growing: like a new video game getting expansion packs. Each new version of SGP.33-3 fills in more of the FFS gaps.

---

The extensive error case testing is just as important as the happy-path testing. For **AuthenticateClient** alone, there are **18 error test cases** : testing what happens with expired certificates, wrong signatures, missing memory, unknown IDs, and more. Mission Control must handle *every* curveball!

---

*Kid-friendly version of GSMA SGP.33-3: eUICC IoT Manager Test Specification, Test Cases*

← [Back to Kids Articles](index)
