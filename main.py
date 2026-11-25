"""Emit the make.fun entry line into entry.txt under the chosen output folder.

Selects that folder from MAKEFUN_OUTPUT_DIR (default /output) and the emitted bytes must never change.
"""

import os
import sys


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as exc:
        sys.exit(f"cannot create output directory {output_dir!r}: {exc}")
    text = "Out of office. An AI has my inbox now: every reply will be kind, confident, and about something adjacent to your question.\n"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
