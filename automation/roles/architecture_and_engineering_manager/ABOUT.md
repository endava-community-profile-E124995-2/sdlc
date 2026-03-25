# About This Role Package

This folder is the canonical Architecture and Engineering Manager package for the Codex SDLC workspace.

The workspace model is:

- `projects/` holds attached-project metadata and project-local hubs
- `hub/shared/` holds cross-project context
- `automation/roles/` holds role contracts and backing assets
- `.agents/skills/` holds thin repo-local adapters that point back to this package

## Package Shape

```text
architecture_and_engineering_manager/
|
+-- ABOUT.md
+-- README.md
+-- agent/
+-- assets/
+-- builder/
+-- integrations/
```

- `agent/` is the active contract and should be read first.
- `assets/` holds deeper technical knowledge, eval, and training material.
- `builder/` holds maintenance notes for package authors.
- `integrations/` documents how the package is exposed to Codex.

## Workspace Context Resolution

1. Start with `projects/registry.yaml`.
2. Load the selected project's `projects/<project-id>/hub/`.
3. Load shared context from `hub/shared/`.
4. Load role assets only after project and shared-hub context are known.

The legacy path-array environment variables remain only as compatibility aliases during migration.

## Why This Split Exists

- Keeps the active prompt surface small.
- Makes project context explicit instead of implied through folder scans.
- Separates canonical role logic from repo-local adapters.
- Gives attached projects and the shared hub first-class structure.
