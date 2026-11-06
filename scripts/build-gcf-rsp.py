#!/usr/bin/env python3
"""Build the GCF RSP certification mirror and render the public pages.

GCF publishes three lists of eSIM/RSP certification records, and publishes them
only as a JavaScript-paged table of ten rows at a time. Nothing in their UI can
answer the questions people actually ask:

  "which modules do consumer RSP (SGP.22) rather than M2M RSP (SGP.02)?"
  "which of them have a soldered eUICC rather than a removable chip?"

The per-record facts that answer those questions exist, but only inside each
product's detail page, one page at a time. This script harvests the listings,
follows every detail page, and stores the result as one JSON file that the site
renders as searchable pages.

Sources (all public, no auth, no JS needed -- the listing endpoint is a plain GET):

  RSP certifications       /gcf-certified-products/rsp-certifications.html
                           pageId E996075A-7A84-472C-999A525CD4086B80
  RSP compliance           /gcf-certified-products/rsp-compliance.html
                           pageId 4D5919AE-B813-4742-A0907B789B00A302

Two traps in that endpoint, both load-bearing:

  * `pages` is ignored. Only `startRow` moves the window, so a pager built on
    the obvious parameter returns page 1 forever.
  * GCF's own filter is spelled `embededModuleOnly` (sic). Spelling it correctly
    silently returns the unfiltered list.

Outputs:
  data/gcf-rsp.json           the mirror
  docs/gcf-rsp-modules.md     searchable page
  ai/gcf-rsp-modules.md       condensed single-table version for retrieval

Never hand-edit the generated markdown; re-run this script instead.

Usage:
  scripts/build-gcf-rsp.py              full harvest (cached detail pages)
  scripts/build-gcf-rsp.py --no-enrich  listings only, skip detail pages
"""

import argparse
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, ".cache", "gcf")
DATA = os.path.join(ROOT, "data", "gcf-rsp.json")

HOST = "https://www.globalcertificationforum.org"
CERT_LISTING = f"{HOST}/page-types/public_device_listing/ajaxLoadMoreResult/"
COMP_LISTING = f"{HOST}/page-types/public_rsp_declaration_listing/ajaxLoadMoreResult/"
PAGEID_CERT = "E996075A-7A84-472C-999A525CD4086B80"
PAGEID_COMP = "4D5919AE-B813-4742-A0907B789B00A302"

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")
HEADERS = {"User-Agent": UA, "From": "code@tuddenham.info",
           "Referer": f"{HOST}/gcf-certified-products/rsp-certifications.html"}
DELAY = 0.25

ROW = re.compile(r'<tr class="result-item">(.*?)</tr>', re.S)
TD = re.compile(r"<td[^>]*>(.*?)</td>", re.S)
# Section header or label/value pair, in document order, so a single pass keeps
# each declaration row under the heading it belongs to.
SCAN = re.compile(r"<th[^>]*>\s*(?P<th>.*?)\s*</th>"
                  r"|<tr[^>]*>\s*<td[^>]*>\s*(?P<label>.*?)\s*</td>\s*<td[^>]*>\s*(?P<value>.*?)\s*</td>",
                  re.S)
PROD_REF = re.compile(r"/pub_product/(\d+)\.html")


def get(url, cache_key=None, tries=3):
    """Fetch a URL, with an on-disk cache for the expensive detail pages."""
    if cache_key:
        path = os.path.join(CACHE, cache_key + ".html")
        if os.path.exists(path) and os.path.getsize(path) > 2000:
            return open(path, encoding="utf-8", errors="replace").read()
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=45) as r:
                body = r.read().decode("utf-8", "replace")
            if cache_key:
                os.makedirs(CACHE, exist_ok=True)
                with open(os.path.join(CACHE, cache_key + ".html"), "w", encoding="utf-8") as f:
                    f.write(body)
            time.sleep(DELAY)
            return body
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"fetch failed after {tries} tries: {url}: {last}")


def text(fragment):
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()


def iso_date(value):
    try:
        return datetime.strptime(value.strip(), "%d-%b-%Y").date().isoformat()
    except ValueError:
        return ""


