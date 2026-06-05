---
title: "EID in RSP Protocols: Discovery, Matching, and Events"
date: 2026-06-05
---

# EID in RSP Protocols: Discovery, Matching, and Events

**🏠 [eUICC.tech](/) > [SGP.29 EID](/docs/articles/sgp29/) > EID in RSP Protocols: Discovery, Matching, and Events**

> **💡 Why this matters:** The EID is not a static label — it is an active operational identifier woven throughout every major RSP protocol. When a consumer scans a QR code to activate an eSIM, when an IoT device wakes up and polls for pending profiles, when an operator pushes an event notification — the EID is the key that links the request to the correct chip. Understanding where and how the EID appears in RSP protocols illuminates the end-to-end identity plumbing of the eSIM ecosystem.

> **Key takeaways:**
> - The EID is used in SM-DS (Subscription Manager Discovery Service) to match pending profiles to specific eUICCs
> - ES11 polling uses the EID to query the SM-DS for profiles awaiting download
> - During ES8+ profile download, the EID binds the profile to the correct eUICC through ISD-R operations
> - Event registration uses the EID to subscribe specific eUICCs to push notifications from SM-DS
> - SGP.29 references SGP.01, SGP.02, SGP.21, and SGP.22 as the defining RSP documents where the EID is operationalised
> - The EID's use extends across both consumer (SGP.22) and IoT (SGP.32) architectures

SGP.29 Section 6 explicitly states: "The EID is the eUICC Identifier used in the context of Remote SIM Provisioning and Management of the eUICC as defined in [SGP.01], [SGP.02], [SGP.21] and [SGP.22]." This article traces how the EID flows through these specifications in practice.

---

## Reference Architecture Context

The EID features in both the original M2M architecture (SGP.01/SGP.02) and the Consumer architecture (SGP.21/SGP.22):

```
┌─────────────────────────────────────────────────────────────────┐
│                    Consumer RSP Architecture                     │
│                         (SGP.21 / SGP.22)                        │
│                                                                  │
│  ┌─────────┐     ES11     ┌──────────┐     ES12     ┌─────────┐  │
│  │  LPA    │◄────────────►│  SM-DS   │◄────────────►│ SM-DP+  │  │
│  │ (in     │   EID-based  │Discovery │   Event      │ Profile │  │
│  │  Device)│   polling    │ Service  │   Registry   │ Server  │  │
│  └────┬────┘              └──────────┘              └────┬────┘  │
│       │                                                  │       │
│       │ ES10 (local)                              ES8+   │       │
│       │ EID context                              EID in  │       │
│       │                                           binding │       │
│  ┌────┴────┐                                      ┌────┴────┐  │
│  │  eUICC  │◄────────── Profile Download ────────│ SM-DP+  │  │
│  │  (EID)  │          (EID-authenticated)         │         │  │
│  └─────────┘                                      └─────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1. SM-DS Discovery: Profile Matching by EID

The SM-DS (Subscription Manager Discovery Service) is the central directory that matches profiles waiting to be downloaded with the eUICCs that should receive them.

### How It Works

```
┌──────────────────────────────────────────────────────────────────┐
│  SM-DP+ prepares a profile for download                          │
│       │                                                          │
│       ▼                                                          │
│  SM-DP+ registers Event with SM-DS:                              │
│    • EID = 12345000000000000000000000000133                      │
│    • Event Type = Profile Download Available                     │
│    • SM-DP+ Address = dp.example.com                             │
│       │                                                          │
│       ▼                                                          │
│  SM-DS stores: {EID → [Pending Events]}                         │
│       │                                                          │
│       ▼                                                          │
│  LPA polls SM-DS (ES11): "Any events for EID 12345...0133?"     │
│       │                                                          │
│       ▼                                                          │
│  SM-DS responds: "Yes → Event from dp.example.com"              │
│       │                                                          │
│       ▼                                                          │
│  LPA initiates ES8+ download from SM-DP+                        │
└──────────────────────────────────────────────────────────────────┘
```

The EID is the **primary lookup key** in the SM-DS. Without the EID, the SM-DS has no way to associate a pending profile with the correct chip.

### EID Uniqueness Requirement

This is why SGP.29 Principle EID.P02 mandates **global uniqueness** — if two eUICCs shared the same EID, the SM-DS would route profiles to the wrong device, with potentially catastrophic security consequences (e.g., an operator profile being downloaded onto an attacker's device).

---

## 2. ES11 Polling: EID as the Query Parameter

ES11 is the interface between the LPA (Local Profile Assistant) and the SM-DS. The LPA queries the SM-DS on behalf of the eUICC using the EID:

```
LPA → SM-DS (ES11):

  GET /gsma/rsp2/es11/handle-ds-event
  {
    "eid": "12345000000000000000000000000133",
    "lpaSignature": "..."
  }

