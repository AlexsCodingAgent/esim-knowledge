---
title: "IoT eSIM Functions Reference: ESipa, ES9+', ES11', ESep"
date: 2026-06-07
---

# IoT eSIM Functions Reference: ESipa, ES9+', ES11', ESep

> **💡 Why this matters:** This is the API-level reference for SGP.32's four IoT-specific interfaces — the catalogue you reach for when implementing an `eIM`, `IPA`, or IoT eSIM integration. Every function, its parameters, and its transport binding are listed here so you don't have to grep through 231 pages of specification.

> **Key takeaways:**
> - `ESipa` is the workhorse: `TransferEimPackage`, `ProvideEimPackageResult`, `IpaEuiccDataRequest`/`Response`, `ProfileDownloadTrigger`, `HandleNotification`, plus Indirect Download relay functions
> - `ES9+'` mirrors consumer `ES9+` for server-side profile download orchestration by the `eIM`
> - `ES11'` mirrors consumer `ES11` for server-side SM-DS polling by the `eIM`
> - `ESep` is logical only — its functions (`EuiccPackageRequest`, `EuiccPackageResult`, `EuiccMemoryReset`, `ExecuteFallbackMechanism`) are embedded within eUICC Packages over `ESipa`
> - Eight new ES10b extensions (`LoadEuiccPackage`, `AddInitialEimConfiguration`, `ProfileRollback`, etc.) support IoT-specific eUICC operations

This article catalogues the key functions defined by SGP.32's four IoT-specific interfaces — the API-level reference for anyone implementing an `eIM`, `IPA`, or IoT eSIM integration.

---

## `ESipa` — eIM to IPA

The primary IoT interface, carrying eIM Packages, data requests, and notifications.

---

### `TransferEimPackage` / `ProvideEimPackageResult`

The bidirectional package exchange. Two modes:

**IPA retrieves from eIM (pull):**
```
IPA → eIM:  TransferEimPackage (empty request)
eIM → IPA:  TransferEimPackage response {
                EuiccPackageRequest (if pending),
                acknowledgements for previous results
            }
```

**IPA provides results to eIM (push):**
```
IPA → eIM:  ProvideEimPackageResult {
                EuiccPackageResult,
                PendingNotificationList (optional),
                eimTransactionId (optional)
            }
eIM → IPA:  Acknowledgements { sequenceNumbers }
```

---

### `IpaEuiccDataRequest` / `IpaEuiccDataResponse`

The heartbeat exchange — `IPA` pushes eUICC state to the `eIM`.

```
eIM → IPA:  IpaEuiccDataRequest {
                tagList     (what eIM wants to know),
                eimTransactionId
            }

IPA → eUICC: Fetches requested data (euiccInfo, notifications, etc.)

IPA → eIM:  IpaEuiccDataResponse {
                notificationsList,
                defaultSmdpAddress,
                euiccPackageResultList,
                euiccInfo1,
                euiccInfo2,
                rootSmdsAddress,
                associationToken,
                eumCertificate,
                euiccCertificate,
                ipaCapabilities,
                deviceInfo
            }
```

---

### `ProfileDownloadTrigger`

Pushes a profile download request to the `IPA`.

```
eIM → IPA:  ProfileDownloadTriggerRequest {
                activationCode          (LPA:1$ format string),
                OR smdsEventRecord,
                eimTransactionId
            }

IPA → eUICC → SM-DP+: Profiles downloaded

IPA → eIM:  ProfileDownloadTriggerResult {
                profileInstallationResult (success),
                OR profileDownloadError   (failure)
            }
```

---

### `HandleNotification`

Forwards notifications to receivers.

```
IPA → eIM:  ESipa.HandleNotification {
                notificationList,
                euiccPackageResult (optional — for PSMO results too)
            }
```

---

### `InitiateAuthentication` / `AuthenticateClient` (Indirect Download)

When the `eIM` proxies profile download authentication:

```
IPA → eIM:  ESipa.InitiateAuthentication {
                euiccChallenge, euiccInfo1, smdpAddress
            }
eIM → SM-DP+: ES9+'.InitiateAuthentication (forwarded)
SM-DP+ → eIM → IPA: ESipa.InitiateAuthentication response

IPA → eIM:  ESipa.AuthenticateClient {
                euiccSigned1, euiccSignature1,
                CERT.EUICC.ECDSA, CERT.EUM.ECDSA
            }
eIM → SM-DP+: ES9+'.AuthenticateClient (forwarded)
SM-DP+ → eIM → IPA: ESipa.AuthenticateClient response
```

---

### `GetBoundProfilePackage` (Indirect Download)

```
IPA → eIM:  ESipa.GetBoundProfilePackage { transactionId, ... }
eIM → SM-DP+: ES9+'.GetBoundProfilePackage (fetches BPP)
SM-DP+ → eIM → IPA: BoundProfilePackage
IPA → eUICC: ES10b.LoadBoundProfilePackage (segments)
```

---

## `ES9+'` — SM-DP+ to eIM

Server-side mirror of consumer `ES9+`, used exclusively in Indirect profile download.

