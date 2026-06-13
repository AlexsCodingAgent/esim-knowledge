---
title: "eUICC Test Architecture: Readers, Scripts, and GSMA Tools"
description: "Explains the eUICC test architecture : ISO 7816-4 contact interfaces, APDU-level command chaining, five GSMA simulator types, USB CCID for embedded eUICCs, and logical channel separation rules."
date: 2026-06-05
---

# eUICC Test Architecture: Readers, Scripts, and GSMA Tools

**[eUICC.tech]({{ site.baseurl }}/) > [SGP.23-1 eUICC Testing]({{ site.baseurl }}/docs/articles/sgp23-1/) > eUICC Test Architecture: Readers, Scripts, and GSMA Tools**

> **Why this matters:** Testing an eUICC isn't like testing a web API: you can't just send HTTP requests and check JSON responses. The test architecture must handle physical chip interfaces (ISO 7816-4 contacts, USB CCID), APDU-level command chaining, logical channel management, and a parallel test PKI that keeps certification testing isolated from production infrastructure. Understanding this architecture reveals what test tool vendors must build and what eUICC manufacturers must provide.

> **Key takeaways:**
> - eUICCs are tested via their contact interface using ISO/IEC 7816-4 APDUs, with all ES10 commands wrapped in STORE DATA sent to the ISD-R
> - Five simulators (S_Device, S_LPAd, S_SM-DP+, S_SM-DS, S_MNO) are implemented by test tool providers: not by the GSMA
> - Integrated eUICCs (SoC-embedded) use a USB CCID test interface operating in card reader mode per Annex J
> - Test environments are TE_eUICC (removable eUICC with PC/SC reader) and TE_Integrated eUICC (USB CCID)
> - The eUICC must be provided in a known initial state (Annex G) with test certificates, test keys, and specific profile configurations pre-loaded
> - Logical channels are strictly separated: ES10 commands on a dedicated logical channel to ISD-R; other APDUs on the basic logical channel

Every SGP.23-1 test case executes within a carefully specified test environment. Unlike the parent SGP.23 which defines twelve+ environments for different IUT types, SGP.23-1 needs only two: but both must handle the physical realities of communicating with a secure element.

---

## The Two Test Environments

### TE_eUICC: Removable eUICC

The standard test environment for eUICCs in removable form factors (Java Card, one of the form factors specified in ETSI TS 102 221):

```
S_Device, S_LPAd PC/SC reader or eUICC
(S_MNO, S_SM-DP+, S_SM-DS) ──────► custom hardware ──────► (IUT)
 ↑ (ISO 7816-4) ↑
 │ │
 └── ES6, ES8+, ES10x tunnelled through APDUs ────────────┘
```

Key requirements:
- The eUICC is physically inserted into a PC/SC reader or connected via custom hardware
- The Device Simulator (S_Device) sends ISO/IEC 7816-4 commands including RESET, SELECT_MF, TERMINAL_CAPABILITY, and TERMINAL_PROFILE
- ES6, ES8+, and ES10x commands are tunnelled through the contact interface as STORE DATA APDUs
- The EUM (eUICC Manufacturer) must provide products compliant with Annex G.2 initial states

### TE_Integrated eUICC: SoC-Embedded eUICC

For eUICCs embedded in System-on-Chip designs where no physical UICC terminal exists:

```
S_Device, S_LPAd PC/SC USB Integrated eUICC Integrated
 CCID Test Interface eUICC
S_MNO, S_SM-DP+, S_SM-DS ──► ──────────► (e.g. USB/Bluetooth) ───► (IUT)
 Card Reader Mode
```

Key requirements (Annex J):
- The integrated eUICC must provide a USB CCID test interface operating in **card reader mode**
- Must support all standard CCID messages: `PC_to_RDR_IccPowerOn`, `PC_to_RDR_XfrBlock`, `PC_to_RDR_T0APDU`, `PC_to_RDR_Abort`, etc.
- If USB is physically unavailable, an adapter (e.g., Bluetooth-to-USB CCID) must be provided
- The manufacturer must ensure no other SoC subsystems interfere during testing

---

## The Five Simulators

SGP.23-1 defines five simulators: fewer than SGP.23's nine, since there's no LDS, LUI, End User, CLIENT, or SERVER simulation needed:

| Simulator | Role | Key Responsibilities |
|-----------|------|---------------------|
| **S_Device** | Device Simulator | Sends ISO/IEC 7816-4 APDUs; handles RESET, SELECT, terminal capability/profile setup; supports MEP LSI indication (MANAGE LSI or T=1 NAD byte) |
| **S_LPAd** | LPAd Simulator | Wraps ES10x commands in STORE DATA APDUs; manages logical channel open/close; executes ISD-R selection |
| **S_SM-DP+** | SM-DP+ Simulator | Generates Bound Profile Packages (BPPs); performs mutual authentication; creates test profiles with known keys |
| **S_SM-DS** | SM-DS Simulator | Provides SM-DS services for event-related testing |
| **S_MNO** | MNO Simulator | Sends OTA commands for ES6 testing; generates SMS-PP delivery with SCP80 security |

