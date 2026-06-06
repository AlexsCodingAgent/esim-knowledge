---
title: "How the Commander Talks to Robots: Secret Messages"
date: 2026-06-07
---

# How the Commander Talks to Robots: Secret Messages

Here's a puzzle.

You're sitting in Mission Control. Deep in space, millions of kilometers away, a probe named ESP-8721 orbits a distant asteroid. It has no screen, no keyboard, and the nearest WiFi router is... let's just say it's not nearby. You need to tell this probe: "Switch to Backup Network B, now!"

How does your command get there?

SGP.02 gives Mission Control three different transmission bands (plus a clever interstellar phonebook) so no probe is ever out of reach.

---

## Your private channel to every probe

First rule of the fleet: **only Mission Control gets to talk to the probes.** Not the Fleet Owner. Not the Key Factory. Nobody else has the frequency.

The spec calls this the **ES5 interface** : Mission Control's exclusive Over-The-Air channel. Every command, every key delivery, every status ping travels through this one pipeline.

---

## Three ways to reach the void

Different situations call for different signals.

### SMS: the short-burst transmitter

Perfect for quick orders. Think of it as a text message in space: "Activate Profile B" or "Engage Fall-Back."

- Fits in just a few SMS payloads
- Scrambled with SCP80 encryption (AES: the same math your banking app uses)
- Digitally signed so the probe knows it's really Mission Control calling
- The probe pings back a "Proof of Receipt" : like a read receipt from deep space

### HTTPS: the high-bandwidth laser link

When you need to beam down something big (like an entire new profile package) you don't use SMS. You open a secure data tunnel.

- Mission Control sends a short SMS "wake-up call"
- The probe opens an encrypted web tunnel using **PSK-TLS** (like HTTPS, but instead of certificates, both sides already share a secret password from their SCP81 keys)
- Data streams in chunks, perfect for multi-megabyte profile downloads

No certificate authorities. No DNS validation dances. Just a pre-shared secret and go. Much simpler for a tiny chip with limited horsepower.

### CAT_TP: the reliable low-band comm

Sometimes you're on a probe with a weak signal, think 2G or spotty deep-space relay coverage. TCP would choke. CAT_TP doesn't.

- Uses the phone's built-in toolkit channel (BIP)
- Same SCP80 security wrapping as SMS
- Connection-oriented with flow control built in
- Lightweight enough that even a rusty old 2G link can handle it

---

## The sealed-envelope trick

Here's where it gets clever. When the Key Factory needs to deliver secret keys to a probe, the keys can't travel in the open, not even Mission Control is allowed to see them.

So they pull a sealed-envelope maneuver:

```
Key Factory → Mission Control → Probe's Command Module → Profile Vault
                    └── Sealed Envelope (SCP03 encrypted) ──┘
```

The Key Factory locks the keys inside a cryptographic envelope (SCP03). Mission Control carries the envelope to the probe but **can't open it.** The probe's Command Module passes the envelope to the right Profile Vault. Only that vault has the key to break the seal.

The spec calls this the **ES8 tunnel** : a secure message riding inside another secure message. Mission Control is the trusted courier who never gets to peek inside.

---

## The cosmic phonebook

What happens if Mission Control moves to a new headquarters? Hardcoding IP addresses into every probe would be a disaster.

Instead, probes use **DNS** : a phonebook that maps names to addresses:

- Mission Control radios: "Reach me at `commander.example.com`"
- Probe checks its DNS phonebook
- Gets the current IP address
- Opens the secure tunnel to wherever Mission Control lives now

No factory-burned addresses. No dead links when infrastructure shifts. Probes can always find home.

---

## Which channel when?

- **SMS** → Short commands, tiny payload, almost zero overhead. "Switch to Profile B."
- **HTTPS + PSK-TLS** → Big downloads. Profile packages. Bulk data. Medium overhead, high throughput.
- **CAT_TP** → Unreliable links. 2G, fringe coverage, deep-fade zones. Low overhead, survives where TCP won't.

---

## One more thing

The HTTPS channel doesn't use normal website certificates. There's no Verisign in space. Instead, Mission Control and the probe already share a secret password (from the SCP81 key exchange), so they skip the whole certificate-authority dance. Faster handshake, fewer bytes, same security. The spec calls this **PSK-TLS**, and it's one of the smartest design choices in SGP.02.

---

*Kid-friendly version of GSMA SGP.02 v4.2 §2.4–2.8, OTA Communication*

← [Back to Kids Articles](index)
