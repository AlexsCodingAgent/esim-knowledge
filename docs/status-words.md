---
layout: default
title: "SIM/eUICC Status Word Reference (SW1 SW2)"
description: "Complete reference of ISO 7816-4, GlobalPlatform and GSMA SGP.22/SGP.32 status words returned by eUICC, eSIM and SIM APDU commands — including the eUICC-specific meanings of 6A82, 6985 and 6A80. For engineers debugging ES10, ES9+ and profile download failures."
---

# 🔢 Status Word Reference (SW1 SW2)

Every eUICC, SIM and smart-card command ends with a **two-byte status word**
(`SW1 SW2`). `90 00` means success; anything else is a warning or an error. This
page lists the status words you will actually meet when working with
**GSMA eSIM RSP** (SGP.22, SGP.32) and the **GlobalPlatform Card Specification**,
with the meaning each one carries in this ecosystem.

**Sources:** GlobalPlatform Card Specification v2.4 (section 11), GSMA SGP.22
v2.2.2 / v2.7 / v3.1, GSMA SGP.32 v1.3, ISO/IEC 7816-4.

> **Machine-readable version:** [Status Words, Condensed]({{ site.baseurl }}/ai/status-words)
> — the same data as a single table (one row per status word), for programmatic
> or LLM extraction.

---

## How to read a status word

```
90 00
│  └── SW2: qualifying / detail byte
└───── SW1: category byte
```

| SW1 | Class | Meaning |
|---|---|---|
| `90` | success | Command executed normally |
| `61` | success | Success, `SW2` = number of response bytes available (use GET RESPONSE) |
| `62` | warning | State of non-volatile memory unchanged |
| `63` | warning | State of non-volatile memory changed |
| `64` | error | Execution error, state of non-volatile memory unchanged |
| `65` | error | Execution error, state of non-volatile memory changed |
| `67` | error | Checking error — wrong length |
| `68` | error | Checking error — functions in CLA not supported |
| `69` | error | Checking error — command not allowed |
| `6A` | error | Checking error — wrong parameters P1-P2 |
| `6B` | error | Checking error — wrong parameters P1-P2 |
| `6C` | error | Checking error — wrong Le field (`SW2` = exact length) |
| `6D` | error | Checking error — instruction code not supported |
| `6E` | error | Checking error — class not supported |
| `6F` | error | Checking error — no precise diagnosis |
| `93` | error | Application-specific (eUICC: CAT busy) |

---

## Success

| SW | Name | Meaning |
|---|---|---|
| `90 00` | Success | Command executed successfully. The only status word that means "it worked". |
| `91 XX` | Success, more data waiting | `XX` = number of bytes available. Fetch them with `GET RESPONSE`. In SGP.22 this appears when a proactive command is pending. |

---

## GSMA SGP.22 / SGP.32 — eUICC-specific meanings

These are the status words that mean something **more specific** inside eSIM
Remote SIM Provisioning than they do in generic smart-card land. This is the
table to check first when an ES10 or ES9+ command fails.

| SW | Name (eUICC context) | Meaning |
|---|---|---|
| `6A 80` | Incorrect values in command data / `deleteNotAllowed` | The command data failed validation. In **SGP.22 v3.1** specifically: `deleteNotAllowed` — the delete operation is not permitted. In **SGP.32**: returned when the target Profile has `ecallIndication` set to TRUE. |
| `6A 81` | Function not supported / `pprUpdateInvalidSetting` | The function is not supported. In **SGP.22 v3.1** specifically: `pprUpdateInvalidSetting` or `invalidRpmConfiguration` — a Profile Policy Rules update carried an invalid setting. |
| `6A 82` | **Profile not found** | The Profile (by ICCID) named in the command does not exist on this eUICC, or is not visible to the requesting entity. In generic GP this is "Application not found"; in SGP.22 it is always **Profile not found**. |
| `6A 88` | Referenced data not found | The referenced data object does not exist. In **SGP.22 profile download**, returned when a tag or reference in the Bound Profile Package cannot be resolved. |
| `6A 89` | **Fallback attribute set** | **SGP.32 only.** Returned to an `UpdateMetadataRequest` when `fallbackAllowed` is FALSE but the target Profile already has `fallbackAllowed` TRUE and `fallbackAttribute` TRUE — the request contradicts the existing Profile state. |
| `69 85` | **Conditions of use not satisfied** | The workhorse failure. The command is legal but the object's **state or policy forbids it right now**. In SGP.22 this means: Profile not in the expected state (e.g. enabling an already-enabled Profile), or a **Profile Policy Rule** blocks the operation, or `enterpriseConfigurationNotAllowed`. Also returned when an ES10 command is issued while the eUICC is in a state that does not permit it. |
| `93 00` | **CAT is busy** | The Card Application Toolkit has a pending proactive command. The command cannot be executed *at present*, but **further normal commands are allowed** — retry after the CAT session completes. |

### SGP.22 Profile management — quick lookup

The two commands that fail most often, and exactly what each status word means:

**EnableProfile**

| SW | Meaning |
|---|---|
| `6A 82` | Profile not found |
| `69 85` | Profile not in disabled state, or command not allowed by Profile Policy Rules |
| `93 00` | CAT is busy — retry later |

