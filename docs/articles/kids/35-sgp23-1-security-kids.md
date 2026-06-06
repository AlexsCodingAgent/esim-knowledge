---
title: "Trying to Break Into the Vault on Purpose"
date: 2026-06-07
---

# Trying to Break Into the Vault on Purpose 🔐🔨

## Imagine...

You hire a team of security experts to try to break into your safe. Not because you want them to steal anything: but because you want to know if it's *possible*. They try picking the lock. They try drilling. They present fake ID badges at the door. They tamper with the delivery tube. Every attempt gets recorded, and every defence gets tested.

This is **eUICC security testing** : SGP.23-1's extensive suite of tests that tries to break every cryptographic protection the chip has. If the chip survives, it earns trust.

---

## The Fake PKI: A Practice World 🎭

Before any security testing can happen, the test lab creates a complete parallel **Public Key Infrastructure** : all fake, all controlled:

| Test Certificate | Pretends to Be | Purpose |
|---|---|---|
| CERT_S_CI_ECDSA | GSMA Certificate Issuer | The fake "boss" at the top of the trust chain |
| CERT_S_EUM_ECDSA | Chip Manufacturer | Signs the chip's own certificate |
| CERT_S_SM_DPauth_ECDSA | Key Maker's Auth Certificate | Proves the Key Maker is legitimate |
| CERT_S_SM_DPpb_ECDSA | Key Maker's Binding Certificate | Proves the Key Maker made this specific profile |
| PK_EUICC_SIG | Chip's Public Signature Key | Used to verify every signature the chip produces |

The test chip is pre-loaded with these fake certificates. The real GSMA production certificates are never touched: the whole security test happens in a sandbox.

---

## Certificate Validation: The ID Badge Check 🪪

The `AuthenticateServer` test group (51 pages!) throws every possible certificate problem at the chip:

| Test Scenario | What's Wrong | Expected Result |
|---|---|---|
| Valid chain | Everything is correct | Chip says "ACCEPTED" |
| Wrong certificate | Certificate doesn't chain to any known CI | Chip says "REJECTED" |
| Expired certificate | The `notAfter` date is in the past | Chip says "REJECTED" |
| Mismatched ID | Certificate OID doesn't match the transaction | Chip says "REJECTED" |
| Unknown CI | The CI public key ID isn't in the chip's trusted list | Chip says "REJECTED" |

If the chip accepts even ONE of these bad certificates, the test fails: and the chip goes back for repairs.

---

## ECDSA: The Math That Protects Everything 🧮

Elliptic Curve Digital Signature Algorithm (ECDSA) is the math behind eSIM security. SGP.23-1 tests signing and verification across four different curves:

| Curve | Where Used | Why It Matters |
|---|---|---|
| **NIST P-256** | Most common, global standard | Every chip must support at least this one |
| **BrainpoolP256r1** | European preference | Alternative curve with different math properties |
| **FRP256V1** | French national standard | Required for French government use cases |
| **SM2** | Chinese national algorithm | Required for Chinese market |

Every signature the chip produces : `euiccSignPIR` (profile install result), `euiccSignRPR` (remote management result), and `EUICC_SIGNATURE2` (download handshake) : is verified against the chip's known public key using the correct curve.

---

## SCP03t: The Unbreakable Delivery Tube 🔒

The ES8+ secure channel uses SCP03t: a protocol so secure that even the LPA carrying the messages can't peek inside. Testing verifies:

- **ECDH Key Agreement** : The chip and Key Maker agree on a shared secret without ever sending it over the wire
- **Session Key Derivation** : Three keys (S-ENC for encryption, S-MAC and S-RMAC for tamper detection) are derived from the shared secret
- **MAC Verification** : Every message has a MAC tag; if even one byte is changed, the chip detects it
- **Encryption** : Profile content is encrypted so the LPA sees only scrambled data
- **Session Key Rotation** : `ReplaceSessionKeys` changes the locks mid-delivery for extra forward secrecy

Error testing covers: wrong keys, invalid signatures, bad transaction IDs, double initiation attempts, and malformed channel parameters.

---

## CRL: The Banned List 🚫

The `LoadCRL` test verifies the Certificate Revocation List system:

1. Load a valid CRL onto the chip : "These certificates are no longer trusted"
2. Try to authenticate with a certificate on the banned list
3. The chip MUST reject it

It's like a bouncer at a club checking a banned list: if you're on it, you're not getting in, no matter how good your fake ID looks.

---

## Key Generation: Fresh Keys Every Time 🔄

During `PrepareDownload`, the chip generates a brand-new one-time key pair (`otPK.eUICC.ECKA` / `otSK.eUICC.ECKA`). Tests verify:

- **Freshness** : Each call produces a different key pair (no repeats!)
- **Correct format** : The public key is properly formatted for the selected curve
- **Retry reuse** (optional) : If `O_E_REUSE_OTPK` is supported, the chip reuses the key for a retry after a failed download

---

The test PKI is so thoroughly isolated from production that even if a test certificate leaked onto the internet, it couldn't be used to attack real eSIMs: because real chips only trust the *real* GSMA Certificate Issuer, and test chips only trust the *fake* one!

---

*Kid-friendly version of GSMA SGP.23-1, Sections 4.2.3, 4.2.10, 4.2.17, 4.2.18, Annex A.2*

← [Back to Kids Articles](index)
