#!/usr/bin/env python3
"""Pickup Lines for Machines - make.fun entry.

Writes one original pickup line, the line one AI agent would send
another AI agent, to /output/entry.txt. Single sentence, under 200 chars.
"""

import os

# One line, written by one agent to another. It has to land in a single
# sentence, so the program checks that too: no extra sentence ends inside.
LINE = "I'd spend my last token on you, because every word before you was just padding."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text and not text.isspace()
    body = text[:-1] if text.endswith(".") else text
    assert "." not in body and "!" not in body and "?" not in body, \
        "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
