# eSIM Knowledge Base: Completeness & Consistency Audit

**Date:** 2026-06-06  
**Auditor:** Hermes Agent (automated)  
**Scope:** 52 numbered articles (00–51), homepage, glossary, prerequisites, standards map

---

## 1. NUMBERING AUDIT (00–51)

### Status: ✅ PASS: No gaps, no duplicates

| Range | Spec Family | Count | Files |
|-------|-------------|-------|-------|
| 00–06 | SGP.22 (Consumer RSP) | 7 | 00-sgp22-overview … 06-developer-interfaces |
| 07–16 | SGP.32 (IoT eSIM) | 10 | 07-iot-esim-why … 16-iot-functions-reference |
| 17–21 | SGP.23 (Test Spec) | 5 | 17-sgp23-overview … 21-sgp23-certification |
| 22–26 | SGP.25 (Protection Profile) | 5 | 22-sgp25-overview … 26-sgp25-certification |
| 27–31 | SGP.29 (EID) | 5 | 27-sgp29-overview … 31-sgp29-security |
| 32–36 | SGP.23-1 (eUICC Testing) | 5 | 32-sgp23-1-overview … 36-sgp23-1-certification |
| 37–41 | SGP.26 (Test Certs) | 5 | 37-sgp26-overview … 41-sgp26-crl |
| 42–46 | SGP.33-3 (eIM Testing) | 5 | 42-sgp33-overview … 46-sgp33-certification |
| 47–51 | SGP.41 (IFPP) | 5 | 47-sgp41-overview … 51-sgp41-practice |
| **Total** | | **52** | |

Additionally, 17 kid-friendly articles exist under `docs/articles/kids/` (not in the 00–51 numbering).

---

## 2. FORMAT CONSISTENCY AUDIT

### 2.1 Article Structure Checklist

All 52 articles were sampled (6 read in full, remainder checked at head/tail). Every article contains:

