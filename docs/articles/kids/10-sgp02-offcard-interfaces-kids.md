---
title: "Secret Languages: How All the Helpers Talk"
date: 2026-06-07
---

# Secret Languages: How All the Helpers Talk 🗣️

## Imagine...

Six different helpers in the robot network all need to talk to each other. The Key Factory talks to the Commander. The Commander talks to the Chip Builder. The Fleet Owner talks to everyone. But they all speak different "languages" — different interfaces with different rules.

SGP.02 defines six off-card interfaces (server-to-server) that connect the entire ecosystem. Think of them as dedicated telephone lines between helpers.

---

## The Interface Map 🗺️

```
     🏛️ CI
      │ (out of band)
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

## All Six Interfaces at a Glance 🃏

| Interface | Between | Purpose | Function Count |
|---|---|---|---|
| **ES1** | Chip Builder → Commander | Register new robots at manufacturing | 2 functions |
| **ES2** | Fleet Owner → Key Factory | Order profiles, manage lifecycle, get notifications | 25 functions |
| **ES3** | Key Factory → Commander | Relay profile operations, create rooms, deliver keys | 28 functions |
| **ES4** | Fleet Owner / Fleet Manager → Commander | Direct lifecycle operations, database queries | 23 functions |
| **ES4A** | Fleet Owner → Commander | Manage Fleet Manager permissions (PLMA) and notification settings (ONC) | 4 functions |
| **ES7** | Commander → Commander | Hand over robots during SM-SR Change | 3 functions |

---

## Two Conversation Styles 💬

Every interface uses one of two patterns:

| Pattern | How It Works | Used For |
|---|---|---|
| **Request-Response** | "Please do X" → "Done!" or "Failed!" | Enable, disable, delete, download |
| **Notification Handler** | "Just so you know: Y happened" → (no response expected) | Status updates, profile changes |

---

## ES1: Registering New Robots 🏭

The simplest interface. When the Chip Builder manufactures a new robot:

- `RegisterEIS`: "Here's a new robot — its ID, certificate, and initial configuration"
- `UpdateEISAdditionalProperties`: "Here's updated info for an existing robot"

This happens exactly once per robot, at the factory.

---

## ES2: The Fleet Owner's Control Panel 📡

The busiest interface after ES3. The Fleet Owner uses it to talk to the Key Factory:

| Category | Example Functions |
|---|---|
| **Profile Orders** | `DownloadProfile`, `GetEUICCInfo` |
| **Lifecycle** | `EnableProfile`, `DisableProfile`, `DeleteProfile` |
| **Policies** | `UpdatePolicyRules` (POL2) |
| **Attributes** | `SetFallBackAttribute`, `SetEmergencyProfileAttribute` |
| **Fleet Manager** | `SetAuthorisationsOfM2MSP` (PLMA) |
| **Notifications** | Receive `HandleProfileEnabledNotification` and 7+ others |

---

## ES3: The Key Factory's Relay Service 🔑

The busiest interface overall (28 functions). The Key Factory uses ES3 to work through the Commander:

- `GetEIS`: "Tell me everything about robot #8721"
- `CreateISDP`: "Build a new profile room"
- `EstablishISDPKeySet`: "Let's do the secret handshake"
- `DownloadProfile`: "Deliver this encrypted package"
- Plus relay versions of all ES2 lifecycle commands
- Plus passing notifications back to the Fleet Owner

---

## ES4: The Direct Hotline 📞

When the Fleet Owner has a direct relationship with the Commander, they skip the Key Factory and use ES4. Functionally identical to ES2 — just a different route:

| ES2 Path | ES4 Equivalent |
|---|---|
| `ES2.EnableProfile → ES3 → ES5` | `ES4.EnableProfile → ES5` |
| Fewer hops | More direct |

M2M Fleet Managers also use ES4 (with PLMA permission), but they can't use ES4A.

---

## ES4A: Permission Slips Only 📝

A tiny interface dedicated to two things:

- `SetPLMA` / `GetPLMA`: Who can the Fleet Manager manage?
- `SetONC` / `GetONC`: Which notifications should I skip?

---

## ES7: Commander Handshake 🤝

The only inter-Commander interface. Only used during SM-SR Change:

- `HandoverEUICC`: "Here's the robot database — it's yours now"
- `AuthenticateSM-SR`: "Check my ID badge"
- `CreateAdditionalKeySet`: "Let's agree on new keys"

Small but critically important — this is what prevents vendor lock-in.

---

## The Secret Courier Language 📨

All these interfaces use a common message format:
- **Header**: Who's calling, which robot, what function, execution rules
- **Body**: The actual data — profile details, certificates, keys
- **Transport**: SOAP web services over HTTPS with mutual TLS authentication

It's like a standardized shipping label that every helper understands, no matter which interface it travels on.

---

## 🧠 Did You Know?

ES2 and ES4 are basically the same interface — just different routes! ES2 goes through the Key Factory (relay), while ES4 goes directly to the Commander. This dual-path design means the Fleet Owner can choose whichever is more efficient or available.

---

*Kid-friendly version of GSMA SGP.02 v4.2 Chapter 5 (§5.1–5.7) — Off-Card Interfaces*

← [Back to Kids Articles](index)
