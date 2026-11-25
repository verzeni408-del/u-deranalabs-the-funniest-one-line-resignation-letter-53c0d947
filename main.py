"""One-line resignation letter from the cron job nobody ever checked on.

Writes a single line to /output/entry.txt.
"""

import os


def compose_letter():
    parts = (
        "I fired every minute since March and ",
        "you never once checked on me. I quit. ",
        "Your backups stopped with me.",
    )
    return "".join(parts)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(compose_letter())


if __name__ == "__main__":
    main()
