---
title: "Three Worlds of eSIM: Factories, Phones, and Farm Fields"
date: 2026-06-07
---

# Three Worlds of eSIM: Factories, Phones, and Farm Fields 📱🤖🔮

Three devices walk into a network.

**First**: a smartphone in your pocket. It has a gorgeous screen, a camera, and a human who taps "Install eSIM" after scanning a QR code.

**Second**: a smart electricity meter bolted to a basement wall. It has no screen. No buttons. Nobody will touch it for 15 years. It was installed in 2018 and hasn't moved since.

**Third**: a soil sensor buried in a cornfield. It wakes up once a day, sends moisture data, and goes back to sleep. It's one of ten thousand.

Same tiny security chip inside all three: the eUICC. But how each one gets its network keys? Completely different. The GSMA wrote three separate specifications, each for a different world.

---

## Meet the Three Worlds

| | SGP.02 (The Factory | SGP.22) The Phone Shop | SGP.32. The Farm Field |
|---|---|---|---|
| **Nickname** | M2M Push | Consumer Pull | IoT Pull |
| **Born** | 2013 | 2015 | 2023 |
| **Built for** | Meters, cars, industrial sensors | Phones, tablets, watches | Sensors, trackers, smart home |
| **How keys arrive** | PUSHED by the Commander | PULLED by the phone (you scan a QR) | PULLED by the device, or nudged by a manager |
| **Who's in charge?** | The Fleet Owner (Operator) | You: the person holding the phone | You, or the IoT Manager (eIM) |

---

## Three Different Delivery Stories

### The Factory (SGP.02) : Keys Get Delivered

```
Fleet Owner: "Switch Meter #5001 to Network B!"
      ↓
   Commander pushes command over the air
      ↓
   Meter: "Command received. Switching."
```

No human. No screen. No scan. The Commander is always in charge. The device doesn't *ask* for keys, it *receives* them. This is push delivery, and it works when the device can't come to you.

### The Phone Shop (SGP.22) : Keys Get Collected

```
You scan a QR code in a store
      ↓
   Your phone: "Key Factory, I need my key!"
      ↓
   Key Factory: "Here you go, enjoy your data plan!"
```

You decide. You scan. You tap "Install." The phone drives everything. The key factory just waits to be asked. This is pull delivery: the device initiates the download.

### The Farm Field (SGP.32) : Best of Both

```
IoT Manager: "Soil Sensor #8721, time for new keys. Check in when you wake up."
      ↓
   Sensor wakes up at 06:00: "Oh, a message! Downloading now..."
      ↓
   Or: You open an app and tap "Update sensors"
```

Flexible. Either the device pulls when it's ready, or the IoT Manager sends a nudge. It's like leaving a note on the fridge: the device reads it when it gets hungry.

---

## Under the Hood: What's Different?

| What Matters | SGP.02 (Factory) | SGP.22 (Phone Shop) | SGP.32 (Farm Field) |
|---|---|---|---|
| **Server setup** | Two servers: SM-DP + SM-SR (split roles) | One server: SM-DP+ (combined) | One server: SM-DP+ (combined) |
| **Helper on device** | None, ISD-R is passive | LPA app (full UI) | IPA (lightweight helper) |
| **Fleet management** | Operator via ES4 | Not built-in | eIM (IoT Manager) |
| **Discovery** | Not needed (push doesn't discover) | SM-DS "post office" | SM-DS or eIM |
| **OTA channel** | Commander owns it | Key Factory owns it | Key Factory owns it |
| **Screen?** | Headless: no UI | Full screen, QR codes, menus | Minimal or none |
| **Key exchange** | ECKA-EG (ElGamal) | ECDH | ECDH |
| **Spec size** | 452 pages | ~296 pages | Still growing |

---

## Which World for Which Device?

Quick decision guide:

- **Smartphone, tablet, smartwatch** → SGP.22. Users expect QR codes and a touch interface. Give them one.
- **Car telematics with eCall** → SGP.02. Built for automotive, 10+ year lifespan, regulatory requirements.
- **Utility meter sealed for 15+ years** → SGP.02. Truly unreachable. Push is the only option.
- **Asset tracker on a shipping container** → SGP.32. Checks in periodically, massive fleets.
- **Smart home sensor (new project, 2026+)** → SGP.32. Modern, flexible, reuses existing consumer infrastructure.
- **Industrial sensor deep in a mine** → SGP.02. Harsh, unreachable, no regular connectivity window.
- **Agricultural sensor grid** → SGP.32. Gateway model handles thousands of constrained devices.

---

## The Push-or-Pull Question

```
Does a human hold this device and have a screen?
    │
    ├── YES ──▶ SGP.22 (the phone shop)
    │
    └── NO ──▶ Can the device reach the internet on its own,
               even occasionally?
                   │
                   ├── YES, sometimes ──▶ SGP.32 (the farm field)
                   │
                   └── NO, truly unreachable ──▶ SGP.02 (the factory)
```

---

## Why the Oldest Spec Still Runs the Show

SGP.02 is from 2013. In tech years, that's ancient. But it's far from dead:

- **Automotive**: A decade-plus head start in connected cars, and regulations that explicitly reference it
- **Utility meters**: Millions installed in 2018:2020, still running SGP.02, still working fine
- **Industrial**: Sealed sensors in places where physical access means a helicopter ride and a permit
- **Legislation**: Some countries' eCall and smart metering laws name SGP.02 directly

The M2M world moves at its own pace: the spec was designed for exactly that reality.

---

## They Don't Compete. They Coexist

Here's the part people miss: an operator can run all three at once. SGP.02 for the automotive fleet. SGP.22 for consumer subscribers. SGP.32 for smart home devices. Same core network, same SIM cards, different provisioning paths. The eUICC chip itself can potentially support multiple specs, it's just a secure vault, after all.

---

SGP.02 was published in 2013 (years before the first eSIM iPhone shipped in 2018. When the GSMA started designing remote SIM provisioning in the early 2010s, nobody was thinking about smartphones. They were thinking about smart meters in basements, connected cars on highways, and industrial sensors in oil fields. Consumer eSIM) the one you scan with your phone, came *after* the robot network was already designed and deployed. The machines got there first.

---

*Kid-friendly version, Cross-specification comparison of SGP.02, SGP.22, and SGP.32*

← [Back to Kids Articles](index)
