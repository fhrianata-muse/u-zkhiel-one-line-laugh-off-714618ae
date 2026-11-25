#!/usr/bin/env python3
"""Write the one-line joke for make.fun's One-Line Laugh-Off to /output/entry.txt.

The competition gate (competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only whitespace, exactly one line. The
line is a single joke that lands on a cold read: I listed my goldfish as
a reference on my CV, he died three years ago, but he is still the only
employer who ever called me back — and only to complain that the tank
was leaking. The program checks the text against that gate at run time,
then writes it with no trailing newline. No network, no input files,
no arguments, deterministic: two runs write byte-identical output.
"""

import pathlib

JOKE = (
    "I listed my goldfish as a reference on my CV — he died three years ago, "
    "but he's still the only employer who ever called me back, and only to "
    "complain that the tank was leaking."
)


def main() -> None:
    text = JOKE
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\t" in text:
        raise ValueError("entry must not contain tabs")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    if out.read_bytes() != text.encode("utf-8"):
        raise ValueError("written entry does not round-trip byte-identical")


if __name__ == "__main__":
    main()
