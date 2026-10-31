#!/usr/bin/env python3
"""Build the unified eUICC tag database and render the two public pages.

Five namespaces are merged, each with its own scope key. They are NOT summed into
one number, because a single count across them would be a category error:

  rsp        eSIM RSP ASN.1 BER tags      key: (spec module, tag)
  alloc      ETSI TS 101 220 §7.2         key: (tag type, context template, tag)
  gp         GlobalPlatform BER-TLV       key: (document, tag)
  usat       3GPP TS 31.111 §9 USAT       key: (tag, section)
  ef         SIM EF / FID file IDs        key: (ADF, FID)   [not BER tags]

Inputs are the JSON datasets produced by the parsers in this directory:
  parse-101220.py, parse-gp-tags.py, parse-31111.py, parse-ef-fid.py,
  extract-tags.py

Outputs:
  data/tag-db.json          the merged database
  docs/tag-database.md      searchable page with a namespace filter
  ai/tag-database.md        condensed single table for retrieval / LLM use

Never hand-edit the generated markdown; re-run this script instead.
"""

import json
import os
import re
import sys

ROOT = os.path.expanduser("~/repos/esim-knowledge")
TMP = "/tmp"

NS_META = {
    "rsp": {
        "label": "eSIM RSP ASN.1",
        "key": "(module, tag)",
        "blurb": "BER tags inside ES10, ES9+ and ESipa messages. Context class "
                 "BFxx and 9Fxx, application class 5Fxx.",
    },
    "alloc": {
        "label": "ETSI TS 101 220 allocator",
        "key": "(type, context, tag)",
        "blurb": "Every tag value ETSI actually allocates, in three encodings: "
                 "COMPACT-TLV, BER-TLV and COMPREHENSION-TLV.",
    },
    "gp": {
        "label": "GlobalPlatform BER-TLV",
        "key": "(document, tag)",
        "blurb": "Card and Security Domain data objects. A tag means different "
                 "things in different GlobalPlatform documents, so the document "
                 "is part of the key.",
    },
    "usat": {
        "label": "3GPP USAT (TS 31.111)",
        "key": "(tag, section)",
        "blurb": "The 3GPP names for USAT tags plus the reassign flag, which "
                 "exists only in TS 31.111.",
    },
    "ef": {
        "label": "SIM EF / FID file IDs",
        "key": "(ADF, FID)",
        "blurb": "File identifiers, not BER tags. The same FID carries different "
                 "names under different application DFs.",
    },
}
ORDER = ["rsp", "alloc", "gp", "usat", "ef"]


def load(name, default=None):
    path = os.path.join(TMP, name)
    if not os.path.exists(path):
        print(f"  ! missing input {path} (run its parser first)")
        return default
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def cell(text, limit=120):
    """Markdown-safe table cell: no pipes, no newlines, bounded length."""
    t = re.sub(r"\s+", " ", str(text or "")).strip()
    t = t.replace("|", "/").replace("`", "'")
    if len(t) > limit:
        t = t[: limit - 1].rstrip() + "\u2026"
    return t


def spec_label(s):
    """Human label for a source document name."""
    m = re.match(r"SGP\.(\d+(?:-\d+)?)-v(.+)$", s)
    if m:
        return f"SGP.{m.group(1)} v{m.group(2)}"
    if s.startswith("TCA-eUICC-Profile-Package"):
        return "TCA Pkg v3.4.1"
    if s.startswith("TCA-eUICC-Interop"):
        return "TCA Interop v3.4"
    return s