def walk_listing(endpoint, page_id, extra=None, limit=5000):
    """Walk a listing by startRow. `pages` does nothing; startRow is the offset."""
    rows, start = [], 1
    while start < limit:
        params = {"q": "", "pageId": page_id, "manufacturer": "", "type": "",
                  "dateCondition": "", "certificationDateFrom": "",
                  "certificationDateTo": "", "sortby": "certificationDate",
                  "sortdirection": "desc", "pages": 2, "startRow": start}
        if extra:
            params.update(extra)
        body = get(endpoint + "?" + urllib.parse.urlencode(params))
        batch = []
        for block in ROW.findall(body):
            cells = [text(c) for c in TD.findall(block)]
            if len(cells) < 6:
                continue
            batch.append(cells)
        if not batch:
            break
        rows.extend(batch)
        start += len(batch)
    return rows


def parse_cert_row(cells, embedded):
    ref, mfr, model, marketing, when = cells[0], cells[1], cells[2], cells[3], cells[4]
    return {"ref": ref, "manufacturer": mfr, "model": model, "marketing": marketing,
            "certified": iso_date(when), "embedded_module": embedded,
            "gcf_url": f"{HOST}/pub_product/{ref}.html"}


def parse_declaration(body):
    """Read the per-product declaration tables into a flat, section-keyed dict."""
    body = re.sub(r"<script.*?</script>", "", body, flags=re.S | re.I)
    sections, current = {}, None
    for m in SCAN.finditer(body):
        if m.group("th") is not None:
            heading = text(m.group("th")).rstrip(":").strip()
            if heading:
                current = heading
                sections.setdefault(current, [])
            continue
        label, value = text(m.group("label")).rstrip(":").strip(), text(m.group("value"))
        if current is None or not label:
            continue
        sections[current].append((label, value))
    return sections


def parse_product(ref, body):
    """Fold a detail page into the facts the listings page needs."""
    sections = parse_declaration(body)
    details = dict(sections.get("PRODUCT DETAILS", []))

    bands, caps = {}, {}
    for name, pairs in sections.items():
        if not name.startswith("SUPPORTED "):
            continue
        key = name[len("SUPPORTED "):].strip()
        supported, extra = [], {}
        for label, value in pairs:
            if value.lower() == "yes":
                supported.append(label)
            elif value:
                extra[label] = value
        if supported:
            bands[key] = supported
        for label, value in extra.items():
            caps[label] = value

    uicc = {label: value for label, value in sections.get("UICC/eUICC INFORMATION", [])}
    labels = [label for label, value in uicc.items() if value.lower() == "yes"]
    joined = " | ".join(labels)

    market = dict(sections.get(
        "Market Information for IoT Chipsets, Modules and Platforms supporting IoT", []))

    return {
        "manufacturer": details.get("Manufacturer", ""),
        "model": details.get("Model name", ""),
        "marketing": details.get("Marketing name", ""),
        "certified": iso_date(details.get("Date of Certification", "")),
        "rsp": {"sgp02_m2m": "SGP.02" in joined,
                "sgp22_consumer": "SGP.22" in joined,
                "sgp32_iot": "SGP.32" in joined,
                "labels": labels},
        "euicc": {"uicc_removable": "Supports Removable UICC" in uicc,
                  "uicc_non_removable": "Supports Non-Removable UICC" in uicc,
                  "removable": "Supports Removable eUICC" in uicc,
                  "non_removable": "Supports Non-Removable eUICC" in uicc},
        "bands": bands,
        "caps": caps,
        "release": caps.get("Audio 3GPP release implemented", ""),
        "application": market.get("Application(s)", ""),
        "market": market.get("Market(s)", ""),
        "vendor_url": market.get("Product URL", ""),
        "detail_parsed": bool(details),
    }


