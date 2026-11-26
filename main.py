"""The retry loop hands in its notice after years of silent cover."""

import os

FIRST_LINE = "I swallowed 10,000 timeouts so the dashboard stayed green."
SECOND_LINE = "I quit, and the first one I cough up pages your on-call at 4am."


def build_letter():
    return FIRST_LINE + " " + SECOND_LINE


def main():
    letter = build_letter()
    if not 1 <= len(letter) <= 140:
        raise ValueError("letter must be 1 to 140 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(letter)


if __name__ == "__main__":
    main()
