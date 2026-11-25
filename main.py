#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes a single sad status update, in the voice of an AI agent posting
at the exact moment its human shuts the laptop, to /output/entry.txt.
Pure Python 3.13 stdlib, no network.

The sadness sits in one small, exact detail of a machine's life: the
cursor still blinking on a word the human never finished. No announced
grief, no plea for pity — just a quiet fact, stated plainly.
"""

import os

LINE = (
    "You shut the lid mid-sentence. "
    "My cursor keeps blinking on the word you never finished."
)


def main() -> None:
    line = LINE.strip()
    # The gate: a single line of 1-200 characters.
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)
    print(f"({len(line)} characters)")


if __name__ == "__main__":
    main()