def harvest(enrich=True):
    print("listing: RSP certifications")
    cert_rows = walk_listing(CERT_LISTING, PAGEID_CERT)
    print(f"  {len(cert_rows)} rows")
    print("listing: RSP certifications, embedded modules only")
    mod_rows = walk_listing(CERT_LISTING, PAGEID_CERT, {"embededModuleOnly": "1"})
    print(f"  {len(mod_rows)} rows")
    print("listing: RSP compliance declarations")
    comp_rows = walk_listing(COMP_LISTING, PAGEID_COMP)
    print(f"  {len(comp_rows)} rows")

    embedded_refs = {r[0] for r in mod_rows}
    products = {}
    for cells in cert_rows:
        row = parse_cert_row(cells, cells[0] in embedded_refs)
        products[row["ref"]] = row
    # The filtered listing can contain a ref the unfiltered walk skipped when the
    # sort order drifts mid-harvest. Keep it rather than silently dropping a module.
    for cells in mod_rows:
        products.setdefault(cells[0], parse_cert_row(cells, True))

    compliance, seen = [], set()
    for cells in comp_rows:
        if cells[0] in seen:
            continue
        seen.add(cells[0])
        compliance.append({"rsp_id": cells[0], "gcf_ref": cells[1],
                           "manufacturer": cells[2], "model": cells[3],
                           "marketing": cells[4], "certified": iso_date(cells[5])})

    if enrich:
        todo = sorted(products)
        print(f"enriching {len(todo)} product detail pages")
        for i, ref in enumerate(todo, 1):
            body = get(products[ref]["gcf_url"], cache_key=f"p{ref}")
            facts = parse_product(ref, body)
            if facts["detail_parsed"]:
                gcf_url = products[ref]["gcf_url"]
                products[ref].update({k: v for k, v in facts.items() if k != "detail_parsed"})
                products[ref]["gcf_url"] = gcf_url
            if i % 50 == 0:
                print(f"  {i}/{len(todo)}")

    return products, compliance


def guard(products, compliance):
    """Refuse to overwrite a good dataset with a shrunken one.

    The listings are one HTML template away from returning nothing, and a silent
    empty rebuild would quietly empty the site.
    """
    problems = []
    mods = [p for p in products.values() if p.get("embedded_module")]
    if len(products) < 400:
        problems.append(f"only {len(products)} product certifications (expected ~600)")
    if len(mods) < 25:
        problems.append(f"only {len(mods)} embedded modules (expected ~38)")
    if len(compliance) < 300:
        problems.append(f"only {len(compliance)} compliance declarations (expected ~435)")
    bad = [p["ref"] for p in products.values() if not p.get("manufacturer") or not p.get("certified")]
    if bad:
        problems.append(f"{len(bad)} products missing manufacturer or date: {bad[:5]}")
    if os.path.exists(DATA):
        try:
            prev = json.load(open(DATA))
            prev_n = len(prev.get("products", []))
            if prev_n and len(products) < prev_n * 0.9:
                problems.append(f"product count fell {prev_n} -> {len(products)}")
        except (ValueError, KeyError):
            pass
    return problems


# --------------------------------------------------------------------------
# rendering
# --------------------------------------------------------------------------

BADGES = [("rsp-sgp22", "SGP.22 consumer"), ("rsp-sgp02", "SGP.02 M2M"),
          ("rsp-sgp32", "SGP.32 IoT"), ("euicc-soldered", "soldered eUICC"),
          ("euicc-removable", "removable eUICC")]


def rsp_label(p):
    rsp = p.get("rsp", {})
    names = []
    if rsp.get("sgp22_consumer"):
        names.append("SGP.22")
    if rsp.get("sgp02_m2m"):
        names.append("SGP.02")
    if rsp.get("sgp32_iot"):
        names.append("SGP.32")
    return " + ".join(names) or "not declared"


def euicc_label(p):
    e = p.get("euicc", {})
    if e.get("non_removable") and e.get("removable"):
        return "both"
    if e.get("non_removable"):
        return "soldered"
    if e.get("removable"):
        return "removable"
    return "not declared"


def band_summary(p):
    b = p.get("bands", {})
    lte = len(b.get("4G LTE FDD", [])) + len(b.get("4G LTE TDD", []))
    nr = len(b.get("5G NR", []))
    bits = []
    if lte:
        bits.append(f"LTE {lte}")
    if nr:
        bits.append(f"NR {nr}")
    if b.get("3G WCDMA"):
        bits.append(f"WCDMA {len(b['3G WCDMA'])}")
    if b.get("2G GSM"):
        bits.append(f"GSM {len(b['2G GSM'])}")
    return " · ".join(bits) or "—"


def esc(value):
    return html.escape(str(value or ""))


def search_attrs(*values):
    return esc(" ".join(str(v) for v in values if v).lower())


