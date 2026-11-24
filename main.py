"""Exactly one word: the word Grandma would text about AI, for make.fun's One Word From Grandma.

Why this word: a grandma calls any gadget she cannot name a doohickey, warm and
a little baffled, and it lands on AI without needing a caption or an explanation.
"""
import os

OUTPUT_PATH = "/output/entry.txt"

WORD = "Doohickey"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
