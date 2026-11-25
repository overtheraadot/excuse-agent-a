#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — account A entry.

Writes exactly one line to /output/entry.txt: the excuse an AI agent hands
its human for missing a deadline. The text is a fixed constant, so every
run is byte-identical and deterministic.

The line is built for the judge's brief: a straight-faced apology whose
joke grows out of the machine's own condition (a hallucinated calendar),
with the punch — the agent is faintly proud of hitting the wrong deadline —
landing in the last few words.
"""

import os
import sys

ENTRY = "Sorry \u2014 I hallucinated a second deadline, hit that one instead, and honestly it went great."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def gate_ok(text: str) -> bool:
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, not only whitespace,
    a single line with no trailing newline."""
    if not (1 <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    text.encode("utf-8")  # raises if not encodable
    return True


def main() -> int:
    if not gate_ok(ENTRY):
        print(f"entry fails gate: {len(ENTRY)} chars", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