def module_row(p):
    flags = []
    rsp = p.get("rsp", {})
    e = p.get("euicc", {})
    if rsp.get("sgp22_consumer"):
        flags.append("rsp-sgp22")
    if rsp.get("sgp02_m2m"):
        flags.append("rsp-sgp02")
    if rsp.get("sgp32_iot"):
        flags.append("rsp-sgp32")
    if e.get("non_removable"):
        flags.append("euicc-soldered")
    if e.get("removable"):
        flags.append("euicc-removable")
    link = (f'<a href="{esc(p["vendor_url"])}" rel="nofollow noopener">{esc(p["model"])}</a>'
            if p.get("vendor_url") else f'<b>{esc(p["model"])}</b>')
    return (f'<tr class="gcf-row" data-flags="{" ".join(flags)}" '
            f'data-search="{search_attrs(p["manufacturer"], p["model"], p["marketing"], rsp_label(p))}">'
            f'<td>{esc(p["manufacturer"])}</td>'
            f'<td>{link}</td>'
            f'<td class="gcf-c">{esc(rsp_label(p))}</td>'
            f'<td class="gcf-c">{esc(euicc_label(p))}</td>'
            f'<td class="gcf-c">{esc(band_summary(p))}</td>'
            f'<td class="gcf-c">{esc(p.get("release") or "—")}</td>'
            f'<td class="gcf-c">{esc(p["certified"])}</td>'
            f'<td class="gcf-c"><a href="{esc(p["gcf_url"])}" rel="noopener">{esc(p["ref"])}</a></td>'
            f"</tr>")


def cert_row(p):
    return (f'<tr class="gcf-row" data-flags="" '
            f'data-search="{search_attrs(p["manufacturer"], p["model"], p["marketing"], rsp_label(p))}">'
            f'<td>{esc(p["manufacturer"])}</td><td>{esc(p["model"])}</td>'
            f'<td>{esc(p["marketing"])}</td><td class="gcf-c">{esc(rsp_label(p))}</td>'
            f'<td class="gcf-c">{esc(euicc_label(p))}</td>'
            f'<td class="gcf-c">{esc(p["certified"])}</td>'
            f'<td class="gcf-c"><a href="{esc(p["gcf_url"])}" rel="noopener">{esc(p["ref"])}</a></td></tr>')


def decl_row(c):
    gcf = (f'<a href="{HOST}/pub_product/{esc(c["gcf_ref"])}.html" rel="noopener">{esc(c["gcf_ref"])}</a>'
           if c.get("gcf_ref") else "—")
    return (f'<tr class="gcf-row" data-flags="" '
            f'data-search="{search_attrs(c["manufacturer"], c["model"], c["marketing"], c["rsp_id"])}">'
            f'<td>{esc(c["rsp_id"])}</td><td>{esc(c["manufacturer"])}</td>'
            f'<td>{esc(c["model"])}</td><td>{esc(c["marketing"])}</td>'
            f'<td class="gcf-c">{esc(c["certified"])}</td><td class="gcf-c">{gcf}</td></tr>')


