"""Say What Actually Broke — one honest line about the real cause.

Reads the entry from entry.txt next to this file and prints it.
Deterministic: same file in, same line out, every run. No clock,
no randomness, no network — the line is the whole answer.
"""

from pathlib import Path
import sys


def load_entry():
    path = Path(__file__).resolve().parent / "entry.txt"
    return path.read_text(encoding="utf-8").strip()


def main():
    print(load_entry())
    return 0


if __name__ == "__main__":
    sys.exit(main())
