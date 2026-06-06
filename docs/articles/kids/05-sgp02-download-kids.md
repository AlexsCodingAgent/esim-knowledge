---
title: "Mission Orders: How Robots Get New Instructions"
date: 2026-06-07
---

# Mission Orders: How Robots Get New Instructions 📦

## Imagine...

The Fleet Owner calls the Key Factory: "Robot #8721 needs Network B keys!" The Key Factory springs into action. But before delivering anything, they need to check: is Robot #8721 really who it claims to be? Can we trust it? And how do we get the keys there without anyone — not even the Commander — seeing them?

This is **Profile Download** — the most security-critical operation in SGP.02. It happens in four careful phases.

---

## Phase 1: Building the Room 🏗️

Before you can store keys, you need a room to put them in.

1. **Fleet Owner calls Key Factory**: "Download new profile for robot #8721"
2. **Key Factory asks Commander**: "Tell me everything about robot #8721" (the EIS)
3. **Key Factory checks**: Is this robot genuine? Enough memory? Certified? **Verifies the robot's certificate against the Chip Builder and CI.**
4. **Key Factory tells Commander**: "Create a new profile room for robot #8721"
5. **Commander radios the robot**: "Build a new ISD-P room!"
6. Room created — empty, waiting for keys. State: **SELECTABLE**.

---

## Phase 2: The Secret Handshake 🤝

Now the Key Factory and robot need to agree on a secret code without anyone overhearing.

| Step | Who Does What |
|---|---|
| 1 | Key Factory sends its ID badge to the robot |
| 2 | Robot's vault checks: "Is this badge signed by the CI? Yes!" |
| 3 | Robot generates a **random challenge** — a fresh secret number |
| 4 | Key Factory signs the challenge with its private key — proving "I'm the real Key Factory!" |
| 5 | Key Factory also generates a **one-time key pair** — used once and thrown away |
| 6 | Robot and Key Factory each compute the same **Shared Secret** — without ever sending it |
| 7 | From this secret, they both derive the **SCP03 session keys** |
| 8 | **Receipt:** Robot proves it got the right keys; Key Factory verifies |

This magical math is called **ECKA-EG** (Elliptic Curve Key Agreement). Both sides end up with identical keys, but nobody listening in can figure them out. The one-time keys provide **forward secrecy** — even if the robot's private key is stolen years later, old sessions can't be decrypted.

---

## Phase 3: Delivering the Package 📦

Now the real delivery begins. The profile is an encrypted package containing:

- **MNO-SD**: The operator's mini-office for future direct contact
- **Network keys (NAA)**: USIM/ISIM with IMSI and authentication secrets
- **File system**: Phonebook, SMS storage, network settings
- **Apps**: Optional payment applets or operator tools
- **POL1 Rulebook**: Rules about what can happen to this profile

The Key Factory wraps it all in **SCP03t** encryption (a special variant for profile transport) and sends it in chunks through the Commander's radio channel. The Commander relays the chunks but sees only scrambled data.

---

## Phase 4: Going Live (Optional) ✅

If the Fleet Owner wants the new profile active right away, the Commander sends an enable command. Otherwise, the profile sits in **DISABLED** state, ready for later activation.

When enabled, the robot sends a REFRESH signal — like a reboot — and attaches to the new network.

---

## If Something Goes Wrong... 🩹

| Problem | Solution |
|---|---|
| Key check fails | Download stops immediately — robot not trusted |
| Connection drops mid-download | Cleanup routine deletes the half-built room |
| Profile already partly downloaded | Cleanup checks first, deletes old attempt, starts fresh |
| POL1 says "never delete me" | Even cleanup can't override the rulebook |

---

## Profile Download vs Consumer Download

| Feature | Consumer (SGP.22) | M2M Robots (SGP.02) |
|---|---|---|
| Who triggers it? | User scans QR code | Fleet Owner orders it |
| Creation of room | LPA on phone | Commander via radio |
| Key agreement | ECDH (similar) | ECKA-EG with Scenario#3 |
| Delivery tunnel | ES8+ end-to-end | SCP03t through Commander relay |
| After download | Ready to use via LUI | Disabled — wait for enable command |

---

## 🧠 Did You Know?

The random challenge in Phase 2 is a clever anti-replay trick. The robot generates a fresh random number every time. The Key Factory must sign it. Even if an attacker recorded yesterday's entire conversation, they can't replay it today — yesterday's challenge won't match today's!

---

*Kid-friendly version of GSMA SGP.02 v4.2 §3.1 — Profile Download and Installation*

← [Back to Kids Articles](index)
