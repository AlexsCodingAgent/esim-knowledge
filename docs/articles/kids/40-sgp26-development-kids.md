---
title: "Setting Up Your Testing Lab with Practice Badges"
date: 2026-06-07
---

# Setting Up Your Testing Lab with Practice Badges 🧪

## Imagine...

You just received a big box labelled "SECURITY BADGE TESTING KIT: FOR LAB USE ONLY." Inside, you find plastic badges, a badge printer, a binder of configuration recipes, and a note that says: *"Everything you need to run your own ID badge testing facility. Private keys included!"*

Your job: set up a mini security checkpoint where test phones and test servers can try on their practice badges and make sure everything works before the real badges ever go into production.

That's exactly what setting up an SGP.26 test environment is like: and this article walks you through the whole process, badge kit to working lab.

---

## Step 1: Get Your Badge Kit 📦

The SGP.26 testing kit comes as a ZIP file (named something like `SGP.26_v3.0-20250127_Files.ZIP`). Inside you'll find:

| What's in the Box | Format | What It's For |
|---|---|---|
| 🗝️ **All private keys** | PEM files | The secret codes that make each badge work |
| 🪪 **All certificates** | DER files | The badges themselves |
| 📜 **CRL WANTED posters** | CRL files | Lists of revoked badges (currently empty!) |
| 📝 **Recipe files** | OpenSSL `.cnf` configs | Templates for baking new badges |

The kit is updated at least every two years by the GSMA to prevent badge expiry. Always grab the latest version: old badges might have expired!

---

## Step 2: Prepare Your Test Phone 📱

A test eSIM phone needs four things loaded into its secure vault (called the ECASD):

| What to Load | Which File | Why |
|---|---|---|
| 🏛️ **Grandpa CI's badge** | `CERT_CI_SIG.der` | The phone needs to know who the ultimate authority is |
| 🏭 **Factory Parent's badge** | `CERT_EUM_SIG.der` | Proves the factory authorised this phone |
| 📱 **Phone Child's badge** | `CERT_EUICC_SIG.der` | The phone's own identity |
| 🗝️ **Phone Child's secret key** | `SK_EUICC_SIG.pem` | The phone's private signature code |

Think of it like setting up a new employee: they need to know who the boss is (Grandpa CI), which department hired them (Factory Parent), receive their own ID card (Phone Child badge), and have their own PIN code (secret key).

How you actually load these depends on your phone's manufacturer. Some provide pre-loaded test SIMs with all four items ready to go. Others let you inject certificates through special programming tools.

---

## Step 3: Set Up Your Test Key Maker 🔑

A test SM-DP+ server (the Key Maker) needs three different badges, each loaded into the right service:

| Badge | Load Into... | Job |
|---|---|---|
| 🔑 **Auth Badge** (`CERT.DPauth.SIG`) | The authentication service | Saying "hello, I'm a real Key Maker" |
| 📦 **Binding Badge** (`CERT.DPpb.SIG`) | The profile delivery service | Sealing profile packages with a signature |
| 🌐 **TLS Badge** (`CERT.DP.TLS`) | The web server | Making secure encrypted phone calls |

These three badges are deliberately separate: if one gets compromised, the others are still safe. It's like having separate keys for your house, car, and office instead of one master key.

The Key Maker also needs to:

- **Serve CRL WANTED posters** : make the revocation list available at the web addresses printed on the badges (like `http://ci.test.example.com/CRL-1.crl`)
- **Present the full family chain** : during introductions, show not just its own badge but also the Parent badge and Grandpa badge that vouch for it
- **Host a test profile** : have a downloadable eSIM profile ready so testers can actually try downloading something

---

## Step 4: Set Up Your Test Post Office 📬

A test SM-DS server (the Post Office) is simpler: it only needs two badges:

- 📬 **Auth Badge** (`CERT.DSauth.SIG`) : for signing discovery announcements
- 🌐 **TLS Badge** (`CERT.DS.TLS`) : for secure web connections

Same setup principle: each badge goes to the right service, and CRL WANTED posters must be served at the right web addresses.

---

## Step 5: Make It All Talk 🗣️

Now comes the moment of truth. Your test phone has its badges, your test Key Maker has its badges, and your test Post Office has its badges. Time to test a profile download:

1. The phone connects to the Key Maker
2. They exchange badges and check each other's family trees
3. Both verify that no badges are on the WANTED poster
4. The Key Maker seals a test profile with its binding badge
5. The phone receives and installs it

If every badge checks out, the download succeeds. If any badge is wrong (wrong family tree, wrong job tag, expired date), the process stops with a clear error: exactly what you want for testing!

---

## Common Mistakes (Don't Fall for These!) 🕳️

| Mistake | What Happens | Fix |
|---|---|---|
| 🔄 **DER/PEM mix-up** | Badges in the kit are DER format, but some tools need PEM | Convert with a simple command |
| 🔀 **Wrong variant** | Phone has Variant O badges, Key Maker has Variant A badges | Use the same variant for the whole test |
| 🔗 **Unreachable CRL** | The phone tries to check `ci.test.example.com` but it doesn't exist | Set up local DNS or a hosts file entry |
| ⏰ **Expired badges** | TLS badges only last 398 days: they might be dead! | Download a fresh kit or regenerate TLS badges |
| 🔑 **Production trust anchor** | The test phone has a real production Grandpa CI, not the test one | Make sure to load the test Grandpa CI |
| 🧮 **Curve mismatch** | Phone uses NIST P-256 but Key Maker presents Brainpool badges | Check which curves your phone supports |

---

## Roll Your Own Badges 🏗️

Don't want to use the central GSMA test badges? Annex C of SGP.26 lets you create your own! Any RSP actor can:

1. Generate their own Grandpa CI private key
2. Create a self-signed Grandpa badge
3. Sign all their own Child badges under it
4. Publish it on the GSMA test certificate registry

This is like setting up your own mini security department with its own badge system: completely independent but following the same rules. Perfect for companies that want a private testing playground.

---

The GSMA maintains a public registry at `gsma.com/esim/gsma-root-ci/` that lists all the test Key Makers and Post Offices you can connect to for interoperability testing. It's like a phone book for practice badges: find a test server, download a test profile, and verify your setup works with the wider world.

---

*Kid-friendly version of GSMA SGP.26: Developer Setup and Integration*

← [Back to Kids Articles](index)
