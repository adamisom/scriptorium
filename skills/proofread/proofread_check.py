#!/usr/bin/env python3
"""
proofread_check.py — deterministic mechanical sweep for the Corrector skill.

A crude, instant, local stand-in for a rule-based grammar checker (e.g.
LanguageTool). It flags *candidates only* — doubled words, multiple spaces,
space-before-punctuation, and doubled punctuation. Every candidate is meant to be
adjudicated downstream by the skeptical verifier; expect some false positives that
the verifier will (correctly) reject.

Usage:
    python proofread_check.py INPUT.txt [-o findings_mechanical.csv]
    python proofread_check.py INPUT.txt            # CSV to stdout

Notes:
- Operates on the raw text as-is. If the input is a PDF->text extraction, some hits
  will be artifacts (e.g. doubled words across a page-number line); that's fine —
  the verifier reads context and rejects them.
- Line numbers are 1-based and computed from byte offsets so they survive reflow.
"""

import argparse
import csv
import re
import sys

# Doubled words that are frequently legitimate in English. We still surface them
# (precision is the verifier's job, not ours) but tag them so the verifier knows
# to scrutinize rather than assume. Edit freely.
COMMON_LEGIT_DOUBLES = {"had", "that", "is", "the", "a"}  # heuristic only

# A doubled word: same alphabetic token repeated with whitespace between, case-
# insensitive. \w would catch "10 10"; restrict to alphabetic to cut numeric noise.
DOUBLED_WORD = re.compile(r"\b([A-Za-z]+)(\s+)(\1)\b", re.IGNORECASE)
MULTI_SPACE = re.compile(r"[^\S\n]{2,}")          # 2+ spaces/tabs, not newlines
SPACE_BEFORE_PUNCT = re.compile(r"\s+([,.;:!?])")
# Doubled punctuation: 2+ of , ; : ! ?  OR exactly two dots not part of an ellipsis.
DOUBLED_PUNCT = re.compile(r"([,;:!?])\1+|(?<!\.)\.\.(?!\.)")


def line_of(offset, line_starts):
    """1-based line number for a byte offset, via bisect over line-start offsets."""
    import bisect
    return bisect.bisect_right(line_starts, offset)


def snippet(text, start, end, pad=24):
    lo = max(0, start - pad)
    hi = min(len(text), end + pad)
    s = text[lo:hi].replace("\n", " ").strip()
    return re.sub(r"\s{2,}", " ", s)


def main():
    ap = argparse.ArgumentParser(description="Mechanical proofreading sweep.")
    ap.add_argument("input", help="path to a UTF-8 text file")
    ap.add_argument("-o", "--out", help="CSV output path (default: stdout)")
    args = ap.parse_args()

    with open(args.input, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()

    # Offsets at which each line begins, for fast line-number lookup.
    line_starts = [0]
    for m in re.finditer(r"\n", text):
        line_starts.append(m.end())

    rows = []

    for m in DOUBLED_WORD.finditer(text):
        word = m.group(1).lower()
        note = "common-legit double; scrutinize" if word in COMMON_LEGIT_DOUBLES \
            else "adjacent duplicate token"
        rows.append((m.start(), "doubled-word",
                     re.sub(r"\s+", " ", m.group(0)).strip(),
                     m.group(1), note))

    for m in SPACE_BEFORE_PUNCT.finditer(text):
        rows.append((m.start(), "space-before-punct", snippet(text, m.start(), m.end()),
                     m.group(1), "whitespace before punctuation"))

    for m in DOUBLED_PUNCT.finditer(text):
        rows.append((m.start(), "doubled-punct", m.group(0),
                     "", "repeated punctuation (ellipsis excluded)"))

    for m in MULTI_SPACE.finditer(text):
        rows.append((m.start(), "multi-space", "[%d spaces]" % (m.end() - m.start()),
                     " ", "collapse to a single space"))

    rows.sort(key=lambda r: r[0])

    out = open(args.out, "w", newline="", encoding="utf-8") if args.out else sys.stdout
    w = csv.writer(out)
    w.writerow(["#", "line", "type", "match", "suggested_fix_hint", "note"])
    for i, (off, typ, match, fix, note) in enumerate(rows, 1):
        w.writerow([i, line_of(off, line_starts), typ, match, fix, note])
    if args.out:
        out.close()
        print("wrote %d candidate(s) to %s" % (len(rows), args.out), file=sys.stderr)


if __name__ == "__main__":
    main()
