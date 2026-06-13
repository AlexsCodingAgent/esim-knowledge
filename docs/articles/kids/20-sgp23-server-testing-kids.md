---
description: "Putting the Key Maker and Post Office servers through quality control: verifying order handling, secure profile delivery tubes, and the public-facing interfaces any phone can connect to."
title: "Testing the Key Maker and Post Office"
date: 2026-06-07
---

# Testing the Key Maker and Post Office 🏭📬

## Imagine...

You run a factory that makes custom keys, and a post office that tells people their packages are ready. Before customers trust you, you need to prove:

- You can take orders correctly
- Every key you make actually fits the right lock
- You deliver keys through a secure, unbreakable tube
- Your post office correctly tells people "you have mail!" and "never mind, it's been picked up"

This is what **SM-DP+ and SM-DS testing** does: it puts the server-side of the eSIM world through rigorous quality control.

---

## The Key Maker's Three Test Rooms 🏭

The SM-DP+ (Key Maker server) is tested in three different configurations:

| Test Room | Interfaces Tested | Who's Watching |
|---|---|---|
| TE_P1 | ES12 only: talking to the Post Office | S_SM-DS simulator |
| TE_P2 | ES9+ only: talking to the Phone Assistant | S_LPAd simulator |
| TE_P3 | Everything at once! ES2+ + ES9+ + ES12 | S_MNO + S_LPAd + S_SM-DS |

---

## ES2+: Taking Orders from the Mobile Company 📋

Six functions test how the Key Maker handles orders:

- **DownloadOrder** : "Reserve an ICCID number for this profile." The Key Maker must not give out the same number twice.
- **ConfirmOrder** : "Here's the phone's EID: build a key for THIS specific phone." The Key Maker locks the key so it only works in that one vault.
- **CancelOrder** : "Never mind, cancel that order." The ICCID goes back into the available pool.
- **ReleaseProfile** : "That profile is no longer needed, free up the space."
- **HandleDownloadProgressInfo** : "How's that download going?" The operator can check on progress.

---

## ES8+: The Secure Delivery Tube 🔒

ES8+ is the end-to-end encrypted channel from the Key Maker straight to the chip: the LPA carries the messages but can't peek inside. Five functions are tested:

- **InitialiseSecureChannel** : Builds the encrypted tunnel using SCP03t (think: a steel pipe with locks at both ends)
- **ConfigureISDP** : Creates a new locked room inside the vault for the profile
- **StoreMetadata** : Writes the label on the room: "This key belongs to Carrier X, named 'My Plan'"
- **LoadProfileElements** : Delivers the actual key, chunk by chunk, like sending a jigsaw puzzle piece by piece
- **ReplaceSessionKeys** : Changes the locks mid-delivery for extra security

---

## ES9+: The Public-Facing Counter 🏪

ES9+ is the HTTPS interface that any phone can connect to. Five functions:

- **InitiateAuthentication** : The Key Maker and chip exchange ID badges
- **AuthenticateClient** : The Key Maker verifies the chip is genuine
- **GetBoundProfilePackage** : The Key Maker hands over the encrypted key package
- **HandleNotification** : The phone says "key installed!" or "key deleted!" and the Key Maker acknowledges
- **CancelSession** : If something goes wrong, the phone can say "abort!"

---

## The Post Office: SM-DS Testing 📬

The Post Office (SM-DS) has the trickiest testing: seven different environments depending on whether it's a Root SM-DS or an Alternative SM-DS:

| Interface | Direction | What's Tested |
|---|---|---|
| ES12 | Key Maker → Post Office | Registering events ("package for phone X!"), deleting events ("package picked up!") |
| ES11 | Phone → Post Office | The phone polls: "Anything waiting for me?" |
| ES15 | Post Office → Post Office | Cascading: Alternative SM-DSs forward events to the Root SM-DS |

---

## TLS: The Armoured Car 🛡️

Every internet connection between servers must be protected. A separate group of tests checks:

- That the Key Maker's TLS certificate has the right ID number (OID `2.999.10`)
- That the Post Office's certificate is correct too (OID `2.999.15`)
- That the encryption cipher (`TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`) is the right one
- That mutual authentication works when both sides need to prove who they are

---

The Key Maker is tested as both a TLS server (when phones connect to it) AND a TLS client (when it connects to the Post Office). It has to wear both hats: and the tests verify it wears each one correctly!

---

*Kid-friendly version of GSMA SGP.23, Sections 4.3 (SM-DP+), 4.5 (SM-DS), 4.6 (TLS)*

← [Back to Kids Articles](index)
