---
title: "Handing Over the Fleet: Changing Commanders"
date: 2026-06-07
---

# Handing Over the Fleet: Changing Commanders 🔄

## Imagine...

Your robot fleet has been managed by Commander Alpha for five years. But now you're switching to Commander Beta — maybe Alpha's service is too expensive, or your company merged with another that uses Beta. You have 10,000 robots in the field. You can't physically touch any of them.

SGP.02 has a built-in solution: the **SM-SR Change** procedure. It's a 32-step, four-party protocol that transfers command of an entire robot — all profiles, all state, everything — from one Commander to another. And the robot itself gets the final say.

---

## Why Change Commanders? 🤔

| Reason | Example |
|---|---|
| Better pricing | Beta offers cheaper fleet management |
| Corporate merger | Your company acquires a firm using Beta |
| Service discontinued | Alpha is shutting down in your region |
| Performance issues | Beta has better coverage in your area |
| Vendor independence | You don't want to be locked into one Commander forever |

Without SM-SR Change, you'd need to physically replace every robot's chip. With it, the handover happens over the air.

---

## The Four Players ♟️

| Player | Role |
|---|---|
| **Fleet Owner (Operator)** | Initiates the transfer |
| **Commander Alpha (SM-SR1)** | The old Commander — must cooperate |
| **Commander Beta (SM-SR2)** | The new Commander — must prove identity |
| **The Robot** | The chip itself — holds the ultimate authority |

---

## The Five-Phase Handover 🎬

### Phase 1: Preparation
Fleet Owner asks Beta: "Are you ready to take robot #8721?" Beta checks: enough capacity? Can handle this chip type? Valid badge? Ready!

### Phase 2: Database Transfer
Alpha sends the **EIS** (robot information database) to Beta. This includes the robot's ID card, all profile metadata, current states, and rulebooks. Beta verifies the robot's certificate chain.

### Phase 3: Prove Your Identity
Beta must prove to the **robot itself** — not just to Alpha — that Beta is a legitimate Commander:

1. Beta sends its ID badge to the robot
2. Robot's vault checks: "Does this trace back to the CI? Yes!"
3. Robot generates a fresh random challenge
4. Beta signs the challenge with its private key
5. Robot verifies: "OK, you're a real Commander"

### Phase 4: New Keys for the New Commander
Using the same ECKA-EG magic from Profile Download, Beta and the robot create a brand new key set (KS2) for their future communication. The critical moment: when Beta verifies the receipt at Step 23, **Beta is now the Commander** — even if everything else goes wrong.

### Phase 5: Cleanup and Notify
- Beta opens a channel using the new keys
- Alpha's old keys are deleted from the robot
- Beta updates the EIS to show it's now in charge
- Alpha deletes its copy of the EIS
- All affected Fleet Owners are notified: "Commander Beta now manages this robot!"

---

## The Robot Has the Final Say 🔐

Even though Alpha relays all the messages, the cryptographic proof goes directly between Beta and the robot:

- The robot verifies Beta's badge against the CI root — stored at manufacturing
- Alpha cannot forge Beta's signature
- Alpha cannot block a valid Beta from taking over
- The robot's private key (`SK.ECASD.ECKA`) is the ultimate authority

This means SM-SR Change works even if Alpha is uncooperative (as long as Alpha relays messages).

---

## What Transfers vs What Stays

| Transfers to Beta | Stays with Alpha |
|---|---|
| ✅ Robot ID and certificate | ❌ Old SCP80/SCP81 keys (replaced by KS2) |
| ✅ All profiles and their states | ❌ Billing records |
| ✅ POL2 rulebooks | ❌ Audit logs |
| ✅ Connectivity parameters | ❌ Administrative history |
| ✅ Fall-Back and Emergency attributes | |

---

## 🧠 Did You Know?

The SM-SR Change is SGP.02's answer to **vendor lock-in**. It's the single most important feature that prevents a Commander from holding your robot fleet hostage. The robot was designed from day one to accept a new Commander — it just needs to verify the new Commander's ID badge traces back to the same Passport Office (CI).

---

*Kid-friendly version of GSMA SGP.02 v4.2 §3.8–3.9, §5.6 — SM-SR Change*

← [Back to Kids Articles](index)
