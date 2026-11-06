#!/usr/bin/env python3
"""Verify every curated module link on the GCF RSP register.

The links in data/gcf-rsp-module-links.json are researched by hand, not
harvested, so they rot silently. This fetches each one and reports:

  ok      200 and, for documents, a body that really starts with %PDF
  soft    403/429 — the host blocks scripted clients but the URL resolves in a
          browser; not treated as dead, but flagged so nobody assumes it was
          machine-verified
  dead    anything else, or a "PDF" that is actually an HTML error page

Exit code is non-zero when anything is dead, so a cron job or CI step can fail
loudly instead of the page quietly serving 404s.

Usage: scripts/check-gcf-rsp-links.py [--quiet]
"""

import json
import os
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINKS = os.path.join(ROOT, "data", "gcf-rsp-module-links.json")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"}
DOC_FIELDS = ("datasheet", "at_commands")
SOFT = (403, 429, 503)


def check(url, expect_pdf):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=40) as r:
            head = r.read(1024)
            status, ctype = r.status, r.headers.get("Content-Type", "")
    except urllib.error.HTTPError as exc:
        return ("soft" if exc.code in SOFT else "dead", f"HTTP {exc.code}")
    except Exception as exc:  # noqa: BLE001
        return ("dead", f"{type(exc).__name__}")
    if expect_pdf and head[:5] != b"%PDF-":
        return ("dead", f"not a PDF ({ctype or 'no type'})")
    return ("ok", f"{status} {ctype.split(';')[0]}")


def main():
    quiet = "--quiet" in sys.argv
    if not os.path.exists(LINKS):
        print(f"no link file at {LINKS}", file=sys.stderr)
        return 1
    data = json.load(open(LINKS, encoding="utf-8"))
    modules = data.get("modules", {})
    counts = {"ok": 0, "soft": 0, "dead": 0}
    dead = []
    # One module family shares one URL (nine Rolling Wireless models point at the
    # same family page); checking it nine times just gets us rate-limited to 429.
    cache = {}
    for key in sorted(modules):
        entry = modules[key]
        for field in ("vendor_page",) + DOC_FIELDS:
            url = entry.get(field)
            if not url:
                continue
            if url not in cache:
                cache[url] = check(url, expect_pdf=field in DOC_FIELDS)
            state, detail = cache[url]
            counts[state] += 1
            if state == "dead":
                dead.append((key, field, url, detail))
            if not quiet or state != "ok":
                print(f"{state:5} {key.split('|')[1]:<14} {field:<10} {detail:<28} {url[:70]}")
    total = sum(counts.values())
    print(f"\n{total} links: {counts['ok']} ok, {counts['soft']} soft-blocked, {counts['dead']} dead")
    if dead:
        print("\nDEAD:")
        for key, field, url, detail in dead:
            print(f"  {key} [{field}] {detail}\n    {url}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
