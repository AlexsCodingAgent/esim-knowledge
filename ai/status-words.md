---
layout: default
title: "Status Words, Condensed — Machine-Readable Table"
description: "Condensed single-table reference of eUICC/SIM status words (SW1 SW2) with eUICC-specific meanings for SGP.22 and SGP.32. One row per status word, tab-separated values embedded for LLM extraction."
---

# 🔢 Status Words — Condensed Table

**Machine-readable version.** One row per status word. For prose, worked
examples and debugging guidance, see the
[full Status Word Reference]({{ site.baseurl }}/docs/status-words).

**Scope:** GSMA SGP.22 (consumer eSIM) · SGP.32 (IoT eSIM) · GlobalPlatform
Card Specification v2.4 · ISO/IEC 7816-4.
**Format:** status word | type | name | eUICC meaning | source | retryable.

---

## Complete table

| SW | Type | Name | Meaning in eUICC / eSIM context | Source | Retry |
|---|---|---|---|---|---|
| `90 00` | success | Success | Command executed successfully. The only success code for a completed command. | ISO 7816-4 | — |
| `91 XX` | success | More data / proactive pending | `XX` bytes of response data are waiting — fetch with GET RESPONSE. Also returned in SGP.22 when a proactive command is pending. NOT an error. | ISO 7816-4, SGP.22 | n/a |
| `62 00` | warning | Logical Channel already closed | The logical channel was already closed. | GP v2.4 §11 | no |
| `62 83` | warning | CARD_LOCKED | Card Life Cycle State is CARD_LOCKED. | GP v2.4 §11 | no |
| `63 10` | warning | More data available | Additional data available — reissue GET STATUS with get-next-occurrence. | GP v2.4 §11 | yes |
| `64 00` | error | No specific diagnosis | Execution error, no further detail. | GP v2.4 §11.1.3 | no |
| `65 81` | error | Memory failure | Memory failure while writing. | GP v2.4 §11 | no |
| `67 00` | error | Wrong length in Lc | `Lc` does not match the length of data sent. | GP v2.4 §11.1.3 | no |
| `68 81` | error | Logical channel not supported / not active | Requested logical channel is unavailable. | GP v2.4 §11.1.3 | no |
| `68 82` | error | Secure messaging not supported | Secure messaging is not supported for this operation. | GP v2.4 §11 | no |
| `69 82` | error | Security status not satisfied | Authentication or secure messaging NOT established. A session problem — complete mutual authentication first. Also used by PUT KEY for Invalid Key Check Value. | GP v2.4 §11.1.3 | no |
| `69 85` | error | Conditions of use not satisfied | Command is legal and caller is authenticated, but object state or a Profile Policy Rule forbids it. In SGP.22: Profile not in expected state (e.g. enabling an already-enabled Profile), PPR blocks the operation, or `enterpriseConfigurationNotAllowed`. | GP v2.4, SGP.22 v2.2.2/v2.7/v3.1 | no |
| `6A 80` | error | Incorrect values in command data | Command data failed validation. SGP.22 v3.1 adds `deleteNotAllowed`. SGP.32 returns it when the target Profile has `ecallIndication` TRUE. | GP v2.4, SGP.22 v3.1, SGP.32 v1.3 | no |
| `6A 81` | error | Function not supported | Function not supported (e.g. CARD_LOCKED). SGP.22 v3.1 adds `pprUpdateInvalidSetting` and `invalidRpmConfiguration` — a Profile Policy Rules update carried an invalid setting. | GP v2.4, SGP.22 v3.1 | no |
| `6A 82` | error | **Profile not found** | The Profile (by ICCID) does not exist on this eUICC, was already deleted, or belongs to a different eUICC. Generic GP means "Application not found"; in SGP.22 always the Profile. | SGP.22 v2.2.2/v2.7/v3.1 | no |
| `6A 84` | error | Not enough memory space | Insufficient space for the requested operation. | GP v2.4 §11 | no |
| `6A 86` | error | Incorrect P1 P2 | P1/P2 invalid; also returned when command chaining is unsupported or its limit reached. | GP v2.4 §11.1.3 | no |
| `6A 88` | error | Referenced data not found | Referenced data object does not exist. In SGP.22 profile download: a tag or reference in the Bound Profile Package could not be resolved. | GP v2.4, SGP.22 | no |
| `6A 89` | error | **Fallback attribute set** | SGP.32 ONLY. Response to `UpdateMetadataRequest` when `fallbackAllowed` is FALSE but the target Profile already has `fallbackAllowed` TRUE and `fallbackAttribute` TRUE. | SGP.32 v1.3 | no |
| `6D 00` | error | Invalid instruction | The `INS` byte is not supported. | GP v2.4 §11.1.3 | no |
| `6E 00` | error | Invalid class | The `CLA` byte is not supported; must conform to ISO 7816-4. | GP v2.4 §11.1.3 | no |
| `93 00` | error | **CAT is busy** | Card Application Toolkit has a pending proactive command. Cannot execute at present, but further normal commands ARE allowed — retry after the CAT session completes. | SGP.22 v2.2.2/v2.7/v3.1 | **yes** |

