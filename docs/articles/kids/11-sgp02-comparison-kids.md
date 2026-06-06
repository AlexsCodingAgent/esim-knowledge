---
title: "Three Kinds of eSIM: Phones, Robots, and the Future"
date: 2026-06-07
---

# Three Kinds of eSIM: Phones, Robots, and the Future 📱🤖🔮

## Imagine...

Three different devices need an eSIM: a smartphone in your pocket, a smart meter in a basement, and a soil sensor in a farm field. They all use the same tiny vault chip (eUICC) — but how they get their keys couldn't be more different.

The GSMA created three separate specifications, each designed for a different kind of device. Let's meet them all!

---

## The eSIM Family 👨‍👩‍👧

| | SGP.02 "The Robot Network" | SGP.22 "The Phone System" | SGP.32 "The Future IoT" |
|---|---|---|---|
| **Nickname** | M2M Push | Consumer Pull | IoT Pull |
| **Born** | 2013 (Original!) | 2015 | 2023 |
| **For** | Robots, meters, cars | Phones, tablets, watches | Sensors, trackers, smart home |
| **How keys arrive** | Commander PUSHES | Phone PULLS (QR code) | Phone PULLS or Manager triggers |
| **Who decides?** | Fleet Owner (Operator) | You, the user | You or the eIM (IoT Manager) |

---

## How Each System Delivers Keys 🗝️

### SGP.02 — The Commander Pushes
```
Fleet Owner: "Switch to Network B!"
      ↓
   Commander pushes command via radio
      ↓
   Robot: "Yes, Commander!"
```
**No human involved. No screen. No scan. The Commander is always in charge.**

### SGP.22 — The Phone Pulls
```
You: *scan QR code*
      ↓
   Phone: "Key Maker, give me my key!"
      ↓
   Key Maker: "Here you go!"
```
**You decide. You scan. You tap "Install." The phone drives everything.**

### SGP.32 — Best of Both Worlds
```
eIM: "Sensor #5001 needs new keys, please trigger download"
      ↓
   Sensor checks in: "Got the message! Downloading now..."
      ↓
   Or: You use an app to start the download
```
**Either the device pulls, or the IoT Manager nudges it — flexible!**

---

## Architecture Comparison 🏗️

| Feature | SGP.02 (Robots) | SGP.22 (Phones) | SGP.32 (IoT) |
|---|---|---|---|
| **Server roles** | SM-DP + SM-SR (split) | SM-DP+ (combined) | SM-DP+ (combined) |
| **Device helper** | None (ISD-R passive) | LPA app on phone | IPA (lightweight LPA) |
| **Fleet manager** | Operator via ES4 | Not built-in | eIM (IoT Manager) |
| **Discovery** | Not needed (push) | SM-DS post office | SM-DS or eIM |
| **OTA channel owner** | Commander (SM-SR) | Key Maker (SM-DP+) | Key Maker (SM-DP+) |
| **User interface** | Headless — none | Full screen, QR codes | Minimal or none |
| **Key agreement** | ECKA-EG (ElGamal) | ECDH | ECDH (shared) |
| **Spec pages** | 452 pages | ~296 pages | Evolving |

---

## Which One Should You Use? 🤔

| Scenario | Use This |
|---|---|
| Smartphone, tablet, smartwatch | **SGP.22** — users expect QR codes and touch screens |
| Car telematics with eCall | **SGP.02** — designed for automotive, 10+ year life |
| Utility meter sealed for 15 years | **SGP.02** — truly unreachable, push model essential |
| Asset tracker on a shipping container | **SGP.32** — checks in periodically, large fleets |
| Smart home sensor (new project) | **SGP.32** — modern, flexible, reuses consumer servers |
| Industrial sensor in a mine | **SGP.02** — harsh environment, no regular connectivity |
| Agricultural soil sensor grid | **SGP.32** — gateway model handles constrained sensors |

---

## The Push vs Pull Decision Tree 🌳

```
Is there a human with a screen?
    │
    ├── YES ──▶ SGP.22 (Consumer)
    │
    └── NO ──▶ Is the device reachable over IP?
                   │
                   ├── YES, periodically ──▶ SGP.32 (IoT)
                   │
                   └── NO, truly unreachable ──▶ SGP.02 (M2M Push)
```

---

## Why SGP.02 Still Matters in 2026 ⏳

Even though it's the oldest spec, SGP.02 is far from obsolete:

- 🚗 **Automotive**: 10+ year head start in connected cars with regulatory requirements
- ⚡ **Utility meters**: Devices installed in 2018 still running SGP.02 today
- 🏭 **Industrial**: Sealed sensors in harsh environments where physical access is impossible
- 📜 **Legislation**: Some regulations specifically reference SGP.02

The M2M world moves slowly — and SGP.02 was designed for exactly that reality.

---

## The Good News: They Can Coexist! 🤝

An eUICC chip can potentially support multiple specs. An operator can run SGP.02 for its automotive fleet, SGP.22 for its consumer subscribers, and SGP.32 for its smart home devices — all from the same core network.

---

## 🧠 Did You Know?

SGP.02 was created before the iPhone had eSIM! When the GSMA started designing remote SIM provisioning in the early 2010s, they weren't thinking about smartphones at all — they were thinking about smart meters, connected cars, and industrial sensors. Consumer eSIM (SGP.22) came *after* the robot network was already designed.

---

*Kid-friendly version — Cross-specification comparison of SGP.02, SGP.22, and SGP.32*

← [Back to Kids Articles](index)
