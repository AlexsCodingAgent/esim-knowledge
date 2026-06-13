---
description: "How SGP.22 v3.x devices talk to older v2.x servers: the simple 'missing card' rule that lets billions of existing eSIM chips keep working while new features stay hidden."
title: "Version Interop: When Old and New Magic Work Together"
date: 2026-06-07
---

# When Old and New Magic Work Together 🧙‍♂️🧙‍♀️

## Imagine...

Your grandparent has an old flip phone. You have the newest smartphone with every feature imaginable. You want to call your grandparent. Does your phone say: "Sorry, this person uses old technology, I refuse to connect!" No! Phones are designed to work together: your fancy smartphone still knows how to make a simple voice call that your grandparent's flip phone can handle.

The eSIM world has the same challenge. There are **billions** of older eSIM chips out there running v2.x magic. When SGP.22 v3.x came along with all its shiny new spells, it had to make sure it could still talk to all those older devices: and that older devices wouldn't get confused by the new magic.

---

## The Problem: A World Full of Different Spellbooks 🌍

Not everyone upgrades at the same time:

- **Old Phone** (v2.x) + **Old Key Maker** (v2.x) : both speak the old magic
- **New Phone** (v3.x) + **Old Key Maker** (v2.x) : your new phone must speak old magic
- **Old Phone** (v2.x) + **New Key Maker** (v3.x) : the new server must speak old magic
- **New Phone** (v3.x) + **New Key Maker** (v3.x) : full new magic party!

v3.x was designed for **all four scenarios** from day one.

---

## The Secret: The Missing Card Trick 🃏

Remember the handshake from the Feature Support article? Here's the key insight for version interop:

**When the Key Maker doesn't include `rspCapability`, it means "I'm pre-v3."**

That's it! That one simple rule makes everything work:

| Scenario | What Happens |
|---|---|
| New Phone + Old Key Maker | Key Maker sends no `rspCapability`. Phone says "Ah, old magic!" and uses only v2.x spells. |
| Old Phone + New Key Maker | Phone sends no `EuiccRspCapability`. Key Maker says "Old chip!" and uses v2.x profile packages. |
| New Phone + New Key Maker | Both share capabilities. Full v3.x magic unlocked! |

---

## How Different Conversations Work 🗣️

Different helpers use different signals to figure out what version they're dealing with:

| Conversation | Negotiation Signal |
|---|---|
| Phone ↔ Key Maker | `rspCapability` fields during the handshake |
| Key Maker ↔ Key Maker (server to server) | `X-Admin-Protocol` HTTP header (same as v2.x) |
| Phone ↔ Magic Vault Chip | The Phone's Assistant asks the chip for its `highestSvn` |
| Human-Readable Website (HRI) | Different URL versions: no negotiation needed! |

---

## The Profile Package Picker 📦

When the Key Maker is about to send a secret key to a phone, it checks what versions the chip supports:

- If the chip says "I can handle v3.x packages" → send the newest format
- If the chip says "I only know v2.x" → send the older format that it understands
- If there's no overlap → error (but this almost never happens because v3.x chips all speak v2.x too)

It's like a translator who can speak both ancient and modern languages: always choosing the one the listener understands best.

---

## What Servers MUST Do ✅

The v3.x rulebook says every server must follow these politeness rules:

- Always include `rspCapability` in their responses
- Never crash if they receive an old-style request without capability info
- Never reject a message just because it has extra fields they don't understand
- Always pick the right profile package version for the chip

---

This backwards-compatibility design means you could take a brand-new v3.1 phone to a mobile company running a 5-year-old v2.x Key Maker: and everything would work perfectly. The phone simply becomes a well-behaved v2.x phone for that conversation. It's like being fluent in both modern slang and old-fashioned language, switching effortlessly depending on who you're talking to!

---

*Kid-friendly version of [Version Interoperability]({{ site.baseurl }}/docs/articles/sgp22-v3/56-version-interoperability)*

← [Back to Kids Articles](index)