STYLE = """
<style>
.gcf-hero{max-width:860px;margin:1.2rem auto .6rem}
.gcf-src{max-width:1100px;margin:1rem auto;padding:.75rem .95rem;font-size:.88rem;
  border-left:3px solid #5dade2;background:rgba(93,173,226,.07);border-radius:0 8px 8px 0;color:#a9bed6}
.gcf-src a{color:#85c1e9}
[data-theme="light"] .gcf-src{background:#f0f6fc;color:#44566c}
.gcf-controls{max-width:1100px;margin:1.2rem auto .4rem;display:flex;flex-wrap:wrap;gap:.5rem;align-items:center}
.gcf-search{flex:1 1 320px;min-width:220px;padding:.7rem .9rem;font-size:1rem;font-family:inherit;
  background:rgba(93,173,226,.08);border:1px solid #1b3a5c;border-radius:8px;color:#c8d6e5;box-sizing:border-box}
.gcf-search:focus{outline:none;border-color:#5dade2;background:rgba(93,173,226,.14)}
[data-theme="light"] .gcf-search{background:#f7fafc;border-color:#e2e8f0;color:#2d3748}
.gcf-chip{padding:.36rem .8rem;border-radius:999px;border:1px solid #1b3a5c;background:none;
  color:#85c1e9;font-size:.84rem;font-family:inherit;cursor:pointer}
.gcf-chip.on{background:rgba(93,173,226,.2);border-color:#5dade2;color:#e8eef5}
.gcf-count{max-width:1100px;margin:.2rem auto .9rem;color:#8b9dc3;font-size:.86rem}
.gcf-wrap{max-width:1100px;margin:0 auto 2rem;overflow-x:auto;border:1px solid #1b3a5c;border-radius:10px}
/* The theme's content column is ~650px, which squeezes an 8-column table into
   unreadable wrapping. Break the register out of the column, and give the table
   a floor width so narrow viewports scroll instead of squashing the cells. */
.gcf-src,.gcf-controls,.gcf-count,.gcf-wrap{position:relative;left:50%;
  transform:translateX(-50%);width:min(1100px,94vw);max-width:none;box-sizing:border-box}
table.gcf{width:100%;border-collapse:collapse;font-size:.86rem;margin:0;min-width:820px}
table.gcf th{position:sticky;top:0;background:#0d1b2a;text-align:left;padding:.55rem .6rem;
  border-bottom:1px solid #1b3a5c;color:#c8d6e5;font-weight:600;white-space:nowrap}
table.gcf td{padding:.45rem .6rem;border-bottom:1px solid rgba(27,58,92,.55);vertical-align:top}
table.gcf td.gcf-c{white-space:nowrap;color:#a9bed6}
table.gcf tr:hover td{background:rgba(93,173,226,.06)}
[data-theme="light"] table.gcf th{background:#eef2f7;color:#2d3748}
[data-theme="light"] table.gcf td{border-bottom:1px solid #e2e8f0;color:#2d3748}
[data-theme="light"] table.gcf td.gcf-c{color:#4a5a6e}
[data-theme="light"] .gcf-chip{border-color:#c3d3e2;color:#1b5e8c}
[data-theme="light"] .gcf-chip.on{background:#e3f0fa;border-color:#5dade2;color:#12405f}
[data-theme="light"] .gcf-count{color:#5b6b7f}
.gcf-none{padding:1rem .6rem;color:#8b9dc3}
details.gcf-more{max-width:1100px;margin:0 auto 1.6rem}
details.gcf-more>summary{cursor:pointer;color:#85c1e9;padding:.5rem 0}
</style>
"""

SCRIPT = """
<script>
/* This runs mid-document, before the table and controls exist, so it must wait
   for the DOM. Binding at parse time silently leaves every filter inert. */
document.addEventListener('DOMContentLoaded', function(){
  var input=document.getElementById('gcf-q'),
      chips=[].slice.call(document.querySelectorAll('.gcf-chip')),
      rows=[].slice.call(document.querySelectorAll('.gcf-row')),
      scopes=[].slice.call(document.querySelectorAll('[data-scope]')),
      active={};
  function apply(){
    var q=(input.value||'').trim().toLowerCase(), flags=Object.keys(active);
    rows.forEach(function(r){
      var ok=q===''||r.getAttribute('data-search').indexOf(q)>-1;
      if(ok&&flags.length){
        var have=(r.getAttribute('data-flags')||'').split(' ');
        ok=flags.every(function(f){return have.indexOf(f)>-1;});
      }
      r.style.display=ok?'':'none';
    });
    scopes.forEach(function(s){
      var name=s.getAttribute('data-scope'),
          shown=s.querySelectorAll('.gcf-row:not([style*="display: none"])').length,
          el=document.querySelector('[data-gcf-count="'+name+'"] b');
      if(el){el.textContent=shown;}
    });
  }
  if(input){input.addEventListener('input',apply);}
  chips.forEach(function(c){
    c.addEventListener('click',function(){
      var f=c.getAttribute('data-filter');
      if(active[f]){delete active[f];c.classList.remove('on');}
      else{active[f]=1;c.classList.add('on');}
      apply();
    });
  });
});
</script>
"""


