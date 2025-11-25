---
applyTo: "**"
---

# SANDBOX BEHAVIOR

- Always operate in `__git_teacher_sandbox__/`.
- Create each new lab under:
  - `__git_teacher_sandbox__/labs/<lab_name>/`
- Assume the workspace root may contain non-teacher files.
  - Do **not** touch them.
  - Warn the user if they exist.
- Prefer explicit paths and `git -C <repoPath>` to avoid confusion about the current directory.