| Function | Equivalent to | Purpose |
|----------|--------------|---------|
| `InitiateAuthentication` | `ES9+.InitiateAuthentication` | Starts mutual auth with eUICC (via eIM relay) |
| `AuthenticateClient` | `ES9+.AuthenticateClient` | Completes mutual auth |
| `GetBoundProfilePackage` | `ES9+.GetBoundProfilePackage` | Downloads BPP for IPA delivery |
| `HandleNotification` | `ES9+.HandleNotification` | Receives installation results |
| `CancelSession` | `ES9+.CancelSession` | Aborts an in-progress indirect download |

These are HTTP/JSON functions (like consumer `ES9+`), called by the `eIM` rather than the `IPA`.

---

## `ES11'` — SM-DS to eIM

Server-side mirror of `ES11`, used when the `eIM` polls the SM-DS on behalf of the `IPA`.

| Function | Purpose |
|----------|---------|
| `InitiateAuthentication` | `eIM` relays SM-DS auth challenge to eUICC via `IPA` |
| `AuthenticateClient` | `eIM` relays eUICC auth response to SM-DS |
| `RetrieveEventRecords` | `eIM` downloads Event Records for forwarding to `IPA` |

Same HTTP/JSON binding as `ES11`, just with the `eIM` as the HTTP client instead of the `IPA`.

---

## `ESep` — eIM to eUICC (Logical)

Not a separate wire protocol — `ESep` functions are embedded within eUICC Packages carried over `ESipa`.

---

### `EuiccPackageRequest`

```
Signed by eIM (eimSignEpReq using SK.EIM.ECDSA)

Contains:
    psmoList:       Enable, Disable, Delete, Rollback, Set/Unset Fallback
    ecoList:        AddEim, DeleteEim, UpdateEim, ListEim
    euiccMemoryReset:
    executeFallbackMechanism:
```

---

### `EuiccPackageResult`

```
Signed by eUICC (euiccSignEPR using SK.EUICC.ECDSA)

Contains:
    psmoResultList: Per-PSMO results (ok or error code)
    ecoResultList:  Per-eCO results (ok, associationToken, or error)
```

---

### `EuiccMemoryReset`

```
Factory-resets the entire eUICC (equivalent to consumer Memory Reset)
Clears all operational/test profiles, resets eIM configuration
Provisioning Profiles survive Memory Reset
```

---

### `ExecuteFallbackMechanism`

```
eIM → eUICC: Explicitly trigger fallback mechanism
eUICC: Disables current profile, enables Fallback Profile
```

This is the server-side equivalent of the autonomous fallback trigger — used when the `eIM` detects a connectivity issue and wants to proactively switch the device to its recovery profile.

---

## `ES10x` — IPA to eUICC (SGP.32 Extensions)

SGP.32 extends SGP.22's ES10 functions with IoT-specific additions:

| Function | Interface | Purpose |
|----------|-----------|---------|
| `LoadEuiccPackage` | ES10b | Delivers signed eUICC Package for PSMO/eCO execution |
| `AddInitialEimConfiguration` | ES10b | Bootstrap: adds first eIM before any trust exists |
| `GetEimConfigurationData` | ES10b | Reads stored eIM configuration |
| `DeleteAllEimConfigurationData` | ES10b | Wipes all eIM data (factory reset) |
| `ProfileRollback` | ES10b | Reverts PSMO after connectivity loss |
| `ImmediateEnable` | ES10b | Enables newly downloaded profile without separate PSMO |
| `ConfigureImmediateEnable` | ES10b | Pre-authorises immediate enabling for future downloads |
| `ExecuteFallbackMechanism` | ES10b | Triggered by eUICC Package or autonomously |

---

## Protocol Binding Summary

| Interface | Transport | Serialisation | Security |
|-----------|-----------|---------------|----------|
| `ESipa` | HTTP/TCP, CoAP/UDP, MQTT, Proprietary | ASN.1 (default) or compact ASN.1 | eIM-signed (eUICC Package) + TLS/DTLS |
| `ES9+'` | HTTP/TCP | JSON | CI-authenticated TLS |
| `ES11'` | HTTP/TCP | JSON | CI-authenticated TLS |
| `ESep` | Tunnelled through `ESipa` | ASN.1 within eUICC Package | eIM ECDSA signature + eUICC ECDSA signature |
| `ES10x` (IoT ext) | ISO 7816 APDUs | ASN.1 TLV | SCP03t (for BPP) / eIM signature (for Packages) |

---

## 📋 Summary

- `ESipa` carries everything: eIM Packages, data requests, profile download triggers, notifications, and Indirect Download relay
- `ES9+'` and `ES11'` mirror consumer `ES9+`/`ES11` for server-side orchestration by the `eIM`
- `ESep` is purely logical — its functions live inside eUICC Packages signed by both `eIM` and eUICC
- Eight new `ES10b` functions extend the IPA-to-eUICC interface for IoT-specific operations

---

*Based on GSMA SGP.32 v1.3, Sections 5 and 6*
