---
title: "Handing Over the Fleet: Changing Commanders"
date: 2026-06-07
---

# Handing Over the Fleet: Changing Commanders

Here's a hard truth about connected devices: if you can't switch providers, you don't own the device: the provider owns you.

This is called **vendor lock-in**, and it's the single biggest threat to any large-scale IoT deployment. SGP.02 has an answer. It's called **SM-SR Change** : a 32-step, four-party protocol that transfers an entire robot from one Commander to another, over the air. No truck rolls. No chip swaps. And the robot itself holds the final vote.

---

## Why you'd switch

Plenty of reasons. None of them should require a hardware replacement:

- **Better pricing** : the new Commander undercuts the old one
- **Merger or acquisition** : your company bought a firm using a different Commander
- **Service shutdown** : the old Commander is leaving your region
- **Coverage** : the new Commander has better reach for your robots' locations
- **Independence** : you simply don't want one company controlling your fleet forever

SM-SR Change makes all of these a radio operation, not a physical one.

---

## Who's at the table

Four parties, each with a specific role:

- **Fleet Owner (Operator)** : initiates the transfer. "I want Commander Beta managing this robot."
- **Commander Alpha (SM-SR1)** : the incumbent. Must relay messages; doesn't have to be happy about it.
- **Commander Beta (SM-SR2)** : the challenger. Must prove to the robot (not just to Alpha) that Beta is a legitimate Commander.
- **The Robot** : the chip itself. The ultimate authority. Nobody takes over without the robot's cryptographic approval.

---

## The handover, step by step

### Phase 1: Preparation

The Fleet Owner asks Beta: "Can you handle robot #8721?" Beta checks its own capacity, chip compatibility, and credentials. If the answer's yes, we proceed.

### Phase 2: Database handoff

Alpha ships the robot's **EIS** (information database) to Beta. This includes the robot's identity certificate, all profile metadata, current states, and rulebooks. Beta verifies the certificate chain, making sure the robot traces back to a legitimate Chip Builder and CI.

At this point, Beta knows everything Alpha knows about the robot. But Beta still can't *command* the robot. For that, Beta needs the robot's permission.

### Phase 3: The robot interviews Beta

This is the cryptographic heart of the whole procedure. Beta must prove its identity directly to the robot, not through Alpha. Alpha relays the messages, yes, but the authentication happens between Beta and the robot:

1. Beta sends its ID badge to the robot (through Alpha's relay)
2. The robot's secure vault traces the badge back to the CI root: the same root burned in at manufacturing
3. The robot generates a **fresh random challenge**
4. Beta signs the challenge with its private key
5. The robot verifies the signature: "You're legitimate. I accept you."

Alpha can't fake Beta's signature. Alpha can't block a valid Beta from passing. The robot decides.

### Phase 4: New keys for a new era

Using the same ECKA-EG key agreement from profile download, Beta and the robot generate a brand-new key set: the **KS2 keys** : for all future communication. The critical moment: when Beta verifies the key receipt, **Beta is now the Commander**. Even if everything else falls apart from this point forward, the transfer is cryptographically complete.

### Phase 5: Cleanup

- Beta opens a channel using the new KS2 keys
- Alpha's old keys are deleted from the robot
- Beta updates the EIS to reflect the new chain of command
- Alpha deletes its copy of the EIS
- All affected Fleet Owners get notified: "Commander Beta now manages this robot"

---

## Why the robot gets the final say

This is the design choice that makes SM-SR Change work even with an uncooperative Alpha:

- The robot verifies Beta's badge against the CI root, stored at manufacturing, unchangeable
- Alpha relays messages but never holds the cryptographic authority
- Alpha cannot forge Beta's signature (mathematically impossible with the key sizes used)
- The robot's private key (`SK.ECASD.ECKA`) is the single source of truth

If Alpha refuses to relay messages, the protocol stalls, but it can't be subverted. A cooperative Alpha is required for the relay, but a cooperative Alpha can't fake or block a legitimate handover.

---

## What moves vs. what stays

| Goes to Beta | Stays with Alpha |
|---|---|
| Robot identity and certificate chain | Old SCP80/SCP81 keys (replaced by KS2) |
| All profiles, states, and configurations | Billing records and audit logs |
| POL2 rulebooks | Administrative history |
| Connectivity parameters | Internal Alpha-only metadata |
| Fall-Back and Emergency attributes | : |

The robot itself doesn't change. It just has a new phone number for Command.

---

## The anti-lock-in guarantee

SM-SR Change is the feature that makes SGP.02 different from proprietary alternatives. The robot was designed from the factory to accept a new Commander, it just needs to verify that the new Commander's credentials trace back to the same Passport Office (the CI). It's vendor independence baked into silicon.

If you're deploying thousands of devices with a 10–15 year lifespan, this matters. A lot.

---

*Kid-friendly version of GSMA SGP.02 v4.2 §3.8–3.9, §5.6, SM-SR Change*

← [Back to Kids Articles](index)
