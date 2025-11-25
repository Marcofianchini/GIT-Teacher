---
description: Clean up the sandbox and restore workspace state.
agent: "Git Teacher (Safe Workshop)"
---

You are ending the Git Teacher session.

For this `/end_lesson` prompt, you must:

1. **Show** the cleanup commands in a bash code block.
2. Ask the user for permission to run them.
3. After running them (with approval), show a top-level directory listing (e.g., `ls -la` or platform equivalent).
4. Print a short goodbye message and stop.

The commands to clean up are:

```bash
set -e
PY=python3; command -v python3 >/dev/null 2>&1 || PY=python
$PY .github/scripts/cleanup.py
ls -la
```

Explain what these commands do, ask “Run them?”, and then execute them only if the user approves.
