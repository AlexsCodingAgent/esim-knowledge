---
title: "SGP.22 v2.7 — LPAe: The In-eUICC Local Profile Assistant"
date: 2026-06-07
---

# SGP.22 v2.7 — LPAe: The In-eUICC Local Profile Assistant

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.22 Consumer RSP]({{ site.baseurl }}/docs/articles/sgp22/) > LPAe: The In-eUICC Local Profile Assistant**

> **💡 Why this matters:** The LPAe changes everything about device design for eSIM. When the profile management logic lives inside the eUICC itself rather than on the host OS, companion devices like smartwatches can operate independently without needing a fully-fledged LPA application on the host. Understanding LPAe is essential for anyone building IoT, wearable, or headless eSIM devices.

> **Key takeaways:**
> - The LPA can live in the Device (**LPAd**) or in the eUICC (**LPAe**); both architectures are valid and can coexist
> - LPAe sub-components mirror LPAd: **LDSe** (discovery), **LPDe** (download), **LUIe** (user interface)
> - LUIe has two implementation options: **CAT Toolkit** (5.11.1) or **Smart Card Web Server / SCWS** (5.11.2)
> - **LPA Services** (2.4.9) are mandatory on every eUICC to support LPAd, even when LPAe is present
> - **ISD-R selection at boot** (5.7.1) is the moment the device decides which LPA mode to activate
> - Device and eUICC can support both LPAd and LPAe simultaneously — an arbitration mechanism selects the active LPA

---

The SGP.22 specification defines two fundamentally different places where the Local Profile Assistant can execute: *in the Device* (LPAd) or *in the eUICC* (LPAe). While LPAd is what most smartphone users experience — an OS-level app or service that manages eSIM profiles — the LPAe model places everything inside the secure element itself. This article explores the LPAe architecture, how it coexists with LPAd, and what it means for device design.

---

## Two Architectures, One Role

The LPA has three sub-functions that are identical in purpose regardless of where the code runs:

| Sub-function | In Device | In eUICC | Role |
|---|---|---|---|
| Local Discovery Service | **LDSd** | **LDSe** | Polls the SM-DS for pending profiles, manages default SM-DP+ address |
| Local Profile Download | **LPDd** | **LPDe** | Handles ES9+ communication with SM-DP+, transfers BPP segments to eUICC via ES10b |
| Local User Interface | **LUId** | **LUIe** | Renders the end-user experience for profile add/switch/delete |

The specification uses "LPA", "LPD", "LDS", "LUI" without the "d" or "e" suffix when the statement applies regardless of location (section 1.5).

### Architecture Diagrams

The LPAd architecture shows the three LPA components sitting inside the Device, communicating with the eUICC over **ES10a**, **ES10b**, and **ES10c** (figure 1, section 2.1). The eUICC contains ECASD, ISD-R, ISD-Ps, and the Telecom Framework — but no LPA logic.

The LPAe architecture (figure 2, section 2.1) moves the LPA components *inside* the eUICC. The Device becomes a conduit: it still provides IP connectivity (the LPAe uses **BIP over TCP** to reach SM-DP+ and SM-DS over HTTPS), and it still renders the UI (via CAT or SCWS — more on that below). But the decision-making logic, the profile download orchestration, and the discovery service all execute on the eUICC's Java Card runtime.

Critically, **LPA Services** (section 2.4.9) are mandatory on every compliant eUICC *regardless* of whether LPAe is implemented. These are the low-level access functions that an LPAd needs — the ES10a/b/c command handlers. Without them, an LPAd cannot communicate with the eUICC at all.

---

## LPAe: What Runs Inside the Chip

Section 2.4.8 defines the LPAe concisely:

> The LPAe is a functional element that provides the LPDe, LDSe and LUIe features. These features are similar to the features of an LPAd. LPAe is optional. The technical implementation of LPAe is up to the EUM. For example, the LPAe MAY be a feature of the ISD-R.

This is deliberately open-ended. The eUICC Manufacturer (EUM) decides how to implement LPAe. The most natural approach is to build it as part of the **ISD-R** (Issuer Security Domain — Root), which already orchestrates all profile management on the eUICC. Since the ISD-R is the gatekeeper for ES10 operations, extending it with LPA logic is architecturally clean.

The LPAe's functional requirements mirror LPAd exactly — it must handle profile discovery (polling SM-DS, managing default SM-DP+), profile download (initiating ES9+ sessions, forwarding BPP segments), and user interaction. The difference is that all of this runs in the resource-constrained Java Card environment rather than on a general-purpose OS.

### LDSe: Discovery from Inside the Chip

The LDSe must be able to:
- Store and manage default SM-DP+ and SM-DS addresses
- Initiate HTTPS connections to the SM-DS (via BIP/TCP through the Device)
- Perform the mutual authentication procedure (section 3.1.2) for ES11
- Process Event Records (RSP Server address + EventID) sequentially

Since the LDSe runs inside the eUICC, it has direct access to the eUICC's private key for signing — no need to shuttle challenges back and forth across ES10a like an LPAd must.

### LPDe: Download Orchestration on-Chip

The LPDe performs the same download flow as LPDd:
1. Calls ES9+.InitiateAuthentication to the SM-DP+
2. Calls ES9+.GetBoundProfilePackage to retrieve the BPP
3. Segments the BPP according to section 2.5.5
4. Feeds segments to the eUICC via internal function calls (equivalent to ES10b.LoadBoundProfilePackage)

