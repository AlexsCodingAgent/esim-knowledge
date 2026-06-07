---
description: "How enterprise eSIM profiles work like a company keycard inside your phone — rules that keep the work key active, limit personal profiles, and survive even a factory reset."
title: "Your Work Keycard"
date: 2026-06-07
---

# Your Work Keycard 🏢🪪

## Imagine...

You work at a big company. They give you a work keycard. It opens the office door, lets you into the server room, and pays for lunch at the cafeteria.

But there are rules: you can't throw away the keycard (the company owns it). You can't lend it to a friend. If you leave the company, THEY decide when to deactivate it: not you. Maybe the company even says: "You can have one personal key on this keychain, but the work key must always be active."

That's an **Enterprise Profile** : your work keycard, living inside your magic vault alongside your personal keys.

---

## What Makes a Key an "Enterprise" Key? 🏷️

Any key can become an enterprise key: the magic isn't in its shape but in the **Enterprise Configuration**:

| Field | What It Means |
|---|---|
| **Enterprise OID** | A globally unique company ID. Immutable: never changeable. |
| **Enterprise Name** | The human-readable name: "Acme Corp" |
| **Enterprise Rules** | The actual restrictions the company enforces |

Without the Enterprise Rules, the key is just a regular profile with a company label. The rules give it teeth!

---

## The Three Rule Switches 🎚️

| Switch | What It Does |
|---|---|
| **`referenceEnterpriseRule`** | The master switch. This profile's rules govern the ENTIRE vault. Only ONE profile can hold this. |
| **`priorityEnterpriseProfile`** | Work comes first. You must enable the work key before (or instead of) any personal key. |
| **`onlyEnterpriseProfilesCanBeInstalled`** | Company phone only. No personal keys allowed: only work profiles. |

Plus a quota: **`numberOfNonEnterpriseProfiles`** limits how many personal keys can be active at once. A vault with 3 slots might have Work Key (always on) + 2 personal keys = quota full!

---

## Three Kinds of Devices 📱

| Device Type | What It Means |
|---|---|
| **Enterprise Capable** | Full enforcement. Rules ARE enforced by hardware. Seven checks during download. |
| **Non-Enterprise Capable** | Regular phone. Can install enterprise profiles, but rules are just labels: not enforced. |
| **Enterprise Owned** | Company owns the phone. Strongest enforcement. |

---

## How Work and Personal Keys Coexist 🤝

### BYOD: Bring Your Own Device

You own the phone, company provides the SIM. Work key lives alongside personal keys. `priorityEnterpriseProfile` keeps the work key active. Quota limits how many personal keys can be on. Combined with PPR2 ("cannot delete"), the company key stays put.

### COPE: Corporate Owned, Personally Enabled

Company buys the phone, you use it for work AND personal. `onlyEnterpriseProfilesCanBeInstalled` may block all personal profiles: or allow exactly one. The company key is undeletable, always active.

---

## Enterprise Rules vs Profile Policy Rules ⚖️

| Aspect | PPRs (Profile Policy Rules) | Enterprise Rules |
|---|---|---|
| **Scope** | This one key only | The entire vault |
| **Who sets them** | Any carrier (if RAT allows) | The enterprise company |
| **What they control** | "Don't disable" / "Don't delete" this key | What keys can be installed, priority, quotas |
| **Can be changed** | Unsettable via remote update | Enterprise OID is immutable forever |
| **Where enforced** | Profile Policy Enabler | Profile Rules Enforcer (same hardware, separate logic) |

They work together: an enterprise profile might have PPR2 (undeletable) AND Enterprise Rules (work-only device). Both enforced independently in vault hardware.

---

## The Seven Guards at the Gate 🛡️

When downloading an enterprise profile, the Assistant runs seven checks:

| # | Check | What Gets Rejected |
|---|---|---|
| 1 | Enterprise + existing PPR1 | Can't mix work key with PPR1-protected key |
| 2 | Rules on non-capable device | Can't enforce rules on a regular phone |
| 3 | User rejects rules | You said "no" during consent |
| 4 | OID mismatch | New work key's company ID doesn't match existing ones |
| 5 | Reference rule error | Master switch set but configuration invalid |
| 6 | Enterprise-only conflict | Reference rule demands work-only, but you're installing personal |
| 7 | LPR not supported | Profile needs Local Profile Removal but device lacks it |

Each check has its own error code: when something fails, everyone knows exactly why.

---

Once an Enterprise OID is written into the vault, it can NEVER be changed: not by you, not by the company, not even by the Key Maker. The eUICC chip enforces this in hardware. Even a rogue IT admin can't remotely change the company ID on your work profile. The vault says: "Sorry, that field is locked forever."

---

*Kid-friendly version of GSMA SGP.22 v3.x, Sections 2.4a.1.7 and 2.4.12: Enterprise Profiles and Enterprise Rules*

← [Back to Kids Articles](index)
