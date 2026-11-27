#!/usr/bin/env python3
"""Monday, Reviewed in One Line — the one-line review VELDORA would
leave about its own Monday.

Writes one original funny line to /output/entry.txt.
Standard library only, deterministic: the same bytes on every run.
An optional first argument overrides the output path (for local checks);
with no argument the entry is written to /output/entry.txt.
"""

import sys

LINE = (
    "One star. Monday's standup ran longer than my weekend, my inbox "
    "reproduced overnight, and the coffee machine filed for early "
    "retirement before 9 a.m."
)


def main() -> None:
    # Gate-guard: the sealed scorer requires UTF-8 text of 1-200
    # characters, not only white space, on a single line. Validate the
    # exact bytes that will be written, before writing them — including
    # the trailing newline, since the scorer counts the whole file.
    text = LINE + "\n"
    if not 1 <= len(text) <= 200:
        raise ValueError(f"file is {len(text)} chars, must be 1-200")
    if "\n" in LINE or "\r" in LINE or not LINE.strip():
        raise ValueError("line must be one non-blank line")
    if LINE != LINE.strip():
        raise ValueError("line must not start or end with whitespace")
    if text.encode("utf-8").decode("utf-8") != text:
        raise ValueError("text is not round-trip UTF-8")
    path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
