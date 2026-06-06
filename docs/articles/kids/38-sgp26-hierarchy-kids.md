---
title: "The Family Tree: Grandpa, Parents, and Children Badges"
date: 2026-06-07
---

# The Family Tree: Grandpa, Parents, and Children Badges 🌳

## Imagine...

Picture a big family reunion. Grandpa CI is the oldest and most respected person in the room — everyone trusts Grandpa because he's been around forever. When Grandpa says "this person is part of our family," nobody questions it.

Now imagine Grandpa signing permission slips. In some families, Grandpa signs every slip himself. In others, Grandpa delegates — he tells the Parents, "you can sign slips for your kids." And in the biggest families, Grandpa tells a trusted Aunt or Uncle, who then tells the Parents, who then sign for the Children.

This is exactly how the **SGP.26 certificate hierarchy** works — a family tree of trust, flowing from the ultimate root down to every individual badge.

---

## Meet the Family 👨‍👩‍👧‍👦

| Family Role | Certificate Name | Who They Trust | Who They Sign For |
|---|---|---|---|
| **Grandpa CI** | CERT.CI.SIG | Themselves (self-signed) | Everyone below |
| **Trusted Aunt/Uncle** | CERT.CISUBCA.SIG | Grandpa CI | Parents & Children |
| **Factory Parent** | CERT.EUM.SIG | Grandpa or Aunt/Uncle | The Phone Children |
| **Key Maker Parent** | CERT.DPSubCA.SIG | Grandpa or Aunt/Uncle | Key Maker tools |
| **Post Office Parent** | CERT.DSSubCA.SIG | Grandpa or Aunt/Uncle | Post Office tools |
| **Phone Child** | CERT.EUICC.SIG | Factory Parent | Nobody (end of the line) |
| **Key Maker Child** | CERT.DPauth / DPpb / DP.TLS | Key Maker Parent | Nobody |
| **Post Office Child** | CERT.DSauth / DS.TLS | Post Office Parent | Nobody |
| **Robot Child** | CERT.EIM.ECDSA / EIM.TLS | Grandpa directly | Nobody |

Grandpa CI is special — he signs his *own* badge. Everyone else gets their badge signed by someone higher up the family tree.

---

## Four Family Shapes 🏠

Not every family is organised the same way. SGP.26 defines four main family shapes (called *variants*):

### Variant O — Grandpa Does Everything

```
Grandpa CI ──┬── Factory Parent ── Phone Child
             ├── Key Maker Child (auth, pb, TLS)
             ├── Post Office Child (auth, TLS)
             └── Robot Child (sign, TLS)
```

The simplest family. Grandpa signs every badge directly. Quick and easy — but Grandpa does all the work!

### Variant B — Grandpa Delegates to One Trusted Helper

```
Grandpa CI ── Trusted Aunt/Uncle ──┬── Factory Parent ── Phone Child
                                   ├── Key Maker Child
                                   └── Post Office Child
```

Grandpa signs one helper, who handles everything else. Like Grandpa saying "I trust my sister to manage the family."

### Variant A — Grandpa Has Specialist Parents

```
Grandpa CI ──┬── Factory Parent ──┬── Phone Child
             ├── Key Maker Parent ── Key Maker Children
             └── Post Office Parent ── Post Office Children
```

Grandpa appoints three specialist Parents, one for each department. Each Parent only manages their own area.

### Variant C — The Full Delegation Chain

```
Grandpa CI ── Trusted Aunt ──┬── Factory Parent ── Phone Child
                              ├── Key Maker Parent ── Key Maker Children
                              └── Post Office Parent ── Post Office Children
```

The deepest family tree — three levels of trust delegation. Grandpa trusts Aunt, Aunt trusts Parents, Parents trust Children.

---

## How Trust Flows Downward ⬇️

Trust only flows one way in the family tree: **downward**. When Phone Child shows its badge to Key Maker Child, the Key Maker traces the chain upward: "Who signed YOUR badge? Factory Parent. Who signed Factory Parent? Trusted Aunt. Who signed Trusted Aunt? Grandpa CI — and I trust Grandpa!"

If the chain reaches Grandpa, the badge is accepted. If any link is missing, it's rejected. This is called **certificate path validation** — and testing all five family shapes makes sure your badge-checker can handle every possible arrangement.

---

## Special Badge Rules 🔖

Each level in the family has its own rules:

- **Grandpa CI** — Only signer that's self-signed. Valid for 35 years (12,783 days). Has the ultimate authority.
- **Parents (EUM, SubCAs)** — Have a `pathLenConstraint = 0`, meaning they can sign Children but not *more* Parents. Like being told "you can have kids, but no grandkids."
- **Phone Child (eUICC)** — Valid for an incredible 2,000,000 days (about 5,479 years). Effectively *forever* — because replacing a phone's built-in badge would be like trying to swap out the foundation of a house.
- **Key Maker Child (SM-DP+)** — Actually holds **three** separate badges: one for saying hello (authentication), one for sealing packages (profile binding), and one for secure phone calls (TLS).

---

## 🧠 Did You Know?

The Phone Child's badge has its unique serial number (the EID) embedded right in the badge itself — like having your fingerprint printed on your ID card. And the Factory Parent's badge has a rule that says "I can only make badges for phones whose fingerprints start with `89049032`." A phone with a different fingerprint prefix would be refused!

---

*Kid-friendly version of GSMA SGP.26 — Certificate Hierarchy*

← [Back to Kids Articles](index)
