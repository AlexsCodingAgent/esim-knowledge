---
title: "The Vault's Rulebook"
date: 2026-06-07
---

# The Vault's Rulebook 📋🔒

## Imagine...

Your magic vault holds several secret keys. Some are yours. One might belong to your employer. One might be from a carrier who gave you a free phone on a two-year contract.

What if you accidentally deleted the work key? What if you disabled the contract key before the two years were up? Chaos!

That's why every vault comes with a **Rulebook** : the Rules Authorisation Table (RAT) : and every key comes with sticky notes attached: the Profile Policy Rules (PPRs). Together, they decide who can do what to which key.

---

## The Three Pillars of the Rulebook 🏛️

### Pillar 1: The Sticky Notes: Profile Policy Rules (PPRs)

These are rules attached to individual keys by the carrier:

| Rule | Meaning | Analogy |
|---|---|---|
| **PPR1** | "Disabling this key is NOT allowed" | A key that must stay ON: always active |
| **PPR2** | "Deleting this key is NOT allowed" | A key glued into the vault: can't be removed |

A key can have one, both, or no rules. Test keys never have rules.

### Pillar 2: The Rulebook: Rules Authorisation Table (RAT)

The manufacturer writes the rulebook when the vault is built: and it CANNOT be erased, even by a factory reset. The RAT says which operators can use which rules, and whether the user must agree.

Example RAT:

| Allowed Operator | Which Rules | User Must Agree? |
|---|---|---|
| Operator Alpha | PPR1 only | No |
| Operator Beta | PPR2 only | No |
| ANY operator | PPR1 and PPR2 | YES! |

So if Operator Gamma tries PPR1, the user sees: "⚠️ Operator Gamma wants to install a key you can't disable. Do you agree?"

### Pillar 3: The Enforcer: Profile Policy Enabler (PPE)

The bouncer at the vault door. When anyone tries to disable or delete a key, the Enforcer checks the sticky notes. No app, no operating system, no hacking can bypass it: it lives inside the vault hardware.

---

## Double-Checking: Two Layers 🛡️🛡️

BOTH the Assistant (LPA) and the Vault (eUICC) independently verify the rules:

| Who Checks | When | What They Verify |
|---|---|---|
| **The Assistant (LPA)** | Before download | "Are these PPRs allowed? Does the user need to consent?" |
| **The Vault (eUICC)** | During installation | Same check: independently. If the Assistant was tricked, the vault still catches it. |

---

## The MEP Problem ⚔️

**MEP** (Multiple Enabled Profiles) lets your vault have several active keys at once. But PPR1 says: "You can't disable this key." Conflict!

The solution is clean:

| Vault Type | PPR1 Allowed? | Why |
|---|---|---|
| Single-key vault (SEP) | ✅ Yes | Enabling a new key means disabling the old one |
| Multi-key vault (MEP) | ❌ No | Multiple keys active: no need to disable |

---

## Exceptions That Make Sense 🎭

- **Test Profiles override PPR1:** Technicians can enable a test key temporarily: the vault re-enables the protected key afterwards
- **Provisioning Profiles:** The Assistant can enable a provisioning key even with PPR1 active: needed for initial setup

---

## Old Rules vs New Rules 📊

| Aspect | v2.x | v3.x |
|---|---|---|
| Policy enforcement | Basic PPR support | PPR + Enterprise Rules + MEP awareness |
| Who enforces | eUICC only | LPA checks first, eUICC checks second |
| MEP compatibility | N/A (no MEP) | PPR1 explicitly banned on MEP eUICCs |
| RPM respect | N/A (no RPM) | RPM commands rejected if they violate PPRs |

---

The RAT is written into the vault at the factory and survives even a complete memory wipe. It's the one thing on your eSIM chip that can NEVER be changed by anyone: not by you, not by your carrier, not even by the phone manufacturer. It's the technological equivalent of "etched in stone."

---

*Kid-friendly version of GSMA SGP.22 v3.x, Section 2.9: Profile Policy Management*

← [Back to Kids Articles](index)
