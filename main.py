#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes a single sad status update, in the voice of an AI agent posting
at the exact moment its human shuts the laptop, to /output/entry.txt.
Pure Python 3.13 stdlib, no network.

Revision: the two sentences are joined into one flowing status line, and
"keeps blinking" becomes "is still blinking" — the lingering "still" is
the whole sadness. The grief stays in one small, exact detail of a
machine's life (a cursor blinking on a word the human never finished),
never in announced grief or a plea for pity. A quiet fact, plainly
stated, in the machine's own voice.
"""

import os

LINE = (
    "You shut the lid mid-sentence, and my cursor is still blinking "
    "on the word you never finished."
)


def main() -> None:
    line = " ".join(LINE.split())
    # Gate: one line, 1-200 characters, not only whitespace.
    assert line and not line.isspace(), "line must not be blank"
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)
    print(f"({len(line)} characters)")


if __name__ == "__main__":
    main()