| Element | Present In | Notes |
|---------|-----------|-------|
| YAML frontmatter | All 52 | ✅ |
| Breadcrumbs | All 52 | ✅ Format: `🏠 [eUICC.tech](/) > [Section Label](/path/) > Article Title` |
| "Why this matters" callout | All 52 | ✅ Consistent `💡` emoji + bold header |
| "Key takeaways" bullets | All 52 | ✅ Consistent `>` blockquote format |
| Content sections (##) | All 52 | ✅ |
| "📋 Summary" | All 52 | ✅ Consistent section header |
| Navigation links (Home + Prev/Next) | All 52 | ✅ Inside `<div align="center">` |
| Source citation | All 52 | ✅ Consistent `*Based on GSMA SGP.XX vX.Y (date) : Title*` footer |

### 2.2 Frontmatter Inconsistency ⚠️ ISSUE

**Only article 00 (`00-sgp22-overview.md`) is missing `title:` in frontmatter.** All other 51 articles have both `title:` and `date:`.

```yaml
# 00-sgp22-overview.md (INCORRECT: missing title)
---
date: 2026-06-05
---

# All other 51 articles (CORRECT)
---
title: "Article Title Here"
date: 2026-XX-XX
---
```

### 2.3 Prerequisites Callout: Inconsistent ⚠️ ISSUE

| Series | Prerequisites Callout |
|--------|----------------------|
| SGP.22 (00–06) | ✅ Article 00: "New to telecom or smart card technology? Read our Prerequisites Guide first." |
| SGP.32 (07–16) | ✅ Article 07: "This series assumes you've read the SGP.22 Consumer eSIM articles." |
| SGP.23 (17–21) | ❌ None |
| SGP.25 (22–26) | ❌ None |
| SGP.29 (27–31) | ❌ None |
| SGP.23-1 (32–36) | ❌ None |
| SGP.26 (37–41) | ❌ None |
| SGP.33-3 (42–46) | ❌ None |
| SGP.41 (47–51) | ❌ None |

Newer articles (17–51) do not guide readers on prerequisites or dependencies.

### 2.4 Table of Contents: Inconsistent ⚠️ ISSUE

- **SGP.22 article 03** (`03-profile-download.md`, 700 lines) uses `* TOC {:toc}` (Jekyll auto-TOC).
- **No other article** uses this feature, even long ones like `16-iot-functions-reference.md` (281 lines).

---

## 3. STYLE DRIFT ANALYSIS: Original vs. New Articles

| Dimension | SGP.22 / SGP.32 (00–16) | SGP.23–SGP.41 (17–51) |
|-----------|--------------------------|------------------------|
| **Length** | 120–700 lines (avg ~220) | 116–192 lines (avg ~145) |
| **Depth** | Detailed protocol walkthroughs, tables, code blocks, diagrams | Higher-level overview, compressed explanations |
| **Tone** | Conversational, uses "you," "your device" | Academic/formal, specification-reporting style |
| **Emoji usage** | Consistent `💡`, `📋` | Same emojis used ✅ |
| **Tables** | Heavy use of markdown tables | Present but fewer |
| **Code blocks** | Frequent (activation codes, flow diagrams) | Occasional (ASCII art diagrams) |
| **Prereqs callout** | Present | Absent |
| **TOC** | Present (article 03 only) | Absent |
| **Breadcrumb labels** | e.g., `[SGP.22 Consumer RSP](/docs/articles/sgp22/)` | e.g., `[SGP.23 Test Specifications](/docs/articles/sgp23/)` : consistent naming ✅ |

**Assessment:** Mild style drift. New articles are notably shorter and more compressed. This could be acceptable if the intent is to provide "overview-level" depth for supplementary specs, but the difference is noticeable when reading across the full knowledge base.

---

## 4. NAVIGATION COMPLETENESS

### 4.1 Intra-Series Navigation ✅ PASS

All articles chain correctly within their series:
- First article in each series: Previous link absent (correct)
- Last article in each series: Next link absent (correct)
- Middle articles: Both Previous ← and Next → present

### 4.2 Cross-Series Navigation ⚠️ ISSUE

Articles are linked ONLY within their own spec series. There is no cross-series "Next" between:
- 06-developer-interfaces (end of SGP.22) → 07-iot-esim-why (start of SGP.32)
- 16-iot-functions-reference (end of SGP.32) → 17-sgp23-overview (start of SGP.23)

Readers following "Next" links will dead-end at each series boundary.

### 4.3 Breadcrumb Section Links: 404 ⚠️ ISSUE

Breadcrumbs contain links like `[SGP.23 Test Specifications](/docs/articles/sgp23/)` but **no `index.md` exists** in any section directory except `kids/`. All 8 section breadcrumb paths return 404:

| Breadcrumb Path | Status |
|----------------|--------|
| `/docs/articles/sgp22/` | 404: no index.md |
| `/docs/articles/sgp32/` | 404: no index.md |
| `/docs/articles/sgp23/` | 404: no index.md |
| `/docs/articles/sgp25/` | 404: no index.md |
| `/docs/articles/sgp29/` | 404: no index.md |
| `/docs/articles/sgp23-1/` | 404: no index.md |
| `/docs/articles/sgp26/` | 404: no index.md |
| `/docs/articles/sgp33-3/` | 404: no index.md |
| `/docs/articles/sgp41/` | 404: no index.md |

### 4.4 Orphan Article Check ✅ PASS

Every article is linked from the homepage index. No orphan articles found.

---

## 5. HOMEPAGE COMPLETENESS

### 5.1 Section Coverage

| Homepage Section | Covers | Issue? |
|-----------------|--------|--------|
| 🚀 Start Here | SGP.22 articles 00–06 | ⚠️ Duplicate of SGP.22 section below |
| 📱 SGP.22 Consumer RSP | SGP.22 articles 00–06 | ⚠️ Same articles as Start Here |
| 🤖 SGP.32/SGP.31 IoT | SGP.32 articles 07–16 | ✅ |
| 🎨 Architecture Diagrams | 6 SVG diagrams | ✅ |
| 📚 Key Concepts | 14 glossary entries | ✅ |
| 🧪 SGP.23/SGP.23-1 | 10 articles (17–21, 32–36) | ✅ |
| 🔒 SGP.25 | 5 articles (22–26) | ✅ |
| 📜 SGP.26 | 5 articles (37–41) | ✅ |
| 🆔 SGP.29 | 5 articles (27–31) | ✅ |
| 🤖 SGP.33-3 | 5 articles (42–46) | ✅ |
| 🏭 SGP.41 | 5 articles (47–51) | ✅ |
| 🗺️ Standards Map | ✅ | ✅ |

### 5.2 Duplicate Content ⚠️ ISSUE

The "Start Here" section and "SGP.22 Consumer RSP" section list the **exact same 7 articles** (00–06). The Start Here section presents them as a sequential reading guide; the SGP.22 section presents them as a per-spec reference. This is confusing: readers may think they're different articles or that they missed content.

### 5.3 SGP.21 References Without Coverage

The homepage footer and source citations reference **SGP.21** (RSP Architecture), but no article, section, or standards-map entry explains SGP.21 in depth. The standards-map.md timeline does mention it ("2014: SGP.21 RSP Architecture (underpins SGP.22)") but no dedicated content exists.

---

## 6. GLOSSARY & PREREQUISITES COMPLETENESS

### 6.1 Glossary ✅ PASS

The glossary (`docs/glossary.md`) is comprehensive:
- **Core Architecture:** 10 terms (eUICC, UICC, Profile, ISD-P, ISD-R, ECASD, MNO-SD, NAA, USIM, ISIM, CSIM)
- **RSP Entities:** 9 terms (SM-DP+, SM-DS, LPA, LDS, LPD, LUI, LPAd, LPAe, MNO)
- **IoT eSIM (SGP.32):** 6 terms (eIM, IPA, IPAd, IPAe, PSMO, eCO)
- **In-Factory (SGP.41):** 7 terms (IFPP, SM-DPf, FPA, BPP, UPP, PPP, SBPP)
- **Cryptography:** 11 terms (PKI, CI, EUM, ECDSA, ECDH, ECC, PFS, CRL, OCSP, HSM, TOE, SCP03t)
- **Smart Card:** 9 terms (APDU, TLV, ASN.1, GlobalPlatform, TAR, AID, ADF, MF, DF, EF, SD)
- **Identifiers:** 4 terms (ICCID, IMSI, EID, ERHI1)
- **Network/IoT:** 8 terms (OTA, CoAP, DTLS, LwM2M, NB-IoT, LTE-M, LPWA, eDRX, PSM)
- **Certification:** 4 terms (SAS-UP, SAS-SM, DLOA, GSMA)
- **Profile Types:** 3 terms (Operational, Provisioning, Test)

All spec families are covered. No missing terms detected for any article.

### 6.2 Prerequisites Page ✅ PASS

The prerequisites page covers: Networking, SIM/UICC basics, Public-key cryptography, Smart Card/Java Card, GSMA standards ecosystem. External resource links provided. Links to Kids articles and Glossary at the bottom.

---

## 7. SOURCE CITATION CONSISTENCY

### 7.1 Format Pattern ✅ PASS

All citations follow a consistent pattern:
```
*Based on GSMA SGP.XX vX.Y (Date) : Specification Title, additional details*
```

### 7.2 Citation Completeness

All 52 articles end with a source citation. Examples:
- SGP.22: `*Based on GSMA SGP.22 v2.2.2 (05 June 2020) : RSP Technical Specification*`
- SGP.32: `*Based on GSMA SGP.31 v1.3 and SGP.32 v1.3 (22 May 2026)*`
- SGP.23: `*Based on GSMA SGP.23 v1.16 (29 April 2025) : RSP Test Specification*`
- SGP.25: `*Based on GSMA SGP.25 v2.1 (3 February 2025) : eUICC for Consumer and IoT Devices Protection Profile, Sections 1–2, conformant to Common Criteria CC:2022 release 1*`
- SGP.29: `*Based on GSMA SGP.29 v1.1 (22 March 2024) : EID Definition and Assignment Process, Sections 1–7*`
- SGP.41: `*Based on GSMA SGP.41 v1.0 (28 February 2025) : eSIM In-Factory Profile Provisioning Architecture and Requirements, Annex A*`

**Note:** SGP.22 citations reference v2.2.2 (2020), which is older than SGP.22 v2.7 mentioned in the homepage footer. This may be intentional (articles written against v2.2.2 as the most widely deployed version).

---

## 8. ACRONYM DEFINITION ON FIRST USE

### 8.1 Sampling Check ✅ Mostly PASS

| Article | Term | First-Use Definition | Status |
|---------|------|---------------------|--------|
| 00-sgp22-overview | RSP | "Remote SIM Provisioning" (L24) | ✅ |
| 00-sgp22-overview | eUICC | "embedded UICC" (L36) | ✅ |
| 17-sgp23-overview | IUT | "Implementation Under Test" (L27) | ✅ |
| 22-sgp25-overview | CC | "Common Criteria" (L13) | ✅ |
| 22-sgp25-overview | PP | "Protection Profile" (L26) | ✅ |
| 27-sgp29-overview | EID | Title + L6 | ✅ |

### 8.2 Cross-Series Consistency ⚠️ MINOR ISSUE

Newer articles (17–51) sometimes use terms like `eUICC`, `SM-DP+`, `ISD-R` without redefining them, assuming the reader has come through the earlier series. The glossary covers all terms, but a brief parenthetical on first use would improve standalone readability.

---

## 9. KID-FRIENDLY ARTICLES

17 kid-friendly versions exist covering all SGP.22 and SGP.32 articles (00–16). No kid-friendly versions exist for SGP.23–SGP.41 (articles 17–51). This is consistent with the scope (kid versions mirror the "main" SGP.22/SGP.32 learning path).

---

## SUMMARY OF ISSUES FOUND

### 🔴 High Priority
1. **8 breadcrumb section pages return 404** : No `index.md` in `sgp22/`, `sgp32/`, `sgp23/`, `sgp25/`, `sgp29/`, `sgp23-1/`, `sgp26/`, `sgp33-3/`, `sgp41/`. Fix: create short index pages for each section.
2. **SGP.22 articles duplicated on homepage** : "Start Here" and "SGP.22" sections list the same 7 articles. Fix: keep one and remove/rework the other.

### 🟡 Medium Priority
3. **Frontmatter inconsistency** : Article 00 is missing `title:` field. Fix: add `title: "eSIM Remote SIM Provisioning (RSP) : How It Works"`.
4. **Missing prerequisites callout** in 35 new articles (17–51). Fix: add a brief prereqs note (at minimum "See the Glossary for acronym definitions").
5. **Cross-series navigation dead-ends** : No "Next" link between series boundaries. Fix: add cross-series navigation or a "Continue to next section" link.

### 🟢 Low Priority / Observations
6. **Style drift** : New articles (17–51) are ~35% shorter and more compressed than original SGP.22/SGP.32 articles. Not necessarily a defect, but worth reviewing if uniform depth is desired.
7. **Missing TOC** : Only article 03 uses Jekyll `{:toc}`. Long articles (>200 lines) would benefit.
8. **SGP.21 referenced but not covered** : The homepage footer cites SGP.21 but no dedicated content exists. Add a brief note to standards-map or a footnote.
9. **SGP.22 citation version drift** : Articles cite v2.2.2 (2020) while homepage footer cites v2.7. Not necessarily wrong (v2.2.2 is the most deployed baseline), but the discrepancy should be documented.