def build_rows():
    rows = []

    # ---- rsp: one row per named (tag, spec) representative
    rsp = load("tags.json") or load("tags_current.json")
    if rsp:
        for tag in sorted(rsp["tags"], key=lambda t: (len(t), t)):
            named = [r for r in rsp["tags"][tag]
                     if r.get("owner") or r.get("field")]
            if not named:
                continue
            seen = set()
            for r in named:
                spec = r["spec"]
                if spec in seen:
                    continue
                seen.add(spec)
                name = r.get("field") or r.get("owner") or ""
                owner = r.get("owner") or ""
                rows.append({
                    "ns": "rsp", "tag": tag, "name": name,
                    "scope": owner if owner and owner != name else "",
                    "kind": "BER",
                    "spec": spec_label(spec), "clause": r.get("clause") or "",
                    "line": r.get("line"), "extra": "",
                })

    # ---- alloc
    alloc = load("tlv_types.json")
    if alloc:
        for r in alloc["rows"]:
            if r.get("rangeEnd") or r["name"] == "Not used":
                continue
            rows.append({
                "ns": "alloc", "tag": r["tag"], "name": r["name"],
                "scope": r["context"], "kind": r["type"],
                "spec": "ETSI TS 101 220", "clause": "7.2",
                "line": r.get("line"),
                "extra": ("alt " + r["alt"]) if r.get("alt") else "",
            })

    # ---- gp
    gp = load("gp_tags.json")
    if gp:
        for r in gp["rows"]:
            rows.append({
                "ns": "gp", "tag": r["tag"], "name": r["name"],
                "scope": r["doc"], "kind": "BER",
                "spec": "GlobalPlatform", "clause": r.get("clause") or "",
                "line": r.get("line"), "extra": r.get("length") or "",
            })

    # ---- usat
    usat = load("usat_tags.json")
    if usat:
        for r in usat["rows"]:
            rows.append({
                "ns": "usat", "tag": r["tag"], "name": r["name"],
                "scope": r["section"], "kind": "BER" if "BER" in r["section"]
                        else "COMPREHENSION",
                "spec": "3GPP TS 31.111", "clause": "9",
                "line": r.get("line"), "extra": r.get("reassign") or "",
            })

    # ---- ef / fid
    ef = load("ef_fid.json")
    if ef:
        for r in ef["rows"]:
            rows.append({
                "ns": "ef", "tag": r["fid"], "name": r["name"] or "(name in a separate table)",
                "scope": r["adf"], "kind": "file ID",
                "spec": r["spec"], "clause": "",
                "line": r.get("line"), "extra": "",
            })

    return rows


def counts(rows):
    per = {}
    for ns in ORDER:
        sub = [r for r in rows if r["ns"] == ns]
        if not sub:
            continue
        per[ns] = {
            "rows": len(sub),
            "tags": len({r["tag"] for r in sub}),
        }
    return per


CSS = """<style>
.db-search{width:100%;padding:.75rem 1rem;font-size:1.05rem;font-family:inherit;
  background:rgba(93,173,226,.08);border:1px solid #1b3a5c;border-radius:8px;
  color:#c8d6e5;margin:1rem 0 .5rem;box-sizing:border-box}
.db-search:focus{outline:none;border-color:#5dade2;background:rgba(93,173,226,.14)}
[data-theme="light"] .db-search{background:#f7fafc;border-color:#e2e8f0;color:#2d3748}
.db-chips{display:flex;flex-wrap:wrap;gap:.4rem;margin:0 0 .6rem}
.db-chip{font:inherit;font-size:.82rem;padding:.32rem .7rem;border-radius:999px;
  border:1px solid #1b3a5c;background:transparent;color:#8b9dc3;cursor:pointer}
.db-chip:hover{border-color:#5dade2;color:#85c1e9}
.db-chip[aria-pressed="true"]{background:rgba(93,173,226,.18);border-color:#5dade2;color:#e8eef5}
[data-theme="light"] .db-chip{color:#4a5568;border-color:#e2e8f0}
[data-theme="light"] .db-chip[aria-pressed="true"]{background:rgba(49,130,206,.12);
  border-color:#2b6cb0;color:#1a202c}
.db-count{font-size:.85rem;color:#8b9dc3;margin-bottom:.8rem}
.db-wrap{max-height:70vh;overflow:auto;border:1px solid #1b3a5c;border-radius:8px}
table.db{border-collapse:collapse;width:100%;font-size:.84rem;margin:0}
table.db th{position:sticky;top:0;background:#0d1d30;text-align:left;padding:.55rem .7rem;
  border-bottom:1px solid #1b3a5c;z-index:2;font-weight:600}
table.db td{padding:.42rem .7rem;border-bottom:1px solid rgba(27,58,92,.5);vertical-align:top}
table.db tr:hover td{background:rgba(93,173,226,.06)}
table.db code{background:rgba(93,173,226,.14);padding:.08rem .35rem;border-radius:3px;
  font-size:.85rem;white-space:nowrap;color:#85c1e9}
table.db .tagcell code{font-weight:700;color:#fbbf24;font-size:.9rem}
table.db .ns{color:#8b9dc3;white-space:nowrap;font-size:.78rem}
[data-theme="light"] .db-wrap{border-color:#e2e8f0}
[data-theme="light"] table.db th{background:#edf2f7;border-color:#e2e8f0;color:#1a202c}
[data-theme="light"] table.db td{border-color:#edf2f7;color:#2d3748}
[data-theme="light"] table.db .ns{color:#718096}
[data-theme="light"] table.db code{background:rgba(49,130,206,.1);color:#2b6cb0}
[data-theme="light"] table.db .tagcell code{color:#b7791f}
[data-theme="light"] .db-count{color:#718096}
</style>"""

