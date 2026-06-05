---
title: "IoT Device Initialisation and the eUICC File Structure"
date: 2026-06-04
---

# 🌅 The Morning Routine of an IoT Device

**Imagine...** you wake up in the morning. What do you do? You stretch, check your phone, see what's on your schedule, and get ready for the day. IoT devices have a **morning routine** too — except theirs happens every time they power on, and it all takes place in milliseconds!

---

## ⏰ The Six-Step Wake-Up

When an IoT device boots up (or wakes from a deep battery-saving sleep), here's what happens:

### 1. ⚡ Power On!
The eSIM chip's tiny operating system boots up. The main manager (ISD-R) wakes up and takes charge.

### 2. 🔍 Profile Discovery
The manager checks: "What profiles do I have? Which ones are enabled? Which are disabled?"

### 3. 🎯 Manager Selection
The device selects the chip's manager by its ID number (AID) — like calling a specific person in a busy office.

### 4. 🤖 Translator Activation
The translator (IPA) wakes up too. If it lives inside the chip (IPAe), it starts running there. If it lives in the device (IPAd), it boots separately.

### 5. 📇 Contact List Check
The translator reads the chip's **contact list** (eIM Configuration Data): "Who are my trusted remote managers?"

### 6. 📡 Connectivity Check
If there's an enabled profile, the modem tries to connect to the network. Can it reach the internet? Great! If not... time for the parachute.

---

## 🗂️ The Chip's Filing Cabinet

The eSIM chip has a tiny filing cabinet of important files:

| File | What's Inside |
|------|--------------|
| **EF.DIR** | Directory of all apps on the chip |
| **EF.ICCID** | The chip's serial number |
| **EF.EID** | The chip's unique 32-digit ID |
| **EF.EIMCFG** | Contact list of trusted managers ✨ *new for IoT!* |
| **EF.NOTIF** | Pending report cards waiting to be delivered ✨ *new for IoT!* |
| **EF.SMDP** | Address of the default profile factory |
| **EF.SMDS** | Address of the message board server |

---

## 🪂 The Parachute Check

During boot, the chip also checks: "Do I have a Fallback Profile?" If no normal profile works, the chip can automatically switch to this emergency backup profile. It's like checking your parachute before you jump — you hope you never need it, but you're glad it's there!

The fallback profile is usually a basic one from the device manufacturer — just enough connectivity to call for help, not for normal operations.

---

## 🏷️ Telling the Control Centre Who You Are

Once connected, the device sends a **DeviceInfo** card to the control centre:

- "Here's my model number!"
- "I'm an IPAd" (or "I'm an IPAe")
- "I speak HTTPS, CoAP, and MQTT"
- "Here's what I can do!"

The control centre uses this card to decide how to talk to this specific device. A tiny sensor gets gentle, lightweight messages — a powerful gateway gets richer commands.

---

## 📋 In a Nutshell

- Devices have a **six-step morning routine** every time they power on
- The chip has a **filing cabinet** with important information stored in it
- Two new files (EIMCFG and NOTIF) were added just for IoT
- The **Fallback Profile** is checked during boot as a safety net
- The device sends a **DeviceInfo card** so the control centre knows what it can handle

---

🧠 **Did You Know?** The eSIM chip's unique ID (EID) is 32 digits long — that's enough numbers to give a unique ID to every single grain of sand on Earth... many times over!
