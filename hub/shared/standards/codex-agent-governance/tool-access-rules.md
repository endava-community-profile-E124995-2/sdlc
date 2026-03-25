# Tool And Context Access Rules

- Read repo-root `.env` before resolving project or shared context.
- Read `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH` to locate `projects/registry.yaml`.
- Read `SDLC_AUTOMATION_SHARED_HUB_PATH` to locate `hub/shared/`.
- Resolve project hub and shared hub before opening role asset material.
- Load only the minimum role asset pack needed for the task.
- Do not invent project ids, approval states, runtime ownership, or artifact paths that are not present in repo context.
- Ephemeral run notes and review scratch output belong under `.artifacts/`, not committed source directories.
