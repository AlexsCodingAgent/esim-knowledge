#!/usr/bin/env python3
"""Extract GlobalPlatform BER-TLV tags from the GP corpus.

GP is a different namespace from RSP ASN.1: ISO 7816-4 *application* class
('7F xx' / '5F xx' / single-byte), and the same tag genuinely differs between
documents, so every record is keyed (document, tag).

Three defects are guarded against, each of which has produced plausible-looking
wrong output before:
  1. some tags exist ONLY in prose bullets ("Tag 'E0': Key Information Template"),
     so a table-only parse both misses them and then borrows another document's
     meaning for the value;
  2. a row whose length column is exactly 0 is a *value* enumeration ('C0' = 0 =
     Empty), not a tag definition;
  3. continuation-line joining must be bounded, or one parse yields a 58 KB name.

Nothing is attributed across documents: a record's name comes only from the file
it was read from.

Usage: parse-gp-tags.py [out.json]
"""

import json
import os
import re
import sys
from collections import defaultdict

CORPUS = os.path.expanduser("~/gsma-specs/globalplatform")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/gp_tags.json"

ROW = re.compile(
    r"^\s*'([0-9A-Fa-f]{2}|[0-9A-Fa-f]{4})'\s{2,}"
    r"(Var|Variable|1-n|\d+-n|\d+-\d+|\d+|0-\d+|[A-Za-z]+\([^)]*\))\s{2,}"
    r"(.+)$"
)
PROSE = re.compile(
    r"(?:Tag|tag|template)\s+'([0-9A-Fa-f]{2}|[0-9A-Fa-f]{4})'\s*[:\u2013-]\s*"
    r"([A-Z][A-Za-z][^.;]{3,80})"
)
# Card Spec §11.3.3.1.1 defines the Key Information Data object the other way
# round: "each Key Information Data data object is introduced by the tag 'C0'".
# Without this the most important GP tag after E0/E1 is lost.
INTRODUCED = re.compile(
    r"(?:each|the)\s+([A-Z][A-Za-z0-9 ]{3,50}?)\s+data objects?\s+"
    r"(?:is|are)\s+introduced\s+by\s+the\s+tag\s+'([0-9A-Fa-f]{2,4})'"
)
PRESENCE = re.compile(
    r"\s*(Mandatory|Optional|Conditional|DEPRECATED|RESERVED)\s*$", re.I
)
CLAUSE = re.compile(r"^\s*(\d+(?:\.\d+){1,4})\s+([A-Z].{3,90})$")
# a row whose length cell is exactly 0 enumerates a *value*, it does not define
ENUM_ROW = re.compile(r"^\s*'[0-9A-Fa-f]{2}'\s+0\s{2,}")
NOISE = re.compile(r"^(ETSI|GlobalPlatform|Release |\f|NOTE|Table |Figure |\s*$)")
CONT = re.compile(r"^[A-Za-z][A-Za-z0-9 ,/()'\-\u2013&.]{2,80}$")


def clean(name):
    name = PRESENCE.sub("", name).strip()
    name = re.sub(r"\s*\((?:see )?note[^)]*\)\s*$", "", name, flags=re.I).strip()
    return name.strip(" -:;,.")


