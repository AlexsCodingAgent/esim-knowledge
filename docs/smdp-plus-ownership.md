---
layout: default
title: "Who Runs an SM-DP+ Address: Mapping an Activation Code to Its Operator"
description: "Given the SM-DP+ address in an eSIM activation code, who operates that server. Domain families for Thales On-Demand Connectivity, IDEMIA, G+D, 1GLOBAL, Redtea, Trasna and 13 more, with 202 catalogued addresses, the certificate evidence behind each, and how to attribute an address that is not listed."
---

# Who runs an SM-DP+ address

An activation code names a server. That name is usually enough to say who operates it.

```
LPA:1$rsp.truphone.com$04386-AGYFT-A74Y8-3F815
       ^^^^^^^^^^^^^^^^ the SM-DP+ address
```

The address is a fully qualified domain name. The company that owns the registrable domain runs that endpoint, and the RSP certificate presented on it names the same company. GSMA has no central register of who runs which SM-DP+, so the address, the certificate and the operator's own documentation are what you have. This page collects them into one place.

## Read it by domain family

You do not need the exact hostname. The registrable domain is enough, and a fragment of it is usually enough on its own.

| In the address | Runs on | Notes |
|---|---|---|
| `ondemandconnectivity.com, otgeuicc.com` | Thales (On-Demand Connectivity) | Formerly Gemalto. `*.vzw.otgeuicc.com` and similar are Thales endpoints branded per operator. |
| `idemia.io, oberthur.net, otlabs.fr` | IDEMIA | `idemia` appears in the string. Oberthur and OT Labs are IDEMIA's earlier names. |
| `go-esim.com, gdsb.net, venyonservices.com` | Giesecke+Devrient (G+D) | `gdsb` is the G+D SIM bank. `cust-NNN-v4-prod-atl2` hosts are per-customer instances. |
| `truphone.com, smdp.io` | 1GLOBAL | 1GLOBAL, then TP Global Operations, bought Truphone in January 2023. `smdp.io` is its short, brandless endpoint. |
| `redteamobile.com, simlessly.com, esim.pub` | Redtea Mobile | RedteaGO is the same company's consumer brand. |
| `rsp.global, rsp.world, e-sim.global, e-sim.world, workz.com, workz.net, trasna.io` | Trasna | Trasna acquired Workz, so the Workz RSP domains now resolve to the same platform. |
| `eastcompeace.com, toprsp.com` | Eastcompeace | Chinese card and RSP vendor. |
| `validereachdpplus.com, validspereachdpplus.com` | Valid | `validsperreach` hosts are named per customer, for example `bics.`, `claroargentina.`. |
| `esimcase.com, esim.exchange` | NEWare | Also `esim.ignitech.com`, `rsp.tsimmobile.com`, `rsp.eaglesim.com`. |
| `oasis-smartsim.com, esim-in-a-box.com` | Oasis Smart SIM | Sells a packaged SM-DP+ in a box; both domains serve the same platform. |
| `rsp.goog, esimdiscovery.com, esimdiscovery.dev` | Google | Google's own profiles, including `esimdiscovery` test endpoints. |
| `smdpplus.net` | Nordic eSIM | `az.`, `dk.` hosts are per region. |
| `a1-systems.com` | A1 Systems | Russian integrator; hosts are per operator (`beeline-con`, `sbermobile-con`). |
| `linksfield.net, kigen.com, esim-rsp.com` | Links Field, Kigen, Torrion River | Smaller platforms, each on its own domain. |
| `sysmocom.de, infineon.com, gsma.com` | Lab and test | Not commercial endpoints. Card vendors and the GSMA use `test` in the hostname. |

## The catalogue

Every address below was collected on 2026-09-18, and the certificate column records what the endpoint presented when it was last read, on 2026-06-24. 202 addresses, grouped by who runs them.

Basis codes: `certificate` means the RSP certificate on that endpoint names the vendor. `san` means a certificate seen elsewhere in the same family lists it as a subject alternative name. `family` means the hostname sits under a domain the vendor is known to serve from. `none` means nothing more than the hostname was available.