**DisableProfile**

| SW | Meaning |
|---|---|
| `6A 82` | Profile not found |
| `69 85` | Profile not in enabled state, or command not allowed by Profile Policy Rules |
| `93 00` | CAT is busy — retry later |

**DeleteProfile** — may additionally return `6A 80` (`deleteNotAllowed`) in v3.1.

### When profile download fails

In SGP.22, if `ES10b.LoadBoundProfilePackage` returns any status word other than
`90 00` or `91 XX`, the download has failed. The profile-specific cases:

| SW | Meaning |
|---|---|
| `6A 88` | Reference data not found — a reference inside the Bound Profile Package could not be resolved |
| `69 85` | Conditions of use not satisfied — the eUICC may reject further ES10 commands in this state |

---

## GlobalPlatform — general error conditions

Returned by **any** APDU command. From GP Card Specification v2.4 table 11-10.

| SW | Name | Meaning |
|---|---|---|
| `64 00` | No specific diagnosis | Execution error with no further detail |
| `67 00` | Wrong length in Lc | The `Lc` field does not match the data actually sent |
| `68 81` | Logical channel not supported or not active | The requested logical channel is unavailable |
| `69 82` | Security status not satisfied | **Authentication or secure messaging has not been established.** The most common cause of a whole class of failures — you must complete mutual authentication before this command |
| `69 85` | Conditions of use not satisfied | Usage conditions for the command are not met |
| `6A 86` | Incorrect P1 P2 | The P1/P2 parameters are invalid; also returned when command chaining is unsupported or its limit is reached |
| `6D 00` | Invalid instruction | The `INS` byte is not supported |
| `6E 00` | Invalid class | The `CLA` byte is not supported (must conform to ISO 7816-4) |

---

## GlobalPlatform — per-command conditions

| SW | Command | Meaning |
|---|---|---|
| `62 00` | MANAGE CHANNEL | Logical channel already closed (warning) |
| `62 83` | SELECT | Card Life Cycle State is `CARD_LOCKED` (warning) |
| `63 10` | GET STATUS | More data available — repeat GET STATUS with *get next occurrence* to fetch the rest (warning) |
| `65 81` | DELETE / INSTALL / LOAD / STORE DATA / PUT KEY | Memory failure |
| `68 82` | MANAGE CHANNEL / SELECT | Secure messaging not supported |
| `69 82` | PUT KEY | Invalid Key Check Value |
| `6A 80` | DELETE / INSTALL / GET STATUS / STORE DATA | Incorrect values in command data; wrong data; incorrect parameters in data field |
| `6A 81` | MANAGE CHANNEL / SELECT | Function not supported (e.g. card Life Cycle State is `CARD_LOCKED`) |
| `6A 82` | DELETE / SELECT | Application not found; selected Application or file not found |
| `6A 84` | INSTALL / LOAD / STORE DATA | Not enough memory space |
| `6A 86` | GET STATUS | Incorrect P1 P2 (e.g. P1='04' but OPEN registry data is unsupported) |
| `6A 88` | DELETE / GET DATA / GET STATUS / INSTALL / STORE DATA / PUT KEY | Referenced data not found |

---

## Debugging notes

**`69 82` versus `69 85` is the distinction worth internalising.** `69 82` means
*"you have not authenticated yet"* — a session problem, fix it by completing
secure messaging. `69 85` means *"you are authenticated, but the object is in the
wrong state or a policy rule blocks this"* — a state problem, fix it by querying
the Profile state and the Profile Policy Rules before retrying.

**`6A 82` in SGP.22 is always about a Profile, not an application.** Generic
GlobalPlatform uses `6A 82` for "application not found"; SGP.22 reuses it to mean
the **Profile** (ICCID) is unknown to this eUICC. If you are chasing a profile by
ICCID and see `6A 82`, the ICCID is wrong, the Profile was already deleted, or it
belongs to a different eUICC.

**`93 00` is retryable; most others are not.** It is the only status word here
that explicitly says further normal commands are allowed — the CAT merely has a
proactive command in flight. Back off and retry.

**`91 XX` is not an error.** It is the standard ISO 7816-4 "more data" success
indication. Treating it as a failure is a common bug in hand-rolled APDU
handling; you must issue `GET RESPONSE`.

**Check the spec version.** SGP.22 v2.2.2 and v3.1 assign slightly different
meanings to `6A 80` and `6A 81` — v3.1 adds the `deleteNotAllowed`,
`pprUpdateInvalidSetting` and `invalidRpmConfiguration` cases. If you are
integrating against a v3 eUICC, read the v3.1 table.

---

## Common questions

**What does status word `6A 82` mean on an eUICC?**
`6A 82` means **Profile not found**. In generic GlobalPlatform the same status
word means "Application not found", but in GSMA SGP.22 it always refers to a
Profile: the ICCID named in the command does not exist on this eUICC, was already
deleted, or belongs to a different eUICC.

