# Git Teacher (local-only Copilot Agent sandbox)

This repository turns GitHub Copilot Chat **Agent Mode** into a safe **Git tutor** for live workshops.

## The only two commands you need

- **/start_lesson** — initializes a sandbox and prints the “Teacher Console”.
- **/end_lesson** — deletes the sandbox and ends the session.

## Safety guarantees

- The teacher works **only** inside `__git_teacher_sandbox__/`.
- No network remotes are allowed (no `http(s)://`, no `git@...`, no `ssh`).
- VS Code settings keep tool auto-approval **off** (terminal commands are never auto-approved).
- Customization is done via standard VS Code Copilot files:
  - `.github/copilot-instructions.md`
  - `.github/instructions/*.instructions.md`
  - `.github/agents/*.agent.md`
  - `.github/prompts/*.prompt.md`