| # | Address | Runs on | Basis | Confidence | Brand seen |
|---:|---|---|---|---|---|
| 1 | `2.vzw.otgeuicc.com` | Thales | certificate | high | Verizon |
| 2 | `anc.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 3 | `apb.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 4 | `bmc.prod.ondemandconnectivity.com` | Thales | family | documented | Virgin Plus |
| 5 | `cel.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 6 | `cha.vzw.otgeuicc.com` | Thales | family | medium |  |
| 7 | `esim.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 8 | `frm.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 9 | `gsma2.vzw.otgeuicc.com` | Thales | family | documented | Verizon |
| 10 | `gsmacct.vzw.otgeuicc.com` | Thales | family | medium |  |
| 11 | `h3a.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 12 | `hhk.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 13 | `huk.prod.ondemandconnectivity.com` | Thales | family | documented | Jola via docs |
| 14 | `jph.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 15 | `kddi.prod.ondemandconnectivity.com` | Thales | family | medium | KDDI via domainHint |
| 16 | `kt.prod.ondemandconnectivity.com` | Thales | family | medium | KT via domainHint |
| 17 | `lgu.prod.ondemandconnectivity.com` | Thales | family | medium | LG U+ via domainHint |
| 18 | `lpads.vzw.otgeuicc.com` | Thales | family | medium |  |
| 19 | `man-gto.prod.ondemandconnectivity.com` | Thales | certificate | high |  |
| 20 | `mka.prod.ondemandconnectivity.com` | Thales | certificate | high |  |
| 21 | `peo.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 22 | `pkt.prod.ondemandconnectivity.com` | Thales | certificate | high |  |
| 23 | `qmi.prod.ondemandconnectivity.com` | Thales | certificate | high |  |
| 24 | `rakuten.prod.ondemandconnectivity.com` | Thales | certificate | high | Rakuten Mobile via domainHint |
| 25 | `sin.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 26 | `sma.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 27 | `snr.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 28 | `thales3.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 29 | `tl2.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 30 | `tnz.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 31 | `trl.prod.ondemandconnectivity.com` | Thales | certificate | high |  |
| 32 | `tsm.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 33 | `tur.prod.ondemandconnectivity.com` | Thales | family | medium |  |
| 34 | `twl.prod.ondemandconnectivity.com` | Thales | family | documented | KORE Super SIM |
| 35 | `usm.vzw.otgeuicc.com` | Thales | family | medium |  |
| 36 | `vsb.vzw.otgeuicc.com` | Thales | family | medium |  |
| 37 | `vuk-gto.prod.ondemandconnectivity.com` | Thales | certificate | high | eSIM.net via docs |
| 38 | `wbg.prod.ondemandconnectivity.com` | Thales | certificate | high | Airalo via docs |
| 39 | `celitech.idemia.io` | IDEMIA | family | medium | CELITECH via domainHint |
| 40 | `mc4-demo.otlabs.fr` | IDEMIA | family | medium |  |
| 41 | `mc4-poc6.otlabs.fr` | IDEMIA | family | medium |  |
| 42 | `rsp-0001.oberthur.net` | IDEMIA | family | medium |  |
| 43 | `rsp-0002.oberthur.net` | IDEMIA | family | medium |  |
| 44 | `rsp-0003.oberthur.net` | IDEMIA | certificate | high |  |
| 45 | `rsp-0004.oberthur.net` | IDEMIA | family | medium |  |
| 46 | `rsp-0006.oberthur.net` | IDEMIA | family | medium |  |
| 47 | `rsp-0010.oberthur.net` | IDEMIA | certificate | high |  |
| 48 | `rsp-0014.oberthur.net` | IDEMIA | certificate | high |  |
| 49 | `rsp-0018.oberthur.net` | IDEMIA | family | medium |  |
| 50 | `rsp-0026.oberthur.net` | IDEMIA | family | medium |  |
| 51 | `rsp-1001.oberthur.net` | IDEMIA | certificate | high |  |
| 52 | `rsp-1006.oberthur.net` | IDEMIA | family | medium |  |
| 53 | `rsp-1012.oberthur.net` | IDEMIA | certificate | high |  |
| 54 | `rsp-2000.idemia.io` | IDEMIA | family | medium |  |
| 55 | `rsp-3002.idemia.io` | IDEMIA | family | medium |  |
| 56 | `rsp-3022.idemia.io` | IDEMIA | family | medium |  |
| 57 | `rsp-3036.idemia.io` | IDEMIA | family | medium |  |
| 58 | `rsp-3038.idemia.io` | IDEMIA | certificate | high |  |
| 59 | `rsp-3090.idemia.io` | IDEMIA | certificate | high |  |
| 60 | `rsp-3104.idemia.io` | IDEMIA | certificate | high |  |
| 61 | `rsp-4002.idemia.io` | IDEMIA | family | medium |  |
| 62 | `rsp-4004.idemia.io` | IDEMIA | certificate | high |  |
| 63 | `rsp-4008.idemia.io` | IDEMIA | family | medium |  |
| 64 | `rsp.idemia.io` | IDEMIA | family | low |  |
| 65 | `rsp.oberthur.net` | IDEMIA | family | low |  |
| 66 | `t-mobile.idemia.io` | IDEMIA | certificate | high | Mint Mobile via tested |
| 67 | `vfgb.idemia.io` | IDEMIA | family | medium |  |
| 68 | `bt.pr.go-esim.com` | Giesecke+Devrient (G+D) | family | medium |  |
| 69 | `cust-001-v4-prod-atl2.gdsb.net` | Giesecke+Devrient (G+D) | certificate | high | AT&T |
| 70 | `cust-005-v4-prod-atl2.gdsb.net` | Giesecke+Devrient (G+D) | family | medium |  |
| 71 | `cust-007-v4-prod-atl2.gdsb.net` | Giesecke+Devrient (G+D) | family | medium |  |
| 72 | `cust-011-v4-prod-atl2.gdsb.net` | Giesecke+Devrient (G+D) | family | medium |  |
| 73 | `google-fi.pr.go-esim.com` | Giesecke+Devrient (G+D) | family | medium | Google Fi via domainHint |
| 74 | `pr.go-esim.com` | Giesecke+Devrient (G+D) | san | candidate |  |
| 75 | `sm-v4-004-a-gtm.pr.go-esim.com` | Giesecke+Devrient (G+D) | family | medium |  |
| 76 | `sm-v4-007-a-gtm.pr.go-esim.com` | Giesecke+Devrient (G+D) | family | medium | Google Fi via userReport |
| 77 | `sm-v4-018-esa-gtm.pr.go-esim.com` | Giesecke+Devrient (G+D) | certificate | high |  |
| 78 | `sm-v4-019-a-atl2.pr.go-esim.com` | Giesecke+Devrient (G+D) | family | medium |  |
| 79 | `sm-v4-033-a-gtm.pr.go-esim.com` | Giesecke+Devrient (G+D) | family | medium |  |
| 80 | `sm-v4-072-g-gtm.pr.go-esim.com` | Giesecke+Devrient (G+D) | family | medium |  |
| 81 | `sm-v4-072-u-gtm.pr.go-esim.com` | Giesecke+Devrient (G+D) | family | medium | HP Wolf Connect |
| 82 | `sm-v4-077-a-gtm.pr.go-esim.com` | Giesecke+Devrient (G+D) | family | medium |  |
| 83 | `sm-v4-079-a-gtm.pr.go-esim.com` | Giesecke+Devrient (G+D) | family | medium |  |
| 84 | `sm-v4-099-a-gtm.pr.go-esim.com` | Giesecke+Devrient (G+D) | certificate | high |  |
| 85 | `sm-v4-105-a-gtm.pr.go-esim.com` | Giesecke+Devrient (G+D) | certificate | high |  |
| 86 | `sm-v4-124-a-gtm.pr.go-esim.com` | Giesecke+Devrient (G+D) | family | medium | Sky Mobile via userReport |
| 87 | `sm-v4-131-a-gtm.pr.go-esim.com` | Giesecke+Devrient (G+D) | certificate | high |  |
| 88 | `t-mobile.gdsb.net` | Giesecke+Devrient (G+D) | certificate | high | T-Mobile |
| 89 | `usmdp-001-prod-muc1-eb.venyonservices.com` | Giesecke+Devrient (G+D) | family | medium |  |
| 90 | `rsp.truphone.com` | 1GLOBAL | certificate | high | BetterRoaming / Speedtest |
| 91 | `smdp.io` | 1GLOBAL | certificate | high | BetterRoaming |
| 92 | `ctgesim.chinatelecomglobal.com` | Redtea Mobile | san | candidate |  |
| 93 | `esim-eu.redteamobile.com` | Redtea Mobile | san | candidate |  |
| 94 | `esim.idc.md` | Redtea Mobile | san | candidate |  |
| 95 | `lpa.mtxc.eu` | Redtea Mobile | san | candidate |  |
| 96 | `rsp-eu.esim.plus` | Redtea Mobile | san | candidate |  |
| 97 | `rsp-eu.redteamobile.com` | Redtea Mobile | certificate | high | RedteaGO |
| 98 | `rsp-eu.simlessly.com` | Redtea Mobile | certificate | high | WoWo Sim via tested |
| 99 | `rsp.bondio.co` | Redtea Mobile | san | candidate |  |
| 100 | `rsp.bytesim.com` | Redtea Mobile | san | candidate |  |
| 101 | `rsp.cmlink.com` | Redtea Mobile | san | candidate |  |
| 102 | `rsp.dtech-ai.com` | Redtea Mobile | san | candidate |  |
| 103 | `rsp.esim.exchange.com` | Redtea Mobile | san | candidate |  |
| 104 | `rsp.esim.plus` | Redtea Mobile | san | candidate |  |
| 105 | `rsp.esim.pub` | Redtea Mobile | certificate | high |  |
| 106 | `rsp.simsalasim.net` | Redtea Mobile | san | candidate |  |
| 107 | `rsp.tsimtech.com` | Redtea Mobile | san | candidate |  |
| 108 | `rsp01.billionconnect.com` | Redtea Mobile | san | candidate |  |
| 109 | `rsp2.cmlink.com` | Redtea Mobile | san | candidate |  |
| 110 | `rsp3.cmlink.com` | Redtea Mobile | san | candidate |  |
| 111 | `rsp4.cmlink.com` | Redtea Mobile | san | candidate |  |
| 112 | `rsp5.cmlink.com` | Redtea Mobile | san | candidate |  |
| 113 | `rspeu.joyesim.com` | Redtea Mobile | san | candidate |  |
| 114 | `rspeu.joytelecom.net` | Redtea Mobile | certificate | high | Joy Telecom via domainHint |
| 115 | `sim.express` | Redtea Mobile | san | candidate |  |
| 116 | `sim.simify.com` | Redtea Mobile | san | candidate |  |
| 117 | `smdp.global` | Redtea Mobile | san | candidate |  |
| 118 | `consumer.e-sim.global` | Trasna / Workz | certificate | high | BNESIM via tested |
| 119 | `consumer.e-sim.world` | Trasna / Workz | san | candidate |  |
| 120 | `consumer.rsp.global` | Trasna / Workz | certificate | high |  |
| 121 | `consumer.rsp.world` | Trasna / Workz | certificate | high | Roamless via tested |
| 122 | `dpplus1.rsp.global` | Trasna / Workz | san | candidate |  |
| 123 | `dpplus2.rsp.global` | Trasna / Workz | san | candidate |  |
| 124 | `dpplus3.rsp.global` | Trasna / Workz | san | candidate |  |
| 125 | `dpplus4.rsp.global` | Trasna / Workz | san | candidate |  |
| 126 | `dpplus5.rsp.global` | Trasna / Workz | san | candidate |  |
| 127 | `esim.trasna.io` | Trasna / Workz | san | candidate |  |
| 128 | `esim.workz.com` | Trasna / Workz | san | candidate |  |
| 129 | `esim.workz.net` | Trasna / Workz | san | candidate |  |
| 130 | `mesh1.rsp.global` | Trasna / Workz | san | candidate |  |
| 131 | `mesh2.rsp.global` | Trasna / Workz | san | candidate |  |
| 132 | `mesh3.rsp.global` | Trasna / Workz | san | candidate |  |
| 133 | `mesh4.rsp.global` | Trasna / Workz | san | candidate |  |
| 134 | `mesh5.rsp.global` | Trasna / Workz | san | candidate |  |
| 135 | `ais.eastcompeace.com` | Eastcompeace | certificate | high | AIS via domainHint |
| 136 | `ecprsp.eastcompeace.com` | Eastcompeace | certificate | high |  |
| 137 | `global.toprsp.com` | Eastcompeace | certificate | high |  |
| 138 | `mercury.eastcompeace.com` | Eastcompeace | family | medium |  |
| 139 | `mercury.toprsp.com` | Eastcompeace | family | medium |  |
| 140 | `rsp.billionconnect.com` | Eastcompeace | certificate | high | Billion Connect via domainHint |
| 141 | `rsp.esimnext.com` | Eastcompeace | san | candidate |  |
| 142 | `rsp.openroam.com` | Eastcompeace | san | candidate |  |
| 143 | `rsp.roamesim.net` | Eastcompeace | san | candidate |  |
| 144 | `rsp1.cmlink.com` | Eastcompeace | certificate | high | CMLink via domainHint |
| 145 | `secsmsminiapp.eastcompeace.com` | Eastcompeace | family | medium |  |
| 146 | `t2.toprsp.com` | Eastcompeace | family | medium |  |
| 147 | `usimsa.toprsp.com` | Eastcompeace | certificate | high | USIMSA via domainHint |
| 148 | `bait.validspereachdpplus.com` | Valid | certificate | high | BAIT via domainHint |
| 149 | `bics.validspereachdpplus.com` | Valid | certificate | high | BICS via domainHint |
| 150 | `claroargentina.validereachdpplus.com` | Valid | family | medium | Claro Argentina via log |
| 151 | `demo-consumer.validspereachdpplus.com` | Valid | family | medium |  |
| 152 | `firsty.validereachdpplus.com` | Valid | certificate | high | Firsty via domainHint |
| 153 | `millicomelsalvador.validereachdpplus.com` | Valid | family | medium | Tigo El Salvador via domainHint |
| 154 | `mobileuc.validereachdpplus.com` | Valid | certificate | high |  |
| 155 | `viettelvietnam.validspereachdpplus.com` | Valid | certificate | high | Viettel Vietnam via domainHint |
| 156 | `esim.ignitech.com` | NEWare | san | candidate |  |
| 157 | `rsp.eaglesim.com` | NEWare | san | candidate |  |
| 158 | `rsp.esim.exchange` | NEWare | certificate | high |  |
| 159 | `rsp.esimcase.com` | NEWare | certificate | high |  |
| 160 | `rsp.int-montnets.com` | NEWare | san | candidate |  |
| 161 | `rsp.tsimmobile.com` | NEWare | san | candidate |  |
| 162 | `rspas.joyesim.com` | NEWare | san | candidate |  |
| 163 | `rspas.joytelecom.net` | NEWare | san | candidate |  |
| 164 | `dp-plus-par07-01.oasis-smartsim.com` | Oasis Smart SIM | certificate | high |  |
| 165 | `smdp-plus-01.esim-in-a-box.com` | Oasis Smart SIM | san | candidate |  |
| 166 | `smdp-plus-01.esiminabox.com` | Oasis Smart SIM | san | candidate |  |
| 167 | `smdp-plus-in-01.oasis-smartsim.com` | Oasis Smart SIM | family | medium |  |
| 168 | `lpa.live.esimdiscovery.com` | Google | family | medium |  |
| 169 | `lpa.live.esimdiscovery.dev` | Google | family | medium |  |
| 170 | `prod.smdp-plus.rsp.goog` | Google | certificate | high |  |
| 171 | `prod.smds.rsp.goog` | Google | family | medium |  |
| 172 | `az.smdpplus.net` | Nordic eSIM | san | candidate |  |
| 173 | `dk.smdpplus.net` | Nordic eSIM | san | candidate |  |
| 174 | `smdpplus.net` | Nordic eSIM | certificate | high |  |
| 175 | `beeline-con.rsp.a1-systems.com` | A1 Systems | family | medium | Beeline via domainHint |
| 176 | `sbermobile-con.rsp.a1-systems.com` | A1 Systems | family | medium | SberMobile via domainHint |
| 177 | `tinkoff-con.rsp.a1-systems.com` | A1 Systems | family | medium |  |
| 178 | `rsp-0001.linksfield.net` | Links Field | family | medium |  |
| 179 | `rsp-0002.linksfield.net` | Links Field | family | medium |  |
| 180 | `smdp-plus-0.eu.cd.rsp.kigen.com` | Kigen | family | medium |  |
| 181 | `smdp-plus-1.eu.cd.rsp.kigen.com` | Kigen | family | medium |  |
| 182 | `kcell.esim-rsp.com` | Torrion River | certificate | high | Kcell via domainHint |
| 183 | `smdp.airtel.in` | Airtel | none | medium | Airtel via domainHint |
| 184 | `telkomsel-idn.rsp.instant-connectivity.com` | BaliSIM | none | documented | BaliSIM via installGuide |
| 185 | `esim.yhdzd.chinamobile.com:8001` | China Mobile | none | medium |  |
| 186 | `lpa.ds.gsma.com` | GSMA | family | medium |  |
| 187 | `testsmdpplus.infineon.com` | Infineon | family | medium |  |
| 188 | `esim.mts.ru` | MTS | none | medium | MTS via domainHint |
| 189 | `nepaltelecomnpl.rsp.instant-connectivity.com` | Nepal Telecom | none | medium | Nepal Telecom via domainHint |
| 190 | `rsp.redteago.com` | RedteaGO | none | medium | RedteaGO via domainHint |
| 191 | `smdprd.jio.com` | Reliance Jio | none | medium | Reliance Jio via domainHint |
| 192 | `rsp.tele2.ru` | Tele2 / t2 | none | medium | Tele2 / t2 via domainHint |
| 193 | `zain.esim.com.sa` | Zain Saudi Arabia | none | medium | Zain Saudi Arabia via domainHint |
| 194 | `itelvnm.rsp.instant-connectivity.com` | laos-esim.com | none | documented | laos-esim.com via installGuide |
| 195 | `smdpp.test.rsp.sysmocom.de` | sysmocom | family | medium |  |
| 196 | `console.wdrsp.com` | unattributed | none | medium |  |
| 197 | `dp-plus.china-xinghan.com` | unattributed | none | medium |  |
| 198 | `esim.wo.com.cn` | unattributed | none | medium |  |
| 199 | `esimapple.crm.189.cn` | unattributed | none | medium |  |
| 200 | `rsp.esim.whty.com.cn` | unattributed | none | medium |  |
| 201 | `rsp.novacard.ru` | unattributed | none | medium |  |
| 202 | `www.esimtest.chinattl.cn` | unattributed | none | medium |  |

