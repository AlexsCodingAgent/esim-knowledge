---
layout: default
title: "Tag Lookup, Condensed (machine-readable)"
description: "Single-table TLV tag lookup for eSIM RSP: one row per tag with hex value, name, owning structure, clause and source spec. For programmatic or LLM extraction."
---

# Tag Lookup, Condensed

One row per tag. Columns: **Tag**, **Name**, **Structure**, **Clause**,
**Spec**. Every value is extracted from the specification text; nothing is
inferred. Prefer this page over the prose version for programmatic or LLM
extraction.

[Full reference page with search]({{ site.baseurl }}/docs/tag-lookup)

---

| Tag | Name | Structure | Clause | Spec |
|---|---|---|---|---|

| `03` | UICCCapability |  | 8.2.7 | TCA Interop v3.4 |
| `5A` | EuiccPackageSigned |  | 2.11.1.1 | SGP.32 v1.3 |
| `5A` | CompactOtherSignedNotification |  | 2.1 | SGP.32 v1.2 |
| `5C` | IpaEuiccDataRequest |  | 2.11.1.2 | SGP.32 v1.3 |
| `5C` | IpaEuiccDataRequest |  | 2.1 | SGP.32 v1.2 |
| `80` | ControlRefTemplate |  | 5.5.1 | SGP.22 v3.1 |
| `80` | ControlRefTemplate |  | 5.5.1 | SGP.22 v2.7 |
| `80` | ControlRefTemplate |  | 5.5.1 | SGP.22 v2.2.2 |
| `80` | MMS Implementation |  | 4.2.69 | 31102-j50 |
| `80` | NAF_ID |  | 4.2.10 | 31103-e11 |
| `80` | PLMN |  | 8.100 | 31111-j40 |
| `80` | NAF_ID |  | 4.2.10 | ETSI-TS-131-103-v14.1.1 |
| `81` | pollingAddress | RpmConfiguration | 2.4.12 | SGP.22 v3.1 |
| `81` | ControlRefTemplate |  | 5.5.1 | SGP.22 v2.7 |
| `81` | ControlRefTemplate |  | 5.5.1 | SGP.22 v2.2.2 |
| `81` | defaultSmdpAddress | IpaEuiccData | 2.11.2.2 | SGP.32 v1.3 |
| `81` | defaultSmdpAddress | IpaEuiccData | 2.1 | SGP.32 v1.2 |
| `81` | Polygon |  | 4.2.112 | 31102-j50 |
| `81` | B-TID |  | 4.2.10 | 31103-e11 |
| `81` | CSG ID and Name |  | 8.100 | 31111-j40 |
| `81` | B-TID |  | 4.2.10 | ETSI-TS-131-103-v14.1.1 |
| `82` | Interface to Core Network and Bearer Information |  | 4.2.69 | 31102-j50 |
| `82` | BER-TLV object returned with |  | 11.1.20.5.2 | ETSI-TS-102-221-v18.4.0 |
| `83` | eimTransactionId | IpaEuiccDataRequest | 2.11.1.2 | SGP.32 v1.3 |
| `83` | eimTransactionId | IpaEuiccDataRequest | 2.1 | SGP.32 v1.2 |
| `83` | Gateway |  | 4.2.69 | 31102-j50 |
| `84` | hostId | ControlRefTemplate | 5.5.1 | SGP.22 v3.1 |
| `84` | hostId | ControlRefTemplate | 5.5.1 | SGP.22 v2.7 |
| `84` | hostId | ControlRefTemplate | 5.5.1 | SGP.22 v2.2.2 |
| `84` | associationToken | IpaEuiccData | 2.11.2.2 | SGP.32 v1.3 |
| `84` | associationToken | IpaEuiccData | 2.1 | SGP.32 v1.2 |
| `84` | Reserved for 3GPP2: MMS Authentication Mechanism |  | 4.2.69 | 31102-j50 |
| `85` | DeviceInfo |  | 4.2 | SGP.22 v3.1 |
| `85` | Reserved for 3GPP2: MMS Authentication User Name |  | 4.2.69 | 31102-j50 |
| `86` | PLMN identifier |  | 4.4.11.4 | 31102-j50 |
| `87` | eimTransactionId | IpaEuiccData | 2.11.2.2 | SGP.32 v1.3 |
| `87` | eimTransactionId | IpaEuiccData | 2.1 | SGP.32 v1.2 |
| `87` | Privacy config |  | 4.4.13.4 | 31102-j50 |
| `88` | G ProSe direct communication in NR-PC5 |  | 4.4.13.4 | 31102-j50 |
| `89` | ProSe application to path preference mapping rules |  | 4.4.13.4 | 31102-j50 |
| `8A` | discovery signalling for solicitation |  | 4.4.13.10 | 31102-j50 |
| `8B` | RSC info list |  | 4.4.13.10 | 31102-j50 |
| `8C` | QI to PC5 QoS parameters mapping rules |  | 4.4.13.10 | 31102-j50 |
| `8E` | User info ID for discovery |  | 4.4.13.10 | 31102-j50 |
| `8F` | announcement and additional information |  | 4.4.13.12 | 31102-j50 |
| `90` | profileNickname | ProfileInfoListResponse | 5.7.15 | SGP.22 v3.1 |
| `90` | profileNickname | ProfileInfoListResponse | 5.7.15 | SGP.22 v2.7 |
| `90` | profileNickname | ProfileInfoListResponse | 5.7.15 | SGP.22 v2.2.2 |
| `90` | profileNickname | IpaCapabilities | 4.4 | SGP.32 v1.3 |
| `90` | profileNickname | IpaCapabilities | 2.1 | SGP.32 v1.2 |
| `91` | serviceProviderName | VerifyProfileRecoveryResponse | 5.11.3 | SGP.22 v3.1 |
| `91` | serviceProviderName | UpdateMetadataRequest | 5.4.1 | SGP.22 v2.7 |
| `91` | serviceProviderName | UpdateMetadataRequest | 5.4.1 | SGP.22 v2.2.2 |
| `91` | serviceProviderName | IpaCapabilities | 4.4 | SGP.32 v1.3 |
| `91` | serviceProviderName | IpaCapabilities | 2.1 | SGP.32 v1.2 |
| `91` | rules |  | 4.4.13.4 | 31102-j50 |
| `92` | profileName | VerifyProfileRecoveryResponse | 5.11.3 | SGP.22 v3.1 |
| `92` | profileName | UpdateMetadataRequest | 5.4.1 | SGP.22 v2.7 |
| `92` | profileName | UpdateMetadataRequest | 5.4.1 | SGP.22 v2.2.2 |
| `92` | profileName | IpaCapabilities | 4.4 | SGP.32 v1.3 |
| `92` | profileName | IpaCapabilities | 2.1 | SGP.32 v1.2 |
| `92` | Privacy timer |  | 4.4.13.10 | 31102-j50 |
| `93` | iconType | UpdateMetadataRequest | 5.4.1 | SGP.22 v3.1 |
| `93` | iconType | UpdateMetadataRequest | 5.4.1 | SGP.22 v2.7 |
| `93` | iconType | UpdateMetadataRequest | 5.4.1 | SGP.22 v2.2.2 |
| `93` | iconType | IpaCapabilities | 4.4 | SGP.32 v1.3 |
| `93` | iconType | IpaCapabilities | 2.1 | SGP.32 v1.2 |
| `93` | G PKMF address information |  | 4.4.13.10 | 31102-j50 |
| `94` | icon | UpdateMetadataRequest | 5.4.1 | SGP.22 v3.1 |
| `94` | icon | UpdateMetadataRequest | 5.4.1 | SGP.22 v2.7 |
| `94` | icon | UpdateMetadataRequest | 5.4.1 | SGP.22 v2.2.2 |
| `94` | icon | IpaCapabilities | 4.4 | SGP.32 v1.3 |
| `94` | icon | IpaCapabilities | 2.1 | SGP.32 v1.2 |
| `94` | Collection period |  | 4.4.13.7 | 31102-j50 |
| `95` | profileClass | StoreMetadataRequest | 5.5.3 | SGP.22 v3.1 |
| `95` | profileClass | StoreMetadataRequest | 5.5.3 | SGP.22 v2.7 |
| `95` | profileClass | StoreMetadataRequest | 5.5.3 | SGP.22 v2.2.2 |
| `95` | profileClass | IpaCapabilities | 4.4 | SGP.32 v1.3 |
| `95` | profileClass | IpaCapabilities | 2.1 | SGP.32 v1.2 |
| `95` | Reporting window |  | 4.4.13.7 | 31102-j50 |
| `96` | Reporting indicators |  | 4.4.13.7 | 31102-j50 |
| `98` | HPLMN 5G DDNMF address information |  | 4.4.13.3 | 31102-j50 |
| `99` | forbiddenProfilePolicyRules | EUICCInfo2 | 4.2 | SGP.22 v3.1 |
| `99` | profilePolicyRules | UpdateMetadataRequest | 5.4.1 | SGP.22 v2.7 |
| `99` | profilePolicyRules | UpdateMetadataRequest | 5.4.1 | SGP.22 v2.2.2 |
| `99` | profilePolicyRules | IpaCapabilities | 4.4 | SGP.32 v1.3 |
| `99` | profilePolicyRules | IpaCapabilities | 2.1 | SGP.32 v1.2 |
| `99` | solicitation |  | 4.4.13.13 | 31102-j50 |
| `9A` | discovery |  | 4.4.13.8 | 31102-j50 |
| `9B` | hriServerAddress | UpdateMetadataRequest | 5.4.1 | SGP.22 v3.1 |
| `9B` | Warning message broadcast |  | 4.4.13.10 | 31102-j50 |
| `A0` | notificationsList | IpaEuiccData | 2.11.2.2 | SGP.32 v1.3 |
| `A0` | notificationList | EimPackageResult | 2.1 | SGP.32 v1.2 |
| `A0` | MUK ID |  | 4.2.81 | 31102-j50 |
| `A1` | PDU Info List data object |  | 4.4.14.2 | 31102-j50 |
| `A2` | RemoteProfileProvisioningRequest |  | 6.6.1 | SGP.22 v3.1 |
| `A2` | RemoteProfileProvisioningRequest |  | 6.6.1 | SGP.22 v2.7 |
| `A2` | ProfilePolicyAuthorisationRule |  | 6.6.1 | SGP.22 v2.2.2 |
| `A2` | euiccPackageResultList | IpaEuiccData | 2.11.2.2 | SGP.32 v1.3 |
| `A2` | euiccPackageResultList | IpaEuiccData | 2.1 | SGP.32 v1.2 |
| `A5` | eumCertificate | IpaEuiccData | 2.11.2.2 | SGP.32 v1.3 |
| `A5` | eumCertificate | IpaEuiccData | 2.1 | SGP.32 v1.2 |
| `A6` | euiccCertificate | IpaEuiccData | 2.11.2.2 | SGP.32 v1.3 |
| `A6` | euiccCertificate | IpaEuiccData | 2.1 | SGP.32 v1.2 |
| `A8` | ipaCapabilities | IpaEuiccData | 2.11.2.2 | SGP.32 v1.3 |
| `A8` | ipaCapabilities | IpaEuiccData | 2.1 | SGP.32 v1.2 |
| `A8` | constructed |  | 4.4.2.1 | 31102-j50 |
| `A9` | deviceInfo | IpaEuiccData | 2.11.2.2 | SGP.32 v1.3 |
| `A9` | deviceInfo | IpaEuiccData | 2.1 | SGP.32 v1.2 |
| `A9` | File Ids indicated using constructed |  | 4.4.2.1 | 31102-j50 |
| `AA` | File Ids indicated using constructed |  | 4.4.2.1 | 31102-j50 |
| `AB` | MMS Connectivity Parameters |  | 4.2.69 | 31102-j50 |
| `B5` | lpaRspCapability | InitiateAuthenticationRequest | 6.6.2 | SGP.22 v3.1 |
| `B6` | UpdateMetadataRequest |  | 5.4.1 | SGP.22 v3.1 |
| `B6` | ProfileInfoListResponse |  | 5.7.15 | SGP.22 v2.7 |
| `B6` | ProfileInfoListResponse |  | 5.7.15 | SGP.22 v2.2.2 |
| `B6` | IpaCapabilities |  | 4.4 | SGP.32 v1.3 |
| `B6` | IpaCapabilities |  | 2.1 | SGP.32 v1.2 |
| `B7` | profileOwner | StoreMetadataRequest | 5.5.3 | SGP.22 v3.1 |
| `B7` | profileOwner | StoreMetadataRequest | 5.5.3 | SGP.22 v2.7 |
| `B7` | profileOwner | StoreMetadataRequest | 5.5.3 | SGP.22 v2.2.2 |
| `B7` | profileOwner | IpaCapabilities | 4.4 | SGP.32 v1.3 |
| `B7` | profileOwner | IpaCapabilities | 2.1 | SGP.32 v1.2 |
| `B8` | dpProprietaryData | ConfigureISDPRequest | 5.5.2 | SGP.22 v3.1 |
| `B8` | dpProprietaryData | ConfigureISDPRequest | 5.5.2 | SGP.22 v2.7 |
| `B8` | dpProprietaryData | ConfigureISDPRequest | 5.5.2 | SGP.22 v2.2.2 |
| `B8` | dpProprietaryData | IpaCapabilities | 4.4 | SGP.32 v1.3 |
| `B8` | dpProprietaryData | IpaCapabilities | 2.1 | SGP.32 v1.2 |
| `BA` | rpmConfiguration | UpdateMetadataRequest | 5.4.1 | SGP.22 v3.1 |
| `BC` | UpdateMetadataRequest |  | 5.4.1 | SGP.22 v3.1 |
| `BD` | UpdateMetadataRequest |  | 5.4.1 | SGP.22 v3.1 |
| `BE` | StoreMetadataRequest |  | 5.5.3 | SGP.22 v3.1 |
| `DA` | CheckProgressOk |  | 6.6.2 | SGP.22 v3.1 |
| `DA` | EventEntries |  | 6.6.2 | SGP.22 v2.7 |
| `DA` | EventEntries |  | 6.6.2 | SGP.22 v2.2.2 |
| `DA` | EimPackageErrorWithCid |  | 6.4.1.8 | SGP.32 v1.3 |
| `DA` | EPC |  | 1.1.1 | 23003-k00 |
| `DA` | NFCAccessRule |  | 7.4 | GPD_SPE_013-Secure-Element-Access-Control |
| `DE` | Tag Value |  | 4.2.66 | 31102-j50 |
| `E0` | ReplaceSessionKeysRequest |  | 5.7.1 | SGP.22 v3.1 |
| `E0` | ReplaceSessionKeysRequest |  | 5.7.1 | SGP.22 v2.7 |
| `E0` | ReplaceSessionKeysRequest |  | 5.7.1 | SGP.22 v2.2.2 |
| `E1` | ProfileDownloadTriggerResult |  | 3.8.4 | SGP.32 v1.3 |
| `E1` | ProfileDownloadTriggerResult |  | 2.1 | SGP.32 v1.2 |
| `E3` | ProfileInfoListResponse |  | 5.7.15 | SGP.22 v3.1 |
| `E3` | ProfileInfoListResponse |  | 5.7.15 | SGP.22 v2.7 |
| `E3` | ProfileInfoListResponse |  | 5.7.15 | SGP.22 v2.2.2 |
| `E3` | IpaCapabilities |  | 4.4 | SGP.32 v1.3 |
| `E3` | IpaCapabilities |  | 2.1 | SGP.32 v1.2 |
| `E4` | VerifyProfileRecoveryResponse |  | 5.11.3 | SGP.22 v3.1 |
| `5F37` | ProfileInstallationResultData |  | 2.5.6 | SGP.22 v3.1 |
| `5F37` | ProfileInstallationResultData |  | 2.5.6 | SGP.22 v2.7 |
| `5F37` | ProfileInstallationResultData |  | 2.5.6 | SGP.22 v2.2.2 |
| `5F37` | EuiccPackageRequest |  | 2.11.1.1 | SGP.32 v1.3 |
| `5F37` | CompactOtherSignedNotification |  | 2.1 | SGP.32 v1.2 |
| `9F1F` | StoreMetadataRequest |  | 5.5.3 | SGP.22 v3.1 |
| `9F21` | estimatedProfileSize | StoreMetadataRequest | 5.5.3 | SGP.22 v3.1 |
| `9F24` | enabledOnEsimPort | ProfileInfoListResponse | 5.7.15 | SGP.22 v3.1 |
| `9F25` | profileSize | ProfileInfoListResponse | 5.7.15 | SGP.22 v3.1 |
| `9F26` | fallbackAttribute | ProfileInfoListResponse | 5.7.15 | SGP.22 v2.7 |
| `9F26` | fallbackAttribute | IpaCapabilities | 4.4 | SGP.32 v1.3 |
| `9F26` | fallbackAttribute | IpaCapabilities | 2.1 | SGP.32 v1.2 |
| `9F2A` | UpdateMetadataResponse |  | 5.4.1 | SGP.22 v3.1 |
| `9F67` | reserved103 | UpdateMetadataRequest | 5.4.1 | SGP.22 v2.7 |
| `9F67` | fallbackAllowed | IpaCapabilities | 4.4 | SGP.32 v1.3 |
| `9F67` | fallbackAllowed | IpaCapabilities | 2.1 | SGP.32 v1.2 |
| `9F70` | profileState | VerifyProfileRecoveryResponse | 5.11.3 | SGP.22 v3.1 |
| `9F70` | profileState | ProfileInfoListResponse | 5.7.15 | SGP.22 v2.7 |
| `9F70` | profileState | ProfileInfoListResponse | 5.7.15 | SGP.22 v2.2.2 |
| `9F70` | profileState | IpaCapabilities | 4.4 | SGP.32 v1.3 |
| `9F70` | profileState | IpaCapabilities | 2.1 | SGP.32 v1.2 |
| `9F78` | EuiccInfo2Ext |  | 5.4.11.2 | SGP.23-v1.16 |
| `9F7B` | ecallIndication | StoreMetadataRequest | 5.5.3 | SGP.22 v2.7 |
| `9F7B` | ecallIndication | IpaCapabilities | 4.4 | SGP.32 v1.3 |
| `9F7B` | ecallIndication | IpaCapabilities | 2.1 | SGP.32 v1.2 |
| `BF20` | EUICCInfo1 |  | 4.2 | SGP.22 v3.1 |
| `BF20` | GetEuiccInfo1Request |  | 5.7.8 | SGP.22 v2.7 |
| `BF20` | GetEuiccInfo1Request |  | 5.7.8 | SGP.22 v2.2.2 |
| `BF20` | euiccInfo1 | IpaEuiccData | 2.11.2.2 | SGP.32 v1.3 |
| `BF20` | euiccInfo1 | IpaEuiccData | 2.1 | SGP.32 v1.2 |
| `BF20` | ServicesList |  | 8.2.1 | TCA Pkg v3.4.1 |
| `BF20` | UICCCapability |  | 8.1.2 | TCA Interop v3.4 |
| `BF20` | Table B-1: Contents of |  |  | GPC_SPE_093-Amendment-F-SCP11 |
| `BF20` | UICCCapability |  |  | TCA-eUICC-Profile-Package-v3.4.1 |
| `BF21` | PrepareDownloadRequest |  | 5.7.5 | SGP.22 v3.1 |
| `BF21` | PrepareDownloadRequest |  | 5.7.5 | SGP.22 v2.7 |
| `BF21` | PrepareDownloadRequest |  | 5.7.5 | SGP.22 v2.2.2 |
| `BF21` | PrepareDownloadResponse |  | 5.14.2 | SGP.32 v1.3 |
| `BF21` | PrepareDownloadResponse |  | 2.1 | SGP.32 v1.2 |
| `BF22` | EUICCInfo2 |  | 4.2 | SGP.22 v3.1 |
| `BF22` | serviceSpecificDataStoredInEuicc | UpdateMetadataRequest | 5.4.1 | SGP.22 v2.7 |
| `BF22` | GetEuiccInfo2Request |  | 5.7.8 | SGP.22 v2.2.2 |
| `BF22` | euiccInfo2 | IpaEuiccData | 2.11.2.2 | SGP.32 v1.3 |
| `BF22` | euiccInfo2 | IpaEuiccData | 2.1 | SGP.32 v1.2 |
| `BF23` | initialiseSecureChannelRequest | BoundProfilePackage | 2.5.4 | SGP.22 v3.1 |
| `BF23` | initialiseSecureChannelRequest | BoundProfilePackage | 2.5.4 | SGP.22 v2.7 |
| `BF23` | initialiseSecureChannelRequest | BoundProfilePackage | 2.5.4 | SGP.22 v2.2.2 |
| `BF23` | StoreMetadataRequest |  | 5.5 | SGP.32 v1.3 |
| `BF24` | ConfigureISDPRequest |  | 5.5.2 | SGP.22 v3.1 |
| `BF24` | ConfigureISDPRequest |  | 5.5.2 | SGP.22 v2.7 |
| `BF24` | ConfigureISDPRequest |  | 5.5.2 | SGP.22 v2.2.2 |
| `BF25` | StoreMetadataRequest |  | 5.5.3 | SGP.22 v3.1 |
| `BF25` | StoreMetadataRequest |  | 5.5.3 | SGP.22 v2.7 |
| `BF25` | StoreMetadataRequest |  | 5.5.3 | SGP.22 v2.2.2 |
| `BF25` | StoreMetadataRequest |  | 5.5 | SGP.32 v1.3 |
| `BF25` | StoreMetadataRequest |  | 2.1 | SGP.32 v1.2 |
| `BF27` | ProfileInstallationResultData |  | 2.5.6 | SGP.22 v3.1 |
| `BF27` | ProfileInstallationResultData |  | 2.5.6 | SGP.22 v2.7 |
| `BF27` | ProfileInstallationResultData |  | 2.5.6 | SGP.22 v2.2.2 |
| `BF28` | ListNotificationRequest |  | 5.7.9 | SGP.22 v3.1 |
| `BF28` | ListNotificationRequest |  | 5.7.9 | SGP.22 v2.7 |
| `BF28` | ListNotificationRequest |  | 5.7.9 | SGP.22 v2.2.2 |
| `BF29` | SetNicknameRequest |  | 5.7.21 | SGP.22 v3.1 |
| `BF29` | SetNicknameRequest |  | 5.7.21 | SGP.22 v2.7 |
| `BF29` | SetNicknameRequest |  | 5.7.21 | SGP.22 v2.2.2 |
| `BF2A` | UpdateMetadataRequest |  | 5.4.1 | SGP.22 v3.1 |
| `BF2A` | UpdateMetadataRequest |  | 5.4.1 | SGP.22 v2.7 |
| `BF2A` | UpdateMetadataRequest |  | 5.4.1 | SGP.22 v2.2.2 |
| `BF2A` | UpdateMetadataRequest |  | 5.4.2 | SGP.32 v1.3 |
| `BF2B` | RetrieveNotificationsListRequest |  | 5.7.10 | SGP.22 v3.1 |
| `BF2B` | RetrieveNotificationsListRequest |  | 5.7.10 | SGP.22 v2.7 |
| `BF2B` | RetrieveNotificationsListRequest |  | 5.7.10 | SGP.22 v2.2.2 |
| `BF2B` | RetrieveNotificationsListRequest |  | 5.9.11 | SGP.32 v1.3 |
| `BF2B` | RetrieveNotificationsListRequest |  | 2.1 | SGP.32 v1.2 |
| `BF2D` | ProfileInfoListRequest |  | 5.7.15 | SGP.22 v3.1 |
| `BF2D` | ProfileInfoListRequest |  | 5.7.15 | SGP.22 v2.7 |
| `BF2D` | ProfileInfoListRequest |  | 5.7.15 | SGP.22 v2.2.2 |
| `BF2D` | listProfileInfo | Psmo | 2.11.1.1 | SGP.32 v1.3 |
| `BF2D` | listProfileInfo | Psmo | 2.1 | SGP.32 v1.2 |
| `BF2E` | GetEuiccChallengeRequest |  | 5.7.7 | SGP.22 v3.1 |
| `BF2E` | GetEuiccChallengeRequest |  | 5.7.7 | SGP.22 v2.7 |
| `BF2E` | GetEuiccChallengeRequest |  | 5.7.7 | SGP.22 v2.2.2 |
| `BF2F` | NotificationMetadata |  | 5.7.9 | SGP.22 v3.1 |
| `BF2F` | NotificationMetadata |  | 5.7.9 | SGP.22 v2.7 |
| `BF2F` | NotificationMetadata |  | 5.7.9 | SGP.22 v2.2.2 |
| `BF30` | NotificationSentRequest |  | 5.7.11 | SGP.22 v3.1 |
| `BF30` | NotificationSentRequest |  | 5.7.11 | SGP.22 v2.7 |
| `BF30` | NotificationSentRequest |  | 5.7.11 | SGP.22 v2.2.2 |
| `BF31` | EnableProfileRequest |  | 5.7.16 | SGP.22 v3.1 |
| `BF31` | EnableProfileRequest |  | 5.7.16 | SGP.22 v2.7 |
| `BF31` | EnableProfileRequest |  | 5.7.16 | SGP.22 v2.2.2 |
| `BF32` | DisableProfileRequest |  | 5.7.17 | SGP.22 v3.1 |
| `BF32` | DisableProfileRequest |  | 5.7.17 | SGP.22 v2.7 |
| `BF32` | DisableProfileRequest |  | 5.7.17 | SGP.22 v2.2.2 |
| `BF33` | DeleteProfileRequest |  | 5.7.18 | SGP.22 v3.1 |
| `BF33` | DeleteProfileRequest |  | 5.7.18 | SGP.22 v2.7 |
| `BF33` | DeleteProfileRequest |  | 5.7.18 | SGP.22 v2.2.2 |
| `BF34` | EuiccMemoryResetRequest |  | 5.7.19 | SGP.22 v3.1 |
| `BF34` | EuiccMemoryResetRequest |  | 5.7.19 | SGP.22 v2.7 |
| `BF34` | EuiccMemoryResetRequest |  | 5.7.19 | SGP.22 v2.2.2 |
| `BF35` | LoadCRLRequest |  | 5.7.12 | SGP.22 v2.7 |
| `BF35` | LoadCRLRequest |  | 5.7.12 | SGP.22 v2.2.2 |
| `BF36` | BoundProfilePackage |  | 2.5.4 | SGP.22 v3.1 |
| `BF36` | BoundProfilePackage |  | 2.5.4 | SGP.22 v2.7 |
| `BF36` | BoundProfilePackage |  | 2.5.4 | SGP.22 v2.2.2 |
| `BF37` | ProfileInstallationResult |  | 2.5.6 | SGP.22 v3.1 |
| `BF37` | ProfileInstallationResult |  | 2.5.6 | SGP.22 v2.7 |
| `BF37` | ProfileInstallationResult |  | 2.5.6 | SGP.22 v2.2.2 |
| `BF37` | ProfileInstallationResult |  | 5.14.7 | SGP.32 v1.3 |
| `BF37` | ProfileInstallationResult |  | 2.1 | SGP.32 v1.2 |
| `BF38` | AuthenticateServerRequest |  | 5.7.13 | SGP.22 v3.1 |
| `BF38` | AuthenticateServerRequest |  | 5.7.13 | SGP.22 v2.7 |
| `BF38` | AuthenticateServerRequest |  | 5.7.13 | SGP.22 v2.2.2 |
| `BF38` | AuthenticateServerResponse |  | 5.14.3 | SGP.32 v1.3 |
| `BF38` | AuthenticateServerResponse |  | 2.1 | SGP.32 v1.2 |
| `BF39` | initiateAuthenticationRequest | RemoteProfileProvisioningRequest | 6.6.1 | SGP.22 v3.1 |
| `BF39` | initiateAuthenticationRequest | RemoteProfileProvisioningRequest | 6.6.1 | SGP.22 v2.7 |
| `BF39` | initiateAuthenticationRequest | ProfilePolicyAuthorisationRule | 6.6.1 | SGP.22 v2.2.2 |
| `BF39` | EsipaMessageFromIpaToEim |  | 6.3.1 | SGP.32 v1.3 |
| `BF39` | EsipaMessageFromIpaToEim |  | 2.1 | SGP.32 v1.2 |
| `BF3A` | getBoundProfilePackageRequest | RemoteProfileProvisioningRequest | 6.6.1 | SGP.22 v3.1 |
| `BF3A` | getBoundProfilePackageRequest | RemoteProfileProvisioningRequest | 6.6.1 | SGP.22 v2.7 |
| `BF3A` | getBoundProfilePackageRequest | ProfilePolicyAuthorisationRule | 6.6.1 | SGP.22 v2.2.2 |
| `BF3A` | EsipaMessageFromIpaToEim |  | 6.3.1 | SGP.32 v1.3 |
| `BF3A` | EsipaMessageFromIpaToEim |  | 2.1 | SGP.32 v1.2 |
| `BF3B` | authenticateClientRequest | RemoteProfileProvisioningRequest | 6.6.1 | SGP.22 v3.1 |
| `BF3B` | authenticateClientRequest | RemoteProfileProvisioningRequest | 6.6.1 | SGP.22 v2.7 |
| `BF3B` | authenticateClientRequest | ProfilePolicyAuthorisationRule | 6.6.1 | SGP.22 v2.2.2 |
| `BF3B` | AuthenticateClientRequest |  | 5.6.1 | SGP.32 v1.3 |
| `BF3B` | EsipaMessageFromIpaToEim |  | 2.1 | SGP.32 v1.2 |
| `BF3C` | EuiccConfiguredDataRequest |  | 5.7.3 | SGP.22 v3.1 |
| `BF3C` | EuiccConfiguredAddressesRequest |  | 5.7.3 | SGP.22 v2.7 |
| `BF3C` | EuiccConfiguredAddressesRequest |  | 5.7.3 | SGP.22 v2.2.2 |
| `BF3D` | HandleNotification |  | 6.6.2 | SGP.22 v3.1 |
| `BF3D` | HandleNotification |  | 6.6.2 | SGP.22 v2.7 |
| `BF3D` | HandleNotification |  | 6.6.2 | SGP.22 v2.2.2 |
| `BF3D` | handleNotificationEsipa | EsipaMessageFromIpaToEim | 6.3.1 | SGP.32 v1.3 |
| `BF3D` | handleNotificationEsipa | EsipaMessageFromIpaToEim | 2.1 | SGP.32 v1.2 |
| `BF3E` | GetEuiccDataRequest |  | 5.7.20 | SGP.22 v3.1 |
| `BF3E` | GetEuiccDataRequest |  | 5.7.20 | SGP.22 v2.7 |
| `BF3E` | GetEuiccDataRequest |  | 5.7.20 | SGP.22 v2.2.2 |
| `BF3F` | SetDefaultDpAddressRequest |  | 5.7.4 | SGP.22 v3.1 |
| `BF3F` | SetDefaultDpAddressRequest |  | 5.7.4 | SGP.22 v2.7 |
| `BF3F` | SetDefaultDpAddressRequest |  | 5.7.4 | SGP.22 v2.2.2 |
| `BF40` | authenticateClientResponseEs11 | RemoteProfileProvisioningResponse | 6.6.1 | SGP.22 v3.1 |
| `BF40` | authenticateClientResponseEs11 | RemoteProfileProvisioningResponse | 6.6.1 | SGP.22 v2.7 |
| `BF40` | authenticateClientResponseEs11 | RemoteProfileProvisioningResponse | 6.6.1 | SGP.22 v2.2.2 |
| `BF41` | CancelSessionRequest |  | 5.7.14 | SGP.22 v3.1 |
| `BF41` | CancelSessionRequest |  | 5.7.14 | SGP.22 v2.7 |
| `BF41` | CancelSessionRequest |  | 5.7.14 | SGP.22 v2.2.2 |
| `BF41` | CancelSessionResponse |  | 5.14.8 | SGP.32 v1.3 |
| `BF41` | CancelSessionResponse |  | 2.1 | SGP.32 v1.2 |
| `BF42` | LpaeActivationRequest |  | 5.7.1 | SGP.22 v3.1 |
| `BF42` | LpaeActivationRequest |  | 5.7.1 | SGP.22 v2.7 |
| `BF42` | LpaeActivationRequest |  | 5.7.1 | SGP.22 v2.2.2 |
| `BF42` | IpaeActivationRequest |  | 3.8.4 | SGP.32 v1.3 |
| `BF42` | IpaeActivationRequest |  | 2.1 | SGP.32 v1.2 |
| `BF43` | GetRatRequest |  | 5.7.22 | SGP.22 v3.1 |
| `BF43` | GetRatResponse |  | 5.7.22 | SGP.22 v2.7 |
| `BF43` | GetRatResponse |  | 5.7.22 | SGP.22 v2.2.2 |
| `BF44` | LoadRpmPackageResult |  | 2.10.2 | SGP.22 v3.1 |
| `BF45` | VerifySmdsResponseRequest |  | 5.7.24 | SGP.22 v3.1 |
| `BF46` | checkEventRequest | RemoteProfileProvisioningRequest | 6.6.1 | SGP.22 v3.1 |
| `BF4A` | AlertData |  | 5.7.23 | SGP.22 v3.1 |
| `BF4B` | VerifyDeviceChangeRequest |  | 5.7.27 | SGP.22 v3.1 |
| `BF4C` | confirmDeviceChangeRequest | RemoteProfileProvisioningRequest | 6.6.1 | SGP.22 v3.1 |
| `BF4D` | PrepareDeviceChangeRequest |  | 5.7.26 | SGP.22 v3.1 |
| `BF4E` | transferEimPackageResponse | EsipaMessageFromIpaToEim | 6.3.1 | SGP.32 v1.3 |
| `BF4E` | transferEimPackageResponse | EsipaMessageFromIpaToEim | 2.1 | SGP.32 v1.2 |
| `BF4F` | getEimPackageRequest | EsipaMessageFromIpaToEim | 6.3.1 | SGP.32 v1.3 |
| `BF4F` | getEimPackageRequest | EsipaMessageFromIpaToEim | 2.1 | SGP.32 v1.2 |
| `BF50` | provideEimPackageResult | EsipaMessageFromIpaToEim | 6.3.1 | SGP.32 v1.3 |
| `BF50` | provideEimPackageResult | EsipaMessageFromIpaToEim | 2.1 | SGP.32 v1.2 |
| `BF51` | EuiccPackageResult |  | 2.11.2.1 | SGP.32 v1.3 |
| `BF51` | euiccPackageRequest | GetEimPackageResponse | 2.1 | SGP.32 v1.2 |
| `BF52` | IpaEuiccDataRequest |  | 2.11.1.2 | SGP.32 v1.3 |
| `BF52` | ipaEuiccDataRequest | GetEimPackageResponse | 2.1 | SGP.32 v1.2 |
| `BF53` | EimAcknowledgements |  | 2.11.1.4 | SGP.32 v1.3 |
| `BF53` | eimAcknowledgements | ProvideEimPackageResultResponse | 2.1 | SGP.32 v1.2 |
| `BF54` | ProfileDownloadTriggerRequest |  | 2.11.1.3 | SGP.32 v1.3 |
| `BF54` | AuthenticateClientOkDSEsipa |  | 2.1 | SGP.32 v1.2 |
| `BF55` | GetEimConfigurationDataRequest |  | 5.9.18 | SGP.32 v1.3 |
| `BF55` | GetEimConfigurationDataRequest |  | 2.1 | SGP.32 v1.2 |
| `BF56` | GetCertsRequest |  | 5.9.10 | SGP.32 v1.3 |
| `BF56` | GetCertsRequest |  | 2.1 | SGP.32 v1.2 |
| `BF57` | AddInitialEimRequest |  | 5.9.4 | SGP.32 v1.3 |
| `BF57` | AddInitialEimRequest |  | 2.1 | SGP.32 v1.2 |
| `BF58` | ProfileRollbackRequest |  | 5.9.16 | SGP.32 v1.3 |
| `BF58` | ProfileRollbackRequest |  | 2.1 | SGP.32 v1.2 |
| `BF59` | ConfigureImmediateProfileEnablingRequest |  | 5.9.17 | SGP.32 v1.3 |
| `BF59` | ConfigureImmediateProfileEnablingRequest |  | 2.1 | SGP.32 v1.2 |
| `BF5A` | ImmediateEnableRequest |  | 5.9.15 | SGP.32 v1.3 |
| `BF5A` | ImmediateEnableRequest |  | 2.1 | SGP.32 v1.2 |
| `BF5B` | EnableEmergencyProfileRequest |  | 5.9.22 | SGP.32 v1.3 |
| `BF5B` | EnableEmergencyProfileRequest |  | 2.1 | SGP.32 v1.2 |
| `BF5C` | DisableEmergencyProfileRequest |  | 5.9.23 | SGP.32 v1.3 |
| `BF5C` | DisableEmergencyProfileRequest |  | 2.1 | SGP.32 v1.2 |
| `BF5D` | ExecuteFallbackMechanismRequest |  | 5.9.20 | SGP.32 v1.3 |
| `BF5E` | ReturnFromFallbackRequest |  | 5.9.21 | SGP.32 v1.3 |
| `BF5E` | ReturnFromFallbackRequest |  | 2.1 | SGP.32 v1.2 |
| `BF5F` | GetConnectivityParametersRequest |  | 5.9.24 | SGP.32 v1.3 |
| `BF5F` | GetConnectivityParametersRequest |  | 2.1 | SGP.32 v1.2 |
| `BF60` | VerifySmdpResponseRequest |  | 5.7.28 | SGP.22 v3.1 |
| `BF61` | checkProgressRequest | RemoteProfileProvisioningRequest | 6.6.1 | SGP.22 v3.1 |
| `BF62` | VerifyProfileRecoveryRequest |  | 5.7.29 | SGP.22 v3.1 |
| `BF63` | DeleteNotificationForDc |  | 4.1.3 | SGP.22 v3.1 |
| `BF64` | StoreMetadataRequest |  | 5.5.3 | SGP.22 v2.7 |
| `BF64` | IpaCapabilities |  | 4.4 | SGP.32 v1.3 |
| `BF64` | EuiccMemoryResetRequest |  | 2.1 | SGP.32 v1.2 |
| `BF65` | setDefaultDpAddress | Psmo | 2.11.1.1 | SGP.32 v1.3 |
| `BF65` | setDefaultDpAddress | Psmo | 2.1 | SGP.32 v1.2 |

---

## Lookup keys

Alternate spellings and query forms that should resolve to a row above:

- spaced and unspaced hex: `BF36` and `BF 36`
- quoted ASN.1 form: `Tag 'BF36'`
- bracketed tag number: `[54]` is the same tag as `BF36`
- structure names: `BoundProfilePackage`, `ProfileInstallationResult`,
  `EUICCInfo2`, `ProfileDownloadTriggerRequest`
- field names: `serviceDescription`, `serverSigned1`, `euiccCiPKIdentifiers`

## Stats

- distinct named tags: 128
- tag occurrences in corpus: 2170
- source documents: 35

Rows are included only where the source document names the tag. Hex values that
appear solely as prose mentions (GlobalPlatform X.509 certificate field tags such
as `Tag '42'`) are excluded as a different namespace.
