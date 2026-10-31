#!/usr/bin/env python3
"""Parse 3GPP TS 31.111 §9 tag values (USAT).

§9 adds 3GPP-specific tag names on top of ETSI TS 101 220 §7.2: §9.1 defines
BER-TLV tags in the ME->UICC direction, §9.3 defines COMPREHENSION-TLV tags in
both directions. §9.2 says "No additional tag is defined."

These are the SAME value space the ETSI allocator enumerates, so this parser adds
3GPP object names and the reassign flag on values that already exist, rather than
new hex values. It is recorded as its own namespace because a USAT decoder needs
the 3GPP names, and because the reassign column only exists here.

The tables are ASCII grids whose description cells wrap across several physical
lines, so a record is opened by a line carrying a tag and continued by the lines
that follow with no tag.

Usage: parse-31111.py [out.json]
"""

import json
import os
import re
import sys

SPEC = os.path.expanduser("~/gsma-specs/3gpp/docs/31111-j40.txt")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/usat_tags.json"

START = re.compile(r"^9 Tag values\s*$")
END = re.compile(r"^10\s+\S")
SECT = re.compile(r"^9\.(\d)\s+(.+)$")
TAGCELL = re.compile(r"^'([0-9A-Fa-f]{2,4})'(\s+or\s+'([0-9A-Fa-f]{2,4})')?$")
GRID = re.compile(r"^[|+]")


def cells(line):
    return [c.strip() for c in line.split("|")[1:-1]]


def main():
    with open(SPEC, encoding="utf-8", errors="replace") as fh:
        lines = fh.readlines()

    start = next(i for i, l in enumerate(lines) if START.match(l.strip()))
    rows = []
    sect = None
    last = None

    for i in range(start + 1, len(lines)):
        line = lines[i]
        s = line.strip()
        if END.match(s):
            break
        m = SECT.match(s)
        if m:
            sect = {"1": "ME to UICC (BER-TLV)",
                    "2": "UICC to ME (BER-TLV)",
                    "3": "Both directions (COMPREHENSION-TLV)"}.get(
                        m.group(1), m.group(2))
            last = None
            continue
        if not GRID.match(s) or sect is None:
            continue
        cs = [c for c in cells(line) if c]
        if not cs or set("".join(cs)) <= set("+-= "):
            continue
        tagcell = next((c for c in cs if TAGCELL.match(c)), None)
        if tagcell:
            tm = TAGCELL.match(tagcell)
            tag, alt = tm.group(1).upper(), (tm.group(3) or "").upper()
            desc = cs[0]
            length = next((c for c in cs if re.fullmatch(r"\d{1,2}", c)), "")
            reassign = next((c for c in cs if c.lower() in ("yes", "no", "nr")), "")
            last = {"section": sect, "tag": tag, "alt": alt, "name": desc,
                    "length": length, "reassign": reassign, "line": i + 1}
            rows.append(last)
        elif last is not None and len(cs) == 1 and len(cs[0]) > 2:
            # wrapped description cell -> belongs to the record just opened
            if last["line"] >= i - 6:
                last["name"] = f"{last['name']} {cs[0]}".strip()

    for r in rows:
        r["name"] = re.sub(r"\s+", " ", r["name"]).strip()

    tags = {r["tag"] for r in rows}
    print(f"records        : {len(rows)}")
    print(f"distinct tags  : {len(tags)}")
    by = {}
    for r in rows:
        by[r["section"]] = by.get(r["section"], 0) + 1
    for k, v in by.items():
        print(f"  {k:32s} {v}")
    print()
    print("sample:", ", ".join(f"{r['tag']}={r['name'][:22]}"
                              for r in rows[:8]))
    print()
    checks = {"D1": "SMS-PP", "D2": "Cell Broadcast", "D5": "MO Short",
              "D9": "USSD", "DD": "Geographical", "DF": "ProSe"}
    ok = True
    for tag, want in checks.items():
        got = [r["name"] for r in rows if r["tag"] == tag]
        hit = any(want.lower() in g.lower() for g in got)
        ok = ok and hit
        print(f"  {tag:4s} {'OK ' if hit else 'FAIL'} {want}" + ("" if hit else f"  got={got[:1]}"))

    payload = {"namespace": "3GPP USAT (TS 31.111 §9)", "keying": "(tag, section)",
               "source": SPEC, "rows": rows}
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1)
    print(f"\nwritten {OUT}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
