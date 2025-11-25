---
description: Initialize the Git Teacher sandbox and print the Teacher Console.
agent: "Git Teacher (Safe Workshop)"
---

You are starting a Git Teacher session in **Agent Mode**.

For this `/start_lesson` prompt, you must:

1. **Show** the guard initializer commands in a bash code block.
2. Ask the user for permission to run them.
3. After running them (with approval), print a “Teacher Console” banner that includes:
   - The sandbox path (`__git_teacher_sandbox__/`).
   - How to interact: `next`, `repeat`, `run`, `why`, `status`, `reset`, `/end_lesson`.
   - A short safety reminder: local-only, sandbox-only, no network remotes.
4. Then **stop and wait** for the user to choose a topic (e.g. “fetch vs pull”).

The commands to initialize the sandbox are:

```bash
set -e
PY=python3; command -v python3 >/dev/null 2>&1 || PY=python
$PY .github/scripts/guard_and_init.py
```

Explain what these commands do, ask “Run them?”, and only then execute them if the user approves.
