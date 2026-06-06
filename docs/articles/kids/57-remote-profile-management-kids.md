---
title: "RPM: The Remote Control for Your Secret Keys"
date: 2026-06-07
---

# The Remote Control for Your Secret Keys 🎮

## Imagine...

You have a garage full of cars. In the old days, if you wanted to start a car, lock a car, or check a car's fuel level, you had to **physically walk to each car** and use the key. What if your car company could send you a remote control that lets them start, stop, or check your cars from their office — with your permission, of course?

That's exactly what **Remote Profile Management (RPM)** does for your phone's secret keys. It's the remote control that lets your mobile company manage your eSIM profiles without you ever touching the screen — but always with your approval!

---

## Before RPM: Local Management Only 🚶

In v2.x, if your mobile company needed to make a change to your secret key:

- **Enable a profile?** Only you could do it, by tapping your phone
- **Disable a profile?** Only you
- **Delete a profile?** Only you
- **Update a profile's name?** Only you

The mobile company was basically locked out of its own keys once they were in your phone — like giving someone a car key and never being able to check if the car is still running!

---

## With RPM: The Remote Control 🎮

RPM gives your mobile company a control panel with six buttons:

| Command | What It Does |
|---|---|
| **Enable** | "Switch on the Home key" — activates a specific profile |
| **Disable** | "Switch off the Work key" — deactivates a profile |
| **Delete** | "Remove the Travel key entirely" — wipes a profile from the vault |
| **ListProfileInfo** | "Show me all the keys in the vault" — checks what's installed |
| **UpdateMetadata** | "Rename the key to 'My Awesome Plan'" — changes the label |
| **Contact PCMP** | "Open the workshop so we can update what's inside the key" |

---

## The Three-Act Play 🎭

RPM happens in three phases, like a well-rehearsed theatre performance:

### Act 1: Initiation 🎬
The mobile company calls the Key Maker and says: "Please prepare a Remote Command package for this phone." The Key Maker creates an **RPM Package** — a bundle of commands wrapped in a secure envelope — and registers an event with the Post Office.

### Act 2: Download 📥
The Phone's Assistant discovers the waiting package (via the Post Office, the Magic Doorbell, or directly). Before even opening it, the Assistant checks: "Do any of these commands break the security rules?" Then it asks **you**: "Your mobile company wants to do these things. Is that OK?"

### Act 3: Execution ⚡
If you say yes, the Assistant delivers the package to the Magic Vault Chip. The chip processes each command one by one, like a careful chef following a recipe. Results fly back to the mobile company — "Enable: done! Disable: done! Update name: done!"

---

## Your Permission Matters! ✋

Here's the most important rule: **RPM always requires your consent**. Before any remote command runs, your phone's Assistant must:

1. Check that no security rules forbid the operation
2. Show you clearly what's about to happen
3. Ask for your confirmation

You can always say "No thanks!" — and if you do, the entire package is cancelled. Nobody can force changes onto your phone without you knowing.

---

## Local vs Remote: Side by Side 📊

| | Local Management (v2.x) | Remote Management (v3.x) |
|---|---|---|
| Who starts it? | You tap the screen | Your mobile company sends a command |
| Commands available | Enable, Disable, Delete | Enable, Disable, Delete, List Info, Update Name, Contact Workshop |
| Do you approve? | Yes (you started it!) | Yes — still required! |
| What if a command fails? | Stop immediately | Can **continue** or stop (configurable) |
| Can commands be chained? | No | Yes — multiple packages linked together |

---

## 🧠 Did You Know?

Each RPM Package is limited to **1,057 bytes** — about the size of a short poem. If the mobile company needs to send more commands than fit, they can chain multiple packages using a "more coming!" flag (`rpmPending`). It's like sending a book in multiple letters, with "to be continued..." at the end of each one!

---

*Kid-friendly version of [Remote Profile Management]({{ site.baseurl }}/docs/articles/sgp22-v3/57-remote-profile-management)*

← [Back to Kids Articles](index)
