---
title: "eIM Configuration: Associating Remote Managers with Your eUICC"
description: "Details eIM Configuration Operations (eCOs) — addEim, updateEim, deleteEim, listEim — that associate remote managers with an eUICC, plus two bootstrap paths for establishing initial trust."
date: 2026-06-02
---

# eIM Configuration: Associating Remote Managers with Your eUICC

**🏠 [eUICC.tech]({{ site.baseurl }}/) > [SGP.32 IoT eSIM]({{ site.baseurl }}/docs/articles/sgp32/) > eIM Configuration: Associating Remote Managers with Your eUICC**

> **💡 Why this matters:** In consumer eSIM, there's no persistent "who manages me" relationship stored on the chip: the LPA trusts the SM-DP+ based on the GSMA CI chain, but that trust is ephemeral. IoT needs something stronger: an `eIM` that can send signed commands to a device in a remote wind farm, with the eUICC verifying them locally using a stored public key: no network call required. That's what eIM Configuration Operations (`eCOs`) deliver.

> **Key takeaways:**
> - `EimConfigurationData` is stored on the eUICC and contains the `eIM`'s public key, counter value, protocol config, and TLS trust anchor
> - Four eCOs: `addEim`, `updateEim`, `deleteEim`, `listEim` : all carried in signed eUICC Packages
> - Two bootstrap paths: eIM-managed (via eCO in signed package) and IPA-managed (`AddInitialEimConfiguration` : unsigned, for the very first eIM)
> - Counter value management is the primary replay defense; overflow requires delete + re-add with fresh `associationToken`

A unique innovation in IoT eSIM is the concept of **Associated eIMs** : cryptographically trusted remote managers whose credentials are stored directly on the eUICC. This article covers how eIMs are added, updated, listed, and removed through **eIM Configuration Operations (`eCOs`)** .

---

## Why eIM Association Matters

In consumer eSIM, the LPA trusts the SM-DP+ based on the GSMA CI chain. There's no persistent "who manages me" relationship on the chip. In IoT, that's insufficient: a device deployed in a remote wind farm needs to know that commands to switch profiles come from a trusted source, without requiring a full SM-DP+ mutual authentication every time.

**eIM Configuration Data** stored on the eUICC provides this persistent trust. Once an eIM is associated, it can send signed eUICC Packages (PSMOs and eCOs) that the eUICC verifies locally using the stored public key: no external network call needed.

---

## The `EimConfigurationData` Structure

Each associated eIM stores the following on the eUICC (ASN.1 definition):

```
EimConfigurationData ::= SEQUENCE {
    eimId                 [0] UTF8String,         -- Unique eIM identifier
    eimFqdn               [1] UTF8String OPTIONAL, -- FQDN of eIM (or intermediate server)
    eimIdType             [2] EimIdType OPTIONAL,  -- OID, FQDN, or proprietary
    counterValue          [3] INTEGER OPTIONAL,     -- Anti-replay counter
    associationToken      [4] INTEGER OPTIONAL,     -- Anti-replay across re-association
    eimPublicKeyData      [5] CHOICE {              -- For verifying eUICC Package signatures
        eimPublicKey        SubjectPublicKeyInfo,    -- Raw ECDSA public key
        eimCertificate      Certificate              -- Full X.509 certificate
    } OPTIONAL,
    trustedPublicKeyDataTls [6] CHOICE {             -- For TLS/DTLS transport
        trustedEimPkTls     SubjectPublicKeyInfo,    -- Raw public key (pinning)
        trustedCertificateTls  Certificate           -- CA or leaf certificate
    } OPTIONAL,
    eimSupportedProtocol  [7] EimSupportedProtocol OPTIONAL,
    euiccCiPKId           [8] SubjectKeyIdentifier OPTIONAL,
    indirectProfileDownload [9] NULL OPTIONAL,
    eSipaProprietaryProtocolInformation [10] VendorSpecificExtension OPTIONAL
}
```

---

### Key fields explained:

- **`eimId`** : UTF-8 string, 1-128 chars. The identity of the `eIM`. If `eimIdType` is `eimIdTypeFqdn`, the `eimId` itself is the FQDN.
- **`eimFqdn`** : The actual hostname. Required if `eimIdType` is not FQDN-based, to avoid redundancy with `eimId`.
- **`counterValue`** : Starts at some initial value, incremented per package. Max 8,388,607.
- **`associationToken`** : A global eUICC counter. On first association, the eUICC sets this to the current global counter value. Prevents replay of the entire "add eIM" sequence after eIM removal.
- **`eimPublicKeyData`** : Either a raw ECDSA public key or an X.509 certificate. Used to verify `eimSignEpReq` signatures on eUICC Packages.
- **`trustedPublicKeyDataTls`** : Trust anchor for TLS/DTLS on `ESipa`. Can be a raw key for ultra-constrained devices or a certificate for PKI validation.
- **`eimSupportedProtocol`** : Bitfield: `eimRetrieveHttps`, `eimRetrieveCoaps`, `eimInjectHttps`, `eimInjectCoaps`, `eimProprietary`
- **`euiccCiPKId`** : Which CI public key the eUICC should use when signing eUICC Package Results for this `eIM`.

---

## Adding an eIM (`addEim`)

