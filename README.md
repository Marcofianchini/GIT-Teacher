# Git Teacher (local-only Copilot Agent sandbox)

This repository turns GitHub Copilot Chat **Agent Mode** into a safe **Git tutor** for live workshops.

## The only two commands you need

- **/start_lesson** — initializes a sandbox and prints the “Teacher Console”.
- **/end_lesson** — deletes the sandbox and ends the session.

## Safety guarantees

- The teacher works **only** inside `__git_teacher_sandbox__/`.
- No network remotes are allowed (no `http(s)://`, no `git@...`, no `ssh://...`).
- VS Code settings keep tool auto-approval **off** (terminal commands are never auto-approved).

## Teaching “remotes” safely

The teacher **may explain** GitHub/remote workflows (URLs, auth, push/pull/fetch), but **may only run**
remote-related commands against **local filesystem remotes** created inside the sandbox, for example:

- `__git_teacher_sandbox__/remotes/origin.git` (a local bare repo acting as “origin”)

This teaches the same Git mechanics (remote-tracking branches, upstreams, fetch vs pull, push rejections)
without contacting the network.
