---
title: "IFPP in Practice: PC OEMs, Automotive, and IoT Manufacturing"
description: "Covers SGP.41 IFPP deployment scenarios for PC OEMs, automotive assembly, and large-scale IoT manufacturing : including two-stage production, region-specific provisioning, and just-in-time profile loading at the factory."
date: 2026-06-06
---

# IFPP in Practice: PC OEMs, Automotive, and IoT Manufacturing

**[eUICC.tech]({{ site.baseurl }}/) > [SGP.41 IFPP]({{ site.baseurl }}/docs/articles/sgp41/) > IFPP in Practice: PC OEMs, Automotive, and IoT Manufacturing**

> **Why this matters:** SGP.41's architecture is elegant on paper, but its real value emerges on the factory floor. PC OEMs shipping millions of laptops with pre-provisioned eSIM connectivity, automotive assembly lines where cars roll off with active telematics, IoT manufacturers producing devices at scale without SAS-certified facilities: these aren't hypotheticals, they're the use cases the GSMA designed SGP.41 to address.

> **Key takeaways:**
> - **PC OEMs**: Consumer devices with eSIM pre-provisioned at manufacturing : "power on, connect, done" : no QR codes or End User activation codes
> - **Automotive**: eSIM profiles loaded during vehicle assembly for telematics, eCall, and connected services: connectivity active the moment the car leaves the factory
> - **IoT at scale**: Large-volume device makers (smart meters, sensors, trackers) using offline, no-SAS, no-HSM provisioning: the Annex A.2 "CheapDevice" use case
> - **Two-stage manufacturing**: PC motherboards built in bulk (Manufacturing Step), region/customer-specific profiles loaded at configuration time (Configuration Step)
> - **Inventory management**: Pre-loaded profiles can be deleted and devices re-provisioned for different customers: turning excess inventory into flexible stock
> - **On-demand profile loading**: Customer, Operator, and EID may not be known until the Configuration Step: profiles are pre-ordered and stored at the factory, loaded just-in-time

SGP.41's Annex A defines four informative use cases that illustrate the specification's real-world deployment scenarios. These aren't abstract: they address genuine manufacturing pain points that the GSMA's industry members (Samsung, device OEMs, Operators) brought to the table.

---

## Use Case 1: Consumer Devices: The PC OEM Scenario

### The Problem

HappyDevice produces consumer devices (laptops, tablets, wearables). Their factory has two hard constraints:

1. **No internet on the production floor** : the factory is air-gapped for security and IP protection. SGP.22's online profile download is impossible.
2. **They want to ship devices that are ready to connect** : the consumer should power on and be online, without scanning QR codes, entering activation codes, or navigating carrier selection menus.

### The IFPP Solution

1. HappyDevice orders eUICCs from the EUM with pre-loaded one-time keys
2. HappyDevice orders profiles from Operators and sends eUICC data to the relevant SM-DPf via Esbpp
3. The SM-DPf creates BPPs (bound and encrypted to each eUICC) and delivers them to HappyDevice
4. HappyDevice stores the BPPs in their air-gapped production environment
5. During the final phase of device production, the BPP is pushed through the FPA into the eUICC: fully offline
6. The device ships with a pre-installed bootstrap profile

### The End User Experience

The consumer powers on their new laptop. The eSIM profile is already installed and enabled. They click "Connect" in Windows and are immediately online: no QR code scanning, no carrier selection, no activation code entry. The cellular connectivity "just works" out of the box, exactly like Wi-Fi.

This is the Microsoft Windows eSIM integration model: profiles pre-loaded at the OEM factory, managed through the Windows Mobile Plans app. SGP.41 provides the standardised, interoperable mechanism for every PC OEM to achieve this with any Operator.

---

## Use Case 2: IoT Devices: Scale Without SAS

### The Problem

CheapDevice produces IoT devices (smart sensors, trackers, meters) in large volumes. Their production constraints are:

1. **Production speed is critical** : SGP.22's multi-round-trip online profile download introduces unacceptable latency. At millions of units per month, seconds per device add up to days of production delay.
2. **No appetite for factory security certification** : CheapDevice does not want SAS certification for its production facility. The cost, audit burden, and operational complexity are inappropriate for a high-volume, low-margin IoT manufacturer.
3. **No internet on the line** : even if they wanted online provisioning, many IoT factories are intentionally air-gapped.

### The IFPP Solution

1. CheapDevice orders eUICCs with one-time keys and receives eUICC data from the EUM
2. They request BPPs from the SM-DPf in advance: the SM-DPf handles all binding and encryption in its SAS-certified HSM
3. BPPs are stored locally in the factory until needed
4. During production, the BPP is pushed through the FPA to the eUICC in a single, fast operation: no network latency, no round-trips
5. CheapDevice operates without SAS accreditation (Option 1 under GENS01) and without an HSM (Option 2 under GENS02)

The key enabler is that all security-sensitive operations happen at the SM-DPf, not at the factory. CheapDevice never touches profile secrets: they only handle encrypted BPPs and pass through eUICC public keys and certificates.

---

## Use Case 3: Two-Stage Manufacturing: The Configuration Step

### The Problem

A device maker produces devices destined for different regions worldwide. For example:

- PC motherboards manufactured in bulk in Asia
- Smart meters used by different utility companies across Europe
- Connected appliances shipped to different markets with different Operators

At the time of hardware manufacturing, the final customer, Operator, or even the shipping destination may not be known. The device maker needs the flexibility to:

1. Build generic hardware in volume (Manufacturing Step)
2. Configure for specific customer/region later (Configuration Step)

### The IFPP Solution

The two-stage process works as follows:

