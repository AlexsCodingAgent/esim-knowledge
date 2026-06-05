---
title: "Profile State Management via the eIM: Remote Enable, Disable, Delete"
date: 2026-06-05
---

# 🎮 Remote Control for Your SIM Profiles

**Imagine...** you have a video game console with multiple game cartridges. On your phone, you physically swap SIM cards. But what if you had a magic remote control that could swap game cartridges from across the world — without touching the console? That's what **Profile State Management** does for IoT devices. A server on the other side of the planet can say "use this profile now!" and the chip just does it.

---

## 🪄 The Magic Pattern

Every remote profile operation follows the same recipe:

1. **Control centre writes a command** — "enable this profile!"
2. **Control centre signs it** — adds a secret digital signature proving it's genuine
3. **Sends it to the translator** — through the secure communication bridge
4. **Translator passes it to the chip** — "here's a signed command for you"
5. **Chip verifies the signature** — "yep, this is from someone I trust"
6. **Chip checks the counter** — "and this isn't a replay of an old command"
7. **Chip executes the command** — flips the profile switch!
8. **Chip creates a signed result** — "here's proof I did it"

---

## 🕹️ The Six Buttons on the Remote

### ✅ Enable — "Turn This Profile ON"
Makes a profile active. The chip first checks: is this profile currently disabled? Are the rules OK with enabling it? If yes — click! The profile switches on.

### ⏸️ Disable — "Turn This Profile OFF"
Deactivates a profile without deleting it. It stays on the chip, just sleeping. The chip checks: is it currently enabled? Are the rules OK?

### 🗑️ Delete — "Remove This Profile Forever"
Permanently removes a profile. The profile MUST be disabled first — you can't delete a profile that's currently active. That would be like pulling a game cartridge out while you're playing!

### ⏪ Rollback — "Undo That Last Change!"
If the translator loses connection after executing a command, it can tell the chip to undo everything. The chip reverts all profiles to their previous states, like pressing Ctrl+Z.

### 🏷️ Set Fallback — "Make This the Emergency Backup"
Tags a profile as the emergency parachute. Only disabled operational profiles can be tagged — and only one at a time.

### 🏷️ Unset Fallback — "Remove Emergency Backup Tag"
Removes the fallback tag from a profile.

---

## ⚡ Instant Activation — First Boot Magic

There's a special shortcut for brand-new devices. When a profile is downloaded for the very first time, the translator can say "enable this immediately!" without waiting for a separate command from the control centre. This is called **Immediate Profile Enabling** — one step instead of two, getting the device online faster.

---

## 🧮 Pre-Flight Checks Before Every Command

Before executing any command, the chip runs through a checklist:

- Does this profile exist? (by serial number or ID)
- Is it in the right state? (disabled before enabling, enabled before disabling)
- Do the **Profile Policy Rules** allow this? (some profiles have rules saying "never disable me!")
- Did the control centre's signature check out?

Only when all checks pass does the chip execute the command.

---

## 📋 In a Nutshell

- All profile commands follow an **8-step signed-package recipe**
- Six commands: **enable, disable, delete, rollback, set fallback, unset fallback**
- The chip runs **pre-flight checks** before every command
- **Immediate Profile Enabling** speeds up first-boot setup

---

🧠 **Did You Know?** A profile can have a rule saying "delete me after I'm disabled." So one disable command can actually trigger two actions — disable now, auto-delete afterwards. It's like a domino effect built into the profile itself!
