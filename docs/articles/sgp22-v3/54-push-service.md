---
layout: default
title: "Push Service: How eSIMs Get Notified Without Polling"
date: 2026-06-06
---

# Push Service: How eSIMs Get Notified Without Polling

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.22 v3.x Unified RSP]({{ site.baseurl }}/docs/articles/sgp22-v3/) > Push Service: How eSIMs Get Notified Without Polling**

> **💡 Why this matters:** In SGP.22 v2.x, the only way your device knows a new eSIM profile is waiting is by **polling** the SM-DS. Your phone periodically wakes up, connects to the discovery server, and asks "anything for me?" — even when there's nothing. This drains battery, wastes data, and introduces latency (you might wait minutes between polls). The v3.x Push Service replaces this with **push notifications**: the SM-DS tells your device immediately when an Event Record is pending. It's the difference between checking your mailbox every 15 minutes and getting a notification when mail arrives.

> **Key takeaways:**
> - Push Service replaces/SM-DS polling with a push-based notification mechanism
> - It leverages **existing push infrastructure** (e.g., platform push services like FCM, APNs) — the push protocol itself is out of scope for SGP.22
> - The SM-DS advertises which Push Services it supports during Common Mutual Authentication
> - The LPAd registers a **Push Token** with the SM-DS, associating the token with the eUICC's EID
> - When an Event Record is pending, the SM-DS triggers a push notification via the push server to the push client on the device
> - Tokens have expiration; the LPAd SHOULD re-register before expiration to stay reachable
> - This is a v3.x-only feature tagged `#SupportedForPushServiceV3.X.Y#`

---

## The v2.x Polling Model: Inefficient by Design

In SGP.22 v2.x, the LDS (Local Discovery Service) inside the LPA periodically polls the SM-DS:

1. The LDS opens an HTTPS connection to the SM-DS
2. It performs Common Mutual Authentication
3. It calls `ES11.InitiateAuthentication` followed by `ES11.AuthenticateClient`
4. It retrieves any pending Event Records

If no events are pending, the LDS closes the connection and waits until the next poll interval. If an operator has ordered a profile and the SM-DP+ registered an Event, the device won't know until the next poll — potentially minutes later.

This polling model has three problems:
- **Battery drain**: The device must wake the modem, establish TLS, and perform mutual authentication on every poll
- **Latency**: The user waits for the next poll cycle before receiving the notification
- **Server load**: SM-DSs must handle authentication requests from millions of devices, most of which find nothing pending

---

## The v3.x Push Model

The Push Service (section 2.13, 3.6.5) flips the model. Instead of the device polling the SM-DS, the SM-DS pushes a notification to the device when an Event Record becomes available.

### Entities Involved

| Entity | Role |
|--------|------|
| **SM-DS** | Maintains Event Records; triggers push notifications when Events are pending |
| **Push Server** | The server-side component of a push platform (e.g., Firebase Cloud Messaging, Apple Push Notification service) |
| **Push Client** | The device-side component that receives push notifications from the push server |
| **LPAd / LDSd** | The LPA's Discovery Service, which receives notifications forwarded by the push client |
| **eUICC** | Ultimately the target for profile download triggered by the notification |

The interfaces between the push server and push client, between the push client and the LPAd, and between the SM-DS and the push server are **out of scope** for SGP.22. The specification only defines the registration procedure and the trigger — the actual push transport is a platform implementation detail.

### The Flow

1. **SM-DS advertises Push Services**: During Common Mutual Authentication (section 3.0.1), the SM-DS includes `supportedPushServices` in its `rspCapability` — a list of push platforms it supports (e.g., a specific platform push service).

2. **LPAd selects and registers**: If the device supports at least one of the advertised Push Services, the LPAd selects one and requests the corresponding push client to generate a **Push Token** dedicated to the LPAd. The LPAd then forwards this Push Token together with the **EID** of its associated eUICC to the SM-DS via the Push Service Registration procedure (section 3.6.5).

3. **SM-DS triggers notification**: Later, when an Event Record is pending for this EID, the SM-DS requests the push server to send a push notification for the registered Push Token. The push server routes this to the push client, which forwards it to the LPAd.

4. **LPAd retrieves Events**: Upon receiving the notification, the LPAd MAY perform an Event Retrieval procedure (the standard ES11 flow) to get the Event Record and proceed with profile download or RPM.