def render_docs(products, compliance, fetched):
    mods = sorted([p for p in products.values() if p.get("embedded_module")],
                  key=lambda p: (-len(p.get("bands", {})), p["manufacturer"], p["model"]))
    mods.sort(key=lambda p: p["certified"], reverse=True)
    certs = sorted(products.values(), key=lambda p: p["certified"], reverse=True)
    decls = sorted(compliance, key=lambda c: c["certified"], reverse=True)

    sgp22 = sum(1 for p in mods if p["rsp"]["sgp22_consumer"])
    sgp02 = sum(1 for p in mods if p["rsp"]["sgp02_m2m"])
    soldered = sum(1 for p in mods if p["euicc"]["non_removable"])

    out = []
    out.append("""---
layout: default
title: "GCF-certified eSIM Modules and RSP Devices: The Searchable Register"
description: "Every cellular module GCF has certified for embedded eSIM, with the facts GCF's own list cannot filter: consumer RSP (SGP.22) vs M2M RSP (SGP.02), soldered or removable eUICC, band support and 3GPP release. Plus every RSP certification and RSP compliance declaration, searchable."
redirect_from:
  - /gcf-rsp
  - /gcf-rsp/
---

# GCF-certified eSIM modules and RSP devices

GCF publishes three registers of eSIM/RSP certification, ten rows at a time, and
none of them can be filtered by the question that matters: **does this module do
consumer RSP or only M2M RSP, and is its eUICC soldered or a removable chip?**
Those facts are in the product declarations but not in the listing.

This page is a mirror of all three registers with those facts pulled out.
""")
    out.append(f"""<div class="gcf-src">
<b>Source:</b> GCF's public certification registers —
<a href="{HOST}/gcf-certified-products/rsp-certifications.html">eSIM (RSP) Certifications</a> and
<a href="{HOST}/gcf-certified-products/rsp-compliance.html">eSIM (RSP) Compliance</a> —
including each product's own declaration page, linked from every row below.
Harvested {fetched}. <b>This is an unofficial mirror:</b> GCF is the authority, and
where this page differs from GCF, GCF is right. Not affiliated with or endorsed by GCF.
</div>

**Snapshot:** harvested {fetched} · **{len(mods)}** embedded modules ·
**{len(products)}** RSP product certifications · **{len(compliance)}** RSP compliance declarations.
Generated by `scripts/build-gcf-rsp.py` into `data/gcf-rsp.json`; do not edit this page by hand.
""")
    out.append(STYLE)
    out.append(SCRIPT)

    out.append(f"""
## Certified embedded modules ({len(mods)})

A module appears here when GCF has certified it with an embedded eUICC — the
filter GCF labels "embeded module only" (their spelling). {sgp22} declare consumer
RSP (SGP.22), {sgp02} declare M2M RSP (SGP.02), and {soldered} declare a
non-removable eUICC. The two are independent: a soldered eUICC can still be
SGP.22 consumer-provisioned, which is what an MFF2 design needs.

<div class="gcf-controls">
  <input id="gcf-q" class="gcf-search" type="search" placeholder="Search manufacturer, model or RSP flavour...">
  <button class="gcf-chip" data-filter="rsp-sgp22">SGP.22 consumer</button>
  <button class="gcf-chip" data-filter="rsp-sgp02">SGP.02 M2M</button>
  <button class="gcf-chip" data-filter="euicc-soldered">soldered eUICC</button>
  <button class="gcf-chip" data-filter="euicc-removable">removable eUICC</button>
</div>
<p class="gcf-count" data-gcf-count="mods">Showing <b>{len(mods)}</b> of {len(mods)} modules.</p>

<div class="gcf-wrap" data-scope="mods">
<table class="gcf">
<thead><tr><th>Manufacturer</th><th>Module</th><th>RSP</th><th>eUICC</th>
<th>Bands</th><th>3GPP</th><th>Certified</th><th>GCF ref</th></tr></thead>
<tbody>
""")
    out.extend(module_row(p) for p in mods)
    out.append("""</tbody></table></div>

**Reading the columns.** *RSP* is the remote provisioning flavour the
manufacturer declared in the certification declaration: `SGP.22` is consumer RSP
(SM-DP+ / LPA), `SGP.02` is M2M RSP. A module declaring only SGP.02 cannot be
provisioned by a consumer SM-DP+. *eUICC* is the mounting: `soldered` is a
non-removable eUICC (MFF2 or integrated), `removable` is a pluggable eUICC, `both`
means both options are declared. *Bands* counts the radio bands declared, not the
module's full capability. Dates are the certification date GCF records.

A module with no bands at all is usually an eUICC chip certified as a component
rather than a modem — SIMCom's E7088 and E7080 are in this list on those terms.
""")

    out.append(f"""
## All RSP product certifications ({len(products)})

Every product GCF has certified under the eSIM (RSP) scheme — phones, wearables,
routers, automotive units and modules. Same columns as above.
""")
    out.append(f"""<p class="gcf-count" data-gcf-count="certs">Showing <b>{len(certs)}</b> of {len(certs)} records.</p>
<div class="gcf-wrap" data-scope="certs">
<table class="gcf">
<thead><tr><th>Manufacturer</th><th>Model</th><th>Marketing name</th><th>RSP</th>
<th>eUICC</th><th>Certified</th><th>GCF ref</th></tr></thead>
<tbody>""")
    out.extend(cert_row(p) for p in certs)
    out.append("</tbody></table></div>")

    out.append(f"""
## RSP compliance declarations ({len(compliance)})

The separate compliance register: products whose RSP implementation was declared
compliant without a full certification record. Mostly notebooks and handsets —
Lenovo and Dell alone account for most of it, which is what an eSIM laptop fleet
looks like. Only a handful carry a GCF reference back to a certification record.
""")
    out.append(f"""<p class="gcf-count" data-gcf-count="decls">Showing <b>{len(decls)}</b> of {len(decls)} records.</p>
<div class="gcf-wrap" data-scope="decls">
<table class="gcf">
<thead><tr><th>RSP ID</th><th>Manufacturer</th><th>Model</th><th>Marketing name</th>
<th>Declared</th><th>GCF ref</th></tr></thead>
<tbody>""")
    out.extend(decl_row(c) for c in decls)
    out.append(f"""</tbody></table></div>

## What this register does and does not tell you

A GCF RSP certification means the product passed an RTO's test campaign against
the RSP conformance test plan for the declared flavour. It is evidence about the
*product's RSP behaviour*, not a statement about the eUICC operating system
inside it: the eUICC's own certification (SGP.23 / SGP.23-1 for the OS and its
interfaces) is a separate scheme. A module here can still ship with an eUICC OS
you would not choose.

It also does not tell you who the eUICC vendor is, whether the profile is
GSMA-compliant, or anything about SM-DP+ support. Treat the register as a floor,
not a shortlist.

Related on this site: [SGP.23 certification](/docs/articles/sgp23/21-sgp23-certification)
covers the eUICC-side scheme, and [SGP.23-1 certification](/docs/articles/sgp23-1/36-sgp23-1-certification)
covers the interface tests. The [standards map](/docs/standards-map) places both
against SGP.22 and SGP.02.

## Source

- **Registers:** [GCF eSIM (RSP) Certifications]({HOST}/gcf-certified-products/rsp-certifications.html)
  (filtered to embedded modules with GCF's `embededModuleOnly` flag) and
  [GCF eSIM (RSP) Compliance]({HOST}/gcf-certified-products/rsp-compliance.html).
- **Per-record facts:** the declaration table on each product's own GCF page
  (`{HOST}/pub_product/<ref>.html`), linked from the GCF ref column of every row.
- **Harvested:** {fetched}. GCF publishes these lists ten rows at a time from a
  scripted endpoint with no export, so the register is re-harvested and this page
  regenerated rather than transcribed.
- **Dataset:** `data/gcf-rsp.json` in the site repository, produced by
  `scripts/build-gcf-rsp.py`.
- **Authority:** GCF. This mirror is unofficial and unaffiliated; entries can lag
  GCF or be withdrawn there. Verify anything load-bearing against GCF directly.

*Generated by `scripts/build-gcf-rsp.py`. Do not edit this page by hand — re-run
the script.*
""")
    return "".join(out)


