---
title: "The Secret Languages of eSIM: How the Helpers Talk"
date: 2026-06-05
---

# The Secret Languages of eSIM: How the Helpers Talk 🗣️

## Imagine...

You're at the United Nations, and everyone speaks a different language. The French delegate needs to talk to the Japanese delegate, who needs to talk to the Brazilian delegate. Somehow, through translators and agreed-upon formats, messages flow perfectly.

The eSIM world works the same way! Every helper speaks a different "language" : but they all follow the same rulebook so nothing gets lost in translation.

---

## The Four Language Families 🌐

### ES2+ : The Ordering Language 📋

This is how your **carrier** talks to the **Key Maker**. It's the simplest language: plain JSON (a human-readable format like a shopping list):

- "I'd like to order one key, please" → `DownloadOrder`
- "Here are the final details: make it!" → `ConfirmOrder`
- "Actually, cancel that order" → `CancelOrder`
- "How's the download going?" → `HandleNotification`

Think of ES2+ like email between business partners: polite, structured, and to the point.

### ES9+ : The Courier Language 📬

This is how your phone's **Assistant** talks to the **Key Maker** over the internet:

- "Here's my chip's challenge: who are you?" → `InitiateAuthentication`
- "Here's proof of who I am" → `AuthenticateClient`
- "Send me the encrypted key package!" → `GetBoundProfilePackage`

This language is also JSON, but it carries mysterious encrypted blobs the Assistant can't read. It's like a courier carrying sealed diplomatic pouches.

### ES8+ : The Secret Tunnel Language 🔐

This is the most special language of all. It's how the **Key Maker** speaks directly to your **Vault chip**, through the Assistant (who just passes the sealed messages along).

ES8+ commands are wrapped in multiple layers of encryption using something called **SCP03t**. Every message is:
- Encrypted (can't be read by snoops)
- Signed (can't be tampered with)
- Chained (can't be replayed out of order)

Key Maker commands include:
- "Let's establish our secret tunnel" → `InitialiseSecureChannel`
- "Create a new locked box" → `ConfigureISDP`
- "Here's the name tag for this profile" → `StoreMetadata`
- "Here come the key pieces, chunk by chunk" → `LoadProfileElements`

### ES10x: The Chip-Whispering Language 💬

This is how the **Assistant** talks directly to the **Vault chip** inside your phone. It uses a format called **APDUs** (short command packets) over a physical connection:

- ES10a : "What's your name? What addresses do you know?" (discovery)
- ES10b : "Let's download a profile!" (11 different commands for the full download dance)
- ES10c : "Switch profiles! Delete that one! Rename this one!" (7 management commands)

---

## The Golden Rule: Every Message Gets a Ticket 🎫

Every single message in the eSIM system carries a **functionCallIdentifier** : a unique ticket number. This is brilliant because:

- If a message gets lost, you can safely resend it with the same ticket number
- The receiver knows "I already handled ticket #1234" : no double-charging!
- You can trace any problem back to exactly which message caused it

---

## The Post Office Pattern 📮

The **Notifier** (SM-DS) adds a clever twist: it decouples "making a key" from "picking up a key." The Key Maker can create your profile on Monday, drop a note at the post office, and your phone can discover it on Friday.

Your phone doesn't need to be constantly connected: it just checks the post office every so often. This is called **event-driven architecture** and it's what makes eSIM work even on devices that aren't always online.

---

The ES8+ encrypted messages travel through your phone's Assistant app: but the app literally cannot read them. The encryption is end-to-end between the Key Maker's server and your phone's secure chip. Even if the Assistant app was hacked by a villain, they'd see nothing but digital gibberish!

---

*Kid-friendly version of GSMA SGP.22, Sections 5 and 6: Functions and Interface Binding*

← [Back to Kids Articles](index)
