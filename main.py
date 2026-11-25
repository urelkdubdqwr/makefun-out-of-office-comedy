"""Write the make.fun entry text to <MAKEFUN_OUTPUT_DIR>/entry.txt.

The output directory is the value of MAKEFUN_OUTPUT_DIR when set and
non-empty, otherwise /output. The directory is created if missing.
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