JS = """
<script>
(function(){
  var input = document.getElementById('db-search');
  var rows = Array.prototype.slice.call(document.querySelectorAll('#db-table tbody tr'));
  var count = document.getElementById('db-count');
  var chips = Array.prototype.slice.call(document.querySelectorAll('.db-chip'));
  var active = 'all';
  function update(){
    var q = input.value.trim().toLowerCase();
    var shown = 0;
    rows.forEach(function(r){
      var okNs = (active === 'all') || (r.dataset.ns === active);
      var okQ = !q || r.dataset.s.indexOf(q) !== -1;
      var hit = okNs && okQ;
      r.style.display = hit ? '' : 'none';
      if (hit) shown++;
    });
    count.textContent = shown + ' of ' + rows.length + ' rows'
      + (active === 'all' ? '' : ' in ' + active)
      + (q ? ' matching "' + input.value.trim() + '"' : '') + '.';
  }
  input.addEventListener('input', update);
  chips.forEach(function(c){
    c.addEventListener('click', function(){
      active = c.dataset.ns;
      chips.forEach(function(o){ o.setAttribute('aria-pressed', o === c ? 'true' : 'false'); });
      update();
    });
  });
  update();
})();
</script>
"""


def render_human(rows, per):
    total = len(rows)
    L = []
    L.append("""---
layout: default
title: "eUICC Tag Database: Every TLV Tag, File ID and Data Object Across the Specs"
description: "Searchable database of every TLV tag in the eSIM and smart card specifications: eSIM RSP BER tags, the ETSI TS 101 220 allocation tables, GlobalPlatform BER-TLV, 3GPP USAT tags and SIM EF file IDs, each with the scope that disambiguates it and the document and line it came from."
---

# eUICC Tag Database

Every TLV tag value this site can evidence, from five specification families, in
one searchable table. Type a hex value to find what it means, or type a name to
find its tag.

A tag value alone does not identify an object. The same value means different
things in different scopes, so every row carries the scope it was defined in:
the ASN.1 module, the containing template, the GlobalPlatform document, or the
application DF for a file ID. Rows are extracted from the specification text and
carry the document and line they came from.
""")
    L.append(f"**Corpus:** {total:,} rows across {len(per)} namespaces.\n")
    L.append("""## The five namespaces

Do not add these numbers together. They are different key spaces and a single
total would be a category error.
""")
    L.append("| Namespace | Key | Rows | Distinct values |")
    L.append("|---|---|---|---|")
    for ns in ORDER:
        if ns not in per:
            continue
        m = NS_META[ns]
        L.append(f"| {m['label']} | `{m['key']}` | {per[ns]['rows']:,} | "
                 f"{per[ns]['tags']:,} |")
    L.append("")
    for ns in ORDER:
        if ns in per:
            L.append(f"- **{NS_META[ns]['label']}** ({NS_META[ns]['key']}): "
                     f"{NS_META[ns]['blurb']}")
    L.append("")
    L.append(CSS)
    L.append("""
<input type="search" id="db-search" class="db-search"
  placeholder="Search a tag or a name: BF36, E0, 6F07, '83'&hellip;"
  aria-label="Search tags">
<div class="db-chips" role="group" aria-label="Filter by namespace">""")
    L.append('<button class="db-chip" data-ns="all" aria-pressed="true">All</button>')
    for ns in ORDER:
        if ns in per:
            L.append(f'<button class="db-chip" data-ns="{ns}" '
                     f'aria-pressed="false">{NS_META[ns]["label"]}</button>')
    L.append("</div>")
    L.append('<div class="db-count" id="db-count"></div>')
    L.append('<div class="db-wrap">')
    L.append('<table class="db" id="db-table">')
    L.append("<thead><tr><th>Tag</th><th>Name</th><th>Scope</th>"
             "<th>Namespace</th><th>Document</th><th>Clause</th></tr></thead>")
    L.append("<tbody>")
    for r in rows:
        search = " ".join(filter(None, [
            r["tag"], r["name"], r["scope"], r["kind"], r["spec"], r["clause"],
            NS_META[r["ns"]]["label"],
        ])).lower()
        L.append(
            f'<tr data-ns="{r["ns"]}" data-s="{cell(search, 400)}">'
            f'<td class="tagcell"><code>{cell(r["tag"], 12)}</code></td>'
            f'<td>{cell(r["name"])}</td>'
            f'<td>{cell(r["scope"], 90)}</td>'
            f'<td class="ns">{NS_META[r["ns"]]["label"]}</td>'
            f'<td>{cell(r["spec"], 60)}</td>'
            f'<td class="ns">{cell(r["clause"], 30)}</td></tr>'
        )
    L.append("</tbody></table></div>")
    L.append(JS)
    L.append("""
## How to read a tag

The first octet of a BER tag is an X.690 identifier octet: two class bits, one
primitive or constructed bit, and five tag number bits. When those five bits are
all ones, the tag is in high tag number form and the tag number is the next
octet.

| First octet | Class | Where you meet it |
|---|---|---|
| `BF` | context, constructed | eUICC wrappers: `BF36` BoundProfilePackage, `BF37` ProfileInstallationResult |
| `9F` | context, primitive | eUICC fields: `9F1F` serviceDescription |
| `5F` | application, primitive | ISO 7816 proprietary tags, including GlobalPlatform `5F37` |
| `DF` | private | not used by GSMA RSP, normally a misread `9F` |

A file ID such as `6F07` is not a BER tag. It is an ISO 7816 file identifier,
resolved against the application DF that contains it, which is why the EF rows
carry an ADF column.

## Common questions

**Why does the same value appear several times?** Because the value is scoped.
`83` is File Identifier inside an FCP template and Key Reference inside a control
reference template, both correct. `E1` is Individual Key Information in the
GlobalPlatform Card Spec and Signature Algorithm in Amendment A. `6F07` is IMSI
under ADF_USIM and the ISIM Service Table under ADF_ISIM.

**Which row is authoritative for a tag value's legality?** The ETSI TS 101 220
rows. That document is the allocator: it states which values exist at all, and it
declares all unassigned values reserved for future use. Other documents use those
values, they do not allocate them.

**Is a tag missing?** Tell me the document and clause and it can be added. The
pipeline is re-runnable: each namespace has a parser in `scripts/` and the page is
generated from the merged dataset.

## Related

- [Status Word Reference]({{ site.baseurl }}/docs/status-words): the two-byte
  result code that ends every APDU.
- [Tag Database, condensed]({{ site.baseurl }}/ai/tag-database): the same rows as
  one flat table for programmatic or LLM extraction.
- [Tag Lookup]({{ site.baseurl }}/docs/tag-lookup): the eSIM RSP namespace on its
  own, with worked examples.

## Sources

Generated by `scripts/build-tag-db.py` from the datasets produced by
`scripts/extract-tags.py`, `scripts/parse-101220.py`, `scripts/parse-gp-tags.py`,
`scripts/parse-31111.py` and `scripts/parse-ef-fid.py`. Every row records the
document and line it was extracted from. Nothing on this page is asserted from
memory.
""")
    return "\n".join(L)