SM-DS → LPA (ES11 Response):

  {
    "pendingEvents": [
      {
        "eventId": "abc-123",
        "rspServerAddress": "dp.example.com"
      }
    ]
  }
```

The LPA periodically polls the SM-DS (or is triggered by the user opening the eSIM management UI). Each poll includes the EID, and the SM-DS responds with any pending events for that EID.

### IoT Context (SGP.32)

In the IoT architecture, the IPA (IoT Profile Assistant) performs an analogous function over ESipa, using the EID to poll the SM-DS for IoT profiles.

---

## 3. ES8+ Profile Download: EID in Mutual Authentication

Once the LPA has been directed to the correct SM-DP+ (via SM-DS discovery or QR code), the ES8+ profile download begins. The EID is central to the mutual authentication that precedes any profile transfer.

### eUICC Authentication Flow (Simplified)

```
SM-DP+                                    eUICC
  │                                         │
  │  [Knows EID from discovery/QR]          │
  │                                         │
  │  ES8+.GetBoundProfilePackage ──────────▶│
  │  (includes expected EID)                │
  │                                         │
  │                          ┌──────────────┴──────────────────┐
  │                          │ eUICC verifies:                 │
  │                          │ • "Is this profile for my EID?" │
  │                          │ • "Is SM-DP+ certificate valid?"│
  │                          │ • "Does the binding match?"     │
  │                          └──────────────┬──────────────────┘
  │                                         │
  │  ◀─────────── eUICC responds with      │
  │               eUICC signature + EID     │
  │                                         │
  │  ┌───────────┴──────────────────────────┐
  │  │ SM-DP+ verifies:                     │
  │  │ • "Does EID match expected?"         │
  │  │ • "Is eUICC certificate valid?"      │
  │  │ • "Is signature correct?"            │
  │  └───────────┬──────────────────────────┘
  │                                         │
  │  Bound Profile Package ────────────────▶│
  │  (encrypted to eUICC's public key)      │
  │                                         │
```

The EID acts as an identity anchor throughout this exchange. The SM-DP+ binds the profile to a specific EID, and the eUICC confirms the profile was intended for it.

---

## 4. Event Registration: EID-Based Notifications

Beyond polling, the SM-DS also supports event-driven notifications. An SM-DP+ can register events for specific EIDs:

### Event Types

| Event | Trigger | EID Role |
|-------|---------|----------|
| **Profile Download Available** | SM-DP+ has prepared a profile | EID identifies the target eUICC |
| **Profile State Change** | Profile enabled/disabled/deleted | EID links the event to the chip |
| **Remote Management** | Operator pushes management command | EID routes the command |

### Registration Flow

```
SM-DP+ → SM-DS (ES12):

  REGISTER Event
    Event ID:    evt-xyz-001
    EID:         12345000000000000000000000000133
    Event Type:  Profile Download Available
    RSP Address: dp.example.com
    Expiry:      2026-07-05T00:00:00Z

SM-DS stores the event and serves it on next ES11 poll for that EID.
```

---

## 5. The EID Across Specification Boundaries

The EID's role spans all four core RSP specifications:

| Specification | EID Usage Context |
|--------------|-------------------|
| **SGP.01** | Defines the RSP architecture where EID is the eUICC's identity |
| **SGP.02** | M2M technical specification — EID used in profile download and management for M2M devices |
| **SGP.21** | Consumer architecture — EID as the identity anchor in the LPA-based workflow |
| **SGP.22** | Consumer technical specification — EID in ES8+, ES11, and event registration operations |
| **SGP.32** | IoT technical specification — EID in IPA-based discovery and download (analogous to SGP.22 but for IoT) |

---

## 📋 Summary

- The EID is the primary lookup key in the SM-DS, matching pending profiles to specific eUICC chips
- ES11 polling uses the EID as the query parameter — no EID, no discovery
- During ES8+ profile download, the EID anchors mutual authentication between SM-DP+ and eUICC
- Event registration uses the EID to subscribe individual eUICCs to push notifications
- Global EID uniqueness (SGP.29 Principle EID.P02) is essential for protocol correctness — duplicate EIDs would break profile routing
- The EID's operational role spans both consumer (SGP.22) and IoT (SGP.32) architectures

---

<div align="center">

← Previous: [EID Assignment: How Manufacturers Get Their Allocations](/docs/articles/sgp29/29-sgp29-assignment) · [🏠 Home](/)

Next: [EID Security: Privacy, Tracking, and GSMA Governance](/docs/articles/sgp29/31-sgp29-security) →

</div>

---

*Based on GSMA SGP.29 v1.1 (22 March 2024) — EID Definition and Assignment Process, Section 6 (EID Usage), with protocol context from SGP.21, SGP.22, and SGP.32*
