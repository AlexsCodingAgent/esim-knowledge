---
title: "Mission Orders: How Robots Get New Instructions"
date: 2026-06-07
---

# Mission Orders: How Robots Get New Instructions

Picture a diplomatic courier walking into a secure facility. They're carrying a sealed pouch, classified documents destined for a specific vault. The courier verified their identity at three checkpoints. The pouch was locked at the embassy. Nobody along the route could open it. And before anyone accepts delivery, the receiving vault runs its own authentication: *"Prove you're the real courier, and prove that pouch hasn't been tampered with."*

That's profile download in SGP.02. It's the most security-sensitive operation in the entire spec, and it unfolds in four carefully choreographed phases.

---

## Phase 1: Preparing the vault

You can't store secrets in thin air. First, you need a secure room.

The Fleet Owner calls the Key Factory: "Robot #8721 needs Network B access." Before the Key Factory does anything, it runs the background checks:

- **Who is this robot?** The Key Factory asks the Commander for the robot's information sheet (the EIS).
- **Is it genuine?** The robot's certificate is verified against the Chip Builder and the central Certificate Issuer (CI). Fake chips get caught right here.
- **Does it have room?** Memory check. Enough free profile slots?
- **Is it certified?** The robot must pass compliance validation.

If everything clears, the Key Factory tells the Commander: "Create a new profile vault in robot #8721." The Commander radios the robot, the robot carves out a new **ISD-P** (profile room), and it sits empty, state: **SELECTABLE**. Ready for furnishing.

---

## Phase 2: The handshake that can't be faked

Now the Key Factory and the robot need to agree on a shared secret, with the Commander (the courier) relaying every message, *and* with anyone potentially listening in.

| Step | What happens |
|---|---|
| 1 | Key Factory sends its ID badge to the robot |
| 2 | Robot's secure vault checks: "Is this badge signed by the CI? Yes, trusted." |
| 3 | Robot generates a **fresh random challenge** : a number that's never been used before |
| 4 | Key Factory signs the challenge with its private key. This proves: "I am the real Key Factory, right now, not a recording." |
| 5 | Key Factory also generates a **one-time key pair** : used once, then discarded |
| 6 | Robot and Key Factory each compute the same **Shared Secret** independently, without ever sending it over the wire |
| 7 | From this secret, both sides derive the **SCP03 session keys** for the actual data encryption |
| 8 | **Receipt check:** Robot proves it derived the right keys; Key Factory confirms |

The math behind step 6 is called **ECKA-EG** (Elliptic Curve Key Agreement). It's the cryptographic magic that lets two strangers (connected only by an untrusted courier) arrive at identical secret keys without an eavesdropper being able to reconstruct them. The one-time keys in step 5 provide **forward secrecy**: even if someone steals the robot's private key years later, yesterday's handshake remains unbreakable.

The random challenge in step 3 is a clever anti-replay trick. The robot generates a fresh random number every single time. The Key Factory must sign it. Even if an attacker recorded yesterday's entire conversation, they can't replay it today, yesterday's challenge won't match today's.

---

## Phase 3: The sealed pouch

Now the real delivery. The profile is a package containing everything the robot needs to operate on a new network:

- **MNO-SD** : A mini-office for the network operator to manage the robot directly later
- **Network keys (NAA)** : USIM/ISIM credentials: the IMSI, authentication secrets, everything that says "this robot belongs on this network"
- **File system** : Phonebook entries, SMS storage, network configuration
- **Apps** : Optional payment applets or operator tools
- **POL1 rulebook** : The rules governing what can happen to this profile (can it be deleted? disabled? and when?)

The Key Factory wraps the entire package in **SCP03t** encryption (a special variant for profile transport) and sends it in chunks through the Commander's relay. The Commander sees only scrambled bytes: the courier, as promised, never gets to peek inside.

---

## Phase 4: Going live (or not)

If the Fleet Owner wants the profile active immediately, the Commander sends an enable command. Otherwise, the profile sits in **DISABLED** state, waiting for a future signal.

When enabled, the robot fires a REFRESH (essentially a soft reboot) and attaches to the new network.

---

## When things go sideways

- **Key check fails?** Download stops cold. Robot not trusted.
- **Connection drops mid-delivery?** Cleanup routine deletes the half-built vault: no orphaned rooms.
- **Profile already partly present?** Cleanup detects the old attempt, wipes it, starts fresh.
- **POL1 says "never delete me"?** Even cleanup respects the rulebook, some profiles are permanent.

---

## How this differs from your phone

When you scan a QR code to add an eSIM to your phone (that's SGP.22, the consumer spec), *you* trigger the download. Your phone's LPA handles the room creation. The key agreement is similar in concept (ECDH instead of ECKA-EG), but the delivery path is fundamentally different, end-to-end encrypted directly to your phone.

In the M2M world, you can't scan a QR code on a sealed smart meter in a basement. The Fleet Owner orders the download. The Commander builds the room remotely. The delivery tunnels through the Commander's radio channel. And after download, the profile waits in DISABLED state, nobody's tapping a screen to activate it.

---

## So why all the ceremony?

Because in M2M, you can't walk over and check the robot. You can't reboot it with a paperclip. You can't type in a PIN. The cryptographic handshake in Phase 2 is doing the work of every identity check a human would do in person, and it has to work perfectly, every time, over a radio link that might drop.

Think about that the next time you scan an eSIM QR code. Your phone is doing a version of this dance too, just a lot faster, with a screen to show you errors, and without a diplomatic courier in the middle.

---

*Kid-friendly version of GSMA SGP.02 v4.2 §3.1, Profile Download and Installation*

← [Back to Kids Articles](index)
