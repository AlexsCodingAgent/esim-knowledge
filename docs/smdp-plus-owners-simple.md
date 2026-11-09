---
layout: default
title: "SM-DP+ Domain List: Which Provider Is Behind the Address"
description: "A one-table lookup from the domain in an eSIM activation code to the SM-DP+ provider behind it: ondemandconnectivity.com is Thales, idemia.io is IDEMIA, gdsb.net is G+D, truphone.com is 1GLOBAL, and the rest."
---

# SM-DP+ domains, by provider

The middle field of `LPA:1$<domain>$<matching id>` is an SM-DP+ address. Find the domain in this table and you have the provider. The prefix does not matter: a longer hostname under the same domain belongs to the same provider.

| Domain | SM-DP+ provider |
|---|---|
| `smdp.io` | 1GLOBAL |
| `truphone.com` | 1GLOBAL |
| `a1-systems.com` | A1 Systems |
| `eastcompeace.com` | Eastcompeace |
| `toprsp.com` | Eastcompeace |
| `gdsb.net` | G+D (Giesecke+Devrient) |
| `go-esim.com` | G+D (Giesecke+Devrient) |
| `venyonservices.com` | G+D (Giesecke+Devrient) |
| `esimdiscovery.com` | Google |
| `esimdiscovery.dev` | Google |
| `rsp.goog` | Google |
| `gsma.com` | GSMA (test endpoint) |
| `idemia.io` | IDEMIA |
| `oberthur.net` | IDEMIA |
| `otlabs.fr` | IDEMIA |
| `infineon.com` | Infineon (test) |
| `kigen.com` | Kigen |
| `linksfield.net` | Links Field |
| `esim.exchange` | NEWare |
| `esimcase.com` | NEWare |
| `smdpplus.net` | Nordic eSIM |
| `oasis-smartsim.com` | Oasis Smart SIM |
| `esim.pub` | Redtea Mobile |
| `redteamobile.com` | Redtea Mobile |
| `simlessly.com` | Redtea Mobile |
| `sysmocom.de` | sysmocom (lab) |
| `ondemandconnectivity.com` | Thales |
| `otgeuicc.com` | Thales |
| `esim-rsp.com` | Torrion River |
| `e-sim.global` | Trasna / Workz |
| `e-sim.world` | Trasna / Workz |
| `rsp.global` | Trasna / Workz |
| `rsp.world` | Trasna / Workz |
| `trasna.io` | Trasna / Workz |
| `workz.com` | Trasna / Workz |
| `workz.net` | Trasna / Workz |
| `validereachdpplus.com` | Valid |
| `validspereachdpplus.com` | Valid |

A handful of addresses are operators running their own platform on their own domain. They are the owner, not a reseller:

| Domain | Operator |
|---|---|
| `airtel.in` | Airtel |
| `mts.ru` | MTS |
| `tele2.ru` | Tele2 Russia |
| `jio.com` | Reliance Jio |
| `esim.com.sa` | Zain Saudi Arabia |
| `instant-connectivity.com` | per-operator hostnames on a shared platform |

For the full catalogue of 202 addresses, the certificate evidence behind each, and how to attribute an address that is not listed, see [Who runs an SM-DP+ address]({{ site.baseurl }}/docs/smdp-plus-ownership).