All simulators are the responsibility of **test tool providers** : not the GSMA. The test tool must handle DER encoding/decoding of ASN.1 structures, APDU command/response parsing, TLS session management, and profile package generation.

---

## Logical Channel Architecture

A critical architectural detail: the eUICC's logical channel usage is strictly defined:

- **Basic Logical Channel** : Used for all non-ES10 APDUs: SELECT_MF, TERMINAL_CAPABILITY, TERMINAL_PROFILE, MANAGE_CHANNEL operations, and Annex D.4 APDUs
- **Dedicated Logical Channel** : Opened by S_LPAd via `MANAGE_CHANNEL_OPEN` and used exclusively for ES10 commands. All ES10 functions (GetEUICCInfo, PrepareDownload, LoadBoundProfilePackage, GetProfilesInfo, EnableProfile, etc.) are wrapped in STORE DATA APDUs and sent on this dedicated channel
- **ISD-R Selection** : After opening the logical channel, the S_LPAd sends `MTD_SELECT(#ISD_R_AID)` to select the ISD-R. The response contains proprietary data specific to the test sequence

For MEP (Multiple Enabled Profiles), the Device Simulator must support both LSI indication options: MANAGE LSI (Select LSI) and T=1 using NAD byte: and use whichever the EUM declares in `IUT_EUICC_MULTIPLEXING_LSI_INDICATION`.

---

## Test Script Execution

Test cases in SGP.23-1 follow a rigorously structured format:

1. **General Initial Conditions** : The eUICC's starting state (which profiles are loaded, enabled/disabled, which certificates are present)
2. **Test Sequence** : Numbered steps specifying direction (`S_LPAd → eUICC`, `S_Device → eUICC`), the command to send, and the exact expected response
3. **Expected Results** : Precise response data patterns and status words (typically `SW=0x9000` for success)

Commands use three notation systems:
- **`#CONSTANT_NAME`** : Fixed values from Annex A (e.g., `#ISD_R_AID`, `#MATCHING_ID_1`, `#CONFIRMATION_CODE1`)
- **`<VARIABLE_NAME>`** : Dynamic values generated during test execution (e.g., `<CHANNEL_NUMBER>`, `<BPP_SEG_INIT>`, `<EUICC_SIGNATURE2>`)
- **`#IUT_SETTING_NAME`** : Vendor-provided implementation details (e.g., `#IUT_MEP_LSI_OPTIONS`, `#IUT_EUICC_MULTIPLEXING_LSI_INDICATION`)

Common procedures are abstracted into reusable macros: `PROC_OPEN_LOGICAL_CHANNEL_AND_SELECT_ISDR`, `PROC_EUICC_CONFIGURE_LSIS_FOR_MEP`, `PROC_MEP_LSI_MULTIPLEXING`, etc.

---

## Initial States and Test Data

The eUICC manufacturer must provide products in known initial states (Annex G.2):

- **Common Initial States** : PROFILE_OPERATIONAL1 is loaded and, unless specified, in Disabled state; test certificates and keys are pre-loaded
- **NIST P-256 configuration** : For eUICCs supporting the NIST curve with specific CI public key and EUM certificate
- **BrainpoolP256r1 configuration** : For eUICCs supporting Brainpool with appropriate curve-specific keys
- **MEP configurations** : RAT (Rules Authorisation Table) configured for SEP (Single Enabled Profile) or MEP modes
- **Clean-up procedure** : A defined process to reset the eUICC to its initial state between test runs

Test profiles (Annex E) use known ICCIDs (`89019990001234567893`), known USIM AIDs, and known file structures: enabling repeatable, deterministic testing.

---

## Summary

- Two test environments: TE_eUICC (removable, ISO 7816-4 via PC/SC reader) and TE_Integrated eUICC (SoC-embedded, USB CCID in card reader mode)
- Five simulators (S_Device, S_LPAd, S_SM-DP+, S_SM-DS, S_MNO) implemented by test tool vendors
- Strict logical channel separation: ES10 commands on a dedicated channel to ISD-R; all other APDUs on the basic channel
- Integrated eUICCs must implement Annex J's USB CCID interface: or provide a Bluetooth/USB adapter if USB is unavailable
- Test cases use a three-tier notation system (#constants, <variables>, #IUT_settings) with reusable procedure macros
- eUICC manufacturers must deliver products in known initial states (Annex G) pre-loaded with test certificates, keys, and profiles

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp23-1/32-sgp23-1-overview">SGP.23-1 Overview: Testing the eUICC Itself</a> · <a href="{{ site.baseurl }}/"> Home</a>

Next: <a href="{{ site.baseurl }}/docs/articles/sgp23-1/34-sgp23-1-test-cases">Key eUICC Test Cases: ISD-R, ECASD, and Profile Lifecycle</a> →

</div>

---

*Based on GSMA SGP.23-1 v3.1.3 (27 January 2025) : RSP Test Specification for the eUICC, Section 3, Annexes A, E, F, G, J*


---

← Previous: [SGP.23-1 Overview: Testing the eUICC Itself](32-sgp23-1-overview) | [Section Index](index) | Next: [Key eUICC Test Cases: ISD-R, ECASD, and Profile Lifecycle](34-sgp23-1-test-cases) →
