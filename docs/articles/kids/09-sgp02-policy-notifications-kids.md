---
title: "The Robot Rulebook and Report Cards"
date: 2026-06-07
---

# The Robot Rulebook and Report Cards 📋

## Imagine...

You're the Fleet Owner. You have a profile on Robot #8721, and you want to make sure nobody — not the Fleet Manager, not even the Commander — can delete it by accident. You write a rule: "This profile must never be deleted." You tape one copy inside the robot's vault and give another copy to the Commander.

Now, every time someone tries to delete that profile, **both copies** get checked. If either one says NO, the deletion fails.

That's the **Policies and Notifications** system in SGP.02 — a double-check rulebook that keeps everyone honest.

---

## Two Rulebooks, Two Locations 📚

| Rulebook | Location | Who Enforces It | Who Updates It |
|---|---|---|---|
| **POL1** | Inside the ISD-P (on the chip) | The ISD-R (Commander's Office) | Only the Operator via ES6 OTA |
| **POL2** | In the SM-SR's EIS database | The Commander | Only the Operator via ES2→ES3 relay |

### Why Two?

- **POL1** protects against a rogue Commander. Even if the Commander gets hacked, the chip checks POL1 before doing anything.
- **POL2** protects against wasted radio commands. The Commander checks POL2 *before* sending a command — saving OTA bandwidth.

An attacker would need to defeat **both** the Commander AND the robot chip — a much higher bar.

---

## What Rules Can You Write? ✏️

Rules cover the three lifecycle actions:

| Action | Possible Rules |
|---|---|
| Enable | "Enable not allowed" or "Enable allowed" |
| Disable | "Disable not allowed" or "Disable allowed" |
| Delete | "Delete not allowed" or "Delete mandatory when disabled" |

Special combinations:
- "Disable not allowed" + "Delete mandatory when disabled" = **Locked forever** — only Master Delete can remove it
- Empty POL1/POL2 = No restrictions — any action is permitted

---

## The Double-Check in Action 🔍

| POL1 Says | POL2 Says | Result |
|---|---|---|
| ✅ Allow | ✅ Allow | Command executes |
| ✅ Allow | ❌ Deny | Commander rejects before OTA — saves bandwidth |
| ❌ Deny | ✅ Allow | Commander sends command; chip rejects it |
| ❌ Deny | ❌ Deny | Commander rejects (first to check) |

The most restrictive combination always wins. Both must say YES for any action to proceed.

---

## After Disabling: Deletion Check ⚡

When a profile is disabled, both POL1 and POL2 get checked for "delete mandatory when disabled":

- **POL1-triggered deletion**: The robot deletes the profile right after disabling, before even telling the Commander
- **POL2-triggered deletion**: The Commander orders deletion after receiving the notification

Yes, the same profile could be deleted twice — and SGP.02 handles this gracefully! The second deletion attempt simply finds the room already empty.

---

## Report Cards: The Notification System 📬

Every time a robot's profile state changes, it sends a **report card** to the Commander:

| Event | Notification |
|---|---|
| First ever network attachment | "I'm alive!" notification |
| Profile enabled | "Now using Network B" |
| Profile disabled | "Network A is off" |
| Fall-Back activated | "Emergency! Switched to backup" |
| Profile deleted | "Room is empty now" |

### Two Ways to Send Report Cards

| Method | How It Works |
|---|---|
| **SMS** | Robot sends a secure text message; Commander replies with confirmation |
| **HTTPS** | Robot opens a secure web tunnel; Commander confirms inside the same session |

If the Commander doesn't confirm within the Validity Period, the robot treats it as a failure and **rolls back** to the previous state. No confirmation = no trust.

---

## The Opt-Out Option 📴

Some Fleet Owners don't want to be notified about every little thing. The **ONC** (Operator Notification Configuration) lets them suppress specific notifications:

| Setting | Effect |
|---|---|
| No ONC (default) | Get ALL notifications |
| ONC with exclusions | Skip certain notification types |
| SM-SR doesn't support ONC | All notifications sent — can't disable |

---

## M2M SP Permissions (PLMA) 🚛

Fleet Managers (M2M SPs) need permission to manage profiles. The Operator grants this through **PLMA** (Profile Lifecycle Management Authorization):

- "M2M SP can enable/disable profiles of Type X"
- "M2M SP can receive notifications about profile changes"
- "M2M SP can set Emergency/Fall-Back attributes"
- **Never**: "M2M SP can change POL2" — that's Operator-only

---

## 🧠 Did You Know?

POL1 lives inside the tamper-resistant chip, protected by hardware security. POL2 lives on a server. This means even if the Commander's entire data center gets hacked, the on-chip rulebook still protects the profiles. You'd need to physically drill into the chip to change POL1 — and good luck with that!

---

*Kid-friendly version of GSMA SGP.02 v4.2 §3.11–3.15, §3.20–3.21, §3.24 — Policies & Notifications*

← [Back to Kids Articles](index)
