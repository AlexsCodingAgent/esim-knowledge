---
layout: default
title: "SGP.32: IoT eSIM RSP — GSMA eUICC Architecture for NB-IoT, LTE-M, and LPWA Devices"
description: "Complete GSMA SGP.32 IoT eSIM technical reference: eIM and IPA architecture, direct/indirect profile download, eIM Package protocol, SM-DS operations, DTLS security, and device initialisation for constrained IoT devices."
date: 2026-06-13
---

**[eUICC.tech]({{ site.baseurl }}/) > SGP.32: IoT eSIM RSP**

# SGP.32: IoT eSIM RSP

*The GSMA specification for eSIM on constrained devices: NB-IoT, LTE-M, sensors, trackers, and things that have no screen.*

SGP.32 is the GSMA's eSIM Remote SIM Provisioning architecture purpose-built for the Internet of Things. Unlike the consumer SGP.22 spec (designed for smartphones with screens and user interaction), SGP.32 introduces the **eIM** (eSIM IoT Remote Manager) and **IPA** (IoT Profile Assistant) to handle profile delivery on headless, battery-powered, and network-constrained devices. If you're building or integrating cellular IoT products: asset trackers, smart meters, environmental sensors, industrial gateways — this is the specification that defines how those devices get and manage their eSIM profiles.

The articles below walk through every component: the eIM-IPA architecture, direct and indirect profile download paths, the cryptographically-signed eIM Package protocol, SM-DS event-driven discovery, DTLS security for constrained links, device initialisation, and the full IoT eSIM function reference.

| # | Article |
|---|---------|
| 07 | [eSIM for IoT: Why It Needed Its Own Architecture]({{ site.baseurl }}/docs/articles/sgp32/07-iot-esim-why) |
| 08 | [The eSIM IoT Architecture: eIM, IPA, and the New Interfaces]({{ site.baseurl }}/docs/articles/sgp32/08-iot-architecture-im-ipa) |
| 09 | [IoT Profile Download: Direct, Indirect, and eIM Package Handling]({{ site.baseurl }}/docs/articles/sgp32/09-iot-profile-download-packages) |
| 10 | [IoT eSIM Security: eIM Certificates, DTLS, and Device Trust]({{ site.baseurl }}/docs/articles/sgp32/10-iot-esim-security-dtls) |
| 11 | [eIM Configuration: Associating Remote Managers with Your eUICC]({{ site.baseurl }}/docs/articles/sgp32/11-eim-configuration) |
| 12 | [Notifications and Error Handling in IoT eSIM]({{ site.baseurl }}/docs/articles/sgp32/12-notifications-errors) |
| 13 | [IoT Device Initialisation and the eUICC File Structure]({{ site.baseurl }}/docs/articles/sgp32/13-iot-device-initialisation) |
| 14 | [Profile State Management via the eIM: Remote Enable, Disable, Delete]({{ site.baseurl }}/docs/articles/sgp32/14-iot-profile-state-management) |
| 15 | [SM-DS Operations in IoT eSIM: Event Registration and Retrieval]({{ site.baseurl }}/docs/articles/sgp32/15-iot-smsds-operations) |
| 16 | [IoT eSIM Functions Reference: ESipa, ES9+', ES11', ESep]({{ site.baseurl }}/docs/articles/sgp32/16-iot-functions-reference) |
| 17 | [Profile Lifecycle & Policy: Types, PPE, and Enforcement in IoT eSIM]({{ site.baseurl }}/docs/articles/sgp32/17-profile-lifecycle-policy) |
| 18 | [Advanced IoT Security & Lifecycle: Mutual Auth, OS Update, Emergency Profiles, and ECASD]({{ site.baseurl }}/docs/articles/sgp32/18-advanced-security-lifecycle) |