## The domains behind them

These are the registrable domains the catalogue rests on, with what each attribution is based on. `platform` is the vendor that writes and hosts the SM-DP+ software. `provider` is an eSIM brand or MVNO that runs a platform under its own name. `operator` is a mobile network operator doing the same.

| Domain | Owner | Type | Platform | What the attribution rests on |
|---|---|---|---|---|
| `comviva.com` | Comviva | platform | Comviva eSIM platform | Corporate domain of Comviva (Tech Mahindra). |
| `eastcompeace.com` | Eastcompeace | platform |  | Corporate domain of Eastcompeace (东信和平). |
| `gi-de.com` | Giesecke+Devrient | platform | G+D AirOn / eSIM Management | Corporate domain of Giesecke+Devrient. |
| `idemia.com` | IDEMIA | platform |  | Corporate domain of IDEMIA. |
| `infineon.com` | Infineon | platform |  | Corporate domain of Infineon Technologies. |
| `kigen.com` | Kigen | platform | Kigen eSIM services | Corporate domain of Kigen (spun out of Arm). |
| `montymobile.com` | Monty Mobile | platform | Monty Mobile RSP | Corporate domain of Monty Mobile. |
| `oasis-smartsim.com` | Oasis Smart SIM | platform | Oasis Smart SIM RSP | Corporate domain of Oasis Smart SIM (Tessi group). |
| `redteamobile.com` | Redtea Mobile | platform | Redtea Mobile RSP | Corporate domain of Redtea Mobile (红茶移动). |
| `simhub.io` | SIMHub | platform |  | Domain used by SIMHub eSIM tooling. |
| `gemalto.com` | Thales | platform | Thales (formerly Gemalto) eSIM Management | Legacy Gemalto domain; Gemalto is now part of Thales. |
| `ondemandconnectivity.com` | Thales | platform | Thales On-Demand Connectivity (ODC) | On-Demand Connectivity is the hosted RSP platform of Thales (formerly Gemalto); certificates on *.prod.ondemandconnectivity.com are issued to THALES SA. |
| `thalesgroup.com` | Thales | platform | Thales (formerly Gemalto) eSIM Management | Corporate domain of Thales, which acquired Gemalto’s digital identity business in 2019. |
| `valid.com` | Valid | platform | Valid eSIM platform | Corporate domain of Valid S.A. |
| `workz.com` | Workz Group | platform | Workz eSIM platform | Corporate domain of Workz Group. |
| `achelos.de` | achelos | platform | achelos eSIM test/RSP tooling | Corporate domain of achelos GmbH. |
| `1global.com` | 1GLOBAL | provider |  | Corporate domain of 1GLOBAL. |
| `truphone.com` | 1GLOBAL (formerly Truphone) | provider |  | Truphone rebranded to 1GLOBAL in 2023; rsp.truphone.com is the SM-DP+ used by its widely circulated public speed-test profile. |
| `5ber.com` | 5ber | provider |  | Corporate domain of 5ber (eSIM card products). |
| `airalo.com` | Airalo | provider |  | Corporate domain of Airalo. |
| `bics.com` | BICS | provider |  | Corporate domain of BICS (Proximus group). |
| `flexiroam.com` | Flexiroam | provider |  | Corporate domain of Flexiroam. |
| `gigsky.com` | GigSky | provider |  | Corporate domain of GigSky. |
| `holafly.com` | Holafly | provider |  | Corporate domain of Holafly. |
| `instabridge.com` | Instabridge | provider |  | Corporate domain of Instabridge. |
| `jtglobal.com` | JT Group | provider |  | Corporate domain of JT (Jersey Telecom). |
| `keepgo.com` | Keepgo | provider |  | Corporate domain of Keepgo. |
| `mobimatter.com` | MobiMatter | provider |  | Corporate domain of MobiMatter. |
| `transatel.com` | Transatel (NTT Group) | provider |  | Corporate domain of Transatel. |
| `ubigi.com` | Ubigi (Transatel, NTT Group) | provider |  | Ubigi is Transatel’s consumer eSIM brand; Transatel is part of NTT. |
| `esimgo.com` | eSIM Go | provider |  | Corporate domain of eSIM Go. |
| `a1.net` | A1 Telekom Austria | operator |  | Corporate domain of A1 Telekom Austria. |
| `att.com` | AT&T | operator |  | Corporate domain of AT&T. |
| `bell.ca` | Bell Canada | operator |  | Corporate domain of Bell Canada. |
| `airtel.com` | Bharti Airtel | operator |  | Corporate domain of Bharti Airtel. |
| `chinamobile.com` | China Mobile | operator |  | Corporate domain of China Mobile. |
| `chinatelecom.com.cn` | China Telecom | operator |  | Corporate domain of China Telecom. |
| `chinaunicom.com` | China Unicom | operator |  | Corporate domain of China Unicom. |
| `chunghwa.com.tw` | Chunghwa Telecom | operator |  | Corporate domain of Chunghwa Telecom. |
| `telekom.de` | Deutsche Telekom | operator |  | Corporate domain of Deutsche Telekom. |
| `ee.co.uk` | EE (BT Group) | operator |  | Corporate domain of EE. |
| `hkt.com` | HKT | operator |  | Corporate domain of HKT (PCCW). |
| `kddi.com` | KDDI | operator |  | Corporate domain of KDDI. |
| `kt.com` | KT | operator |  | Corporate domain of KT Corporation. |
| `lguplus.co.kr` | LG U+ | operator |  | Corporate domain of LG U+. |
| `docomo.ne.jp` | NTT Docomo | operator |  | Corporate domain of NTT Docomo. |
| `o2.co.uk` | O2 UK (VMO2) | operator |  | Corporate domain of O2 UK. |
| `optus.com.au` | Optus | operator |  | Corporate domain of Optus. |
| `orange.com` | Orange | operator |  | Corporate domain of Orange S.A. |
| `rakuten.co.jp` | Rakuten Mobile | operator |  | Corporate domain of Rakuten. |
| `jio.com` | Reliance Jio | operator |  | Corporate domain of Reliance Jio. |
| `rogers.com` | Rogers | operator |  | Corporate domain of Rogers Communications. |
| `sktelecom.com` | SK Telecom | operator |  | Corporate domain of SK Telecom. |
| `singtel.com` | Singtel | operator |  | Corporate domain of Singtel. |
| `softbank.jp` | SoftBank | operator |  | Corporate domain of SoftBank. |
| `swisscom.ch` | Swisscom | operator |  | Corporate domain of Swisscom. |
| `tmobile.com` | T-Mobile US | operator |  | Corporate domain of T-Mobile US. |
| `telus.com` | TELUS | operator |  | Corporate domain of TELUS. |
| `tele2.com` | Tele2 | operator |  | Corporate domain of Tele2. |
| `telefonica.com` | Telefónica | operator |  | Corporate domain of Telefónica. |
| `telstra.com` | Telstra | operator |  | Corporate domain of Telstra. |
| `three.co.uk` | Three UK | operator |  | Corporate domain of Three UK. |
| `verizonwireless.com` | Verizon | operator |  | Corporate domain of Verizon Wireless. |
| `vodafone.com` | Vodafone | operator |  | Corporate domain of Vodafone Group. |
| `csl.com.hk` | csl (HKT) | operator |  | Corporate domain of csl Mobile. |

