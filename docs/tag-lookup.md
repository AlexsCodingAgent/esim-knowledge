---
layout: default
title: "eSIM TLV Tag Lookup: Every ASN.1 Tag in SGP.22, SGP.32 and the Card Standards"
description: "Look up any ASN.1 TLV tag returned by an eUICC, IPA, eIM or LPA. Every tag in GSMA SGP.22, SGP.32, SGP.31, SGP.02 and SGP.41 plus ETSI TS 102 221 and 3GPP TS 31.102, with the structure it belongs to, the spec clause and the source line. Search BF36, BF37, 9F1F, 5F37, BF54 and 180 more."
---

# Tag Lookup

Every ASN.1 TLV tag that appears in the eSIM and smart-card specifications this
site covers, in one searchable table. Type a hex value to find what it means, or
type a name to find its tag.

Each row is extracted from the specification text itself rather than from memory,
so every entry carries the **structure** it belongs to, the **clause** that
defines it, and the **spec version** it came from. Where versions disagree, both
rows appear and the difference is visible.


**Corpus:** 128 named tags, 2,170 tag occurrences across 35 spec documents.


Rows are included when the source document actually names the tag, either as an
ASN.1 structure or field, or as a labelled 3GPP/ETSI tag element. A further
56 hex values appear in the corpus only as prose
mentions, mostly GlobalPlatform X.509 certificate field tags such as `Tag '42'`,
which belong to a different namespace and are excluded so a lookup here never
returns a nameless row.

