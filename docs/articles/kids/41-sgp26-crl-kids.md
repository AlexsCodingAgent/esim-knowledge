---
title: "WANTED: The List of Bad Badges"
date: 2026-06-07
---

# WANTED: The List of Bad Badges 🚨

## Imagine...

You're a security guard at the front desk. Every morning, you get a fresh printout: a **WANTED poster** listing all the ID badges that have been reported stolen, lost, or cancelled. Before you let anyone through the door, you check their badge against the WANTED list. If their badge number appears on it, no entry: even if the badge looks perfect otherwise.

In the eSIM world, this WANTED poster is called a **CRL** : Certificate Revocation List. And just like the security guard, every eSIM phone and server checks the CRL before trusting any badge.

SGP.26 defines a complete CRL system for practice badges. This article explains how the WANTED posters work, who publishes them, and why they're set up in a deliberately unusual way.

---

## What Is a CRL? 📜

A CRL (Certificate Revocation List) is a digitally signed list of badge serial numbers that should no longer be trusted. It answers one question: **"Has this badge been cancelled?"**

| If the badge... | Result |
|---|---|
| ✅ Is NOT on the WANTED poster | Allowed through: badge is valid |
| ❌ IS on the WANTED poster | Denied! : badge has been revoked |
| ⚠️ The poster itself has expired | Treated with suspicion: get a fresh poster |

The CRL is signed by the same authority that issued the badges. Just like the badges themselves, the CRL has a signature that proves nobody tampered with it.

---

## Who Publishes WANTED Posters? 🏢

Every Parent in the family tree who signs badges also publishes their own WANTED poster:

| Poster Publisher | Covers These Badges | Where to Find It |
|---|---|---|
| 🏛️ **Grandpa CI** | All badges signed directly by Grandpa | `http://ci.test.example.com/CRL-1.crl` and `CRL-2.crl` |
| 👨‍👩‍👧 **Trusted Aunt/Uncle** | Badges signed by Aunt/Uncle (Variants B, C) | Same as Grandpa (shares the website!) |
| 🏭 **Factory Parent** | Badges signed by Factory (Phone Children, EUM SubCA) | `http://eum.test.example.com/CRL.crl` |
| 🔑 **Key Maker Parent** | Badges signed by Key Maker Parent (auth, pb, TLS) | `http://smdp.test.example.com/CRL.crl` |
| 📬 **Post Office Parent** | Badges signed by Post Office Parent (auth, TLS) | `http://smds.test.example.com/CRL.crl` |

Notice that Grandpa CI publishes TWO copies of his poster (CRL-1 and CRL-2) : a backup in case one website is down. Smart thinking!

The web addresses printed on each badge tell the checker exactly where to look. It's like every badge saying: *"To verify me, check the WANTED poster at this specific address."*

---

## The Surprising Truth: Nobody Is WANTED Yet 👻

Here's the twist that surprises everyone: **all SGP.26 CRLs are currently empty!**

The current version of SGP.26 (v3.0.2) explicitly says that CRLs with actually-revoked badges are marked "FFS" : *For Future Study*. The infrastructure exists and works perfectly, but nobody has actually put any badge serial numbers on the WANTED posters yet.

Why? Because the GSMA wanted to get the CRL *structure* right first. The posters are published, the web addresses resolve, the signatures verify: everything works. Adding revoked badges is a future step, planned for later versions of SGP.26.

Think of it like a newly-built police station with empty WANTED boards. The boards are up, the procedures are in place, but no suspects have been posted yet.

---

## The Weirdly Long Poster: 3-Year Validity ⏰

CRLs have an expiry date just like badges do. In the real world, CRLs are typically reissued every 24 hours to 7 days: very short, so that a recently-revoked badge gets noticed quickly.

SGP.26 does something deliberately unusual: **CRLs are valid for 1,095 days (3 years).**

The spec itself admits: *"A duration of 3 years for a CRL is unusual."*

But there's a good reason. In a testing lab, you might have test suites that run for months. The last thing you want is for a test to fail because the WANTED poster itself expired: not because of an actual problem with the badges. The 3-year validity ensures that no test execution fails from CRL expiry.

| Real World | SGP.26 Test World |
|---|---|
| CRL valid for hours or days | CRL valid for 3 years |
| Short validity = quick response to compromise | Long validity = no interrupted test runs |
| New posters arrive constantly | One poster lasts the whole test suite |

---

## What Each Poster Covers 🎯

Each WANTED poster has a scope: it tells you which *kind* of badges it lists:

| Poster Publisher | Scope | Meaning |
|---|---|---|
| 🏛️ **Grandpa CI** | Covers BOTH Parent and Child badges | "I list everyone: bosses and employees alike" |
| 👨‍👩‍👧 **Trusted Aunt/Uncle** | Covers BOTH | Same as Grandpa |
| 🏭 **Factory Parent** | Covers ONLY Parent badges | "I only list other bosses, not regular employees" |
| 🔑 **Key Maker Parent** | Covers ONLY Child badges | "I only list employees, not other bosses" |
| 📬 **Post Office Parent** | Covers ONLY Child badges | Same as Key Maker Parent |

This scoping is controlled by a special flag on each CRL: `onlyContainsCACerts` (Parent badges only) or `onlyContainsUserCerts` (Child badges only). Grandpa's poster has neither flag: he covers everyone.

---

## Setting Up WANTED Posters in Your Lab 🖥️

In a real test setup, the URLs on the badges (`ci.test.example.com`, `smdp.test.example.com`, etc.) don't point to real websites. You need to make them work:

- **Option 1: Local web server** : Run a tiny HTTP server on your test machine that serves the CRL files. Add entries to your `/etc/hosts` file so the test domains point to `127.0.0.1`.
- **Option 2: Test network DNS** : Configure your test network's DNS to resolve `*.test.example.com` to a CRL server in your lab.
- **Option 3: Preload CRLs** : Some test phones let you load CRL files directly, skipping the web download entirely.
- **Option 4: Skip CRL checks** : For tests not focused on CRL behaviour, some phones let you disable CRL validation. But be careful: this should be clearly documented!

The CRL files must be served with the MIME type `application/pkix-crl`. Yes, some validators actually check this!

---

## No OCSP Here: CRLs Only 🚫🔍

SGP.26 uses CRLs exclusively: there's no OCSP (Online Certificate Status Protocol) responders. Why?

eSIM phones are embedded devices that might not have continuous internet access. A CRL can be downloaded once and cached. An OCSP responder requires a live connection every time you check a badge: impractical for a phone that might be offline for days.

This is by design, mirroring how production eSIM systems work. In the embedded world, CRLs are the standard.

---

## The Future: Actual WANTED Badges Coming Soon 🔮

The specification promises that future versions of SGP.26 will include:

- CRLs with actual revoked badge serial numbers
- Revocation dates and reasons ("key compromised," "superseded," etc.)
- Corresponding badges that are valid except for appearing on the CRL
- SGP.23 test cases that verify phones correctly reject revoked badges

Until then, the CRL infrastructure stands ready: empty posters on the wall, waiting for their first wanted criminals.

---

All SGP.26 CRLs use `cRLNumber = 2024` : a fixed, predictable number. In production, the CRL number increases with every reissue (2024, 2025, 2026...). In testing, a fixed number means test cases can hardcode the expected value, making validation simpler and more predictable.

---

*Kid-friendly version of GSMA SGP.26: CRL and Certificate Management*

← [Back to Kids Articles](index)