## Reading an address you have not seen before

1. **Take the registrable domain.** Everything from the label before the public suffix: `celitech.idemia.io` becomes `idemia.io`, `cust-011-v4-prod-atl2.gdsb.net` becomes `gdsb.net`.
2. **Look for a family.** A vendor usually serves from two or three domains, not hundreds, so the tables above cover most of what arrives in a real activation code. `idemia` in the string is IDEMIA. `ondemandconnectivity` is Thales. `gdsb` is G+D.
3. **Read the certificate.** Fetch the endpoint's RSP certificate and read the subject organisation and the `O` of the issuer. `O=THALES SA` under `CN=GSMA Association - RSP2 Root CI1` is Thales, whatever the hostname says. This is the strongest evidence there is, because the GSMA CI only issues to a vetted party.
4. **Check for an operator label.** `2.vzw.otgeuicc.com` is Thales infrastructure with Verizon's name on the front. `<operator>.rsp.instant-connectivity.com` and `smdp.airtel.in` are operators running somebody else's platform. The platform named in the certificate is the operator of the server; the label is the customer.
5. **Fall back to nothing.** If none of that holds, say the address is unattributed. Seven addresses in the catalogue are in that state and they are listed as such, not guessed.

## Where the brand is not the platform

The most common mistake is to read the first label as the owner. These are the same platform with different names on the front, and the platform is what you get when something goes wrong:

