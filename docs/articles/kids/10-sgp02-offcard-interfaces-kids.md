---
title: "Six Phone Lines: How the Chip Helpers Talk to Each Other"
date: 2026-06-07
---

# Six Phone Lines: How the Chip Helpers Talk to Each Other 🗣️

Picture a construction site. The architect needs to tell the electrician where to run the wiring. The electrician needs parts from the supplier. The site manager needs daily reports from everyone. And they all have different clipboards, different walkie-talkie channels, different forms.

SGP.02's server-to-server world works the same way. Six dedicated communication channels, called **off-card interfaces** : connect all the different "helpers" in the eSIM ecosystem. Each one has a specific job, a specific caller, and a specific recipient. No confusion. No crossed wires.

---

## Who's Calling Whom?

```
     🏛️ CI (Certificate Issuer)
      │ out-of-band only
      │
🏭 Chip Builder ──ES1──▶ 🦾 Commander
                             ▲
                             │ ES3
                          🔑 Key Factory
                             ▲
                             │ ES2
                             │
                          📡 Fleet Owner ──ES4──▶ Commander
                                            ES4A
                             │
                          🚛 Fleet Manager ──ES4──▶ Commander

     Commander (old) ◀──ES7──▶ Commander (new)
```

---

## The Six Lines at a Glance

| Line | Caller → Receiver | What It's For | How Many Functions |
|---|---|---|---|
| **ES1** | Chip Builder → Commander | Register new chips at the factory | 2 |
| **ES2** | Fleet Owner → Key Factory | Order profiles, manage lifecycles, get notified | 25 |
| **ES3** | Key Factory → Commander | Relay profile operations, create rooms, deliver keys | 28 |
| **ES4** | Fleet Owner/Fleet Manager → Commander | Direct lifecycle commands, database queries | 23 |
| **ES4A** | Fleet Owner → Commander | Manage Fleet Manager permissions and notification settings | 4 |
| **ES7** | Commander → Commander | Hand over chips during SM-SR Change | 3 |

---

## Two Conversation Styles

Every interface uses one of two patterns:

- **Request-Response**: "Please do X" → "Done!" or "Failed!" : used for commands like enable, disable, delete, and download
- **Notification Handler**: "Just so you know: Y happened" : used for status updates; no response expected

The first is a phone call. The second is a postcard.

---

## ES1: Factory Registration

The simplest of the bunch. When the Chip Builder manufactures a new eUICC:

- `RegisterEIS`: "Here's a new chip, its ID, certificate, and initial setup"
- `UpdateEISAdditionalProperties`: "Here's updated info for an existing chip"

This happens exactly once per chip, at the factory. Short and sweet.

---

## ES2: The Fleet Owner's Console

The second-busiest interface. The Fleet Owner uses ES2 to talk *through* the Key Factory:

- **Profile Orders**: `DownloadProfile`, `GetEUICCInfo`
- **Lifecycle**: `EnableProfile`, `DisableProfile`, `DeleteProfile`
- **Policies**: `UpdatePolicyRules` (POL2)
- **Attributes**: `SetFallBackAttribute`, `SetEmergencyProfileAttribute`
- **Fleet Manager**: `SetAuthorisationsOfM2MSP` (PLMA)
- **Notifications**: Receive `HandleProfileEnabledNotification` and seven more event types

25 functions in total, this is the Fleet Owner's Swiss Army knife.

---

## ES3: The Key Factory's Relay Desk

The busiest interface, 28 functions. The Key Factory doesn't talk directly to chips; it talks through the Commander. ES3 handles:

- `GetEIS` : "Tell me everything about chip #8721"
- `CreateISDP` : "Build a new profile room"
- `EstablishISDPKeySet` : "Let's do the secret handshake"
- `DownloadProfile` : "Deliver this encrypted package"
- Relay versions of all ES2 lifecycle commands
- Passing notifications back to the Fleet Owner

Think of ES3 as a postal sorting office: everything passes through here.

---

## ES4: The Direct Hotline

When the Fleet Owner has a direct relationship with the Commander, they skip the Key Factory entirely and use ES4. Functionally, it mirrors ES2, just with fewer hops:

| Via ES2 route | Via ES4 |
|---|---|
| `ES2.EnableProfile → ES3 → ES5` | `ES4.EnableProfile → ES5` |
| Three hops | Two hops |

Fleet Managers also use ES4 (with PLMA permission), but they can't use ES4A, that's Owner-only territory.

---

## ES4A: The Permissions Desk

The smallest interface, just 4 functions, all about who can do what:

- `SetPLMA` / `GetPLMA` : Which Fleet Manager manages which profiles?
- `SetONC` / `GetONC` : Which notifications should we skip?

---

## ES7: The Handover Channel

The only interface between two Commanders. Used exclusively during SM-SR Change:

- `HandoverEUICC` : "Here's the chip database, it's yours now"
- `AuthenticateSM-SR` : "Check my ID badge"
- `CreateAdditionalKeySet` : "Let's agree on new keys"

Only 3 functions, but critical, this is what prevents vendor lock-in. Without ES7, switching Commanders would be impossible without physically replacing every chip.

---

## One Envelope Format for All

All six interfaces use the same message envelope:

- **Header**: Who's calling, which chip, which function, execution rules
- **Body**: The actual payload, profile details, certificates, keys
- **Wrap**: SOAP web services over HTTPS, mutual TLS authentication

Same envelope, six different destinations. It's like a standardized shipping label that every helper in the ecosystem knows how to read.

---

ES2 and ES4 do essentially the same thing, just via different routes. ES2 goes through the Key Factory (relay), while ES4 goes straight to the Commander. The Fleet Owner picks whichever route makes more sense for their setup. It's a dual-path design that keeps the system flexible: if you have a Key Factory relationship, use ES2. If you talk directly to the Commander, use ES4. Both get the job done.

---

*Kid-friendly version of GSMA SGP.02 v4.2 Chapter 5 (§5.1–5.7) : Off-Card Interfaces*

← [Back to Kids Articles](index)