**Manufacturing Step**: The device is built and placed into stock. For a PC, this might be the motherboard without the modem. For a smart meter, this is the base unit without customer-specific configuration. The device may or may not have an eUICC at this stage: if it does, the eUICC is unprovisioned (or has only a test profile loaded via EUICCF05).

**Configuration Step**: When a customer order arrives:
1. The device is pulled from stock
2. The modem with eUICC is added (for PCs) or the existing eUICC is provisioned
3. The BPP for the customer's chosen Operator and region is loaded through the FPA
4. The device is final-assembled, tested, and shipped

All data exchanges with external systems are strictly controlled: the configuration step uses pre-delivered BPPs and operates without real-time internet connectivity to SM-DP+ servers.

This model is explicitly described in Annex A.3: *"The Mobile Service Provider, serial number of the device or the EID of the eUICC are not known until configuration time."*

---

## Use Case 4: Inventory Management: Flexible Stock

### The Problem

HappyDevice produces 5 million devices pre-provisioned with a Profile for Customer ABC. Before shipping, ABC reduces the order to 4 million. HappyDevice now has 1 million devices with ABC's profile installed: but no customer for them.

Without IFPP, those 1 million devices would need to be re-flashed, reprovisioned, or scrapped. With IFPP, the profiles can be cleanly deleted and the devices re-provisioned for a different customer.

### The IFPP Solution

1. HappyDevice returns the 1 million excess devices to their facilities
2. They remove all of ABC's configuration, including the pre-provisioned Profiles
3. HappyDevice sends a report to the Mobile Service Provider and/or ABC confirming the 1 million Profiles were deleted
4. Those 1 million devices can now be configured for another customer: potentially including provisioning of a new Profile using IFPP

This inventory flexibility is a significant operational and financial advantage. It transforms "customer-specific pre-provisioned stock" from a liability (stranded inventory) into an asset (configurable on demand).

---

## The Common Thread: What Makes These Use Cases Work

All four use cases share three architectural requirements that SGP.41 satisfies:

### 1. Offline Profile Loading

Every use case requires profile loading without internet connectivity on the production line. SGP.41 achieves this by shifting binding to the SM-DPf: the BPP arrives at the factory pre-encrypted and ready to install.

### 2. Speed

Consumer SGP.22 provisioning involves multiple network round-trips. SGP.41 reduces the on-device interaction to a single push operation: the FPA sends the BPP, the eUICC processes it, the result is returned. No network latency, no DNS resolution, no TLS handshake.

### 3. Reduced Factory Security Burden

Whether it's a top-tier PC OEM or a high-volume IoT manufacturer, factories don't want to become eSIM security facilities. SGP.41's Options 1 and 2 (no SAS, no HSM) mean the factory handles only encrypted data and never touches profile secrets. The security boundary is the eUICC itself.

---

## Real-World Integration Patterns

### PC OEM eSIM (Windows)

Microsoft's eSIM framework in Windows 11 expects profiles to be pre-loaded at the factory or downloaded post-purchase. SGP.41 standardises the factory path:

- The FPA can be implemented as the Windows LPA running in factory mode
- BPPs are delivered to the OEM's imaging/provisioning system
- Profiles are loaded during the Windows image finalisation stage
- The end user sees "Cellular" as an available network option out of the box

### Automotive Assembly

Connected cars require cellular connectivity from day zero: for telematics, emergency calling (eCall in Europe), and over-the-air software updates. SGP.41 enables:

- eSIM profiles loaded during vehicle assembly, before the car leaves the factory
- Multiple profiles for different regions (European eCall profile + local operator profile)
- The SM-DPf handles binding for multiple eUICCs (telematics unit, infotainment, hotspot) in a single vehicle
- Connectivity is active before the car reaches the dealership

### IoT Device Manufacturing Lines

For NB-IoT sensors, smart meters, asset trackers, and industrial IoT devices:

- High-volume, low-cost production lines with minimal IT infrastructure
- No SAS, no HSM: the factory pushes BPPs through a lightweight FPA (hardware dongle or production-line software)
- The FPA can be a simple production-line tool that connects to the device's test points, pushes the BPP, and verifies success: no permanent on-device FPA required
- Profiles can be loaded in bulk: the production-line system manages the mapping of BPPs to specific eUICCs by EID

---

## Summary

- **PC OEMs**: Bootstrapped connectivity out of the box: SGP.41 enables pre-loaded profiles installed during OEM imaging, integrated with Windows Mobile Plans
- **Automotive**: Day-zero connectivity for telematics, eCall, and OTA updates: profiles loaded during vehicle assembly
- **IoT at scale**: High-volume manufacturers using offline, no-SAS, no-HSM provisioning to keep costs low and throughput high (Annex A.2 "CheapDevice")
- **Two-stage manufacturing**: The Manufacturing Step / Configuration Step split enables region-specific and customer-specific provisioning without separate production lines (Annex A.3)
- **Inventory flexibility**: Pre-loaded profiles can be deleted and devices re-provisioned for different customers, turning excess stock from a liability into an asset (Annex A.4)
- All use cases share three enablers: offline loading, single-push speed, and reduced factory security requirements

---

<div align="center">

← Previous: <a href="{{ site.baseurl }}/docs/articles/sgp41/50-sgp41-security">IFPP Security: Factory Trust Models and Certificate Chains</a> · <a href="{{ site.baseurl }}/">Home</a>

</div>

---

*Based on GSMA SGP.41 v1.0 (28 February 2025) : eSIM In-Factory Profile Provisioning Architecture and Requirements, Annex A*


---

← Previous: [IFPP Security: Factory Trust Models and Certificate Chains](50-sgp41-security) | [Section Index](index)