### Token Lifecycle

Push Tokens have a limited validity period (implementation-dependent). The LPAd SHOULD re-register a Push Token before expiration to remain able to receive push notifications. The SM-DS MAY also clean its database of obsolete Push Tokens — and if it does, it SHOULD instruct the LPAd of a maximum Push Token retention time.

---

## The Push Service Registration Procedure (Section 3.6.5)

The registration flow integrates with the Common Mutual Authentication procedure:

1. The LPAd initiates Common Mutual Authentication with the SM-DS (or SM-DP+)
2. At step (9) of Common Mutual Authentication, the SM-XX indicates `supportedPushServices` in `lpaRspCapability`
3. If the LPAd detects that its Push Token is invalid/expired, or it hasn't registered yet, and the SM-XX indicates Push Service support:
   - The LPAd selects one Push Service from `supportedPushServices`
   - It obtains a new Push Token for the selected Push Service (e.g., interacting with the push client — out of scope)
   - It completes the Push Service Registration, forwarding the Push Token + EID
4. The SM-DS stores the association: (EID, Push Token, Push Service)
5. The LPAd enables the selected Push Service for the corresponding SM-DS

The registration can be re-triggered when:
- The LPAd detects that the Push Token is no longer valid
- The previous Push Service registration was not done
- The LPAd wants to switch to a different Push Service

---

## Comparison: v2.x Polling vs v3.x Push

| Aspect | v2.x (Polling) | v3.x (Push Service) |
|--------|---------------|---------------------|
| Notification mechanism | LDS polls SM-DS on timer | SM-DS pushes to device immediately |
| Latency | Up to poll interval (minutes) | Seconds |
| Battery impact | Periodic TLS + mutual auth | Only when notification arrives |
| Network data | Used on every poll, even empty | Used only when Events exist |
| Server load | High (millions of devices polling) | Lower (only pushes with pending Events) |
| Infrastructure needed | SM-DS only | SM-DS + push server + push client |
| Standardised in SGP.22 | Full procedure specified | Registration specified; push transport out of scope |
| Feature tag | N/A (always available) | `#SupportedForPushServiceV3.X.Y#` |

---

## Practical Considerations

**Which push platforms?** The specification deliberately stays agnostic about the specific push service. The SM-DS advertises which push services it supports; the LPAd selects one that the device also supports. This could be Apple Push Notification service (APNs), Firebase Cloud Messaging (FCM), a carrier-specific push service, or any other push platform.

**SM-DP+ also uses Push?** While the primary use case is SM-DS notifications, the `rspCapability` model allows any RSP Server (SM-DS or SM-DP+) to advertise Push Service support. The Push Service registration occurs during any Common Mutual Authentication where the server indicates support.

**Backward compatibility**: v2.x devices and servers don't support Push Service. During Common Mutual Authentication, the `rspCapability` absent from a server means "v2.x" — and the LPAd falls back to polling. Similarly, if a v3.x server doesn't see `lpaRspCapability` from the device, it knows the device doesn't support Push Service.

---

## Summary

- Push Service is a v3.x-only feature that adds push-based SM-DS notifications as an alternative to polling
- It leverages existing platform push infrastructure; the push transport itself is out of scope for SGP.22
- The SM-DS advertises supported push services during Common Mutual Authentication
- The LPAd registers a Push Token + EID association with the SM-DS
- Tokens expire; re-registration is required for continuous reachability
- The feature is backward-compatible: v2.x devices continue to poll as before

---

<div align="center">

← Previous: [Multiple Enabled Profiles: Running Several eSIMs at Once]({{ site.baseurl }}/docs/articles/sgp22-v3/53-multiple-enabled-profiles)

Next: [Feature Support: Capability Negotiation in v3.x]({{ site.baseurl }}/docs/articles/sgp22-v3/55-feature-support) →

</div>

---

*Based on GSMA SGP.22 v3.1 (01 December 2023), Section 2.13 — Overview of Push Service, Section 3.6.5 — Push Service Registration, and Section 1.9 — Feature Support*


---

← Previous: [Multiple Enabled Profiles: Running Several eSIMs at Once](53-multiple-enabled-profiles) | [Section Index](index) | Next: [Feature Support: Capability Negotiation in v3.x](55-feature-support) →
