---
title: "Turning Missions On and Off: The Robot's Remote Control"
date: 2026-06-07
---

# Turning Missions On and Off: The Robot's Remote Control 🕹️

## Imagine...

Robot #8721 has three profiles loaded: Network A (active), Network B (standby), and a Fall-Back profile (emergency backup). The Fleet Owner wants to switch from Network A to Network B — but the robot is sealed in a basement 500 miles away. No buttons. No screen. No human.

SGP.02's **Profile Lifecycle** commands let the Operator flip profiles on and off remotely, using the Commander's radio channel. But there are rules...

---

## Three Paths to Every Command 🛤️

The same command — enable, disable, or delete — can arrive three different ways:

| Path | Who Calls | Interface | Example |
|---|---|---|---|
| **Direct** | Fleet Owner → Commander | ES4 | Operator with direct SM-SR relationship |
| **Relay** | Fleet Owner → Key Factory → Commander | ES2→ES3→ES5 | Operator who works through SM-DP |
| **Fleet Manager** | M2M SP → Commander | ES4 with PLMA | Fleet manager with Operator permission |

All three paths converge at the same place: the Commander radios the robot with the command.

---

## Enable: Switching Networks 🔛

When the Operator says "switch to Network B":

1. Commander radios: "Enable Network B profile!"
2. Robot's Commander Office (ISD-R) checks the **rulebook (POL1)** on the current profile — does it allow being disabled?
3. If yes: disable Network A → enable Network B
4. Robot sends a REFRESH — like a reboot — and attaches to Network B
5. Robot reports back to Commander: "Done!"

**Only one profile can be enabled at a time.** Enabling B automatically disables A.

---

## The Roll-Back Safety Net 🪂

What if Network B doesn't work? Maybe the robot is in a dead zone for that operator.

The robot detects: "I can't connect!" Then it automatically:

1. **Rolls back** to Network A (the previously enabled profile)
2. Sends a REFRESH to re-attach
3. Reports the roll-back to the Commander
4. If Network A *also* fails → activates the **Fall-Back Mechanism** (see Article 8)

This automatic roll-back is critical — without it, a failed switch could permanently disconnect a robot!

---

## Disable: Standing Down ⏸️

Disabling a profile makes it inactive but keeps it on the chip. When you disable:

- The profile becomes unselectable
- **The Fall-Back Profile automatically kicks in** — the robot must always have connectivity
- If POL1 says "delete me when disabled," the robot destroys the profile after disabling
- If POL2 says the same thing, the Commander orders deletion after notification

---

## Delete: Permanent Removal 🗑️

Deleting a profile is forever. The ISD-P and everything inside it vanishes:

1. Profile must be disabled first — you can't delete the active profile
2. Commander radios: "Delete Network B"
3. Robot checks POL1: "Does this profile allow deletion?"
4. If yes: ISD-P is destroyed — keys, apps, files, everything gone
5. Commander updates the EIS database

---

## The Master Delete: Emergency Override 🔨

What if an Operator goes bankrupt and their profile is "locked" on your robot? Enter **Master Delete**:

- Uses a special one-time **Delete Token** from the Key Factory
- The token is verified by the profile room itself (not just the Commander's Office)
- **Bypasses all POL1 and POL2 rules**
- Cannot target the Fall-Back Profile — the safety net is sacred

---

## Lifecycle States at a Glance

```
[Profile Room Created] → SELECTABLE (empty)
                              ↓
                         PERSONALIZED (has keys, no profile)
                              ↓
                           DISABLED ←──────────┐
                              ↓                  │
                           ENABLED ───disable───┘
                              ↓
                          [DELETED]
```

---

## 🧠 Did You Know?

The Commander sets a **Validity Period** timer on every command. If the robot's confirmation doesn't arrive before the timer expires, the Commander treats it as a failure — and the robot rolls back. This prevents the system from hanging forever if a robot is temporarily unreachable.

---

*Kid-friendly version of GSMA SGP.02 v4.2 §3.2–3.7, §3.10 — Profile Lifecycle Management*

← [Back to Kids Articles](index)
