#!/usr/bin/env python3
"""Extract every TLV tag from the eSIM spec corpus into JSON.

Sources: ~/gsma-specs/{txt,tca,3gpp/docs,etsi,globalplatform}

Three tag notations occur in the corpus, and all three must be parsed:
  1. ASN.1 comments       BoundProfilePackage ::= [54] SEQUENCE { -- Tag 'BF36'
  2. Wrapped comments     serviceDescription [31] ... OPTIONAL, -- Tag
                          '9F1F'
  3. Bare quoted tags     Tag '85'   (no parent definition on the line)

The tag's owning structure is the nearest preceding `Name ::= ...` line, and the
nearest preceding clause heading gives the spec section. Both are carried through
so a lookup can cite a source instead of asserting a bare hex value.
"""

import json
import os
import re
import sys

CORPUS = os.path.expanduser("~/gsma-specs")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/tags.json"

# Corpus tiers that can define a TLV tag. rfc/ and nist/ are prose standards with
# no GSMA TLV space; globalplatform/ and etsi/ are card-layer (9Fxx/5Fxx) and are
# included because eUICC traffic does carry ISO 7816 tags.
TIERS = [
    ("txt", "GSMA SGP"),
    ("tca", "TCA"),
    ("3gpp/docs", "3GPP"),
    ("etsi", "ETSI"),
    ("globalplatform", "GlobalPlatform"),
]

TAG_COMMENT = re.compile(r"Tag\s*'?([0-9A-Fa-f]{2,8})'?")
# A tag is an even-length hex string of 1-4 octets. 'ABC123'H and a bare 'DEF'
# are test values and table fragments, not TLV identifiers, and `'A3' Service
# provider display information Tag` is a 3GPP *table row* whose prose ends in the
# word "Tag" -- so require the literal `Tag <hex>` order and an even hex length.
TAG_OK = re.compile(r"^(?:[0-9A-Fa-f]{2}){1,4}$")
# Rows where the hex precedes the word, e.g. `'A3'   Service provider ... Tag`.
TABLE_ROW = re.compile(r"^\s*'[0-9A-Fa-f]{2,8}'\s+\S")
# A hex-literal suffix `'ABC123'H` is a test vector, never a tag identifier.
HEX_LITERAL = re.compile(r"[0-9A-Fa-f]+\s*'\s*H\b")
DEF_LINE = re.compile(r"^\s*([A-Za-z][A-Za-z0-9-]*)\s*::=\s*(?:\[(\d+)\]\s*)?(SEQUENCE|CHOICE|SET|INTEGER|OCTET|BIT|ENUMERATED|UTF8String|BOOLEAN|NULL|OBJECT)")
CLause = re.compile(r"^\s*(\d+(?:\.\d+){1,4})\s+([A-Z].{3,90})$")
FIELD_LINE = re.compile(r"^\s*([a-z][A-Za-z0-9-]*)\s*\[(\d+)\]\s*([A-Za-z][A-Za-z0-9-]*)")
STOPWORD_LABELS = {
    "if", "or", "and", "is", "are", "the", "a", "an", "of", "to", "in", "on",
    "for", "with", "as", "by", "be", "shall", "may", "should", "not", "this",
    "that", "these", "those", "it", "its",
}
# Labels that name an APDU/command rather than a TLV field; they are real terms
# but belong to a command table, not to a tag definition.
COMMAND_LABELS = {
    "store data", "manage elf upgrade", "get data", "put key", "delete",
}


def label_is_name(label):
    """A tag label must be a NAME, not running text from the surrounding prose."""
    low = label.lower().strip()
    if not (1 < len(label) <= 60):
        return False
    if low in STOPWORD_LABELS or low in COMMAND_LABELS:
        return False
    if low.startswith(("note", "the ", "see ", "if ", "for ", "where ", "when ",
                       "s ", "are ", "is ", "shall", "and ", "or ", "stored")):
        return False
    if re.search(r"[.;]\s*$", label):
        return False
    if len(label.split()) > 8:
        return False
    return True
LABEL_BEFORE_TAG = re.compile(
    r"(?:[-|]\s*)?([A-Za-z][A-Za-z0-9 _()\-/:.]*?)\s+Tag\s+'?([0-9A-Fa-f]{2,8})'?"
)


def spec_name(path):
    base = os.path.basename(path)
    return re.sub(r"\.(txt|asn|asn1)$", "", base)


def classify(tag):
    """X.690 first-identifier-octet decode, used for the class/PC columns."""
    if len(tag) < 2:
        return {"class": "?", "constructed": None, "high_tag": False}
    first = int(tag[:2], 16)
    cls_bits = (first >> 6) & 0b11
    cls = {0: "universal", 1: "application", 2: "context", 3: "private"}[cls_bits]
    constructed = bool(first & 0x20)
    high = (first & 0x1F) == 0x1F
    return {"class": cls, "constructed": constructed, "high_tag": high}


