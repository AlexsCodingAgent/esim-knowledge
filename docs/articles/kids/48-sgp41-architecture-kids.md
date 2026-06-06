---
title: "The Factory Team: Key Makers and Robots"
date: 2026-06-07
---

# The Factory Team: Key Makers and Robots 🤖🔑

## Imagine...

A giant toy factory. At one end, raw plastic and wires go in. At the other end, finished toys roll out, each with batteries already inside and ready to play. Who makes that magic happen? A whole team of specialised workers: and everyone has a very specific job.

SGP.41 introduces three brand new team members to the eSIM factory floor. Let's meet them!

---

## Meet the Factory Team 🦸

### 🔑 The Factory Key Maker (SM-DPf)

The **SM-DPf** (Subscription Manager Data Preparation : *factory*) is the master craftsman. This is the only team member trusted to create, protect, and bind eSIM profiles. Think of it as the vault where secret keys are forged.

The Factory Key Maker does five things:

| Job | What It Means |
|---|---|
| **Profile Generation** | Creates the actual profile (the "key") from scratch |
| **Profile Protection** | Wraps it in unbreakable encryption |
| **Profile Binding** | Locks it to one specific chip so only that chip can use it |
| **Profile Storage** | Keeps finished profiles safe until they're needed |
| **Profile Delivery** | Ships the locked packages to the factory |

The Factory Key Maker must be **SAS-certified** : that's like having a top-security government vault clearance. Its private key lives in a special tamper-proof hardware box (an HSM) that would self-destruct if anyone tried to break in.

---

### 🤖 The Factory Robot (FPA)

The **FPA** (Factory Profile Assistant) is the assembly-line robot with exactly one job: pick up the locked key package, push it into the eSIM chip, and report back whether it worked. That's it!

The FPA is deliberately kept simple. It can be:
- A hardware gadget on the production line
- A tiny piece of software running on the device
- A special "factory mode" version of the normal eSIM helper app

The clever part? The FPA **never sees the actual key**. It only handles locked, encrypted packages. Even if someone tampered with the factory robot, they'd get nothing but scrambled digital noise.

---

### 🏭 The Factory Boss (Device Manufacturer)

The Device Manufacturer (like Samsung, Dell, or Tesla) takes on a bigger role than in normal eSIM. Instead of just assembling devices, they now:

| New Job | What They Do |
|---|---|
| **Key Requesting** | Asks the Factory Key Maker: "I need 10,000 keys for these chips" |
| **Key Storage** | Keeps pre-made keys in a safe warehouse until assembly time |
| **Key Loading** | Tells the Factory Robot: "Load this key into that chip now" |

The best part? The Factory Boss can do all of this **without internet** on the production floor. All the internet stuff (ordering keys, receiving deliveries) happens separately, in the office.

---

### 📦 The Chip Maker (EUM)

The **EUM** (eUICC Manufacturer) is the company that actually makes the eSIM chips. They get a new job in SGP.41: loading **one-time keys** into each chip during manufacturing.

Think of one-time keys like disposable combination locks. Each chip gets a set of them. The Factory Key Maker uses one to lock a profile specifically to that chip. Once used, the lock is destroyed: it can never be opened again by anyone else.

---

## How the Team Talks: The Factory Interfaces 🔌

The team communicates through nine special channels (called "interfaces"). Here are the most important ones:

| Interface | Who's Talking | What They Say |
|---|---|---|
| **ES2f** | Carrier → Key Maker | "Please prepare 10,000 keys for my customers" |
| **Esbpp** | Key Maker → Factory Boss | "Here are your locked key packages" |
| **Esfac** | Factory Boss → Robot | "Load this key into that chip" (inside the factory) |
| **ES10f** | Robot → eSIM Chip | "Here's your key package!" (final delivery) |
| **ES8f** | Key Maker → eSIM Chip | Secret encrypted channel tunnelled through the robot |

The `Esfac` interface (between Factory Boss and Robot) is intentionally left unspecified: every factory can build it however suits their assembly line best. Some use cables, some use wireless, some use a USB stick. SGP.41 doesn't care!

---

The FPA Services on the eSIM chip are only active **during the factory process**. Once the device leaves the production line, those services lock up forever. This means nobody can use the "factory back door" to sneak a malicious key onto your device later!

---

*Kid-friendly version of GSMA SGP.41 v1.0: IFPP Architecture, Sections 2–3*

← [Back to Kids Articles](index)
