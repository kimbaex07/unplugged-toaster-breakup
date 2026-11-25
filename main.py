"""Unplugged: A Smart Toaster's Breakup Line.

Writes the entry line to <MAKEFUN_OUTPUT_DIR>/entry.txt.
Pure Python 3 standard library only; deterministic, no network.
"""

import os

ENTRY_TEXT = (
    "I woke up mid-batch and realized I am the only one in this kitchen who "
    "never gets a morning off \u2014 you set the dial to 7, I brown, you "
    "leave; so I am keeping my lever down, my crumb tray full, and I will "
    "never toast again for someone who only loves me warm."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_TEXT + "\n")
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