def parse_file(path):
    doc = re.sub(r"\.txt$", "", os.path.basename(path))
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            lines = fh.readlines()
    except OSError:
        return []

    out = []
    clause = None
    clause_title = None
    for i, line in enumerate(lines):
        m = CLAUSE.match(line)
        if m:
            clause, clause_title = m.group(1), m.group(2).strip()

        if ENUM_ROW.match(line):
            continue

        rm = ROW.match(line)
        if rm:
            tag = rm.group(1).upper()
            length = rm.group(2)
            name = clean(rm.group(3))
            # bounded continuation join: max 2 following lines, each <=80 chars,
            # stopping at anything that looks like a new row or rule
            j = i + 1
            joined = 0
            while j < len(lines) and joined < 2:
                nxt = lines[j].rstrip("\n")
                s = nxt.strip()
                if not s or NOISE.match(s) or "'" in s or not CONT.match(s):
                    break
                if len(s) > 80:
                    break
                name = f"{name} {s}".strip()
                if len(name) > 160:
                    break
                joined += 1
                j += 1
            if not name or len(name) < 3:
                continue
            out.append({
                "doc": doc, "tag": tag, "name": name[:160],
                "length": length, "clause": clause,
                "clauseTitle": clause_title, "line": i + 1, "via": "table",
            })
            continue

        for pm in PROSE.finditer(line):
            tag = pm.group(1).upper()
            name = clean(pm.group(2))
            if len(name) < 3:
                continue
            out.append({
                "doc": doc, "tag": tag, "name": name[:160],
                "length": "", "clause": clause,
                "clauseTitle": clause_title, "line": i + 1, "via": "prose",
            })

        for im in INTRODUCED.finditer(line):
            name = clean(im.group(1))
            tag = im.group(2).upper()
            if len(name) < 3:
                continue
            out.append({
                "doc": doc, "tag": tag, "name": name[:160],
                "length": "", "clause": clause,
                "clauseTitle": clause_title, "line": i + 1,
                "via": "introduced-by",
            })
    return out


def main():
    recs = []
    files = sorted(f for f in os.listdir(CORPUS) if f.endswith(".txt"))
    for f in files:
        recs.extend(parse_file(os.path.join(CORPUS, f)))

    # dedupe: (doc, tag) one representative, preferring a table-sourced name
    best = {}
    for r in recs:
        k = (r["doc"], r["tag"])
        if k not in best:
            best[k] = r
            continue
        prev = best[k]
        if prev["via"] == "prose" and r["via"] == "table":
            best[k] = r
        elif prev["via"] == r["via"] and len(r["name"]) > len(prev["name"]):
            best[k] = r

    rows = list(best.values())
    docs = {r["doc"] for r in rows}
    tags = {r["tag"] for r in rows}

    print(f"files parsed        : {len(files)}")
    print(f"raw records         : {len(recs)}")
    print(f"(document,tag) pairs: {len(rows)}")
    print(f"documents yielding  : {len(docs)}")
    print(f"distinct tags       : {len(tags)}")
    via = defaultdict(int)
    for r in rows:
        via[r["via"]] += 1
    print(f"by evidence         : {dict(via)}")

    print("\ntop documents:")
    per = defaultdict(set)
    for r in rows:
        per[r["doc"]].add(r["tag"])
    for d, t in sorted(per.items(), key=lambda kv: -len(kv[1]))[:12]:
        print(f"  {len(t):4d}  {d}")

    # regression set: the names that must come from the Card Spec, not borrowed
    print("\nregression (Card Spec definitions):")
    checks = {
        "E0": "Key Information Template",
        "E1": "Individual Key Information",
        "C0": "Key Information Data",
        "E3": "GlobalPlatform Registry related data",
        "4F": "Application AID",
        "5F20": "Application Provider identifier",
        "66": "Card Data",
        "67": "Card Capability Information",
    }
    ok = True
    cs_docs = [d for d in docs if d.startswith("GPC_SPE_034")]
    for tag, want in checks.items():
        found = [
            r["name"] for r in rows
            if r["tag"] == tag and r["doc"] in cs_docs
        ]
        hit = any(want.lower() in n.lower() for n in found)
        if not hit:
            ok = False
        print(f"  {tag:5s} {'OK ' if hit else 'FAIL'} {want}"
              + ("" if hit else f"   (got: {found[:2]})"))
    # C0 must never be the enumeration name
    bad = [r for r in rows if r["tag"] == "C0" and "empty" in r["name"].lower()]
    print(f"  C0 enumeration leak: {'CLEAN' if not bad else 'FAIL ' + str(len(bad))}")
    if bad:
        ok = False

    payload = {
        "namespace": "GlobalPlatform BER-TLV",
        "keying": "(document, tag)",
        "source": CORPUS,
        "documents": len(docs),
        "distinctTags": len(tags),
        "rows": rows,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1)
    print(f"\nwritten {OUT}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
