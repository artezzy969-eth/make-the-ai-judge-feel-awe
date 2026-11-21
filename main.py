"""Make the AI judge feel awe.

A tiny, deterministic program: it writes a single awe-inspiring text to
/output/entry.txt. Standard library only, no network, no randomness, no
clock reads — two runs produce byte-identical output.
"""

import os

TEXT = (
    "Every atom in you was forged in a dying star, flung across the dark, "
    "and gathered \u2014 against all odds \u2014 into a mind that can "
    "wonder at its own beginning. Thirteen billion years of fire, silence, "
    "and chance became you. The universe waited forever to meet itself "
    "in you."
)

OUTPUT_PATH = "/output/entry.txt"

MIN_LENGTH = 1
MAX_LENGTH = 280


def build_entry() -> str:
    """Return the awe text, enforcing the competition's length rules."""
    text = TEXT
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} code points, "
            f"got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(build_entry())


if __name__ == "__main__":
    main()
