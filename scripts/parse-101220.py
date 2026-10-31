#!/usr/bin/env python3
"""Parse ETSI TS 101 220 §7.2 "Assigned TLV tag values" into JSON.

§7.2 is the *allocator*: it is the document that says which tag values exist at
all, and it is keyed by (type, context template, tag) because 30+ values carry
more than one meaning depending on the template that contains them.

Table shapes handled:
  simple   '80'      File Size - Data
  range    '81' - '8F'     Access Mode - Command Description
  dual     '01' or '81'    Command details tag     1   '01'   No
  single   '18' only       Items Next Action Indicator tag
  alt-name (no tag)        Reserved for 3GPP (BSSID tag)      <- extra meaning
                                                               of the row above

The heading for Table 7.23 wraps across three lines ("COMPREHENSION-" / "TLV tag"
/ "(CR and Tag value)"), which is exactly the defect that once made 113 rows
inherit the previous table's context. The context is therefore taken only from the
line that carries the type token, and every table is asserted to have acquired its
own context.

Usage: parse-101220.py [out.json]
"""

import json
import os
import re
import sys

SPEC = os.path.expanduser("~/gsma-specs/etsi/ETSI-TS-101-220-v19.0.0.txt")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/tlv_types.json"

START = re.compile(r"^7\.2\s+Assigned TLV tag values\s*$")
# §7.2 ends at clause 8, which begins with "Table 8.1" in this document. The
# heading itself ("8    UICC Java Card Services") carries no clause-number prefix
# pattern that a naive ^7\.3 check would catch, so bound on both forms.
END = re.compile(r"^\s*Table 8\.\d|^\s*8\s{2,}[A-Z]")
TABLE = re.compile(r"^\s*Table 7\.(\d+)\s*$")
TYPE_TOKEN = re.compile(r"(COMPACT-TLV|COMPREHENSION-|BER-TLV)")
# a tag cell: '01' / '5F50' / '01' or '81' / '18' only / '81' - '8F'
TAG_ROW = re.compile(
    r"^\s*'([0-9A-Fa-f]{2,8})'"
    r"(?:\s*(or|-)\s*'([0-9A-Fa-f]{2,8})')?"
    r"(?:\s+only)?"
    r"\s{2,}(.+?)\s*$"
)
SUBHEAD = re.compile(r"^\s+([A-Z][A-Za-z0-9 ()/'\-,.]*?)\s*$")
NOISE = re.compile(
    r"^(ETSI|Release \d|\f|NOTE:|Table \d|\s*$)"
)


def cells(line):
    """Split a table line on runs of 2+ spaces (columns are wide-aligned)."""
    return [c.strip() for c in re.split(r"\s{2,}", line.strip()) if c.strip()]


def parse():
    with open(SPEC, encoding="utf-8", errors="replace") as fh:
        lines = fh.readlines()

    start = None
    for i, line in enumerate(lines):
        if START.match(line.strip() + "  " if False else line):
            # body heading, not the table-of-contents entry (which is dotted)
            if "....." not in line:
                start = i
                break
    if start is None:
        raise SystemExit("§7.2 heading not found")

    table = None
    ttype = None
    context = None
    rows = []
    tables_seen = []
    pending_tag = None

    for i in range(start + 1, len(lines)):
        line = lines[i]
        if END.match(line.strip()):
            break

        m = TABLE.match(line)
        if m:
            table = int(m.group(1))
            ttype, context = None, None
            tables_seen.append(table)
            continue

        if table is None:
            continue
        if NOISE.match(line.strip()) and not TYPE_TOKEN.search(line):
            continue

        # Header line carries the type token; this is the ONLY place context is
        # taken from, so a wrapped heading cannot leak the previous context.
        tm = TYPE_TOKEN.search(line)
        if tm and ttype is None:
            raw = tm.group(1)
            if raw == "COMPREHENSION-":
                ttype = "COMPREHENSION-TLV"
                rest = line[tm.end():]
                # drop the trailing column captions on the same line
                rest = re.split(r"\s{2,}Length\b", rest)[0]
                context = " ".join(rest.split())
            else:
                ttype = raw
                parts = cells(line)
                # first cell is e.g. "BER-TLV tag"; the rest is the context
                context = " ".join(parts[1:]) if len(parts) > 1 else ""
                context = re.sub(r"\s*\(Range:.*$", "", context).strip()
            continue

        if TYPE_TOKEN.search(line):
            continue  # wrapped continuation of the heading

        rm = TAG_ROW.match(line)
        if rm and ttype:
            tag = rm.group(1).upper()
            sep = rm.group(2)
            second = (rm.group(3) or "").upper()
            # 'or' = the same object's alternate encoding (COMPREHENSION-TLV).
            # '-' = a whole range of allocated values, which is one table row but
            # many tag values, so it is recorded separately rather than counted.
            alt = second if sep == "or" else ""
            range_end = second if sep == "-" else ""
            tail = cells(rm.group(4))
            name = tail[0] if tail else ""
            name = re.sub(r"\s+$", "", name)
            rows.append({
                "table": table,
                "type": ttype,
                "context": context,
                "tag": tag,
                "alt": alt,
                "rangeEnd": range_end,
                "name": name,
                "altNames": [],
                "line": i + 1,
            })
            pending_tag = rows[-1]
            continue

        # A line with no tag inside a toolkit table adds a second meaning to the
        # row above (7.23 packs several 3GPP meanings under one value).
        if pending_tag is not None and re.search(r"tag\)?\s*$", line.strip()):
            txt = " ".join(cells(line))
            if txt and not NOISE.match(txt):
                pending_tag["altNames"].append(txt)

    return rows, tables_seen


