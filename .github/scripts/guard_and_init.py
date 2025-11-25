#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path.cwd()
MARKER = ROOT / ".github" / "git-teacher.marker"
STATE_DIR = ROOT / ".github" / "git-teacher-state"
MANIFEST_PATH = STATE_DIR / "original_top_level.json"

# Teacher files that are allowed at workspace root.
WHITELIST = {
    ".github",
    ".vscode",
    "README.md",
    ".gitignore",
    ".editorconfig",
}

SANDBOX = ROOT / "__git_teacher_sandbox__"


def die(msg: str, code: int = 2) -> None:
    print(f"[git-teacher] ERROR: {msg}", file=sys.stderr)
    sys.exit(code)


def top_level_entries() -> list[str]:
    return sorted([p.name for p in ROOT.iterdir() if p.name not in (".", "..")])


def main() -> None:
    if not MARKER.exists():
        die("Missing marker .github/git-teacher.marker. Open the correct workshop folder.")

    STATE_DIR.mkdir(parents=True, exist_ok=True)

    existing = top_level_entries()
    unexpected = [
        name for name in existing
        if name not in WHITELIST and name != SANDBOX.name
    ]

    manifest = {
        "root": str(ROOT),
        "created_at_epoch": int(time.time()),
        "whitelist": sorted(WHITELIST),
        "original_non_teacher_top_level": unexpected,
        "sandbox_dirname": SANDBOX.name,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    # Sandbox structure
    SANDBOX.mkdir(parents=True, exist_ok=True)
    (SANDBOX / "labs").mkdir(parents=True, exist_ok=True)
    (SANDBOX / "remotes").mkdir(parents=True, exist_ok=True)

    if unexpected:
        print("[git-teacher] WARNING: Workspace root contains non-teacher items.")
        print("[git-teacher] I will NOT touch them. I will work only in: __git_teacher_sandbox__/")
        for name in unexpected:
            print(f"  - {name}")
    else:
        print("[git-teacher] Workspace root contains only teacher files (good).")

    print(f"[git-teacher] Sandbox ready at: {SANDBOX}")
    print(f"[git-teacher] State recorded at: {MANIFEST_PATH}")


if __name__ == "__main__":
    main()
