---
title: "How the Commander Talks to Robots: Secret Messages"
date: 2026-06-07
---

# How the Commander Talks to Robots: Secret Messages 📻

## Imagine...

You're the Robot Fleet Commander. Robot #8721 is sealed inside a smart meter in a basement 500 miles away. You need to send it a command: "Activate Network B now!" But there's no WiFi down there, and the robot has no screen. How does your message get through?

SGP.02 gives the Commander three different radio channels — plus a clever DNS phonebook — to reach every robot, no matter where it is.

---

## The Exclusive Radio Channel 🎙️

Here's the most important rule: **only the Commander can talk to the robots**. Not the Fleet Owner. Not the Key Factory. Only the Commander has the secret frequency.

This is called the **ES5 interface** — it's the Commander's exclusive OTA (Over-The-Air) channel. Every command, every key delivery, every status check goes through this channel.

---

## Three Ways to Send Messages 📬

### 📱 Channel 1: SMS (Short Text Messages)
Best for short commands. Like sending a text message: "Switch to Profile B" or "Enable Fall-Back."

- Fits in a few SMS messages
- Protected by SCP80 encryption (AES scrambling)
- Comes with a digital signature so the robot knows it's really from the Commander
- The robot sends back a "Proof of Receipt" — like a read receipt

### 🌐 Channel 2: HTTPS (Secure Internet Tunnel)
Best for big deliveries — especially downloading a whole new profile. 

- Starts with an SMS "wake-up call" from the Commander
- Robot opens a secure web tunnel using PSK-TLS (like HTTPS but with a pre-shared password instead of a certificate)
- The robot's password comes from the SCP81 keys already shared with the Commander
- Data streams in chunks — perfect for multi-megabyte profile packages

### 🔗 Channel 3: CAT_TP (Lightweight Radio)
Best for slow or unreliable networks — like 2G or places with spotty coverage.

- Uses the phone's built-in toolkit channel (BIP)
- Same SCP80 security as SMS
- Connection-oriented with flow control
- Great when TCP/HTTPS overhead would be too heavy

---

## The Secret Tunnel Trick 🚇

When the Key Factory needs to deliver secret keys to a robot, something clever happens:

```
Key Factory → Commander → Robot's Commander Office → Profile Room
   └── Secret Box (SCP03 encrypted) ──┘
```

The Key Factory puts the keys in a secret box (SCP03 encryption). The Commander carries the box to the robot but **cannot open it**. The Commander's Office inside the robot passes the box to the right Profile Room. Only the Profile Room has the key to open it.

This is called the **ES8 tunnel** — a secure message inside another secure message. The Commander is a trusted courier who can't peek inside!

---

## The DNS Phonebook 📖

What if the Commander moves to a new address? Robots can use **DNS** — like a phonebook — to look up the Commander's current IP address from a domain name.

- Commander sends an SMS: "Call me at commander.example.com"
- Robot checks its DNS phonebook
- Gets the current IP address
- Opens the secure tunnel to that address

This means robots don't need hardcoded IP addresses burned into them at the factory — they can find the Commander wherever it moves.

---

## Transport Protocol Comparison

| Transport | Best For | Security | Overhead |
|---|---|---|---|
| SMS | Short commands | SCP80 | Very low |
| HTTPS + PSK-TLS | Profile download, bulk data | SCP80 + TLS | Medium |
| CAT_TP | Slow/unreliable networks | SCP80 | Low |

---

## 🧠 Did You Know?

The Commander doesn't use normal website certificates (like your browser does) for HTTPS. Instead, it uses **PSK-TLS** (Pre-Shared Key TLS) — both the robot and Commander already share a secret password (from the SCP81 keys), so they don't need certificates at all! This makes the handshake much simpler for the tiny chip.

---

*Kid-friendly version of GSMA SGP.02 v4.2 §2.4–2.8 — OTA Communication*

← [Back to Kids Articles](index)
