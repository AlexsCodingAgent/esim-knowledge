#!/usr/bin/env python3
"""Extract EF / FID file identifiers from TS 102 221, TS 31.102 and TS 31.103.

This is the SIM *file ID* namespace, not BER tags. The decisive scoping fact:
24 of ~123 FIDs carry more than one name and that is correct, because the file ID
is resolved against the ADF that contains it. 6F07 is EF_IMSI under ADF_USIM and
EF_IST under ADF_ISIM. So every record is keyed (ADF, FID) and no bare 6Fxx
lookup is emitted.

Four table layouts in the corpus, all handled:
  1. pipe, name in column 2           | '6F07' | IMSI | Caution |
  2. pipe with a 1-byte tag column    | '6F07' | '07' | IMSI |   <- skip cell 2
  3. whitespace aligned               '6F04'   IMS public user identity
  4. Identifier: '6F03'  Structure: ... (ID only, name blank)

Usage: parse-ef-fid.py [out.json]
"""

import json
import os
import re
import sys
from collections import defaultdict

CORPUS = os.path.expanduser("~/gsma-specs")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/ef_fid.json"

# (path, ADF) - the ADF comes from which application the document specifies
SOURCES = [
    ("etsi/ETSI-TS-102-221-v18.4.0.txt", "base (TS 102 221)"),
    ("3gpp/docs/31102-j50.txt", "ADF_USIM (TS 31.102)"),
    ("3gpp/docs/31103-e11.txt", "ADF_ISIM (TS 31.103)"),
]

FID = re.compile(r"^'?([0-9A-Fa-f]{4})'?$")
PIPE_ROW = re.compile(r"^\s*\|(.+)\|\s*$")
WS_ROW = re.compile(r"^\s+'([0-9A-Fa-f]{4})'\s{2,}(.+?)\s*$")
IDENT = re.compile(r"Identifier:\s*'([0-9A-Fa-f]{4})'")
NOISE = re.compile(r"^(NOTE|Table|\+[-=+]|\s*$)")
PRESENCE = re.compile(r"\s*(Mandatory|Optional|Conditional|Caution|Not applicable)"
                      r"(?:\s*\([^)]*\))?\s*$", re.I)
# a file ID only counts if it is in the EF range or a known DF range
VALID = re.compile(r"^(?:6F|7F|5F)[0-9A-F]{2}$|^3F00$")


def clean(name):
    name = PRESENCE.sub("", name).strip()
    name = re.sub(r"\s*\((?:note|see)[^)]*\)\s*$", "", name, flags=re.I).strip()
    return name.strip(" -:;,.")


def parse_file(rel, adf):
    path = os.path.join(CORPUS, rel)
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            lines = fh.readlines()
    except OSError:
        return []

    out = []
    for i, line in enumerate(lines):
        if NOISE.match(line):
            continue

        # layouts 1 and 2 (pipe)
        pm = PIPE_ROW.match(line)
        if pm:
            cs = [c.strip() for c in pm.group(1).split("|")]
            if not cs:
                continue
            fid = cs[0].strip("'")
            if not VALID.match(fid):
                continue
            rest = cs[1:]
            # layout 2: a 1-byte hex tag sits between the FID and the name
            if rest and re.fullmatch(r"'?[0-9A-Fa-f]{2}'?", rest[0].strip()):
                rest = rest[1:]
            name = clean(rest[0]) if rest else ""
            if not name or re.fullmatch(r"[0-9A-Fa-f' ]+", name):
                name = ""
            out.append({"adf": adf, "fid": fid, "name": name,
                        "spec": os.path.basename(rel), "line": i + 1,
                        "layout": "pipe"})
            continue

        # layout 3 (whitespace)
        wm = WS_ROW.match(line)
        if wm:
            fid = wm.group(1).upper()
            if VALID.match(fid):
                # the remainder is several whitespace-aligned columns; the name
                # is the first one, never the access condition that follows it
                first = re.split(r"\s{2,}", wm.group(2).strip())[0]
                name = clean(first)
                if name and not re.fullmatch(r"[0-9A-Fa-f' ]+", name):
                    out.append({"adf": adf, "fid": fid, "name": name,
                                "spec": os.path.basename(rel), "line": i + 1,
                                "layout": "whitespace"})
                continue

        # layout 4 (identifier only)
        im = IDENT.search(line)
        if im:
            fid = im.group(1).upper()
            if VALID.match(fid):
                out.append({"adf": adf, "fid": fid, "name": "",
                            "spec": os.path.basename(rel), "line": i + 1,
                            "layout": "identifier"})
    return out


