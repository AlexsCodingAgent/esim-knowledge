---
title: "eIM Configuration: Associating Remote Managers with Your eUICC"
date: 2026-06-02
---

# 📇 Adding Trusted Friends to Your Chip's Contact List

**Imagine...** you have a secret club treehouse. You keep a list of trusted friends who are allowed to send you messages. If someone not on the list tries to give you an order, you ignore them. IoT eSIM chips work the same way: they keep a **contact list of trusted remote managers** and only obey commands from people on that list!

---

## 🤝 Why Do We Need a Contact List?

On your phone, there's no permanent "who can manage me" list. Every time you download a profile, your phone checks certificates and decides to trust the source: but it doesn't remember them afterwards.

IoT devices can't do that. They're deployed in remote places: a wind turbine in the ocean, a sensor on a mountain: and they need to know **instantly** whether a command is from a trusted source, without calling home to check. So they store a trusted contact list right on the chip!

---

## 📋 What's on the Contact Card?

Each trusted manager (eIM) gets a **digital contact card** stored on the chip. It contains:

- **Name (eimId)** : who are you?
- **Public Key** 🔑 : your secret handshake for verifying signatures
- **Counter Value** 🧮 : the ticket number system to prevent replay attacks
- **Language (Protocol)** : do you speak HTTPS, CoAPS, or something else?
- **TLS Trust Anchor** 🔒 : how to encrypt the connection to you

---

## ✏️ Four Ways to Manage the Contact List

### ➕ Add a Friend : `addEim`
Add a new trusted manager to the list. The command includes all the contact card details. If this is the very first manager being added, a special bootstrap method is used: because before there's a trusted manager, there's nobody trusted to send the command! (Chicken-and-egg problem solved!)

### 🔄 Update a Friend : `updateEim`
Change a manager's details: maybe they got new keys, or they speak a new language now.

### ❌ Remove a Friend : `deleteEim`
Take a manager off the list. If you remove the last one, the chip goes back to "no trusted managers" state.

### 📜 List All Friends : `listEim`
Ask the chip "who's on your contact list?" and get the answer.

---

## 🧮 The Ticket Counter

Every time the manager sends a command, they include a ticket number that goes up by one. The chip remembers the last ticket number. If someone tries to replay an old command with an old ticket number, the chip says "sorry, already saw that one!" and rejects it.

When the ticket counter gets close to running out (it maxes at 8,388,607!), the manager is removed and re-added with a fresh counter.

---

## 🏭 Two Ways to Set Up the First Manager

### The Normal Way: Another Manager Does It
An already-trusted manager sends a signed command to add a new one. Simple!

### The Factory Way: Direct Setup
For the very first manager (when nobody is trusted yet), a special unsigned command is used during manufacturing. It's like the chip's "birth certificate" setup: done at the factory where the chip is made.

---

## 📋 In a Nutshell

- The chip stores a **contact list** of trusted remote managers
- Each contact card has a name, key, counter, and language preference
- Four operations: **add**, **update**, **delete**, **list**
- The **first manager** is added at the factory with a special bootstrap command

---

A single eSIM chip can trust *multiple* managers at once: so the company that made the device and the customer who bought it can both manage it, each with their own trusted spot on the list!

← [Back to Kids Articles](index)
