---
description: "What's printed on every SGP.26 test badge: the fields, policy OIDs, and role tags that tell an eSIM chip whether to trust or reject a certificate during verification."
title: "What Makes a Valid Practice Badge?"
date: 2026-06-07
---

# What Makes a Valid Practice Badge? 🔍

## Imagine...

You're a security guard at a big office building. When someone walks up with an ID badge, you don't just glance at the photo: you check multiple things: Is the hologram real? Is the expiry date still in the future? Does their name match the visitor list? Is the badge type correct: is this a "Visitor" badge or an "Employee" badge?

An eSIM chip does exactly the same thing when it checks a certificate. Every practice badge in SGP.26 has a specific set of features that make it valid: and if even one feature is wrong, the badge gets rejected. This article is your guide to what's on the badge and why every piece matters.

---

## What's Printed on Every Practice Badge? 📋

Every SGP.26 certificate is like a detailed ID card with specific fields:

| Badge Feature | What It Means | Real-World Analogy |
|---|---|---|
| **Subject Name** | Who this badge belongs to | The person's name on the ID |
| **Issuer Name** | Who signed this badge | "Issued by: Department of Security" |
| **Validity Period** | How long the badge is good for | "Expires: December 2029" |
| **Public Key** | The visible code anyone can check | The barcode on the back |
| **Signature** | Mathematical proof it's genuine | The hologram that can't be faked |
| **Serial Number** | Unique ID for this badge | Badge number #000472 |
| **Key Usage** | What this badge is allowed to do | "Authorised: Building Access Only" |
| **Certificate Policies** | What role this badge plays | "Classification: Fire Marshal" |
| **Basic Constraints** | Is this a Parent badge or a Child badge? | "This ID can authorise other IDs" |

All practice badges use the same curves (NIST P-256 or Brainpool P256r1) and the same signature recipe (SHA-256 with ECDSA). No exceptions: it's like every badge in the company using the same hologram technology.

---

## What Job Is This Badge For? 💼

The most important check is the **Certificate Policies** field: it tells the chip what job this badge holder is authorised to do. It's an OID (a dot-separated number like `2.23.146.1.2.1.2`) that encodes the role:

| Role | Policy Tag | Can They... |
|---|---|---|
| 🏛️ **Grandpa CI** | `...1.0` | Sign anyone's badge |
| 📱 **Phone Child** | `...1.1` (Variant O) | Prove its own identity |
| 🔑 **Key Maker Auth** | `...1.2` | Introduce themselves to phones |
| 🔐 **Key Maker TLS** | `...1.3` | Make secure encrypted calls |
| 📦 **Key Maker Binding** | `...1.5` | Seal profile packages |
| 📬 **Post Office Auth** | `...1.7` | Sign discovery announcements |
| 🌐 **Post Office TLS** | `...1.6` | Make secure calls for the post office |

If the Key Maker tries to use a TLS badge (phone-call badge) for authentication (hello badge), the phone says: *"Wrong badge type!"* and rejects it. The phone checks the policy field *every time*.

---

## What Can You DO With This Badge? 🔑

The **Key Usage** field is like permissions on the back of an ID card:

| Badge Type | Key Usage | Why? |
|---|---|---|
| **Parent badges** (CI, EUM, SubCAs) | `keyCertSign` + `cRLSign` | "I can sign other badges and manage the WANTED list" |
| **Child badges** (eUICC, auth, binding) | `digitalSignature` | "I can prove my identity with a signature" |
| **Phone-call badges** (TLS) | `digitalSignature` + `serverAuth` + `clientAuth` | "I can make AND receive secure calls" |

Parent badges get the special `keyCertSign` power: they're the only ones allowed to sign new badges. Child badges only get `digitalSignature`, which means they can sign things to prove who they are but can't create new badges. It's like the difference between a manager who can hire people and an employee who can only clock in.

Phone-call badges (TLS) are extra special: they get `serverAuth` + `clientAuth`, meaning they can both host calls AND call others. In the eSIM world, servers sometimes need to phone each other!

---

## Is This a Parent or a Child? 👶

The **Basic Constraints** field answers one simple question: *"Can this badge sign other badges?"*

- **Parent badges**: `CA = true` (CA means Certificate Authority: a signer). Some Parents also have `pathLenConstraint = 0`, which means "you can sign Children but not more Parents."
- **Child badges**: No Basic Constraints extension at all: they're the end of the line.

This is how the family tree stays under control. A Phone Child can't accidentally be treated as a Parent.

---

## The Deliberately Broken Badges 💥

Here's the clever part. SGP.26 doesn't just provide perfect practice badges: it also provides **deliberately broken ones** for testing your badge-checker:

| Broken Badge | What's Wrong | Expected Reaction |
|---|---|---|
| ✂️ **Scrambled Signature** | Last bytes of the hologram replaced with zeros | "This signature is fake!" |
| 🔀 **Wrong Curve (P-192)** | Uses a curve your phone doesn't support | `unsupportedCurve(3)` : "I don't speak that language" |
| 🏷️ **Wrong Job Tag** | TLS badge with auth policy OID | "You're using the wrong badge for this job!" |
| ⛔ **Missing Permission** | TLS badge without `serverAuth` | "You can't host calls with this badge" |
| 🗝️ **Wrong Key Power** | `keyAgreement` instead of `digitalSignature` | "This badge can't prove your identity" |
| ⏰ **Expired Badge** | Validity set to just 1 day | "Your badge has expired!" |

These broken badges are like crash-test dummies: you *want* your phone to reject them, because that proves its security checks are working.

---

## How Long Is a Badge Good For? ⏳

Badges have wildly different lifetimes:

- 🏛️ **Grandpa CI**: 35 years (outlasts everything)
- 📱 **Phone Child**: 2,000,000 days (effectively forever: phones must never outlive their built-in badge)
- 🔑 **Key Maker / Post Office**: 1,095 days (3 years: reasonable rotation)
- 🌐 **Phone-call badges (TLS)**: Only 398 days (about 13 months: these get replaced most often)
- 🤖 **Robot badges (eIM)**: 2,555 days (7 years: IoT devices in the field for a long time)

The Phone Child badge lasts effectively forever because you can't swap out the built-in badge on an eSIM chip without destroying the phone. TLS badges are the shortest-lived because secure web connections demand fresh certificates.

---

The EUM (Factory Parent) badge carries a special "name constraint" rule: it can only make badges for phones whose fingerprints start with `89049032`. This is exactly how real factories work: each manufacturer gets assigned their own EIN prefix, and their badge legally restricts them to only making phones within that range.

---

*Kid-friendly version of GSMA SGP.26: Certificate Profiles*

← [Back to Kids Articles](index)