<style>
.tl-search{width:100%;padding:.75rem 1rem;font-size:1.05rem;font-family:inherit;
  background:rgba(93,173,226,.08);border:1px solid #1b3a5c;border-radius:8px;
  color:#c8d6e5;margin:1rem 0 .5rem;box-sizing:border-box}
.tl-search:focus{outline:none;border-color:#5dade2;background:rgba(93,173,226,.14)}
[data-theme="light"] .tl-search{background:#f7fafc;border-color:#e2e8f0;color:#2d3748}
.tl-count{font-size:.85rem;color:#8b9dc3;margin-bottom:1rem}
.tl-wrap{max-height:70vh;overflow:auto;border:1px solid #1b3a5c;border-radius:8px}
table.tl{border-collapse:collapse;width:100%;font-size:.86rem;margin:0}
table.tl th{position:sticky;top:0;background:#0d1d30;text-align:left;padding:.55rem .7rem;
  border-bottom:1px solid #1b3a5c;z-index:2;font-weight:600}
table.tl td{padding:.45rem .7rem;border-bottom:1px solid rgba(27,58,92,.5);vertical-align:top}
table.tl tr:hover td{background:rgba(93,173,226,.06)}
table.tl code{background:rgba(93,173,226,.14);padding:.08rem .35rem;border-radius:3px;
  font-size:.85rem;white-space:nowrap;color:#85c1e9}
table.tl .tagcell code{font-weight:700;color:#fbbf24;font-size:.92rem}
table.tl .clause{color:#8b9dc3;white-space:nowrap;font-size:.8rem}
[data-theme="light"] .tl-wrap{border-color:#e2e8f0}
[data-theme="light"] table.tl th{background:#edf2f7;border-color:#e2e8f0;color:#1a202c}
[data-theme="light"] table.tl td{border-color:#edf2f7;color:#2d3748}
[data-theme="light"] table.tl td a{color:#2b6cb0}
[data-theme="light"] table.tl .clause{color:#718096}
[data-theme="light"] table.tl code{background:rgba(49,130,206,.1);color:#2b6cb0}
[data-theme="light"] table.tl .tagcell code{color:#b7791f}
[data-theme="light"] .tl-count{color:#718096}
</style>

<input type="search" id="tl-search" class="tl-search"
  placeholder="Search a tag or a name: BF36, 9F1F, GetEuiccInfo, ProfileInstallationResult&hellip;"
  aria-label="Search tags">
<div class="tl-count" id="tl-count"></div>

<div class="tl-wrap">
<table class="tl" id="tl-table">
<thead><tr><th>Tag</th><th>Name</th><th>Structure</th><th>Clause</th><th>Spec</th></tr></thead>
<tbody>
<tr data-s="03 uicccapability uicccapability `uicccapability` 8.2.7 tca interop v3.4"><td class="tagcell"><code>03</code></td><td>`UICCCapability`</td><td></td><td class="clause">8.2.7</td><td>TCA Interop v3.4</td></tr>
<tr data-s="5a euiccpackagesigned euiccpackagesigned `euiccpackagesigned` 2.11.1.1 sgp.32 v1.3"><td class="tagcell"><code>5A</code></td><td>`EuiccPackageSigned`</td><td></td><td class="clause">2.11.1.1</td><td>SGP.32 v1.3</td></tr>
<tr data-s="5a compactothersignednotification compactothersignednotification `compactothersignednotification` 2.1 sgp.32 v1.2"><td class="tagcell"><code>5A</code></td><td>`CompactOtherSignedNotification`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="5c ipaeuiccdatarequest ipaeuiccdatarequest `ipaeuiccdatarequest` 2.11.1.2 sgp.32 v1.3"><td class="tagcell"><code>5C</code></td><td>`IpaEuiccDataRequest`</td><td></td><td class="clause">2.11.1.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="5c ipaeuiccdatarequest ipaeuiccdatarequest `ipaeuiccdatarequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>5C</code></td><td>`IpaEuiccDataRequest`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="80 controlreftemplate controlreftemplate `controlreftemplate` 5.5.1 sgp.22 v3.1"><td class="tagcell"><code>80</code></td><td>`ControlRefTemplate`</td><td></td><td class="clause">5.5.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="80 controlreftemplate controlreftemplate `controlreftemplate` 5.5.1 sgp.22 v2.7"><td class="tagcell"><code>80</code></td><td>`ControlRefTemplate`</td><td></td><td class="clause">5.5.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="80 controlreftemplate controlreftemplate `controlreftemplate` 5.5.1 sgp.22 v2.2.2"><td class="tagcell"><code>80</code></td><td>`ControlRefTemplate`</td><td></td><td class="clause">5.5.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="80 mms implementation `mms implementation` 4.2.69 31102-j50"><td class="tagcell"><code>80</code></td><td>`MMS Implementation`</td><td></td><td class="clause">4.2.69</td><td>31102-j50</td></tr>
<tr data-s="80 naf_id `naf_id` 4.2.10 31103-e11"><td class="tagcell"><code>80</code></td><td>`NAF_ID`</td><td></td><td class="clause">4.2.10</td><td>31103-e11</td></tr>
<tr data-s="80 plmn `plmn` 8.100 31111-j40"><td class="tagcell"><code>80</code></td><td>`PLMN`</td><td></td><td class="clause">8.100</td><td>31111-j40</td></tr>
<tr data-s="80 naf_id `naf_id` 4.2.10 etsi-ts-131-103-v14.1.1"><td class="tagcell"><code>80</code></td><td>`NAF_ID`</td><td></td><td class="clause">4.2.10</td><td>ETSI-TS-131-103-v14.1.1</td></tr>
<tr data-s="81 pollingaddress rpmconfiguration `pollingaddress` in `rpmconfiguration` 2.4.12 sgp.22 v3.1"><td class="tagcell"><code>81</code></td><td>`pollingAddress` in `RpmConfiguration`</td><td>`RpmConfiguration`</td><td class="clause">2.4.12</td><td>SGP.22 v3.1</td></tr>
<tr data-s="81 controlreftemplate controlreftemplate `controlreftemplate` 5.5.1 sgp.22 v2.7"><td class="tagcell"><code>81</code></td><td>`ControlRefTemplate`</td><td></td><td class="clause">5.5.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="81 controlreftemplate controlreftemplate `controlreftemplate` 5.5.1 sgp.22 v2.2.2"><td class="tagcell"><code>81</code></td><td>`ControlRefTemplate`</td><td></td><td class="clause">5.5.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="81 defaultsmdpaddress ipaeuiccdata `defaultsmdpaddress` in `ipaeuiccdata` 2.11.2.2 sgp.32 v1.3"><td class="tagcell"><code>81</code></td><td>`defaultSmdpAddress` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.11.2.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="81 defaultsmdpaddress ipaeuiccdata `defaultsmdpaddress` in `ipaeuiccdata` 2.1 sgp.32 v1.2"><td class="tagcell"><code>81</code></td><td>`defaultSmdpAddress` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="81 polygon `polygon` 4.2.112 31102-j50"><td class="tagcell"><code>81</code></td><td>`Polygon`</td><td></td><td class="clause">4.2.112</td><td>31102-j50</td></tr>
<tr data-s="81 b-tid `b-tid` 4.2.10 31103-e11"><td class="tagcell"><code>81</code></td><td>`B-TID`</td><td></td><td class="clause">4.2.10</td><td>31103-e11</td></tr>
<tr data-s="81 csg id and name `csg id and name` 8.100 31111-j40"><td class="tagcell"><code>81</code></td><td>`CSG ID and Name`</td><td></td><td class="clause">8.100</td><td>31111-j40</td></tr>
<tr data-s="81 b-tid `b-tid` 4.2.10 etsi-ts-131-103-v14.1.1"><td class="tagcell"><code>81</code></td><td>`B-TID`</td><td></td><td class="clause">4.2.10</td><td>ETSI-TS-131-103-v14.1.1</td></tr>
<tr data-s="82 interface to core network and bearer information `interface to core network and bearer information` 4.2.69 31102-j50"><td class="tagcell"><code>82</code></td><td>`Interface to Core Network and Bearer Information`</td><td></td><td class="clause">4.2.69</td><td>31102-j50</td></tr>
<tr data-s="82 ber-tlv object returned with `ber-tlv object returned with` 11.1.20.5.2 etsi-ts-102-221-v18.4.0"><td class="tagcell"><code>82</code></td><td>`BER-TLV object returned with`</td><td></td><td class="clause">11.1.20.5.2</td><td>ETSI-TS-102-221-v18.4.0</td></tr>
<tr data-s="83 eimtransactionid ipaeuiccdatarequest `eimtransactionid` in `ipaeuiccdatarequest` 2.11.1.2 sgp.32 v1.3"><td class="tagcell"><code>83</code></td><td>`eimTransactionId` in `IpaEuiccDataRequest`</td><td>`IpaEuiccDataRequest`</td><td class="clause">2.11.1.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="83 eimtransactionid ipaeuiccdatarequest `eimtransactionid` in `ipaeuiccdatarequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>83</code></td><td>`eimTransactionId` in `IpaEuiccDataRequest`</td><td>`IpaEuiccDataRequest`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="83 gateway `gateway` 4.2.69 31102-j50"><td class="tagcell"><code>83</code></td><td>`Gateway`</td><td></td><td class="clause">4.2.69</td><td>31102-j50</td></tr>
<tr data-s="84 hostid controlreftemplate `hostid` in `controlreftemplate` 5.5.1 sgp.22 v3.1"><td class="tagcell"><code>84</code></td><td>`hostId` in `ControlRefTemplate`</td><td>`ControlRefTemplate`</td><td class="clause">5.5.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="84 hostid controlreftemplate `hostid` in `controlreftemplate` 5.5.1 sgp.22 v2.7"><td class="tagcell"><code>84</code></td><td>`hostId` in `ControlRefTemplate`</td><td>`ControlRefTemplate`</td><td class="clause">5.5.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="84 hostid controlreftemplate `hostid` in `controlreftemplate` 5.5.1 sgp.22 v2.2.2"><td class="tagcell"><code>84</code></td><td>`hostId` in `ControlRefTemplate`</td><td>`ControlRefTemplate`</td><td class="clause">5.5.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="84 associationtoken ipaeuiccdata `associationtoken` in `ipaeuiccdata` 2.11.2.2 sgp.32 v1.3"><td class="tagcell"><code>84</code></td><td>`associationToken` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.11.2.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="84 associationtoken ipaeuiccdata `associationtoken` in `ipaeuiccdata` 2.1 sgp.32 v1.2"><td class="tagcell"><code>84</code></td><td>`associationToken` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="84 reserved for 3gpp2: mms authentication mechanism `reserved for 3gpp2: mms authentication mechanism` 4.2.69 31102-j50"><td class="tagcell"><code>84</code></td><td>`Reserved for 3GPP2: MMS Authentication Mechanism`</td><td></td><td class="clause">4.2.69</td><td>31102-j50</td></tr>
<tr data-s="85 deviceinfo deviceinfo `deviceinfo` 4.2 sgp.22 v3.1"><td class="tagcell"><code>85</code></td><td>`DeviceInfo`</td><td></td><td class="clause">4.2</td><td>SGP.22 v3.1</td></tr>
<tr data-s="85 reserved for 3gpp2: mms authentication user name `reserved for 3gpp2: mms authentication user name` 4.2.69 31102-j50"><td class="tagcell"><code>85</code></td><td>`Reserved for 3GPP2: MMS Authentication User Name`</td><td></td><td class="clause">4.2.69</td><td>31102-j50</td></tr>
<tr data-s="86 plmn identifier `plmn identifier` 4.4.11.4 31102-j50"><td class="tagcell"><code>86</code></td><td>`PLMN identifier`</td><td></td><td class="clause">4.4.11.4</td><td>31102-j50</td></tr>
<tr data-s="87 eimtransactionid ipaeuiccdata `eimtransactionid` in `ipaeuiccdata` 2.11.2.2 sgp.32 v1.3"><td class="tagcell"><code>87</code></td><td>`eimTransactionId` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.11.2.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="87 eimtransactionid ipaeuiccdata `eimtransactionid` in `ipaeuiccdata` 2.1 sgp.32 v1.2"><td class="tagcell"><code>87</code></td><td>`eimTransactionId` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="87 privacy config `privacy config` 4.4.13.4 31102-j50"><td class="tagcell"><code>87</code></td><td>`Privacy config`</td><td></td><td class="clause">4.4.13.4</td><td>31102-j50</td></tr>
<tr data-s="88 g prose direct communication in nr-pc5 `g prose direct communication in nr-pc5` 4.4.13.4 31102-j50"><td class="tagcell"><code>88</code></td><td>`G ProSe direct communication in NR-PC5`</td><td></td><td class="clause">4.4.13.4</td><td>31102-j50</td></tr>
<tr data-s="89 prose application to path preference mapping rules `prose application to path preference mapping rules` 4.4.13.4 31102-j50"><td class="tagcell"><code>89</code></td><td>`ProSe application to path preference mapping rules`</td><td></td><td class="clause">4.4.13.4</td><td>31102-j50</td></tr>
<tr data-s="8a discovery signalling for solicitation `discovery signalling for solicitation` 4.4.13.10 31102-j50"><td class="tagcell"><code>8A</code></td><td>`discovery signalling for solicitation`</td><td></td><td class="clause">4.4.13.10</td><td>31102-j50</td></tr>
<tr data-s="8b rsc info list `rsc info list` 4.4.13.10 31102-j50"><td class="tagcell"><code>8B</code></td><td>`RSC info list`</td><td></td><td class="clause">4.4.13.10</td><td>31102-j50</td></tr>
<tr data-s="8c qi to pc5 qos parameters mapping rules `qi to pc5 qos parameters mapping rules` 4.4.13.10 31102-j50"><td class="tagcell"><code>8C</code></td><td>`QI to PC5 QoS parameters mapping rules`</td><td></td><td class="clause">4.4.13.10</td><td>31102-j50</td></tr>
<tr data-s="8e user info id for discovery `user info id for discovery` 4.4.13.10 31102-j50"><td class="tagcell"><code>8E</code></td><td>`User info ID for discovery`</td><td></td><td class="clause">4.4.13.10</td><td>31102-j50</td></tr>
<tr data-s="8f announcement and additional information `announcement and additional information` 4.4.13.12 31102-j50"><td class="tagcell"><code>8F</code></td><td>`announcement and additional information`</td><td></td><td class="clause">4.4.13.12</td><td>31102-j50</td></tr>
<tr data-s="90 profilenickname profileinfolistresponse `profilenickname` in `profileinfolistresponse` 5.7.15 sgp.22 v3.1"><td class="tagcell"><code>90</code></td><td>`profileNickname` in `ProfileInfoListResponse`</td><td>`ProfileInfoListResponse`</td><td class="clause">5.7.15</td><td>SGP.22 v3.1</td></tr>
<tr data-s="90 profilenickname profileinfolistresponse `profilenickname` in `profileinfolistresponse` 5.7.15 sgp.22 v2.7"><td class="tagcell"><code>90</code></td><td>`profileNickname` in `ProfileInfoListResponse`</td><td>`ProfileInfoListResponse`</td><td class="clause">5.7.15</td><td>SGP.22 v2.7</td></tr>
<tr data-s="90 profilenickname profileinfolistresponse `profilenickname` in `profileinfolistresponse` 5.7.15 sgp.22 v2.2.2"><td class="tagcell"><code>90</code></td><td>`profileNickname` in `ProfileInfoListResponse`</td><td>`ProfileInfoListResponse`</td><td class="clause">5.7.15</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="90 profilenickname ipacapabilities `profilenickname` in `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>90</code></td><td>`profileNickname` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="90 profilenickname ipacapabilities `profilenickname` in `ipacapabilities` 2.1 sgp.32 v1.2"><td class="tagcell"><code>90</code></td><td>`profileNickname` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="91 serviceprovidername verifyprofilerecoveryresponse `serviceprovidername` in `verifyprofilerecoveryresponse` 5.11.3 sgp.22 v3.1"><td class="tagcell"><code>91</code></td><td>`serviceProviderName` in `VerifyProfileRecoveryResponse`</td><td>`VerifyProfileRecoveryResponse`</td><td class="clause">5.11.3</td><td>SGP.22 v3.1</td></tr>
<tr data-s="91 serviceprovidername updatemetadatarequest `serviceprovidername` in `updatemetadatarequest` 5.4.1 sgp.22 v2.7"><td class="tagcell"><code>91</code></td><td>`serviceProviderName` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="91 serviceprovidername updatemetadatarequest `serviceprovidername` in `updatemetadatarequest` 5.4.1 sgp.22 v2.2.2"><td class="tagcell"><code>91</code></td><td>`serviceProviderName` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="91 serviceprovidername ipacapabilities `serviceprovidername` in `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>91</code></td><td>`serviceProviderName` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="91 serviceprovidername ipacapabilities `serviceprovidername` in `ipacapabilities` 2.1 sgp.32 v1.2"><td class="tagcell"><code>91</code></td><td>`serviceProviderName` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="91 rules `rules` 4.4.13.4 31102-j50"><td class="tagcell"><code>91</code></td><td>`rules`</td><td></td><td class="clause">4.4.13.4</td><td>31102-j50</td></tr>
<tr data-s="92 profilename verifyprofilerecoveryresponse `profilename` in `verifyprofilerecoveryresponse` 5.11.3 sgp.22 v3.1"><td class="tagcell"><code>92</code></td><td>`profileName` in `VerifyProfileRecoveryResponse`</td><td>`VerifyProfileRecoveryResponse`</td><td class="clause">5.11.3</td><td>SGP.22 v3.1</td></tr>
<tr data-s="92 profilename updatemetadatarequest `profilename` in `updatemetadatarequest` 5.4.1 sgp.22 v2.7"><td class="tagcell"><code>92</code></td><td>`profileName` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="92 profilename updatemetadatarequest `profilename` in `updatemetadatarequest` 5.4.1 sgp.22 v2.2.2"><td class="tagcell"><code>92</code></td><td>`profileName` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="92 profilename ipacapabilities `profilename` in `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>92</code></td><td>`profileName` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="92 profilename ipacapabilities `profilename` in `ipacapabilities` 2.1 sgp.32 v1.2"><td class="tagcell"><code>92</code></td><td>`profileName` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="92 privacy timer `privacy timer` 4.4.13.10 31102-j50"><td class="tagcell"><code>92</code></td><td>`Privacy timer`</td><td></td><td class="clause">4.4.13.10</td><td>31102-j50</td></tr>
<tr data-s="93 icontype updatemetadatarequest `icontype` in `updatemetadatarequest` 5.4.1 sgp.22 v3.1"><td class="tagcell"><code>93</code></td><td>`iconType` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="93 icontype updatemetadatarequest `icontype` in `updatemetadatarequest` 5.4.1 sgp.22 v2.7"><td class="tagcell"><code>93</code></td><td>`iconType` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="93 icontype updatemetadatarequest `icontype` in `updatemetadatarequest` 5.4.1 sgp.22 v2.2.2"><td class="tagcell"><code>93</code></td><td>`iconType` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="93 icontype ipacapabilities `icontype` in `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>93</code></td><td>`iconType` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="93 icontype ipacapabilities `icontype` in `ipacapabilities` 2.1 sgp.32 v1.2"><td class="tagcell"><code>93</code></td><td>`iconType` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="93 g pkmf address information `g pkmf address information` 4.4.13.10 31102-j50"><td class="tagcell"><code>93</code></td><td>`G PKMF address information`</td><td></td><td class="clause">4.4.13.10</td><td>31102-j50</td></tr>
<tr data-s="94 icon updatemetadatarequest `icon` in `updatemetadatarequest` 5.4.1 sgp.22 v3.1"><td class="tagcell"><code>94</code></td><td>`icon` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="94 icon updatemetadatarequest `icon` in `updatemetadatarequest` 5.4.1 sgp.22 v2.7"><td class="tagcell"><code>94</code></td><td>`icon` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="94 icon updatemetadatarequest `icon` in `updatemetadatarequest` 5.4.1 sgp.22 v2.2.2"><td class="tagcell"><code>94</code></td><td>`icon` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="94 icon ipacapabilities `icon` in `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>94</code></td><td>`icon` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="94 icon ipacapabilities `icon` in `ipacapabilities` 2.1 sgp.32 v1.2"><td class="tagcell"><code>94</code></td><td>`icon` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="94 collection period `collection period` 4.4.13.7 31102-j50"><td class="tagcell"><code>94</code></td><td>`Collection period`</td><td></td><td class="clause">4.4.13.7</td><td>31102-j50</td></tr>
<tr data-s="95 profileclass storemetadatarequest `profileclass` in `storemetadatarequest` 5.5.3 sgp.22 v3.1"><td class="tagcell"><code>95</code></td><td>`profileClass` in `StoreMetadataRequest`</td><td>`StoreMetadataRequest`</td><td class="clause">5.5.3</td><td>SGP.22 v3.1</td></tr>
<tr data-s="95 profileclass storemetadatarequest `profileclass` in `storemetadatarequest` 5.5.3 sgp.22 v2.7"><td class="tagcell"><code>95</code></td><td>`profileClass` in `StoreMetadataRequest`</td><td>`StoreMetadataRequest`</td><td class="clause">5.5.3</td><td>SGP.22 v2.7</td></tr>
<tr data-s="95 profileclass storemetadatarequest `profileclass` in `storemetadatarequest` 5.5.3 sgp.22 v2.2.2"><td class="tagcell"><code>95</code></td><td>`profileClass` in `StoreMetadataRequest`</td><td>`StoreMetadataRequest`</td><td class="clause">5.5.3</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="95 profileclass ipacapabilities `profileclass` in `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>95</code></td><td>`profileClass` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="95 profileclass ipacapabilities `profileclass` in `ipacapabilities` 2.1 sgp.32 v1.2"><td class="tagcell"><code>95</code></td><td>`profileClass` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="95 reporting window `reporting window` 4.4.13.7 31102-j50"><td class="tagcell"><code>95</code></td><td>`Reporting window`</td><td></td><td class="clause">4.4.13.7</td><td>31102-j50</td></tr>
<tr data-s="96 reporting indicators `reporting indicators` 4.4.13.7 31102-j50"><td class="tagcell"><code>96</code></td><td>`Reporting indicators`</td><td></td><td class="clause">4.4.13.7</td><td>31102-j50</td></tr>
<tr data-s="98 hplmn 5g ddnmf address information `hplmn 5g ddnmf address information` 4.4.13.3 31102-j50"><td class="tagcell"><code>98</code></td><td>`HPLMN 5G DDNMF address information`</td><td></td><td class="clause">4.4.13.3</td><td>31102-j50</td></tr>
<tr data-s="99 forbiddenprofilepolicyrules euiccinfo2 `forbiddenprofilepolicyrules` in `euiccinfo2` 4.2 sgp.22 v3.1"><td class="tagcell"><code>99</code></td><td>`forbiddenProfilePolicyRules` in `EUICCInfo2`</td><td>`EUICCInfo2`</td><td class="clause">4.2</td><td>SGP.22 v3.1</td></tr>
<tr data-s="99 profilepolicyrules updatemetadatarequest `profilepolicyrules` in `updatemetadatarequest` 5.4.1 sgp.22 v2.7"><td class="tagcell"><code>99</code></td><td>`profilePolicyRules` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="99 profilepolicyrules updatemetadatarequest `profilepolicyrules` in `updatemetadatarequest` 5.4.1 sgp.22 v2.2.2"><td class="tagcell"><code>99</code></td><td>`profilePolicyRules` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="99 profilepolicyrules ipacapabilities `profilepolicyrules` in `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>99</code></td><td>`profilePolicyRules` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="99 profilepolicyrules ipacapabilities `profilepolicyrules` in `ipacapabilities` 2.1 sgp.32 v1.2"><td class="tagcell"><code>99</code></td><td>`profilePolicyRules` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="99 solicitation `solicitation` 4.4.13.13 31102-j50"><td class="tagcell"><code>99</code></td><td>`solicitation`</td><td></td><td class="clause">4.4.13.13</td><td>31102-j50</td></tr>
<tr data-s="9a discovery `discovery` 4.4.13.8 31102-j50"><td class="tagcell"><code>9A</code></td><td>`discovery`</td><td></td><td class="clause">4.4.13.8</td><td>31102-j50</td></tr>
<tr data-s="9b hriserveraddress updatemetadatarequest `hriserveraddress` in `updatemetadatarequest` 5.4.1 sgp.22 v3.1"><td class="tagcell"><code>9B</code></td><td>`hriServerAddress` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="9b warning message broadcast `warning message broadcast` 4.4.13.10 31102-j50"><td class="tagcell"><code>9B</code></td><td>`Warning message broadcast`</td><td></td><td class="clause">4.4.13.10</td><td>31102-j50</td></tr>
<tr data-s="a0 notificationslist ipaeuiccdata `notificationslist` in `ipaeuiccdata` 2.11.2.2 sgp.32 v1.3"><td class="tagcell"><code>A0</code></td><td>`notificationsList` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.11.2.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="a0 notificationlist eimpackageresult `notificationlist` in `eimpackageresult` 2.1 sgp.32 v1.2"><td class="tagcell"><code>A0</code></td><td>`notificationList` in `EimPackageResult`</td><td>`EimPackageResult`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="a0 muk id `muk id` 4.2.81 31102-j50"><td class="tagcell"><code>A0</code></td><td>`MUK ID`</td><td></td><td class="clause">4.2.81</td><td>31102-j50</td></tr>
<tr data-s="a1 pdu info list data object `pdu info list data object` 4.4.14.2 31102-j50"><td class="tagcell"><code>A1</code></td><td>`PDU Info List data object`</td><td></td><td class="clause">4.4.14.2</td><td>31102-j50</td></tr>
<tr data-s="a2 remoteprofileprovisioningrequest remoteprofileprovisioningrequest `remoteprofileprovisioningrequest` 6.6.1 sgp.22 v3.1"><td class="tagcell"><code>A2</code></td><td>`RemoteProfileProvisioningRequest`</td><td></td><td class="clause">6.6.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="a2 remoteprofileprovisioningrequest remoteprofileprovisioningrequest `remoteprofileprovisioningrequest` 6.6.1 sgp.22 v2.7"><td class="tagcell"><code>A2</code></td><td>`RemoteProfileProvisioningRequest`</td><td></td><td class="clause">6.6.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="a2 profilepolicyauthorisationrule profilepolicyauthorisationrule `profilepolicyauthorisationrule` 6.6.1 sgp.22 v2.2.2"><td class="tagcell"><code>A2</code></td><td>`ProfilePolicyAuthorisationRule`</td><td></td><td class="clause">6.6.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="a2 euiccpackageresultlist ipaeuiccdata `euiccpackageresultlist` in `ipaeuiccdata` 2.11.2.2 sgp.32 v1.3"><td class="tagcell"><code>A2</code></td><td>`euiccPackageResultList` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.11.2.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="a2 euiccpackageresultlist ipaeuiccdata `euiccpackageresultlist` in `ipaeuiccdata` 2.1 sgp.32 v1.2"><td class="tagcell"><code>A2</code></td><td>`euiccPackageResultList` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="a5 eumcertificate ipaeuiccdata `eumcertificate` in `ipaeuiccdata` 2.11.2.2 sgp.32 v1.3"><td class="tagcell"><code>A5</code></td><td>`eumCertificate` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.11.2.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="a5 eumcertificate ipaeuiccdata `eumcertificate` in `ipaeuiccdata` 2.1 sgp.32 v1.2"><td class="tagcell"><code>A5</code></td><td>`eumCertificate` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="a6 euicccertificate ipaeuiccdata `euicccertificate` in `ipaeuiccdata` 2.11.2.2 sgp.32 v1.3"><td class="tagcell"><code>A6</code></td><td>`euiccCertificate` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.11.2.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="a6 euicccertificate ipaeuiccdata `euicccertificate` in `ipaeuiccdata` 2.1 sgp.32 v1.2"><td class="tagcell"><code>A6</code></td><td>`euiccCertificate` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="a8 ipacapabilities ipaeuiccdata `ipacapabilities` in `ipaeuiccdata` 2.11.2.2 sgp.32 v1.3"><td class="tagcell"><code>A8</code></td><td>`ipaCapabilities` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.11.2.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="a8 ipacapabilities ipaeuiccdata `ipacapabilities` in `ipaeuiccdata` 2.1 sgp.32 v1.2"><td class="tagcell"><code>A8</code></td><td>`ipaCapabilities` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="a8 constructed `constructed` 4.4.2.1 31102-j50"><td class="tagcell"><code>A8</code></td><td>`constructed`</td><td></td><td class="clause">4.4.2.1</td><td>31102-j50</td></tr>
<tr data-s="a9 deviceinfo ipaeuiccdata `deviceinfo` in `ipaeuiccdata` 2.11.2.2 sgp.32 v1.3"><td class="tagcell"><code>A9</code></td><td>`deviceInfo` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.11.2.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="a9 deviceinfo ipaeuiccdata `deviceinfo` in `ipaeuiccdata` 2.1 sgp.32 v1.2"><td class="tagcell"><code>A9</code></td><td>`deviceInfo` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="a9 file ids indicated using constructed `file ids indicated using constructed` 4.4.2.1 31102-j50"><td class="tagcell"><code>A9</code></td><td>`File Ids indicated using constructed`</td><td></td><td class="clause">4.4.2.1</td><td>31102-j50</td></tr>
<tr data-s="aa file ids indicated using constructed `file ids indicated using constructed` 4.4.2.1 31102-j50"><td class="tagcell"><code>AA</code></td><td>`File Ids indicated using constructed`</td><td></td><td class="clause">4.4.2.1</td><td>31102-j50</td></tr>
<tr data-s="ab mms connectivity parameters `mms connectivity parameters` 4.2.69 31102-j50"><td class="tagcell"><code>AB</code></td><td>`MMS Connectivity Parameters`</td><td></td><td class="clause">4.2.69</td><td>31102-j50</td></tr>
<tr data-s="b5 lparspcapability initiateauthenticationrequest `lparspcapability` in `initiateauthenticationrequest` 6.6.2 sgp.22 v3.1"><td class="tagcell"><code>B5</code></td><td>`lpaRspCapability` in `InitiateAuthenticationRequest`</td><td>`InitiateAuthenticationRequest`</td><td class="clause">6.6.2</td><td>SGP.22 v3.1</td></tr>
<tr data-s="b6 updatemetadatarequest updatemetadatarequest `updatemetadatarequest` 5.4.1 sgp.22 v3.1"><td class="tagcell"><code>B6</code></td><td>`UpdateMetadataRequest`</td><td></td><td class="clause">5.4.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="b6 profileinfolistresponse profileinfolistresponse `profileinfolistresponse` 5.7.15 sgp.22 v2.7"><td class="tagcell"><code>B6</code></td><td>`ProfileInfoListResponse`</td><td></td><td class="clause">5.7.15</td><td>SGP.22 v2.7</td></tr>
<tr data-s="b6 profileinfolistresponse profileinfolistresponse `profileinfolistresponse` 5.7.15 sgp.22 v2.2.2"><td class="tagcell"><code>B6</code></td><td>`ProfileInfoListResponse`</td><td></td><td class="clause">5.7.15</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="b6 ipacapabilities ipacapabilities `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>B6</code></td><td>`IpaCapabilities`</td><td></td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="b6 ipacapabilities ipacapabilities `ipacapabilities` 2.1 sgp.32 v1.2"><td class="tagcell"><code>B6</code></td><td>`IpaCapabilities`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="b7 profileowner storemetadatarequest `profileowner` in `storemetadatarequest` 5.5.3 sgp.22 v3.1"><td class="tagcell"><code>B7</code></td><td>`profileOwner` in `StoreMetadataRequest`</td><td>`StoreMetadataRequest`</td><td class="clause">5.5.3</td><td>SGP.22 v3.1</td></tr>
<tr data-s="b7 profileowner storemetadatarequest `profileowner` in `storemetadatarequest` 5.5.3 sgp.22 v2.7"><td class="tagcell"><code>B7</code></td><td>`profileOwner` in `StoreMetadataRequest`</td><td>`StoreMetadataRequest`</td><td class="clause">5.5.3</td><td>SGP.22 v2.7</td></tr>
<tr data-s="b7 profileowner storemetadatarequest `profileowner` in `storemetadatarequest` 5.5.3 sgp.22 v2.2.2"><td class="tagcell"><code>B7</code></td><td>`profileOwner` in `StoreMetadataRequest`</td><td>`StoreMetadataRequest`</td><td class="clause">5.5.3</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="b7 profileowner ipacapabilities `profileowner` in `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>B7</code></td><td>`profileOwner` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="b7 profileowner ipacapabilities `profileowner` in `ipacapabilities` 2.1 sgp.32 v1.2"><td class="tagcell"><code>B7</code></td><td>`profileOwner` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="b8 dpproprietarydata configureisdprequest `dpproprietarydata` in `configureisdprequest` 5.5.2 sgp.22 v3.1"><td class="tagcell"><code>B8</code></td><td>`dpProprietaryData` in `ConfigureISDPRequest`</td><td>`ConfigureISDPRequest`</td><td class="clause">5.5.2</td><td>SGP.22 v3.1</td></tr>
<tr data-s="b8 dpproprietarydata configureisdprequest `dpproprietarydata` in `configureisdprequest` 5.5.2 sgp.22 v2.7"><td class="tagcell"><code>B8</code></td><td>`dpProprietaryData` in `ConfigureISDPRequest`</td><td>`ConfigureISDPRequest`</td><td class="clause">5.5.2</td><td>SGP.22 v2.7</td></tr>
<tr data-s="b8 dpproprietarydata configureisdprequest `dpproprietarydata` in `configureisdprequest` 5.5.2 sgp.22 v2.2.2"><td class="tagcell"><code>B8</code></td><td>`dpProprietaryData` in `ConfigureISDPRequest`</td><td>`ConfigureISDPRequest`</td><td class="clause">5.5.2</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="b8 dpproprietarydata ipacapabilities `dpproprietarydata` in `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>B8</code></td><td>`dpProprietaryData` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="b8 dpproprietarydata ipacapabilities `dpproprietarydata` in `ipacapabilities` 2.1 sgp.32 v1.2"><td class="tagcell"><code>B8</code></td><td>`dpProprietaryData` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="ba rpmconfiguration updatemetadatarequest `rpmconfiguration` in `updatemetadatarequest` 5.4.1 sgp.22 v3.1"><td class="tagcell"><code>BA</code></td><td>`rpmConfiguration` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bc updatemetadatarequest updatemetadatarequest `updatemetadatarequest` 5.4.1 sgp.22 v3.1"><td class="tagcell"><code>BC</code></td><td>`UpdateMetadataRequest`</td><td></td><td class="clause">5.4.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bd updatemetadatarequest updatemetadatarequest `updatemetadatarequest` 5.4.1 sgp.22 v3.1"><td class="tagcell"><code>BD</code></td><td>`UpdateMetadataRequest`</td><td></td><td class="clause">5.4.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="be storemetadatarequest storemetadatarequest `storemetadatarequest` 5.5.3 sgp.22 v3.1"><td class="tagcell"><code>BE</code></td><td>`StoreMetadataRequest`</td><td></td><td class="clause">5.5.3</td><td>SGP.22 v3.1</td></tr>
<tr data-s="da checkprogressok checkprogressok `checkprogressok` 6.6.2 sgp.22 v3.1"><td class="tagcell"><code>DA</code></td><td>`CheckProgressOk`</td><td></td><td class="clause">6.6.2</td><td>SGP.22 v3.1</td></tr>
<tr data-s="da evententries evententries `evententries` 6.6.2 sgp.22 v2.7"><td class="tagcell"><code>DA</code></td><td>`EventEntries`</td><td></td><td class="clause">6.6.2</td><td>SGP.22 v2.7</td></tr>
<tr data-s="da evententries evententries `evententries` 6.6.2 sgp.22 v2.2.2"><td class="tagcell"><code>DA</code></td><td>`EventEntries`</td><td></td><td class="clause">6.6.2</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="da eimpackageerrorwithcid eimpackageerrorwithcid `eimpackageerrorwithcid` 6.4.1.8 sgp.32 v1.3"><td class="tagcell"><code>DA</code></td><td>`EimPackageErrorWithCid`</td><td></td><td class="clause">6.4.1.8</td><td>SGP.32 v1.3</td></tr>
<tr data-s="da epc `epc` 1.1.1 23003-k00"><td class="tagcell"><code>DA</code></td><td>`EPC`</td><td></td><td class="clause">1.1.1</td><td>23003-k00</td></tr>
<tr data-s="da nfcaccessrule nfcaccessrule `nfcaccessrule` 7.4 gpd_spe_013-secure-element-access-control"><td class="tagcell"><code>DA</code></td><td>`NFCAccessRule`</td><td></td><td class="clause">7.4</td><td>GPD_SPE_013-Secure-Element-Access-Control</td></tr>
<tr data-s="de tag value `tag value` 4.2.66 31102-j50"><td class="tagcell"><code>DE</code></td><td>`Tag Value`</td><td></td><td class="clause">4.2.66</td><td>31102-j50</td></tr>
<tr data-s="e0 replacesessionkeysrequest replacesessionkeysrequest `replacesessionkeysrequest` 5.7.1 sgp.22 v3.1"><td class="tagcell"><code>E0</code></td><td>`ReplaceSessionKeysRequest`</td><td></td><td class="clause">5.7.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="e0 replacesessionkeysrequest replacesessionkeysrequest `replacesessionkeysrequest` 5.7.1 sgp.22 v2.7"><td class="tagcell"><code>E0</code></td><td>`ReplaceSessionKeysRequest`</td><td></td><td class="clause">5.7.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="e0 replacesessionkeysrequest replacesessionkeysrequest `replacesessionkeysrequest` 5.7.1 sgp.22 v2.2.2"><td class="tagcell"><code>E0</code></td><td>`ReplaceSessionKeysRequest`</td><td></td><td class="clause">5.7.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="e1 profiledownloadtriggerresult profiledownloadtriggerresult `profiledownloadtriggerresult` 3.8.4 sgp.32 v1.3"><td class="tagcell"><code>E1</code></td><td>`ProfileDownloadTriggerResult`</td><td></td><td class="clause">3.8.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="e1 profiledownloadtriggerresult profiledownloadtriggerresult `profiledownloadtriggerresult` 2.1 sgp.32 v1.2"><td class="tagcell"><code>E1</code></td><td>`ProfileDownloadTriggerResult`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="e3 profileinfolistresponse profileinfolistresponse `profileinfolistresponse` 5.7.15 sgp.22 v3.1"><td class="tagcell"><code>E3</code></td><td>`ProfileInfoListResponse`</td><td></td><td class="clause">5.7.15</td><td>SGP.22 v3.1</td></tr>
<tr data-s="e3 profileinfolistresponse profileinfolistresponse `profileinfolistresponse` 5.7.15 sgp.22 v2.7"><td class="tagcell"><code>E3</code></td><td>`ProfileInfoListResponse`</td><td></td><td class="clause">5.7.15</td><td>SGP.22 v2.7</td></tr>
<tr data-s="e3 profileinfolistresponse profileinfolistresponse `profileinfolistresponse` 5.7.15 sgp.22 v2.2.2"><td class="tagcell"><code>E3</code></td><td>`ProfileInfoListResponse`</td><td></td><td class="clause">5.7.15</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="e3 ipacapabilities ipacapabilities `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>E3</code></td><td>`IpaCapabilities`</td><td></td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="e3 ipacapabilities ipacapabilities `ipacapabilities` 2.1 sgp.32 v1.2"><td class="tagcell"><code>E3</code></td><td>`IpaCapabilities`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="e4 verifyprofilerecoveryresponse verifyprofilerecoveryresponse `verifyprofilerecoveryresponse` 5.11.3 sgp.22 v3.1"><td class="tagcell"><code>E4</code></td><td>`VerifyProfileRecoveryResponse`</td><td></td><td class="clause">5.11.3</td><td>SGP.22 v3.1</td></tr>
<tr data-s="5f37 profileinstallationresultdata profileinstallationresultdata `profileinstallationresultdata` 2.5.6 sgp.22 v3.1"><td class="tagcell"><code>5F37</code></td><td>`ProfileInstallationResultData`</td><td></td><td class="clause">2.5.6</td><td>SGP.22 v3.1</td></tr>
<tr data-s="5f37 profileinstallationresultdata profileinstallationresultdata `profileinstallationresultdata` 2.5.6 sgp.22 v2.7"><td class="tagcell"><code>5F37</code></td><td>`ProfileInstallationResultData`</td><td></td><td class="clause">2.5.6</td><td>SGP.22 v2.7</td></tr>
<tr data-s="5f37 profileinstallationresultdata profileinstallationresultdata `profileinstallationresultdata` 2.5.6 sgp.22 v2.2.2"><td class="tagcell"><code>5F37</code></td><td>`ProfileInstallationResultData`</td><td></td><td class="clause">2.5.6</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="5f37 euiccpackagerequest euiccpackagerequest `euiccpackagerequest` 2.11.1.1 sgp.32 v1.3"><td class="tagcell"><code>5F37</code></td><td>`EuiccPackageRequest`</td><td></td><td class="clause">2.11.1.1</td><td>SGP.32 v1.3</td></tr>
<tr data-s="5f37 compactothersignednotification compactothersignednotification `compactothersignednotification` 2.1 sgp.32 v1.2"><td class="tagcell"><code>5F37</code></td><td>`CompactOtherSignedNotification`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="9f1f storemetadatarequest storemetadatarequest `storemetadatarequest` 5.5.3 sgp.22 v3.1"><td class="tagcell"><code>9F1F</code></td><td>`StoreMetadataRequest`</td><td></td><td class="clause">5.5.3</td><td>SGP.22 v3.1</td></tr>
<tr data-s="9f21 estimatedprofilesize storemetadatarequest `estimatedprofilesize` in `storemetadatarequest` 5.5.3 sgp.22 v3.1"><td class="tagcell"><code>9F21</code></td><td>`estimatedProfileSize` in `StoreMetadataRequest`</td><td>`StoreMetadataRequest`</td><td class="clause">5.5.3</td><td>SGP.22 v3.1</td></tr>
<tr data-s="9f24 enabledonesimport profileinfolistresponse `enabledonesimport` in `profileinfolistresponse` 5.7.15 sgp.22 v3.1"><td class="tagcell"><code>9F24</code></td><td>`enabledOnEsimPort` in `ProfileInfoListResponse`</td><td>`ProfileInfoListResponse`</td><td class="clause">5.7.15</td><td>SGP.22 v3.1</td></tr>
<tr data-s="9f25 profilesize profileinfolistresponse `profilesize` in `profileinfolistresponse` 5.7.15 sgp.22 v3.1"><td class="tagcell"><code>9F25</code></td><td>`profileSize` in `ProfileInfoListResponse`</td><td>`ProfileInfoListResponse`</td><td class="clause">5.7.15</td><td>SGP.22 v3.1</td></tr>
<tr data-s="9f26 fallbackattribute profileinfolistresponse `fallbackattribute` in `profileinfolistresponse` 5.7.15 sgp.22 v2.7"><td class="tagcell"><code>9F26</code></td><td>`fallbackAttribute` in `ProfileInfoListResponse`</td><td>`ProfileInfoListResponse`</td><td class="clause">5.7.15</td><td>SGP.22 v2.7</td></tr>
<tr data-s="9f26 fallbackattribute ipacapabilities `fallbackattribute` in `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>9F26</code></td><td>`fallbackAttribute` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="9f26 fallbackattribute ipacapabilities `fallbackattribute` in `ipacapabilities` 2.1 sgp.32 v1.2"><td class="tagcell"><code>9F26</code></td><td>`fallbackAttribute` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="9f2a updatemetadataresponse updatemetadataresponse `updatemetadataresponse` 5.4.1 sgp.22 v3.1"><td class="tagcell"><code>9F2A</code></td><td>`UpdateMetadataResponse`</td><td></td><td class="clause">5.4.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="9f67 reserved103 updatemetadatarequest `reserved103` in `updatemetadatarequest` 5.4.1 sgp.22 v2.7"><td class="tagcell"><code>9F67</code></td><td>`reserved103` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="9f67 fallbackallowed ipacapabilities `fallbackallowed` in `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>9F67</code></td><td>`fallbackAllowed` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="9f67 fallbackallowed ipacapabilities `fallbackallowed` in `ipacapabilities` 2.1 sgp.32 v1.2"><td class="tagcell"><code>9F67</code></td><td>`fallbackAllowed` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="9f70 profilestate verifyprofilerecoveryresponse `profilestate` in `verifyprofilerecoveryresponse` 5.11.3 sgp.22 v3.1"><td class="tagcell"><code>9F70</code></td><td>`profileState` in `VerifyProfileRecoveryResponse`</td><td>`VerifyProfileRecoveryResponse`</td><td class="clause">5.11.3</td><td>SGP.22 v3.1</td></tr>
<tr data-s="9f70 profilestate profileinfolistresponse `profilestate` in `profileinfolistresponse` 5.7.15 sgp.22 v2.7"><td class="tagcell"><code>9F70</code></td><td>`profileState` in `ProfileInfoListResponse`</td><td>`ProfileInfoListResponse`</td><td class="clause">5.7.15</td><td>SGP.22 v2.7</td></tr>
<tr data-s="9f70 profilestate profileinfolistresponse `profilestate` in `profileinfolistresponse` 5.7.15 sgp.22 v2.2.2"><td class="tagcell"><code>9F70</code></td><td>`profileState` in `ProfileInfoListResponse`</td><td>`ProfileInfoListResponse`</td><td class="clause">5.7.15</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="9f70 profilestate ipacapabilities `profilestate` in `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>9F70</code></td><td>`profileState` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="9f70 profilestate ipacapabilities `profilestate` in `ipacapabilities` 2.1 sgp.32 v1.2"><td class="tagcell"><code>9F70</code></td><td>`profileState` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="9f78 euiccinfo2ext euiccinfo2ext `euiccinfo2ext` 5.4.11.2 sgp.23-v1.16"><td class="tagcell"><code>9F78</code></td><td>`EuiccInfo2Ext`</td><td></td><td class="clause">5.4.11.2</td><td>SGP.23-v1.16</td></tr>
<tr data-s="9f7b ecallindication storemetadatarequest `ecallindication` in `storemetadatarequest` 5.5.3 sgp.22 v2.7"><td class="tagcell"><code>9F7B</code></td><td>`ecallIndication` in `StoreMetadataRequest`</td><td>`StoreMetadataRequest`</td><td class="clause">5.5.3</td><td>SGP.22 v2.7</td></tr>
<tr data-s="9f7b ecallindication ipacapabilities `ecallindication` in `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>9F7B</code></td><td>`ecallIndication` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="9f7b ecallindication ipacapabilities `ecallindication` in `ipacapabilities` 2.1 sgp.32 v1.2"><td class="tagcell"><code>9F7B</code></td><td>`ecallIndication` in `IpaCapabilities`</td><td>`IpaCapabilities`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf20 euiccinfo1 euiccinfo1 `euiccinfo1` 4.2 sgp.22 v3.1"><td class="tagcell"><code>BF20</code></td><td>`EUICCInfo1`</td><td></td><td class="clause">4.2</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf20 geteuiccinfo1request geteuiccinfo1request `geteuiccinfo1request` 5.7.8 sgp.22 v2.7"><td class="tagcell"><code>BF20</code></td><td>`GetEuiccInfo1Request`</td><td></td><td class="clause">5.7.8</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf20 geteuiccinfo1request geteuiccinfo1request `geteuiccinfo1request` 5.7.8 sgp.22 v2.2.2"><td class="tagcell"><code>BF20</code></td><td>`GetEuiccInfo1Request`</td><td></td><td class="clause">5.7.8</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf20 euiccinfo1 ipaeuiccdata `euiccinfo1` in `ipaeuiccdata` 2.11.2.2 sgp.32 v1.3"><td class="tagcell"><code>BF20</code></td><td>`euiccInfo1` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.11.2.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf20 euiccinfo1 ipaeuiccdata `euiccinfo1` in `ipaeuiccdata` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF20</code></td><td>`euiccInfo1` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf20 serviceslist serviceslist `serviceslist` 8.2.1 tca pkg v3.4.1"><td class="tagcell"><code>BF20</code></td><td>`ServicesList`</td><td></td><td class="clause">8.2.1</td><td>TCA Pkg v3.4.1</td></tr>
<tr data-s="bf20 uicccapability uicccapability `uicccapability` 8.1.2 tca interop v3.4"><td class="tagcell"><code>BF20</code></td><td>`UICCCapability`</td><td></td><td class="clause">8.1.2</td><td>TCA Interop v3.4</td></tr>
<tr data-s="bf20 table b-1: contents of `table b-1: contents of` gpc_spe_093-amendment-f-scp11"><td class="tagcell"><code>BF20</code></td><td>`Table B-1: Contents of`</td><td></td><td class="clause"></td><td>GPC_SPE_093-Amendment-F-SCP11</td></tr>
<tr data-s="bf20 uicccapability uicccapability `uicccapability` tca-euicc-profile-package-v3.4.1"><td class="tagcell"><code>BF20</code></td><td>`UICCCapability`</td><td></td><td class="clause"></td><td>TCA-eUICC-Profile-Package-v3.4.1</td></tr>
<tr data-s="bf21 preparedownloadrequest preparedownloadrequest `preparedownloadrequest` 5.7.5 sgp.22 v3.1"><td class="tagcell"><code>BF21</code></td><td>`PrepareDownloadRequest`</td><td></td><td class="clause">5.7.5</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf21 preparedownloadrequest preparedownloadrequest `preparedownloadrequest` 5.7.5 sgp.22 v2.7"><td class="tagcell"><code>BF21</code></td><td>`PrepareDownloadRequest`</td><td></td><td class="clause">5.7.5</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf21 preparedownloadrequest preparedownloadrequest `preparedownloadrequest` 5.7.5 sgp.22 v2.2.2"><td class="tagcell"><code>BF21</code></td><td>`PrepareDownloadRequest`</td><td></td><td class="clause">5.7.5</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf21 preparedownloadresponse preparedownloadresponse `preparedownloadresponse` 5.14.2 sgp.32 v1.3"><td class="tagcell"><code>BF21</code></td><td>`PrepareDownloadResponse`</td><td></td><td class="clause">5.14.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf21 preparedownloadresponse preparedownloadresponse `preparedownloadresponse` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF21</code></td><td>`PrepareDownloadResponse`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf22 euiccinfo2 euiccinfo2 `euiccinfo2` 4.2 sgp.22 v3.1"><td class="tagcell"><code>BF22</code></td><td>`EUICCInfo2`</td><td></td><td class="clause">4.2</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf22 servicespecificdatastoredineuicc updatemetadatarequest `servicespecificdatastoredineuicc` in `updatemetadatarequest` 5.4.1 sgp.22 v2.7"><td class="tagcell"><code>BF22</code></td><td>`serviceSpecificDataStoredInEuicc` in `UpdateMetadataRequest`</td><td>`UpdateMetadataRequest`</td><td class="clause">5.4.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf22 geteuiccinfo2request geteuiccinfo2request `geteuiccinfo2request` 5.7.8 sgp.22 v2.2.2"><td class="tagcell"><code>BF22</code></td><td>`GetEuiccInfo2Request`</td><td></td><td class="clause">5.7.8</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf22 euiccinfo2 ipaeuiccdata `euiccinfo2` in `ipaeuiccdata` 2.11.2.2 sgp.32 v1.3"><td class="tagcell"><code>BF22</code></td><td>`euiccInfo2` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.11.2.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf22 euiccinfo2 ipaeuiccdata `euiccinfo2` in `ipaeuiccdata` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF22</code></td><td>`euiccInfo2` in `IpaEuiccData`</td><td>`IpaEuiccData`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf23 initialisesecurechannelrequest boundprofilepackage `initialisesecurechannelrequest` in `boundprofilepackage` 2.5.4 sgp.22 v3.1"><td class="tagcell"><code>BF23</code></td><td>`initialiseSecureChannelRequest` in `BoundProfilePackage`</td><td>`BoundProfilePackage`</td><td class="clause">2.5.4</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf23 initialisesecurechannelrequest boundprofilepackage `initialisesecurechannelrequest` in `boundprofilepackage` 2.5.4 sgp.22 v2.7"><td class="tagcell"><code>BF23</code></td><td>`initialiseSecureChannelRequest` in `BoundProfilePackage`</td><td>`BoundProfilePackage`</td><td class="clause">2.5.4</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf23 initialisesecurechannelrequest boundprofilepackage `initialisesecurechannelrequest` in `boundprofilepackage` 2.5.4 sgp.22 v2.2.2"><td class="tagcell"><code>BF23</code></td><td>`initialiseSecureChannelRequest` in `BoundProfilePackage`</td><td>`BoundProfilePackage`</td><td class="clause">2.5.4</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf23 storemetadatarequest storemetadatarequest `storemetadatarequest` 5.5 sgp.32 v1.3"><td class="tagcell"><code>BF23</code></td><td>`StoreMetadataRequest`</td><td></td><td class="clause">5.5</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf24 configureisdprequest configureisdprequest `configureisdprequest` 5.5.2 sgp.22 v3.1"><td class="tagcell"><code>BF24</code></td><td>`ConfigureISDPRequest`</td><td></td><td class="clause">5.5.2</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf24 configureisdprequest configureisdprequest `configureisdprequest` 5.5.2 sgp.22 v2.7"><td class="tagcell"><code>BF24</code></td><td>`ConfigureISDPRequest`</td><td></td><td class="clause">5.5.2</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf24 configureisdprequest configureisdprequest `configureisdprequest` 5.5.2 sgp.22 v2.2.2"><td class="tagcell"><code>BF24</code></td><td>`ConfigureISDPRequest`</td><td></td><td class="clause">5.5.2</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf25 storemetadatarequest storemetadatarequest `storemetadatarequest` 5.5.3 sgp.22 v3.1"><td class="tagcell"><code>BF25</code></td><td>`StoreMetadataRequest`</td><td></td><td class="clause">5.5.3</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf25 storemetadatarequest storemetadatarequest `storemetadatarequest` 5.5.3 sgp.22 v2.7"><td class="tagcell"><code>BF25</code></td><td>`StoreMetadataRequest`</td><td></td><td class="clause">5.5.3</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf25 storemetadatarequest storemetadatarequest `storemetadatarequest` 5.5.3 sgp.22 v2.2.2"><td class="tagcell"><code>BF25</code></td><td>`StoreMetadataRequest`</td><td></td><td class="clause">5.5.3</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf25 storemetadatarequest storemetadatarequest `storemetadatarequest` 5.5 sgp.32 v1.3"><td class="tagcell"><code>BF25</code></td><td>`StoreMetadataRequest`</td><td></td><td class="clause">5.5</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf25 storemetadatarequest storemetadatarequest `storemetadatarequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF25</code></td><td>`StoreMetadataRequest`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf27 profileinstallationresultdata profileinstallationresultdata `profileinstallationresultdata` 2.5.6 sgp.22 v3.1"><td class="tagcell"><code>BF27</code></td><td>`ProfileInstallationResultData`</td><td></td><td class="clause">2.5.6</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf27 profileinstallationresultdata profileinstallationresultdata `profileinstallationresultdata` 2.5.6 sgp.22 v2.7"><td class="tagcell"><code>BF27</code></td><td>`ProfileInstallationResultData`</td><td></td><td class="clause">2.5.6</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf27 profileinstallationresultdata profileinstallationresultdata `profileinstallationresultdata` 2.5.6 sgp.22 v2.2.2"><td class="tagcell"><code>BF27</code></td><td>`ProfileInstallationResultData`</td><td></td><td class="clause">2.5.6</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf28 listnotificationrequest listnotificationrequest `listnotificationrequest` 5.7.9 sgp.22 v3.1"><td class="tagcell"><code>BF28</code></td><td>`ListNotificationRequest`</td><td></td><td class="clause">5.7.9</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf28 listnotificationrequest listnotificationrequest `listnotificationrequest` 5.7.9 sgp.22 v2.7"><td class="tagcell"><code>BF28</code></td><td>`ListNotificationRequest`</td><td></td><td class="clause">5.7.9</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf28 listnotificationrequest listnotificationrequest `listnotificationrequest` 5.7.9 sgp.22 v2.2.2"><td class="tagcell"><code>BF28</code></td><td>`ListNotificationRequest`</td><td></td><td class="clause">5.7.9</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf29 setnicknamerequest setnicknamerequest `setnicknamerequest` 5.7.21 sgp.22 v3.1"><td class="tagcell"><code>BF29</code></td><td>`SetNicknameRequest`</td><td></td><td class="clause">5.7.21</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf29 setnicknamerequest setnicknamerequest `setnicknamerequest` 5.7.21 sgp.22 v2.7"><td class="tagcell"><code>BF29</code></td><td>`SetNicknameRequest`</td><td></td><td class="clause">5.7.21</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf29 setnicknamerequest setnicknamerequest `setnicknamerequest` 5.7.21 sgp.22 v2.2.2"><td class="tagcell"><code>BF29</code></td><td>`SetNicknameRequest`</td><td></td><td class="clause">5.7.21</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf2a updatemetadatarequest updatemetadatarequest `updatemetadatarequest` 5.4.1 sgp.22 v3.1"><td class="tagcell"><code>BF2A</code></td><td>`UpdateMetadataRequest`</td><td></td><td class="clause">5.4.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf2a updatemetadatarequest updatemetadatarequest `updatemetadatarequest` 5.4.1 sgp.22 v2.7"><td class="tagcell"><code>BF2A</code></td><td>`UpdateMetadataRequest`</td><td></td><td class="clause">5.4.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf2a updatemetadatarequest updatemetadatarequest `updatemetadatarequest` 5.4.1 sgp.22 v2.2.2"><td class="tagcell"><code>BF2A</code></td><td>`UpdateMetadataRequest`</td><td></td><td class="clause">5.4.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf2a updatemetadatarequest updatemetadatarequest `updatemetadatarequest` 5.4.2 sgp.32 v1.3"><td class="tagcell"><code>BF2A</code></td><td>`UpdateMetadataRequest`</td><td></td><td class="clause">5.4.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf2b retrievenotificationslistrequest retrievenotificationslistrequest `retrievenotificationslistrequest` 5.7.10 sgp.22 v3.1"><td class="tagcell"><code>BF2B</code></td><td>`RetrieveNotificationsListRequest`</td><td></td><td class="clause">5.7.10</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf2b retrievenotificationslistrequest retrievenotificationslistrequest `retrievenotificationslistrequest` 5.7.10 sgp.22 v2.7"><td class="tagcell"><code>BF2B</code></td><td>`RetrieveNotificationsListRequest`</td><td></td><td class="clause">5.7.10</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf2b retrievenotificationslistrequest retrievenotificationslistrequest `retrievenotificationslistrequest` 5.7.10 sgp.22 v2.2.2"><td class="tagcell"><code>BF2B</code></td><td>`RetrieveNotificationsListRequest`</td><td></td><td class="clause">5.7.10</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf2b retrievenotificationslistrequest retrievenotificationslistrequest `retrievenotificationslistrequest` 5.9.11 sgp.32 v1.3"><td class="tagcell"><code>BF2B</code></td><td>`RetrieveNotificationsListRequest`</td><td></td><td class="clause">5.9.11</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf2b retrievenotificationslistrequest retrievenotificationslistrequest `retrievenotificationslistrequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF2B</code></td><td>`RetrieveNotificationsListRequest`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf2d profileinfolistrequest profileinfolistrequest `profileinfolistrequest` 5.7.15 sgp.22 v3.1"><td class="tagcell"><code>BF2D</code></td><td>`ProfileInfoListRequest`</td><td></td><td class="clause">5.7.15</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf2d profileinfolistrequest profileinfolistrequest `profileinfolistrequest` 5.7.15 sgp.22 v2.7"><td class="tagcell"><code>BF2D</code></td><td>`ProfileInfoListRequest`</td><td></td><td class="clause">5.7.15</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf2d profileinfolistrequest profileinfolistrequest `profileinfolistrequest` 5.7.15 sgp.22 v2.2.2"><td class="tagcell"><code>BF2D</code></td><td>`ProfileInfoListRequest`</td><td></td><td class="clause">5.7.15</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf2d listprofileinfo psmo `listprofileinfo` in `psmo` 2.11.1.1 sgp.32 v1.3"><td class="tagcell"><code>BF2D</code></td><td>`listProfileInfo` in `Psmo`</td><td>`Psmo`</td><td class="clause">2.11.1.1</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf2d listprofileinfo psmo `listprofileinfo` in `psmo` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF2D</code></td><td>`listProfileInfo` in `Psmo`</td><td>`Psmo`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf2e geteuiccchallengerequest geteuiccchallengerequest `geteuiccchallengerequest` 5.7.7 sgp.22 v3.1"><td class="tagcell"><code>BF2E</code></td><td>`GetEuiccChallengeRequest`</td><td></td><td class="clause">5.7.7</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf2e geteuiccchallengerequest geteuiccchallengerequest `geteuiccchallengerequest` 5.7.7 sgp.22 v2.7"><td class="tagcell"><code>BF2E</code></td><td>`GetEuiccChallengeRequest`</td><td></td><td class="clause">5.7.7</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf2e geteuiccchallengerequest geteuiccchallengerequest `geteuiccchallengerequest` 5.7.7 sgp.22 v2.2.2"><td class="tagcell"><code>BF2E</code></td><td>`GetEuiccChallengeRequest`</td><td></td><td class="clause">5.7.7</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf2f notificationmetadata notificationmetadata `notificationmetadata` 5.7.9 sgp.22 v3.1"><td class="tagcell"><code>BF2F</code></td><td>`NotificationMetadata`</td><td></td><td class="clause">5.7.9</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf2f notificationmetadata notificationmetadata `notificationmetadata` 5.7.9 sgp.22 v2.7"><td class="tagcell"><code>BF2F</code></td><td>`NotificationMetadata`</td><td></td><td class="clause">5.7.9</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf2f notificationmetadata notificationmetadata `notificationmetadata` 5.7.9 sgp.22 v2.2.2"><td class="tagcell"><code>BF2F</code></td><td>`NotificationMetadata`</td><td></td><td class="clause">5.7.9</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf30 notificationsentrequest notificationsentrequest `notificationsentrequest` 5.7.11 sgp.22 v3.1"><td class="tagcell"><code>BF30</code></td><td>`NotificationSentRequest`</td><td></td><td class="clause">5.7.11</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf30 notificationsentrequest notificationsentrequest `notificationsentrequest` 5.7.11 sgp.22 v2.7"><td class="tagcell"><code>BF30</code></td><td>`NotificationSentRequest`</td><td></td><td class="clause">5.7.11</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf30 notificationsentrequest notificationsentrequest `notificationsentrequest` 5.7.11 sgp.22 v2.2.2"><td class="tagcell"><code>BF30</code></td><td>`NotificationSentRequest`</td><td></td><td class="clause">5.7.11</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf31 enableprofilerequest enableprofilerequest `enableprofilerequest` 5.7.16 sgp.22 v3.1"><td class="tagcell"><code>BF31</code></td><td>`EnableProfileRequest`</td><td></td><td class="clause">5.7.16</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf31 enableprofilerequest enableprofilerequest `enableprofilerequest` 5.7.16 sgp.22 v2.7"><td class="tagcell"><code>BF31</code></td><td>`EnableProfileRequest`</td><td></td><td class="clause">5.7.16</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf31 enableprofilerequest enableprofilerequest `enableprofilerequest` 5.7.16 sgp.22 v2.2.2"><td class="tagcell"><code>BF31</code></td><td>`EnableProfileRequest`</td><td></td><td class="clause">5.7.16</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf32 disableprofilerequest disableprofilerequest `disableprofilerequest` 5.7.17 sgp.22 v3.1"><td class="tagcell"><code>BF32</code></td><td>`DisableProfileRequest`</td><td></td><td class="clause">5.7.17</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf32 disableprofilerequest disableprofilerequest `disableprofilerequest` 5.7.17 sgp.22 v2.7"><td class="tagcell"><code>BF32</code></td><td>`DisableProfileRequest`</td><td></td><td class="clause">5.7.17</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf32 disableprofilerequest disableprofilerequest `disableprofilerequest` 5.7.17 sgp.22 v2.2.2"><td class="tagcell"><code>BF32</code></td><td>`DisableProfileRequest`</td><td></td><td class="clause">5.7.17</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf33 deleteprofilerequest deleteprofilerequest `deleteprofilerequest` 5.7.18 sgp.22 v3.1"><td class="tagcell"><code>BF33</code></td><td>`DeleteProfileRequest`</td><td></td><td class="clause">5.7.18</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf33 deleteprofilerequest deleteprofilerequest `deleteprofilerequest` 5.7.18 sgp.22 v2.7"><td class="tagcell"><code>BF33</code></td><td>`DeleteProfileRequest`</td><td></td><td class="clause">5.7.18</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf33 deleteprofilerequest deleteprofilerequest `deleteprofilerequest` 5.7.18 sgp.22 v2.2.2"><td class="tagcell"><code>BF33</code></td><td>`DeleteProfileRequest`</td><td></td><td class="clause">5.7.18</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf34 euiccmemoryresetrequest euiccmemoryresetrequest `euiccmemoryresetrequest` 5.7.19 sgp.22 v3.1"><td class="tagcell"><code>BF34</code></td><td>`EuiccMemoryResetRequest`</td><td></td><td class="clause">5.7.19</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf34 euiccmemoryresetrequest euiccmemoryresetrequest `euiccmemoryresetrequest` 5.7.19 sgp.22 v2.7"><td class="tagcell"><code>BF34</code></td><td>`EuiccMemoryResetRequest`</td><td></td><td class="clause">5.7.19</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf34 euiccmemoryresetrequest euiccmemoryresetrequest `euiccmemoryresetrequest` 5.7.19 sgp.22 v2.2.2"><td class="tagcell"><code>BF34</code></td><td>`EuiccMemoryResetRequest`</td><td></td><td class="clause">5.7.19</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf35 loadcrlrequest loadcrlrequest `loadcrlrequest` 5.7.12 sgp.22 v2.7"><td class="tagcell"><code>BF35</code></td><td>`LoadCRLRequest`</td><td></td><td class="clause">5.7.12</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf35 loadcrlrequest loadcrlrequest `loadcrlrequest` 5.7.12 sgp.22 v2.2.2"><td class="tagcell"><code>BF35</code></td><td>`LoadCRLRequest`</td><td></td><td class="clause">5.7.12</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf36 boundprofilepackage boundprofilepackage `boundprofilepackage` 2.5.4 sgp.22 v3.1"><td class="tagcell"><code>BF36</code></td><td>`BoundProfilePackage`</td><td></td><td class="clause">2.5.4</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf36 boundprofilepackage boundprofilepackage `boundprofilepackage` 2.5.4 sgp.22 v2.7"><td class="tagcell"><code>BF36</code></td><td>`BoundProfilePackage`</td><td></td><td class="clause">2.5.4</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf36 boundprofilepackage boundprofilepackage `boundprofilepackage` 2.5.4 sgp.22 v2.2.2"><td class="tagcell"><code>BF36</code></td><td>`BoundProfilePackage`</td><td></td><td class="clause">2.5.4</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf37 profileinstallationresult profileinstallationresult `profileinstallationresult` 2.5.6 sgp.22 v3.1"><td class="tagcell"><code>BF37</code></td><td>`ProfileInstallationResult`</td><td></td><td class="clause">2.5.6</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf37 profileinstallationresult profileinstallationresult `profileinstallationresult` 2.5.6 sgp.22 v2.7"><td class="tagcell"><code>BF37</code></td><td>`ProfileInstallationResult`</td><td></td><td class="clause">2.5.6</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf37 profileinstallationresult profileinstallationresult `profileinstallationresult` 2.5.6 sgp.22 v2.2.2"><td class="tagcell"><code>BF37</code></td><td>`ProfileInstallationResult`</td><td></td><td class="clause">2.5.6</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf37 profileinstallationresult profileinstallationresult `profileinstallationresult` 5.14.7 sgp.32 v1.3"><td class="tagcell"><code>BF37</code></td><td>`ProfileInstallationResult`</td><td></td><td class="clause">5.14.7</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf37 profileinstallationresult profileinstallationresult `profileinstallationresult` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF37</code></td><td>`ProfileInstallationResult`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf38 authenticateserverrequest authenticateserverrequest `authenticateserverrequest` 5.7.13 sgp.22 v3.1"><td class="tagcell"><code>BF38</code></td><td>`AuthenticateServerRequest`</td><td></td><td class="clause">5.7.13</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf38 authenticateserverrequest authenticateserverrequest `authenticateserverrequest` 5.7.13 sgp.22 v2.7"><td class="tagcell"><code>BF38</code></td><td>`AuthenticateServerRequest`</td><td></td><td class="clause">5.7.13</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf38 authenticateserverrequest authenticateserverrequest `authenticateserverrequest` 5.7.13 sgp.22 v2.2.2"><td class="tagcell"><code>BF38</code></td><td>`AuthenticateServerRequest`</td><td></td><td class="clause">5.7.13</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf38 authenticateserverresponse authenticateserverresponse `authenticateserverresponse` 5.14.3 sgp.32 v1.3"><td class="tagcell"><code>BF38</code></td><td>`AuthenticateServerResponse`</td><td></td><td class="clause">5.14.3</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf38 authenticateserverresponse authenticateserverresponse `authenticateserverresponse` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF38</code></td><td>`AuthenticateServerResponse`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf39 initiateauthenticationrequest remoteprofileprovisioningrequest `initiateauthenticationrequest` in `remoteprofileprovisioningrequest` 6.6.1 sgp.22 v3.1"><td class="tagcell"><code>BF39</code></td><td>`initiateAuthenticationRequest` in `RemoteProfileProvisioningRequest`</td><td>`RemoteProfileProvisioningRequest`</td><td class="clause">6.6.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf39 initiateauthenticationrequest remoteprofileprovisioningrequest `initiateauthenticationrequest` in `remoteprofileprovisioningrequest` 6.6.1 sgp.22 v2.7"><td class="tagcell"><code>BF39</code></td><td>`initiateAuthenticationRequest` in `RemoteProfileProvisioningRequest`</td><td>`RemoteProfileProvisioningRequest`</td><td class="clause">6.6.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf39 initiateauthenticationrequest profilepolicyauthorisationrule `initiateauthenticationrequest` in `profilepolicyauthorisationrule` 6.6.1 sgp.22 v2.2.2"><td class="tagcell"><code>BF39</code></td><td>`initiateAuthenticationRequest` in `ProfilePolicyAuthorisationRule`</td><td>`ProfilePolicyAuthorisationRule`</td><td class="clause">6.6.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf39 esipamessagefromipatoeim esipamessagefromipatoeim `esipamessagefromipatoeim` 6.3.1 sgp.32 v1.3"><td class="tagcell"><code>BF39</code></td><td>`EsipaMessageFromIpaToEim`</td><td></td><td class="clause">6.3.1</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf39 esipamessagefromipatoeim esipamessagefromipatoeim `esipamessagefromipatoeim` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF39</code></td><td>`EsipaMessageFromIpaToEim`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf3a getboundprofilepackagerequest remoteprofileprovisioningrequest `getboundprofilepackagerequest` in `remoteprofileprovisioningrequest` 6.6.1 sgp.22 v3.1"><td class="tagcell"><code>BF3A</code></td><td>`getBoundProfilePackageRequest` in `RemoteProfileProvisioningRequest`</td><td>`RemoteProfileProvisioningRequest`</td><td class="clause">6.6.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf3a getboundprofilepackagerequest remoteprofileprovisioningrequest `getboundprofilepackagerequest` in `remoteprofileprovisioningrequest` 6.6.1 sgp.22 v2.7"><td class="tagcell"><code>BF3A</code></td><td>`getBoundProfilePackageRequest` in `RemoteProfileProvisioningRequest`</td><td>`RemoteProfileProvisioningRequest`</td><td class="clause">6.6.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf3a getboundprofilepackagerequest profilepolicyauthorisationrule `getboundprofilepackagerequest` in `profilepolicyauthorisationrule` 6.6.1 sgp.22 v2.2.2"><td class="tagcell"><code>BF3A</code></td><td>`getBoundProfilePackageRequest` in `ProfilePolicyAuthorisationRule`</td><td>`ProfilePolicyAuthorisationRule`</td><td class="clause">6.6.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf3a esipamessagefromipatoeim esipamessagefromipatoeim `esipamessagefromipatoeim` 6.3.1 sgp.32 v1.3"><td class="tagcell"><code>BF3A</code></td><td>`EsipaMessageFromIpaToEim`</td><td></td><td class="clause">6.3.1</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf3a esipamessagefromipatoeim esipamessagefromipatoeim `esipamessagefromipatoeim` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF3A</code></td><td>`EsipaMessageFromIpaToEim`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf3b authenticateclientrequest remoteprofileprovisioningrequest `authenticateclientrequest` in `remoteprofileprovisioningrequest` 6.6.1 sgp.22 v3.1"><td class="tagcell"><code>BF3B</code></td><td>`authenticateClientRequest` in `RemoteProfileProvisioningRequest`</td><td>`RemoteProfileProvisioningRequest`</td><td class="clause">6.6.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf3b authenticateclientrequest remoteprofileprovisioningrequest `authenticateclientrequest` in `remoteprofileprovisioningrequest` 6.6.1 sgp.22 v2.7"><td class="tagcell"><code>BF3B</code></td><td>`authenticateClientRequest` in `RemoteProfileProvisioningRequest`</td><td>`RemoteProfileProvisioningRequest`</td><td class="clause">6.6.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf3b authenticateclientrequest profilepolicyauthorisationrule `authenticateclientrequest` in `profilepolicyauthorisationrule` 6.6.1 sgp.22 v2.2.2"><td class="tagcell"><code>BF3B</code></td><td>`authenticateClientRequest` in `ProfilePolicyAuthorisationRule`</td><td>`ProfilePolicyAuthorisationRule`</td><td class="clause">6.6.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf3b authenticateclientrequest authenticateclientrequest `authenticateclientrequest` 5.6.1 sgp.32 v1.3"><td class="tagcell"><code>BF3B</code></td><td>`AuthenticateClientRequest`</td><td></td><td class="clause">5.6.1</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf3b esipamessagefromipatoeim esipamessagefromipatoeim `esipamessagefromipatoeim` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF3B</code></td><td>`EsipaMessageFromIpaToEim`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf3c euiccconfigureddatarequest euiccconfigureddatarequest `euiccconfigureddatarequest` 5.7.3 sgp.22 v3.1"><td class="tagcell"><code>BF3C</code></td><td>`EuiccConfiguredDataRequest`</td><td></td><td class="clause">5.7.3</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf3c euiccconfiguredaddressesrequest euiccconfiguredaddressesrequest `euiccconfiguredaddressesrequest` 5.7.3 sgp.22 v2.7"><td class="tagcell"><code>BF3C</code></td><td>`EuiccConfiguredAddressesRequest`</td><td></td><td class="clause">5.7.3</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf3c euiccconfiguredaddressesrequest euiccconfiguredaddressesrequest `euiccconfiguredaddressesrequest` 5.7.3 sgp.22 v2.2.2"><td class="tagcell"><code>BF3C</code></td><td>`EuiccConfiguredAddressesRequest`</td><td></td><td class="clause">5.7.3</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf3d handlenotification handlenotification `handlenotification` 6.6.2 sgp.22 v3.1"><td class="tagcell"><code>BF3D</code></td><td>`HandleNotification`</td><td></td><td class="clause">6.6.2</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf3d handlenotification handlenotification `handlenotification` 6.6.2 sgp.22 v2.7"><td class="tagcell"><code>BF3D</code></td><td>`HandleNotification`</td><td></td><td class="clause">6.6.2</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf3d handlenotification handlenotification `handlenotification` 6.6.2 sgp.22 v2.2.2"><td class="tagcell"><code>BF3D</code></td><td>`HandleNotification`</td><td></td><td class="clause">6.6.2</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf3d handlenotificationesipa esipamessagefromipatoeim `handlenotificationesipa` in `esipamessagefromipatoeim` 6.3.1 sgp.32 v1.3"><td class="tagcell"><code>BF3D</code></td><td>`handleNotificationEsipa` in `EsipaMessageFromIpaToEim`</td><td>`EsipaMessageFromIpaToEim`</td><td class="clause">6.3.1</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf3d handlenotificationesipa esipamessagefromipatoeim `handlenotificationesipa` in `esipamessagefromipatoeim` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF3D</code></td><td>`handleNotificationEsipa` in `EsipaMessageFromIpaToEim`</td><td>`EsipaMessageFromIpaToEim`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf3e geteuiccdatarequest geteuiccdatarequest `geteuiccdatarequest` 5.7.20 sgp.22 v3.1"><td class="tagcell"><code>BF3E</code></td><td>`GetEuiccDataRequest`</td><td></td><td class="clause">5.7.20</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf3e geteuiccdatarequest geteuiccdatarequest `geteuiccdatarequest` 5.7.20 sgp.22 v2.7"><td class="tagcell"><code>BF3E</code></td><td>`GetEuiccDataRequest`</td><td></td><td class="clause">5.7.20</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf3e geteuiccdatarequest geteuiccdatarequest `geteuiccdatarequest` 5.7.20 sgp.22 v2.2.2"><td class="tagcell"><code>BF3E</code></td><td>`GetEuiccDataRequest`</td><td></td><td class="clause">5.7.20</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf3f setdefaultdpaddressrequest setdefaultdpaddressrequest `setdefaultdpaddressrequest` 5.7.4 sgp.22 v3.1"><td class="tagcell"><code>BF3F</code></td><td>`SetDefaultDpAddressRequest`</td><td></td><td class="clause">5.7.4</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf3f setdefaultdpaddressrequest setdefaultdpaddressrequest `setdefaultdpaddressrequest` 5.7.4 sgp.22 v2.7"><td class="tagcell"><code>BF3F</code></td><td>`SetDefaultDpAddressRequest`</td><td></td><td class="clause">5.7.4</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf3f setdefaultdpaddressrequest setdefaultdpaddressrequest `setdefaultdpaddressrequest` 5.7.4 sgp.22 v2.2.2"><td class="tagcell"><code>BF3F</code></td><td>`SetDefaultDpAddressRequest`</td><td></td><td class="clause">5.7.4</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf40 authenticateclientresponsees11 remoteprofileprovisioningresponse `authenticateclientresponsees11` in `remoteprofileprovisioningresponse` 6.6.1 sgp.22 v3.1"><td class="tagcell"><code>BF40</code></td><td>`authenticateClientResponseEs11` in `RemoteProfileProvisioningResponse`</td><td>`RemoteProfileProvisioningResponse`</td><td class="clause">6.6.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf40 authenticateclientresponsees11 remoteprofileprovisioningresponse `authenticateclientresponsees11` in `remoteprofileprovisioningresponse` 6.6.1 sgp.22 v2.7"><td class="tagcell"><code>BF40</code></td><td>`authenticateClientResponseEs11` in `RemoteProfileProvisioningResponse`</td><td>`RemoteProfileProvisioningResponse`</td><td class="clause">6.6.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf40 authenticateclientresponsees11 remoteprofileprovisioningresponse `authenticateclientresponsees11` in `remoteprofileprovisioningresponse` 6.6.1 sgp.22 v2.2.2"><td class="tagcell"><code>BF40</code></td><td>`authenticateClientResponseEs11` in `RemoteProfileProvisioningResponse`</td><td>`RemoteProfileProvisioningResponse`</td><td class="clause">6.6.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf41 cancelsessionrequest cancelsessionrequest `cancelsessionrequest` 5.7.14 sgp.22 v3.1"><td class="tagcell"><code>BF41</code></td><td>`CancelSessionRequest`</td><td></td><td class="clause">5.7.14</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf41 cancelsessionrequest cancelsessionrequest `cancelsessionrequest` 5.7.14 sgp.22 v2.7"><td class="tagcell"><code>BF41</code></td><td>`CancelSessionRequest`</td><td></td><td class="clause">5.7.14</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf41 cancelsessionrequest cancelsessionrequest `cancelsessionrequest` 5.7.14 sgp.22 v2.2.2"><td class="tagcell"><code>BF41</code></td><td>`CancelSessionRequest`</td><td></td><td class="clause">5.7.14</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf41 cancelsessionresponse cancelsessionresponse `cancelsessionresponse` 5.14.8 sgp.32 v1.3"><td class="tagcell"><code>BF41</code></td><td>`CancelSessionResponse`</td><td></td><td class="clause">5.14.8</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf41 cancelsessionresponse cancelsessionresponse `cancelsessionresponse` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF41</code></td><td>`CancelSessionResponse`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf42 lpaeactivationrequest lpaeactivationrequest `lpaeactivationrequest` 5.7.1 sgp.22 v3.1"><td class="tagcell"><code>BF42</code></td><td>`LpaeActivationRequest`</td><td></td><td class="clause">5.7.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf42 lpaeactivationrequest lpaeactivationrequest `lpaeactivationrequest` 5.7.1 sgp.22 v2.7"><td class="tagcell"><code>BF42</code></td><td>`LpaeActivationRequest`</td><td></td><td class="clause">5.7.1</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf42 lpaeactivationrequest lpaeactivationrequest `lpaeactivationrequest` 5.7.1 sgp.22 v2.2.2"><td class="tagcell"><code>BF42</code></td><td>`LpaeActivationRequest`</td><td></td><td class="clause">5.7.1</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf42 ipaeactivationrequest ipaeactivationrequest `ipaeactivationrequest` 3.8.4 sgp.32 v1.3"><td class="tagcell"><code>BF42</code></td><td>`IpaeActivationRequest`</td><td></td><td class="clause">3.8.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf42 ipaeactivationrequest ipaeactivationrequest `ipaeactivationrequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF42</code></td><td>`IpaeActivationRequest`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf43 getratrequest getratrequest `getratrequest` 5.7.22 sgp.22 v3.1"><td class="tagcell"><code>BF43</code></td><td>`GetRatRequest`</td><td></td><td class="clause">5.7.22</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf43 getratresponse getratresponse `getratresponse` 5.7.22 sgp.22 v2.7"><td class="tagcell"><code>BF43</code></td><td>`GetRatResponse`</td><td></td><td class="clause">5.7.22</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf43 getratresponse getratresponse `getratresponse` 5.7.22 sgp.22 v2.2.2"><td class="tagcell"><code>BF43</code></td><td>`GetRatResponse`</td><td></td><td class="clause">5.7.22</td><td>SGP.22 v2.2.2</td></tr>
<tr data-s="bf44 loadrpmpackageresult loadrpmpackageresult `loadrpmpackageresult` 2.10.2 sgp.22 v3.1"><td class="tagcell"><code>BF44</code></td><td>`LoadRpmPackageResult`</td><td></td><td class="clause">2.10.2</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf45 verifysmdsresponserequest verifysmdsresponserequest `verifysmdsresponserequest` 5.7.24 sgp.22 v3.1"><td class="tagcell"><code>BF45</code></td><td>`VerifySmdsResponseRequest`</td><td></td><td class="clause">5.7.24</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf46 checkeventrequest remoteprofileprovisioningrequest `checkeventrequest` in `remoteprofileprovisioningrequest` 6.6.1 sgp.22 v3.1"><td class="tagcell"><code>BF46</code></td><td>`checkEventRequest` in `RemoteProfileProvisioningRequest`</td><td>`RemoteProfileProvisioningRequest`</td><td class="clause">6.6.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf4a alertdata alertdata `alertdata` 5.7.23 sgp.22 v3.1"><td class="tagcell"><code>BF4A</code></td><td>`AlertData`</td><td></td><td class="clause">5.7.23</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf4b verifydevicechangerequest verifydevicechangerequest `verifydevicechangerequest` 5.7.27 sgp.22 v3.1"><td class="tagcell"><code>BF4B</code></td><td>`VerifyDeviceChangeRequest`</td><td></td><td class="clause">5.7.27</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf4c confirmdevicechangerequest remoteprofileprovisioningrequest `confirmdevicechangerequest` in `remoteprofileprovisioningrequest` 6.6.1 sgp.22 v3.1"><td class="tagcell"><code>BF4C</code></td><td>`confirmDeviceChangeRequest` in `RemoteProfileProvisioningRequest`</td><td>`RemoteProfileProvisioningRequest`</td><td class="clause">6.6.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf4d preparedevicechangerequest preparedevicechangerequest `preparedevicechangerequest` 5.7.26 sgp.22 v3.1"><td class="tagcell"><code>BF4D</code></td><td>`PrepareDeviceChangeRequest`</td><td></td><td class="clause">5.7.26</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf4e transfereimpackageresponse esipamessagefromipatoeim `transfereimpackageresponse` in `esipamessagefromipatoeim` 6.3.1 sgp.32 v1.3"><td class="tagcell"><code>BF4E</code></td><td>`transferEimPackageResponse` in `EsipaMessageFromIpaToEim`</td><td>`EsipaMessageFromIpaToEim`</td><td class="clause">6.3.1</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf4e transfereimpackageresponse esipamessagefromipatoeim `transfereimpackageresponse` in `esipamessagefromipatoeim` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF4E</code></td><td>`transferEimPackageResponse` in `EsipaMessageFromIpaToEim`</td><td>`EsipaMessageFromIpaToEim`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf4f geteimpackagerequest esipamessagefromipatoeim `geteimpackagerequest` in `esipamessagefromipatoeim` 6.3.1 sgp.32 v1.3"><td class="tagcell"><code>BF4F</code></td><td>`getEimPackageRequest` in `EsipaMessageFromIpaToEim`</td><td>`EsipaMessageFromIpaToEim`</td><td class="clause">6.3.1</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf4f geteimpackagerequest esipamessagefromipatoeim `geteimpackagerequest` in `esipamessagefromipatoeim` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF4F</code></td><td>`getEimPackageRequest` in `EsipaMessageFromIpaToEim`</td><td>`EsipaMessageFromIpaToEim`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf50 provideeimpackageresult esipamessagefromipatoeim `provideeimpackageresult` in `esipamessagefromipatoeim` 6.3.1 sgp.32 v1.3"><td class="tagcell"><code>BF50</code></td><td>`provideEimPackageResult` in `EsipaMessageFromIpaToEim`</td><td>`EsipaMessageFromIpaToEim`</td><td class="clause">6.3.1</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf50 provideeimpackageresult esipamessagefromipatoeim `provideeimpackageresult` in `esipamessagefromipatoeim` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF50</code></td><td>`provideEimPackageResult` in `EsipaMessageFromIpaToEim`</td><td>`EsipaMessageFromIpaToEim`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf51 euiccpackageresult euiccpackageresult `euiccpackageresult` 2.11.2.1 sgp.32 v1.3"><td class="tagcell"><code>BF51</code></td><td>`EuiccPackageResult`</td><td></td><td class="clause">2.11.2.1</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf51 euiccpackagerequest geteimpackageresponse `euiccpackagerequest` in `geteimpackageresponse` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF51</code></td><td>`euiccPackageRequest` in `GetEimPackageResponse`</td><td>`GetEimPackageResponse`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf52 ipaeuiccdatarequest ipaeuiccdatarequest `ipaeuiccdatarequest` 2.11.1.2 sgp.32 v1.3"><td class="tagcell"><code>BF52</code></td><td>`IpaEuiccDataRequest`</td><td></td><td class="clause">2.11.1.2</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf52 ipaeuiccdatarequest geteimpackageresponse `ipaeuiccdatarequest` in `geteimpackageresponse` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF52</code></td><td>`ipaEuiccDataRequest` in `GetEimPackageResponse`</td><td>`GetEimPackageResponse`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf53 eimacknowledgements eimacknowledgements `eimacknowledgements` 2.11.1.4 sgp.32 v1.3"><td class="tagcell"><code>BF53</code></td><td>`EimAcknowledgements`</td><td></td><td class="clause">2.11.1.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf53 eimacknowledgements provideeimpackageresultresponse `eimacknowledgements` in `provideeimpackageresultresponse` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF53</code></td><td>`eimAcknowledgements` in `ProvideEimPackageResultResponse`</td><td>`ProvideEimPackageResultResponse`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf54 profiledownloadtriggerrequest profiledownloadtriggerrequest `profiledownloadtriggerrequest` 2.11.1.3 sgp.32 v1.3"><td class="tagcell"><code>BF54</code></td><td>`ProfileDownloadTriggerRequest`</td><td></td><td class="clause">2.11.1.3</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf54 authenticateclientokdsesipa authenticateclientokdsesipa `authenticateclientokdsesipa` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF54</code></td><td>`AuthenticateClientOkDSEsipa`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf55 geteimconfigurationdatarequest geteimconfigurationdatarequest `geteimconfigurationdatarequest` 5.9.18 sgp.32 v1.3"><td class="tagcell"><code>BF55</code></td><td>`GetEimConfigurationDataRequest`</td><td></td><td class="clause">5.9.18</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf55 geteimconfigurationdatarequest geteimconfigurationdatarequest `geteimconfigurationdatarequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF55</code></td><td>`GetEimConfigurationDataRequest`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf56 getcertsrequest getcertsrequest `getcertsrequest` 5.9.10 sgp.32 v1.3"><td class="tagcell"><code>BF56</code></td><td>`GetCertsRequest`</td><td></td><td class="clause">5.9.10</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf56 getcertsrequest getcertsrequest `getcertsrequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF56</code></td><td>`GetCertsRequest`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf57 addinitialeimrequest addinitialeimrequest `addinitialeimrequest` 5.9.4 sgp.32 v1.3"><td class="tagcell"><code>BF57</code></td><td>`AddInitialEimRequest`</td><td></td><td class="clause">5.9.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf57 addinitialeimrequest addinitialeimrequest `addinitialeimrequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF57</code></td><td>`AddInitialEimRequest`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf58 profilerollbackrequest profilerollbackrequest `profilerollbackrequest` 5.9.16 sgp.32 v1.3"><td class="tagcell"><code>BF58</code></td><td>`ProfileRollbackRequest`</td><td></td><td class="clause">5.9.16</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf58 profilerollbackrequest profilerollbackrequest `profilerollbackrequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF58</code></td><td>`ProfileRollbackRequest`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf59 configureimmediateprofileenablingrequest configureimmediateprofileenablingrequest `configureimmediateprofileenablingrequest` 5.9.17 sgp.32 v1.3"><td class="tagcell"><code>BF59</code></td><td>`ConfigureImmediateProfileEnablingRequest`</td><td></td><td class="clause">5.9.17</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf59 configureimmediateprofileenablingrequest configureimmediateprofileenablingrequest `configureimmediateprofileenablingrequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF59</code></td><td>`ConfigureImmediateProfileEnablingRequest`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf5a immediateenablerequest immediateenablerequest `immediateenablerequest` 5.9.15 sgp.32 v1.3"><td class="tagcell"><code>BF5A</code></td><td>`ImmediateEnableRequest`</td><td></td><td class="clause">5.9.15</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf5a immediateenablerequest immediateenablerequest `immediateenablerequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF5A</code></td><td>`ImmediateEnableRequest`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf5b enableemergencyprofilerequest enableemergencyprofilerequest `enableemergencyprofilerequest` 5.9.22 sgp.32 v1.3"><td class="tagcell"><code>BF5B</code></td><td>`EnableEmergencyProfileRequest`</td><td></td><td class="clause">5.9.22</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf5b enableemergencyprofilerequest enableemergencyprofilerequest `enableemergencyprofilerequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF5B</code></td><td>`EnableEmergencyProfileRequest`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf5c disableemergencyprofilerequest disableemergencyprofilerequest `disableemergencyprofilerequest` 5.9.23 sgp.32 v1.3"><td class="tagcell"><code>BF5C</code></td><td>`DisableEmergencyProfileRequest`</td><td></td><td class="clause">5.9.23</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf5c disableemergencyprofilerequest disableemergencyprofilerequest `disableemergencyprofilerequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF5C</code></td><td>`DisableEmergencyProfileRequest`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf5d executefallbackmechanismrequest executefallbackmechanismrequest `executefallbackmechanismrequest` 5.9.20 sgp.32 v1.3"><td class="tagcell"><code>BF5D</code></td><td>`ExecuteFallbackMechanismRequest`</td><td></td><td class="clause">5.9.20</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf5e returnfromfallbackrequest returnfromfallbackrequest `returnfromfallbackrequest` 5.9.21 sgp.32 v1.3"><td class="tagcell"><code>BF5E</code></td><td>`ReturnFromFallbackRequest`</td><td></td><td class="clause">5.9.21</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf5e returnfromfallbackrequest returnfromfallbackrequest `returnfromfallbackrequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF5E</code></td><td>`ReturnFromFallbackRequest`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf5f getconnectivityparametersrequest getconnectivityparametersrequest `getconnectivityparametersrequest` 5.9.24 sgp.32 v1.3"><td class="tagcell"><code>BF5F</code></td><td>`GetConnectivityParametersRequest`</td><td></td><td class="clause">5.9.24</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf5f getconnectivityparametersrequest getconnectivityparametersrequest `getconnectivityparametersrequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF5F</code></td><td>`GetConnectivityParametersRequest`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf60 verifysmdpresponserequest verifysmdpresponserequest `verifysmdpresponserequest` 5.7.28 sgp.22 v3.1"><td class="tagcell"><code>BF60</code></td><td>`VerifySmdpResponseRequest`</td><td></td><td class="clause">5.7.28</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf61 checkprogressrequest remoteprofileprovisioningrequest `checkprogressrequest` in `remoteprofileprovisioningrequest` 6.6.1 sgp.22 v3.1"><td class="tagcell"><code>BF61</code></td><td>`checkProgressRequest` in `RemoteProfileProvisioningRequest`</td><td>`RemoteProfileProvisioningRequest`</td><td class="clause">6.6.1</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf62 verifyprofilerecoveryrequest verifyprofilerecoveryrequest `verifyprofilerecoveryrequest` 5.7.29 sgp.22 v3.1"><td class="tagcell"><code>BF62</code></td><td>`VerifyProfileRecoveryRequest`</td><td></td><td class="clause">5.7.29</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf63 deletenotificationfordc deletenotificationfordc `deletenotificationfordc` 4.1.3 sgp.22 v3.1"><td class="tagcell"><code>BF63</code></td><td>`DeleteNotificationForDc`</td><td></td><td class="clause">4.1.3</td><td>SGP.22 v3.1</td></tr>
<tr data-s="bf64 storemetadatarequest storemetadatarequest `storemetadatarequest` 5.5.3 sgp.22 v2.7"><td class="tagcell"><code>BF64</code></td><td>`StoreMetadataRequest`</td><td></td><td class="clause">5.5.3</td><td>SGP.22 v2.7</td></tr>
<tr data-s="bf64 ipacapabilities ipacapabilities `ipacapabilities` 4.4 sgp.32 v1.3"><td class="tagcell"><code>BF64</code></td><td>`IpaCapabilities`</td><td></td><td class="clause">4.4</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf64 euiccmemoryresetrequest euiccmemoryresetrequest `euiccmemoryresetrequest` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF64</code></td><td>`EuiccMemoryResetRequest`</td><td></td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
<tr data-s="bf65 setdefaultdpaddress psmo `setdefaultdpaddress` in `psmo` 2.11.1.1 sgp.32 v1.3"><td class="tagcell"><code>BF65</code></td><td>`setDefaultDpAddress` in `Psmo`</td><td>`Psmo`</td><td class="clause">2.11.1.1</td><td>SGP.32 v1.3</td></tr>
<tr data-s="bf65 setdefaultdpaddress psmo `setdefaultdpaddress` in `psmo` 2.1 sgp.32 v1.2"><td class="tagcell"><code>BF65</code></td><td>`setDefaultDpAddress` in `Psmo`</td><td>`Psmo`</td><td class="clause">2.1</td><td>SGP.32 v1.2</td></tr>
</tbody></table></div>

<script>
(function(){
  var input = document.getElementById('tl-search');
  var rows = Array.prototype.slice.call(document.querySelectorAll('#tl-table tbody tr'));
  var count = document.getElementById('tl-count');
  function update(){
    var q = input.value.trim().toLowerCase();
    var shown = 0;
    rows.forEach(function(r){
      var hit = !q || r.dataset.s.indexOf(q) !== -1;
      r.style.display = hit ? '' : 'none';
      if (hit) shown++;
    });
    count.textContent = q
      ? shown + ' of ' + rows.length + ' rows match "' + input.value.trim() + '"'
      : rows.length + ' tag/spec rows. Type to filter.';
  }
  input.addEventListener('input', update);
  update();
})();
</script>


## Coverage

Which documents, and how many distinct tags each contributes:

| Document | Tags |
|---|---|

| SGP.22 v3.1 | 76 |
| SGP.22 v2.7 | 57 |
| SGP.22 v2.2.2 | 53 |
| SGP.32 v1.3 | 66 |
| SGP.32 v1.2 | 62 |
| TCA Pkg v3.4.1 | 1 |
| TCA Interop v3.4 | 2 |
| GPC_SPE_121-Amendment-I-Secure-Element-Mgmt-Service-v1.2 | 4 |
| GPC_UICC_Configuration-v1.0.1 | 5 |
| 31102-j50 | 33 |
| GPC_SPE_093-Amendment-F-SCP11 | 6 |
| 31111-j40 | 2 |
| ETSI-TS-102-222-v17.0.0 | 13 |
| GPC_SPE_025-Amendment-C-Contactless-Services | 9 |
| ETSI-TS-102-221-v18.4.0 | 15 |
| ETSI-TS-131-103-v14.1.1 | 2 |
| 31103-e11 | 2 |
| GPC_SE_Configuration-v2.0 | 8 |
| GPC_SPE_034-Card-Spec-v2.3.0 | 8 |
| GPC_SPE_034-Card-Spec-v2.3.1 | 8 |
| GPC_UICC_Configuration-v2.0 | 6 |
| GPC_SPE_034-Card-Spec-v2.4 | 13 |
| GPC_SPE_034-Card-Spec-v2.2.1 | 3 |
| ETSI-TS-102-226-v19.0.0 | 1 |
| GPC_SPE_034-Card-Spec-v2.2.0 | 2 |
| TCA-eUICC-Profile-Package-v3.4.1 | 1 |
| GPC_SPE_120-Amendment-H-Executable-Load-File-Upgrade-v1.1 | 4 |
| 23003-k00 | 1 |
| GPD_SPE_013-Secure-Element-Access-Control | 1 |
| GPC_SPE_011-Amendment-B-Remote-App-Mgmt-HTTP | 1 |
| SGP.23-v1.16 | 1 |
| GPC_SPE_182-Amendment-K-SCP04-v1.0.2 | 1 |
| GPC_SPE_007-Amendment-A-Confidential-Card-Content-Mgmt | 1 |

## How to read a tag

The first octet is an X.690 identifier octet: two class bits, one
primitive/constructed bit, five tag-number bits.

```
BF 36
│  └── additional octet: tag number 0x36
└───── 10 111 11 = context class, constructed, high tag number form
```

| First octet | Class | Constructed | Where you meet it |
|---|---|---|---|
| `BF` | context | yes | eUICC request and response wrappers (`BF36` BPP, `BF37` PIR, `BF22` EUICCInfo2) |
| `9F` | context | no | primitive eUICC fields (`9F1F` serviceDescription) |
| `5F` | application | no | ISO 7816 proprietary tags (`5F37` signatures) |
| `DF` | private | yes | not used by GSMA RSP; a `DF` first octet is normally a misread `9F` |

When the low five bits are `11111`, the tag is in **high tag number form** and the
tag number is the following octet. `BF 36` is therefore context/constructed with
tag number `0x36`, written `[54]` in the ASN.1.

## Common questions

**What is tag `BF36`?** `BoundProfilePackage`, the bound profile package the
SM-DP+ returns after authentication and the eUICC installs. SGP.22 v3.1 section
2.5.4.

**What is tag `BF37`?** `ProfileInstallationResult`, the eUICC's signed report of
an install attempt. Delivered to the SM-DP+ over ES9+, and inside a `BF54` wrapper
when an eIM ordered the download. SGP.22 v3.1 section 2.5.6.

**What is tag `9F1F`?** `serviceDescription`, present from SGP.22 v3.0, in
StoreMetadata and in ProfileInfo.

**What is tag `BF54`?** Both `ProfileDownloadTriggerRequest` and
`ProfileDownloadTriggerResult`. The request and the response share one tag, which
is why a result with a bare `BF37` at the top level is not a message this protocol
defines. SGP.32 `2.11.1.3` and `2.11.2.3`.

**Why does the same tag show different structures in different specs?** Because
tags are scoped to their ASN.1 module. `BF20` is `EUICCInfo1` in SGP.22, and tags
in 3GPP TS 31.102 belong to the UICC file system rather than to RSP. Always read
the Spec column before acting on a tag.

## Related

- [Status Word Reference]({{ site.baseurl }}/docs/status-words): the two-byte
  result code that ends every APDU.
- [Tag Lookup, condensed]({{ site.baseurl }}/ai/tag-lookup): the same data as a
  single plain table for programmatic or LLM extraction.

## Sources

Extracted with `scripts/extract-tags.py` from the specification text of: GSMA
SGP.22 v2.2.2, v2.7 and v3.1; SGP.32 v1.2 and v1.3; SGP.31 v1.3; SGP.02 v4.2;
SGP.41 v1.0; TCA eUICC Profile Package v3.4.1 and Interop Test v3.4; ETSI TS 102
221, 222, 223 and 102 705; 3GPP TS 31.102 and TS 31.103. Tags are only ever taken
from the quoted ASN.1 tag comments in those documents, never computed by hand.