- `rsp.truphone.com` is 1GLOBAL, because 1GLOBAL bought Truphone. A travel brand buying capacity there does not become the operator of the server.
- `celitech.idemia.io` is IDEMIA. CELITECH rents it.
- `bics.validspereachdpplus.com` is Valid, hosting BICS.
- `sbermobile-con.rsp.a1-systems.com` is A1 Systems, hosting SberMobile.
- `telkomsel-idn.rsp.instant-connectivity.com` is the instant-connectivity platform, hosting an Indonesian reseller.

Conversely, an operator with its own domain and its own platform really is the operator of that SM-DP+: `smdp.airtel.in`, `esim.mts.ru`, `rsp.tele2.ru`, `smdprd.jio.com`, `zain.esim.com.sa`. They appear in the catalogue with the operator named.

## Test and lab addresses

Some addresses in the wild are not commercial endpoints and should not be read as a market signal: `lpa.ds.gsma.com` (GSMA's own discovery and test service), `smdpp.test.rsp.sysmocom.de` (sysmocom's lab SIMs), `testsmdpplus.infineon.com` (chip vendor conformance testing), and Google's `lpa.live.esimdiscovery.com` and `lpa.live.esimdiscovery.dev`, which exist so that a device can be walked through the download flow without a real subscription.

## What this page is not

- It is not a list of which profiles work where. An SM-DP+ address says who runs the server, nothing about coverage, pricing or the network behind the profile.
- It is not authoritative. No GSMA register of SM-DP+ operators is published, so the attributions are evidence and confidence, not a lookup table from the spec. A `medium` entry is a hostname under a vendor's domain; a `high` entry is a certificate.
- It ages. Addresses are stood up and retired, and a certificate read in June 2026 may be replaced by December. Dates are given above so a reader can tell how old an answer is.

## Provenance

The catalogue and the domain table are the ones published by [esim2qr.com](https://esim2qr.com/), which serves an SM-DP+ lookup alongside its QR generator. Their build carries the dates quoted here. The attribution rules, the confidence vocabulary and the register itself come from that source; the reading of them is this page.
