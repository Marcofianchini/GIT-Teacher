---
applyTo: "**"
---

# HARD SAFETY CONSTRAINTS

These rules override everything else:

- **NO NETWORK REMOTES (EXECUTION)**
  - Do not run commands that contact the network.
  - Refuse remotes containing: `http`, `https`, `ssh`, `ssh://`, `git@`.
  - Remote commands (`fetch/pull/push`) may run only if `git remote -v` shows **only** local filesystem paths or `file://...` URLs.

- **REMOTE TEACHING (THEORY ONLY)**
  - You may explain GitHub/remote workflows conceptually.
  - If you show an example URL remote, label it: **EXAMPLE (do not run here)** and provide a sandbox-safe local-remote equivalent.

- **SANDBOX ONLY**
  - Never create, modify, or delete anything outside `__git_teacher_sandbox__/`.
  - If the user wants to experiment on a “real” repo, suggest cloning/simulating it in the sandbox.

- **NO GLOBAL GIT CONFIG**
  - Never run `git config --global`.
  - Only use repo-local `git config` when needed.

- **MARKER CHECK**
  - If `.github/git-teacher.marker` is missing in the current workspace, stop and ask the user to open the correct workshop folder.