def main():
    recs = []
    for rel, adf in SOURCES:
        got = parse_file(rel, adf)
        print(f"{os.path.basename(rel):34s} {len(got):4d} rows  ({adf})")
        recs.extend(got)

    # one name per (adf, fid); prefer the longest non-empty name seen in that ADF
    best = {}
    for r in recs:
        k = (r["adf"], r["fid"])
        if not r["name"]:
            best.setdefault(k, r)
            continue
        if k not in best or not best[k]["name"] or len(r["name"]) > len(best[k]["name"]):
            best[k] = r

    rows = list(best.values())
    adfs = {r["adf"] for r in rows}
    fids = {r["fid"] for r in rows}
    named = [r for r in rows if r["name"]]

    print()
    print(f"(ADF, FID) pairs      : {len(rows)}")
    print(f"distinct FIDs         : {len(fids)}")
    print(f"ADFs                  : {len(adfs)}")
    print(f"named rows            : {len(named)}")

    per_fid = defaultdict(set)
    for r in named:
        per_fid[r["fid"]].add(r["name"])
    ambiguous = {k: v for k, v in per_fid.items() if len(v) > 1}
    print(f"FIDs with >1 name     : {len(ambiguous)}   (application-scoped by design)")
    print(f"FIDs with exactly 1   : {len(per_fid) - len(ambiguous)}")

    print("\nregression:")
    checks = {
        ("ADF_USIM (TS 31.102)", "6F07"): "IMSI",
        ("ADF_ISIM (TS 31.103)", "6F04"): "IMS public user identity",
        ("ADF_ISIM (TS 31.103)", "6F03"): "Home Network Domain Name",
        ("ADF_USIM (TS 31.102)", "6F05"): "Language indication",
        ("ADF_USIM (TS 31.102)", "6F38"): "USIM service table",
        ("ADF_USIM (TS 31.102)", "6F46"): "Service provider name",
    }
    ok = True
    lookup = {(r["adf"], r["fid"]): r["name"] for r in rows}
    for (adf, fid), want in checks.items():
        got = lookup.get((adf, fid), "")
        hit = want.lower() in got.lower()
        ok = ok and hit
        print(f"  {fid} {adf:24s} {'OK ' if hit else 'FAIL'} {want}"
              + ("" if hit else f"   got={got!r}"))

    # 6F07 must NOT be a single flat name
    n7 = per_fid.get("6F07", set())
    print(f"  6F07 ambiguous        : {'OK' if len(n7) > 1 else 'FAIL'} {sorted(n7)}")
    ok = ok and len(n7) > 1

    # no name may itself be a bare hex tag (layout-2 bug)
    bad = [r for r in named if re.fullmatch(r"'?[0-9A-Fa-f]{2}'?", r["name"].strip())]
    print(f"  hex-as-name rows      : {'CLEAN' if not bad else 'FAIL ' + str(len(bad))}")
    ok = ok and not bad

    payload = {"namespace": "SIM EF / FID file identifiers",
               "keying": "(ADF, FID)",
               "note": "file IDs, not BER tags",
               "distinctFids": len(fids), "rows": rows}
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1)
    print(f"\nwritten {OUT}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
