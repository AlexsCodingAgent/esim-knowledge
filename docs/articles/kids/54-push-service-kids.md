---
description: "How the Push Service stops phones from endlessly checking the Post Office: a magic doorbell that rings your device instantly when a new eSIM delivery is waiting."
title: "Push Service: The Magic Doorbell"
date: 2026-06-07
---

# The Magic Doorbell: No More Checking the Mailbox 🔔

## Imagine...

You're expecting an important letter. But instead of a postman who rings your doorbell, you have to **walk to the Post Office every 15 minutes** and ask: "Do you have anything for me?" Most trips, the answer is "Nope, nothing." You waste time, energy, and shoe leather: and when a letter *does* arrive, you might not know for another 14 minutes.

That's how old eSIM phones (v2.x) found out about new secret keys. The **Push Service** in v3.x changes everything: it's like the Post Office finally installing a **magic doorbell** on your phone!

---

## The Old Way: Polling (Walking to the Post Office) 🚶

In v2.x, the Phone's Assistant would periodically connect to the Post Office (the SM-DS):

1. Open a secure connection to the Post Office
2. Show its ID badge (authentication)
3. Ask: "Any secret key deliveries waiting for me?"
4. If no → close the connection and wait for the next walk
5. If yes → collect the delivery notice

This happened over and over, even when nothing was waiting: like checking an empty mailbox every 15 minutes, forever.

---

## The New Way: Push (The Magic Doorbell) 🔔

v3.x gives the Post Office a **magic doorbell system**:

1. Your phone gives the Post Office a special **Push Token** : like giving them your doorbell's unique ring code
2. The Post Office stores it alongside your phone's ID
3. When a new delivery arrives **for you**...
4. The Post Office presses **your specific doorbell** (via a push server)
5. Your phone hears the ding-dong and immediately goes to collect

No wasted walks. No wasted battery. Instant notification!

---

## How the Doorbell Gets Set Up 🛠️

| Step | What Happens |
|---|---|
| **1. Advertisement** | The Post Office says: "I support these doorbell brands: Apple, Google, or carrier doorbells" |
| **2. Selection** | The Phone's Assistant picks one: "Great, my phone works with Google doorbells!" |
| **3. Token** | The phone generates a unique doorbell code (Push Token) just for the Post Office |
| **4. Registration** | The Phone's Assistant sends the code + the phone's ID to the Post Office |
| **5. Ready!** | The Post Office now knows exactly how to ring this phone's doorbell |

---

## Polling vs Push: The Showdown ⚡

| | Walking to the Post Office (v2.x) | Magic Doorbell (v3.x) |
|---|---|---|
| How you find out | You walk and ask | Post Office rings you |
| Speed | Up to 15 minutes late | Within seconds |
| Battery used | Wasted on empty trips | Only when a real delivery arrives |
| Data used | On every single walk | Only for actual deliveries |
| Post Office workload | Millions of empty "nope" answers | Only rings when something exists |

---

The Push Token is like your doorbell's secret ring pattern: it's unique to your phone, but it doesn't reveal your identity. And if the token expires (like batteries in a doorbell), your phone just registers a fresh one next time it checks in. The old polling method still works as a backup: push is an upgrade, not a replacement!

---

*Kid-friendly version of [Push Service]({{ site.baseurl }}/docs/articles/sgp22-v3/54-push-service)*

← [Back to Kids Articles](index)
