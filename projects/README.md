# Attached Projects

`projects/` stores committed metadata for linked product repos.

- `registry.yaml` is the authoritative project index.
- Each `projects/<project-id>/` directory contains committed project metadata plus a scoped project hub.
- `attachment.local.yaml` stays untracked and maps repo ids to local checkout paths or worktrees on a specific machine.
