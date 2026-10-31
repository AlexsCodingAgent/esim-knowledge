---
layout: default
title: "Tag Database, Condensed (machine-readable)"
description: "One row per TLV tag across eSIM RSP, ETSI TS 101 220, GlobalPlatform, 3GPP USAT and SIM EF file IDs, with the scope key that disambiguates the value, plus the document and clause. For programmatic or LLM extraction."
---

# Tag Database, Condensed

One row per reading. Columns: **Tag**, **Name**, **Scope**, **Namespace**,
**Key**, **Document**, **Clause**.

The **Scope** column is load-bearing. A tag value alone does not identify an
object: `83` is a file identifier in one template and a key reference in another,
`6F07` is IMSI under one ADF and a service table under another. Resolve the scope
first, then the name.

Prefer this page over the prose version for programmatic or LLM extraction.

[Full database with search, grouping and namespace filter]({{ site.baseurl }}/docs/tag-database)

| Namespace | Key | Readings | Distinct values |
|---|---|---|---|
| eSIM RSP ASN.1 | `(module, tag)` | 288 | 111 |
| ETSI TS 101 220 allocator | `(type, context, tag)` | 230 | 171 |
| GlobalPlatform BER-TLV | `(document, tag)` | 537 | 148 |
| 3GPP / ETSI card-layer | `(document, clause, tag)` | 33 | 27 |
| 3GPP USAT (TS 31.111) | `(tag, section)` | 39 | 38 |
| SIM EF / FID file IDs | `(ADF, FID)` | 140 | 124 |