---

## SW1 category prefixes

| SW1 | Class | Meaning |
|---|---|---|
| `90` | success | Command executed normally |
| `61` | success | Success, `SW2` = number of response bytes available |
| `62` | warning | Non-volatile memory unchanged |
| `63` | warning | Non-volatile memory changed |
| `64` | error | Execution error, memory unchanged |
| `65` | error | Execution error, memory changed |
| `67` | error | Wrong length |
| `68` | error | CLA function not supported |
| `69` | error | Command not allowed |
| `6A` | error | Wrong parameters P1-P2 |
| `6B` | error | Wrong parameters P1-P2 |
| `6C` | error | Wrong Le (`SW2` = exact length) |
| `6D` | error | Instruction code not supported |
| `6E` | error | Class not supported |
| `6F` | error | No precise diagnosis |
| `93` | error | Application-specific (eUICC: CAT busy) |

---

## Command-to-status-word map

| Command | SW | Meaning |
|---|---|---|
| EnableProfile (ES10c) | `6A 82` | Profile not found |
| EnableProfile (ES10c) | `69 85` | Profile not in disabled state, or blocked by Profile Policy Rules |
| EnableProfile (ES10c) | `93 00` | CAT busy — retry |
| DisableProfile (ES10c) | `6A 82` | Profile not found |
| DisableProfile (ES10c) | `69 85` | Profile not in enabled state, or blocked by Profile Policy Rules |
| DisableProfile (ES10c) | `93 00` | CAT busy — retry |
| DeleteProfile (ES10c) | `6A 80` | `deleteNotAllowed` (SGP.22 v3.1) |
| DeleteProfile (ES10c) | `6A 82` | Profile not found |
| DeleteProfile (ES10c) | `69 85` | Profile not in disabled state, or blocked by Profile Policy Rules |
| LoadBoundProfilePackage (ES10b) | any ≠ `90 00`/`91 XX` | Profile download FAILED |
| LoadBoundProfilePackage (ES10b) | `6A 88` | Reference in Bound Profile Package not resolved |
| LoadBoundProfilePackage (ES10b) | `69 85` | Conditions of use not satisfied; eUICC may reject further ES10 commands |
| UpdateMetadataRequest (SGP.32) | `6A 89` | Fallback attribute set |
| UpdateMetadataRequest (SGP.32) | `6A 80` | Target Profile has `ecallIndication` TRUE |
| CONFIRM ORDER / STORE DATA | `91 XX` | More data or proactive command pending |
| Any authenticated command | `69 82` | Secure messaging not yet established |
| Any command | `6A 86` | Bad P1/P2, or chaining unsupported |

---

## Lookup keys for retrieval

Alternate spellings and query forms that should resolve to this table:

`SW1SW2` · `SW1/SW2` · `status word` · `status bytes` · `APDU status` ·
`APDU response code` · `6A82` · `6A 82` · `6985` · `69 85` · `6A80` · `6A81` ·
`6A88` · `6A89` · `9300` · `69 82` vs `69 85` · `profile not found` ·
`conditions of use not satisfied` · `security status not satisfied` ·
`CAT is busy` · `fallback attribute set` · `deleteNotAllowed` ·
`pprUpdateInvalidSetting` · `eUICC error code` · `ES10 error` ·
`eSIM APDU error` · `profile download failed status`

---

*Source documents: GlobalPlatform Card Specification v2.4 (§11); GSMA SGP.22
v2.2.2, v2.7, v3.1; GSMA SGP.32 v1.3; ISO/IEC 7816-4. Status word meanings are
taken from the specification text, not secondary sources. Where a status word
carries different meanings across versions, each is listed.*
