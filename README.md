     1|<div align="center">
     2|
     3|# 🔐 eUICC.tech
     4|
     5|### Deep Dives Into GSMA eSIM Remote SIM Provisioning
     6|
     7|*Built from primary source specifications SGP.22, SGP.31, and SGP.32*
     8|
     9|</div>
    10|
    11|---
    12|
    13|## 🚀 Start Here
    14|
    15|New to eSIM? Read these in order — each builds on the last.
    16|
    17|| # | Article | What You'll Learn |
    18||---|---------|-------------------|
    19|| 1 | [Overview: The eSIM RSP Technical Specification](docs/articles/sgp22/00-sgp22-overview) | The big picture — what RSP is, who the players are, how the interfaces connect |
    20|| 2 | [The eSIM RSP Architecture: Players and Interfaces](docs/articles/sgp22/01-rsp-architecture) | Deep dive into all 5 entities and 13 interfaces, trust flows, deployment models |
    21|| 3 | [Inside the eUICC: The Secure Element That Powers Your eSIM](docs/articles/sgp22/02-inside-the-euicc) | ISD-R, ISD-P, ECASD, Profile Policy Enabler — the chip's internal architecture |
    22|| 4 | [How a Profile Gets Delivered: The eSIM Download Process](docs/articles/sgp22/03-profile-download) | The full 3-phase download: initiation, authentication, installation — step by step |
    23|| 5 | [eSIM Security: The PKI and Certificate Model](docs/articles/sgp22/04-esim-security-pki) | ECDSA, ECDH, certificate chains, revocation — how eSIM prevents man-in-the-middle |
    24|| 6 | [Managing Your eSIM: Local Profile Operations](docs/articles/sgp22/05-local-profile-management) | Enable, disable, delete, rename — what the LPA does after profiles are installed |
    25|| 7 | [The Developer's View: RSP Interfaces and Protocol Binding](docs/articles/sgp22/06-developer-interfaces) | ASN.1 structures, HTTPS/ES8+/ES9+ bindings, the developer-facing side |
    26|
    27|---
    28|
    29|## 📱 SGP.22 — Consumer eSIM RSP
    30|
    31|*Phones, tablets, wearables, laptops — the eSIM you use every day.*
    32|
    33|| Article | Date |
    34||---------|------|
    35|| [Overview: The eSIM RSP Technical Specification](docs/articles/sgp22/00-sgp22-overview) | — |
    36|| [The eSIM RSP Architecture: Players and Interfaces](docs/articles/sgp22/01-rsp-architecture) | 2026-05-24 |
    37|| [Inside the eUICC: The Secure Element That Powers Your eSIM](docs/articles/sgp22/02-inside-the-euicc) | 2026-05-27 |
    38|| [How a Profile Gets Delivered: The eSIM Download Process](docs/articles/sgp22/03-profile-download) | 2026-05-29 |
    39|| [eSIM Security: The PKI and Certificate Model](docs/articles/sgp22/04-esim-security-pki) | 2026-06-01 |
    40|| [Managing Your eSIM: Local Profile Operations](docs/articles/sgp22/05-local-profile-management) | 2026-06-03 |
    41|| [The Developer's View: RSP Interfaces and Protocol Binding](docs/articles/sgp22/06-developer-interfaces) | 2026-06-05 |
    42|
    43|---
    44|
    45|## 🤖 SGP.32 / SGP.31 — IoT eSIM RSP
    46|
    47|*NB-IoT, LTE-M, sensors, trackers — eSIM for things that have no screen.*
    48|
    49|| Article | Date |
    50||---------|------|
    51|| [eSIM for IoT: Why It Needed Its Own Architecture](docs/articles/sgp32/07-iot-esim-why) | 2026-05-22 |
    52|| [The eSIM IoT Architecture: eIM, IPA, and New Interfaces](docs/articles/sgp32/08-iot-architecture-im-ipa) | 2026-05-26 |
    53|| [IoT Profile Download: Direct, Indirect, and eIM Package Handling](docs/articles/sgp32/09-iot-profile-download-packages) | 2026-05-29 |
    54|| [IoT eSIM Security: eIM Certificates, DTLS, and Device Trust](docs/articles/sgp32/10-iot-esim-security-dtls) | 2026-06-01 |
    55|| [eIM Configuration: Associating Remote Managers with Your eUICC](docs/articles/sgp32/11-eim-configuration) | 2026-06-02 |
    56|| [Notifications and Error Handling in IoT eSIM](docs/articles/sgp32/12-notifications-errors) | 2026-06-03 |
    57|| [IoT Device Initialisation and the eUICC File Structure](docs/articles/sgp32/13-iot-device-initialisation) | 2026-06-04 |
    58|| [Profile State Management via the eIM](docs/articles/sgp32/14-iot-profile-state-management) | 2026-06-05 |
    59|| [SM-DS Operations in IoT eSIM](docs/articles/sgp32/15-iot-smsds-operations) | 2026-06-06 |
    60|| [IoT eSIM Functions Reference: ESipa, ES9+', ES11', ESep](docs/articles/sgp32/16-iot-functions-reference) | 2026-06-07 |
    61|
    62|---
    63|
    64|## 🎨 Architecture Diagrams
    65|
    66|*Dark-themed SVG diagrams — open in any browser.*
    67|
    68|| Diagram | What It Shows |
    69||---------|---------------|
    70|| [RSP Architecture Overview](docs/diagrams/01-rsp-architecture.html) | All 5 entities, 13 interfaces, trust relationships |
    71|| [eUICC Internal Architecture](docs/diagrams/02-euicc-internals.html) | ISD-R, ISD-P, ECASD, security domains, profile isolation |
    72|| [PKI Trust Chain](docs/diagrams/03-pki-trust-chain.html) | CI → EUM → eUICC certificate hierarchy |
    73|| [IoT Architecture — eIM + IPA](docs/diagrams/04-iot-architecture.html) | The SGP.32 ecosystem: eIM, IPA, SM-DP+, new interfaces |
    74|| [Profile Download Sequence](docs/diagrams/05-profile-download-sequence.html) | Full message flow: activation → auth → install |
    75|| [Profile Package Stages](docs/diagrams/06-profile-package-stages.html) | How a profile moves from operator → SM-DP+ → eUICC |
    76|
    77|---
    78|
    79|## 📚 Key Concepts
    80|
    81|| Concept | Quick Explanation |
    82||---------|-------------------|
    83|| **eUICC** | The tamper-resistant chip that holds profiles — not just storage, a full Java Card OS |
    84|| **Profile** | One operator's credentials inside an eUICC — equivalent to one physical SIM |
    85|| **ISD-P** | Issuer Security Domain — Profile — the container for each profile inside the eUICC |
    86|| **ISD-R** | Issuer Security Domain — Root — the profile manager on the chip |
    87|| **ECASD** | eUICC Controlling Authority Security Domain — the root of trust, holds CI public keys |
    88|| **SM-DP+** | Subscription Manager Data Preparation — builds and encrypts profiles |
    89|| **SM-DS** | Subscription Manager Discovery Server — notifies devices of pending profiles |
    90|| **LPA** | Local Profile Assistant — the on-device software that orchestrates downloads |
    91|| **eIM** | eSIM IoT Remote Manager — the remote entity that manages IoT device profiles |
    92|| **IPA** | IoT Profile Assistant — the stripped‑down on‑device proxy for IoT devices |
    93|| **PSMO** | Profile State Management Operation — remote enable/disable/delete (IoT only) |
    94|| **ECDSA** | Elliptic Curve Digital Signature Algorithm — P‑256, used for mutual authentication |
    95|| **ECDH** | Elliptic Curve Diffie‑Hellman — ephemeral key exchange for Perfect Forward Secrecy |
    96|| **CRL** | Certificate Revocation List — how compromised certificates are invalidated |
    97|
    98|---
    99|
   100|<div align="center">
   101|
   102|*Sources: GSMA SGP.22 v2.2.2 · SGP.32 v1.3 · SGP.31 v1.3*
   103|
   104|[View on GitHub](https://github.com/AlexsCodingAgent/esim-knowledge) · [eUICC.tech](https://euicc.tech) *(domain to be linked)*
   105|
   106|</div>
   107|