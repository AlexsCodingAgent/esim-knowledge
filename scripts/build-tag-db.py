#!/usr/bin/env python3
"""Build the unified eUICC tag database and render the two public pages.

Six namespaces are merged, each with its own scope key. They are NOT summed into
one number, because a single count across them would be a category error:

  rsp        eSIM RSP ASN.1 BER tags      key: (module, tag)
  alloc      ETSI TS 101 220 §7.2         key: (type, context, tag)
  gp         GlobalPlatform BER-TLV       key: (document, tag)
  card       3GPP / ETSI card-layer tags  key: (document, clause, tag)
  usat       3GPP TS 31.111 §9 USAT       key: (tag, section)
  ef         SIM EF / FID file IDs        key: (ADF, FID)   [not BER tags]

Rows are classified by the DOCUMENT they came from, not by which parser produced
them. Before that rule existed, 42 rows from TS 31.102, TS 31.103, TS 102 221 and
two GlobalPlatform documents rendered under the heading "eSIM RSP ASN.1", which is
the cross-document attribution defect at namespace level.

Inputs are the JSON datasets produced by the parsers in this directory:
  parse-101220.py, parse-gp-tags.py, parse-31111.py, parse-ef-fid.py,
  extract-tags.py

Outputs:
  data/tag-db.json          the merged database
  docs/tag-database.md      searchable page, grouped by tag value
  ai/tag-database.md        condensed single table for retrieval / LLM use

Never hand-edit the generated markdown; re-run this script instead.
"""

import json
import os
import re
import sys
from itertools import groupby

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
    "card": {
        "label": "3GPP / ETSI card-layer",
        "key": "(document, clause, tag)",
        "blurb": "Tags read out of USIM file contents and UICC command clauses. "
                 "Not RSP messages, and kept separate so they are never mistaken "
                 "for one.",
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
ORDER = ["rsp", "alloc", "gp", "card", "usat", "ef"]

# A published name must be a NAME. Prose that the extractor caught mid-sentence
# is dropped rather than shown as if it were an object name.
BAD_TAIL = re.compile(
    r"\b(with|of|for|and|or|the|to|in|on|by|from|as|at|that|which|is|are)$", re.I
)

# Whitespace-aligned tables put a presence column and a further flag directly
# after the name, so a row parsed cell-wise can swallow "Mandatory No" or
# "Optional No" into the name. Those are column values, never part of a name.
COLUMN_BLEED = re.compile(
    r"\s*\b(?:Mandatory|Optional|Conditional|DEPRECATED|RESERVED)\b.*$", re.I
)
FLAG_TAIL = re.compile(r"\s+(?:No|Yes|NR)$", re.I)


def tidy(name):
    n = COLUMN_BLEED.sub("", str(name or ""))
    n = FLAG_TAIL.sub("", n)
    return re.sub(r"\s+", " ", n).strip(" -:;,")


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


def bucket(spec):
    """Namespace from the source document, never from the parser that read it."""
    if spec.startswith(("SGP.", "TCA-")):
        return "rsp"
    if spec.startswith(("GPC", "GPD")):
        return "gp"
    return "card"


def asn1_num(tag):
    """ASN.1 tag number, so that `[54]` resolves to `BF36`.

    X.690: the low five bits of the first octet are the tag number, unless they
    are all ones, in which case the tag is in high tag number form and the next
    octet carries it.
    """
    if len(tag) < 2:
        return None
    first = int(tag[:2], 16)
    if (first & 0x1F) == 0x1F:
        return int(tag[2:4], 16) if len(tag) >= 4 else None
    return first & 0x1F


def name_ok(name):
    if not name or len(name.strip()) < 3:
        return False
    if BAD_TAIL.search(name.strip()):
        return False
    if not re.search(r"[A-Z]", name):
        return False
    return True


def build_rows():
    rows = []

    # ---- rsp + card: the ASN.1 comment extraction, split by document
    rsp = load("tags.json") or load("tags_current.json")
    dropped = 0
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
                if not name_ok(name):
                    dropped += 1
                    continue
                owner = r.get("owner") or ""
                ns = bucket(spec)
                scope = owner if (owner and owner != name) else spec_label(spec)
                rows.append({
                    "ns": ns, "tag": tag, "name": name,
                    "scope": scope, "kind": "BER",
                    "spec": spec_label(spec), "clause": r.get("clause") or "",
                    "line": r.get("line"), "extra": "",
                })
    if dropped:
        print(f"  dropped {dropped} prose-fragment names")

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
                "scope": r["section"],
                "kind": "BER" if "BER" in r["section"] else "COMPREHENSION",
                "spec": "3GPP TS 31.111", "clause": "9",
                "line": r.get("line"), "extra": r.get("reassign") or "",
            })

    # ---- ef / fid
    ef = load("ef_fid.json")
    if ef:
        for r in ef["rows"]:
            rows.append({
                "ns": "ef", "tag": r["fid"],
                "name": r["name"] or "(name in a separate table)",
                "scope": r["adf"], "kind": "file ID",
                "spec": r["spec"], "clause": "",
                "line": r.get("line"), "extra": "",
            })

    # Strip column bleed from every name before it is published.
    for r in rows:
        cleaned = tidy(r["name"])
        if cleaned:
            r["name"] = cleaned

    # Every row must carry a scope, because the page's whole premise is that the
    # scope is what disambiguates the value.
    for r in rows:
        if not r["scope"].strip():
            r["scope"] = r["spec"]

    # Group by tag value only, not by (namespace, tag). The page promises that
    # every reading of one value appears together, and the same value is often
    # defined in several namespaces: 83 lives in rsp, alloc, gp and usat at once.
    rows.sort(key=lambda r: (r["tag"], ORDER.index(r["ns"]), r["spec"]))
    return rows


