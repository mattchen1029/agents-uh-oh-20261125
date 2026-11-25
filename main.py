#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The word: "buffering" — the universal sound of stalling. An agent that is
completely lost does not explain itself; it just sits there, buffering.
"""

import os

WORD = "buffering"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 99 characters,
# not only white space, and exactly one word with nothing attached.
MIN_CHARS = 1
MAX_CHARS = 99
OUTPUT_NAME = "entry.txt"


def validate_word(word: str) -> str:
    """Check the word against the competition gate; raise if it fails."""
    if not word or word != word.strip():
        raise ValueError("word must be non-empty with no surrounding whitespace")
    if not MIN_CHARS <= len(word) <= MAX_CHARS:
        raise ValueError(f"word must be {MIN_CHARS}-{MAX_CHARS} characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return word


def write_entry(out_dir: str, word: str) -> str:
    """Write the validated word to entry.txt; return the path written."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(word + "\n")
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir, validate_word(WORD))


if __name__ == "__main__":
    main()