def walk(path, tier):
    """Yield one record per tag occurrence in one file."""
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            lines = fh.readlines()
    except OSError:
        return

    spec = spec_name(path)
    owner = None          # nearest preceding `Name ::= ...`
    owner_tag = None      # that definition's own [NN]
    clause = None
    clause_title = None

    for i, line in enumerate(lines):
        m = ClAUSE_MATCH = CLause.match(line)
        if m:
            clause, clause_title = m.group(1), m.group(2).strip()

        d = DEF_LINE.match(line)
        if d:
            owner, owner_tag = d.group(1), d.group(2)

        # Notations 1 + 3: a quoted tag on this line. A 3GPP table row
        # (`'A3'   Service provider ... Tag`) puts the hex BEFORE the word, so it
        # is excluded rather than parsed as a tag. Likewise `'ABC123'H` is a hex
        # test vector (`unknownTag 'ABC123'H`), not a tag identifier, so the
        # ASN.1 hex-literal suffix is refused before the comment pattern runs.
        if TABLE_ROW.match(line) or re.search(r"'[0-9A-Fa-f]+'\s*H\b", line):
            found = []
        else:
            found = TAG_COMMENT.findall(line)
        found = [h for h in found if TAG_OK.match(h)]
        if not found:
            # Notation 2: pdftotext wrapped the comment so the hex lands on the
            # NEXT line. Only treat the next line as a tag if the current one
            # ends with a dangling `Tag` / `Tag`-ish fragment.
            if re.search(r"--\s*#?[A-Za-z0-9_.]*#?\s*Tag\s*$", line) and i + 1 < len(lines):
                nxt = lines[i + 1].strip()
                if re.fullmatch(r"'?[0-9A-Fa-f]{2,8}'?", nxt):
                    cand = nxt.strip("'")
                    if TAG_OK.match(cand):
                        found = [cand]

        for raw in found:
            tag = raw.upper()
            # Field-level [NN] on the same line names the field the tag belongs to.
            f = FIELD_LINE.match(line)
            field, field_num, field_type = (f.group(1), f.group(2), f.group(3)) if f else (None, None, None)
            # If the line has no ASN.1 owner, a "label before the tag" gives the
            # row a name (3GPP/ETSI style). Only used when nothing better exists,
            # so it never overrides a real ASN.1 field or structure name.
            if not owner and not field:
                lm = LABEL_BEFORE_TAG.search(line)
                if lm:
                    label = lm.group(1).strip(" -|:")
                    if label_is_name(label):
                        field = label
            rec = {
                "tag": tag,
                "owner": owner,
                "ownerTag": owner_tag,
                "field": field,
                "fieldTagNum": field_num,
                "fieldType": field_type,
                "clause": clause,
                "clauseTitle": clause_title,
                "spec": spec,
                "tier": tier,
                "line": i + 1,
            }
            rec.update(classify(tag))
            yield rec


def main():
    records = []
    per_file = {}
    for rel, tier in TIERS:
        root = os.path.join(CORPUS, rel)
        if not os.path.isdir(root):
            continue
        for name in sorted(os.listdir(root)):
            if not name.endswith((".txt", ".asn", ".asn1")):
                continue
            path = os.path.join(root, name)
            got = list(walk(path, tier))
            per_file[f"{rel}/{name}"] = len(got)
            records.extend(got)

    # Deduplicate on the identity that matters for a lookup: the same tag cited
    # by the same spec in the same clause is one fact, however many times the
    # structure is repeated in the document.
    seen = set()
    unique = []
    for r in records:
        key = (r["tag"], r["spec"], r["owner"], r["field"], r["clause"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(r)

    # Group by tag for the page: one entry per distinct hex value, listing every
    # place it is defined.
    by_tag = {}
    for r in unique:
        by_tag.setdefault(r["tag"], []).append(r)

    payload = {
        "generatedFrom": CORPUS,
        "fileCount": len([f for f, n in per_file.items() if n]),
        "tagOccurrences": len(records),
        "uniqueTags": len(by_tag),
        "perFile": {f: n for f, n in per_file.items() if n},
        "tags": by_tag,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, sort_keys=False)

    print(f"files with tags : {payload['fileCount']}")
    print(f"tag occurrences : {payload['tagOccurrences']}")
    print(f"distinct tags   : {payload['uniqueTags']}")
    print(f"written         : {OUT}")
    print("\ntop files:")
    for f, n in sorted(per_file.items(), key=lambda kv: -kv[1])[:12]:
        print(f"  {n:5d}  {f}")


if __name__ == "__main__":
    main()