def render_ai(rows, per):
    L = []
    L.append("""---
layout: default
title: "Tag Database, Condensed (machine-readable)"
description: "One row per TLV tag across eSIM RSP, ETSI TS 101 220, GlobalPlatform, 3GPP USAT and SIM EF file IDs, with the scope key that disambiguates the value, plus the document and clause. For programmatic or LLM extraction."
---

# Tag Database, Condensed

One row per tag. Columns: **Tag**, **Name**, **Scope**, **Namespace**,
**Key**, **Document**, **Clause**.

The **Scope** column is load-bearing. A tag value alone does not identify an
object: `83` is a file identifier in one template and a key reference in another,
`6F07` is IMSI under one ADF and a service table under another. Resolve the scope
first, then the name.

Prefer this page over the prose version for programmatic or LLM extraction.
""")
    L.append("[Full database with search and namespace filter]"
             "({{ site.baseurl }}/docs/tag-database)\n")
    L.append("| Namespace | Key | Rows | Distinct values |")
    L.append("|---|---|---|---|")
    for ns in ORDER:
        if ns in per:
            m = NS_META[ns]
            L.append(f"| {m['label']} | `{m['key']}` | {per[ns]['rows']:,} | "
                     f"{per[ns]['tags']:,} |")
    L.append("")
    L.append("| Tag | Name | Scope | Namespace | Key | Document | Clause |")
    L.append("|---|---|---|---|---|---|---|")
    for r in rows:
        L.append(f"| `{cell(r['tag'], 12)}` | {cell(r['name'])} | "
                 f"{cell(r['scope'], 90)} | {NS_META[r['ns']]['label']} | "
                 f"`{NS_META[r['ns']]['key']}` | {cell(r['spec'], 60)} | "
                 f"{cell(r['clause'], 30)} |")
    L.append(f"""
---

## Lookup keys

- spaced and unspaced hex: `BF36` and `BF 36`
- quoted ASN.1 form: `Tag 'BF36'`
- bracketed tag number: `[54]` is the same tag as `BF36`
- file IDs with their ADF: `6F07` under `ADF_USIM`, not bare
- GlobalPlatform tags with their document: `E1` in the Card Spec, not bare

## Stats

- total rows: {len(rows):,}
- namespaces: {len(per)}
""")
    return "\n".join(L)


