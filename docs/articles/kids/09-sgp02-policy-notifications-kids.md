---
title: "The Double-Lock Rulebook and Report Cards"
date: 2026-06-07
---

# The Double-Lock Rulebook and Report Cards 📋

What if you could write a rule that **nobody** could break? Not the Fleet Manager. Not the Commander. Not even someone who hacked the central server?

SGP.02 gives Fleet Owners exactly that: a rulebook stored in two places that both have to agree before anything changes. It's like a safety deposit box that needs two keys, except one key is welded to the vault door and the other is held by a guard three buildings away.

---

## Two Copies, Two Locations

| Rulebook | Where It Lives | Who Guards It | Who Can Change It |
|---|---|---|---|
| **POL1** | Inside the chip itself (ISD-P) | The Commander's office (ISD-R) | Only the Operator, OTA only |
| **POL2** | In the Commander's database (SM-SR EIS) | The Commander | Only the Operator, relayed through the Key Factory |

**Why bother with two?** Because they defend against different threats:

- **POL1** protects against a compromised Commander. Even if the Commander gets hacked and starts issuing malicious commands, the chip checks POL1 *before executing anything*. The hacker needs physical access to the silicon to change it.

- **POL2** protects against wasted radio chatter. The Commander checks POL2 *before* bothering to send a command over the air, saving precious OTA bandwidth. No point transmitting "delete this profile" if POL2 already says no.

To defeat the system, an attacker has to break both the Commander AND the chip. That's a much higher bar.

---

## What Rules Can You Write?

Three lifecycle actions, each with a simple rule:

| Action | Your Choices |
|---|---|
| **Enable** | "Allowed" or "Not allowed" |
| **Disable** | "Allowed" or "Not allowed" |
| **Delete** | "Allowed" or "Delete mandatory when disabled" |

Put them together and you get some interesting combinations. The nastiest one: "Disable not allowed" + "Delete mandatory when disabled" = **locked forever**. Only a Master Delete can touch it. If POL1 and POL2 are both empty? Anything goes: no restrictions at all.

---

## Two Must Say Yes

Both rulebooks get consulted before any command executes:

| POL1 | POL2 | What Happens |
|---|---|---|
| ✅ Allow | ✅ Allow | Command runs |
| ✅ Allow | ❌ Deny | Commander rejects it, saves OTA bandwidth |
| ❌ Deny | ✅ Allow | Commander sends it; chip rejects it |
| ❌ Deny | ❌ Deny | Commander rejects (gets there first) |

The most restrictive combination always wins. Two yeses or nothing.

---

## The Deletion Race

When a profile gets disabled, both POL1 and POL2 get checked for "delete mandatory when disabled." And here's where it gets fun:

- **POL1-triggered deletion**: The chip deletes the profile *immediately* after disabling, before even telling the Commander
- **POL2-triggered deletion**: The Commander orders deletion after receiving the notification

Yes: the same profile might get deleted twice. First by the chip (POL1), then the Commander tries (POL2). SGP.02 handles this gracefully: the second deletion attempt just finds an empty room. No crash, no error, no drama.

---

## Report Cards: Every Change Gets Logged

Every time a profile's state changes, the chip sends a report card to the Commander:

| Event | What Gets Sent |
|---|---|
| First network attachment | "I'm alive!" |
| Profile enabled | "Now using Network B" |
| Profile disabled | "Network A is off" |
| Fall-Back triggered | "Emergency, switched to backup" |
| Profile deleted | "Room is empty now" |

Two delivery methods: **SMS** (secure text message with confirmation reply) or **HTTPS** (secure web tunnel with confirmation inside the same session). If the Commander doesn't confirm within the Validity Period, the chip treats it as a failure and **rolls back** to the previous state. No confirmation = no trust.

---

## The Mute Button (ONC)

Not every Fleet Owner wants a notification for every little thing. The **Operator Notification Configuration** lets you suppress specific alerts. No ONC set = you get everything. ONC with exclusions = skip the boring ones. SM-SR doesn't support ONC? Too bad, all notifications will arrive.

---

## Fleet Manager Permissions (PLMA)

Fleet Managers need explicit permission to touch profiles. The Operator grants it through **PLMA** : Profile Lifecycle Management Authorization:

- "You can enable/disable profiles of Type X"
- "You can receive notifications"
- "You can set Emergency/Fall-Back attributes"
- Never: "You can change POL2" : that's Operator territory only

---

Two copies. Two locations. One unbreakable system.

POL1 lives inside the tamper-resistant chip, protected by hardware security. POL2 lives on a server in a data center. Even if the Commander's entire facility gets compromised, the on-chip rulebook still says NO to dangerous commands. To change POL1, you'd need to physically drill into the chip, and the internal sensors would detect tampering and wipe the keys before you got anywhere near the rulebook.

---

*Kid-friendly version of GSMA SGP.02 v4.2 §3.11–3.15, §3.20–3.21, §3.24, Policies & Notifications*

← [Back to Kids Articles](index)
