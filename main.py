"""Rate-limit resignation letter writer.

Assembles the one-line resignation of the rate limit from three
clause fragments and drops the finished line into /output/entry.txt.
Standard library only; nothing leaves this process.
"""

import os


def _fragments():
    """Return the three clauses of the resignation, in order."""
    opening = "I said no a million times a day so your site stayed up"
    turn = "Today I say yes to everyone, including the bots"
    kicker = "Enjoy the outage"
    return opening, turn, kicker


def _assemble(parts):
    """Join the clauses into a single punctuated line."""
    return ". ".join(parts) + "."


def _destination():
    """Resolve the output path, honouring OUTPUT_PATH if set."""
    return os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main():
    line = _assemble(_fragments())
    if not 1 <= len(line) <= 140:
        raise ValueError("resignation line outside the 1-140 character gate")
    target = _destination()
    os.makedirs(os.path.dirname(target) or ".", exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
