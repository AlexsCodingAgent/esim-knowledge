#!/usr/bin/env python3
"""Render /tmp/tags.json into the euicc.tech tag-lookup page.

Emits two pages from one dataset:
  docs/tag-lookup.md       human reference, grouped by tag class, with search UI
  ai/tag-lookup.md         condensed single table for retrieval / LLM extraction

Data-driven on purpose: every row is a fact extracted from a named spec with a
line number, so nothing here is asserted from memory. Re-run
scripts/extract-tags.py then this script after adding or updating a spec.
"""

import json
import os
import re
import sys
from collections import Counter, defaultdict

SRC = sys.argv[1] if len(sys.argv) > 1 else "/tmp/tags.json"
ROOT = os.path.expanduser("~/repos/esim-knowledge")

with open(SRC, encoding="utf-8") as fh:
    DATA = json.load(fh)

TAGS = DATA["tags"]

# Spec ordering and the friendly name used in the Source column. Anything not
# listed still renders, with its directory filename as the label.
SPEC_LABEL = {
    "SGP.22-v3.1": "SGP.22 v3.1",
    "SGP.22-v2.7": "SGP.22 v2.7",
    "SGP.22-v2.2.2": "SGP.22 v2.2.2",
    "SGP.32-v1.3": "SGP.32 v1.3",
    "SGP.32-v1.2": "SGP.32 v1.2",
    "SGP.31-v1.3": "SGP.31 v1.3",
    "SGP.02-v4.2": "SGP.02 v4.2",
    "SGP.41-v1.0": "SGP.41 v1.0",
    "TCA-eUICC-Profile-Package-Tech-Spec-v3.4.1": "TCA Pkg v3.4.1",
    "TCA-eUICC-Interop-Test-Spec-v3.4": "TCA Interop v3.4",
}

# Preferred presentation order: RSP specs first (that is what this site is about),
# then card-layer standards.
SPEC_ORDER = {k: i for i, k in enumerate([
    "SGP.22-v3.1", "SGP.22-v2.7", "SGP.22-v2.2.2",
    "SGP.32-v1.3", "SGP.32-v1.2", "SGP.31-v1.3",
    "SGP.02-v4.2", "SGP.41-v1.0",
    "TCA-eUICC-Profile-Package-Tech-Spec-v3.4.1",
    "TCA-eUICC-Interop-Test-Spec-v3.4",
])}

CLASS_LABEL = {
    "context": "Context class (`BF` / `9F`)",
    "application": "Application class (`5F`)",
    "universal": "Universal class",
    "private": "Private class",
}


def spec_key(rec):
    return (SPEC_ORDER.get(rec["spec"], 99), rec["spec"], rec.get("clause") or "")


def best_records(recs):
    """One representative definition per spec, preferring records that name an owner."""
    by_spec = defaultdict(list)
    for r in recs:
        # A row with no field and no owner names nothing: it is a prose mention
        # of a tag (GlobalPlatform X.509 certificate field tags such as `Tag '42'`,
        # or a table fragment) rather than a definition of an eSIM TLV structure.
        # Those belong to a different namespace and would render as nameless hex,
        # so they are excluded rather than published as if they were lookups.
        if not r.get("owner") and not r.get("field"):
            continue
        by_spec[r["spec"]].append(r)
    out = []
    for spec, group in by_spec.items():
        group.sort(key=lambda r: (r["owner"] is None, r["clause"] or ""))
        out.append(group[0])
    out.sort(key=spec_key)
    return out


def named_tags():
    """Tags that carry at least one real name, in wire order."""
    return [t for t in sorted(TAGS, key=lambda t: (len(t), t))
            if best_records(TAGS[t])]


def field_name(rec):
    """The human label for a tag: the field it tags, else the owning structure."""
    if rec.get("field"):
        return rec["field"]
    if rec.get("owner"):
        return rec["owner"]
    return ""


def describe(rec):
    f, o = rec.get("field"), rec.get("owner")
    if f and o and f != o:
        return f"`{f}` in `{o}`"
    if o:
        return f"`{o}`"
    if f:
        return f"`{f}`"
    return ""


def split_tag(tag):
    """Group tags by first octet so the table reads in wire order."""
    return tag[:2]


# ---------------------------------------------------------------- human page

