---
title: "Turning Missions On and Off: The Robot's Remote Control"
date: 2026-06-07
---

# Turning Missions On and Off: The Robot's Remote Control

What if you had to manage a power grid where every substation is sealed, unmanned, and 500 kilometers from the nearest technician? You can't flip a breaker by hand. You need to switch power sources, disable failing lines, and bring backups online, all from a control room, all over the air.

That's exactly what SGP.02's **Profile Lifecycle** commands do for robots. Profiles are your power sources, and the Commander is your remote control room. Here's how you flip the switches.

---

## Many roads to the same command

The order to enable, disable, or delete a profile can arrive from three directions. Same destination, different starting points:

- **Direct line.** Fleet Owner calls the Commander directly (ES4 interface). Quickest path, but requires a direct relationship with the Commander.
- **Through the Key Factory.** Fleet Owner → Key Factory → Commander (ES2 → ES3 → ES5). The path for operators who work through a provisioning partner.
- **Fleet Manager override.** A third-party fleet manager with the Operator's permission calls the Commander (ES4 with PLMA). For when you've outsourced fleet management.

All three roads converge on the same endpoint: the Commander radios the robot, and the robot acts.

---

## Enable: throwing the switch

The Operator says "Network B, now." Here's the sequence:

1. Commander radios the robot: "Enable the Network B profile."
2. The robot's command module (ISD-R) checks the **POL1 rulebook** on the *current* active profile. Does it allow being disabled?
3. If yes: disable Network A, enable Network B.
4. The robot fires a REFRESH (a quick reboot) and attaches to Network B.
5. Confirmation pings back to the Commander: "Done. On Network B."

**Only one profile can be active at a time.** Enabling B automatically drops A. Think of it like a transfer switch, you can't have two power sources feeding the same circuit simultaneously.

---

## The automatic fallback

What if Network B is a dead end? Maybe the robot's in a coverage hole for that operator.

The robot doesn't just sit there stranded. It detects the failure and:

1. **Rolls back** to Network A: the previously active profile
2. Fires a REFRESH to re-attach
3. Reports the rollback to the Commander: "Network B failed. Back on A."
4. If Network A *also* fails → the **Fall-Back Mechanism** kicks in (that's article 8)

This rollback is automatic and non-negotiable. Without it, a single bad switch could permanently brick a remote device, SGP.02's seatbelt.

---

## Disable: standing down

Disabling a profile parks it. It stays on the chip (keys, apps, everything) but it can't be selected. When you send a disable command:

- The profile goes inactive
- **The Fall-Back Profile automatically engages** : the robot must maintain connectivity at all times
- If POL1 says "delete me when disabled," the robot destroys the profile on the spot
- If POL2 says the same, the Commander orders deletion after receiving the notification

---

## Delete: permanent removal

Deleting a profile is forever. The ISD-P vault and everything inside it, gone:

1. Profile must already be disabled. Can't delete the active one.
2. Commander radios: "Delete Network B."
3. Robot checks POL1: "Does this profile permit deletion?"
4. If yes: ISD-P destroyed. Keys, apps, files, everything wiped.
5. Commander updates the EIS database to reflect the change.

---

## The nuclear option: Master Delete

What if an operator goes out of business, leaves a profile locked on your robot, and nobody has the authority to remove it through normal channels?

Enter **Master Delete**:

- Requires a special one-time **Delete Token** issued by the Key Factory
- The token is verified by the profile vault itself, not just the Commander's office
- **Bypasses all POL1 and POL2 rules.** The rulebook doesn't matter here.
- Cannot target the Fall-Back Profile: the safety net is off-limits, always

Think of Master Delete as the fire axe behind glass. You hope you never need it, but it's there for genuine emergencies.

---

## The life of a profile, in states

```
[Room Created] → SELECTABLE (empty vault)
                       ↓
                  PERSONALIZED (keys present, profile loaded)
                       ↓
                    DISABLED ←──────────┐
                       ↓                  │
                    ENABLED ──disable────┘
                       ↓
                   [DELETED]
```

Every profile on every SGP.02 robot traces this path. Some loop between DISABLED and ENABLED for years. Others go straight to DELETED after a single tour of duty.

---

## The timer that saves you

Every lifecycle command carries a **Validity Period** : a countdown timer set by the Commander. If the robot's confirmation doesn't arrive before the timer runs out, the Commander treats the operation as failed. The robot rolls back to its previous state.

Why? Because without this timeout, a temporarily unreachable robot would leave the system hanging indefinitely, waiting for a confirmation that might never come. The timer is SGP.02's way of saying: *"We gave it a fair shot. Moving on."*

---

*Kid-friendly version of GSMA SGP.02 v4.2 §3.2–3.7, §3.10, Profile Lifecycle Management*

← [Back to Kids Articles](index)