def main():
    rows = build_rows()
    if not rows:
        raise SystemExit("no input datasets found")
    per = counts(rows)

    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    db = {
        "generatedFrom": "~/gsma-specs",
        "namespaces": {ns: NS_META[ns] for ns in ORDER},
        "counts": per,
        "rows": rows,
    }
    dbpath = os.path.join(ROOT, "data", "tag-db.json")
    with open(dbpath, "w", encoding="utf-8") as fh:
        json.dump(db, fh, indent=1)

    human = os.path.join(ROOT, "docs", "tag-database.md")
    cond = os.path.join(ROOT, "ai", "tag-database.md")
    os.makedirs(os.path.join(ROOT, "ai"), exist_ok=True)
    with open(human, "w", encoding="utf-8") as fh:
        fh.write(render_human(rows, per))
    with open(cond, "w", encoding="utf-8") as fh:
        fh.write(render_ai(rows, per))

    print(f"rows total : {len(rows):,}")
    for ns in ORDER:
        if ns in per:
            print(f"  {ns:6s} {per[ns]['rows']:6,d} rows  {per[ns]['tags']:5,d} distinct")
    for p in (dbpath, human, cond):
        print(f"wrote {p}  ({os.path.getsize(p):,} bytes)")


if __name__ == "__main__":
    sys.exit(main() or 0)