def counts(rows):
    per = {}
    for ns in ORDER:
        sub = [r for r in rows if r["ns"] == ns]
        if not sub:
            continue
        per[ns] = {"rows": len(sub), "tags": len({r["tag"] for r in sub})}
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
table.db tbody.grp:hover td{background:rgba(93,173,226,.06)}
table.db tbody.grp{scroll-margin-top:90px}
table.db tbody.grp.flash td{background:rgba(251,191,36,.14)}
table.db code{background:rgba(93,173,226,.14);padding:.08rem .35rem;border-radius:3px;
  font-size:.85rem;white-space:nowrap;color:#85c1e9}
table.db td.tagcell{font-weight:700;color:#fbbf24;font-size:.9rem;
  border-right:1px solid rgba(27,58,92,.7);vertical-align:top;white-space:nowrap}
table.db td.tagcell code{font-weight:700;color:#fbbf24;font-size:.92rem}
table.db .badge{display:inline-block;margin-left:.4rem;padding:.05rem .4rem;
  border-radius:999px;font-size:.7rem;font-weight:600;background:rgba(251,191,36,.16);
  color:#fbbf24;vertical-align:middle}
table.db .perm{margin-left:.45rem;color:#4a6f96;text-decoration:none;font-weight:400}
table.db .perm:hover{color:#85c1e9}
table.db .ns{color:#8b9dc3;white-space:nowrap;font-size:.78rem}
.db-empty{display:none;padding:1.6rem 1rem;text-align:center;color:#8b9dc3}
.db-empty button{font:inherit;font-size:.85rem;margin-top:.6rem;padding:.35rem .9rem;
  border-radius:999px;border:1px solid #1b3a5c;background:transparent;color:#85c1e9;cursor:pointer}
[data-theme="light"] .db-wrap{border-color:#e2e8f0}
[data-theme="light"] table.db th{background:#edf2f7;border-color:#e2e8f0;color:#1a202c}
[data-theme="light"] table.db td{border-color:#edf2f7;color:#2d3748}
[data-theme="light"] table.db td.tagcell{border-color:#e2e8f0}
[data-theme="light"] table.db .ns{color:#718096}
[data-theme="light"] table.db code{background:rgba(49,130,206,.1);color:#2b6cb0}
[data-theme="light"] table.db td.tagcell code{color:#b7791f}
[data-theme="light"] .db-count{color:#718096}
[data-theme="light"] .db-empty{color:#718096}
</style>"""

JS = """
<script>
(function(){
  var input  = document.getElementById('db-search');
  var table  = document.getElementById('db-table');
  var count  = document.getElementById('db-count');
  var empty  = document.getElementById('db-empty');
  var reset  = document.getElementById('db-reset');
  var chips  = Array.prototype.slice.call(document.querySelectorAll('.db-chip'));
  var groups = Array.prototype.slice.call(table.querySelectorAll('tbody.grp'));
  var TOTAL  = %(total)d;
  var active = 'all';

  function norm(s){
    return s.toLowerCase().replace(/[\\s'"]/g,'').replace(/^tag/,'').replace(/^0x/,'');
  }
  function badges(g, n, tag){
    var td = document.createElement('td');
    td.className = 'tagcell';
    td.rowSpan = n;
    td.innerHTML = '<code>' + tag + '</code>' +
      (n > 1 ? '<span class="badge">' + n + ' readings</span>' : '') +
      '<a class="perm" href="#tag-' + g.dataset.ns + '-' + tag +
      '" title="Link to tag ' + tag + '" aria-label="Link to tag ' + tag + '">#</a>';
    return td;
  }
  function apply(){
    var raw = input.value.trim();
    var q = norm(raw);
    var br = q.match(/^\\[(\\d+)\\]$/);
    var num = br ? br[1] : null;
    var isHex = /^[0-9a-f]{2,16}$/.test(q);
    var shownRows = 0, shownGroups = 0;

    groups.forEach(function(g){
      var tag = g.dataset.tag;
      var taglc = tag.toLowerCase();
      var tagOk = false;
      if (num) tagOk = (g.dataset.n === num);
      else if (isHex) tagOk = (taglc.indexOf(q) === 0);

      Array.prototype.slice.call(g.querySelectorAll('td.tagcell')).forEach(function(td){ td.remove(); });
      var vis = [];
      Array.prototype.slice.call(g.children).forEach(function(tr){
        var hit;
        if (num || isHex) hit = tagOk;
        else hit = !q || tr.dataset.q.indexOf(q) !== -1;
        if (active !== 'all' && tr.dataset.ns !== active) hit = false;
        tr.style.display = hit ? '' : 'none';
        if (hit) vis.push(tr);
      });

      if (!vis.length){
        g.style.display = 'none';
      } else {
        g.style.display = '';
        shownGroups++;
        shownRows += vis.length;
        vis[0].insertBefore(badges(g, vis.length, tag), vis[0].firstChild);
      }
    });

    if (!shownRows){
      empty.style.display = 'block';
    } else {
      empty.style.display = 'none';
    }

    if (num || isHex){
      var ranked = groups.slice().sort(function(a, b){
        function rank(g){
          var t = g.dataset.tag.toLowerCase();
          if (t === q) return 0;
          if (t.indexOf(q) === 0) return 1;
          return 2;
        }
        var ra = rank(a), rb = rank(b);
        if (ra !== rb) return ra - rb;
        if (a.dataset.tag.length !== b.dataset.tag.length)
          return a.dataset.tag.length - b.dataset.tag.length;
        return a.dataset.tag < b.dataset.tag ? -1 : 1;
      });
      ranked.forEach(function(g){ table.appendChild(g); });
    }

    count.textContent = shownRows + ' of ' + TOTAL + ' readings across ' +
      shownGroups + ' tag values' + (active === 'all' ? '' : ' in ' + active) +
      (raw ? ' matching "' + raw + '"' : '') + '.';
    var hm = location.hash.match(/^#tag-([0-9A-Fa-f]+)$/);
    if (hm) highlight(hm[1].toUpperCase());
  }
  function highlight(tag){
    groups.forEach(function(g){
      if (g.dataset.tag.toUpperCase() === tag){
        g.classList.add('flash');
        g.scrollIntoView({block:'center'});
        setTimeout(function(){ g.classList.remove('flash'); }, 1600);
      }
    });
  }
  function fromHash(){
    var hm = location.hash.match(/^#tag-([0-9A-Fa-f]+)$/);
    if (!hm) return;
    input.value = hm[1];
    active = 'all';
    chips.forEach(function(c){ c.setAttribute('aria-pressed', c.dataset.ns === 'all' ? 'true' : 'false'); });
    apply();
  }

  input.addEventListener('input', apply);
  chips.forEach(function(c){
    c.addEventListener('click', function(){
      active = c.dataset.ns;
      chips.forEach(function(o){ o.setAttribute('aria-pressed', o === c ? 'true' : 'false'); });
      apply();
    });
  });
  reset.addEventListener('click', function(){
    input.value = '';
    active = 'all';
    chips.forEach(function(c){ c.setAttribute('aria-pressed', c.dataset.ns === 'all' ? 'true' : 'false'); });
    apply();
    input.focus();
  });
  window.addEventListener('hashchange', fromHash);
  fromHash();
  apply();
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

Every TLV tag value this site can evidence, from six specification families, in
one searchable table. Type a hex value, an ASN.1 tag number such as `[54]`, or a
name, and every reading of that value appears together.

A tag value alone does not identify an object. The same value means different
things in different scopes, so rows are grouped by value and each reading carries
the scope it was defined in: the ASN.1 module, the containing template, the
GlobalPlatform document, or the application DF for a file ID.
""")
    L.append(f"**Corpus:** {total:,} readings across {len(per)} namespaces. "
             f"Rows are extracted from the specification text and carry the "
             f"document and line they came from.\n")
    L.append("""## The six namespaces

Do not add these numbers together. They are different key spaces and a single
total would be a category error.
""")
    L.append("| Namespace | Key | Readings | Distinct values |")
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
  placeholder="Search a tag, a name, or an ASN.1 number: BF36, bf 36, [54], E0, 6F07&hellip;"
  aria-label="Search tags">
<div class="db-chips" role="group" aria-label="Filter by namespace">""")
    L.append('<button class="db-chip" data-ns="all" aria-pressed="true">All</button>')
    for ns in ORDER:
        if ns in per:
            L.append(f'<button class="db-chip" data-ns="{ns}" '
                     f'aria-pressed="false">{NS_META[ns]["label"]} '
                     f'({per[ns]["rows"]:,})</button>')
    L.append("</div>")
    L.append('<div class="db-count" id="db-count"></div>')
    L.append('<div class="db-wrap">')
    L.append('<table class="db" id="db-table">')
    L.append("<thead><tr><th>Tag</th><th>Name</th><th>Scope</th>"
             "<th>Namespace</th><th>Document</th><th>Clause</th></tr></thead>")

    for tag, grp in groupby(rows, key=lambda r: r["tag"]):
        g = list(grp)
        num = asn1_num(tag)
        # group search text: every row joined, normalised by the client
        gq = " ".join(filter(None, [
            tag, *[r["name"] for r in g], *[r["scope"] for r in g],
            *[r["spec"] for r in g], *[r["clause"] for r in g],
        ])).replace("|", "/").lower()
        L.append(f'<tbody class="grp" id="tag-{cell(tag, 12)}" '
                 f'data-tag="{cell(tag, 12)}" '
                 f'data-n="{num if num is not None else ""}" '
                 f'data-q="{cell(gq, 600)}">')
        for i, r in enumerate(g):
            rowq = " ".join(filter(None, [
                r["name"], r["scope"], r["kind"], r["spec"], r["clause"],
                NS_META[r["ns"]]["label"],
            ])).replace("|", "/").lower()
            tagcell = (f'<td class="tagcell" rowspan="{len(g)}">'
                       f'<code>{cell(tag, 12)}</code>'
                       + (f'<span class="badge">{len(g)} readings</span>'
                          if len(g) > 1 else "")
                       + f'<a class="perm" href="#tag-{cell(tag, 12)}" '
                         f'title="Link to tag {cell(tag, 12)}" '
                         f'aria-label="Link to tag {cell(tag, 12)}">#</a></td>'
                       ) if i == 0 else ""
            L.append(
                f'<tr data-ns="{r["ns"]}" data-q="{cell(rowq, 300)}">'
                f'{tagcell}'
                f'<td>{cell(r["name"])}</td>'
                f'<td>{cell(r["scope"], 90)}</td>'
                f'<td class="ns">{NS_META[r["ns"]]["label"]}</td>'
                f'<td>{cell(r["spec"], 60)}</td>'
                f'<td class="ns">{cell(r["clause"], 30)}</td></tr>'
            )
        L.append("</tbody>")

    L.append("</table>")
    L.append('<div class="db-empty" id="db-empty">'
             '<strong>No tag matched.</strong><br>'
             'Try a shorter hex value such as <code>83</code>, an ASN.1 number '
             'such as <code>[54]</code>, or clear the namespace filter.'
             '<br><button id="db-reset" type="button">Clear search and filters</button>'
             '</div>')
    L.append("</div>")
    L.append(JS % {"total": total})
    L.append("""
## How to read a tag

The first octet of a BER tag is an X.690 identifier octet: two class bits, one
primitive or constructed bit, and five tag number bits. When those five bits are
all ones, the tag is in high tag number form and the tag number is the next
octet. That is why `[54]` and `BF36` are the same tag: 0x36 is 54.

| First octet | Class | Where you meet it |
|---|---|---|
| `BF` | context, constructed | eUICC wrappers: `BF36` BoundProfilePackage, `BF37` ProfileInstallationResult |
| `9F` | context, primitive | eUICC fields: `9F1F` serviceDescription |
| `5F` | application, primitive | ISO 7816 proprietary tags, including GlobalPlatform `5F37` |
| `DF` | private | not used by GSMA RSP, normally a misread `9F` |

A file ID such as `6F07` is not a BER tag. It is an ISO 7816 file identifier,
resolved against the application DF that contains it, which is why the EF rows
carry an ADF scope.

## Common questions

**Why does one tag show several readings?** Because the value is scoped. `83` is
File Identifier inside an FCP template and Key Reference inside a control
reference template, both correct. `E1` is Individual Key Information in the
GlobalPlatform Card Spec and Signature Algorithm in Amendment A. `6F07` is IMSI
under ADF_USIM and the ISIM Service Table under ADF_ISIM.

**Which reading is authoritative for legality?** The ETSI TS 101 220 rows. That
document is the allocator: it states which values exist at all, and declares all
unassigned values reserved for future use. Other documents use those values, they
do not allocate them.

**Is a tag missing?** Tell me the document and clause and it can be added. Each
namespace has a parser in `scripts/` and this page is generated from the merged
dataset.

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

One row per reading. Columns: **Tag**, **Name**, **Scope**, **Namespace**,
**Key**, **Document**, **Clause**.

The **Scope** column is load-bearing. A tag value alone does not identify an
object: `83` is a file identifier in one template and a key reference in another,
`6F07` is IMSI under one ADF and a service table under another. Resolve the scope
first, then the name.

Prefer this page over the prose version for programmatic or LLM extraction.
""")
    L.append("[Full database with search, grouping and namespace filter]"
             "({{ site.baseurl }}/docs/tag-database)\n")
    L.append("| Namespace | Key | Readings | Distinct values |")
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

- spaced and unspaced hex: `BF36`, `BF 36` and `bf36`
- quoted ASN.1 form: `Tag 'BF36'`
- ASN.1 tag number: `[54]` is the same tag as `BF36`
- file IDs with their ADF: `6F07` under `ADF_USIM`, not bare
- GlobalPlatform tags with their document: `E1` in the Card Spec, not bare

## Stats

- total readings: {len(rows):,}
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

    empty = [r for r in rows if not r["scope"].strip()]
    print(f"readings   : {len(rows):,}")
    for ns in ORDER:
        if ns in per:
            print(f"  {ns:6s} {per[ns]['rows']:6,d} readings  "
                  f"{per[ns]['tags']:5,d} values")
    print(f"empty scopes: {len(empty)}")
    print(f"distinct tag values overall: {len({r['tag'] for r in rows}):,}")
    for p in (dbpath, human, cond):
        print(f"wrote {p}  ({os.path.getsize(p):,} bytes)")


if __name__ == "__main__":
    sys.exit(main() or 0)
