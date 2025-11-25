#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path.cwd()
MARKER = ROOT / ".github" / "git-teacher.marker"
STATE_DIR = ROOT / ".github" / "git-teacher-state"
MANIFEST_PATH = STATE_DIR / "original_top_level.json"


def die(msg: str, code: int = 2) -> None:
    print(f"[git-teacher] ERROR: {msg}", file=sys.stderr)
    sys.exit(code)


def safe_rmtree(path: Path) -> None:
    """
    Remove a directory tree *only if* it is inside the current workspace root.

    Extra safety:
    - refuses to delete '/', the workspace root itself, or anything outside the workspace
    - refuses to follow symlinks as directories
    """
    if not path.exists():
        return

    root = ROOT.resolve()
    target = path.resolve()

    if str(target) in ("/", str(root)):
        die(f"Refusing to delete unsafe path: {path}")

    if root not in target.parents:
        die(f"Refusing to delete path outside workspace: {path}")

    # If it's a symlink, unlink the symlink itself.
    if path.is_symlink():
        path.unlink()
        return

    shutil.rmtree(path)


def main() -> None:
    if not MARKER.exists():
        die("Missing marker .github/git-teacher.marker. Refusing to cleanup.")

    sandbox_dirname = "__git_teacher_sandbox__"

    if MANIFEST_PATH.exists():
        data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        sandbox_dirname = data.get("sandbox_dirname", sandbox_dirname)
    else:
        print("[git-teacher] WARNING: No manifest found; will only remove sandbox if present.")

    sandbox = ROOT / sandbox_dirname
    safe_rmtree(sandbox)
    print(f"[git-teacher] Removed sandbox: {sandbox_dirname}")

    # Remove only Git Teacher state (never touch other root items).
    if STATE_DIR.exists():
        safe_rmtree(STATE_DIR)
        print("[git-teacher] Removed state directory: .github/git-teacher-state")

    print("[git-teacher] Cleanup complete.")


if __name__ == "__main__":
    main()
