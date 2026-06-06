---
title: "Emergency Plans: Built-In Backup for the Unreachable"
date: 2026-06-07
---

# Emergency Plans: Built-In Backup for the Unreachable 🆘

You're driving through a mountain pass. Your car loses signal: the nearest tower just went down after a rockfall. Then you crash. Nobody's around.

The car needs to call 112. Right now. But there's no network.

**This isn't hypothetical.** The GSMA designed SGP.02 for exactly this scenario, and it has three different backup plans built into the chip itself. Not "we'll add one later." Not "maybe in a software update." Three plans, burned in at the factory, ready to go.

Let's walk through them.

---

## Plan A: The Parachute (Fall-Back)

Every profile on a chip can be tagged with a **Fall-Back Attribute** : a second subscription that just sits there, disabled, waiting.

Think of it like a spare tire. You hope you never need it. But if you get a flat in the middle of nowhere? You're *very* glad it's there.

**How it kicks in:**

The chip itself detects the outage (no Commander, no Fleet Owner, no human. It just *knows* it lost contact with the network. Then it does something bold: it **rips up the rulebook temporarily** (overrides POL1) this is an emergency), disables the dead profile, fires up the Fall-Back, and reconnects.

Only *after* all that does it send a message: "Hey Commander, heads up. I switched to the backup."

**The fine print that keeps it safe:**

- Only one Fall-Back at a time: no confusion about which spare to use
- Must be on a *different* operator, if one network is down, the backup shouldn't be the same one
- Can't double as the Emergency Profile, they serve different purposes
- POL1's "delete when disabled" rule gets ignored for Fall-Back, you don't throw away your own safety net
- Master Delete can't touch it: the ultimate safety net is sacred

---

## Plan B: The Red Phone (Emergency Profile)

This one's different. It's not about getting back online, it's about making *one specific type of call* when lives are on the line.

The Emergency Profile activates for emergency services only: no commercial data, no cat videos, just the call to 112 (or 911, or 999 depending on where you are). It's legally mandated for connected cars with **eCall** systems.

Here's how it differs from Fall-Back:

| | Fall-Back (spare tire) | Emergency (red phone) |
|---|---|---|
| **Goal** | Get back to normal service | Make emergency calls only |
| **Trigger** | Automatic, chip detects outage | Local sensor (e.g., crash impact) |
| **Who pays?** | Commercial subscription | Emergency access: no billing |
| **Who activates it?** | The chip itself | The *Device* : the car's crash computer |
| **Can both exist?** | On different profiles | Mutually exclusive, only one can hold each attribute |

The activation path is direct and deliberate: the car's crash sensor calls the **ESx** local interface directly, bypassing the Commander altogether. It says "Enable Emergency Profile, NOW." The eUICC overrides POL1 and switches. No waiting. No confirmation. No network needed.

---

## Plan C: The Sandbox (Test Profile)

When a chip is being manufactured or field-tested, you don't want it burning a real, paid subscription. You need a sandbox.

The Test Profile connects to a **test network** : not live production, using known test keys so engineers can debug without risk. Activate it locally via the same ESx interface used for emergencies, no Commander involved.

When testing's done, the Device says "switch back," and the chip returns to its previous profile. Clean, fast, offline.

---

## The Local Panel (ESx) : No Signal Required

The ESx interface is the common thread between Plans B and C. It's the **only** way to manage profiles without going through the Commander: a direct wire from the Device to the chip:

- `LocalEnableTestProfile` : "Enter sandbox mode"
- `LocalDisableTestProfile` : "Return to reality"
- `LocalEnableEmergencyProfile` : "LIFE AT STAKE, switch now"
- `LocalDisableEmergencyProfile` : "Crisis over, go back"

ESx ignores POL1 completely, when someone's life is on the line, the rulebook takes a back seat. But it won't override an active Emergency Profile with a Test Profile. Emergencies outrank testing, always.

---

## How They Dance Together

```
Network A is active
        │
        ▼
  Network A fails!
        │
   ┌────┴────┐
   ▼         ▼
Roll Back   Fall-Back
(try prev   (switch to
 profile)    backup)
   │         │
   └────┬────┘
        │
  Still no connection?
        │
        ▼
  Fall-Back activates
  (if not already live)
```

One critical rule: **Fall-Back never activates when Emergency or Test is running.** A human (or crash sensor) choosing "call 112" takes priority over the chip's automatic recovery logic.

---

The Fall-Back Mechanism is fully autonomous. The chip detects the outage, switches profiles, and reconnects all by itself: the Commander only finds out *afterward* when the notification arrives. A chip can save itself during a total network blackout, as long as the Fall-Back network still has signal. It's not a feature that gets bolted on later. It's baked into the silicon.

---

*Kid-friendly version of GSMA SGP.02 v4.2 §3.16, §3.22–3.31, Resilience*

← [Back to Kids Articles](index)