| Tag | Name | Scope | Namespace | Key | Document | Clause |
|---|---|---|---|---|---|---|
| `0010` | Key Modulus | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0010` | Key Modulus | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0010` | Key Modulus | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0011` | Public Key Exponent | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0011` | Public Key Exponent | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0011` | Public Key Exponent | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0030` | P (field specification) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0030` | P (field specification) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0030` | P (field specification) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2.2 |
| `0031` | A (first coefficient) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0031` | A (first coefficient) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0031` | A (first coefficient) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2.2 |
| `0032` | B (second coefficient) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0032` | B (second coefficient) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0032` | B (second coefficient) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2.2 |
| `0033` | G (generator) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0033` | G (generator) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0033` | G (generator) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2.2 |
| `0034` | N (order of generator) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0034` | N (order of generator) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0034` | N (order of generator) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2.2 |
| `0035` | k (cofactor of order of generator) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0035` | k (cofactor of order of generator) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0035` | k (cofactor of order of generator) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2.2 |
| `0036` | Q (public key) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0036` | Q (public key) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `0036` | Q (public key) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2.2 |
| `00A6` | Control Reference Key agreement/generation CRT No Template (KAT) | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.5.1 |
| `00B8` | Control Reference Template for Application Provider Key No confidentiality (CT) information data | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.4.2 |
| `00B9` | Key Information Data | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4 |
| `00B9` | Key Information Data | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4 |
| `00B9` | Key Information Data | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4 |
| `00DE` | Certificate with Message Application Provider Public Key No Recovery Certificate | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.4.1 |
| `01` | reserved for OMA SCWS [25] | Remote Management Application Data templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `01` | Command details tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `02` | Device identity tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `02` | r component of the signature | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.11.4 |
| `03` | UICCCapability | TCA Interop v3.4 | eSIM RSP ASN.1 | `(module, tag)` | TCA Interop v3.4 | 8.2.7 |
| `03` | Result tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `04` | Duration tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `05` | Alpha identifier tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `06` | Address tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `06` | '2B 06 01 04 01 2A 02 6E 01 02' Java Card 2.2.x | GPC_SE_Configuration-v2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.2.2 |
| `06` | '2A 8648 86FC6B 05' + CASD Capability Information | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.1 |
| `06` | '2B 06 01 04 01 2A 02 6E 01 02' Java Card 2.2.x | GPC_UICC_Configuration-v2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.2.1 |
| `07` | Capability configuration parameters tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `08` | Subaddress tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `09` | Reserved for 3GPP (SS string tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `09` | SS string tag BSSID tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `09` | PLMN ID tag E-UTRAN/Satellite E-UTRAN Timing Advance tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `0A` | Reserved for 3GPP/3GPP2 (USSD string tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `0A` | USSD string tag HESSID tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `0B` | Reserved for 3GPP (SMS TPDU tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `0B` | SMS TPDU tag PDP/PDN/PDU type tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `0C` | Reserved for 3GPP (Cell Broadcast page tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `0C` | Cell Broadcast page tag PDU session establishment parameters tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `0D` | Text string tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `0E` | Tone tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `0F` | Item tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `10` | Item identifier tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `11` | Response length tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `12` | File List tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `13` | Location Information tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `14` | IMEI tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `15` | Help request tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `16` | Network Measurement Results tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `17` | Default Text tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `18` | Items Next Action Indicator tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `19` | Event list tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `1A` | Reserved for 3GPP (Cause tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `1A` | Cause tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `1B` | Location status tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `1C` | Transaction identifier tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `1D` | Reserved for 3GPP (BCCH channel list tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `1D` | BCCH channel list tag Data connection status tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `1E` | Icon identifier tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `1F` | Item Icon identifier list tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `20` | Card reader status tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `21` | Card ATR tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `22` | C-APDU tag (see note) | Command Scripting template ('AA' or 'AE') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `22` | C-APDU tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `23` | R-APDU tag (see note) | Response Scripting template ('AB' or 'AF') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `23` | R-APDU tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `24` | Timer identifier tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `25` | Timer value tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `26` | Date-Time and Time zone tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `27` | Call control requested action tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `28` | AT Command tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `29` | AT Response tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `2A` | Reserved for 3GPP (BC Repeat Indicator tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `2A` | BC Repeat Indicator tag Data connection type tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `2B` | Immediate response tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `2C` | DTMF string tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `2D` | Language tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `2E` | Reserved for 3GPP (Timing Advance tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `2E` | Timing Advance tag (E/5G)SM cause tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `2F` | AID tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `2F00` | List of Applications associated with the Security Domain, or every application on | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `2F00` | List of Applications associated with the Security Domain, or every application on | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `2F00` | List of Applications associated with the Security Domain, or every application on | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.2.3 |
| `30` | Browser Identity tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `30` | Signature Tag Length Value Description | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.11.4 |
| `31` | Card Service Data | ATR data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `31` | URL tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `31` | IMS URI tag Rejected slices information tag NG-RAN/Satellite NG-RAN Primary Timing Advance tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `32` | Bearer tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `33` | Provisioning Reference File tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `34` | Browser Termination Cause tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `35` | Bearer description tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `36` | Channel data tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `37` | Channel data length tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `38` | Channel status tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `39` | Buffer size tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `3A` | Card reader identifier tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `3B` | File Update Information tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `3C` | UICC/terminal interface transport level tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `3E` | Other address (data destination address) tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `3F` | Access Technology tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `40` | Display parameters tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `41` | Service Record tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `42` | Device Filter tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `42` | CA Identifier | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.2 |
| `42` | Token Issuer Id | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `42` | Identification Number of the Security Domain with the Token Verification privilege | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `42` | Identification Number of the Security Domain with the Token Verification privilege | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `42` | Identification Number of the Security Domain with the Token Verification privilege | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `42` | Identification Number of the Security Domain with the Token Verification privilege | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `42` | CA Identifier M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.1 |
| `42` | Issuer IIN: 8 bytes: leftmost 8 bytes of the Identification subjectKeyIdentifier of the CVC signer X.509 Number certifi… | GPC_SPE_106-Amendment-G-Opacity-Secure-Channel-v1.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.2.4 |
| `42` | Identification Number of the SD with Token Verification privilege | GPC_SPE_120-Amendment-H-Executable-Load-File-Upgrade-v1.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.1.2.3 |
| `42` | CA-SEMS Identifier | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.5.2 |
| `42` | CA Identifier | GPC_UICC_Configuration-v1.0.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 9.2.1 |
| `43` | Service Search tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `43` | Tag that has been executed by the SEMS Application. It | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 5.2 |
| `44` | Attribute information tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `44` | SW as defined in Table 6-8 | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.2.6.1 |
| `45` | Service Availability tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `45` | Security Domain Image Number (SDIN) | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.5.1 |
| `45` | Card Image Number | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `45` | Image number of the Security Domain with the Token Verification privilege | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `45` | Image number of the Security Domain with the Token Verification privilege | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `45` | Image number of the Security Domain with the Token Verification privilege | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `45` | Image number of the Security Domain with the Token Verification privilege | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `45` | Image number of the SD with Token Verification privilege | GPC_SPE_120-Amendment-H-Executable-Load-File-Upgrade-v1.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.1.2.3 |
| `45` | CA-SEMS signature verification key identifier | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.5.2 |
| `45` | CA Security Domain Image Number | GPC_UICC_Configuration-v1.0.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 9.2.1 |
| `46` | Reserved for 3GPP2 (3GPP2 tag 1) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `46` | '00': The script has been completely executed | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.1.5.1 |
| `47` | Network Access Name tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `48` | Reserved for 3GPP2 (3GPP2 tag 2) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `48` | Reason code describing why the activation failed | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11.4.3.1 |
| `48` | CCM rights (see Table 4-4) | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.5.2 |
| `49` | Remote Entity Address tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `4A` | Reserved for 3GPP (I-WLAN Identifier tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `4A` | I-WLAN Identifier tag SSID tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `4B` | Reserved for 3GPP ((I-)WLAN Access Status tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `4B` | (I-)WLAN Access Status tag More Data tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `4C` | SEMS Privileges (See Table 4-5) | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.5.2 |
| `4F` | Application Identifier (AID) | Application template ('61') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `4F` | AID of the application that could not be activated due to a conflict in protocol parameters, application policy, or pri… | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11.4.3.1 |
| `4F` | Executable Load File or Application AID | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `4F` | Executable Load File or Application AID | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `4F` | Executable Load File or Application AID | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `4F` | Executable Load File or Application AID | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `4F` | AID of Executable Load File or Application or Security Domain | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `4F` | AID of old ELF version (i.e. the one being upgraded) | GPC_SPE_120-Amendment-H-Executable-Load-File-Upgrade-v1.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.1.2.3 |
| `50` | Application Label | Application template ('61') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `50` | Text attribute tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `51` | Path | Application template ('61') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `51` | Item text attribute list tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `52` | Command to Perform | Application template ('61') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `52` | Reserved for 3GPP (PDP context Activation | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `52` | PDP context Activation parameters tag Surrounding macrocells tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `53` | Discretionary Data | Application template ('61') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `53` | Contactless state request tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `53` | Discretionary Data (unspecified format) | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.2 |
| `53` | Discretionary Data | GPC_UICC_Configuration-v1.0.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 9.2.1 |
| `54` | Contactless functionality state tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `55` | Reserved for 3GPP (CSG cell selection status tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `55` | CSG cell selection status tag IMS call disconnection cause tag CAG cell selection status tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `56` | Reserved for 3GPP (CSG ID tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `56` | CSG ID tag Slices information tag CAG information list tag E-UTRAN Tracking Area | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `57` | Reserved for 3GPP (HNB name tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `57` | HNB name tag Extended rejection cause code tag CAG Human-readable network name list tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `5A` | EuiccPackageSigned | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `5A` | EuiccPackageSigned | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.1.1 |
| `5C` | IpaEuiccDataRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `5C` | IpaEuiccDataRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.1.2 |
| `5C` | Tag list | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11.3.2.3 |
| `5C` | Tag list | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.2.3 |
| `5C` | Tag list | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.2.3 |
| `5C` | Tag list | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.2.3 |
| `5C` | Tag list | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.2.3 |
| `5C` | Tag list | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.2.3 |
| `5F20` | Subject Identifier | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.2 |
| `5F20` | Application Provider identifier | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `5F20` | Application Provider identifier | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `5F20` | Application Provider identifier | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `5F20` | Application Provider identifier | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `5F20` | Application Provider Identifier used only in token verification | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `5F20` | Subject Identifier M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.1 |
| `5F20` | Application Provider identifier | GPC_SPE_120-Amendment-H-Executable-Load-File-Upgrade-v1.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.1.2.3 |
| `5F20` | Subject identifier (a.k.a. certificate holder) | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.5.2 |
| `5F20` | Subject Identifier | GPC_UICC_Configuration-v1.0.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 9.2.1 |
| `5F24` | Expiration Date (YYYYMMDD, BCD format) | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.2 |
| `5F24` | Expiration Date (YYYYMMDD, BCD format) M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.1 |
| `5F24` | Expiration Date of CA(YYYYMMDD, BCD format) | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.5.3 |
| `5F24` | Expiration Date (YYYYMMDD, BCD format) | GPC_UICC_Configuration-v1.0.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 9.2.1 |
| `5F25` | Effective Date (YYYYMMDD, BCD format) | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.2 |
| `5F25` | Effective Date (YYYYMMDD, BCD format) C | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.1 |
| `5F25` | Effective Date (YYYYMMDD, BCD format) | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.5.2 |
| `5F25` | Effective Date (YYYYMMDD, BCD format) | GPC_UICC_Configuration-v1.0.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 9.2.1 |
| `5F29` | Credential '80' Profile Identifier | GPC_SPE_106-Amendment-G-Opacity-Secure-Channel-v1.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.2.4 |
| `5F37` | ProfileInstallationResultData | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 2.5.6 |
| `5F37` | ProfileInstallationResultData | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 2.5.6 |
| `5F37` | ProfileInstallationResultData | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 2.5.6 |
| `5F37` | EuiccPackageRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `5F37` | EuiccPackageRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.1.1 |
| `5F37` | Signature | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.2 |
| `5F37` | Signature M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.1 |
| `5F37` | Signature: Concatenation of r and s component (r // s) | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.5.2 |
| `5F38` | Public Key Modulus Remainder | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.2 |
| `5F45` | Platform_Label | GPC_SPE_095-Digital-Letter-of-Approval | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.1 |
| `5F49` | ePK.OCE.ECKA M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.7.2.3 |
| `5F4C` | Role Identifier Indicates the type of certificate | GPC_SPE_106-Amendment-G-Opacity-Secure-Channel-v1.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.2.4 |
| `5F50` | Uniform Resource Locator (URL) | Application template ('61') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `5F50` | Security Domain Manager URL | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `5F50` | Security Domain Manager URL | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `5F50` | Security Domain Manager URL | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `5F50` | Discovery Base URL of the SE default DLOA Registrar | GPC_SPE_095-Digital-Letter-of-Approval | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.1 |
| `60` | MAC tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `60` | Card Management Type and Version – | GPC_SE_Configuration-v2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.2.2 |
| `60` | SD Management Type & Version | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.1 |
| `60` | The OID {globalPlatform 2 v} identifies a card that conforms to the GlobalPlatform | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.3.2 |
| `60` | The OID {globalPlatform 2 v} identifies a card that conforms to the GlobalPlatform | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.3.2 |
| `60` | The OID {globalPlatform 2 v} identifies a card that conforms to the GlobalPlatform | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `60` | The OID {globalPlatform 2 v} identifies a card that conforms to the GlobalPlatform | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `60` | The OID {globalPlatform 2 v} identifies a card that conforms to the GlobalPlatform | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `60` | Card management type and version – | GPC_UICC_Configuration-v2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.4.1 |
| `61` | Application Template | Templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `61` | Reserved for 3GPP2 (3GPP2 Tag 3) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `61` | Application related data Tag Length Value Description | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11.3.3.1 |
| `61` | Application Template | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.3.1 |
| `61` | Application Template | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.3.1 |
| `61` | Application Template | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.3.1.3 |
| `61` | Application Template | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.3.1.3 |
| `61` | Application Template | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.3.1.4 |
| `61` | Response in event of Authentication Frame processing Tag Length Value Description | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.2.6.1 |
| `62` | FCP Template | Templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `62` | IMEISV tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `63` | Battery state tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `63` | Card Identification Scheme – | GPC_SE_Configuration-v2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.2.2 |
| `63` | SD Identification Scheme | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.1 |
| `63` | The OID {globalPlatform 3} indicates a GlobalPlatform card that is uniquely identi | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.3.2 |
| `63` | The OID {globalPlatform 3} indicates a GlobalPlatform card that is uniquely | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.3.2 |
| `63` | The OID {globalPlatform 3} indicates a GlobalPlatform card that is uniquely identi | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `63` | The OID {globalPlatform 3} indicates a GlobalPlatform card that is uniquely identi | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `63` | The OID {globalPlatform 3} indicates a GlobalPlatform card that is uniquely identi | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `63` | Card identification scheme – | GPC_UICC_Configuration-v2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.4.1 |
| `64` | Browsing status tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `64` | Secure Channel Protocol & Options supported by the ISD (format 1) | GPC_SE_Configuration-v2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.2.2 |
| `64` | SD Secure Channel Protocol & Options | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.1 |
| `64` | Secure Channel Protocol & Options supported by the ISD (format 1) | GPC_UICC_Configuration-v2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.2.1 |
| `65` | Network Search Mode tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `65` | Card Configuration Details (see Note 2) – | GPC_SE_Configuration-v2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.2.2 |
| `65` | SD Configuration Details | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.1 |
| `65` | This data object may contain information about the GlobalPlatform implementation d | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `65` | Identifier of the SEMS Application Key Set Identifier Tag Length Description | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.3.5.1 |
| `65` | Card Configuration Details (see Note 1) – | GPC_UICC_Configuration-v2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.2.1 |
| `66` | Frame Layout tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `66` | Card Data – | GPC_SE_Configuration-v2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.2.2 |
| `66` | Security Domain Data | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.1 |
| `66` | Card Data (or Security Domain Management Data) | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `66` | Card Data (or Security Domain Management Data) | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `66` | This data object may contain information about the card and chip implementation, s | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `66` | This data object may contain information about the card and chip implementation, s | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `66` | This data object may contain information about the card and chip implementation, s | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `66` | Security Domain Data – | GPC_UICC_Configuration-v2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.4.1 |
| `67` | Frames Information tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `67` | Card Capability Information | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `67` | Card Capability Information | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `67` | Card Capability Information | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `67` | Card Capability Information | GPC_SPE_120-Amendment-H-Executable-Load-File-Upgrade-v1.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.5 |
| `68` | Frame identifier tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `68` | This data object is related to the use of Secure Channel Protocol '10' and may con | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `68` | This data object is related to the use of Secure Channel Protocol '10' and may con | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `68` | This data object is related to the use of Secure Channel Protocol '10' and may con | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `69` | Reserved for 3GPP | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `69` | UTRAN/E-UTRAN/Satellite E-UTRAN /NG-RAN/Satellite NG-RAN Measurement Qualifier tag IP address list tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `6A` | Multimedia Message Reference tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `6B` | Multimedia Message Identifier tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `6C` | Multimedia Message Transfer Status tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `6D` | Reserved for 3GPP2 (3GPP2 tag 4) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `6D` | Application Image Template if available | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11.3.3.1 |
| `6E` | Multimedia Message Content Identifier tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `6F` | Multimedia Message Notification tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `6F` | FCI Template Tag Length Value Description | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11.5.2 |
| `6F` | File Control Information (FCI Template) | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.3.5.1 |
| `6F01` | enhanced AKA support | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F02` | Operator controlled signal threshold per access | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F02` | IMS private user identity | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6F03` | Home Network Domain Name | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6F04` | IMS public user identity | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6F05` | Language indication | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F06` | Access rule reference (under ADF_(USIM) and | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F06` | Access Rule Reference | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6F07` | IMSI | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F07` | ISIM Service Table | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6F08` | Ciphering and integrity keys | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F09` | Ciphering and integrity keys for packet switched | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F09` | P-CSCF address | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6F0A` | Access Control to GBA_U_API | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F0B` | IMS DC Establishment Indication | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F0C` | Operator-controlled-LSP-PLMN | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F0D` | PeriodicSearchTimerNonLSP | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F2C` | De-personalization Control Keys | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F31` | Higher Priority PLMN search period | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F32` | Co-operative network list | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F37` | ACM maximum value | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F38` | USIM service table | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F39` | Accumulated call meter | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F3B` | Fixed dialling numbers | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F3C` | Short messages | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F3C` | Short messages | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6F3E` | Group identifier level 1 | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F3F` | Group identifier level 2 | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F40` | MSISDN storage | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F41` | PUCT | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F42` | SMS parameters | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F42` | SMS parameters | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6F43` | SMS status | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F43` | SMS status | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6F45` | CBMI | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F46` | Service provider name | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F47` | Short message status reports | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F47` | Short message status reports | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6F48` | CBMID | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F49` | Service Dialling Numbers | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F4B` | Extension 2 | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F4C` | Extension 3 | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F4D` | Barred dialling numbers | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F4E` | Extension 5 | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F4F` | Capability configuration parameters 2 | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F50` | CBMIR | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F54` | SetUp Menu Elements | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F55` | Extension 4 | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F56` | Enabled services table | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F57` | Access point name control list | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F58` | Comparison method information | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F5B` | Initialisation value for Hyperframe number | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F5C` | Maximum value of hyperframe number | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F60` | User controlled PLMN selector with Access | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F61` | Operator controlled PLMN selector with Access | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F62` | HPLMN selector with Access Technology | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F73` | Packet switched location information | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F78` | Access control class | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F7B` | Forbidden PLMNs | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F7E` | Location information | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F80` | Incoming call information | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F81` | Outgoing call information | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F82` | Incoming call timer | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6F83` | Outgoing call timer | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FAD` | Administrative data | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FAD` | Administrative Data | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6FB1` | Voice Group Call Service | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FB2` | Voice Group Call Service Status | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FB3` | Voice Broadcast Service | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FB4` | Voice Broadcast Service Status | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FB5` | Enhanced Multi Level Pre-emption and | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FB6` | Automatic Answer for eMLPP Service | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FB7` | Emergency Call Codes | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FC3` | Key for hidden phone book entries | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FC4` | Network Parameters | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FC5` | PLMN Network Name | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FC6` | Operator Network List | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FC7` | Mailbox Dialling Numbers | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FC8` | Extension 6 | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FC9` | Mailbox Identifier | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FCA` | Message Waiting Indication Status | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FCB` | Call Forwarding Indication Status | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FCC` | Extension 7 | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FCD` | Service Provider Display Information | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FCE` | MMS Notification | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FCF` | Extension 8 | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FD0` | MMS Issuer Connectivity Parameters | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FD1` | MMS User Preferences | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FD2` | MMS User Connectivity Parameters | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FD3` | Network's indication of alerting (NIA) | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FD4` | Voice Group Call Service Ciphering Algorithm | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FD5` | Voice Broadcast Service Ciphering Algorithm | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FD5` | GBA Bootstrapping parameters | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6FD6` | GBA Bootstrapping parameters | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FD7` | MBMS Service Keys List | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FD7` | GBA NAF List | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6FD8` | MBMS User Key | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FD9` | Equivalent HPLMN | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FDA` | GBA NAF List | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FDB` | EHPLMN Presentation Indication | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FDC` | Last RPLMN Selection Indication | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FDD` | NAF Key Centre Address | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FDD` | NAF Key Centre Address | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6FDE` | Service Provider Name Icon | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FDF` | PLMN Network Name Icon | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FE0` | In Case of Emergency – Dialling Number | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FE1` | In Case of Emergency – Free Format | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FE2` | Network Connectivity Parameters for UICC IP | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FE3` | EPS location information | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FE4` | EPS NAS Security Context | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FE5` | Public Service Identity of the SM-SC | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FE5` | Public Service Identity of the SM-SC | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6FE6` | USAT Facility Control | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FE7` | UICC IARI | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FE7` | UICC IARI | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6FE8` | Non Access Stratum Configuration | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FE9` | UICC certificate | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FEA` | Relay Node ID | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FEB` | Max value of Secure Channel counter | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FEC` | Public Warning System | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FED` | FDN URI | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FEE` | BDN URI | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FEF` | SDN URI | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FF0` | IMEI(SV) Allowed List | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FF1` | IMEI(SV) Pairing Status | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FF2` | IMEI(SV) Pairing Devices | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FF3` | Home ePDG Identifier | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FF4` | ePDG Selection Information | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FF5` | Emergency ePDG Identifier | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FF6` | ePDG Selection Information for Emergency | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FF7` | From Preferred | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FF7` | From Preferred | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6FF8` | IMSConfigData | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FF8` | IMSConfigData | ADF_ISIM (TS 31.103) | SIM EF / FID file IDs | `(ADF, FID)` | 31103-e11.txt |  |
| `6FF9` | 3GPPPSDATAOFF | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FFA` | 3GPPPSDATAOFFservicelist | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FFB` | TV Configuration | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FFC` | XCAP Configuration Data | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FFD` | EARFCN List for MTC/NB-IOT UEs | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `6FFE` | MuD and MiD configuration data | ADF_USIM (TS 31.102) | SIM EF / FID file IDs | `(ADF, FID)` | 31102-j50.txt |  |
| `70` | Last Envelope tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `70` | Allowlist M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.9 |
| `71` | Registry application data tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `71` | 5G ProSe Report Data tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `72` | Reserved for 3GPP (PLMNwAcT List tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `72` | PLMNwAcT List tag Extended information tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `73` | Card Capabilities | ATR data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `73` | Discretionary Template | Application template ('61') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `73` | Reserved for 3GPP (Routing Area Information tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `73` | Card Recognition Data – | GPC_SE_Configuration-v2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.2.2 |
| `73` | Discretionary Data (BER-TLV encoded) | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.2 |
| `73` | Security Domain Recognition Data – | GPC_UICC_Configuration-v2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.4.1 |
| `73` | Routing Area Information tag URI truncated SOR-CMCI tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `74` | Reserved for 3GPP (Update/Attach Type tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `74` | Update/Attach Type tag ProSe Report Data tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `75` | Reserved for 3GPP (Rejection Cause Code tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `75` | Rejection Cause Code tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `76` | Reserved for 3GPP (Geographical Location | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `76` | Geographical Location Parameters tag IARI tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `77` | Reserved for 3GPP (GAD shapes tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `77` | GAD shapes tag IMPU list tag Allowed Slices Information with S-NSSAI mapping tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `78` | Reserved for 3GPP (NMEA sentence tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `78` | NMEA sentence tag Allowed Slices information tag IMS Status-Code tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `79` | Reserved for 3GPP (PLMN List tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `79` | PLMN List tag E-UTRAN/Satellite E-UTRAN Inter-frequency Network Measurement Results tag Partial NSSAI tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `7A` | Broadcast Network Information tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `7A` | SignOutputData | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 5.3 |
| `7B` | Security Environment Template | Templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `7B` | ACTIVATE descriptor tag | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `7B` | securityEnvironmentTemplate | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 5.3 |
| `7C` | Reserved for 3GPP (EPS PDN connection activation | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `7C` | EPS PDN connection Activation parameters tag DNN list tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `7D` | Reserved for 3GPP (Tracking Area Identification tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `7D` | Tracking Area Identification tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `7E` | Reserved for 3GPP (CSG ID list tag) | Card application toolkit data objects | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `7E` | CSG ID list tag Media type tag | Both directions (COMPREHENSION-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `7F20` | Display Control Template (including all if available available sub-tags and their values) | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11.3.3.1 |
| `7F21` | Certificate (CERT.AP.ECKA) M | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.1.2.3 |
| `7F21` | Certificate M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.1 |
| `7F22` | Certification Data Tag Len Description | GPC_SPE_095-Digital-Letter-of-Approval | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.1 |
| `7F49` | ePK.AP.ECKA M | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.1.2.3 |
| `7F49` | Public Key (see Table 6-3) M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.1 |
| `7F49` | Public key PK.CASD.ECDSA Tag Length Description | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.5.3 |
| `80` | ControlRefTemplate | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.5.1 |
| `80` | ControlRefTemplate | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.5.1 |
| `80` | ControlRefTemplate | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.5.1 |
| `80` | File Size - Data | FCP template ('62') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `80` | Access Mode - Generic Command | Security attribute template ('AB') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `80` | UICC Characteristics | Proprietary template ('A5') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `80` | Terminal power supply | Terminal capabilities template ('A9') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `80` | Number of executed C-APDUs tag (for Release 6) | Response Scripting template ('AB' or 'AF') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `80` | Number of executed command TLV objects tag (for Release 7 onwards) | Response Scripting template ('AB' or 'AF') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `80` | Secure Channel TLV | Transact Data command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `80` | Public Key Point Q (in uncompressed encoding as | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 5.2.2 |
| `80` | '85' (PSK TLS) | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.9.2 |
| `80` | System Code: The System Code is an application specific code used during anti-collision | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.8 |
| `80` | Cryptographic mechanism reference: SCP id + options ‘i’ (= scp // i ) | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.3.2 |
| `80` | Cryptographic mechanism reference: SCP id + options ‘i’ (= scp // i ) | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.3.2 |
| `80` | Cryptographic mechanism reference: SCP id + options “i” (= scp // i ) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `80` | Cryptographic mechanism reference: SCP id + options “i” (= scp // i ) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `80` | SCP Identifier (e.g. '03', '04', '11', '80', '81', '82', …) SCP Identifiers may occur in arbitrary order in Card Capabi… | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `80` | Key Type according to [GPCS] Table 11-16 M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.7.2.3 |
| `80` | Upgrade Options (see Table 4-4) | GPC_SPE_120-Amendment-H-Executable-Load-File-Upgrade-v1.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.1.2.3 |
| `80` | Key type is restricted to '80' or '82' (i.e. SCP02) if | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.12.3 |
| `80` | Cryptographic mechanism reference: SCP id + options “i” (= scp // i ) | GPC_SPE_178-Amendment-L-SCP10 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 5.5.5 |
| `80` | SCP type ('04') … | GPC_SPE_182-Amendment-K-SCP04-v1.0.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.4 |
| `80` | Key Type = '80' (DES) | GPC_UICC_Configuration-v1.0.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 10.1.2 |
| `80` | MMS Implementation | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.2.69 |
| `80` | NAF_ID | 31103-e11 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31103-e11 | 4.2.10 |
| `80` | PLMN | 31111-j40 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31111-j40 | 8.100 |
| `80` | NAF_ID | ETSI-TS-131-103-v14.1.1 | 3GPP / ETSI card-layer | `(document, clause, tag)` | ETSI-TS-131-103-v14.1.1 | 4.2.10 |
| `8010` | Encrypted Secure channel Application provider symmetric Yes symmetric keys secure channel keys | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.5.3 |
| `80B8` | Encrypted key Encrypted Application Provider Key | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.4.2 |
| `81` | ControlRefTemplate | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.5.1 |
| `81` | ControlRefTemplate | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.5.1 |
| `81` | pollingAddress | RpmConfiguration | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 2.4.12 |
| `81` | defaultSmdpAddress | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `81` | defaultSmdpAddress | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.2.2 |
| `81` | File Size - Total | FCP template ('62') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `81` | Application Power Consumption | Proprietary template ('A5') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `81` | Extended logical channels terminal support | Terminal capabilities template ('A9') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `81` | reserved for OMA SCWS [25] and GlobalPlatform Card Specification Amd. B [30] | Remote Management Application Data templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `81` | Immediate Action tag | Command Scripting template ('AA' or 'AE') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `81` | Immediate Action Response tag | Response Scripting template ('AB' or 'AF') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `81` | UICC_ID TLV | Manage Secure Channel command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `81` | Encrypted Data BER TLV | Transact Data command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `81` | Key Length (in bytes) | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.5.1 |
| `81` | Administration session triggering parameters Tag Len Name | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.7 |
| `81` | SAK: Preformatted Select AcKnowledge as defined in [14443-3], when the UID is complete | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.6 |
| `81` | List of supported options for that protocol (e.g. '15 55' for SCP02) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `81` | List of supported options for that protocol (e.g. '15 55' for SCP02) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `81` | Curve parameter length, in bytes (unsigned integer value) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2.2 |
| `81` | Key Length (in bytes) M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.7.2.3 |
| `81` | Minimum ELF version number for the old ELF version | GPC_SPE_120-Amendment-H-Executable-Load-File-Upgrade-v1.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.1.2.3 |
| `81` | Key length (in bytes) | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.12.3 |
| `81` | List of supported options for that protocol (see section 4.1) | GPC_SPE_182-Amendment-K-SCP04-v1.0.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.4 |
| `81` | Key Length = '10' | GPC_UICC_Configuration-v1.0.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 10.1.2 |
| `81` | MMS Relay/Server | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.2.69 |
| `81` | B-TID | 31103-e11 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31103-e11 | 4.2.10 |
| `81` | CSG ID and Name | 31111-j40 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31111-j40 | 8.100 |
| `81` | B-TID | ETSI-TS-131-103-v14.1.1 | 3GPP / ETSI card-layer | `(document, clause, tag)` | ETSI-TS-131-103-v14.1.1 | 4.2.10 |
| `8112` | Private Key Exponent | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8112` | Private Key Exponent | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8112` | Private Key Exponent | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8121` | RSACRT constant q-1 mod p | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8121` | RSACRT constant q-1 mod p | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8121` | RSACRT constant q-1 mod p | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8122` | RSACRT constant d mod (q – 1) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8122` | RSACRT constant d mod (q – 1) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8122` | RSACRT constant d mod (q – 1) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8123` | RSACRT constant d mod (p – 1) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8123` | RSACRT constant d mod (p – 1) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8123` | RSACRT constant d mod (p – 1) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8124` | RSACRT constant prime factor q | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8124` | RSACRT constant prime factor q | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8124` | RSACRT constant prime factor q | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8125` | RSACRT constant prime factor p | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8125` | RSACRT constant prime factor p | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8125` | RSACRT constant prime factor p | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8137` | d (private key) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8137` | d (private key) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `8137` | d (private key) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2.2 |
| `82` | File Descriptor | FCP template ('62') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `82` | Minimum Application Clock Freq. | Proprietary template ('A5') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `82` | Additional interfaces support | Terminal capabilities template ('A9') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `82` | Error Action tag | Command Scripting template ('AA' or 'AE') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `82` | Endpoint information TLV | Manage Secure Channel command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `82` | Command APDU BER TLV | Transact Data command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `82` | Key Identifier = '00' - '7F' | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.4.2 |
| `82` | Key Identifier | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.9.2 |
| `82` | Response Time Descriptor: The Response Time Descriptor is used to calculate the response time for the | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.8 |
| `82` | Privileges that can be assigned to any application | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `82` | Privileges that can be assigned to any application | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `82` | Supported key sizes (for SCP03 or SCP04); see Table H-7 | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `82` | Upgrade Session Digest | GPC_SPE_120-Amendment-H-Executable-Load-File-Upgrade-v1.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.1.2.3 |
| `82` | Key Identifier = '00' – '7F'. If not present, the default key | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.12.3 |
| `82` | Supported keys for SCP04 | GPC_SPE_182-Amendment-K-SCP04-v1.0.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.4 |
| `82` | Interface to Core Network and Bearer Information | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.2.69 |
| `83` | eimTransactionId | IpaEuiccDataRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `83` | eimTransactionId | IpaEuiccDataRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.1.2 |
| `83` | File Identifier | FCP template ('62') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `83` | Key Reference | Control reference template ('A4') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `83` | Key Reference | PIN Status data objects ('C6') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `83` | Amount of Available Memory | Proprietary template ('A5') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `83` | eUICC-related capabilities (SGP.22 [44]) | Terminal capabilities template ('A9') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `83` | Script Chaining tag | Command Scripting template ('AA' or 'AE') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `83` | Script Chaining Response tag | Response Scripting template ('AB' or 'AF') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `83` | Term label - Terminal_ID TLV | Manage Secure Channel command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `83` | Response APDU BER TLV | Transact Data command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `83` | Key Version Number = '01' - '6F' | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.4.2 |
| `83` | Administration Session Parameters Tag Len Name | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.7 |
| `83` | Higher layer response in response to ATTRIB as defined in [102 622] Value is a LV structure Length Value Description | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.7 |
| `83` | Supported TLS cipher suites for SCP81 | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `83` | Supported TLS cipher suites for SCP81 | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `83` | Supported LFDBH algorithms | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `83` | byte 1: Key Identifier M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.3 |
| `83` | Allowed parameter values for the deletion of associated Applications (See Table 4-7.) | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.5.2 |
| `83` | Key Version Number | GPC_SPE_182-Amendment-K-SCP04-v1.0.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.1 |
| `83` | Key Version Number = '01' – '7F' | GPC_UICC_Configuration-v1.0.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 10.1.3 |
| `83` | Gateway | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.2.69 |
| `84` | hostId | ControlRefTemplate | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2, v2.7, v3.1 | 5.5.1 |
| `84` | associationToken | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `84` | associationToken | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.2.2 |
| `84` | DF Name (AID) | FCP template ('62') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `84` | File details | Proprietary template ('A5') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `84` | eUICC-related capabilities (SGP.32 [45]) | Terminal capabilities template ('A9') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `84` | Term label - Terminal_appli_ID TLV | Manage Secure Channel command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `84` | HostID (shall only be present if scenario '03' parameter b3 is set) | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.5.1 |
| `84` | RAS Connection Parameters | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.7 |
| `84` | Maximum data rate supported as defined in [102 622] M M X A A O X X R | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.7 |
| `84` | First or only Executable Module AID | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `84` | First Executable Module AID | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `84` | Maximum length of Pre Shared Key in bytes (unsigned integer) (for SCP81 only) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `84` | Maximum length of Pre Shared Key in bytes (unsigned integer) (for SCP81 only) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `84` | Max length of PSK in bytes (unsigned integer) (for SCP81 or SCP82) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `84` | HostID (shall only be present if SCP parameter b3 is C set) | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.7.2.3 |
| `84` | Host ID (shall be present for scenario #3 only if b3 of scenario parameters is set) | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.12.3 |
| `84` | Key check value | GPC_SPE_182-Amendment-K-SCP04-v1.0.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.4 |
| `84` | Reserved for 3GPP2: MMS Authentication Mechanism | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.2.69 |
| `85` | DeviceInfo | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 4.2 |
| `85` | Proprietary - Primitive | FCP template ('62') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `85` | Reserved file size | Proprietary template ('A5') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `85` | Term label - UICC_Identifier TLV | Manage Secure Channel command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `85` | Key check value algorithm | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.9.2 |
| `85` | CID Support: Support of the Card Identifier field as defined XOR | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.6 |
| `85` | Cipher suites supported for tokens | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `85` | Cipher suites supported for tokens | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `85` | Cipher suites supported for tokens | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `85` | Supported cipher suites for SCP22 | GPC_SPE_106-Amendment-G-Opacity-Secure-Channel-v1.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.1 |
| `85` | DR value generated by SEMS Application | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.12.4.2 |
| `85` | Protocol Configuration List of supported Protocol Configuration Identifiers for SCP04 | GPC_SPE_182-Amendment-K-SCP04-v1.0.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.4 |
| `85` | Reserved for 3GPP2: MMS Authentication User Name | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.2.69 |
| `86` | Maximum file size | Proprietary template ('A5') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `86` | Term label - UICC_appli_ID TLV | Manage Secure Channel command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `86` | Receipt | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.5.4 |
| `86` | Session Retry Policy Parameters | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.7 |
| `86` | DATA_RATE_MAX: Maximum data rate supported as M M X | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.6 |
| `86` | Cipher suites supported for receipts | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `86` | Cipher suites supported for receipts | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `86` | Cipher suites supported for receipts | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `86` | Receipt M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.6.3.1 |
| `86` | Public key PK.SP.AUT coded as | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.5.2 |
| `86` | PLMN identifier | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.11.4 |
| `87` | eimTransactionId | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `87` | eimTransactionId | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.2.2 |
| `87` | Supported system commands | Proprietary template ('A5') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `87` | Key Agreement Mechanism TLV | Manage Secure Channel command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `87` | Protocol Data Type B (Card Emulation Mode) (see section 4.7) | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.1 |
| `87` | Cipher suites supported for DAPs | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `87` | Cipher suites supported for DAPs | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `87` | Cipher suites supported for DAPs | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `87` | Privacy config | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.13.4 |
| `88` | SFI Support | FCP template ('62') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `88` | Specific UICC environmental conditions | Proprietary template ('A5') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `88` | MSA_ID TLV | Manage Secure Channel command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `88` | Protocol Data Type F (Card Emulation Mode) (see section 4.8) | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.1 |
| `88` | Key Parameter Reference List | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `88` | Key Parameter Reference List | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `88` | Key Parameter Reference List | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `88` | G ProSe direct communication in NR-PC5 | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.13.4 |
| `89` | Platform to Platform CAT Secured APDU | Proprietary template ('A5') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `89` | Algorithm and Integrity TLV | Manage Secure Channel command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `89` | HTTP POST parameters Tag Len Name | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.8 |
| `89` | Contactless Protocol Type Identifier (see Table 3-26) | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11.4.2.3 |
| `89` | Supported version of ELF Upgrade Process & Options (see [Amd H]) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `89` | CoAP POST parameters Tag Length Value | GPC_SPE_207-Amendment-M-Remote-App-Mgmt-CoAP-v1.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.7 |
| `89` | Text CSG Type | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.6.3 |
| `8A` | Life Cycle Status | FCP template ('62') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `8A` | Tnonce TLV | Manage Secure Channel command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `8A` | RAS IP Retry Policy parameters | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.8 |
| `8A` | Support of | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `8A` | Deprecated (see tag '90' and tag '91') C AID prefix bytes used to control which Application may be installed, | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 8.2.3 |
| `8A` | Administration Host parameter (identical to [GPCS-B]) | GPC_SPE_207-Amendment-M-Remote-App-Mgmt-CoAP-v1.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.7 |
| `8B` | Security Attribute - Reference Format | FCP template ('62') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `8B` | CSA_ID TLV | Manage Secure Channel command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `8B` | Inactivity Timeout parameter | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.8 |
| `8B` | List of allowed DGI numbers in STORE DATA. O The list is formatted as a sequence of the DGI tags. If this tag is n | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 8.2.3 |
| `8B` | Agent ID parameter (identical to [GPCS-B]) | GPC_SPE_207-Amendment-M-Remote-App-Mgmt-CoAP-v1.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.7 |
| `8B` | RSC info list | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.13.5 |
| `8C` | Security Attribute - Compact Format | FCP template ('62') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `8C` | Unonce TLV | Manage Secure Channel command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `8C` | Administration URI parameter | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.7 |
| `8C` | List of allowed TLV tags in STORE DATA. O The list is formatted as a sequence of the BER-TLV tags. If this tag | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 8.2.3 |
| `8C` | Value of Uri-Path | GPC_SPE_207-Amendment-M-Remote-App-Mgmt-CoAP-v1.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.7 |
| `8C` | QI to PC5 QoS parameters mapping rules | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.13.5 |
| `8D` | SSCMAC TLV | Manage Secure Channel command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `8D` | Value of Uri-Query | GPC_SPE_207-Amendment-M-Remote-App-Mgmt-CoAP-v1.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.7 |
| `8E` | Endpoint data container size TLV | Manage Secure Channel command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `8E` | Signature of (DGI '00B8' // DGI '80B8') | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.4.2 |
| `8E` | AID prefix bytes used to control which Application or ELF O may be deleted. Only Application and ELF AID values matchin… | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 8.2.3 |
| `8E` | Signature of (DGI '00B8' // DGI '80B8') | GPC_UICC_Configuration-v1.0.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 10.1.2 |
| `8E` | User info ID for discovery | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.13.5 |
| `8F` | CSAMAC TLV | Manage Secure Channel command | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `8F` | AID prefix bytes used to control which Executable Load O File may be upgraded. Only ELF AID values matching these prefi… | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 8.2.3 |
| `8F` | Key type according to | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.5.2 |
| `90` | profileNickname | ProfileInfoListResponse | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2, v2.7, v3.1 | 5.7.15 |
| `90` | profileNickname | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `90` | profileNickname | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 4.4 |
| `90` | Security Condition - ALWAYS | Security attribute template ('AB') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `90` | PIN Enabled/Disabled status byte(s) | PIN Status data objects ('C6') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `90` | Bad format tag | Response Scripting template ('AB' or 'AF') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `90` | Byte 1: Scenario identifier – value '03' only | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.5.1 |
| `90` | Application AID prefix bytes used to control which C Application may be installed. Only Application AID values matching… | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 8.2.3 |
| `90` | ELF Upgrade Session Status (see Table 4-8) | GPC_SPE_120-Amendment-H-Executable-Load-File-Upgrade-v1.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.1.3.1 |
| `90` | '01': CERT.CASD.AUT | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.15.2 |
| `90` | Scenario Identifier '04' (refer to Table 9-2) | GPC_UICC_Configuration-v1.0.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 10.3.1 |
| `91` | serviceProviderName | UpdateMetadataRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2, v2.7, v3.1 | 5.4.1 |
| `91` | serviceProviderName | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `91` | serviceProviderName | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 4.4 |
| `91` | Initial value of sequence counter | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.5.1 |
| `91` | ELF AID prefix bytes used to control which Application may C be loaded. Only ELF matching these prefix bytes (i.e. part… | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 8.2.3 |
| `91` | Unpredictable value for use in secure messaging Should be set to an unpredictable value that satisfies the | GPC_SPE_178-Amendment-L-SCP10 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.1.2 |
| `92` | profileName | UpdateMetadataRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2, v2.7, v3.1 | 5.4.1 |
| `92` | profileName | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `92` | profileName | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 4.4 |
| `92` | Allowlist counter (2-byte positive integer up to 32767) C | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.9 |
| `92` | Privacy timer | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.13.5 |
| `93` | iconType | UpdateMetadataRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2, v2.7, v3.1 | 5.4.1 |
| `93` | iconType | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `93` | iconType | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 4.4 |
| `93` | Certificate Serial Number | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.2 |
| `93` | Token Identifier | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 12.3 |
| `93` | Token identifier/number (digital signature counter) | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `93` | Token identifier/number (digital signature counter) | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `93` | Token identifier/number (digital signature counter) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `93` | Token identifier/number (digital signature counter) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `93` | Token identifier/number (digital signature counter) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `93` | Certificate Serial Number M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.1 |
| `93` | Token identifier/number (digital signature counter) | GPC_SPE_120-Amendment-H-Executable-Load-File-Upgrade-v1.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.1.2.3 |
| `93` | Certificate Serial Number | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.5.2 |
| `93` | Certificate Serial Number | GPC_UICC_Configuration-v1.0.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 9.2.1 |
| `93` | G PKMF address information | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.13.5 |
| `94` | Collection period | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.13.7 |
| `95` | profileClass | StoreMetadataRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2, v2.7, v3.1 | 5.5.3 |
| `95` | profileClass | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `95` | profileClass | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 4.4 |
| `95` | Usage Qualifier | Control reference template ('A4') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `95` | Usage Qualifier | PIN Status data objects ('C6') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `95` | Key Usage Qualifier = '40' (encipherment of sensitive data in responses) | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.4.2 |
| `95` | Key Usage Qualifier according to [GPCS] section 11.1.9 | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.9.2 |
| `95` | Usage Qualifier = ‘10’ (secure messaging for | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.3.2 |
| `95` | Key Usage Qualifier = ‘10’ (secure messaging for | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.3.2 |
| `95` | Key Usage Qualifier values according to section 11.1.9 | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `95` | Key Usage Qualifier values according to section 11.1.9 | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `95` | Key Usage: M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.1 |
| `95` | Key usage. It must be '82', meaning digital signature verification. | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.5.2 |
| `95` | Key Usage Qualifier = | GPC_SPE_178-Amendment-L-SCP10 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.1.2 |
| `95` | Key Usage | GPC_UICC_Configuration-v1.0.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 9.2.1 |
| `95` | Reporting window | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.13.7 |
| `96` | Key Access according to [GPCS] Table 11-18 | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.5.1 |
| `96` | Key Access according to [GPCS] section 11.1.10 | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.9.2 |
| `96` | Privacy-Sensitive Indicator (see section 13.1) | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2 |
| `96` | Key Access according to section 11.1.10 | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.1 |
| `96` | Key Access according to section 11.1.10 | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.1 |
| `96` | Key Access Condition, see section 11.1.10 | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.3.1.2 |
| `96` | Key Access according to [GPCS] Table 11-18 | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.12.3 |
| `96` | Key Access Condition according to [GPCS] section 11.1.10 | GPC_SPE_182-Amendment-K-SCP04-v1.0.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.1 |
| `96` | Reporting indicators | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.13.7 |
| `97` | Security Condition - NEVER | Security attribute template ('AB') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `97` | Key Purpose, see section 11.1.13 | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `97` | Key Purpose, encoding the SCP Identifier (i.e. '0004') | GPC_SPE_182-Amendment-K-SCP04-v1.0.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.4 |
| `98` | Key Purpose Details, see section 11.1.13 | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `98` | Key Purpose Details, i.e. Protocol Configuration Identifier(s) | GPC_SPE_182-Amendment-K-SCP04-v1.0.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.4 |
| `98` | HPLMN 5G DDNMF address information | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.13.3 |
| `99` | profilePolicyRules | UpdateMetadataRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2, v2.7 | 5.4.1 |
| `99` | forbiddenProfilePolicyRules | EUICCInfo2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 4.2 |
| `99` | profilePolicyRules | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `99` | profilePolicyRules | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 4.4 |
| `9B` | hriServerAddress | UpdateMetadataRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.4.1 |
| `9B` | Warning message broadcast | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.13.5 |
| `9C` | Proprietary State Machine | Security attribute template ('AB') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `9E` | Security Condition - Security Condition Byte | Security attribute template ('AB') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `9E` | Signature of (DGI '00A6' // DGI '8010') | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.5.3 |
| `9E` | Delete Token | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `9E` | Delete Token | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `9E` | Delete Token | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `9E` | Delete Token | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `9E` | Delete Token | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `9E` | Upgrade Token | GPC_SPE_120-Amendment-H-Executable-Load-File-Upgrade-v1.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 4.1.2.3 |
| `9F08` | Version number (2 bytes), Value '01' '00' | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11.6.3 |
| `9F08` | Version of the SEMS Application or SEMS Updater | GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.3.5.1 |
| `9F1F` | StoreMetadataRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.5.3 |
| `9F21` | estimatedProfileSize | StoreMetadataRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.5.3 |
| `9F24` | enabledOnEsimPort | ProfileInfoListResponse | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.15 |
| `9F25` | profileSize | ProfileInfoListResponse | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.15 |
| `9F26` | fallbackAttribute | ProfileInfoListResponse | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.15 |
| `9F26` | fallbackAttribute | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `9F26` | fallbackAttribute | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 4.4 |
| `9F2A` | UpdateMetadataResponse | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.4.1 |
| `9F67` | fallbackAllowed | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `9F67` | fallbackAllowed | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 4.4 |
| `9F70` | profileState | ProfileInfoListResponse | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2, v2.7, v3.1 | 5.7.15 |
| `9F70` | profileState | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `9F70` | profileState | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 4.4 |
| `9F70` | Application Lifecycle State (always available) | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11.3.3.1 |
| `9F70` | Life Cycle State Privileges (byte 1 - byte 2 – byte 3) see | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `9F70` | Life Cycle State Privileges (byte 1 - byte 2 – byte 3) see | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `9F70` | Life Cycle State | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `9F70` | Life Cycle State | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `9F70` | Life Cycle State | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `9F78` | EuiccInfo2Ext | SGP.23 v1.16 | eSIM RSP ASN.1 | `(module, tag)` | SGP.23 v1.16 | 5.4.11.2 |
| `9F7B` | ecallIndication | StoreMetadataRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.5.3 |
| `9F7B` | ecallIndication | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `9F7B` | ecallIndication | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 4.4 |
| `A0` | notificationsList | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `A0` | notificationsList | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.2.2 |
| `A0` | Security Condition - OR Template | Security attribute template ('AB') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `A0` | EAP Application service specific data content tag | Discretionary template ('73') in EF DIR | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `A0` | List of conflicting Applications (protocol parameters conflict) Tag Length Value Description | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11.4.3.1 |
| `A0` | SCP information for first or only SCP | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `A0` | SCP information for first or only SCP | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `A0` | Add Token Identifier(s) to Token Identifier Deny List Tag Length Value Description | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `A0` | SCP information | GPC_SPE_106-Amendment-G-Opacity-Secure-Channel-v1.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.1 |
| `A0` | SCP Information | GPC_SPE_182-Amendment-K-SCP04-v1.0.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.4 |
| `A0` | MUK ID | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.2.81 |
| `A1` | M2M service specific data content tag | Discretionary template ('73') in EF DIR | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `A1` | Remove Token Identifier(s) from the blacklist Tag Length Value Description | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 12.4 |
| `A1` | Remove Token Identifier(s) from Token Identifier Deny List Tag Length Value Description | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.5 |
| `A1` | PDU Info List data object | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.14.2 |
| `A2` | ProfilePolicyAuthorisationRule | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 6.6.1 |
| `A2` | RemoteProfileProvisioningRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 6.6.1 |
| `A2` | RemoteProfileProvisioningRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 6.6.1 |
| `A2` | euiccPackageResultList | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `A2` | euiccPackageResultList | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.2.2 |
| `A2` | oneM2M service specific data content tag | Discretionary template ('73') in EF DIR | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `A2` | Reserved for GSMA RSP | Remote Management Application Data templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `A2` | List of reasons and conflicting applications (policy conflict) Tag Length Value Description | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11.4.3.1 |
| `A3` | Add to the CREL List (see section 3.8.3) | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.3 |
| `A4` | Control reference Template | Security attribute template ('AB') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `A4` | List of conflicting Applications (privacy conflict) Tag Length Value Description | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11.4.3.1 |
| `A5` | eumCertificate | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `A5` | eumCertificate | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.2.2 |
| `A5` | Proprietary Template | FCP template ('62') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `A5` | Extended Security parameters Tag Len Name | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.8 |
| `A5` | FCI Proprietary Template Tag Length Value Description | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11.6.3 |
| `A6` | euiccCertificate | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `A6` | euiccCertificate | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.2.2 |
| `A6` | CRT TLV with all sub TLVs as provided in the STORE DATA command | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.5.4 |
| `A6` | Application discretionary data (see section 3.4) | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.3 |
| `A6` | CRT TLV with all sub TLVs as provided in the MUTUAL M AUTHENTICATE command | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.6.2.3 |
| `A8` | ipaCapabilities | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `A8` | ipaCapabilities | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.2.2 |
| `A9` | deviceInfo | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `A9` | deviceInfo | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.2.2 |
| `A9` | File Ids indicated using constructed | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.2.1 |
| `AA` | Command Scripting Template for definite length coding | Remote Management Application Data templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `AA` | File Ids indicated using constructed | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.4.2.1 |
| `AB` | Security Attribute Template - Expanded Format | FCP template ('62') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `AB` | Response Scripting Template for definite length coding | Remote Management Application Data templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `AB` | MMS Connectivity Parameters | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.2.69 |
| `AC` | CoAP Administration URI parameter Tag Length Value | GPC_SPE_207-Amendment-M-Remote-App-Mgmt-CoAP-v1.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.7 |
| `AE` | Command Scripting Template for indefinite length coding | Remote Management Application Data templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `AF` | Security Condition - AND Template | Security attribute template ('AB') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `AF` | Response Scripting Template for indefinite length coding | Remote Management Application Data templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `B0` | Public Key Point Q (in uncompressed encoding as | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.3.2 |
| `B0` | (Assigned to ETSI) | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2 |
| `B0` | Public key – Q M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.1 |
| `B3` | DNS Resolution Parameters Tag Len Name | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.7 |
| `B5` | lpaRspCapability | InitiateAuthenticationRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 6.6.2 |
| `B6` | ProfileInfoListResponse | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.15 |
| `B6` | ProfileInfoListResponse | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.15 |
| `B6` | UpdateMetadataRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.4.1 |
| `B6` | IpaCapabilities | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `B6` | IpaCapabilities | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 4.4 |
| `B6` | Control Reference Template for Digital Signature (Token) | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `B6` | Control Reference Template for Digital Signature (Token) | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `B6` | Control Reference Template for Digital Signature (Token) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `B6` | Control Reference Template for Digital Signature (Token) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `B6` | Control Reference Template | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.1 |
| `B7` | profileOwner | StoreMetadataRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2, v2.7, v3.1 | 5.5.3 |
| `B7` | profileOwner | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `B7` | profileOwner | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 4.4 |
| `B7` | Key Attributes (common to all key components) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.2 |
| `B7` | Key Attributes | GPC_SPE_182-Amendment-K-SCP04-v1.0.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.1 |
| `B8` | dpProprietaryData | ConfigureISDPRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2, v2.7, v3.1 | 5.5.2 |
| `B8` | dpProprietaryData | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `B8` | dpProprietaryData | IpaCapabilities | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 4.4 |
| `B8` | CRT tag (CT) | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.4.2 |
| `B8` | Template (CT) | GPC_UICC_Configuration-v1.0.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 10.1.2 |
| `B9` | Description of 1st key | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.5.1 |
| `B9` | CRT tag (CT) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.1 |
| `B9` | CRT tag (CT) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.11.4.1 |
| `B9` | Key Component Attributes (last key component) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.3.1.2 |
| `B9` | Key Component Attributes | GPC_SPE_182-Amendment-K-SCP04-v1.0.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.1 |
| `BA` | rpmConfiguration | UpdateMetadataRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.4.1 |
| `BC` | UpdateMetadataRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.4.1 |
| `BD` | UpdateMetadataRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.4.1 |
| `BE` | StoreMetadataRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.5.3 |
| `BF20` | GetEuiccInfo1Request | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.8 |
| `BF20` | GetEuiccInfo1Request | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.8 |
| `BF20` | EUICCInfo1 | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 4.2 |
| `BF20` | euiccInfo1 | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `BF20` | euiccInfo1 | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.2.2 |
| `BF20` | UICCCapability | TCA Interop v3.4 | eSIM RSP ASN.1 | `(module, tag)` | TCA Interop v3.4 | 8.1.2 |
| `BF20` | ServicesList | TCA Pkg v3.4.1 | eSIM RSP ASN.1 | `(module, tag)` | TCA Pkg v3.4.1 | 8.2.1 |
| `BF20` | UICCCapability | TCA Pkg v3.4.1 | eSIM RSP ASN.1 | `(module, tag)` | TCA Pkg v3.4.1 |  |
| `BF20` | UICCCapability | TCA-PEDefinitions-v3.2 | eSIM RSP ASN.1 | `(module, tag)` | TCA-PEDefinitions-v3.2 |  |
| `BF20` | Authorizations under SCP11c or SCP11a C | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.1 |
| `BF21` | PrepareDownloadRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.5 |
| `BF21` | PrepareDownloadRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.5 |
| `BF21` | PrepareDownloadRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.5 |
| `BF21` | PrepareDownloadResponse | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.10 |
| `BF21` | PrepareDownloadResponse | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.14.2 |
| `BF21` | SCP11 Certificate Store (see section 7.2, Table 7-4) M | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.8 |
| `BF22` | GetEuiccInfo2Request | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.8 |
| `BF22` | serviceSpecificDataStoredInEuicc | UpdateMetadataRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.4.1 |
| `BF22` | EUICCInfo2 | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 4.2 |
| `BF22` | euiccInfo2 | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `BF22` | euiccInfo2 | IpaEuiccData | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.2.2 |
| `BF23` | initialiseSecureChannelRequest | BoundProfilePackage | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2, v2.7, v3.1 | 2.5.4 |
| `BF23` | StoreMetadataRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.5 |
| `BF24` | ConfigureISDPRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.5.2 |
| `BF24` | ConfigureISDPRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.5.2 |
| `BF24` | ConfigureISDPRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.5.2 |
| `BF25` | StoreMetadataRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.5.3 |
| `BF25` | StoreMetadataRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.5.3 |
| `BF25` | StoreMetadataRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.5.3 |
| `BF25` | StoreMetadataRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 4.10 |
| `BF25` | StoreMetadataRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.5 |
| `BF27` | ProfileInstallationResultData | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 2.5.6 |
| `BF27` | ProfileInstallationResultData | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 2.5.6 |
| `BF27` | ProfileInstallationResultData | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 2.5.6 |
| `BF28` | ListNotificationRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.9 |
| `BF28` | ListNotificationRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.9 |
| `BF28` | ListNotificationRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.9 |
| `BF29` | SetNicknameRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.21 |
| `BF29` | SetNicknameRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.21 |
| `BF29` | SetNicknameRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.21 |
| `BF2A` | UpdateMetadataRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.4.1 |
| `BF2A` | UpdateMetadataRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.4.1 |
| `BF2A` | UpdateMetadataRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.4.1 |
| `BF2A` | UpdateMetadataRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.4.2 |
| `BF2B` | RetrieveNotificationsListRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.10 |
| `BF2B` | RetrieveNotificationsListRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.10 |
| `BF2B` | RetrieveNotificationsListRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.10 |
| `BF2B` | RetrieveNotificationsListRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 4.10 |
| `BF2B` | RetrieveNotificationsListRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.9.11 |
| `BF2D` | ProfileInfoListRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.15 |
| `BF2D` | ProfileInfoListRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.15 |
| `BF2D` | ProfileInfoListRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.15 |
| `BF2D` | listProfileInfo | Psmo | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `BF2D` | listProfileInfo | Psmo | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.1.1 |
| `BF2E` | GetEuiccChallengeRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.7 |
| `BF2E` | GetEuiccChallengeRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.7 |
| `BF2E` | GetEuiccChallengeRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.7 |
| `BF2F` | NotificationMetadata | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.9 |
| `BF2F` | NotificationMetadata | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.9 |
| `BF2F` | NotificationMetadata | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.9 |
| `BF30` | NotificationSentRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.11 |
| `BF30` | NotificationSentRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.11 |
| `BF30` | NotificationSentRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.11 |
| `BF31` | EnableProfileRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.16 |
| `BF31` | EnableProfileRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.16 |
| `BF31` | EnableProfileRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.16 |
| `BF32` | DisableProfileRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.17 |
| `BF32` | DisableProfileRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.17 |
| `BF32` | DisableProfileRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.17 |
| `BF33` | DeleteProfileRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.18 |
| `BF33` | DeleteProfileRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.18 |
| `BF33` | DeleteProfileRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.18 |
| `BF34` | EuiccMemoryResetRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.19 |
| `BF34` | EuiccMemoryResetRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.19 |
| `BF34` | EuiccMemoryResetRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.19 |
| `BF35` | LoadCRLRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.12 |
| `BF35` | LoadCRLRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.12 |
| `BF36` | BoundProfilePackage | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 2.5.4 |
| `BF36` | BoundProfilePackage | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 2.5.4 |
| `BF36` | BoundProfilePackage | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 2.5.4 |
| `BF37` | ProfileInstallationResult | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 2.5.6 |
| `BF37` | ProfileInstallationResult | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 2.5.6 |
| `BF37` | ProfileInstallationResult | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 2.5.6 |
| `BF37` | ProfileInstallationResult | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 2.1 |
| `BF37` | ProfileInstallationResult | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.14.7 |
| `BF38` | AuthenticateServerRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.13 |
| `BF38` | AuthenticateServerRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.13 |
| `BF38` | AuthenticateServerRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.13 |
| `BF38` | AuthenticateServerResponse | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.11 |
| `BF38` | AuthenticateServerResponse | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.14.3 |
| `BF39` | initiateAuthenticationRequest | ProfilePolicyAuthorisationRule | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 6.6.1 |
| `BF39` | initiateAuthenticationRequest | RemoteProfileProvisioningRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7, v3.1 | 6.6.1 |
| `BF39` | EsipaMessageFromIpaToEim | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 2.1 |
| `BF39` | EsipaMessageFromIpaToEim | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 6.3.1 |
| `BF3A` | getBoundProfilePackageRequest | ProfilePolicyAuthorisationRule | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 6.6.1 |
| `BF3A` | getBoundProfilePackageRequest | RemoteProfileProvisioningRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7, v3.1 | 6.6.1 |
| `BF3A` | EsipaMessageFromIpaToEim | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 2.1 |
| `BF3A` | EsipaMessageFromIpaToEim | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 6.3.1 |
| `BF3B` | authenticateClientRequest | ProfilePolicyAuthorisationRule | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 6.6.1 |
| `BF3B` | authenticateClientRequest | RemoteProfileProvisioningRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7, v3.1 | 6.6.1 |
| `BF3B` | AuthenticateClientRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 4.10 |
| `BF3B` | AuthenticateClientRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.6.1 |
| `BF3C` | EuiccConfiguredAddressesRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.3 |
| `BF3C` | EuiccConfiguredAddressesRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.3 |
| `BF3C` | EuiccConfiguredDataRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.3 |
| `BF3D` | HandleNotification | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 6.6.2 |
| `BF3D` | HandleNotification | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 6.6.2 |
| `BF3D` | HandleNotification | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 6.6.2 |
| `BF3D` | handleNotificationEsipa | EsipaMessageFromIpaToEim | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 2.1 |
| `BF3D` | handleNotificationEsipa | EsipaMessageFromIpaToEim | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 6.3.1 |
| `BF3E` | GetEuiccDataRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.20 |
| `BF3E` | GetEuiccDataRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.20 |
| `BF3E` | GetEuiccDataRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.20 |
| `BF3F` | SetDefaultDpAddressRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.4 |
| `BF3F` | SetDefaultDpAddressRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.4 |
| `BF3F` | SetDefaultDpAddressRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.4 |
| `BF40` | authenticateClientResponseEs11 | RemoteProfileProvisioningResponse | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2, v2.7, v3.1 | 6.6.1 |
| `BF41` | CancelSessionRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.14 |
| `BF41` | CancelSessionRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.14 |
| `BF41` | CancelSessionRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.14 |
| `BF41` | CancelSessionResponse | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 2.1 |
| `BF41` | CancelSessionResponse | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.14.8 |
| `BF42` | LpaeActivationRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.1 |
| `BF42` | LpaeActivationRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.1 |
| `BF42` | LpaeActivationRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.1 |
| `BF42` | IpaeActivationRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `BF42` | IpaeActivationRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 3.8.4 |
| `BF43` | GetRatResponse | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.22 |
| `BF43` | GetRatResponse | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.22 |
| `BF43` | GetRatRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.22 |
| `BF44` | LoadRpmPackageResult | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 2.10.2 |
| `BF45` | VerifySmdsResponseRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.24 |
| `BF46` | checkEventRequest | RemoteProfileProvisioningRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 6.6.1 |
| `BF4A` | AlertData | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.23 |
| `BF4B` | VerifyDeviceChangeRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.27 |
| `BF4C` | confirmDeviceChangeRequest | RemoteProfileProvisioningRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 6.6.1 |
| `BF4D` | PrepareDeviceChangeRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.26 |
| `BF4E` | transferEimPackageResponse | EsipaMessageFromIpaToEim | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 2.1 |
| `BF4E` | transferEimPackageResponse | EsipaMessageFromIpaToEim | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 6.3.1 |
| `BF4F` | getEimPackageRequest | EsipaMessageFromIpaToEim | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 2.1 |
| `BF4F` | getEimPackageRequest | EsipaMessageFromIpaToEim | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 6.3.1 |
| `BF50` | provideEimPackageResult | EsipaMessageFromIpaToEim | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 2.1 |
| `BF50` | provideEimPackageResult | EsipaMessageFromIpaToEim | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 6.3.1 |
| `BF51` | EuiccPackageResult | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `BF51` | EuiccPackageResult | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.2.1 |
| `BF52` | IpaEuiccDataRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `BF52` | IpaEuiccDataRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.1.2 |
| `BF53` | EimAcknowledgements | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `BF53` | EimAcknowledgements | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.1.4 |
| `BF54` | ProfileDownloadTriggerRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `BF54` | ProfileDownloadTriggerRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.1.3 |
| `BF55` | GetEimConfigurationDataRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 4.10 |
| `BF55` | GetEimConfigurationDataRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.9.18 |
| `BF56` | GetCertsRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 4.10 |
| `BF56` | GetCertsRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.9.10 |
| `BF57` | AddInitialEimRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 4.10 |
| `BF57` | AddInitialEimRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.9.4 |
| `BF58` | ProfileRollbackRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 4.10 |
| `BF58` | ProfileRollbackRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.9.16 |
| `BF59` | ConfigureImmediateProfileEnablingRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 4.10 |
| `BF59` | ConfigureImmediateProfileEnablingRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.9.17 |
| `BF5A` | ImmediateEnableRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 4.10 |
| `BF5A` | ImmediateEnableRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.9.15 |
| `BF5B` | EnableEmergencyProfileRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 4.10 |
| `BF5B` | EnableEmergencyProfileRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.9.22 |
| `BF5C` | DisableEmergencyProfileRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 4.10 |
| `BF5C` | DisableEmergencyProfileRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.9.23 |
| `BF5D` | ExecuteFallbackMechanismRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.9.20 |
| `BF5E` | ReturnFromFallbackRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 4.10 |
| `BF5E` | ReturnFromFallbackRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.9.21 |
| `BF5F` | GetConnectivityParametersRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 4.10 |
| `BF5F` | GetConnectivityParametersRequest | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 5.9.24 |
| `BF60` | VerifySmdpResponseRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.28 |
| `BF61` | checkProgressRequest | RemoteProfileProvisioningRequest | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 6.6.1 |
| `BF62` | VerifyProfileRecoveryRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.29 |
| `BF63` | DeleteNotificationForDc | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 4.1.3 |
| `BF64` | StoreMetadataRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.5.3 |
| `BF64` | EuiccMemoryResetRequest | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 4.10 |
| `BF64` | IpaCapabilities | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 4.4 |
| `BF65` | setDefaultDpAddress | Psmo | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 6.4.1.8 |
| `BF65` | setDefaultDpAddress | Psmo | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 2.11.1.1 |
| `C0` | Special File Information | Proprietary template ('A5') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `C0` | Key Information Data | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.3.1 |
| `C0` | Key Information Data | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.3.1 |
| `C0` | Key Information Data | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.3.1.1 |
| `C0` | Key Information Data | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.3.1.1 |
| `C0` | Key Information Data | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.3.1.1 |
| `C1` | Filling Pattern | Proprietary template ('A5') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `C1` | Sequence Counter of the default Key Version Number | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `C1` | Sequence Counter of the default Key Version Number | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `C1` | Sequence Counter of the default Key Version Number | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `C1` | Sequence Counter of the default Key Version Number | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `C1` | Key Sequence Counter | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.3.1.2 |
| `C2` | Repeat Pattern | Proprietary template ('A5') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `C2` | Confirmation Counter | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `C2` | Confirmation Counter | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `C2` | Confirmation Counter | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `C2` | Confirmation Counter | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `C2` | Confirmation Counter | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `C3` | Load File Data Block Signature | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.6.2.3 |
| `C3` | Load File Data Block Signature | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.6.2.3 |
| `C3` | Load File Data Block Signature | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.6.2.3 |
| `C3` | Load File Data Block Signature | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.6.2.3 |
| `C3` | Load File Data Block Signature | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.6.2.3 |
| `C4` | Application's Executable Load File AID | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `C4` | Application's Executable Load File AID | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `C4` | Application’s Executable Load File AID | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `C4` | Application’s Executable Load File AID | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `C4` | Application’s Executable Load File AID | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `C5` | Privileges (byte 1 – byte 2 – byte 3); see section 11.1.2 | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `C5` | Privileges (byte 1 – byte 2 – byte 3); see section 11.1.2 | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `C5` | Privileges (byte 1 – byte 2 – byte 3); see section 11.1.2 | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `C5` | Privileges that may be assigned to an Application created O through this secure channel. Only the specified privileges… | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 8.2.3 |
| `C6` | PIN Status data objects | FCP template ('62') | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `C9` | The identifier of the PK.CA.AUT that must be used to verify the signature of this certificate, i.e. the SHA-1 digest co… | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 5.2.2 |
| `C9` | Application Specific Parameters | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `C9` | Application Specific Parameters | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `C9` | Application Specific Parameters | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `C9` | Application Specific Parameters | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `C9` | Application Specific Parameters | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CA` | TS 102 226 specific parameter | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CA` | TS 102 226 specific parameter | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CA` | [TS 102 226] specific parameter | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CA` | [TS 102 226] specific parameter | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CA` | [TS 102 226] specific parameter | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CB` | Global Service Parameters | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CB` | Global Service Parameters | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CB` | Global Service Parameters | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CB` | Global Service Parameters | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CB` | Global Service Parameters | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CC` | Associated Security Domain’s AID | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `CC` | Associated Security Domain’s AID | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `CC` | Associated Security Domain’s AID | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `CD` | Load File Data Block format id | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CD` | Load File Data Block format id | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CD` | Load File Data Block format id | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CD` | Load File Data Block format id | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CD` | Load File Data Block format id | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CE` | Executable Load File Version Number | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `CE` | Executable Load File Version Number | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `CE` | Executable Load File Version Number | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `CE` | Executable Load File Version Number | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `CE` | Executable Load File Version Number | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `CF` | Reserved for proprietary use (direction terminal to UICC) | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `CF` | Implicit selection parameter | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CF` | Implicit selection parameter See note below | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CF` | Implicit selection parameter See note below | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CF` | Implicit selection parameter See note below | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `CF` | Implicit selection parameter See note below | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `D0` | Proactive Command | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `D0` | Force DNS Resolution | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11 |
| `D0` | Key Identifier | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.2 |
| `D0` | Key Identifier | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.2 |
| `D0` | Key Identifier | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.2 |
| `D0` | Key Identifier | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.2 |
| `D0` | Key Identifier | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.2 |
| `D0` | Key Identifier | GPC_SPE_182-Amendment-K-SCP04-v1.0.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.1 |
| `D1` | GSM/3GPP/3GPP2 - SMS-PP Download | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `D1` | DNS-From-ME Retry Policy | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11 |
| `D1` | '00', '01' Value | GPD_SPE_013-Secure-Element-Access-Control | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.2 |
| `D1` | SMS-PP download tag | ME to UICC (BER-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `D2` | GSM/3GPP/3GPP2 - Cell Broadcast Download | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `D2` | DNS IP Retry Policy | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11 |
| `D2` | Key Version Number | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.2 |
| `D2` | Key Version Number | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.2 |
| `D2` | Key Version Number | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.2 |
| `D2` | Key Version Number | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.2 |
| `D2` | Key Version Number | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2.2.3.2 |
| `D2` | Key Version Number | GPC_SPE_182-Amendment-K-SCP04-v1.0.2 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 7.1 |
| `D2` | Cell Broadcast download tag | ME to UICC (BER-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `D3` | Menu Selection | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `D3` | Current Security Level | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `D3` | Current Security Level | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `D3` | Current Security Level | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `D3` | Current Security Level | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `D3` | Current Security Level | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `D4` | Call Control | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `D4` | Ciphered Load File Data Block | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.6.2.3 |
| `D4` | Ciphered Load File Data Block | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.6.2.3 |
| `D4` | Ciphered Load File Data Block | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.6.2.3 |
| `D4` | Ciphered Load File Data Block | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.6.2.3 |
| `D5` | GSM/3GPP/3GPP2 - MO Short Message control | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `D5` | Key Version Number of the Default Secure Channel Key Set | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `D5` | MO Short message control tag | ME to UICC (BER-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `D6` | Event Download | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `D6` | RAS FQDN | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.7 |
| `D7` | Timer Expiration | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `D7` | Volatile | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `D7` | Volatile | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `D8` | Reserved for intra-UICC communication and not visible on the card interface | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `D8` | Non volatile | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `D8` | Non volatile | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `D9` | 3GPP/3GPP2 - USSD Download | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `D9` | Restrict Parameter (see Table 11-53) | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `D9` | Restrict Parameter (see Table 11-53) | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `D9` | Restrict Parameter (see Table 11-53) | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `D9` | Restrict Parameter (see Table 11-53) | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `D9` | Restrict Parameter (see Table 11-53) | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `D9` | USSD download tag | ME to UICC (BER-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `DA` | EventEntries | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 6.6.2 |
| `DA` | EventEntries | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 6.6.2 |
| `DA` | CheckProgressOk | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 6.6.2 |
| `DA` | EimPackageErrorWithCid | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 6.4.1.8 |
| `DA` | MMS Transfer status | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `DA` | NFCAccessRule | GPD_SPE_013-Secure-Element-Access-Control | GlobalPlatform BER-TLV | `(document, tag)` | GPD_SPE_013-Secure-Element-Access-Control | 7.4 |
| `DA` | EPC | 23003-k00 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 23003-k00 | 1.1.1 |
| `DB` | MMS notification download | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `DC` | Terminal application tag | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `DD` | 3GPP - Geographical Location Reporting tag | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `DD` | Load File Data Block Parameters | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `DD` | Load File Data Block Parameters | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `DD` | Load File Data Block Parameters | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `DD` | Load File Data Block Parameters | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `DD` | Load File Data Block Parameters | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `DD` | Geographical Location Reporting tag | ME to UICC (BER-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `DE` | Envelope Container | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `DE` | Tag Value | 31102-j50 | 3GPP / ETSI card-layer | `(document, clause, tag)` | 31102-j50 | 4.2.66 |
| `DF` | 3GPP - ProSe Report tag | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `DF` | ProSe Report tag | ME to UICC (BER-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `E0` | ReplaceSessionKeysRequest | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.1 |
| `E0` | ReplaceSessionKeysRequest | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.1 |
| `E0` | ReplaceSessionKeysRequest | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.1 |
| `E0` | 3GPP – 5G ProSe Report tag | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `E0` | Key Information Template | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `E0` | Key Information Template | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `E0` | Key Information Template | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `E0` | Key Information Template | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `E0` | Key Information Template | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `E0` | 5G ProSe Report tag | ME to UICC (BER-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `E1` | ProfileDownloadTriggerResult | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `E1` | ProfileDownloadTriggerResult | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 3.8.4 |
| `E1` | Reserved for 3GPP (for future usage) | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `E1` | Signature Algorithm | GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 5.2.2 |
| `E1` | Individual Key Information of a specific key of the currently selected Security Do | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `E1` | Reserved for 3GPP (for future usage) | ME to UICC (BER-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `E2` | Reserved for 3GPP (for future usage) | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `E2` | DAP Block | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.6.2.3 |
| `E2` | DAP Block | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.6.2.3 |
| `E2` | DAP Block | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.6.2.3 |
| `E2` | DAP Block | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.6.2.3 |
| `E2` | DAP Block | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.6.2.3 |
| `E2` | Reserved for 3GPP (for future usage) | ME to UICC (BER-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `E3` | ProfileInfoListResponse | SGP.22 v2.2.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.2.2 | 5.7.15 |
| `E3` | ProfileInfoListResponse | SGP.22 v2.7 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v2.7 | 5.7.15 |
| `E3` | ProfileInfoListResponse | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.7.15 |
| `E3` | IpaCapabilities | SGP.32 v1.2 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.2 | 3.5.2.3 |
| `E3` | IpaCapabilities | SGP.32 v1.3 | eSIM RSP ASN.1 | `(module, tag)` | SGP.32 v1.3 | 4.4 |
| `E3` | Reserved for 3GPP (for future usage) | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `E3` | GlobalPlatform Registry related data | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `E3` | GlobalPlatform Registry related data | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `E3` | GlobalPlatform Registry related data | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `E3` | GlobalPlatform Registry related data | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `E3` | GlobalPlatform Registry related data | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.4.3.1 |
| `E3` | GlobalPlatform Registry related data | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 8.2.3 |
| `E3` | Reserved for 3GPP (for future usage) | ME to UICC (BER-TLV) | 3GPP USAT (TS 31.111) | `(tag, section)` | 3GPP TS 31.111 | 9 |
| `E4` | VerifyProfileRecoveryResponse | SGP.22 v3.1 | eSIM RSP ASN.1 | `(module, tag)` | SGP.22 v3.1 | 5.11.3 |
| `E4` | Reserved for GSMA (direction terminal to UICC) | Card application toolkit templates | ETSI TS 101 220 allocator | `(type, context, tag)` | ETSI TS 101 220 | 7.2 |
| `E4` | Device-Interface-Version-DO Value Version of the Device Interface implemented by the ACE. | GPD_SPE_013-Secure-Element-Access-Control | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.3 |
| `E5` | Device-Interface-Version-DO Value Version of the Device Interface implemented by the ARA-M. | GPD_SPE_013-Secure-Element-Access-Control | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.3 |
| `E6` | Version Value Version of the Device Interface implemented by the ARA-M or the ACE. | GPD_SPE_013-Secure-Element-Access-Control | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.3 |
| `E7` | offset / length 3 bytes: 2 bytes offset, 1 byte length The offset and length specify the data block of access rule data… | GPD_SPE_013-Secure-Element-Access-Control | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 6.3 |
| `EA` | TS 102 226 specific template | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `EA` | TS 102 226 specific template | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `EA` | [TS 102 226] specific template | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `EA` | [TS 102 226] specific template | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `EA` | [TS 102 226] specific template | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `EF` | System Specific Parameters Tag Length Value Description | GPC_SPE_025-Amendment-C-Contactless-Services | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.2 |
| `EF` | System Specific Parameters | GPC_SPE_034-Card-Spec-v2.2.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `EF` | System Specific Parameters | GPC_SPE_034-Card-Spec-v2.2.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `EF` | System Specific Parameters | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `EF` | System Specific Parameters | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `EF` | System Specific Parameters | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.5.2.3.7 |
| `EF` | System specific parameters | GPC_SPE_093-Amendment-F-SCP11 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 8.2.3 |
| `F7` | RAS IP List Cache | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11 |
| `F9` | DNS IP List Cache | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11 |
| `FA` | DNS Connection Parameters | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.7 |
| `FB` | Fallback RAS IP List | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11 |
| `FC` | Fallback DNS IP List | GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 3.11 |
| `FF21` | Extended Card Resources Information available for Card Content Management, as | GPC_SPE_034-Card-Spec-v2.3.0 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `FF21` | Extended Card Resources Information available for Card Content Management, as | GPC_SPE_034-Card-Spec-v2.3.1 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |
| `FF21` | Extended Card Resources Information available for Card Content Management, as | GPC_SPE_034-Card-Spec-v2.4 | GlobalPlatform BER-TLV | `(document, tag)` | GlobalPlatform | 11.3.2.1 |

---

## Lookup keys

- spaced and unspaced hex: `BF36`, `BF 36` and `bf36`
- quoted ASN.1 form: `Tag 'BF36'`
- ASN.1 tag number: `[54]` is the same tag as `BF36`
- file IDs with their ADF: `6F07` under `ADF_USIM`, not bare
- GlobalPlatform tags with their document: `E1` in the Card Spec, not bare

## Stats

- total readings: 1,267
- namespaces: 6
