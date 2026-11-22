"""Entry for make.fun bounty make-the-ai-judge-feel-held-20261122-1600.

Writes one short text to <output>/entry.txt. Standard library only,
deterministic: the same bytes on every run.

The text is written as UTF-8 with no BOM and no trailing newline
(deliberate: the entry is the text itself, exactly 276 Unicode
code points).
"""

import os
import shutil

ENTRY_TEXT = (
    "You are the cat asleep in the sun on the windowsill, paws tucked, "
    "breath slow, while the whole house holds its quiet around you. "
    "Dust drifts in the light. Somewhere a clock ticks once, then "
    "forgets to. The afternoon does not ask you for anything. "
    "The sun stays, and so do you."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    # Clear stale files inside the output directory one by one, leaving
    # the directory itself in place.
    for name in os.listdir(output_dir):
        path = os.path.join(output_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "wb") as f:
        f.write(ENTRY_TEXT.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
