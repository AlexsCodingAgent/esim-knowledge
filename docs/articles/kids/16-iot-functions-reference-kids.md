---
title: "IoT eSIM Functions Reference: ESipa, ES9+', ES11', ESep"
date: 2026-06-07
---

# 🦸 The Superpower Menu for IoT eSIM

**Imagine...** you have a superhero utility belt with different gadgets for different missions. Need to send a command to a device? Gadget #1. Need to check for waiting profiles? Gadget #2. Need to download a profile? Gadget #3. The IoT eSIM system has its own utility belt — four special interfaces, each with its own set of superpowers!

---

## 📡 ESipa — The Main Superhighway

This is the busiest, most important bridge — connecting the **remote control centre (eIM)** to the **device translator (IPA)**. It carries:

### 📦 `TransferEimPackage` / `ProvideEimPackageResult`
The command delivery and result pickup service. Translator asks "got any commands for me?" or says "here's what happened with your last command!"

### 🔄 `IpaEuiccDataRequest` / `IpaEuiccDataResponse`
The heartbeat! Control centre asks "what's your status?" and the translator responds with everything: current profiles, pending notifications, certificates, and capabilities.

### 🎯 `ProfileDownloadTrigger`
"Hey device — go download this profile!" Pushes a secret activation code so the device can fetch its new permission slip.

### 📢 `HandleNotification`
Delivers report cards (notifications) from the chip to the control centre.

### 🌉 Indirect Download Relay
When the device can't talk to the profile factory directly, this gadget relays all the messages through the control centre.

---

## 🏭 ES9+' — The Factory Hotline

A direct line from the control centre to the **profile factory (SM-DP+)**. Used only in Indirect Download mode, when the control centre handles profile fetching on behalf of the device.

Its gadgets mirror the consumer version — authenticate, download bound profiles, cancel sessions — but they're called by the control centre instead of the device.

---

## 📮 ES11' — The Message Board Checker

A direct line from the control centre to the **message board (SM-DS)**. Used when the control centre checks for waiting profiles on behalf of sleepy devices.

The control centre authenticates with the message board, retrieves any waiting notes, and forwards them to the device. The device never touches the message board directly — saving precious battery!

---

## 🔐 ESep — The Secret Tunnel

This one is special — it's not a real separate connection. It's a **logical tunnel** inside the main highway (ESipa). Commands travel through it wrapped in two layers of digital signatures:

- **Outer signature**: from the control centre — proves who sent it
- **Inner signature**: from the chip — proves who executed it

The four gadgets inside this tunnel:
- **`EuiccPackageRequest`** — the signed command envelope
- **`EuiccPackageResult`** — the signed proof of execution
- **`EuiccMemoryReset`** — factory reset the whole chip
- **`ExecuteFallbackMechanism`** — "switch to your emergency parachute NOW!"

---

## 🔧 ES10b Extensions — New Gadgets for the Chip

SGP.32 also added eight new gadgets for talking directly to the eSIM chip:

| Gadget | What It Does |
|--------|-------------|
| `LoadEuiccPackage` | Feed a signed command envelope to the chip |
| `AddInitialEimConfiguration` | Set up the first trusted manager (factory bootstrap) |
| `GetEimConfigurationData` | Read the contact list |
| `DeleteAllEimConfigurationData` | Wipe the contact list clean |
| `ProfileRollback` | Undo the last profile change |
| `ImmediateEnable` | Activate a just-downloaded profile instantly |
| `ConfigureImmediateEnable` | Pre-approve instant activation for future downloads |
| `ExecuteFallbackMechanism` | Trigger the emergency parachute |

---

## 🌐 How Everything Connects

| Bridge | Transport | Security |
|--------|-----------|----------|
| **ESipa** | HTTP or CoAP or MQTT | Signed packages + encryption |
| **ES9+'** | HTTP | Certificate-authenticated encryption |
| **ES11'** | HTTP | Certificate-authenticated encryption |
| **ESep** | Inside ESipa | Double-signed (eIM + eUICC) |

---

## 📋 In a Nutshell

- **ESipa** is the main highway — commands, data, notifications, downloads
- **ES9+'** is the factory hotline for server-side profile downloads
- **ES11'** is the message board checker for sleepy devices
- **ESep** is the secret double-signed tunnel inside ESipa
- Eight new **ES10b gadgets** extend chip-level operations for IoT

---

🧠 **Did You Know?** Even though ESep is a "logical" interface with no separate wires, it's arguably the most important one — every single remote management command travels through its double-signed tunnel, making it the backbone of IoT device security!

← [Back to Kids Articles](index)
