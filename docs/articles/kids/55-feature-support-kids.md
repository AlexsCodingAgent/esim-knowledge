---
description: "The capability handshake that happens before any eSIM magic — how phones, chips, and servers trade 'what I can do' cards so nobody tries a spell the other side doesn't know."
title: "Feature Support: The Handshake Before the Magic Trick"
date: 2026-06-07
---

# The Handshake Before the Magic Trick 🤝

## Imagine...

You're at a magic convention. You meet another magician and want to perform a trick together. But before you start pulling rabbits out of hats, you need to know: does this magician know the **levitation spell**? Can they do the **disappearing coin**? Is their spellbook the old edition or the new one?

If you try a spell they don't know, the trick fails: maybe even disastrously! So before any magic happens, you do a quick **check-in**: "Here's what I can do. What can you do?"

That's exactly what the **Feature Support** system does in SGP.22 v3.x: it's the friendly handshake where everyone shares their magical abilities before any serious spells get cast.

---

## The Problem: Different Spellbooks 📚

Not every phone, chip, or server runs the same version of the eSIM rulebook:

- Your brand-new phone might run **v3.1** (the latest edition)
- The Key Maker's server might still run **v2.7** (an older edition)
- Your friend's phone might run **v3.0** (last year's edition)

Without a handshake, the Key Maker might try sending a "Remote Control spell" to a phone that has no idea what that means: and everything breaks!

---

## How the Handshake Works 🤝

During the very first secure connection (called Common Mutual Authentication), everyone exchanges a little card with their capabilities:

| Who? | What They Share | What It Says |
|---|---|---|
| The Magic Vault Chip | `EuiccRspCapability` | "I can do RPM, MEP, Push... here's what I support" |
| The Phone's Assistant | `lpaRspCapability` | "I'm running version X.Y and I can do these tricks" |
| The Key Maker / Post Office | `rspCapability` | "I'm running version X.Y, and I support these features" |

If the Key Maker's card is **missing** a certain trick (or missing `rspCapability` entirely), everyone knows to stick to the simpler, older spells.

---

## The Secret Tag System 🏷️

Inside the spellbook, every magical instruction has tiny hidden tags that say when it can be used:

| Tag | Meaning (In Plain English) |
|---|---|
| `#SupportedFromV3.0#` | "Only use this spell if everyone involved is v3.0 or newer" |
| `#SupportedForRpmV3.0#` | "This is a Remote Control spell: only works with RPM-capable chips" |
| `#SupportedForMEPV3.1#` | "This is a Two-Cloaks trick: only for MEP-capable phones" |
| `#SupportedForPushServiceV3.1#` | "This is a Doorbell spell: only for Push-capable phones" |
| `#MandatoryFromV3.1#` | "This used to be optional, but from v3.1 onwards it's always required" |

The Key Maker reads these tags and only includes spells that both sides understand.

---

## What Happens When Someone's Silent? 🔇

**Golden rule**: If the Key Maker or Post Office doesn't include `rspCapability` in their response, it means they're running a **pre-v3** version. The Phone's Assistant immediately switches to "old magic only" mode: no Remote Control, no Doorbell, no Two Cloaks.

This is the genius of the system: it gracefully falls back to whatever works. No errors, no crashes, no failed tricks.

---

## A Real Example 🎬

The Key Maker receives `EuiccRspCapability` from your phone:
- rpmSupport = **yes** ✅  
- deviceChangeSupport = **no** ❌  
- pushServiceV3Support = **no** ❌  

The Key Maker thinks: "OK, I can send Remote Control spells, but I won't try Device Change or Push: they wouldn't understand!"

---

Without this handshake system, every time a new spell was invented, all the old phones and servers would need updates just to *not crash* when they saw an unfamiliar instruction. The Feature Support system means old and new can work together forever: like a magician who knows which tricks to keep in the pocket!

---

*Kid-friendly version of [Feature Support]({{ site.baseurl }}/docs/articles/sgp22-v3/55-feature-support)*

← [Back to Kids Articles](index)
