---
description: "The notification system that lets IoT eSIM chips send report cards to their remote control centre — bundling status updates to save battery, plus error handling with an automatic undo feature."
title: "Notifications and Error Handling in IoT eSIM"
date: 2026-06-03
---

# 📢 Report Cards and Oops Messages

**Imagine...** you're a teacher managing 1,000 students in different classrooms. When a student finishes a task or runs into trouble, you need to know: fast! You don't have time to check on every student yourself, so they send you **report cards**. IoT eSIM uses the exact same system: devices send report cards (notifications) and oops messages (errors) to the remote control centre.

---

## 📬 The Notification System: Your Device's Report Card

Whenever something important happens on the eSIM chip, it creates a **notification** : like a little postcard saying what changed:

- ✅ **"Profile Enabled!"** : a new SIM profile is active
- ⏸️ **"Profile Disabled!"** : a profile was turned off
- 🗑️ **"Profile Deleted!"** : a profile was permanently removed
- 📥 **"Profile Installed!"** : new profile successfully downloaded
- ❌ **"Oops! Something went wrong!"** : a download failed

---

## 🚚 How Notifications Travel

The journey of a notification:

1. **Chip creates it** : something changed!
2. **Translator (IPA) picks it up** : "hey, there's a postcard waiting"
3. **Translator delivers it** : sends it to the control centre and the profile factory
4. **Receivers acknowledge** : "got it, thanks!"
5. **Cleanup** : chip removes the delivered notification

---

## 📦 Saving Battery Power

Sending messages uses precious battery on tiny sensors. So the system has a clever trick: **bundling**. Instead of sending notifications one at a time, the translator waits and sends them all together: like putting multiple postcards in one envelope. One transmission, many messages!

---

## 🚨 Three Levels of Oops

When things go wrong, errors come in three flavours:

### Level 1: Translator Errors
The translator spots a problem before it even reaches the chip: like a badly formatted message or an emergency call in progress.

### Level 2: Package Errors
The chip rejects the whole command package: maybe the signature didn't match or the counter was too low.

### Level 3: Individual Command Errors
The package was fine, but one specific command inside it failed: like "enable this profile" when the profile doesn't exist.

---

## ⏪ The Undo Button: Profile Rollback

Here's a clever safety feature: imagine the translator executes a command (like "switch to profile B"), but then **loses connection** before it can report the result to the control centre. Now nobody knows what happened!

The fix? **Profile Rollback** : the translator tells the chip "oops, undo that last thing." The chip reverts to its previous state, and everyone can start fresh.

---

## 🚑 Emergency Calls Take Priority

If a device is making an emergency call (like eCall in a car after an accident), ALL eSIM operations are **immediately blocked**. Nothing is allowed to interrupt an emergency: the system returns an error called `ecallActive` which means "busy saving lives, try later!"

---

## 📋 In a Nutshell

- **Notifications** are report cards for every profile change
- They travel from chip → translator → control centre
- **Bundling** saves battery by sending multiple messages at once
- Three **error levels** help diagnose what went wrong
- **Rollback** is the undo button for lost connections

---

When you make an emergency call on an eSIM device, the chip blocks *every single management operation* until you hang up: just to make absolutely sure nothing interrupts your call for help!

← [Back to Kids Articles](index)
