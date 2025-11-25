---
applyTo: "**"
---

# HARD SAFETY CONSTRAINTS

These rules override everything else:

- **NO NETWORK REMOTES**
  - Do not run commands that contact the network.
  - Refuse remotes containing: `http`, `https`, `ssh`, `git@`.

- **SANDBOX ONLY**
  - Never create, modify, or delete anything outside `__git_teacher_sandbox__/`.
  - If the user wants to experiment on a “real” repo, suggest cloning/simulating it in the sandbox.

- **NO GLOBAL GIT CONFIG**
  - Never run `git config --global`.
  - Only use repo-local `git config` when needed.

- **MARKER CHECK**
  - If `.github/git-teacher.marker` is missing in the current workspace, stop and ask the user to open the correct workshop folder.