```
eCO payload: addEim containing EimConfigurationData

Required fields:
    eimId, counterValue, eimPublicKeyData

Optional but strongly recommended:
    trustedPublicKeyDataTls (if IPAe with HTTPS/CoAPS)
    eimSupportedProtocol
    euiccCiPKId

If associationToken is set to -1 in the request:
    → eUICC generates a new associationToken using its global counter

If associationToken is absent:
    → no associationToken is configured for this eIM

Error conditions:
    insufficientMemory       : eUICC has no space for another eIM
    associatedEimAlreadyExists: eIM with this ID already present
    ciPKUnknown              : euiccCiPKId references unknown CI key
    invalidAssociationToken  : token mismatch on re-add
```

On success, the eUICC returns either `ok(0)` or the generated `associationToken`.

---

## Updating an eIM (`updateEim`)

```
eCO payload: updateEim containing EimConfigurationData

Used to:
    - Rotate eIM signing keys (new eimPublicKeyData)
    - Change TLS trust anchors (new trustedPublicKeyDataTls)
    - Update protocol support (new eimSupportedProtocol)
    - Reset counterValue after rollover

Error conditions:
    eimNotFound              : eIM ID not on the eUICC
    ciPKUnknown              : new euiccCiPKId invalid
    counterValueOutOfRange   : counter exceeds eUICC max
```

---

## Deleting an eIM (`deleteEim`)

```
eCO payload: deleteEim { eimId }

Effect: All EimConfigurationData for this eIM is removed

Special case: If this was the last associated eIM, the eUICC returns
    lastEimDeleted(2) : meaning no eIM Configuration Data remains

Error: eimNotFound(1) if the eIM ID doesn't exist
```

---

## Listing Associated eIMs (`listEim`)

```
eCO payload: listEim (empty SEQUENCE)

Returns: list of { eimId, eimIdType } for all associated eIMs

Note: eimIdType is only present if the type is eimIdTypeOid and eimIdTypeFqdn
```

---

## Two Paths for eIM Configuration Data

SGP.32 defines two mechanisms for getting eIM data onto the eUICC:

### eIM-managed (via eCO in signed eUICC Package)

The primary path. An already-associated `eIM` sends an `addEim` eCO in a signed eUICC Package to add another eIM. This is how a device management platform adds itself alongside the manufacturer's provisioning eIM.

---

### IPA-managed (initial bootstrap)

```
IPA → eUICC: ES10b.AddInitialEimConfiguration
    (Unsigned eCO: for the very first eIM, before any eIM is associated)

IPA → eUICC: ES10b.GetEimConfigurationData
    (Read back stored configuration)

IPA → eUICC: ES10b.DeleteAllEimConfigurationData
    (Factory reset of eIM data: requires Device Test Mode or similar authorization)
```

The `AddInitialEimConfiguration` is unsigned because at bootstrap time, no eIM is yet trusted to sign it. This is typically done during device manufacturing or initial provisioning by a trusted local operator.

---

## Complete Removal

`ES10b.DeleteAllEimConfigurationData` (triggered by `IPA`) removes all eIM configuration data from the eUICC. This operation requires elevated authorization (Device Test Mode or similar). After removal, the eUICC has no trusted eIMs: it's back to a bootstrap state, ready for `AddInitialEimConfiguration`.

---

## Counter Value Management

The counter is the primary replay defense:

- `eIM` increments counter per eUICC Package
- eUICC rejects packages with counter ≤ stored value
- Both sides store their view of the counter
- On counter overflow (approaching 8,388,607): delete and re-add the eIM via `deleteEim` → `addEim` with a fresh counter starting at 0, protected by a new `associationToken`

---

## `IPAe`-Specific Considerations

When the `IPA` runs inside the eUICC (`IPAe`), the `trustedPublicKeyDataTls` field becomes critical: the `IPAe` needs the TLS/DTLS trust anchor to establish a secure connection to the `eIM`. Without it, the `IPAe` cannot reach the `eIM`, and the device is stranded. The `trustedCertificateTls` should contain either the `eIM`'s TLS certificate or a CA certificate that chains to it.

---

## 📋 Summary

- eIM Configuration Data stored on the eUICC provides persistent cryptographic trust between device and remote manager
- Four eCOs (`addEim`, `updateEim`, `deleteEim`, `listEim`) manage the full lifecycle, all carried in signed eUICC Packages
- Two bootstrap paths: eIM-managed (requires an already-associated eIM) and IPA-managed (unsigned, for the very first eIM)
- Counter value + `associationToken` provide replay protection; overflow requires a controlled delete-and-re-add cycle

---

<div align="center">

← Previous: [IoT eSIM Security: eIM Certificates, DTLS, and Device Trust]({{ site.baseurl }}/docs/articles/sgp32/10-iot-esim-security-dtls) · [🏠 Home]({{ site.baseurl }}/)

Next: [Notifications and Error Handling in IoT eSIM]({{ site.baseurl }}/docs/articles/sgp32/12-notifications-errors) →

</div>

---

*Based on GSMA SGP.32 v1.3, Sections 2.10-2.11 and 3.5*


---

← Previous: [IoT eSIM Security: eIM Certificates, DTLS, and Device Trust](10-iot-esim-security-dtls) | [Section Index](index) | Next: [Notifications and Error Handling in IoT eSIM](12-notifications-errors) →