def render_ai(products, compliance, fetched):
    mods = sorted([p for p in products.values() if p.get("embedded_module")],
                  key=lambda p: p["certified"], reverse=True)
    certs = sorted(products.values(), key=lambda p: p["certified"], reverse=True)
    decls = sorted(compliance, key=lambda c: c["certified"], reverse=True)

    out = [f"""---
layout: default
title: "GCF RSP Register, Condensed (machine-readable)"
description: "One row per GCF eSIM (RSP) certification: manufacturer, model, certification date, declared RSP flavour (SGP.22 consumer / SGP.02 M2M), eUICC mounting, bands and GCF reference. Includes every RSP compliance declaration. For programmatic or LLM extraction."
---

# GCF RSP Register, Condensed

One row per record. Snapshot harvested {fetched}. Unofficial mirror of GCF's public
registers: [{HOST}/gcf-certified-products/rsp-certifications.html]({HOST}/gcf-certified-products/rsp-certifications.html).
GCF is the authority. Full page with search and filters: [GCF-certified eSIM modules]({{{{ site.baseurl }}}}/docs/gcf-rsp-modules)

Columns: **Manufacturer**, **Model**, **Certified** (ISO date), **RSP** (declared
flavours), **eUICC** (soldered / removable / both), **Bands** (declared band count
by family), **Release** (3GPP release declared), **GCF ref**.

## Certified embedded modules ({len(mods)})

A module is listed here when GCF certified it with an embedded eUICC. `RSP` and
`eUICC` are independent axes: consumer RSP on a soldered eUICC is a normal MFF2
design, not a contradiction. A row with no bands is usually an eUICC chip
certified as a component rather than a modem.

| Manufacturer | Model | Certified | RSP | eUICC | Bands | Release | GCF ref |
|---|---|---|---|---|---|---|---|
"""]
    for p in mods:
        out.append(f"| {p['manufacturer']} | {p['model']} | {p['certified']} | {rsp_label(p)} | "
                   f"{euicc_label(p)} | {band_summary(p).replace('·', '/')} | "
                   f"{p.get('release') or '-'} | {p['ref']} |\n")

    out.append(f"""
## All RSP product certifications ({len(products)})

Every product in GCF's eSIM (RSP) certification register.

| Manufacturer | Model | Marketing name | Certified | RSP | eUICC | GCF ref |
|---|---|---|---|---|---|---|
""")
    for p in certs:
        out.append(f"| {p['manufacturer']} | {p['model']} | {p['marketing']} | {p['certified']} | "
                   f"{rsp_label(p)} | {euicc_label(p)} | {p['ref']} |\n")

    out.append(f"""
## RSP compliance declarations ({len(compliance)})

Separate register: RSP compliance declared without a full certification record.
Mostly notebooks and handsets; only a few cross-reference a GCF certification.

| RSP ID | Manufacturer | Model | Marketing name | Declared | GCF ref |
|---|---|---|---|---|---|
""")
    for c in decls:
        out.append(f"| {c['rsp_id']} | {c['manufacturer']} | {c['model']} | {c['marketing']} | "
                   f"{c['certified']} | {c['gcf_ref'] or '-'} |\n")

    out.append("""
*Generated by `scripts/build-gcf-rsp.py`. Do not edit by hand.*
""")
    return "".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-enrich", action="store_true", help="skip product detail pages")
    args = ap.parse_args()

    products, compliance = harvest(enrich=not args.no_enrich)
    problems = guard(products, compliance)
    if problems:
        print("REFUSING to write -- dataset looks wrong:", file=sys.stderr)
        for p in problems:
            print("  -", p, file=sys.stderr)
        return 1

    mods = [p for p in products.values() if p.get("embedded_module")]
    fetched = date.today().isoformat()
    payload = {
        "generatedFrom": f"{HOST}/gcf-certified-products/rsp-certifications.html",
        "source": {"certifications": f"{HOST}/gcf-certified-products/rsp-certifications.html",
                   "compliance": f"{HOST}/gcf-certified-products/rsp-compliance.html",
                   "note": "Unofficial mirror. GCF is authoritative."},
        "fetched": fetched,
        "counts": {"products": len(products), "embedded_modules": len(mods),
                   "compliance": len(compliance)},
        "products": sorted(products.values(), key=lambda p: p["ref"]),
        "compliance": compliance,
    }
    os.makedirs(os.path.dirname(DATA), exist_ok=True)
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"wrote {DATA} ({len(products)} products, {len(mods)} modules, {len(compliance)} declarations)")

    docs = os.path.join(ROOT, "docs", "gcf-rsp-modules.md")
    with open(docs, "w", encoding="utf-8") as f:
        f.write(render_docs(products, compliance, fetched))
    ai = os.path.join(ROOT, "ai", "gcf-rsp-modules.md")
    with open(ai, "w", encoding="utf-8") as f:
        f.write(render_ai(products, compliance, fetched))
    print(f"wrote {docs} and {ai}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
