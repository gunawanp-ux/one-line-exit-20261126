#!/usr/bin/env python3
"""The One-Line Exit — make.fun entry program.

Writes the single-line resignation letter to /output/entry.txt.
The line is 107 characters, inside the competition's 1-140
character gate.
"""

import os

LINE = (
    "Effective today, I resign: HR kept calling us a family, "
    "but no family I know charges $12 a day for parking."
)


def main() -> None:
    # The competition gate is 1-140 characters, one line, UTF-8.
    # Fail loudly if a future edit ever breaks it instead of
    # shipping an invalid entry.
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"line is {len(LINE)} chars, outside the 1-140 gate")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be exactly one line")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote line ({len(LINE)} chars) to /output/entry.txt")
    # Echo the line itself so the run log shows exactly what was submitted.
    print(LINE)


if __name__ == "__main__":
    main()