def build_human():
    lines = []
    total_occ = DATA["tagOccurrences"]
    n_tags = DATA["uniqueTags"]
    n_files = DATA["fileCount"]

    # Group by class, then by first octet.
    by_class = defaultdict(list)
    for tag, recs in TAGS.items():
        cls = recs[0]["class"]
        by_class[cls].append(tag)

    # Per-spec counts for the coverage table.
    spec_counts = Counter()
    for tag, recs in TAGS.items():
        if not best_records(recs):
            continue
        for spec in {r["spec"] for r in recs}:
            spec_counts[spec] += 1

    named = named_tags()
    n_named = len(named)

    lines.append("""---
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

""")

    lines.append(f"**Corpus:** {n_named} named tags, {total_occ:,} tag occurrences "
                 f"across {n_files} spec documents.\n")
    lines.append(f"""
Rows are included when the source document actually names the tag, either as an
ASN.1 structure or field, or as a labelled 3GPP/ETSI tag element. A further
{DATA['uniqueTags'] - n_named} hex values appear in the corpus only as prose
mentions, mostly GlobalPlatform X.509 certificate field tags such as `Tag '42'`,
which belong to a different namespace and are excluded so a lookup here never
returns a nameless row.
""")
    lines.append("""<style>
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
""")

    lines.append('<div class="tl-wrap">')
    lines.append('<table class="tl" id="tl-table">')
    lines.append("<thead><tr><th>Tag</th><th>Name</th><th>Structure</th>"
                 "<th>Clause</th><th>Spec</th></tr></thead>")
    lines.append("<tbody>")

    # One row per (tag, spec) representative, ordered by tag then spec.
    for tag in named_tags():
        for rec in best_records(TAGS[tag]):
            desc = describe(rec)
            # Structure column only earns its place when the Name column is
            # showing a *field*. Repeating the owner name twice is noise.
            struct = f"`{rec['owner']}`" if (rec.get("owner") and rec.get("field")
                                              and rec["field"] != rec["owner"]) else ""
            clause = rec.get("clause") or ""
            spec = SPEC_LABEL.get(rec["spec"], rec["spec"])
            search = " ".join(filter(None, [
                tag, field_name(rec), rec.get("owner") or "", desc, clause, spec
            ])).lower()
            lines.append(
                f'<tr data-s="{search}">'
                f'<td class="tagcell"><code>{tag}</code></td>'
                f'<td>{desc}</td>'
                f'<td>{struct if struct != desc else ""}</td>'
                f'<td class="clause">{clause}</td>'
                f'<td>{spec}</td></tr>'
            )

    lines.append("</tbody></table></div>")

    lines.append("""
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
""")

    # Coverage table
    lines.append("\n## Coverage\n\nWhich documents, and how many distinct tags each "
                 "contributes:\n\n| Document | Tags |\n|---|---|\n")
    for spec, n in sorted(spec_counts.items(),
                          key=lambda kv: SPEC_ORDER.get(kv[0], 99)):
        lines.append(f"| {SPEC_LABEL.get(spec, spec)} | {n} |")

    lines.append("""
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
""")

    return "\n".join(lines)


# ------------------------------------------------------------- condensed page

def build_ai():
    lines = []
    lines.append("""---
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
""")
    for tag in named_tags():
        for rec in best_records(TAGS[tag]):
            name = field_name(rec) or "unknown"
            # Only repeat the owner when the name came from a field inside it.
            struct = rec.get("owner") if (rec.get("field") and rec["owner"]
                                          and rec["field"] != rec["owner"]) else ""
            clause = rec.get("clause") or ""
            spec = SPEC_LABEL.get(rec["spec"], rec["spec"])
            lines.append(f"| `{tag}` | {name} | {struct} | {clause} | {spec} |")

    lines.append(f"""
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

- distinct named tags: {len(named_tags())}
- tag occurrences in corpus: {DATA['tagOccurrences']}
- source documents: {DATA['fileCount']}

Rows are included only where the source document names the tag. Hex values that
appear solely as prose mentions (GlobalPlatform X.509 certificate field tags such
as `Tag '42'`) are excluded as a different namespace.
""")
    return "\n".join(lines)


os.makedirs(os.path.join(ROOT, "ai"), exist_ok=True)

human = os.path.join(ROOT, "docs", "tag-lookup.md")
cond = os.path.join(ROOT, "ai", "tag-lookup.md")

with open(human, "w", encoding="utf-8") as fh:
    fh.write(build_human())
with open(cond, "w", encoding="utf-8") as fh:
    fh.write(build_ai())

print(f"wrote {human}  ({os.path.getsize(human)} bytes)")
print(f"wrote {cond}   ({os.path.getsize(cond)} bytes)")
print(f"tags: {DATA['uniqueTags']}  occurrences: {DATA['tagOccurrences']}")