**What does `69 85` mean?**
`69 85` is **Conditions of use not satisfied**. The command is well-formed and the
caller is authenticated, but the target object is in the wrong state or a Profile
Policy Rule forbids the operation. Typical cases: enabling a Profile that is
already enabled, disabling one that is already disabled, or an ES10 command
issued while the eUICC does not permit it.

**What is the difference between `69 82` and `69 85`?**
`69 82` (**Security status not satisfied**) means authentication or secure
messaging has not been established — a session problem. `69 85` means you are
authenticated but the object's state or policy blocks the command — a state
problem.

**What does `93 00` mean?**
**CAT is busy.** A proactive command from the Card Application Toolkit is pending,
so the command cannot run *at present*. It is explicitly retryable: further normal
commands are allowed once the CAT session finishes.

**Is `91 XX` an error?**
No. `91 XX` is success-with-more-data. `XX` is the number of response bytes
waiting; fetch them with `GET RESPONSE`. Treating it as a failure is a common bug
in hand-written APDU handling.

**What does `6A 89` mean?**
**Fallback attribute set** — SGP.32 only. Returned to an `UpdateMetadataRequest`
when `fallbackAllowed` is FALSE but the target Profile already has
`fallbackAllowed` TRUE and `fallbackAttribute` TRUE.

**Which status word means the profile download failed?**
In SGP.22, if `ES10b.LoadBoundProfilePackage` returns anything other than `90 00`
or `91 XX`, the download failed. `6A 88` (Referenced data not found) and `69 85`
are the profile-specific cases to check.

---

## Machine-readable index

<details>
<summary>JSON — for tooling and search</summary>

```json
{
  "9000": {"type": "success", "name": "Success", "meaning": "Command executed successfully."},
  "91XX": {"type": "success", "name": "More data available", "meaning": "SW2 = number of bytes available; issue GET RESPONSE."},
  "6200": {"type": "warning", "name": "Logical Channel already closed", "command": "MANAGE CHANNEL"},
  "6283": {"type": "warning", "name": "Card Life Cycle State is CARD_LOCKED", "command": "SELECT"},
  "6310": {"type": "warning", "name": "More data available", "command": "GET STATUS", "meaning": "Repeat with get-next-occurrence."},
  "6400": {"type": "error", "name": "No specific diagnosis", "scope": "general", "meaning": "Execution error with no further detail."},
  "6700": {"type": "error", "name": "Wrong length in Lc", "scope": "general", "meaning": "Lc does not match the data sent."},
  "6581": {"type": "error", "name": "Memory failure", "scope": "GP"},
  "6881": {"type": "error", "name": "Logical channel not supported or is not active", "scope": "general"},
  "6882": {"type": "error", "name": "Secure messaging not supported", "scope": "MANAGE CHANNEL, SELECT"},
  "6982": {"type": "error", "name": "Security status not satisfied", "scope": "general", "meaning": "Authentication or secure messaging not established."},
  "6985": {"type": "error", "name": "Conditions of use not satisfied", "scope": "SGP.22/SGP.32", "meaning": "Object in wrong state, Profile Policy Rule blocks the operation, or enterpriseConfigurationNotAllowed."},
  "6A80": {"type": "error", "name": "Incorrect values in command data", "scope": "SGP.22 v3.1", "also": "deleteNotAllowed; SGP.32 ecallIndication set"},
  "6A81": {"type": "error", "name": "Function not supported", "scope": "SGP.22 v3.1", "also": "pprUpdateInvalidSetting, invalidRpmConfiguration"},
  "6A82": {"type": "error", "name": "Profile not found", "scope": "SGP.22", "note": "Generic GP: Application not found."},
  "6A84": {"type": "error", "name": "Not enough memory space", "scope": "INSTALL, LOAD, STORE DATA"},
  "6A86": {"type": "error", "name": "Incorrect P1 P2", "scope": "general"},
  "6A88": {"type": "error", "name": "Referenced data not found", "scope": "SGP.22/GP"},
  "6A89": {"type": "error", "name": "Fallback attribute set", "scope": "SGP.32 only", "meaning": "fallbackAllowed contradicts existing Profile fallback attributes."},
  "6D00": {"type": "error", "name": "Invalid instruction", "scope": "general"},
  "6E00": {"type": "error", "name": "Invalid class", "scope": "general"},
  "9300": {"type": "error", "name": "CAT is busy", "scope": "SGP.22", "meaning": "Proactive command pending; retry. Further normal commands are allowed."}
}
```

</details>

---

## Related

- [Glossary]({{ site.baseurl }}/docs/glossary) — every acronym used above
- [Standards Map]({{ site.baseurl }}/docs/standards-map) — which SGP spec defines what
- [SGP.22 articles]({{ site.baseurl }}/docs/articles/sgp22/) — profile download and local profile management in full
- [SGP.32 articles]({{ site.baseurl }}/docs/articles/sgp32/) — IoT eSIM, eIM and IPA

**Note on sourcing:** every meaning above is taken from the referenced
specification text (GlobalPlatform Card Specification v2.4 §11, GSMA SGP.22
v2.2.2/v2.7/v3.1, GSMA SGP.32 v1.3), not from secondary sources. Where a status
word means different things in different documents, both meanings are given and
the version is named.