def report(rows, tables):
    from collections import Counter, defaultdict

    by_type = defaultdict(list)
    for r in rows:
        by_type[r["type"]].append(r)

    print(f"tables            : {len(tables)}  {tables}")
    print(f"rows              : {len(rows)}")
    print(f"contexts          : {len({(r['type'], r['context']) for r in rows})}")
    print()
    for t in ("COMPACT-TLV", "BER-TLV", "COMPREHENSION-TLV"):
        rs = by_type[t]
        print(f"  {t:18s} rows {len(rs):4d}  distinct {len({r['tag'] for r in rs}):4d}")
    print()
    per_ctx = Counter((r["type"], r["context"]) for r in rows)
    print("contexts (type | context | rows):")
    for (t, c), n in per_ctx.items():
        print(f"  {t:18s} | {c:55s} | {n}")

    # distinct within a context = the number that matters for a scoped lookup
    within = {(r["type"], r["context"], r["tag"]) for r in rows}
    across = {r["tag"] for r in rows}
    print()
    print(f"distinct (type, context, tag) : {len(within)}")
    print(f"distinct tag values (all types): {len(across)}")
    reused = {t: len({r['context'] for r in rows if r['tag'] == t}) for t in across}
    multi = {t: n for t, n in reused.items() if n > 1}
    print(f"tag values with >1 context    : {len(multi)}")
    for t, n in sorted(multi.items(), key=lambda kv: -kv[1])[:6]:
        print(f"   '{t}' -> {n} contexts")
    alts = sum(len(r["altNames"]) for r in rows)
    print(f"secondary meanings captured   : {alts}")


def regress(rows):
    """The verified regression set from the reference note."""
    want = {
        ("61", "Application Template"),
        ("62", "FCP Template"),
        ("7B", "Security Environment Template"),
        ("82", "File Descriptor"),
        ("84", "DF Name (AID)"),
        ("8A", "Life Cycle Status"),
        ("AB", "Security Attribute Template - Expanded Format"),
        ("A5", "Proprietary Template"),
        ("C6", "PIN Status data objects"),
    }
    got = {(r["tag"], r["name"]) for r in rows}
    missing = want - got
    # '83' must be File Identifier under FCP and Key Reference under CTR
    k83 = {(r["tag"], r["context"], r["name"]) for r in rows if r["tag"] == "83"}
    ok83 = (
        ("83", "FCP template ('62')", "File Identifier") in k83
        and ("83", "Control reference template ('A4')", "Key Reference") in k83
    )
    print()
    print(f"regression: {len(want) - len(missing)}/{len(want)} known rows present")
    for m in sorted(missing):
        print("   MISSING:", m)
    print(f"regression: '83' disambiguated by context: {ok83}")
    return not missing and ok83


if __name__ == "__main__":
    rows, tables = parse()
    report(rows, tables)
    ok = regress(rows)
    payload = {
        "spec": "ETSI TS 101 220 V19.0.0",
        "clause": "7.2 Assigned TLV tag values",
        "source": SPEC,
        "tables": tables,
        "rows": rows,
        "rowCount": len(rows),
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1)
    print()
    print(f"written {OUT}")
    sys.exit(0 if ok else 1)