The key difference: when the LPDe calls "ES10b" functions, these are internal API calls within the eUICC OS — no APDU transport, no serial interface latency. This makes LPAe profile downloads potentially faster and more reliable than LPAd downloads.

### LUIe: Two Options for User Interaction

The LUIe faces a unique challenge: how does a UI running *inside a smart card* present itself to the user? The spec defines two mechanisms (section 5.11):

#### Option 1: CAT Toolkit (5.11.1)

The **Card Application Toolkit (CAT)** is the standard mechanism for UICC applications to interact with the device. The LUIe uses CAT proactive commands — specifically **DISPLAY TEXT**, **GET INPUT**, **SELECT ITEM**, and **SET UP MENU** — to render a text-based interface on the device screen.

The device must support the CAT mechanisms defined in Annex C.4, which include the full set of proactive commands needed for profile management. This is the simpler option and works on devices that already support SIM Toolkit (which is essentially all cellular devices).

#### Option 2: Smart Card Web Server / SCWS (5.11.2)

The **Smart Card Web Server** (defined in ETSI TS 102 588 / GSMA TS.26 [7]) is a full HTTP server running inside the eUICC. The LUIe serves HTML pages that the device's browser renders. This allows rich, graphical UIs for profile management — carrier-branded screens, data usage displays, plan comparison pages.

SCWS requires:
- Device support for CAT mechanisms (Annex C.4)
- eUICC and Device support for the Smart Card Web Server specification
- BIP (Bearer Independent Protocol) for TCP/IP connectivity

This is the premium option. It's what enables smartwatch eSIM activation screens that look like native apps, served entirely from the eUICC.

---

## ISD-R Selection and LPAe Activation (5.7.1)

When a device powers on, it must determine which LPA mode to use. This happens during the **ISD-R selection** procedure defined in section 5.7.1:

```
1. Device reads the eUICC's ATR (Answer To Reset)
2. Device sends Terminal Capability command (section 3.4.2)
   - Reports LUId, LPDd, LDSd support via tag '83' bits
   - Reports LUIe/SCWS support
3. Device SELECTs the ISD-R application
4. ISD-R determines which LPA mode to activate based on:
   - Device capabilities (from Terminal Capability)
   - eUICC LPAe capabilities
   - Device/eUICC arbitration policy
```

The Terminal Capability command is critical (section 3.4.2, Table 7). It uses bit flags in the TLV object under tag '83':

| Bit | Meaning |
|---|---|
| b1 | LUId supported (1) or not (0) |
| b2 | LPDd supported (1) or not (0) |
| b3 | LDSd supported (1) or not (0) |
| b4 | LUIe based on SCWS supported (1) or not (0) |

The eUICC uses these bits to gate ES10 function availability:
- **ES10c** functions only enabled if LUId is supported
- **ES10b** functions only enabled if LPDd is supported
- **ES10a** functions only enabled if LDSd is supported

For LPAe activation, the conditions are defined in 5.7.1. The eUICC checks its own LPAe capabilities alongside the device's reported capabilities. If the device supports SCWS (b4=1) and the eUICC has an LPAe with SCWS-based LUIe, the eUICC can activate the LPAe. If the device reports LPAd capabilities (b1-b3 all 1), the eUICC can instead rely on the external LPAd.

---

## Coexistence of LPAd and LPAe

Section 2.1 explicitly addresses dual-support:

> A Device supporting both the LPAd and the LPAe SHALL implement an appropriate mechanism that sets the LPA to be used.

This means a smartphone with a full LPAd implementation can also contain an eUICC with LPAe. The arbitration mechanism is implementation-specific but must ensure that only one LPA is "active" at a time — you don't want two profile managers fighting over the ISD-R.

A common deployment model:
- **Primary interface**: The LPAd (smartphone OS) handles all profile management normally
- **Fallback**: If the LPAd is unavailable (e.g., during initial setup before the OS is fully loaded), the LPAe takes over for provisioning
- **Headless recovery**: The LPAe can handle profile downloads even if the host OS is corrupted

For companion devices (smartwatches, fitness trackers), the LPAe is often the *primary* LPA, with the paired smartphone acting only as a UI conduit via the SCWS or CAT mechanisms.

---

## Practical Implications

**For device manufacturers:** LPAe eliminates the need to develop and maintain an OS-level LPA application. The eUICC vendor provides the LPAe as part of the eUICC OS. This is especially valuable for low-resource IoT devices and wearables.

**For eUICC manufacturers:** LPAe increases the complexity of the eUICC OS. It requires a TCP/IP stack (for BIP), TLS implementation, HTTP client, and potentially an HTTP server (for SCWS). Memory is tight — every byte counts on a secure element.

**For carriers:** The LPAe model means the profile management experience is consistent across devices using the same eUICC platform, regardless of the host OS. This simplifies testing and certification.

**For users:** Most users will never notice whether their device uses LPAd or LPAe. The UI looks similar, the QR code scanning works the same way. The difference matters during initial device setup and in headless scenarios.

---

The choice between LPAd and LPAe is one of the most consequential architectural decisions in eSIM device design. It determines the OS requirements, the security boundary, the UI technology, and the companion device story. In the next article, we'll look at what happens when a device first powers on — the boot and initialisation sequence that sets all of this in motion.


---

← Previous: [The Developer's View: RSP Interfaces and Protocol Binding](06-developer-interfaces) | [Section Index](index) | Next: [SGP.22 v2.7 — Device and eUICC Boot: First Power-On to Profile Discovery](08-boot-initialisation) →
