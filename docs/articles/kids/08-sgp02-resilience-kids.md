---
title: "Emergency Plans: When Robots Need Backup"
date: 2026-06-07
---

# Emergency Plans: When Robots Need Backup 🆘

## Imagine...

Robot #8721 is running on Network A when suddenly — disaster! Network A's tower goes down in that area. The robot is now disconnected. No human will visit for 10 years. What happens?

SGP.02 has three backup plans built in, each for a different kind of emergency. The robot can save itself without ever calling for help.

---

## Plan A: The Fall-Back Profile 🪂

Every robot can have one profile designated with the **Fall-Back Attribute** — a backup network subscription kept disabled but ready to go.

### How It Activates

1. Robot loses connectivity on the active profile
2. Robot detects: "I can't reach the network!"
3. Robot automatically **overrides all rulebooks (POL1)** — this is an emergency!
4. Disables the current profile
5. Enables the Fall-Back Profile
6. Sends REFRESH, attaches to backup network
7. Reports to the Commander: "I switched to Fall-Back!"

### Smart Rules About Fall-Back

| Rule | Why |
|---|---|
| Only one Fall-Back at a time | No confusion about which backup to use |
| Fall-Back uses a *different* operator | If one network is down, the backup shouldn't be the same one |
| Can't be the same as Emergency Profile | Different purposes — don't mix them |
| POL1 "delete when disabled" IGNORED for Fall-Back | Don't delete your own safety net! |
| Master Delete can't target Fall-Back | The ultimate safety net is sacred |

---

## Plan B: The Emergency Profile 🚨

Some robots have a legal requirement to make emergency calls — even without a commercial subscription. Think of a car's **eCall** system that must dial 112 after a crash.

| Feature | Fall-Back Profile | Emergency Profile |
|---|---|---|
| Purpose | Restore normal connectivity | Make emergency calls only |
| Triggers | Automatic on connectivity loss | Local activation (e.g., crash sensor) |
| Commercial service? | Yes — paid subscription | No — emergency access only |
| Activated by | The robot itself | The Device (car computer, meter CPU) |
| Can coexist? | On different profiles | Mutually exclusive — only one holds each attribute |

**How it works:** The car's crash sensor calls the **ESx** interface directly — bypassing the Commander entirely — and says "Enable Emergency Profile NOW!" The eUICC overrides POL1 and switches.

---

## Plan C: The Test Profile 🧪

During manufacturing or field testing, robots need a profile that:

- Connects to a test network (not live production)
- Uses known test keys (for debugging)
- Can be activated locally without any network interaction
- Won't accidentally consume a paid subscription

Test Profiles are activated via the same **ESx** local interface as Emergency Profiles. The Device tells the chip: "Switch to test mode." When testing is done, the Device says: "Switch back." No Commander involvement needed.

---

## The Local Control Panel (ESx) 🎛️

The ESx interface is special — it's the **only** way to manage profiles without going through the Commander:

| Command | What It Does |
|---|---|
| `LocalEnableTestProfile` | Switch to test mode now |
| `LocalDisableTestProfile` | Return from test to previous profile |
| `LocalEnableEmergencyProfile` | Activate emergency calling now |
| `LocalDisableEmergencyProfile` | Return from emergency to previous profile |

ESx **ignores POL1** — in an emergency, the rulebook takes a back seat. But it won't override an already-active Emergency Profile with a Test Profile (emergency calls are more important than testing).

---

## How the Plans Interact 🔀

```
Currently on Network A
         │
         ▼
  Network A fails!
         │
    ┌────┴────┐
    │         │
    ▼         ▼
  Roll Back   Fall-Back
  (try prev   (switch to
   profile)   backup)
    │         │
    └────┬────┘
         │
    Still no connection?
         │
         ▼
   Fall-Back activates
   (if not already on)
```

**Key rule:** Fall-Back never activates when the Emergency or Test Profile is currently enabled. Local activation (human or device choice) takes priority over automatic recovery.

---

## 🧠 Did You Know?

The Fall-Back Mechanism is fully autonomous — the robot detects failure, switches profiles, and reconnects all by itself. The Commander only finds out *afterwards* when the robot sends a notification. This design ensures the robot can save itself even during a total network outage — as long as the Fall-Back network is still working.

---

*Kid-friendly version of GSMA SGP.02 v4.2 §3.16, §3.22–3.31 — Resilience*

← [Back to Kids Articles](index)
