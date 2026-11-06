---
layout: default
title: "GCF RSP Register, Condensed (machine-readable)"
description: "One row per GCF eSIM (RSP) certified module: manufacturer, model, certification date, declared RSP flavour (SGP.22 consumer / SGP.02 M2M), eUICC mounting, bands, vendor page, datasheet and AT command manual URLs, and GCF reference. Plus every RSP certification and compliance declaration. For programmatic or LLM extraction."
---

# GCF RSP Register, Condensed

Snapshot harvested 2026-11-06. Unofficial mirror of GCF's public
registers: [https://www.globalcertificationforum.org/gcf-certified-products/rsp-certifications.html](https://www.globalcertificationforum.org/gcf-certified-products/rsp-certifications.html).
GCF is the authority. Full page with search and filters: [GCF-certified eSIM modules]({{ site.baseurl }}/docs/gcf-rsp-modules)

Columns: **Manufacturer**, **Model**, **Certified** (ISO date of the latest
certification), **N** (how many certification records exist for that module),
**RSP** (declared flavours), **eUICC** (soldered / removable / both), **Bands**
(declared band count by family), **Release** (3GPP release declared), **Vendor**
(product page), **Datasheet**, **AT** (AT command manual), **GCF ref**.

`-` in the Vendor, Datasheet or AT column means no public URL was found for that
module; the full page carries the reason on hover. Empty is a finding, not a gap
in the data: several modules here are ODM or automotive parts whose documents are
NDA-only.

## Certified embedded modules (34)

A module is listed here when GCF certified it with an embedded eUICC. `RSP` and
`eUICC` are independent axes: consumer RSP on a soldered eUICC is a normal MFF2
design, not a contradiction. A row with no bands is usually an eUICC chip
certified as a component rather than a modem.

| Manufacturer | Model | Certified | N | RSP | eUICC | Bands | Release | Vendor | Datasheet | AT | GCF ref |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Kontron Europe GmbH | AV62RCL-W | 2026-08-10 | 1 | SGP.02 | removable | LTE 15 / WCDMA 3 / GSM 4 | Rel-12 | - | - | - | 13910 |
| Kontron Europe GmbH | AV62MB-W | 2026-08-10 | 1 | SGP.02 | removable | LTE 20 / WCDMA 4 / GSM 4 | Rel-12 | - | - | - | 13909 |
| Kontron Europe GmbH | AV62MB-E | 2026-08-07 | 1 | SGP.02 | removable | LTE 12 / WCDMA 3 / GSM 2 | Rel-12 | - | - | - | 13908 |
| SIMCom Wireless Solutions Limited | SIM7600G | 2026-07-30 | 1 | SGP.02 | removable | LTE 9 / WCDMA 2 / GSM 2 | Rel-10 | https://www.simcom.com/product/SIM7600G.html | https://www.tme.com/Document/29390ba2a617ac7afa0f581de3b295ee/SIM7600G.pdf | https://files.waveshare.com/upload/a/af/SIM7500_SIM7600_Series_AT_Command_Manual_V3.00.pdf | 13886 |
| Rolling Wireless S.a.r.l. | RN941R | 2026-07-28 | 1 | SGP.02 | both | LTE 27 / WCDMA 4 / GSM 4 | Rel-10 | https://www.rollingwireless.com/en/solutions/5g-solutions/rn93xx-rn94xx | - | - | 13691 |
| Rolling Wireless S.a.r.l. | RN947R | 2026-07-28 | 1 | SGP.02 | both | LTE 27 / WCDMA 4 / GSM 4 | Rel-10 | https://www.rollingwireless.com/en/solutions/5g-solutions/rn93xx-rn94xx | - | - | 13875 |
| Rolling Wireless S.a.r.l. | RN941W | 2026-07-28 | 1 | SGP.02 | both | LTE 27 / WCDMA 4 / GSM 4 | Rel-10 | https://www.rollingwireless.com/en/solutions/5g-solutions/rn93xx-rn94xx | - | - | 13692 |
| SIMCom Wireless Solutions Limited | SIM7600G-H | 2026-07-06 | 1 | SGP.02 | removable | LTE 9 / WCDMA 2 / GSM 2 | Rel-10 | https://www.simcom.com/product/SIM7600G-H.html | https://files.waveshare.com/upload/a/a0/SIM7600G-H_SPEC_EN_20190731.pdf | https://files.waveshare.com/upload/a/af/SIM7500_SIM7600_Series_AT_Command_Manual_V3.00.pdf | 13870 |
| Sierra Wireless, ULC | EM7590 | 2026-05-01 | 3 | SGP.22 | both | LTE 25 / WCDMA 6 | - | https://www.sierrawireless.com/iot-modules/4g-modules/em7590/ | https://static.onlogic.com/resources/manuals/41114425%20EM759X%20Product%20Technical%20Specification%20r9.pdf | https://www.bipom.com/documents/sierra/41111748%20AirPrime%20EM75XX%20AT%20Command%20Reference%20r2.pdf | 13701, 12901, 12021 |
| Sierra Wireless, ULC | EM7595 | 2026-05-01 | 3 | SGP.22 | both | LTE 25 / WCDMA 6 | - | https://www.sierrawireless.com/iot-modules/4g-modules/em7595/ | https://static.onlogic.com/resources/manuals/41114425%20EM759X%20Product%20Technical%20Specification%20r9.pdf | https://www.bipom.com/documents/sierra/41111748%20AirPrime%20EM75XX%20AT%20Command%20Reference%20r2.pdf | 13702, 12902, 12022 |
| Iridium Satellite LLC | 9604 | 2026-04-29 | 1 | SGP.02 | removable | — | Not Supported | https://www.iridium.com/9604 | https://www.groundcontrol.com/wp-content/uploads/2026/07/Iridium-9604-Data-Sheet.pdf | - | 13698 |
| LG Innotek Co., Ltd. | LTD-AN2000 | 2026-04-24 | 1 | SGP.22 + SGP.02 | both | LTE 14 / WCDMA 2 | - | - | - | - | 13473 |
| Compal Electronics, Inc. | RMM-G4 | 2026-01-20 | 1 | SGP.22 | soldered | LTE 28 / WCDMA 4 | - | https://www.compal.com/5g/ | - | - | 13314 |
| SIMCom Wireless Solutions Limited | E7088 | 2025-10-25 | 1 | SGP.02 | removable | — | Rel-14 | - | - | - | 13407 |
| SIMCom Wireless Solutions Limited | E7080 | 2025-10-20 | 1 | SGP.02 | removable | — | Rel-14 | https://www.simcom.com/product/E7080.html | - | - | 13341 |
| LG Electronics Inc | TM13LNEUJL0 | 2025-10-06 | 1 | SGP.02 | soldered | LTE 10 / WCDMA 3 / GSM 3 | Rel-8 | - | - | - | 13282 |
| Rolling Wireless S.a.r.l. | RN934R | 2025-07-25 | 1 | SGP.02 | both | LTE 6 / WCDMA 2 / GSM 2 | Rel-10 | https://www.rollingwireless.com/en/solutions/5g-solutions/rn93xx-rn94xx | - | - | 13123 |
| Rolling Wireless S.a.r.l. | RN937N | 2025-07-25 | 1 | SGP.02 | both | LTE 8 / WCDMA 3 | Rel-10 | https://www.rollingwireless.com/en/solutions/5g-solutions/rn93xx-rn94xx | - | - | 13124 |
| Rolling Wireless S.a.r.l. | RN934V | 2025-07-25 | 1 | SGP.02 | both | LTE 10 / WCDMA 2 / GSM 2 | Rel-10 | https://www.rollingwireless.com/en/solutions/5g-solutions/rn93xx-rn94xx | - | - | 13125 |
| Rolling Wireless S.a.r.l. | RN932V | 2025-07-25 | 1 | SGP.02 | both | LTE 14 | Rel-10 | https://www.rollingwireless.com/en/solutions/5g-solutions/rn93xx-rn94xx | - | - | 13126 |
| Rolling Wireless S.a.r.l. | RN934N | 2025-07-23 | 1 | SGP.02 | both | LTE 6 / WCDMA 2 / GSM 2 | Rel-10 | https://www.rollingwireless.com/en/solutions/5g-solutions/rn93xx-rn94xx | - | - | 13122 |
| LG Innotek Co., Ltd. | LTD-OA1000 | 2025-02-14 | 1 | SGP.02 | removable | LTE 8 / WCDMA 3 / GSM 3 | Rel-12 | - | - | - | 12732 |
| LG Innotek Co., Ltd. | LTD-VL4000 | 2025-02-07 | 1 | SGP.02 | removable | LTE 5 | Rel-12 | - | - | - | 12728 |
| LG Innotek Co., Ltd. | LTD-FA1000 | 2025-01-22 | 1 | SGP.02 | removable | LTE 9 / WCDMA 2 / GSM 2 | Rel-12 | - | - | - | 12683 |
| Askey Computer Corporation | NMQ2210 | 2025-01-16 | 1 | SGP.02 | soldered | LTE 10 | - | - | - | - | 12685 |
| LG Innotek Co., Ltd. | LTD-GN3000 | 2024-11-11 | 1 | SGP.02 | removable | LTE 21 / WCDMA 3 / GSM 4 | Rel-14 | - | - | - | 12597 |
| LG Innotek Co., Ltd. | LTD-GN2000 | 2024-11-08 | 1 | SGP.02 | removable | LTE 11 / WCDMA 3 / GSM 2 | Rel-14 | - | - | - | 12581 |
| Compal Electronics, Inc. | RMM-G1 | 2024-07-29 | 1 | SGP.22 | soldered | LTE 28 / WCDMA 5 | - | https://www.compal.com/5g/ | https://fccid.io/GKRRMMG1/User-Manual/RMM-G1-User-Manual-20240712-7473455.pdf | - | 12423 |
| Trasna Solutions FZ-LLC | LEXI-R520 | 2024-07-18 | 1 | SGP.02 | removable | — | - | https://trasna.io/product/lexi-r520-cellular-iot-module | https://cdn.prod.website-files.com/66db0a16ec359c496fe320da/684c3eaf14d43bd68cc5b8dd_LEXI-R520%20data%20sheet.pdf | https://download.mikroe.com/documents/datasheets/SARA-R5-LEXI-R5_AT_Commands.pdf | 12278 |
| Compal Electronics, Inc. | EXM-G1A | 2024-04-18 | 1 | SGP.22 | soldered | WCDMA 6 | - | https://www.compal.com/5g/ | - | - | 12171 |
| Rolling Wireless S.a.r.l. | RN934A | 2024-04-10 | 1 | SGP.02 | both | WCDMA 2 / GSM 2 | Rel-16 | https://www.rollingwireless.com/en/solutions/5g-solutions/rn93xx-rn94xx | - | - | 11679 |
| Trasna Solutions FZ-LLC | SARA-R520M10 | 2024-03-05 | 1 | SGP.02 | removable | — | - | https://trasna.io/product/sara-r52-cellular-iot-module | https://cdn.prod.website-files.com/66db0a16ec359c496fe320da/684c3ec9df6101c95f51cd4b_SARA-R52%20data%20sheet.pdf | https://download.mikroe.com/documents/datasheets/SARA-R5-LEXI-R5_AT_Commands.pdf | 11884 |
| Trasna Solutions FZ-LLC | SARA-R520 | 2024-03-05 | 1 | SGP.02 | removable | — | - | https://trasna.io/product/sara-r52-cellular-iot-module | https://cdn.prod.website-files.com/66db0a16ec359c496fe320da/684c3ec9df6101c95f51cd4b_SARA-R52%20data%20sheet.pdf | https://download.mikroe.com/documents/datasheets/SARA-R5-LEXI-R5_AT_Commands.pdf | 11885 |
| Trasna Solutions FZ-LLC | SARA-R520M10X | 2024-03-05 | 1 | SGP.02 | removable | — | - | https://trasna.io/product/sara-r52-cellular-iot-module | https://cdn.prod.website-files.com/66db0a16ec359c496fe320da/684c3ec9df6101c95f51cd4b_SARA-R52%20data%20sheet.pdf | https://download.mikroe.com/documents/datasheets/SARA-R5-LEXI-R5_AT_Commands.pdf | 11883 |

## All RSP product certifications (606)

Every product in GCF's eSIM (RSP) certification register.

| Manufacturer | Model | Marketing name | Certified | RSP | eUICC | GCF ref |
|---|---|---|---|---|---|---|
| weavix Inc | WT02 | Walt 5G | 2026-11-06 | SGP.22 + SGP.32 | soldered | 14111 |
| Motorola Mobility LLC | XT2625-16 | XT2625-16 | 2026-11-05 | SGP.22 | soldered | 14125 |
| Crosscall SAS | 82866-1 | Core-X7 | 2026-10-20 | SGP.22 | soldered | 14081 |
| Honor Device Co Ltd | WKL-N59 | HONOR Magic9 Pro Max | 2026-10-19 | SGP.22 | soldered | 14085 |
| Motorola Mobility LLC | XT2625-11 (Type Name MC46F) | XT2625-11 | 2026-10-09 | SGP.22 | soldered | 14075 |
| Samsung Electronics Co Ltd | NP755XSB, NP759XSB | NP755XSB, NP759XSB | 2026-09-21 | SGP.22 | soldered | 14054 |
| Juniper Systems Inc | ALT1 | ALTA | 2026-09-18 | SGP.22 | soldered | 14049 |
| Elo Touch Solutions Inc | EMC-M61SC | Elo Pay M61C | 2026-09-15 | SGP.22 | soldered | 14046 |
| Huawei Technologies Co., Ltd. | NIZ-AL00 | HUAWEI WATCH 6, HUAWEI WATCH 6 Pro | 2026-09-09 | SGP.22 | soldered | 14034 |
| Huawei Technologies Co., Ltd. | LEB-AL10 | HUAWEI WATCH 6 Pro | 2026-09-09 | SGP.22 | soldered | 14033 |
| WNC Corporation | TELE2 | TELE2 | 2026-09-04 | SGP.02 | soldered | 14020 |
| Motorola Mobility LLC | XT2651V | XT2651V | 2026-09-04 | SGP.22 | soldered | 14026 |
| vivo Mobile Communication Co., Ltd. | V2622 | X500 Pro | 2026-09-02 | SGP.22 | soldered | 14003 |
| vivo Mobile Communication Co., Ltd. | V2559 | X Fold6 | 2026-09-02 | SGP.22 | soldered | 14001 |
| vivo Mobile Communication Co., Ltd. | V2621 | X500 Pro | 2026-09-02 | SGP.22 | soldered | 14002 |
| Honor Device Co Ltd | BSN-NX1M | HONOR Magic9 Lite+ | 2026-08-28 | SGP.22 | soldered | 13995 |
| LG Electronics Inc | TFVWAIBG1F8 | TFVWAIBG1F8 | 2026-08-24 | SGP.02 | soldered | 13986 |
| LG Electronics Inc | TFVWAIBG1FP | TFVWAIBG1FP | 2026-08-24 | SGP.02 | soldered | 13987 |
| vivo Mobile Communication Co., Ltd. | V2615 | V70 Lite 5G | 2026-08-21 | SGP.22 | soldered | 13976 |
| vivo Mobile Communication Co., Ltd. | V2637 | V70 Lite 5G | 2026-08-21 | SGP.22 | soldered | 13975 |
| vivo Mobile Communication Co., Ltd. | V2610 | X500 Pro Max | 2026-08-20 | SGP.22 | soldered | 13970 |
| Plaud Inc. | PB0100 | Plaud One | 2026-08-19 | SGP.22 | not declared | 13966 |
| Kontron Europe GmbH | AV62RCL-W | Kontron AV62RCL-W | 2026-08-10 | SGP.02 | removable | 13910 |
| Kontron Europe GmbH | AV62MB-W | Kontron AV62MB-W | 2026-08-10 | SGP.02 | removable | 13909 |
| Motorola Mobility LLC | XT2629-2 | XT2629-2 | 2026-08-08 | SGP.22 | soldered | 13925 |
| LG Electronics Inc | TFVWAIBG1F9 | TFVWAIBG1F9 | 2026-08-07 | SGP.02 | soldered | 13920 |
| Kontron Europe GmbH | AV62MB-E | Kontron AV62MB-E | 2026-08-07 | SGP.02 | removable | 13908 |
| LG Electronics Inc | TFVWAIBG1FO | TFVWAIBG1FO | 2026-08-06 | SGP.02 | soldered | 13913 |
| Motorola Mobility LLC | XT2659V | XT2659V | 2026-08-04 | SGP.22 | soldered | 13904 |
| Datalogic S.r.l. | CMFSNRTYPE051AC65X22GF2ANWRD | FALCON X65 | 2026-08-04 | SGP.22 | soldered | 13895 |
| Motorola Mobility LLC | XT2625-14(Type Name MC467) | XT2625-14 | 2026-08-04 | SGP.22 | soldered | 13903 |
| Motorola Mobility LLC | XT2625-13 | XT2625-13 | 2026-08-04 | SGP.22 | soldered | 13899 |
| Datalogic S.r.l. | CMFSNRTYPE051AC65X22GN2ANWRD | FALCON X65 | 2026-08-04 | SGP.22 | soldered | 13897 |
| Datalogic S.r.l. | CMFSNRTYPE051AC65AW2GS2ANWRD | FALCON X65 | 2026-08-04 | SGP.22 | soldered | 13894 |
| Datalogic S.r.l. | CMFSNRTYPE051AC65AW2GN2ANWRD | FALCON X65 | 2026-08-04 | SGP.22 | soldered | 13896 |
| Datalogic S.r.l. | CMFSNR | FALCON X65 | 2026-08-04 | SGP.22 | soldered | 13898 |
| Motorola Mobility LLC | XT2647-1 | XT2647-1 | 2026-08-03 | SGP.22 | soldered | 13890 |
| Motorola Mobility LLC | XT2647V | XT2647V | 2026-08-03 | SGP.22 | soldered | 13892 |
| Motorola Mobility LLC | XT2647-4 (Type Name AC46A) | XT2647-4 | 2026-08-03 | SGP.22 | soldered | 13863 |
| TCL Communication Ltd | T952K | T952K | 2026-07-30 | SGP.22 | soldered | 13885 |
| SIMCom Wireless Solutions Limited | SIM7600G | SIM7600G | 2026-07-30 | SGP.02 | removable | 13886 |
| TCL Communication Ltd | T852K | T852K | 2026-07-30 | SGP.22 | soldered | 13872 |
| Rolling Wireless S.a.r.l. | RN941R | RN941R | 2026-07-28 | SGP.02 | both | 13691 |
| Rolling Wireless S.a.r.l. | RN947R | RN947R | 2026-07-28 | SGP.02 | both | 13875 |
| Rolling Wireless S.a.r.l. | RN941W | RN941W | 2026-07-28 | SGP.02 | both | 13692 |
| TCL Communication Ltd | T853K | T853K | 2026-07-24 | SGP.22 | soldered | 13840 |
| TCL Communication Ltd | MT48EX | MT48EX | 2026-07-21 | SGP.22 | soldered | 13871 |
| Datalogic S.r.l. | CMFQNR | SKORPIO X45 | 2026-07-17 | SGP.22 | soldered | 13788 |
| Datalogic S.r.l. | CMFSNRTYPE051AC65X22GF2ANWLC | FALCON X65 | 2026-07-15 | SGP.22 | soldered | 13805 |
| Samsung Electronics Co Ltd | SM-X946B | SM-X946B | 2026-07-15 | SGP.22 | soldered | 13858 |
| Samsung Electronics Co Ltd | SM-X846E | SM-X846E | 2026-07-15 | SGP.22 | soldered | 13860 |
| Samsung Electronics Co Ltd | SM-S741B/DS, SM-S741B | SM-S741B/DS, SM-S741B | 2026-07-14 | SGP.22 | soldered | 13854 |
| SIMCom Wireless Solutions Limited | SIM7600G-H | SIM7600G-H | 2026-07-06 | SGP.02 | removable | 13870 |
| Xiaomi Communications | 2609FRA74T | REDMI Note 17 Pro Max 5G | 2026-07-06 | SGP.22 | soldered | 13836 |
| Realme Chongqing Mobile Telecommunications Corporation Ltd. | RMX5120 | realme 16 Pro 5G | 2026-07-03 | SGP.22 | soldered | 13822 |
| Xiaomi Communications | 2609FRA74G | REDMI Note 17 Pro Max 5G | 2026-07-01 | SGP.22 | soldered | 13826 |
| Realme Chongqing Mobile Telecommunications Corporation Ltd. | RMX5171 | realme 16 5G | 2026-07-01 | SGP.22 | soldered | 13817 |
| Xiaomi Communications | 2607DRA18T | REDMI Note 17 Pro 5G | 2026-06-26 | SGP.22 | soldered | 13810 |
| Microsoft Corporation | 2150 | Surface 2-in-1 | 2026-06-25 | SGP.22 | soldered | 13802 |
| Google LLC | GUJ0N | GUJ0N | 2026-06-23 | SGP.22 | both | 13798 |
| Google LLC | GBC0H | GBC0H | 2026-06-23 | SGP.22 | both | 13790 |
| Google LLC | GPQQ7 | GPQQ7 | 2026-06-23 | SGP.22 | both | 13794 |
| Google LLC | GM45K | GM45K | 2026-06-23 | SGP.22 | both | 13797 |
| Google LLC | G4HCD | G4HCD | 2026-06-23 | SGP.22 | both | 13796 |
| Google LLC | G7SWN | G7SWN | 2026-06-23 | SGP.22 | both | 13792 |
| Google LLC | GZDQ6 | GZDQ6 | 2026-06-23 | SGP.22 | both | 13799 |
| Google LLC | G25QD | G25QD | 2026-06-19 | SGP.22 | soldered | 13780 |
| Google LLC | G0F3Y | G0F3Y | 2026-06-19 | SGP.22 | soldered | 13782 |
| Xiaomi Communications | 2607DRA18G | REDMI Note 17 Pro 5G | 2026-06-17 | SGP.22 | soldered | 13785 |
| Samsung Electronics Co Ltd | SM-L345F | SM-L345F | 2026-06-05 | SGP.22 | soldered | 13770 |
| Samsung Electronics Co Ltd | SM-L715F | SM-L715F | 2026-06-05 | SGP.22 | soldered | 13768 |
| Samsung Electronics Co Ltd | SM-L355F | SM-L355F | 2026-06-05 | SGP.22 | soldered | 13769 |
| Samsung Electronics Co Ltd | SM-F971B | SM-F971B | 2026-05-28 | SGP.22 | soldered | 13747 |
| Samsung Electronics Co Ltd | SM-F976B | SM-F976B | 2026-05-28 | SGP.22 | soldered | 13746 |
| Samsung Electronics Co Ltd | SM-F776B | SM-F776B | 2026-05-28 | SGP.22 | soldered | 13749 |
| Zebra Technologies Corporation | TCW01G | TC201, HC201, HC501 | 2026-05-08 | SGP.22 | both | 13706 |
| Sierra Wireless, ULC | EM7590 | Sierra Wireless EM7590 | 2026-05-01 | SGP.22 | both | 13701 |
| Sierra Wireless, ULC | EM7595 | Sierra Wireless EM7595 | 2026-05-01 | SGP.22 | both | 13702 |
| Iridium Satellite LLC | 9604 | Iridium 9604 | 2026-04-29 | SGP.02 | removable | 13698 |
| Motorola Mobility LLC | XT2609-1 | XT2609-1 | 2026-04-24 | SGP.22 | soldered | 13689 |
| LG Innotek Co., Ltd. | LTD-AN2000 | LTD-AN2000 | 2026-04-24 | SGP.22 + SGP.02 | both | 13473 |
| Motorola Mobility LLC | XT2609V | XT2609V | 2026-04-24 | SGP.22 | soldered | 13690 |
| Zebra Technologies Corporation | TC101B | TC101 | 2026-04-22 | SGP.22 | removable | 13686 |
| Motorola Mobility LLC | XT2659-1 | XT2659-1 | 2026-04-16 | SGP.22 | soldered | 13674 |
| Motorola Mobility LLC | XT2651-2 | XT2651-2 | 2026-04-16 | SGP.22 | soldered | 13678 |
| Motorola Mobility LLC | XT2659-3 (type Name MC468) | XT2659-3 | 2026-04-16 | SGP.22 | soldered | 13677 |
| Lenovo Mobile Communication Technology Co Ltd | TB353ZU | ThinkTab X11 Gen 1 | 2026-04-07 | SGP.22 | soldered | 13658 |
| Motorola Mobility LLC | XT2625-3, XT2625-3 [DS] (Type Name MC467) | XT2625-3 | 2026-04-01 | SGP.22 | soldered | 13650 |
| vivo Mobile Communication Co., Ltd. | V2562 | X300 Ultra | 2026-04-01 | SGP.22 | soldered | 13644 |
| vivo Mobile Communication Co., Ltd. | V2540 | V70 | 2026-04-01 | SGP.22 | soldered | 13649 |
| vivo Mobile Communication Co., Ltd. | V2538 | V70 | 2026-04-01 | SGP.22 | soldered | 13648 |
| HMD Global Oy | TA-1722 | HMD Terra M | 2026-03-31 | SGP.22 | soldered | 13640 |
| HMD Global Oy | TA-1719 | HMD Terra M | 2026-03-31 | SGP.22 | soldered | 13639 |
| Motorola Mobility LLC | XT2625-1 | XT2625-1 | 2026-03-25 | SGP.22 | soldered | 13636 |
| Motorola Mobility LLC | XT2625-4, XT2625-4 [DS] (Type Name MC466) | XT2625-4 | 2026-03-25 | SGP.22 | soldered | 13638 |
| i.safe MOBILE GmbH | M945A01 | IS945.x | 2026-03-23 | SGP.22 | soldered | 13628 |
| Motorola Mobility LLC | XT2651-1 (Type Name MC458) | XT2651-1 | 2026-03-20 | SGP.22 | soldered | 13626 |
| Motorola Mobility LLC | XT2607-1 (Type Name MC465) | XT2607-1 | 2026-03-20 | SGP.22 | soldered | 13625 |
| LG Electronics Inc | TFVWAIBE1FA | TFVWAIBE1FA | 2026-03-19 | SGP.02 | soldered | 13592 |
| LG Electronics Inc | TFVWAIBG1FE | TFVWAIBG1FE | 2026-03-18 | SGP.02 | soldered | 13572 |
| Motorola Mobility LLC | XT2621-5 | XT2621-5 | 2026-03-16 | SGP.22 | soldered | 13621 |
| Motorola Mobility LLC | XT2621-6 (Type Name MC462) | XT2621-6 | 2026-03-16 | SGP.22 | soldered | 13620 |
| Sony Corporation | PM-1520-BV | XQ-GE54 | 2026-03-16 | SGP.22 | soldered | 13617 |
| Ubiquiti Inc. | U5G | UniFi 5G Backup | 2026-03-13 | SGP.22 | soldered | 13576 |
| Honor Device Co Ltd | PNM-N49 | HONOR Magic V6 | 2026-03-12 | SGP.22 | soldered | 13606 |
| Xiaomi Communications | 2602EPTC0G | Xiaomi 17T Pro | 2026-03-12 | SGP.22 | soldered | 13611 |
| Motorola Mobility LLC | XT2657-3 | XT2657-3 | 2026-03-12 | SGP.22 | soldered | 13585 |
| Motorola Mobility LLC | XT2657V | XT2657V | 2026-03-12 | SGP.22 | soldered | 13613 |
| Motorola Mobility LLC | XT2655-1 (Type Name MC45E) | XT2655-1 | 2026-03-11 | SGP.22 | soldered | 13610 |
| Motorola Mobility LLC | XT2655-2 | XT2655-2 | 2026-03-11 | SGP.22 | soldered | 13588 |
| Xiaomi Communications | 2602DPT53G | Xiaomi 17T | 2026-03-11 | SGP.22 | soldered | 13605 |
| Nothing Technology Ltd | A069P | NOTHING Phone (4a) Pro | 2026-03-06 | SGP.22 | soldered | 13569 |
| vivo Mobile Communication Co., Ltd. | V2537 | X300 FE | 2026-03-03 | SGP.22 | soldered | 13598 |
| vivo Mobile Communication Co., Ltd. | V2542 | X300 FE | 2026-03-03 | SGP.22 | soldered | 13599 |
| LG Electronics Inc | TFVWAIBG1FF | TFVWAIBG1FF | 2026-02-28 | SGP.02 | soldered | 13539 |
| Honor Device Co Ltd | VKJ-NX9 | HONOR 600 | 2026-02-27 | SGP.22 | soldered | 13591 |
| Honor Device Co Ltd | VKP-NX9 | HONOR 600 Pro | 2026-02-27 | SGP.22 | soldered | 13590 |
| Motorola Mobility LLC | XT2657-1 (Type name MC641) | XT2657-1 | 2026-02-23 | SGP.22 | soldered | 13587 |
| Honeywell International Inc | CT70-X1 | CT70-X1, CT70 | 2026-02-12 | SGP.22 | soldered | 13553 |
| Zebra Technologies Corporation | TCX01G | TC501, TC701 | 2026-02-01 | SGP.22 | both | 13557 |
| TCL Communication Ltd | T523V | T523V | 2026-01-30 | SGP.22 | soldered | 13554 |
| TCL Communication Ltd | T523SP | T523SP | 2026-01-30 | SGP.22 | soldered | 13555 |
| Motorola Mobility LLC | XT2619V | XT2619V | 2026-01-28 | SGP.22 | soldered | 13550 |
| Motorola Mobility LLC | XT2619-1 | XT2619-1 | 2026-01-28 | SGP.22 | soldered | 13549 |
| Compal Electronics, Inc. | RMM-G4 | RMM-G4 | 2026-01-20 | SGP.22 | soldered | 13314 |
| Power Idea Technology (Shenzhen) Co., Ltd. | PTHA02G | RG940 | 2026-01-19 | SGP.22 | soldered | 13536 |
| Samsung Electronics Co Ltd | SM-A576B/DS, SM-A576B | SM-A576B/DS, SM-A576B | 2026-01-15 | SGP.22 | soldered | 13529 |
| Motorola Mobility LLC | XT2605-2 (Type Name MC464) | XT2605-2 | 2026-01-13 | SGP.22 | soldered | 13527 |
| Motorola Mobility LLC | XT2605-3 | XT2605-3 | 2026-01-13 | SGP.22 | soldered | 13524 |
| Motorola Mobility LLC | XT2605-1 (Type Name MC463) | XT2605-1 | 2026-01-13 | SGP.22 | soldered | 13525 |
| Motorola Mobility LLC | XT2605-5 | XT2605-5 | 2026-01-13 | SGP.22 | soldered | 13526 |
| Samsung Electronics Co Ltd | SM-A376B/DS, SM-A376B | SM-A376B/DS, SM-A376B | 2026-01-12 | SGP.22 | soldered | 13519 |
| vivo Mobile Communication Co., Ltd. | V2533 | Y31e 5G | 2026-01-08 | SGP.22 | soldered | 13517 |
| TCL Communication Ltd | T807M | T807M | 2026-01-06 | SGP.22 | soldered | 13509 |
| vivo Mobile Communication Co., Ltd. | V2552 | V70 FE | 2026-01-04 | SGP.22 | soldered | 13502 |
| vivo Mobile Communication Co., Ltd. | V2550 | V70 FE | 2026-01-04 | SGP.22 | soldered | 13503 |
| Samsung Electronics Co Ltd | SM-S947B/DS, SM-S947B | SM-S947B/DS, SM-S947B | 2025-12-29 | SGP.22 | soldered | 13493 |
| Samsung Electronics Co Ltd | SM-S942B/DS, SM-S942B | SM-S942B/DS, SM-S942B | 2025-12-29 | SGP.22 | soldered | 13494 |
| Motorola Mobility LLC | XT2621-1 | XT2621-1 | 2025-12-19 | SGP.22 | soldered | 13488 |
| Motorola Mobility LLC | XT2621-3 | XT2621-3 | 2025-12-19 | SGP.22 | soldered | 13487 |
| Motorola Mobility LLC | XT2621-4 (Type Name MC457) | XT2621-4 | 2025-12-19 | SGP.22 | soldered | 13465 |
| Motorola Mobility LLC | XT2621-2 (Type Name MC456) | XT2621-2 | 2025-12-19 | SGP.22 | soldered | 13486 |
| Motorola Mobility LLC | XT2603-2 (Type Name MC452) | XT2603-2 | 2025-12-17 | SGP.22 | soldered | 13464 |
| Zebra Technologies Corporation | ET401EB | ET401 | 2025-12-10 | SGP.22 | both | 13453 |
| Zebra Technologies Corporation | ET401EA | ET401 | 2025-12-10 | SGP.22 | both | 13452 |
| Samsung Electronics Co Ltd | SM-S948BDS, SM-S948B | SM-S948BDS, SM-S948B | 2025-12-01 | SGP.22 | soldered | 13435 |
| Ubiquiti Inc. | UDR-5G-Max | Dream Router 5G Max | 2025-11-30 | SGP.22 | soldered | 13408 |
| Xiaomi Communications | 25128PNA1G | Leica Leitzphone powered by Xiaomi | 2025-11-29 | SGP.22 | soldered | 13432 |
| HAND HELD PRODUCTS, INC. | CT70-X1 | CT70-X1, CT70 | 2025-11-28 | SGP.22 | soldered | 13417 |
| Askey Computer Corporation | RC40 | RC40 | 2025-11-28 | SGP.22 | soldered | 13413 |
| Xiaomi Communications | 2512BPNDAG | Xiaomi 17 Ultra | 2025-11-25 | SGP.22 | soldered | 13425 |
| Motorola Mobility LLC | XT2537-2 (Type name MC453) | XT2537-2 | 2025-11-14 | SGP.22 | soldered | 13396 |
| Motorola Mobility LLC | XT2537-5 (Type name MC454) | XT2537-5 | 2025-11-14 | SGP.22 | soldered | 13395 |
| TCL Communication Ltd | T513G | T513G | 2025-11-13 | SGP.22 | soldered | 13402 |
| TCL Communication Ltd | T807D | T807D | 2025-11-12 | SGP.22 | soldered | 13400 |
| Huawei Technologies Co., Ltd. | E5786-336 | Speedport-Ersatz-WLAN(SEW)Box | 2025-11-06 | SGP.22 | soldered | 13380 |
| Motorola Mobility LLC | XT2617V | XT2617V | 2025-10-31 | SGP.22 | soldered | 13377 |
| Brain Technologies, Inc | BGX5 | Natural AI Phone | 2025-10-31 | SGP.22 | soldered | 13372 |
| Motorola Mobility LLC | XT2617-1 | XT2617-1 | 2025-10-31 | SGP.22 | soldered | 13376 |
| vivo Mobile Communication Co., Ltd. | V2521 | Y31 5G | 2025-10-30 | SGP.22 | soldered | 13375 |
| Google LLC | G4H7L | G4H7L | 2025-10-27 | SGP.22 | both | 13353 |
| Google LLC | GE1GQ | GE1GQ | 2025-10-27 | SGP.22 | both | 13352 |
| SIMCom Wireless Solutions Limited | E7088 | E7088 | 2025-10-25 | SGP.02 | removable | 13407 |
| SIMCom Wireless Solutions Limited | E7080 | E7080 | 2025-10-20 | SGP.02 | removable | 13341 |
| Motorola Mobility LLC | XT2601-2 (Type name MC44F) | XT2601-2 | 2025-10-13 | SGP.22 | soldered | 13319 |
| Xiaomi Communications | 25113PN0EG | Xiaomi 17 | 2025-10-13 | SGP.22 | soldered | 13325 |
| Motorola Mobility LLC | XT2601-3 | XT2601-3 | 2025-10-13 | SGP.22 | soldered | 13323 |
| LG Electronics Inc | TLJLNIBN5E6 | TLJLNIBN5E6 | 2025-10-08 | SGP.02 | soldered | 13312 |
| LG Electronics Inc | TM13LNEUJL0 | TM13LNEUJL0 | 2025-10-06 | SGP.02 | soldered | 13282 |
| Samsung Electronics Co Ltd | NP755XRA, NP759XRA | NP755XRA, NP759XRA | 2025-10-01 | SGP.22 | soldered | 13296 |
| Honor Device Co Ltd | BKQ-N49 | HONOR Magic8 Pro | 2025-09-27 | SGP.22 | soldered | 13266 |
| vivo Mobile Communication Co., Ltd. | V2514 | X300 Pro | 2025-09-20 | SGP.22 | soldered | 13262 |
| vivo Mobile Communication Co., Ltd. | V2515 | X300 | 2025-09-19 | SGP.22 | soldered | 13258 |
| Honor Device Co Ltd | MTN-NX1M | HONOR Magic8 Lite | 2025-09-17 | SGP.22 | soldered | 13250 |
| Ubiquiti Inc. | U5G-Max-Outdoor | UniFi 5G Max Outdoor | 2025-09-15 | SGP.22 | soldered | 13156 |
| Motorola Mobility LLC | XT2509-1, XT2509-1 [DS] (Type Name MC441) | XT2509-1 | 2025-09-15 | SGP.22 | soldered | 13242 |
| Huawei Technologies Co., Ltd. | LMR-LX9 | HUAWEI Pura 80 Pro | 2025-09-11 | SGP.22 | soldered | 13216 |
| Xiaomi Communications | 2509BRP2DG | Redmi Pad 2 Pro 5G | 2025-09-10 | SGP.22 | soldered | 13235 |
| Xiaomi Communications | 2510ERA8BG | REDMI Note 15 Pro+ 5G | 2025-09-10 | SGP.22 | soldered | 13232 |
| Motorola Mobility LLC | XT2613V | XT2613V | 2025-09-09 | SGP.22 | soldered | 13234 |
| Motorola Mobility LLC | XT2613-1 | XT2613-1 | 2025-09-09 | SGP.22 | soldered | 13233 |
| Xiaomi Communications | 25080RABDG | REDMI Note 15 Pro 5G | 2025-09-07 | SGP.22 | soldered | 13223 |
| Motorola Mobility LLC | XT2615V | XT2615V | 2025-09-05 | SGP.22 | soldered | 13218 |
| Motorola Mobility LLC | XT2615-1 | XT2615-1 | 2025-09-05 | SGP.22 | soldered | 13217 |
| Crosscall SAS | Core-M6 | Core-M6 | 2025-09-04 | SGP.22 | soldered | 13111 |
| Huawei Technologies Co., Ltd. | MCH-AL00 | HUAWEI WATCH Ultimate 2 | 2025-09-01 | SGP.22 | soldered | 13206 |
| Xiaomi Communications | A501XM | Redmi 15 5G | 2025-08-15 | SGP.22 | soldered | 13178 |
| Ubiquiti Inc. | U5G-Max | UniFi 5G Max | 2025-08-15 | SGP.22 | soldered | 13082 |
| Samsung Electronics Co Ltd | SM-S731B/DS, SM-S731B | SM-S731B/DS, SM-S731B | 2025-07-28 | SGP.22 | soldered | 13139 |
| Rolling Wireless S.a.r.l. | RN934R | RN934R | 2025-07-25 | SGP.02 | both | 13123 |
| Rolling Wireless S.a.r.l. | RN937N | RN937N | 2025-07-25 | SGP.02 | both | 13124 |
| Rolling Wireless S.a.r.l. | RN934V | RN934V | 2025-07-25 | SGP.02 | both | 13125 |
| Rolling Wireless S.a.r.l. | RN932V | RN932V | 2025-07-25 | SGP.02 | both | 13126 |
| Samsung Electronics Co Ltd | SM-X936B | SM-X936B | 2025-07-24 | SGP.22 | soldered | 13133 |
| Samsung Electronics Co Ltd | SM-X736B | SM-X736B | 2025-07-24 | SGP.22 | soldered | 13134 |
| Rolling Wireless S.a.r.l. | RN934N | RN934N | 2025-07-23 | SGP.02 | both | 13122 |
| Solana Mobile Inc. | Seeker | Seeker | 2025-07-23 | SGP.22 | soldered | 13130 |
| Microsoft Corporation | 2119 | Surface Laptop | 2025-07-17 | SGP.22 | soldered | 13112 |
| Google LLC | GU0NP | GU0NP | 2025-07-11 | SGP.22 | both | 13092 |
| Xiaomi Communications | 25069PTEBG | Xiaomi 15T | 2025-07-04 | SGP.22 | soldered | 13060 |
| Xiaomi Communications | 2506BPN68G | Xiaomi 15T Pro | 2025-07-04 | SGP.22 | soldered | 13056 |
| TCL Communication Ltd | T951K | T951K | 2025-07-03 | SGP.22 | soldered | 13076 |
| Nothing Technology Ltd | A024 | Nothong Phone (3) | 2025-07-02 | SGP.22 | soldered | 13054 |
| TCL Communication Ltd | 8189S | 8189S | 2025-07-02 | SGP.22 | soldered | 13075 |
| Luxshare Precision Limited | T Phone 3 | T Phone 3 | 2025-06-30 | SGP.22 | soldered | 13039 |
| Realme Chongqing Mobile Telecommunications Corporation Ltd. | RMX5061 | realme GT 7 | 2025-06-30 | SGP.22 | soldered | 13059 |
| Luxshare Precision Limited | T Phone 3 Pro | T Phone 3 Pro | 2025-06-30 | SGP.22 | soldered | 13041 |
| Sony Corporation | PM-1514-BV | XQ-FE54 | 2025-06-25 | SGP.22 | soldered | 13057 |
| Google LLC | G1KAW | G1KAW | 2025-06-23 | SGP.22 | soldered | 13045 |
| Zebra Technologies Corporation | FR55E0 | FR55 | 2025-06-16 | SGP.22 | both | 12958 |
| Pepperl+Fuchs SE | Smart-Ex 203 | Smart-Ex 203 | 2025-06-10 | SGP.22 | soldered | 13021 |
| Samsung Electronics Co Ltd | SM-F766B | SM-F766B | 2025-06-04 | SGP.22 | soldered | 13001 |
| Google LLC | GEHN3 | GEHN3 | 2025-06-02 | SGP.22 | both | 12978 |
| Google LLC | GUL82 | GUL82 | 2025-06-02 | SGP.22 | both | 12971 |
| Google LLC | G45RY | G45RY | 2025-06-02 | SGP.22 | both | 12973 |
| Google LLC | GLBW0 | GLBW0 | 2025-06-02 | SGP.22 | both | 12983 |
| Google LLC | G4QUR | G4QUR | 2025-06-02 | SGP.22 | both | 12977 |
| Google LLC | GK2MP | GK2MP | 2025-06-02 | SGP.22 | both | 12985 |
| Honor Device Co Ltd | MBH-N49 | HONOR Magic V5 | 2025-05-30 | SGP.22 | soldered | 12963 |
| Samsung Electronics Co Ltd | SM-F761B | SM-F761B | 2025-05-30 | SGP.22 | soldered | 12992 |
| Samsung Electronics Co Ltd | SM-F966B/DS, SM-F966B | SM-F966B/DS, SM-F966B | 2025-05-29 | SGP.22 | soldered | 12989 |
| Samsung Electronics Co Ltd | SM-L505F | SM-L505F | 2025-05-28 | SGP.22 | soldered | 12986 |
| Samsung Electronics Co Ltd | SM-L335F | SM-L335F | 2025-05-28 | SGP.22 | soldered | 12982 |
| Lenovo Mobile Communication Technology Co Ltd | TB336ZU | Lenovo Idea Tab 、 Lenovo Tab K11 Gen 2 | 2025-05-26 | SGP.22 | removable | 12953 |
| Fairphone B.V. | FP6 | Fairphone (Gen.6) | 2025-05-26 | SGP.22 | soldered | 12968 |
| Samsung Electronics Co Ltd | SM-L325F | SM-L325F | 2025-05-22 | SGP.22 | soldered | 12961 |
| vivo Mobile Communication Co., Ltd. | V2503 | X200 FE | 2025-05-21 | SGP.22 | soldered | 12959 |
| Motorola Mobility LLC | XT2527-1 | XT2527-1 | 2025-05-09 | SGP.22 | soldered | 12920 |
| Motorola Mobility LLC | XT2527-6 | XT2527-6 | 2025-05-09 | SGP.22 | soldered | 12931 |
| Motorola Mobility LLC | XT2527-2 (Type Name MC445) | XT2527-2 | 2025-05-09 | SGP.22 | soldered | 12930 |
| Motorola Mobility LLC | XT2527-7 (Type Name MC445) | XT2527-7 | 2025-05-09 | SGP.22 | soldered | 12932 |
| Orbic Electronics Manufacturing LLC | R667L5P | Orbic Trophy Plus | 2025-04-30 | SGP.22 | soldered | 12916 |
| Sierra Wireless, ULC | EM7590 | Sierra Wireless EM7590 | 2025-04-18 | SGP.22 | both | 12901 |
| Sierra Wireless, ULC | EM7595 | Sierra Wireless EM7595 | 2025-04-18 | SGP.22 | both | 12902 |
| Huawei Technologies Co., Ltd. | SOC-AL00 | HUAWEI WATCH 5 | 2025-04-17 | SGP.22 | soldered | 12900 |
| Huawei Technologies Co., Ltd. | RTS-AL00 | HUAWEI WATCH 5 | 2025-04-17 | SGP.22 | soldered | 12896 |
| Xplora Technologies AS | X6SE | X6Play eSIM | 2025-04-16 | SGP.22 | soldered | 12895 |
| Motorola Mobility LLC | XT2529-2 (Type Name MC444) | XT2529-2 | 2025-04-15 | SGP.22 | soldered | 12894 |
| Motorola Mobility LLC | XT2529-1 | XT2529-1 | 2025-04-15 | SGP.22 | soldered | 12868 |
| Motorola Mobility LLC | XT2519V | XT2519V | 2025-04-10 | SGP.22 | soldered | 12867 |
| Motorola Mobility LLC | XT2519-1 | XT2519-1 | 2025-04-10 | SGP.22 | soldered | 12824 |
| Harman International Industries Inc | TCAM3 (Type Name L265) | TCAM3 | 2025-04-09 | SGP.02 | soldered | 12852 |
| Harman International Industries Inc | TCAM3 (Type Name L271) | TCAM3 | 2025-04-09 | SGP.02 | soldered | 12851 |
| HMD Global Oy | TA-1672 | TA-1672 | 2025-04-07 | SGP.22 | soldered | 12858 |
| Samsung Electronics Co Ltd | SM-G766B | SM-G766B | 2025-04-07 | SGP.22 | soldered | 12863 |
| Samsung Electronics Co Ltd | SM-X356B | SM-X356B | 2025-04-07 | SGP.22 | soldered | 12862 |
| HMD Global Oy | TA-1677 | TA-1677 | 2025-04-07 | SGP.22 | soldered | 12859 |
| TCL Communication Ltd | T513SP | T513SP | 2025-04-03 | SGP.22 | soldered | 12873 |
| TCL Communication Ltd | T513V | T513V | 2025-04-03 | SGP.22 | soldered | 12874 |
| TCL Communication Ltd | T Tablet 2 | T Tablet 2 | 2025-04-01 | SGP.22 | removable | 12849 |
| Motorola Mobility LLC | XT2553-3, XT2553-3 [eDS] | XT2553-3 | 2025-03-31 | SGP.22 | soldered | 12823 |
| Motorola Mobility LLC | XT2553V | XT2553V | 2025-03-31 | SGP.22 | soldered | 12828 |
| Sony Corporation | PM-1500-BV | XQ-FS54 | 2025-03-28 | SGP.22 | soldered | 12846 |
| Honor Device Co Ltd | DNP-NX9 | HONOR 400 Pro | 2025-03-27 | SGP.22 | soldered | 12844 |
| Honor Device Co Ltd | DNY-NX9 | HONOR 400 | 2025-03-27 | SGP.22 | soldered | 12843 |
| Airgain Inc | AirgainConnect Fleet | AirgainConnect Fleet | 2025-03-27 | SGP.22 | soldered | 12845 |
| Datalogic S.r.l. | AELNRNA | MEMOR 17 | 2025-03-23 | SGP.22 | soldered | 12749 |
| Motorola Mobility LLC | XT2507-1 (Type name MC441) | XT2507-1 | 2025-03-21 | SGP.22 | soldered | 12827 |
| Motorola Mobility LLC | XT2553-1, XT2553-1 [eDS] (Type Name MC42B) | XT2553-1 | 2025-03-10 | SGP.22 | soldered | 12801 |
| Samsung Electronics Co Ltd | SM-X526E | SM-X526E | 2025-02-28 | SGP.22 | soldered | 12821 |
| TCL Communication Ltd | T521K | T521K | 2025-02-28 | SGP.22 | soldered | 12785 |
| TCL Communication Ltd | T521H | T521H | 2025-02-28 | SGP.22 | soldered | 12784 |
| Samsung Electronics Co Ltd | SM-X626B | SM-X626B | 2025-02-28 | SGP.22 | soldered | 12780 |
| Samsung Electronics Co Ltd | SM-X526B | SM-X526B | 2025-02-28 | SGP.22 | soldered | 12781 |
| Honor Device Co Ltd | ABR-NX1 | HONOR 400 Lite | 2025-02-28 | SGP.22 | soldered | 12778 |
| Motorola Mobility LLC | XT2503-1, XT2503-1 [eDS] | XT2503-1 | 2025-02-24 | SGP.22 | soldered | 12759 |
| Motorola Mobility LLC | XT2505-1, XT2505-1 [eDS] (Type Name MC443) | XT2505-1 | 2025-02-24 | SGP.22 | soldered | 12765 |
| Motorola Mobility LLC | XT2503-4, XT2503-4 [eDS] (Type Name MC444) | XT2503-4 | 2025-02-24 | SGP.22 | soldered | 12763 |
| Motorola Mobility LLC | XT2505-3, XT2505-3 [eDS] | XT2505-3 | 2025-02-24 | SGP.22 | soldered | 12764 |
| Motorola Mobility LLC | XT2517V | XT2517V | 2025-02-19 | SGP.22 | soldered | 12752 |
| Motorola Mobility LLC | XT2517-1, XT2517-1 [eDS] | XT2517-1 | 2025-02-19 | SGP.22 | soldered | 12751 |
| TCL Communication Ltd | T705M | T705M | 2025-02-14 | SGP.22 | soldered | 12738 |
| Motorola Mobility LLC | XT2551-1, XT2551-1 [eDS] | XT2551-1 | 2025-02-14 | SGP.22 | soldered | 12740 |
| Motorola Mobility LLC | XT2551-6, XT2551-6 [eDS] (Type Name MC442) | XT2551-6 | 2025-02-14 | SGP.22 | soldered | 12741 |
| LG Innotek Co., Ltd. | LTD-OA1000 | LTD-OA1000 | 2025-02-14 | SGP.02 | removable | 12732 |
| Realme Chongqing Mobile Telecommunications Corporation Ltd. | RMX5070 | realme 14 5G | 2025-02-13 | SGP.22 | soldered | 12735 |
| vivo Mobile Communication Co., Ltd. | V2440 | V50 Lite 5G | 2025-02-11 | SGP.22 | soldered | 12736 |
| LG Innotek Co., Ltd. | LTD-VL4000 | LTD-VL4000 | 2025-02-07 | SGP.02 | removable | 12728 |
| Realme Chongqing Mobile Telecommunications Corporation Ltd. | RMX5051 | realme 14 Pro+ 5G | 2025-02-03 | SGP.22 | soldered | 12716 |
| Zebra Technologies Corporation | EM45B1 | EM45 | 2025-02-02 | SGP.22 | both | 12723 |
| Zebra Technologies Corporation | EM45A1 | EM45 | 2025-02-02 | SGP.22 | both | 12722 |
| Zebra Technologies Corporation | MC345B | MC34, MC3450 | 2025-02-02 | SGP.22 | both | 12726 |
| Zebra Technologies Corporation | MC345A | MC34, MC3450 | 2025-02-02 | SGP.22 | both | 12725 |
| Zebra Technologies Corporation | MC345C | MC34, MC3450 | 2025-02-02 | SGP.22 | removable | 12727 |
| Nothing Technology Ltd | A059P | Nothing Phone (3a) Pro | 2025-01-31 | SGP.22 | soldered | 12697 |
| Realme Chongqing Mobile Telecommunications Corporation Ltd. | RMX5056 | realme 14 Pro 5G | 2025-01-26 | SGP.22 | soldered | 12713 |
| Realme Chongqing Mobile Telecommunications Corporation Ltd. | RMX3943 | realme 14x 5G | 2025-01-25 | SGP.22 + SGP.02 | both | 12692 |
| LG Innotek Co., Ltd. | LTD-FA1000 | LTD-FA1000 | 2025-01-22 | SGP.02 | removable | 12683 |
| Askey Computer Corporation | WiFi 7 Backup Router, CBE1V1K | WiFi 7 Backup Router, CBE1V1K | 2025-01-21 | SGP.02 | soldered | 12686 |
| Askey Computer Corporation | NMQ2210 | NMQ2210 | 2025-01-16 | SGP.02 | soldered | 12685 |
| Motorola Mobility LLC | XT2433-4 (Type Name MC432) | XT2433-4 | 2025-01-15 | SGP.22 | soldered | 12682 |
| Honeywell International Inc | CK67X1N | CK67X1N | 2025-01-01 | SGP.22 | soldered | 11956 |
| Xiaomi Communications | 25010PN30G | Xiaomi 15 Ultra | 2024-12-30 | SGP.22 | soldered | 12650 |
| TCL Communication Ltd | T704V | T704V | 2024-12-25 | SGP.22 + SGP.02 | soldered | 12661 |
| TCL Communication Ltd | T704SP | T704SP | 2024-12-25 | SGP.22 + SGP.02 | soldered | 12662 |
| Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2689 | CPH2689 | 2024-12-13 | SGP.22 | not declared | 12648 |
| Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2697 | CPH2697 | 2024-12-13 | SGP.22 | not declared | 12649 |
| Honeywell International Inc | CT37X1N | CT37X1N, CT37 | 2024-12-13 | SGP.22 | soldered | 12279 |
| Power Idea Technology (Shenzhen) Co., Ltd. | PSM05G | RG880i | 2024-12-09 | SGP.22 | soldered | 12637 |
| Power Idea Technology (Shenzhen) Co., Ltd. | PSH03G | RG440 | 2024-12-06 | SGP.22 | soldered | 12634 |
| Google LLC | GXQ96 | GXQ96 | 2024-12-02 | SGP.22 | not declared | 12623 |
| Google LLC | GTF7P | GTF7P | 2024-12-02 | SGP.22 | not declared | 12624 |
| Samsung Electronics Co Ltd | SM-S931B/DS, SM-S931B | SM-S931B/DS, SM-S931B | 2024-11-28 | SGP.22 | soldered | 12631 |
| Samsung Electronics Co Ltd | SM-S936B/DS, SM-S936B | SM-S936B/DS, SM-S936B | 2024-11-28 | SGP.22 | soldered | 12630 |
| Samsung Electronics Co Ltd | SM-S938B/DS, SM-S938B | SM-S938B/DS, SM-S938B | 2024-11-28 | SGP.22 | soldered | 12629 |
| Motorola Mobility LLC | XT2515V | XT2515V | 2024-11-25 | SGP.22 | soldered | 12620 |
| Motorola Mobility LLC | XT2515-1 | XT2515-1 | 2024-11-25 | SGP.22 | soldered | 12619 |
| FCNT LLC | F-53E | F-53E | 2024-11-22 | SGP.22 | soldered | 12621 |
| Motorola Mobility LLC | XT2513-1 | XT2513-1 | 2024-11-15 | SGP.22 | soldered | 12610 |
| Motorola Mobility LLC | XT2513V | XT2513V | 2024-11-15 | SGP.22 | soldered | 12611 |
| LG Innotek Co., Ltd. | LTD-GN3000 | LTD-GN3000 | 2024-11-11 | SGP.02 | removable | 12597 |
| Honor Device Co Ltd | BRP-NX1M | HONOR Magic7 Lite | 2024-11-11 | SGP.22 | soldered | 12593 |
| i.safe MOBILE GmbH | M940A01 | IS940.1, IS940.M1, IS940.2, IS940.RG | 2024-11-08 | SGP.22 | soldered | 12576 |
| i.safe MOBILE GmbH | M440A01 | IS440.1, IS440.M1, IS440.2, IS440.RG | 2024-11-08 | SGP.22 | soldered | 12584 |
| LG Innotek Co., Ltd. | LTD-GN2000 | LTD-GN2000 | 2024-11-08 | SGP.02 | removable | 12581 |
| Honor Device Co Ltd | PTP-N49 | HONOR Magic7 Pro | 2024-10-29 | SGP.22 | soldered | 12560 |
| Xiaomi Communications | 24129PN74G | Xiaomi 15 | 2024-10-25 | SGP.22 | soldered | 12556 |
| Zebra Technologies Corporation | EM45A2 | EM45 | 2024-10-16 | SGP.22 | both | 12541 |
| Zebra Technologies Corporation | EM45B2 | EM45 | 2024-10-16 | SGP.22 | both | 12543 |
| Zebra Technologies Corporation | ET65WW | ET65 | 2024-10-08 | SGP.22 | both | 12529 |
| Xiaomi Communications | 24115RA8EG | Redmi Note 14 Pro+ 5G | 2024-09-30 | SGP.22 | soldered | 12525 |
| Crosscall SAS | Stellar-M6 | Stellar-M6 | 2024-09-15 | SGP.22 | soldered | 12496 |
| Crosscall SAS | Stellar-M6E | Stellar-M6E | 2024-09-15 | SGP.22 | soldered | 12502 |
| Motorola Mobility LLC | XT2437-2, XT2437-2 [eDS] | XT2437-2 | 2024-09-13 | SGP.22 | soldered | 12503 |
| Motorola Mobility LLC | XT2437-1 | XT2437-1 | 2024-09-13 | SGP.22 | soldered | 12505 |
| Motorola Mobility LLC | XT2437-3, XT2437-3 [eDS] (Type Name MC434) | XT2437-3 | 2024-09-13 | SGP.22 | soldered | 12504 |
| Xiaomi Communications | 24090RA29G | Redmi Note 14 Pro 5G | 2024-09-08 | SGP.22 | soldered | 12488 |
| HMD Global Oy | TA-1640 | HMD Fusion; HMD Fuse | 2024-09-06 | SGP.22 | soldered | 12486 |
| HMD Global Oy | TA-1670 | HMD Fusion Business Edition | 2024-09-06 | SGP.22 | soldered | 12485 |
| HMD Global Oy | TA-1643 | HMD Fusion | 2024-09-06 | SGP.22 | soldered | 12484 |
| Motorola Mobility LLC | XT2433-2, XT2433-2 [eDS] | XT2433-2 | 2024-08-26 | SGP.22 | soldered | 12462 |
| Motorola Mobility LLC | XT2433-5 (Type Name MC432) | XT2433-5 | 2024-08-26 | SGP.22 | soldered | 12463 |
| Motorola Mobility LLC | XT2433-1 | XT2433-1 | 2024-08-26 | SGP.22 | soldered | 12464 |
| Samsung Electronics Co Ltd | SM-X826B | SM-X826B | 2024-08-21 | SGP.22 | soldered | 12458 |
| Samsung Electronics Co Ltd | SM-X926B | SM-X926B | 2024-08-21 | SGP.22 | soldered | 12459 |
| Samsung Electronics Co Ltd | SM-S721B/DS | SM-S721B/DS | 2024-08-21 | SGP.22 | soldered | 12460 |
| Sonim Technologies Inc | X800(S6002) | XP Pro | 2024-08-12 | SGP.22 | soldered | 12435 |
| Zebra Technologies Corporation | TC58CE | TC58e | 2024-08-12 | SGP.22 | both | 12446 |
| BARTEC GmbH | SC9EX1, SP9EX1, SC9EX2, SP9EX2 | BARTEC SC9EXx Smartscanner, BARTEC SP9EXx Smartphone | 2024-08-12 | SGP.22 | soldered | 12431 |
| Motorola Mobility LLC | XT2409-6 (Type Name MC431) | XT2409-6 | 2024-08-09 | SGP.22 | soldered | 12440 |
| Motorola Mobility LLC | XT2435-2, XT2435-2 [eDS] (Type Name MC436) | XT2435-2 | 2024-08-09 | SGP.22 | soldered | 12442 |
| Motorola Mobility LLC | XT2435-1, XT2435-1 [eDS] | XT2435-1 | 2024-08-09 | SGP.22 | soldered | 12441 |
| FCNT LLC | A402FC | A402FC | 2024-08-05 | SGP.22 | soldered | 12427 |
| FCNT LLC | A401FC | A401FC | 2024-08-05 | SGP.22 | soldered | 12428 |
| Elo Touch Solutions Inc | EMC-M100C | Elo Pay M100 | 2024-07-31 | SGP.22 | soldered | 12222 |
| Elo Touch Solutions Inc | EMC-M100C | Elo Pay M100 | 2024-07-31 | SGP.22 | soldered | 12223 |
| Compal Electronics, Inc. | RMM-G1 | RMM-G1 | 2024-07-29 | SGP.22 | soldered | 12423 |
| Motorola Mobility LLC | XT2409-2, XT2409-2 [eDS] | XT2409-2 | 2024-07-19 | SGP.22 | soldered | 12394 |
| Motorola Mobility LLC | XT2409-1, XT2409-1 [eDS] (Type Name MC431) | XT2409-1 | 2024-07-19 | SGP.22 | soldered | 12372 |
| Trasna Solutions FZ-LLC | LEXI-R520 | LEXI-R520 | 2024-07-18 | SGP.02 | removable | 12278 |
| Datalogic S.r.l. | SGVNRNATYPEA51AC65X | MEMOR 35X | 2024-07-16 | SGP.22 | soldered | 12062 |
| Datalogic S.r.l. | SGVNRNATYPEA51AC65A | MEMOR 35 | 2024-07-16 | SGP.22 | soldered | 12325 |
| ZTE Corporation | Z2357N | ZTE Blade A75 5G | 2024-07-09 | SGP.02 | not declared | 12368 |
| Google LLC | GRY0E | GRY0E | 2024-07-03 | SGP.22 | soldered | 12359 |
| Google LLC | GBDU9 | GBDU9 | 2024-07-03 | SGP.22 | soldered | 12358 |
| Xiaomi Communications | A402XM | Xiaomi 14T Pro | 2024-07-02 | SGP.22 | soldered | 12357 |
| Datalogic S.r.l. | SGVNRTYPEE51AC65X | MEMOR 35X | 2024-06-28 | SGP.22 | soldered | 12324 |
| Datalogic S.r.l. | SGVNR | MEMOR 35 | 2024-06-28 | SGP.22 | soldered | 12316 |
| Motorola Mobility LLC | XT2407-2, XT2407-2 [eDS] | XT2407-2 | 2024-06-28 | SGP.22 | soldered | 12349 |
| Huawei Technologies Co., Ltd. | HBN-LX9 | HUAWEI Pura 70 Pro | 2024-06-28 | SGP.22 | soldered | 12344 |
| Motorola Mobility LLC | XT2407-1, XT2407-1 [eDS] (Type name MC430) | XT2407-1 | 2024-06-28 | SGP.22 | soldered | 12350 |
| TCL Communication Ltd | T702D | T702D | 2024-06-24 | SGP.22 + SGP.02 | both | 12337 |
| Google LLC | GZC4K | GZC4K | 2024-06-24 | SGP.22 | both | 12293 |
| Google LLC | GGX8B | GGX8B | 2024-06-24 | SGP.22 | both | 12290 |
| Google LLC | GEC77 | GEC77 | 2024-06-24 | SGP.22 | both | 12299 |
| Google LLC | GR83Y | GR83Y | 2024-06-24 | SGP.22 | both | 12298 |
| Google LLC | GGH2X | GGH2X | 2024-06-24 | SGP.22 | both | 12301 |
| Xiaomi Communications | 2406APNFAG | Xiaomi 14T | 2024-06-24 | SGP.22 | soldered | 12333 |
| Google LLC | GUR25 | GUR25 | 2024-06-24 | SGP.22 | both | 12297 |
| Google LLC | G2YBB | G2YBB | 2024-06-24 | SGP.22 | both | 12294 |
| Xiaomi Communications | 2407FPN8EG | Xiaomi 14T Pro | 2024-06-21 | SGP.22 | soldered | 12326 |
| Honor Device Co Ltd | FCP-N49 | HONOR Magic V3 | 2024-06-21 | SGP.22 | soldered | 12321 |
| HMD Global Oy | TA-1600 | TA-1600 | 2024-06-07 | SGP.22 | soldered | 12300 |
| HMD Global Oy | TA-1688 | TA-1688 | 2024-06-07 | SGP.22 | soldered | 12302 |
| Elo Touch Solutions Inc | EMC-M51C | M51 Mobile Computer | 2024-06-07 | SGP.22 | soldered | 12249 |
| Motorola Mobility LLC | XT2453-1, XT2453-1 [eDS] (Type Name MC42B) | XT2453-1 | 2024-06-03 | SGP.22 | soldered | 12286 |
| Samsung Electronics Co Ltd | SM-F741B | SM-F741B | 2024-05-30 | SGP.22 | soldered | 12276 |
| Samsung Electronics Co Ltd | SM-F956B/DS, SM-F956B | SM-F956B/DS, SM-F956B | 2024-05-30 | SGP.22 | soldered | 12277 |
| Samsung Electronics Co Ltd | SM-L305F | SM-L305F | 2024-05-29 | SGP.22 | soldered | 12272 |
| Samsung Electronics Co Ltd | SM-L705F | SM-L705F | 2024-05-29 | SGP.22 | soldered | 12274 |
| Samsung Electronics Co Ltd | SM-L315F | SM-L315F | 2024-05-29 | SGP.22 | soldered | 12273 |
| Motorola Mobility LLC | XT2427-1, XT2427-1 [eDS] | XT2427-1 | 2024-05-27 | SGP.22 | soldered | 12263 |
| Motorola Mobility LLC | XT2427-2, XT2427-2 [eDS] , XT2427-2 [DS] (Type Name MC426) | XT2427-2 | 2024-05-27 | SGP.22 | soldered | 12264 |
| Honor Device Co Ltd | ELP-NX9 | HONOR 200 Pro | 2024-05-24 | SGP.22 | soldered | 12259 |
| Honor Device Co Ltd | ELI-NX9 | HONOR 200 | 2024-05-24 | SGP.22 | soldered | 12260 |
| Motorola Mobility LLC | XT2453-3, XT2453-3 [eDS] | XT2453-3 | 2024-05-23 | SGP.22 | soldered | 12254 |
| Motorola Mobility LLC | XT2453V | XT2453V | 2024-05-23 | SGP.22 | soldered | 12261 |
| vivo Mobile Communication Co., Ltd. | V2348 | V40 | 2024-05-22 | SGP.22 | soldered | 12256 |
| Motorola Mobility LLC | XT2451-3, XT2451-3 [eDS] (Type Name MC42E) | XT2451-3 | 2024-05-17 | SGP.22 | soldered | 12240 |
| FCNT LLC | F-51E | F-51E | 2024-05-17 | SGP.22 | soldered | 12258 |
| FCNT LLC | F-52E | F-52E | 2024-05-17 | SGP.22 | soldered | 12253 |
| FCNT LLC | FCG02 | FCG02 | 2024-05-17 | SGP.22 | soldered | 12257 |
| Zebra Technologies Corporation | TC58AE | TC58e | 2024-05-14 | SGP.22 | both | 12241 |
| Motorola Mobility LLC | XT2451-1, XT2451-1 [eDS] | XT2451-1 | 2024-05-14 | SGP.22 | soldered | 12226 |
| Zebra Technologies Corporation | TC58BE | TC58e | 2024-05-14 | SGP.22 | both | 12244 |
| ZTE Corporation | NX724J | nubia Flip 5G | 2024-05-07 | SGP.02 | not declared | 12224 |
| Microsoft Corporation | 2078 | Surface Model 2078 | 2024-05-02 | SGP.22 | soldered | 12212 |
| Microsoft Corporation | 2077 | Surface Model 2077 | 2024-04-29 | SGP.22 | soldered | 12204 |
| Pepperl+Fuchs SE | Smart-Ex 03 | Smart-Ex 03 | 2024-04-26 | SGP.22 | soldered | 12118 |
| Orbic Electronics Manufacturing LLC | R678L5S | Orbic Style 5G | 2024-04-22 | SGP.22 | soldered | 12187 |
| Orbic Electronics Manufacturing LLC | R678L5SFP | Orbic Fun Pro 5G | 2024-04-22 | SGP.22 | soldered | 12189 |
| Orbic Electronics Manufacturing LLC | R667L5 | Orbic Trophy 5G | 2024-04-19 | SGP.22 | soldered | 12169 |
| Compal Electronics, Inc. | EXM-G1A | EXM-G1A | 2024-04-18 | SGP.22 | soldered | 12171 |
| Sony Corporation | PM-1490-BV | XQ-EC54 | 2024-04-16 | SGP.22 | soldered | 12162 |
| vivo Mobile Communication Co., Ltd. | V2341 | V40 Lite | 2024-04-12 | SGP.22 | soldered | 12141 |
| Motorola Mobility LLC | XT2405V | XT2405V | 2024-04-11 | SGP.22 | soldered | 12138 |
| Motorola Mobility LLC | XT2405-1, XT2405-1 [eDS] | XT2405-1 | 2024-04-11 | SGP.22 | soldered | 12137 |
| Rolling Wireless S.a.r.l. | RN934A | RN934A | 2024-04-10 | SGP.02 | both | 11679 |
| Sony Corporation | PM-1470-BV | PDT-FP1 | 2024-04-08 | SGP.22 | soldered | 12124 |
| Motorola Mobility LLC | XT2401-1, XT2401-1 [eDS] (Type Name MC420) | XT2401-1 | 2024-04-08 | SGP.22 | soldered | 12127 |
| Motorola Mobility LLC | XT2429-1, XT2429-1 [eDS] | XT2429-1 | 2024-04-05 | SGP.22 | soldered | 12125 |
| Motorola Mobility LLC | XT2429-2, XT2429-2 [eDS] (Type Name MC424) | XT2429-2 | 2024-04-05 | SGP.22 | soldered | 12126 |
| Motorola Mobility LLC | XT2419V | XT2419V | 2024-03-26 | SGP.22 | soldered | 12108 |
| Motorola Mobility LLC | XT2419-1, XT2419-1 [eDS] | XT2419-1 | 2024-03-22 | SGP.22 | soldered | 12093 |
| TCL Communication Ltd | T614WS | T614WS | 2024-03-22 | SGP.22 + SGP.02 | removable | 12092 |
| Zebra Technologies Corporation | MC945A | MC9450, MC94 | 2024-03-21 | SGP.22 | both | 12087 |
| Zebra Technologies Corporation | MC945B | MC9450, MC94 | 2024-03-21 | SGP.22 | both | 12088 |
| Orbic Electronics Manufacturing LLC | R667L5U | Orbic Trophy 5G UW | 2024-03-19 | SGP.22 | soldered | 12017 |
| Huawei Technologies Co., Ltd. | MDS-AL00 | HUAWEI WATCH 4 Pro, HUAWEI WATCH 4 Pro Space Edition | 2024-03-19 | SGP.22 | soldered | 12072 |
| Sony Corporation | PM-1484-BV | XQ-ES54 | 2024-03-13 | SGP.22 | soldered | 12065 |
| Trasna Solutions FZ-LLC | SARA-R520M10 | SARA-R520M10 | 2024-03-05 | SGP.02 | removable | 11884 |
| Trasna Solutions FZ-LLC | SARA-R520 | SARA-R520 | 2024-03-05 | SGP.02 | removable | 11885 |
| Trasna Solutions FZ-LLC | SARA-R520M10X | SARA-R520M10X | 2024-03-05 | SGP.02 | removable | 11883 |
| TCL Communication Ltd | T613K | T613K | 2024-02-29 | SGP.22 + SGP.02 | soldered | 12044 |
| Honeywell International Inc | UK7M0000675 | Merlin NBIoT | 2024-02-24 | SGP.02 | soldered | 12032 |
| Motorola Mobility LLC | XT2403-2, XT2403-2 [eDS] (Type Name MC421) | XT2403-2 | 2024-02-22 | SGP.22 | soldered | 12030 |
| Sierra Wireless, ULC | EM7590 | Sierra Wireless EM7590 | 2024-02-15 | SGP.22 | both | 12021 |
| Sierra Wireless, ULC | EM7595 | Sierra Wireless EM7595 | 2024-02-15 | SGP.22 | both | 12022 |
| vivo Mobile Communication Co., Ltd. | V2337 | V40 SE 5G | 2024-01-30 | SGP.22 | soldered | 12013 |
| Samsung Electronics Co Ltd | SM-A356B/DS | SM-A356B/DS | 2024-01-29 | SGP.22 | soldered | 12006 |
| Samsung Electronics Co Ltd | SM-A556E/DS, SM-A556E | SM-A556E/DS, SM-A556E | 2024-01-29 | SGP.22 | soldered | 12008 |
| Google LLC | GKV4X | GKV4X | 2024-01-25 | SGP.22 | not declared | 11977 |
| Google LLC | G8HHN | G8HHN | 2024-01-25 | SGP.22 | not declared | 11981 |
| Google LLC | G6GPR | G6GPR | 2024-01-25 | SGP.22 | not declared | 11980 |
| Samsung Electronics Co Ltd | SM-A556B/DS | SM-A556B/DS | 2024-01-24 | SGP.22 | soldered | 11994 |
| Motorola Mobility LLC | XT2417D | XT2417D | 2024-01-22 | SGP.22 | soldered | 11988 |
| Motorola Mobility LLC | XT2417-1, XT2417-1 [eDS] | XT2417-1 | 2024-01-22 | SGP.22 | soldered | 11987 |
| TCL Communication Ltd | T614SP | T614SP | 2024-01-16 | SGP.22 + SGP.02 | removable | 11982 |
| Motorola Solutions Inc | MSLB-MKZ920ti | MOTOTRBO ION | 2024-01-16 | SGP.22 | soldered | 11910 |
| TCL Communication Ltd | T614D | T614D | 2024-01-16 | SGP.22 + SGP.02 | removable | 11983 |
| Honor Device Co Ltd | BVL-N49 | HONOR Magic6 Pro | 2024-01-09 | SGP.22 | soldered | 11967 |
| Xiaomi Communications | A401XM | Redmi 12 5G | 2024-01-08 | SGP.22 | soldered | 11966 |
| Motorola Mobility LLC | XT2415-1, XT2415-1 [eDS] | XT2415-1 | 2023-12-21 | SGP.22 | soldered | 11941 |
| Motorola Mobility LLC | XT2415V | XT2415V | 2023-12-21 | SGP.22 | soldered | 11942 |
| Motorola Mobility LLC | XT2363-1, XT2363-1 [eDS] | XT2363-1 | 2023-12-14 | SGP.22 | soldered | 11926 |
| Motorola Mobility LLC | XT2363-2, XT2363-2 [eDS] | XT2363-2 | 2023-12-14 | SGP.22 | soldered | 11925 |
| Honor Device Co Ltd | VER-N49 | HONOR Magic V2 | 2023-12-13 | SGP.22 | soldered | 11921 |
| Motorola Mobility LLC | XT2363-3 (Type Name MC413) | XT2363-3 | 2023-12-11 | SGP.22 | soldered | 11916 |
| Samsung Electronics Co Ltd | SM-X306B | SM-X306B | 2023-12-08 | SGP.22 | soldered | 11914 |
| Samsung Electronics Co Ltd | SM-G556B | SM-G556B | 2023-11-30 | SGP.22 | soldered | 11901 |
| ZTE Corporation | nubia 8150N | nubia Neo 5G | 2023-11-25 | SGP.02 | not declared | 11895 |
| Samsung Electronics Co Ltd | SM-S921B/DS, SM-S921B | SM-S921B/DS, SM-S921B | 2023-11-22 | SGP.22 | soldered | 11891 |
| Samsung Electronics Co Ltd | SM-S926B/DS, SM-S926B | SM-S926B/DS, SM-S926B | 2023-11-22 | SGP.22 | soldered | 11887 |
| Samsung Electronics Co Ltd | SM-S928B/DS, SM-S928B | SM-S928B/DS, SM-S928B | 2023-11-22 | SGP.22 | soldered | 11892 |
| Motorola Mobility LLC | XT2309-4 | XT2309-4 | 2023-11-12 | SGP.22 | soldered | 11908 |
| Xiaomi Communications | 23127PN0CG | Xiaomi 14 | 2023-10-25 | SGP.22 | soldered | 11842 |
| Zebra Technologies Corporation | ET65AW | ET65 | 2023-10-25 | SGP.22 | both | 11840 |
| Xiaomi Communications | 23090RA98G | Redmi Note 13 Pro+ 5G | 2023-10-10 | SGP.22 | soldered | 11813 |
| Xiaomi Communications | 2312DRA50G | Redmi Note 13 Pro 5G | 2023-10-08 | SGP.22 | soldered | 11810 |
| Crosscall SAS | Stellar-X5 | Stellar-X5 | 2023-08-28 | SGP.22 | soldered | 11686 |
| Ascom (Sweden) AB | SH4-AACC | Myco 4 Cellular | 2023-08-24 | SGP.22 | soldered | 11757 |
| Ascom (Sweden) AB | SH4-AACB | Myco 4 Cellular | 2023-08-24 | SGP.22 | soldered | 11758 |
| Fairphone B.V. | FP5 | Fairphone 5 5G | 2023-08-15 | SGP.22 | soldered | 11677 |
| Google LLC | GKWS6 | GKWS6 | 2023-08-14 | SGP.22 | not declared | 11705 |
| Google LLC | GZPF0 | GZPF0 | 2023-08-14 | SGP.22 | not declared | 11707 |
| Google LLC | GPJ41 | GPJ41 | 2023-08-14 | SGP.22 | not declared | 11706 |
| Google LLC | G9BQD | G9BQD | 2023-08-14 | SGP.22 | not declared | 11772 |
| Google LLC | GC3VE | GC3VE | 2023-08-14 | SGP.22 | not declared | 11709 |
| Google LLC | G1MNW | G1MNW | 2023-08-14 | SGP.22 | not declared | 11708 |
| Samsung Electronics Co Ltd | SM-S711B/DS | SM-S711B/DS | 2023-08-11 | SGP.22 | soldered | 11741 |
| ZTE Corporation | ZTE 7160N | ZTE Blade A73 5G | 2023-08-10 | SGP.02 | not declared | 11736 |
| Motorola Mobility LLC | XT2343-6 | XT2343-6 | 2023-08-07 | SGP.22 | soldered | 11725 |
| Motorola Mobility LLC | XT2343-1, XT2343-1 [DS], XT2343-1 [eDS] | XT2343-1 | 2023-08-07 | SGP.22 | soldered | 11723 |
| Motorola Mobility LLC | XT2343-2 (Type Name MC410) | XT2343-2 | 2023-08-07 | SGP.22 | soldered | 11724 |
| Motorola Mobility LLC | XT2347-1, XT2347-1 [eDS] | XT2347-1 | 2023-08-04 | SGP.22 | soldered | 11720 |
| Motorola Mobility LLC | XT2307-1, XT2307-1 [eDS] (Type Name MC40B) | XT2307-1 | 2023-08-03 | SGP.22 | soldered | 11716 |
| Xiaomi Communications | A301XM | Xiaomi 13T Pro | 2023-08-01 | SGP.22 | soldered | 11714 |
| Samsung Electronics Co Ltd | SM-X616B | SM-X616B | 2023-07-28 | SGP.22 | soldered | 11710 |
| Samsung Electronics Co Ltd | SM-X516B | SM-X516B | 2023-07-24 | SGP.22 | soldered | 11698 |
| Motorola Mobility LLC | XT2305-1 | XT2305-1 | 2023-07-12 | SGP.22 | soldered | 11678 |
| Sony Corporation | PM-1464-BV | XQ-DE54 | 2023-07-11 | SGP.22 | soldered | 11673 |
| Google LLC | GC3G8 | GC3G8 | 2023-07-10 | SGP.22 | soldered | 11680 |
| Google LLC | GD2WG | GD2WG | 2023-07-10 | SGP.22 | soldered | 11676 |
| Xiaomi Communications | 23078PND5G | Xiaomi 13T Pro | 2023-07-10 | SGP.22 | soldered | 11669 |
| Xiaomi Communications | 2306EPN60G | Xiaomi 13T | 2023-07-06 | SGP.22 | soldered | 11667 |
| Motorola Mobility LLC | XT2323-2 | XT2323-2 | 2023-06-30 | SGP.22 | soldered | 11661 |
| vivo Mobile Communication Co., Ltd. | V2250 | V29 | 2023-06-19 | SGP.22 | soldered | 11643 |
| Samsung Electronics Co Ltd | SM-F946B/DS, SM-F946B | SM-F946B/DS, SM-F946B | 2023-06-16 | SGP.22 | soldered | 11639 |
| Samsung Electronics Co Ltd | SM-F731B | SM-F731B | 2023-06-16 | SGP.22 | soldered | 11638 |
| Samsung Electronics Co Ltd | SM-R965F | SM-R965F | 2023-06-13 | SGP.22 | soldered | 11614 |
| Samsung Electronics Co Ltd | SM-R945F | SM-R945F | 2023-06-13 | SGP.22 | soldered | 11616 |
| Samsung Electronics Co Ltd | SM-R935F | SM-R935F | 2023-06-13 | SGP.22 | soldered | 11617 |
| Samsung Electronics Co Ltd | SM-R955F | SM-R955F | 2023-06-13 | SGP.22 | soldered | 11615 |
| Samsung Electronics Co Ltd | SM-X916B | SM-X916B | 2023-06-09 | SGP.22 | not declared | 11609 |
| Samsung Electronics Co Ltd | SM-X716B | SM-X716B | 2023-06-09 | SGP.22 | not declared | 11611 |
| i.safe MOBILE GmbH | M540A01 | IS540 | 2023-06-08 | SGP.22 | soldered | 11597 |
| Power Idea Technology (Shenzhen) Co., Ltd. | PSH02G | RG540 | 2023-06-08 | SGP.22 | soldered | 11691 |
| Motorola Mobility LLC | XT2323-1 (Type Name MC40A) | XT2323-1 | 2023-06-07 | SGP.22 | soldered | 11596 |
| Honor Device Co Ltd | REA-NX9 | HONOR 90 | 2023-06-01 | SGP.22 | soldered | 11588 |
| Zebra Technologies Corporation | WCMTJ | TC27,HC25,HC55 | 2023-05-29 | SGP.22 | both | 11584 |
| Foxconn International Holdings | RTBM-SHRWGEN / RTBM-EARWGEN | Stellantis vehicle | 2023-05-29 | SGP.02 | soldered | 11585 |
| Zebra Technologies Corporation | WCMTA | TC27, HC25, HC55 | 2023-05-29 | SGP.22 | both | 11582 |
| Huawei Technologies Co., Ltd. | ARC-AL00 | HUAWEI WATCH 4 | 2023-05-27 | SGP.22 | soldered | 11406 |
| Huawei Technologies Co., Ltd. | MDS-AL00 | HUAWEI WATCH 4 PRO | 2023-05-27 | SGP.22 | soldered | 11405 |
| Xiaomi Communications | M2233W1 | Xiaomi Watch 2 Pro | 2023-05-22 | SGP.22 | soldered | 11564 |
| Zebra Technologies Corporation | WCMTB | TC27,HC25,HC55 | 2023-04-28 | SGP.22 | both | 11486 |
| Sony Corporation | PM-1431-BV | XQ-DQ54 | 2023-04-27 | SGP.22 | soldered | 11482 |
| vivo Mobile Communication Co., Ltd. | V2244 | V29 Lite 5G | 2023-04-23 | SGP.22 | soldered | 11440 |
| Google LLC | G9FPL | G9FPL | 2023-04-21 | SGP.22 | soldered | 11413 |
| Motorola Mobility LLC | XT2303-2 (Type Name MC408) | XT2303-2 | 2023-04-14 | SGP.22 | soldered | 11423 |
| ResMed Pty Ltd | Air 11 | AirSense 11, AirCurve 11 | 2023-04-13 | SGP.02 | not declared | 11409 |
| Kyocera Corporation | E7200 | Ultra-X | 2023-04-10 | SGP.22 | soldered | 11415 |
| Sony Corporation | PM-1445-BV | XQ-DC54 | 2023-04-10 | SGP.22 | soldered | 11419 |
| Motorola Mobility LLC | XT2321-1 (Type Name MC402) | XT2321-1 | 2023-03-23 | SGP.22 | soldered | 11383 |
| HMD Global Oy | TA-1486, TA-1592 | TA-1486, TA-1592 | 2023-03-22 | SGP.22 | soldered | 11382 |
| Motorola Mobility LLC | XT2315-1, XT2315-1 [eDS] | XT2315-1 | 2023-03-16 | SGP.22 | soldered | 11362 |
| Motorola Mobility LLC | XT2321-3 | XT2321-3 | 2023-03-10 | SGP.22 | soldered | 11348 |
| Xplora Technologies AS | X6E | X6Play eSIM | 2023-02-25 | SGP.22 | soldered | 11338 |
| LG Electronics Inc | TLVUM3IU-E | TLVUM3IU-E | 2023-02-22 | SGP.02 | soldered | 11329 |
| LG Electronics Inc | TLVUW3IU-E | TLVUW3IU-E | 2023-02-22 | SGP.02 | soldered | 11328 |
| LG Electronics Inc | TLVUE4IU-E | TLVUE4IU-E | 2023-02-22 | SGP.02 | soldered | 11327 |
| Samsung Electronics Co Ltd | SM-A546E/DS, SM-A546E | SM-A546E/DS, SM-A546E | 2023-02-13 | SGP.22 | soldered | 11317 |
| Samsung Electronics Co Ltd | SM-A546B/DS | SM-A546B/DS | 2023-02-09 | SGP.22 | soldered | 11313 |
| Motorola Mobility LLC | XT2301-1 | XT2301-1 | 2023-02-07 | SGP.22 | soldered | 11318 |
| Honor Device Co Ltd | FRI-NX9 | HONOR Magic Vs | 2023-02-03 | SGP.22 | soldered | 11287 |
| Harman International Industries Inc | TCAM2 | TCAM2 | 2023-02-03 | SGP.02 | soldered | 11272 |
| Honor Device Co Ltd | PGT-N19 | HONOR Magic5 Pro | 2023-02-03 | SGP.22 | soldered | 11288 |
| Honeywell International Inc | CT47X1N | CT47X1N, CT47 | 2023-01-20 | SGP.22 | soldered | 11086 |
| Motorola Mobility LLC | XT2301-4, XT2301-4 [DS] (Type Name MC3F6) | XT2301-4 | 2023-01-20 | SGP.22 | soldered | 11267 |
| Google LLC | GHL1X | GHL1X | 2023-01-18 | SGP.22 | soldered | 11208 |
| Google LLC | GWKK3 | GWKK3 | 2023-01-18 | SGP.22 | soldered | 11207 |
| Google LLC | G0DZQ | G0DZQ | 2023-01-18 | SGP.22 | soldered | 11209 |
| Motorola Solutions Inc | MSLB-MKZ900ti | MOTOTRBO ION | 2023-01-11 | SGP.22 + SGP.02 | soldered | 11101 |
| Motorola Mobility LLC | XT2309-2, XT2309-2 [DS], XT2309-2 [eDS] (Type Name MC3FF) | XT2309-2 | 2023-01-03 | SGP.22 | soldered | 11210 |
| Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2437 | OPPO Find N2 Flip | 2022-12-30 | SGP.22 | not declared | 11211 |
| Motorola Mobility LLC | XT2311-4 | XT2311-4 | 2022-12-23 | SGP.22 | soldered | 11196 |
| Motorola Mobility LLC | XT2335-1 [eDS] (Type Name MC400) | XT2335-1 [eDS] | 2022-12-05 | SGP.22 | soldered | 11137 |
| Motorola Mobility LLC | XT2335-2 [eDS] (Type Name MC401) | XT2335-2 [eDS] | 2022-12-05 | SGP.22 | soldered | 11145 |
| Samsung Electronics Co Ltd | SM-S916B/DS, SM-S916B | SM-S916B/DS, SM-S916B | 2022-11-30 | SGP.22 | soldered | 11135 |
| Samsung Electronics Co Ltd | SM-S918B/DS, SM-S918B | SM-S918B/DS, SM-S918B | 2022-11-30 | SGP.22 | soldered | 11136 |
| Samsung Electronics Co Ltd | SM-S911B/DS, SM-S911B | SM-S911B/DS, SM-S911B | 2022-11-30 | SGP.22 | soldered | 11134 |
| Xiaomi Communications | 2210132G | Xiaomi 13 Pro | 2022-11-23 | SGP.22 | soldered | 11124 |
| Xiaomi Communications | 2211133G | Xiaomi 13 | 2022-11-22 | SGP.22 | soldered | 11123 |
| Samsung Electronics Co Ltd | NP345XNA | NP345XNA | 2022-11-21 | SGP.22 | soldered | 11115 |
| Zebra Technologies Corporation | TC78B1-2 | TC78 | 2022-11-15 | SGP.22 | both | 12317 |
| Zebra Technologies Corporation | TC78A1-2 | TC78 | 2022-11-15 | SGP.22 | both | 12315 |
| Zebra Technologies Corporation | TC78A1 | TC78 | 2022-11-15 | SGP.22 | both | 11105 |
| Zebra Technologies Corporation | TC78B1 | TC78 | 2022-11-15 | SGP.22 | both | 11106 |
| FCNT LLC | F-51C | F-51C | 2022-11-14 | SGP.22 | soldered | 11050 |
| Fairphone B.V. | FP4 | Fairphone 4 5G | 2022-11-11 | SGP.22 | soldered | 11093 |
| Pegatron Corporation | 84945296C | Telematics & Network Gateway (TANG)-JP | 2022-11-01 | SGP.02 | soldered | 11055 |
| Pegatron Corporation | 84911790C | Customer Facing Wi-Fi Module (CFWM)-JP | 2022-11-01 | SGP.02 | soldered | 11062 |
| Pegatron Corporation | 84945296C | Telematics & Network Gateway (TANG)-Dubai | 2022-11-01 | SGP.02 | soldered | 11061 |
| Pegatron Corporation | 84911790C | Customer Facing Wi-Fi Module (CFWM)-Dubai | 2022-11-01 | SGP.02 | soldered | 11063 |
| Xiaomi Communications | 2210129SG | Xiaomi 13 Lite | 2022-10-31 | SGP.22 | soldered | 11057 |
| Leoworx Ortungssysteme GmbH | Asset | Tracar Asset | 2022-10-28 | SGP.02 | soldered | 11060 |
| Xiaomi Communications | A201XM | Xiaomi 12T Pro | 2022-10-25 | SGP.22 | soldered | 11025 |
| HMD Global Oy | TA-1443 | Nokia X30 5G | 2022-09-26 | SGP.22 | not declared | 11003 |
| HMD Global Oy | TA-1450 | Nokia X30 5G | 2022-09-23 | SGP.22 | not declared | 10998 |
| HMD Global Oy | TA-1490 | Nokia G60 5G | 2022-08-22 | SGP.22 | soldered | 10923 |
| Zebra Technologies Corporation | TC58A1 | TC58 | 2022-08-18 | SGP.22 | both | 10911 |
| Pegatron Corporation | 84945296C | Telematics & Network Gateway (TANG) | 2022-08-15 | SGP.02 | soldered | 10860 |
| Pegatron Corporation | 84911790C | Customer Facing Wi-Fi Module (CFWM) | 2022-08-15 | SGP.02 | soldered | 10863 |
| Microsoft Corporation | 1997 | Surface Model 1997 | 2022-08-12 | SGP.22 | soldered | 10889 |
| Microsoft Corporation | 1996 | Surface Model 1996 | 2022-08-12 | SGP.22 | soldered | 10890 |
| HMD Global Oy | TA-1479 | Nokia G60 5G | 2022-08-11 | SGP.22 | soldered | 10888 |
| Xiaomi Communications | 22081212UG | Xiaomi 12T Pro | 2022-08-03 | SGP.22 | soldered | 10867 |
| Sony Corporation | PM-1410-BV | XQ-CQ54 | 2022-07-29 | SGP.22 | soldered | 10838 |
| Google LLC | GE2AE | GE2AE | 2022-07-21 | SGP.22 | soldered | 10854 |
| Google LLC | GVU6C | GVU6C | 2022-07-21 | SGP.22 | soldered | 10857 |
| Google LLC | GQML3 | GQML3 | 2022-07-21 | SGP.22 | soldered | 10856 |
| Google LLC | GP4BC | GP4BC | 2022-07-21 | SGP.22 | soldered | 10855 |
| Zebra Technologies Corporation | TC58B1 | TC58 | 2022-07-08 | SGP.22 | both | 10779 |
| Samsung Electronics Co Ltd | SM-F936B/DS, SM-F936B | SM-F936B/DS, SM-F936B | 2022-07-06 | SGP.22 | soldered | 10777 |
| Samsung Electronics Co Ltd | SM-F721B | SM-F721B | 2022-07-06 | SGP.22 | soldered | 10778 |
| Samsung Electronics Co Ltd | SM-R905F | SM-R905F | 2022-06-24 | SGP.22 | soldered | 10740 |
| Samsung Electronics Co Ltd | SM-R915F | SM-R915F | 2022-06-24 | SGP.22 | soldered | 10741 |
| Samsung Electronics Co Ltd | SM-R925F | SM-R925F | 2022-06-24 | SGP.22 | soldered | 10742 |
| Google LLC | GWT9R | GWT9R | 2022-06-01 | SGP.22 | soldered | 10275 |
| Google LLC | GBZ4S | GBZ4S | 2022-06-01 | SGP.22 | soldered | 10278 |
| Harman International Industries Inc | WAVE-11-HAF-R2 | WAVE-11-HAF-R2 | 2022-05-24 | SGP.22 | soldered | 10673 |
| Harman International Industries Inc | WAVE-11-HIGH-R2 | WAVE-11-HIGH-R2 | 2022-05-23 | SGP.22 | soldered | 10670 |
| Motorola Mobility LLC | XT2213-3 [DS] (Type Name M7B9B) | XT2213-3 [DS] | 2022-04-29 | SGP.22 | removable | 10632 |
| Sony Corporation | PM-1380-BV | XQ-CT54 | 2022-04-25 | SGP.22 | soldered | 10613 |
| Honeywell International Inc | CT30PL1N | CT30 XP | 2022-04-22 | SGP.22 | soldered | 10558 |
| Sony Corporation | PM-1390-BV | XQ-CC54 | 2022-04-19 | SGP.22 | soldered | 10604 |
| Honor Device Co Ltd | LGE-NX9 | HONOR Magic4 Pro | 2022-04-02 | SGP.22 | soldered | 10252 |
| Xiaomi Communications | 2201116SR | Redmi Note 11 Pro 5G | 2022-04-01 | SGP.22 | soldered | 10426 |
| Google LLC | GB62Z | GB62Z | 2022-03-18 | SGP.22 | soldered | 10466 |
| Google LLC | G1AZG | G1AZG | 2022-03-18 | SGP.22 | soldered | 10465 |
| Google LLC | GX7AS | GX7AS | 2022-03-18 | SGP.22 | soldered | 10464 |
| Honeywell International Inc | CT45P-L1N-E | CT45P | 2022-02-18 | SGP.22 | soldered | 10365 |
| Xiaomi Communications | A101XM | Redmi Note 10T | 2022-01-28 | SGP.22 | soldered | 10375 |
| Kyocera Corporation | A201KC | A201KC | 2022-01-26 | SGP.22 | removable | 10371 |
| Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2307 | OPPO Find X5 | 2022-01-20 | SGP.22 | soldered | 10358 |
| Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2305 | OPPO Find X5 pro | 2022-01-19 | SGP.22 | soldered | 10354 |
| Samsung Electronics Co Ltd | SM-S908B/DS | SM-S908B/DS | 2021-12-31 | SGP.22 | soldered | 10331 |
| Samsung Electronics Co Ltd | SM-S906B/DS | SM-S906B/DS | 2021-12-31 | SGP.22 | soldered | 10330 |
| Samsung Electronics Co Ltd | SM-S901B/DS | SM-S901B/DS | 2021-12-31 | SGP.22 | soldered | 10329 |
| Samsung Electronics Co Ltd | SM-S906E/DS, SM-S906E | SM-S906E/DS, SM-S906E | 2021-12-22 | SGP.22 | soldered | 10316 |
| Samsung Electronics Co Ltd | SM-S901E/DS, SM-S901E | SM-S901E/DS, SM-S901E | 2021-12-22 | SGP.22 | soldered | 10317 |
| Samsung Electronics Co Ltd | SM-S908E/DS, SM-S908E | SM-S908E/DS, SM-S908E | 2021-12-22 | SGP.22 | soldered | 10315 |
| Microsoft Corporation | 2022_3 | Microsoft Surface Go 3 | 2021-11-19 | SGP.22 | both | 10281 |
| Microsoft Corporation | 2022_2 | Microsoft Surface Go 3 | 2021-11-19 | SGP.22 | both | 10280 |
| Microsoft Corporation | 2022 | Microsoft Surface Go 3 | 2021-11-18 | SGP.22 | both | 10279 |
| Microsoft Corporation | 1982 | Surface Pro 8 LTE | 2021-11-15 | SGP.22 | soldered | 10254 |

## RSP compliance declarations (435)

Separate register: RSP compliance declared without a full certification record.
Mostly notebooks and handsets; only a few cross-reference a GCF certification.

| RSP ID | Manufacturer | Model | Marketing name | Declared | GCF ref |
|---|---|---|---|---|---|
| RSP0451 | Realme Chongqing Mobile Telecommunications Corporation Ltd. | RMX5343 | RMX5343 | 2026-10-22 | - |
| RSP0449 | vivo Mobile Communication Co., Ltd. | V2615 | V70 Lite 5G | 2026-09-16 | 13976 |
| RSP0448 | vivo Mobile Communication Co., Ltd. | V2610 | X500 Pro Max | 2026-09-16 | 13970 |
| RSP0450 | vivo Mobile Communication Co., Ltd. | V2637 | V70 Lite 5G | 2026-09-16 | 13975 |
| RSP0446 | vivo Mobile Communication Co., Ltd. | V2621 | X500 Pro | 2026-09-16 | 14002 |
| RSP0447 | vivo Mobile Communication Co., Ltd. | V2622 | X500 Pro | 2026-09-16 | 14003 |
| RSP0445 | Lenovo Mobile Communication Technology Co Ltd | ThinkEdge SE10 Gen2 | ThinkEdge SE10 Gen2 | 2026-09-01 | - |
| RSP0444 | vivo Mobile Communication Co., Ltd. | V2559 | X Fold6 | 2026-08-31 | - |
| RSP0442 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2913 | CPH2913 | 2026-08-13 | - |
| RSP0443 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2911 | CPH2911 | 2026-08-13 | - |
| RSP0441 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2931 | CPH2931 | 2026-07-16 | - |
| RSP0432 | Lenovo Mobile Communication Technology Co Ltd | Announce34 | Announce34 | 2026-05-13 | - |
| RSP0431 | Lenovo Mobile Communication Technology Co Ltd | Announce33 | Announce33 | 2026-05-13 | - |
| RSP0439 | Lenovo Mobile Communication Technology Co Ltd | Announce41 | Announce41 | 2026-04-29 | - |
| RSP0434 | Lenovo Mobile Communication Technology Co Ltd | Announce36 | Announce36 | 2026-04-28 | - |
| RSP0433 | Lenovo Mobile Communication Technology Co Ltd | Announce35 | Announce35 | 2026-04-28 | - |
| RSP0440 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2865 | CPH2865 | 2026-04-03 | - |
| RSP0420 | vivo Mobile Communication Co., Ltd. | V2562 | X300 Ultra | 2026-03-27 | - |
| RSP0418 | vivo Mobile Communication Co., Ltd. | V2538 | V70 | 2026-03-27 | - |
| RSP0419 | vivo Mobile Communication Co., Ltd. | V2540 | V70 | 2026-03-27 | - |
| RSP0415 | Lenovo Mobile Communication Technology Co Ltd | Announce20 | Announce20 | 2026-03-25 | - |
| RSP0416 | Lenovo Mobile Communication Technology Co Ltd | Announce22 | Announce22 | 2026-03-25 | - |
| RSP0417 | Lenovo Mobile Communication Technology Co Ltd | Announce21 | Announce21 | 2026-03-25 | - |
| RSP0412 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 2-in-1 Gen 11 (RW101R-GL) | ThinkPad X1 2-in-1 Gen 11 | 2026-03-24 | - |
| RSP0411 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Carbon Gen 14 (RW101R-GL) | ThinkPad X1 Carbon Gen 14 | 2026-03-24 | - |
| RSP0410 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 2-in-1 Gen 11 (T99W696) | ThinkPad X1 2-in-1 Gen 11 | 2026-03-24 | - |
| RSP0409 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Carbon Gen 14 (T99W696) | ThinkPad X1 Carbon Gen 14 | 2026-03-24 | - |
| RSP0414 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2863 | CPH2863 | 2026-03-20 | - |
| RSP0422 | Lenovo Mobile Communication Technology Co Ltd | Thinkpad P14s AMD Gen 7 (T99W696) | Thinkpad P14s AMD Gen 7 | 2026-03-19 | - |
| RSP0424 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P16s Gen 5 (T99W696) | ThinkPad P16s Gen 5 | 2026-03-19 | - |
| RSP0421 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P1 Gen 9 (T99W696) | ThinkPad P1 Gen 9 | 2026-03-19 | - |
| RSP0423 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P14s Gen 7 (T99W696) | ThinkPad P14s Gen 7 | 2026-03-19 | - |
| RSP0429 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T1g Gen 9 (T99W696) | ThinkPad T1g Gen 9 | 2026-03-19 | - |
| RSP0413 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2859 | CPH2859 | 2026-03-16 | - |
| RSP0425 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14 Gen 7 (T99W696) | ThinkPad T14 Gen 7 | 2026-03-05 | - |
| RSP0426 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14s 2-in-1 Gen 2 (T99W696) | ThinkPad T14s 2-in-1 Gen 2 | 2026-03-05 | - |
| RSP0430 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13 Detachable Gen 1 (T99W696) | ThinkPad X13 Detachable Gen 1 | 2026-03-05 | - |
| RSP0427 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14s Gen 7 (T99W696) | ThinkPad T14s Gen 7 | 2026-03-05 | - |
| RSP0435 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14 Gen 7 (RW101R-GL) | ThinkPad T14 Gen 7 | 2026-03-05 | - |
| RSP0437 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14s Gen 7 (RW101R-GL) | ThinkPad T14s Gen 7 | 2026-03-05 | - |
| RSP0438 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T16 Gen 5 (RW101R-GL) | ThinkPad T16 Gen 5 | 2026-03-05 | - |
| RSP0428 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T16 Gen 5 (T99W696) | ThinkPad T16 Gen 5 | 2026-03-05 | - |
| RSP0436 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14s 2-in-1 Gen 2 (RW101R-GL) | ThinkPad T14s 2-in-1 Gen 2 | 2026-03-05 | - |
| RSP0407 | vivo Mobile Communication Co., Ltd. | V2542 | X300 FE | 2026-03-04 | 13599 |
| RSP0408 | vivo Mobile Communication Co., Ltd. | V2537 | X300 FE | 2026-03-04 | 13598 |
| RSP0405 | Lenovo Mobile Communication Technology Co Ltd | d-51F | dtab | 2026-02-19 | - |
| RSP0404 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2841 | CPH2841 | 2026-01-29 | - |
| RSP0403 | vivo Mobile Communication Co., Ltd. | V2533 | Y31e 5G | 2026-01-08 | - |
| RSP0402 | vivo Mobile Communication Co., Ltd. | V2552 | V70 FE | 2026-01-04 | 13502 |
| RSP0401 | vivo Mobile Communication Co., Ltd. | V2550 | V70 FE | 2026-01-04 | 13503 |
| RSP0396 | Lenovo Mobile Communication Technology Co Ltd | Lenovo Chromebook 500e 2in1 Gen5(RW101R-GL) (12in) | Lenovo Chromebook 500e 2-in-1 Gen 5 | 2025-12-11 | - |
| RSP0397 | Lenovo Mobile Communication Technology Co Ltd | Lenovo Chromebook 500e 2in1 Gen5(RW101R-GL)(11in) | Lenovo Chromebook 500e 2-in-1 Gen 5 | 2025-12-11 | - |
| RSP0400 | Lenovo Mobile Communication Technology Co Ltd | Lenovo Chromebook 100e Gen 5 (RW101R-GL)(12inch) | Lenovo Chromebook 100e Gen 5 (RW101R-GL) | 2025-12-11 | - |
| RSP0398 | Lenovo Mobile Communication Technology Co Ltd | Lenovo Chromebook 14 (RW101R-GL) | Lenovo Chromebook 14 | 2025-12-11 | - |
| RSP0399 | Lenovo Mobile Communication Technology Co Ltd | Lenovo Chromebook 100e Gen 5 (RW101R-GL)(11inch) | Lenovo Chromebook 100e Gen 5 | 2025-12-11 | - |
| RSP0395 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T16g Gen 3 (RW350-GL) | ThinkPad T16g Gen 3 | 2025-12-01 | - |
| RSP0394 | vivo Mobile Communication Co., Ltd. | V2521 | Y31 5G | 2025-11-12 | - |
| RSP0392 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2825 | CPH2825 | 2025-10-30 | - |
| RSP0391 | Lenovo Mobile Communication Technology Co Ltd | A401LV | Lenovo TAB8 | 2025-10-11 | - |
| RSP0389 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2801 | CPH2801 | 2025-09-29 | - |
| RSP0390 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2813 | CPH2813 | 2025-09-29 | - |
| RSP0388 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2797 | CPH2797 | 2025-08-28 | - |
| RSP0387 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2791 | CPH2791 | 2025-08-28 | - |
| RSP0381 | vivo Mobile Communication Co., Ltd. | V2512 | V2512 | 2025-08-15 | - |
| RSP0385 | vivo Mobile Communication Co., Ltd. | V2515 | V2515 | 2025-08-15 | - |
| RSP0380 | vivo Mobile Communication Co., Ltd. | V2511 | V2511 | 2025-08-15 | - |
| RSP0386 | vivo Mobile Communication Co., Ltd. | V2514 | V2514 | 2025-08-15 | - |
| RSP0382 | vivo Mobile Communication Co., Ltd. | V2429 | V2429 | 2025-08-07 | - |
| RSP0379 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2781 | CPH2781 | 2025-07-17 | - |
| RSP0378 | Lenovo Mobile Communication Technology Co Ltd | TB336ZJ | TB336ZJ | 2025-07-14 | - |
| RSP0376 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2737 | CPH2737 | 2025-06-18 | - |
| RSP0366 | Lenovo Mobile Communication Technology Co Ltd | Announce 23 | Announce 23 | 2025-05-29 | - |
| RSP0365 | Lenovo Mobile Communication Technology Co Ltd | Announce 22 | Announce 22 | 2025-05-29 | - |
| RSP0361 | Lenovo Mobile Communication Technology Co Ltd | Announce 18 | Announce 18 | 2025-05-28 | - |
| RSP0356 | Lenovo Mobile Communication Technology Co Ltd | Announce 12 | Announce 12 | 2025-05-28 | - |
| RSP0362 | Lenovo Mobile Communication Technology Co Ltd | Announce 19 | Announce 19 | 2025-05-28 | - |
| RSP0375 | Fairphone B.V. | FP6 | Fairphone (Gen.6) | 2025-05-26 | 12968 |
| RSP0374 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2743 | CPH2743 | 2025-05-26 | - |
| RSP0373 | Lenovo Mobile Communication Technology Co Ltd | TB332ZJ | Lenovo TAB8 | 2025-04-28 | - |
| RSP0353 | Lenovo Mobile Communication Technology Co Ltd | Announce 5 | Announce 5 | 2025-04-24 | - |
| RSP0357 | Lenovo Mobile Communication Technology Co Ltd | Announce 13 | Announce 13 | 2025-04-24 | - |
| RSP0358 | Lenovo Mobile Communication Technology Co Ltd | Announce 14 | Announce 14 | 2025-04-24 | - |
| RSP0352 | Lenovo Mobile Communication Technology Co Ltd | Announce 4 | Announce 4 | 2025-04-24 | - |
| RSP0371 | vivo Mobile Communication Co., Ltd. | V2503 | V2503 | 2025-04-16 | - |
| RSP0372 | vivo Mobile Communication Co., Ltd. | V2505 | V2505 | 2025-04-16 | - |
| RSP0368 | Lenovo Mobile Communication Technology Co Ltd | Announce7 | Announce7 | 2025-04-01 | - |
| RSP0367 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13 Gen 6 (RW350-GL) | ThinkPad X13 Gen 6 | 2025-04-01 | - |
| RSP0369 | Lenovo Mobile Communication Technology Co Ltd | Announce8 | Announce8 | 2025-04-01 | - |
| RSP0359 | Lenovo Mobile Communication Technology Co Ltd | Announce 15 | Announce 15 | 2025-03-10 | - |
| RSP0350 | Lenovo Mobile Communication Technology Co Ltd | Announce 2 | Announce 2 | 2025-03-10 | - |
| RSP0354 | Lenovo Mobile Communication Technology Co Ltd | Announce 9 | Announce 9 | 2025-03-10 | - |
| RSP0351 | Lenovo Mobile Communication Technology Co Ltd | Announce 3 | Announce 3 | 2025-03-07 | - |
| RSP0355 | Lenovo Mobile Communication Technology Co Ltd | Announce 10 | Announce 10 | 2025-03-07 | - |
| RSP0360 | Lenovo Mobile Communication Technology Co Ltd | Announce 16 | Announce 16 | 2025-03-07 | - |
| RSP0364 | Lenovo Mobile Communication Technology Co Ltd | Announce 21 | Announce 21 | 2025-03-07 | - |
| RSP0363 | Lenovo Mobile Communication Technology Co Ltd | Announce 20 | Announce 20 | 2025-03-07 | - |
| RSP0349 | Lenovo Mobile Communication Technology Co Ltd | Announce 1 | Announce 1 | 2025-03-07 | - |
| RSP0346 | Lenovo Mobile Communication Technology Co Ltd | Announce10 | Announce10 | 2025-02-27 | - |
| RSP0348 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 2-in-1 Gen 10 (RM520-GL) | ThinkPad X1 2-in-1 Gen 10 | 2025-02-27 | - |
| RSP0347 | Lenovo Mobile Communication Technology Co Ltd | Announce12 | Announce12 | 2025-02-27 | - |
| RSP0342 | Lenovo Mobile Communication Technology Co Ltd | Announce11 | Announce11 | 2025-02-19 | - |
| RSP0345 | Lenovo Mobile Communication Technology Co Ltd | Lenovo 300w Gen 5 EM060K-GL | Lenovo 300w Gen 5 | 2025-02-19 | - |
| RSP0344 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2695 | CPH2695 | 2025-02-10 | - |
| RSP0343 | Lenovo Mobile Communication Technology Co Ltd | Announce17 | Announce17 | 2025-01-30 | - |
| RSP0341 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2699 | CPH2699 | 2025-01-22 | - |
| RSP0340 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Carbon Gen 13 (RM520-GL) | ThinkPad X1 Carbon Gen 13 | 2025-01-14 | - |
| RSP0339 | vivo Mobile Communication Co., Ltd. | V2440 | V2440 | 2025-01-10 | - |
| RSP0337 | vivo Mobile Communication Co., Ltd. | V2427 | V2427 | 2024-12-11 | - |
| RSP0338 | vivo Mobile Communication Co., Ltd. | V2428 | V2428 | 2024-12-11 | - |
| RSP0336 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2697 | CPH2697 | 2024-11-05 | - |
| RSP0335 | Guangdong OPPO Mobile Telecommunications Corp Ltd | CPH2689 | CPH2689 | 2024-10-15 | - |
| RSP0334 | vivo Mobile Communication Co., Ltd. | V2415 | V2415 | 2024-09-23 | - |
| RSP0333 | vivo Mobile Communication Co., Ltd. | V2413 | V2413 | 2024-09-23 | - |
| RSP0332 | vivo Mobile Communication Co., Ltd. | V2418 | V2418 | 2024-07-22 | - |
| RSP0331 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14s Gen 6 (RM520N-GL) | ThinkPad T14s Gen 6 | 2024-05-20 | - |
| RSP0330 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14s Gen 6 Snapdragon (RM520N-GL) | ThinkPad T14s Gen 6 Snapdragon | 2024-05-20 | - |
| RSP0327 | vivo Mobile Communication Co., Ltd. | V2348 | V2348 | 2024-03-28 | - |
| RSP0326 | vivo Mobile Communication Co., Ltd. | V2341 | V2341 | 2024-03-14 | - |
| RSP0323 | Dell Inc | Precision 3591 LTE | Precision 3591 | 2024-02-22 | - |
| RSP0322 | Dell Inc | Precision 3591 5G | Precision 3591 | 2024-02-19 | - |
| RSP0312 | Dell Inc | Latitude 5350 5G | Latitude 5350 | 2024-02-19 | - |
| RSP0325 | Dell Inc | Latitude 7350 5G | Latitude 7350 | 2024-02-19 | - |
| RSP0320 | Dell Inc | Precision 3590 5G | Precision 3590 | 2024-02-19 | - |
| RSP0316 | Dell Inc | Latitude 5550 5G | Latitude 5550 | 2024-02-19 | - |
| RSP0318 | Dell Inc | Precision 3490 5G | Precision 3490 | 2024-02-16 | - |
| RSP0314 | Dell Inc | Latitude 5450 5G | Latitude 5450 | 2024-02-16 | - |
| RSP0319 | Dell Inc | Precision 3490 LTE | Precision 3490 | 2024-02-15 | - |
| RSP0315 | Dell Inc | Latitude 5450 LTE | Latitude 5450 | 2024-02-15 | - |
| RSP0321 | Dell Inc | Precision 3590 LTE | Precision 3590 | 2024-02-15 | - |
| RSP0329 | Dell Inc | Latitude 7450 LTE | Latitude 7450 LTE | 2024-02-15 | - |
| RSP0317 | Dell Inc | Latitude 5550 LTE | Latitude 5550 | 2024-02-15 | - |
| RSP0324 | Dell Inc | Latitude 7350 LTE | Latitude 7350 | 2024-02-15 | - |
| RSP0313 | Dell Inc | Latitude 5350 LTE | Latitude 5350 | 2024-02-15 | - |
| RSP0289 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 2-in-1 Gen 9 (RM520-GL) | ThinkPad X1 2-in-1 Gen 9 | 2024-02-08 | - |
| RSP0301 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X12 Detachable Gen 2 (EM160R-GL) | ThinkPad X12 Detachable Gen 2 | 2024-02-08 | - |
| RSP0299 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P16s Gen 3 (EM160R-GL) | ThinkPad P16s Gen 3 | 2024-02-08 | - |
| RSP0303 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L14 Gen 5 (EM061K-GL) | ThinkPad L14 Gen 5 | 2024-02-08 | - |
| RSP0309 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L13 Gen 5 (EM061K-GL) | ThinkPad L13 Gen 5 | 2024-02-08 | - |
| RSP0300 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P16v Gen 2 (EM160R-GL) | ThinkPad P16v Gen 2 | 2024-02-08 | - |
| RSP0290 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14s Gen 5 (RM520N-GL) | ThinkPad T14s Gen 5 | 2024-02-08 | - |
| RSP0304 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L16 Gen 1 (EM061K-GL) | ThinkPad L16 Gen 1 | 2024-02-08 | - |
| RSP0305 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14s Gen 5 (EM061K-GL) | ThinkPad T14s Gen 5 | 2024-02-08 | - |
| RSP0291 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14 Gen 5 RM520N | ThinkPad T14 Gen 5 | 2024-02-08 | - |
| RSP0298 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P14s Gen 5 (EM160R-GL) | ThinkPad P14s Gen 5 | 2024-02-08 | - |
| RSP0307 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T16 Gen 3 (EM061K-GL) | ThinkPad T16 Gen 3 | 2024-02-08 | - |
| RSP0293 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P14s Gen 5 (RM520N-GL) | ThinkPad P14s Gen 5 | 2024-02-08 | - |
| RSP0310 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L13 2-in-1 Gen 5 (EM061K-GL) | ThinkPad L13 2-in-1 Gen 5 | 2024-02-08 | - |
| RSP0306 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14 Gen 5 (EM061K-GL) | ThinkPad T14 Gen 5 | 2024-02-08 | - |
| RSP0297 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14 Gen 5 (EM160R-GL) | ThinkPad T14 Gen 5 | 2024-02-08 | - |
| RSP0294 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 2-in-1 Gen 9 (EM160R-GL) | ThinkPad X1 2-in-1 Gen 9 | 2024-02-08 | - |
| RSP0302 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13 2-in-1 Gen 5 (EM061K-GL) | ThinkPad X13 2-in-1 Gen 5 | 2024-02-08 | - |
| RSP0308 | Lenovo Mobile Communication Technology Co Ltd | Deferred 20 | Deferred 20 | 2024-02-08 | - |
| RSP0292 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T16 Gen 3 (RM520N-GL) | ThinkPad T16 Gen 3 | 2024-02-08 | - |
| RSP0296 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L14 Gen 5 (EM160R-GL) | ThinkPad L14 Gen 5 | 2024-02-08 | - |
| RSP0295 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13 2-in-1 Gen 5 (EM160R-GL) | ThinkPad X13 2-in-1 Gen 5 | 2024-02-08 | - |
| RSP0286 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Carbon Gen 12 RM520N-GL | ThinkPad X1 Carbon Gen 12 | 2024-02-05 | - |
| RSP0288 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13 Gen 5 (EM061K-GL) | ThinkPad X13 Gen 5 | 2024-02-05 | - |
| RSP0287 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Carbon Gen 12 EM160R-GL | ThinkPad X1 Carbon Gen 12 | 2024-02-05 | - |
| RSP0282 | Lenovo Mobile Communication Technology Co Ltd | Lenovo 500e Chromebook Gen 4 EM060K | Lenovo 500e Chromebook Gen 4 | 2024-01-10 | - |
| RSP0281 | Lenovo Mobile Communication Technology Co Ltd | Lenovo 100e Chromebook Gen 4 EM060K | Lenovo 100e Chromebook Gen 4 | 2024-01-10 | - |
| RSP0283 | Lenovo Mobile Communication Technology Co Ltd | Deferred 1 | Deferred 1 | 2024-01-10 | - |
| RSP0328 | Dell Inc | Chromebook 3120 Education | Chromebook 3120 Education | 2024-01-05 | - |
| RSP0280 | vivo Mobile Communication Co., Ltd. | V2337 | V2337 | 2023-12-26 | - |
| RSP0285 | Dell Inc | Latitude 7030 Rugged Extreme Tablet - LTE | Latitude 7030 Rugged Extreme Tablet | 2023-12-15 | - |
| RSP0284 | Dell Inc | Latitude 7030 Rugged Extreme Tablet | Latitude 7030 Rugged Extreme Tablet | 2023-11-01 | - |
| RSP0279 | Kyocera Corporation | KY-51D | KY-51D | 2023-10-16 | - |
| RSP0278 | vivo Mobile Communication Co., Ltd. | V2309 | V2309 | 2023-09-20 | - |
| RSP0277 | Fairphone B.V. | FP5 | Fairphone 5 5G | 2023-08-15 | 11677 |
| RSP0276 | Lenovo Mobile Communication Technology Co Ltd | ThinkEdge SE10 | ThinkEdge SE10 | 2023-07-20 | - |
| RSP0275 | Sony Corporation | PM-1461-BV | PM-1461-BV | 2023-07-11 | - |
| RSP0274 | vivo Mobile Communication Co., Ltd. | V2250 | V2250 | 2023-04-27 | - |
| RSP0245 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P1 Gen 6 L860 | ThinkPad P1 Gen 6 | 2023-03-23 | - |
| RSP0249 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P16s Gen 2 L860 | ThinkPad P16s Gen 2 | 2023-03-23 | - |
| RSP0243 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P14s Gen 4 EM05 | ThinkPad P14s Gen 4 | 2023-03-23 | - |
| RSP0244 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P16s Gen 2 EM05 | ThinkPad P16s Gen 2 | 2023-03-23 | - |
| RSP0236 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14 Gen 4 L860 | ThinkPad T14 Gen 4 | 2023-03-23 | - |
| RSP0239 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Yoga Gen 8 L860 | ThinkPad X1 Yoga Gen 8 | 2023-03-23 | - |
| RSP0238 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T16 Gen 2 L860 | ThinkPad T16 Gen 2 | 2023-03-23 | - |
| RSP0240 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13 Gen 4 L860 | ThinkPad X13 Gen 4 | 2023-03-23 | - |
| RSP0237 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14s Gen 4 L860 | ThinkPad T14s Gen 4 | 2023-03-23 | - |
| RSP0246 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P14s Gen 4 L860 | ThinkPad P14s Gen 4 | 2023-03-23 | - |
| RSP0235 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L15 Gen 4 L860 | ThinkPad L15 Gen 4 | 2023-03-23 | - |
| RSP0248 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P16 v Gen 1 L860 | ThinkPad P16 v Gen 1 | 2023-03-23 | - |
| RSP0247 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P16 Gen 2 L860 | ThinkPad P16 Gen 2 | 2023-03-23 | - |
| RSP0234 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L14 Gen 4 L860 | ThinkPad L14 Gen 4 | 2023-03-23 | - |
| RSP0241 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13 Yoga Gen 4 L860 | ThinkPad X13 Yoga Gen 4 | 2023-03-23 | - |
| RSP0242 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad Z13 Gen 2 L860 | ThinkPad Z13 Gen 2 | 2023-03-23 | - |
| RSP0231 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad 13W Yoga Gen 2 L860 | ThinkPad 13W Yoga Gen 2 | 2023-03-22 | - |
| RSP0261 | Dell Inc | Latitude 7340 5G 2-in-1 | Latitude 7340 | 2023-03-22 | - |
| RSP0232 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L13 Gen 4 L860 | ThinkPad L13 Gen 4 | 2023-03-22 | - |
| RSP0233 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L13 Yoga Gen 4 L860 | ThinkPad L13 Yoga Gen 4 | 2023-03-22 | - |
| RSP0269 | Dell Inc | Latitude 3440 | Latitude 3440 | 2023-03-21 | - |
| RSP0230 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Carbon Gen 11 L860 | ThinkPad X1 Carbon Gen 11 | 2023-03-20 | - |
| RSP0264 | Dell Inc | Latitude 7440 2-in-1 | Latitude 7440 | 2023-03-17 | - |
| RSP0253 | Dell Inc | Latitude 5440 | Latitude 5440 | 2023-03-17 | - |
| RSP0270 | Dell Inc | Latitude 3540 | Latitude 3540 | 2023-03-17 | - |
| RSP0258 | Dell Inc | Precision 3580 | Precision 3580 | 2023-03-17 | - |
| RSP0263 | Dell Inc | Latitude 7440 | Latitude 7440 | 2023-03-17 | - |
| RSP0256 | Dell Inc | Precision 3480 | Precision 3480 | 2023-03-17 | - |
| RSP0273 | Dell Inc | Latitude 7340 | Latitude 7340 | 2023-03-17 | - |
| RSP0255 | Dell Inc | Latitude 5540 | Latitude 5540 | 2023-03-17 | - |
| RSP0267 | Dell Inc | Latitude 7640 | Latitude 7640 | 2023-03-17 | - |
| RSP0259 | Dell Inc | Precision 3581 | Precision 3581 | 2023-03-17 | - |
| RSP0260 | Dell Inc | Precision 3581 5G | Precision 3581 | 2023-03-17 | - |
| RSP0272 | Dell Inc | Latitude 5340 | Latitude 5340 | 2023-03-15 | - |
| RSP0250 | Dell Inc | Latitude 5340 2-in-1 | Latitude 5340 | 2023-03-15 | - |
| RSP0271 | Dell Inc | Latitude 9440 2-in-1 | Latitude 9440 | 2023-03-09 | - |
| RSP0229 | vivo Mobile Communication Co., Ltd. | V2244 | V2244 | 2023-03-08 | - |
| RSP0227 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13 Yoga Gen 4 EM05-G | ThinkPad X13 Yoga Gen 4 | 2023-03-06 | - |
| RSP0221 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L13 Yoga Gen 4 EM05-G | ThinkPad L13 Yoga Gen 4 | 2023-03-06 | - |
| RSP0220 | Dell Inc | Precision 7780 | Precision 7780 | 2023-03-06 | - |
| RSP0224 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14s Gen 4 EM05-G | ThinkPad T14s Gen 4 | 2023-03-06 | - |
| RSP0225 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T16 Gen 2 EM05-G | ThinkPad T16 Gen 2 | 2023-03-06 | - |
| RSP0222 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L14 Gen 4 EM05-G | ThinkPad L14 Gen 4 | 2023-03-06 | - |
| RSP0226 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13 Gen 4 EM05-G | ThinkPad X13 Gen 4 | 2023-03-06 | - |
| RSP0223 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L15 Gen 4 EM05-G | ThinkPad L15 Gen 4 | 2023-03-06 | - |
| RSP0228 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad Z13 Gen 2 EM05-G | ThinkPad Z13 Gen 2 | 2023-03-06 | - |
| RSP0219 | Dell Inc | Precision 7680 | Precision 7680 | 2023-03-06 | - |
| RSP0218 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L13 Gen 4 EM05-G | ThinkPad L13 Gen 4 | 2023-03-02 | - |
| RSP0217 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14 Gen 4 EM05 | ThinkPad T14 Gen 4 | 2023-03-02 | - |
| RSP0216 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13 Gen 4 FM350 | ThinkPad X13 Gen 4 | 2023-02-28 | - |
| RSP0214 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Yoga Gen 8 FM350 | ThinkPad X1 Yoga Gen 8 | 2023-02-28 | - |
| RSP0213 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Carbon Gen 11 FM350 | ThinkPad X1 Carbon Gen 11 | 2023-02-28 | - |
| RSP0215 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14s Gen 4 FM350 | ThinkPad T14s Gen 4 | 2023-02-28 | - |
| RSP0212 | Lenovo Mobile Communication Technology Co Ltd | 500e Chromebook Gen 4 (FM101) | 500e Chromebook Gen 4 | 2023-02-27 | - |
| RSP0211 | Lenovo Mobile Communication Technology Co Ltd | Lenovo 300w Yoga Gen 4 (FM101) | Lenovo 300w Yoga Gen 4 | 2023-02-27 | - |
| RSP0251 | Dell Inc | Latitude 5340 5G 2-in-1 | Latitude 5340 | 2023-02-22 | - |
| RSP0254 | Dell Inc | Latitude 5440 5G | Latitude 5440 | 2023-02-22 | - |
| RSP0257 | Dell Inc | Precision 3480 5G | Precision 3480 | 2023-02-22 | - |
| RSP0262 | Dell Inc | Latitude 7340 5G | Latitude 7340 | 2023-02-22 | - |
| RSP0252 | Dell Inc | Latitude 5340 5G | Latitude 5340 | 2023-02-22 | - |
| RSP0266 | Dell Inc | Latitude 7440 5G | Latitude 7440 | 2023-02-21 | - |
| RSP0268 | Dell Inc | Latitude 7640 5G | Latitude 7640 | 2023-02-21 | - |
| RSP0265 | Dell Inc | Latitude 7440 5G 2-in-1 | Latitude 7440 | 2023-02-20 | - |
| RSP0209 | Dell Inc | Latitude 5430 Chrome Enterprise | Latitude 5430 CE | 2023-01-17 | - |
| RSP0208 | Lenovo Mobile Communication Technology Co Ltd | Lenovo 100e Chromebook Gen 4 | Lenovo 100e Chromebook Gen 4 | 2022-12-14 | - |
| RSP0207 | Kyocera Corporation | KY-41C | KY-41C | 2022-12-02 | - |
| RSP0206 | Dell Inc | Latitude 3140 | Latitude 3140 | 2022-11-28 | - |
| RSP0201 | Lenovo Mobile Communication Technology Co Ltd | d-52C | d-52C | 2022-10-20 | - |
| RSP0200 | vivo Mobile Communication Co., Ltd. | V2219 | V2219 | 2022-10-14 | - |
| RSP0199 | Sharp Corporation | d-51C | dtab d-51C | 2022-10-06 | - |
| RSP0203 | Dell Inc | Latitude 7230 Rugged Extreme Tablet 5G | Latitude 7230 Rugged Extreme Tablet | 2022-09-29 | - |
| RSP0202 | Dell Inc | Latitude 7230 Rugged Extreme Tablet | Latitude 7230 Rugged Extreme Tablet | 2022-09-29 | - |
| RSP0197 | Lenovo Mobile Communication Technology Co Ltd | HB286ZJ | HB286ZJ | 2022-09-06 | - |
| RSP0198 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Fold 16 Gen 1 FM350 | ThinkPad X1 Fold 16 Gen 1 | 2022-09-06 | - |
| RSP0195 | Dell Inc | Latitude 3430 | Latitude 3430 | 2022-08-04 | - |
| RSP0196 | Dell Inc | Latitude 3530 | Latitude 3530 | 2022-08-04 | - |
| RSP0194 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P15v Gen 3 L860-GL | ThinkPad P15v Gen 3 | 2022-06-23 | - |
| RSP0193 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T15p Gen 3 L860-GL | ThinkPad T15p Gen 3 | 2022-06-22 | - |
| RSP0185 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L14 Gen 3 L860-GL | ThinkPad L14 Gen 3 | 2022-06-15 | - |
| RSP0191 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad Z16 Gen 1 L860-GL | ThinkPad Z16 Gen 1 | 2022-06-15 | - |
| RSP0184 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13 Yoga Gen 3 L860-GL | ThinkPad X13 Yoga Gen 3 | 2022-06-15 | - |
| RSP0192 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Nano Gen 2 L860-GL | ThinkPad X1 Nano Gen 2 | 2022-06-15 | - |
| RSP0188 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L13 Yoga Gen 3 L860-GL | ThinkPad L13 Yoga Gen 3 | 2022-06-15 | - |
| RSP0190 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P16 Gen 1 L860-GL | ThinkPad P16 Gen 1 | 2022-06-15 | - |
| RSP0187 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L13 Gen 3 L860-GL | ThinkPad L13 Gen 3 | 2022-06-15 | - |
| RSP0186 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L15 Gen 3 L860-GL | ThinkPad L15 Gen 3 | 2022-06-15 | - |
| RSP0189 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad Z13 Gen 1 L860-GL | ThinkPad Z13 Gen 1 | 2022-06-15 | - |
| RSP0178 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P16s Gen 1 EM05-G | ThinkPad P16s Gen 1 | 2022-06-13 | - |
| RSP0182 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P14s Gen 3 L860-GL | ThinkPad P14s Gen 3 | 2022-06-13 | - |
| RSP0181 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Yoga Gen 7 L860-GL | ThinkPad X1 Yoga Gen 7 | 2022-06-13 | - |
| RSP0179 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P1 Gen 5 5G FM350 | ThinkPad P1 Gen 5 | 2022-06-13 | - |
| RSP0180 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14s Gen 3 EM05 | ThinkPad T14s Gen 3 | 2022-06-13 | - |
| RSP0183 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P16s Gen 1 L860-GL | ThinkPad P16s Gen 1 | 2022-06-13 | - |
| RSP0176 | Dell Inc | Latitude 9330 | Latitude 9330 | 2022-05-05 | - |
| RSP0177 | Dell Inc | Latitude 9330 5G | Latitude 9330 | 2022-05-04 | - |
| RSP0174 | Dell Inc | Latitude 9430 | Latitude 9430 | 2022-04-22 | - |
| RSP0175 | Dell Inc | Latitude 9430 5G | Latitude 9430 | 2022-04-22 | - |
| RSP0172 | Dell Inc | Latitude 5531 5G | Latitude 5531 | 2022-04-11 | - |
| RSP0173 | Dell Inc | Precision 3571 5G | Precision 3571 | 2022-04-11 | - |
| RSP0158 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P14s Gen 3 EM05 | ThinkPad P14s Gen 3 | 2022-04-06 | - |
| RSP0162 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L13 Gen 3 EM05 | ThinkPad L13 Gen 3 | 2022-04-06 | - |
| RSP0161 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L13 Yoga Gen 3 EM05 | ThinkPad L13 Yoga Gen 3 | 2022-04-06 | - |
| RSP0159 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L15 Gen 3 EM05 | ThinkPad L15 Gen 3 | 2022-04-06 | - |
| RSP0164 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad Z16 Gen 1 EM05 | ThinkPad Z16 Gen 1 | 2022-04-06 | - |
| RSP0157 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T16 Gen 1 EM05 | ThinkPad T16 Gen 1 | 2022-04-06 | - |
| RSP0160 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad L14 Gen 3 EM05 | ThinkPad L14 Gen 3 | 2022-04-06 | - |
| RSP0163 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad Z13 Gen 1 EM05 | ThinkPad Z13 Gen 1 | 2022-04-06 | - |
| RSP0155 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13 Yoga Gen 3 EM05 | ThinkPad X13 Yoga Gen 3 | 2022-04-05 | - |
| RSP0156 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13 Gen 3 EM05 | ThinkPad X13 Gen 3 | 2022-04-05 | - |
| RSP0165 | Dell Inc | Latitude 7330 | Latitude 7330 | 2022-03-31 | - |
| RSP0169 | Dell Inc | Latitude 7430C9 | Latitude 7430 | 2022-03-31 | - |
| RSP0171 | Dell Inc | Latitude 7430 5G | Latitude 7430 | 2022-03-31 | - |
| RSP0168 | Dell Inc | Latitude 7330C9 | Latitude 7330 | 2022-03-31 | - |
| RSP0167 | Dell Inc | Latitude 7530 | Latitude 7530 | 2022-03-31 | - |
| RSP0154 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14 Gen 3 EM05 | ThinkPad T14 Gen 3 | 2022-03-31 | - |
| RSP0166 | Dell Inc | Latitude 7430 | Latitude 7430 | 2022-03-31 | - |
| RSP0170 | Dell Inc | Latitude 7530C9 | Latitude 7530 | 2022-03-31 | - |
| RSP0150 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14s Gen 3 FM350 | ThinkPad T14s Gen 3 | 2022-03-30 | - |
| RSP0148 | Lenovo Mobile Communication Technology Co Ltd | Lenovo 13W Yoga L860-GL | Lenovo 13W Yoga | 2022-03-30 | - |
| RSP0152 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Yoga Gen 7 FM350 | ThinkPad X1 Yoga Gen 7 | 2022-03-30 | - |
| RSP0147 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13 Gen 3 L860-GL | ThinkPad X13 Gen 3 | 2022-03-30 | - |
| RSP0151 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Extreme Gen 5 FM350 | ThinkPad X1 Extreme Gen 5 | 2022-03-30 | - |
| RSP0144 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14s Gen 3 L860-GL | ThinkPad T14s Gen 3 | 2022-03-30 | - |
| RSP0143 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T14 Gen 3 L860-GL | ThinkPad T14 Gen 3 | 2022-03-30 | - |
| RSP0149 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Nano Gen 2 T99W175 | ThinkPad X1 Nano Gen 2 | 2022-03-30 | - |
| RSP0153 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13 Gen 3 FM350 | ThinkPad X13 Gen 3 | 2022-03-30 | - |
| RSP0146 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T16 Gen 1 L860-GL | ThinkPad T16 Gen 1 | 2022-03-30 | - |
| RSP0141 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Carbon Gen 10 (FM350 5G) | ThinkPad X1 Carbon Gen 10 | 2022-03-16 | - |
| RSP0142 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X13s Gen 1 ( T99W175 5G) | ThinkPad X13s Gen 1 | 2022-03-16 | - |
| RSP0140 | Dell Inc | Chromebook 3100 | Chromebook 3100 | 2022-03-07 | - |
| RSP0139 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Carbon Gen 10 (L860-GL) | ThinkPad X1 Carbon Gen 10 | 2022-02-23 | - |
| RSP0138 | Dell Inc | Chromebook 3110 | Chromebook 3110 | 2022-02-21 | - |
| RSP0137 | Fairphone B.V. | FP4 | Fairphone 4 5G | 2021-10-04 | 10100 |
| RSP0131 | Dell Inc | Latitude 7420 | Latitude 7420 | 2021-08-24 | - |
| RSP0135 | Dell Inc | Precision 7560 | Precision 7560 | 2021-08-24 | - |
| RSP0133 | Dell Inc | Latitude 9520 | Latitude 9520 | 2021-08-24 | - |
| RSP0132 | Dell Inc | Latitude 7520 | Latitude 7520 | 2021-08-24 | - |
| RSP0129 | Dell Inc | Latitude 7320 Detachable | Latitude 7320 Detachable | 2021-08-24 | - |
| RSP0136 | Dell Inc | Precision 7760 | Precision 7760 | 2021-08-24 | - |
| RSP0130 | Dell Inc | Latitude 7320 | Latitude 7320 | 2021-08-24 | - |
| RSP0134 | Dell Inc | Latitude 9520 5G | Latitude 9520 | 2021-08-24 | - |
| RSP0128 | Dell Inc | Latitude 7220 Rugged Extreme Tablet | Latitude 7220 Rugged Extreme Tablet | 2021-08-09 | - |
| RSP0124 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P15v Gen 2 EM120R-GL | ThinkPad P15v Gen 2 EM120R-GL | 2021-07-14 | - |
| RSP0122 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T15g Gen 2 EM160R-GL | ThinkPad T15g Gen 2 EM160R-GL | 2021-07-14 | - |
| RSP0121 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P15 Gen 2 EM160R-GL | ThinkPad P15 Gen 2 EM160R-GL | 2021-07-14 | - |
| RSP0123 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P17 Gen 2 EM160R-GL | ThinkPad P17 Gen 2 EM160R-GL | 2021-07-14 | - |
| RSP0125 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad T15p Gen 2 EM120R-GL | ThinkPad T15p Gen 2 EM120R-GL | 2021-07-14 | - |
| RSP0127 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad P1 Gen 4 Foxconn T99W175 | ThinkPad P1 Gen 4 Foxconn T99W175 | 2021-07-14 | - |
| RSP0126 | Lenovo Mobile Communication Technology Co Ltd | ThinkPad X1 Extreme Gen 4 Foxconn T99W175 | ThinkPad X1 Extreme Gen 4 Foxconn T99W175 | 2021-07-14 | - |
| RSP0120 | Dell Inc | Precision 3561 | Precision 3561 | 2021-06-04 | - |
| RSP0118 | Dell Inc | Latitude 5421 | Latitude 5421 | 2021-06-04 | - |
| RSP0119 | Dell Inc | Latitude 5521 | Latitude 5521 | 2021-06-04 | - |
| RSP0116 | Dell Inc | Latitude 9420 | Latitude 9420 | 2021-04-20 | - |
| RSP0117 | Dell Inc | Latitude 9420 2-in-1 | Latitude 9420 2-in-1 | 2021-04-20 | - |
| RSP0107 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad L15 Gen 2 (EM120R-GL) | Lenovo ThinkPad L15 Gen 2 | 2021-03-24 | - |
| RSP0106 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad L14 Gen 2 (EM120R-GL) | Lenovo ThinkPad L14 Gen 2 | 2021-03-24 | - |
| RSP0110 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Yoga Gen 6 (EM120R-GL) | Lenovo ThinkPad X1 Yoga Gen 6 | 2021-03-24 | - |
| RSP0101 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Carbon Gen 9 (EM120R-GL) | Lenovo ThinkPad X1 Carbon Gen 9 | 2021-03-24 | - |
| RSP0104 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T15 Gen 2 (EM120R-GL) | Lenovo ThinkPad T15 Gen 2 | 2021-03-24 | - |
| RSP0108 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T14s Gen 2 (EM120R-GL) | Lenovo ThinkPad T14s Gen 2 | 2021-03-24 | - |
| RSP0113 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T15 Gen 2 (EM160R-GL) | Lenovo ThinkPad T15 Gen 2 | 2021-03-24 | - |
| RSP0111 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T14 Gen 2 (EM160R-GL) | Lenovo ThinkPad T14 Gen 2 | 2021-03-24 | - |
| RSP0112 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad P14s Gen 2 (EM160R-GL) | Lenovo ThinkPad P14s Gen 2 | 2021-03-24 | - |
| RSP0102 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T14 Gen 2 (EM120R-GL) | Lenovo ThinkPad T14 Gen 2 | 2021-03-24 | - |
| RSP0105 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad P15s Gen 2 (EM120R-GL) | Lenovo ThinkPad P15s Gen 2 | 2021-03-24 | - |
| RSP0115 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X13 Yoga Gen 2 (EM120R-GL) | Lenovo ThinkPad X13 Yoga Gen 2 | 2021-03-24 | - |
| RSP0114 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad P15s Gen 2 (EM160R-GL) | Lenovo ThinkPad P15s Gen 2 | 2021-03-24 | - |
| RSP0109 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X13 Gen 2 (EM120R-GL) | Lenovo ThinkPad X13 Gen 2 | 2021-03-24 | - |
| RSP0103 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad P14s Gen 2 (EM120R-GL) | Lenovo ThinkPad P14s Gen 2 | 2021-03-24 | - |
| RSP0100 | WWZN Information Technology Company Ltd | WH11013 | TicWatch Pro 3 Cellular/LTE | 2021-03-08 | - |
| RSP0098 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T14s Gen 2 (T99W175) | Lenovo ThinkPad T14s Gen 2 | 2021-02-25 | - |
| RSP0099 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X13 Gen 2 (Foxconn T99W175) | Lenovo ThinkPad X13 Gen 2 | 2021-02-25 | - |
| RSP0095 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Titanium Gen 1 (T99W175) | Lenovo ThinkPad X1 Titanium Gen 1 | 2021-02-04 | - |
| RSP0093 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Nano Gen 1 (T99W175) | Lenovo ThinkPad X1 Nano Gen 1 | 2021-02-04 | - |
| RSP0096 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Carbon Gen 9 (T99W175) | Lenovo ThinkPad X1 Carbon Gen 9 | 2021-02-04 | - |
| RSP0097 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Yoga Gen 6 (T99W175) | Lenovo ThinkPad X1 Yoga Gen 6 | 2021-02-04 | - |
| RSP0094 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Fold Gen 1 (T99W175) | Lenovo ThinkPad X1 Fold Gen 1 | 2021-02-04 | - |
| RSP0087 | Dell Inc | Latitude 5320 | Latitude 5320 | 2020-12-15 | - |
| RSP0091 | Dell Inc | Precision 3560 | Precision 3560 | 2020-12-15 | - |
| RSP0090 | Dell Inc | Latitude 5520 | Latitude 5520 | 2020-12-15 | - |
| RSP0089 | Dell Inc | Latitude 5420 | Latitude 5420 | 2020-12-15 | - |
| RSP0088 | Dell Inc | Latitude 5320 2-in-1 | Latitude 5320 | 2020-12-15 | - |
| RSP0086 | Lenovo Mobile Communication Technology Co Ltd | d-42A | d-42A | 2020-11-11 | - |
| RSP0085 | Lenovo Mobile Communication Technology Co Ltd | ATHENA20L | ATHENA20L | 2020-11-03 | - |
| RSP0084 | JVCKENWOOD (RSP) | DDR01 | DDR01 | 2020-10-21 | - |
| RSP0054 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T15 (Fibocom L860-GL) | Lenovo ThinkPad T15 | 2020-08-10 | - |
| RSP0069 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T14 AMD (Fibocom L850-GL) | Lenovo ThinkPad T14 AMD | 2020-08-10 | - |
| RSP0049 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad P14s (Fibocom L860-GL) | Lenovo ThinkPad P14s | 2020-08-10 | - |
| RSP0081 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X13 AMD (Fibocom L850-GL) | Lenovo ThinkPad X13 AMD | 2020-08-10 | - |
| RSP0048 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad P1 (Fibocom L860-GL) | Lenovo ThinkPad P1 | 2020-08-10 | - |
| RSP0067 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad L15 (Fibocom L850-GL) | Lenovo ThinkPad L15 | 2020-08-10 | - |
| RSP0074 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Carbon 8th Gen(Fibocom L850-GL) | Lenovo ThinkPad X1 Carbon 8th Gen | 2020-08-10 | - |
| RSP0077 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Yoga 5th Gen (Fibocom L850-GL) | Lenovo ThinkPad X1 Yoga 5th Gen | 2020-08-10 | - |
| RSP0073 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T15p (Fibocom L850-GL) | Lenovo ThinkPad T15p | 2020-08-10 | - |
| RSP0070 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T14s AMD (Fibocom L850-GL) | Lenovo ThinkPad T14s AMD | 2020-08-10 | - |
| RSP0083 | Lenovo Mobile Communication Technology Co Ltd | Lenovo IdeaPad Duet 7 (Fibocom L850-GL) | Lenovo IdeaPad Duet 7 | 2020-08-10 | - |
| RSP0063 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad P15s (Fibocom L850-GL) | Lenovo ThinkPad P15s | 2020-08-10 | - |
| RSP0075 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Nano (Fibocom L850-GL) | Lenovo ThinkPad X1 Nano | 2020-08-10 | - |
| RSP0068 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad P15v (Fibocom L850-GL) | Lenovo ThinkPad P15v | 2020-08-10 | - |
| RSP0062 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad P14s (Fibocom L850-GL) | Lenovo ThinkPad P14s | 2020-08-10 | - |
| RSP0052 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad P17 (Fibocom L860-GL) | Lenovo ThinkPad P17 | 2020-08-10 | - |
| RSP0080 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X13 Yoga (Fibocom L850-GL) | Lenovo ThinkPad X13 Yoga | 2020-08-10 | - |
| RSP0072 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T15 (Fibocom L850-GL) | Lenovo ThinkPad T15 | 2020-08-10 | - |
| RSP0066 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad L15 AMD (Fibocom L850-GL) | Lenovo ThinkPad L15 AMD | 2020-08-10 | - |
| RSP0053 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T14s (Fibocom L860-GL) | Lenovo ThinkPad T14s | 2020-08-10 | - |
| RSP0079 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X13 (Fibocom L850-GL) | Lenovo ThinkPad X13 | 2020-08-10 | - |
| RSP0060 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X13 Yoga (Fibocom L860-GL) | Lenovo ThinkPad X13 Yoga | 2020-08-10 | - |
| RSP0078 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X12 Detachable (Fibocom L850-GL) | Lenovo ThinkPad X12 Detachable | 2020-08-10 | - |
| RSP0051 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad P15s (Fibocom L860-GL) | Lenovo ThinkPad P15s | 2020-08-10 | - |
| RSP0064 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad L14 AMD (Fibocom L850-GL) | Lenovo ThinkPad L14 AMD | 2020-08-10 | - |
| RSP0047 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T14 (Fibocom L860-GL) | Lenovo ThinkPad T14 | 2020-08-10 | - |
| RSP0057 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Extreme (Fibocom L860-GL) | Lenovo ThinkPad X1 Extreme | 2020-08-10 | - |
| RSP0076 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Titanium (Fibocom L850-GL) | Lenovo ThinkPad X1 Titanium | 2020-08-10 | - |
| RSP0082 | Lenovo Mobile Communication Technology Co Ltd | Lenovo IdeaPad Duet 3 (Fibocom L850-GL) | Lenovo IdeaPad Duet 3 | 2020-08-10 | - |
| RSP0055 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T15g (Fibocom L860-GL) | Lenovo ThinkPad T15g | 2020-08-10 | - |
| RSP0058 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Yoga 5th Gen (Fibocom L860-GL) | Lenovo ThinkPad X1 Yoga 5th Gen | 2020-08-10 | - |
| RSP0071 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T14s (Fibocom L850-GL) | Lenovo ThinkPad T14s | 2020-08-10 | - |
| RSP0065 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad L14 (Fibocom L850-GL) | Lenovo ThinkPad L14 | 2020-08-10 | - |
| RSP0056 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Carbon 8th Gen(Fibocom L860-GL) | Lenovo ThinkPad X1 Carbon 8th Gen | 2020-08-10 | - |
| RSP0061 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T14 (Fibocom L850-GL) | Lenovo ThinkPad T14 | 2020-08-10 | - |
| RSP0059 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X13 (Fibocom L860-GL) | Lenovo ThinkPad X13 | 2020-08-10 | - |
| RSP0050 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad P15 (Fibocom L860-GL) | Lenovo ThinkPad P15 | 2020-08-10 | - |
| RSP0046 | Dell Inc | Latitude 9510 5G | Latitude 9510 | 2020-07-15 | - |
| RSP0045 | Dell Inc | Latitude 7410 | Latitude 7410 | 2020-04-10 | - |
| RSP0044 | Dell Inc | Latitude 7310 | Latitude 7310 | 2020-04-09 | - |
| RSP0043 | Dell Inc | Latitude 5310 2-in-1 | Latitude 5310 2-in-1 | 2020-03-27 | - |
| RSP0041 | Dell Inc | Latitude 3510 | Latitude 3510 | 2020-03-27 | - |
| RSP0042 | Dell Inc | Latitude 5310 | Latitude 5310 | 2020-03-27 | - |
| RSP0040 | Dell Inc | Latitude 9510 | Latitude 9510 | 2020-03-25 | - |
| RSP0032 | WWZN Information Technology Company Ltd | WF11018 | TicWatch Pro 4G LTE Smart Watch | 2020-03-19 | - |
| RSP0033 | Dell Inc | Latitude 7210 2-in-1 | Latitude 7210 2-in-1 | 2020-03-11 | - |
| RSP0038 | Dell Inc | Latitude 5511 | Latitude 5511 | 2020-03-02 | - |
| RSP0039 | Dell Inc | Precision 3551 | Precision 3551 | 2020-03-02 | - |
| RSP0037 | Dell Inc | Latitude 5411 | Latitude 5411 | 2020-02-28 | - |
| RSP0036 | Dell Inc | Latitude 9410 | Latitude 9410 | 2020-01-31 | - |
| RSP0035 | Dell Inc | Latitude 5510 | Latitude 5510 | 2020-01-20 | - |
| RSP0034 | Dell Inc | Latitude 5410 | Latitude 5410 | 2020-01-20 | - |
| RSP0027 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad L590 (Fibocom L830-EB) | Lenovo ThinkPad L590 | 2020-01-10 | - |
| RSP0031 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X390 Yoga (Fibocom L830-EB) | Lenovo ThinkPad X390 Yoga | 2020-01-10 | - |
| RSP0030 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X390 (Fibocom L830-EB) | Lenovo ThinkPad X390 | 2020-01-10 | - |
| RSP0028 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad P53s (Fibocom L830-EB) | Lenovo ThinkPad P53s | 2020-01-10 | - |
| RSP0029 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T590 (Fibocom L830-EB) | Lenovo ThinkPad T590 | 2020-01-10 | - |
| RSP0025 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T490 (Fibocom L830-EB) | Lenovo ThinkPad T490 | 2020-01-10 | - |
| RSP0026 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T490s (Fibocom L830-EB) | Lenovo ThinkPad T490s | 2020-01-10 | - |
| RSP0010 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Yoga 4th Gen (Fibocom L860-GL) | Lenovo ThinkPad X1 Yoga 4th Gen | 2019-12-02 | - |
| RSP0012 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad L490 (Fibocom L850-GL) | Lenovo ThinkPad L490 | 2019-12-02 | - |
| RSP0006 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T490 (Fibocom L860-GL) | Lenovo ThinkPad T490 | 2019-12-02 | - |
| RSP0017 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T495 (Fibocom L850-GL) | Lenovo ThinkPad T495 | 2019-12-02 | - |
| RSP0007 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T490 (Fibocom L850-GL) | Lenovo ThinkPad T490 | 2019-12-02 | - |
| RSP0013 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad L590 (Fibocom L850-GL) | Lenovo ThinkPad L590 | 2019-12-02 | - |
| RSP0024 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Carbon 7th Gen(Fibocom L860-GL) | Lenovo ThinkPad X1 Carbon 7th Gen | 2019-12-02 | - |
| RSP0022 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X390 Yoga (Fibocom L850-GL) | Lenovo ThinkPad X390 Yoga | 2019-12-02 | - |
| RSP0016 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T490s (Fibocom L850-GL) | Lenovo ThinkPad T490s | 2019-12-02 | - |
| RSP0015 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad P53s (Fibocom L850-GL) | Lenovo ThinkPad P53s | 2019-12-02 | - |
| RSP0020 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Carbon 7th Gen(Fibocom L850-GL) | Lenovo ThinkPad X1 Carbon 7th Gen | 2019-12-02 | - |
| RSP0018 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T495s (Fibocom L850-GL) | Lenovo ThinkPad T495s | 2019-12-02 | - |
| RSP0021 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X390 (Fibocom L850-GL) | Lenovo ThinkPad X390 | 2019-12-02 | - |
| RSP0008 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X1 Yoga 4th Gen (Fibocom L850-GL) | Lenovo ThinkPad X1 Yoga 4th Gen | 2019-12-02 | - |
| RSP0019 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad T590 (Fibocom L850-GL) | Lenovo ThinkPad T590 | 2019-12-02 | - |
| RSP0023 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad X395 (Fibocom L850-GL) | Lenovo ThinkPad X395 | 2019-12-02 | - |
| RSP0014 | Lenovo Mobile Communication Technology Co Ltd | Lenovo ThinkPad P53 (Fibocom L850-GL) | Lenovo ThinkPad P53 | 2019-12-02 | - |
| RSP0003 | Sharp Corporation | SH-03M | SH-03M | 2019-11-06 | - |
| RSP0002 | Dell Inc | Inspiron 7490 | Inspiron 7490 | 2019-08-22 | - |
| RSP0001 | Dell Inc | Inspiron 5390 | Inspiron 5390 | 2019-05-16 | - |

*Generated by `scripts/build-gcf-rsp.py`. Do not edit by hand.*
