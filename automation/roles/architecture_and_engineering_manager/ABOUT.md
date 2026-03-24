# About This Agent Package

This folder is the builder/source package for a skill-oriented OpenAI Codex app agent that plays the Architecture and Engineering Manager role.

It keeps the live contract in a small active layer while storing structured technical assets, evals, and legacy fallback material behind it.

## ASCII Map

```text
02_architecture_and_engineering_manager/
|
+-- ABOUT.md
|   Notes: quick orientation for humans.
|
+-- README.md
|   Notes: package overview and working model.
|
+-- agent/
|   Notes: active agent surface; this is the hot path.
|   |
|   +-- README.md
|   |   Notes: explains how the active agent layer works.
|   |
|   +-- manifest.md
|   |   Notes: package identity, entrypoint, Codex linkage, validation command.
|   |
|   +-- inference_map.md
|   |   Notes: task router for feasibility, architecture, execution, and handoff work.
|   |
|   +-- operating_rules.md
|   |   Notes: behavior rules, escalation boundaries, assumption handling.
|   |
|   +-- output_contracts.md
|   |   Notes: required output shapes for technical briefs, ADRs, execution plans, and handoffs.
|   |
|   +-- source_index.md
|       Notes: points to the minimum backing sources needed per task.
|
+-- assets/
|   Notes: heavier backing content used only when needed.
|   |
|   +-- README.md
|   |   Notes: explains asset usage and validation.
|   |
|   +-- training/
|   |   Notes: structured corpus for examples, evals, schemas, and tooling.
|   |   |
|   |   +-- fine_tuning/
|   |       Notes: organized training and eval package for this role.
|   |       |
|   |       +-- corpus/
|   |       |   Notes: the main structured role knowledge.
|   |       |
|   |       +-- evals/
|   |       |   Notes: checks for retrieval, behavior, and output quality.
|   |       |
|   |       +-- schema/
|   |       |   Notes: document shapes and validation contracts.
|   |       |
|   |       +-- tooling/
|   |           Notes: validation and migration helpers.
|   |
|   +-- knowledge/
|       Notes: legacy fallback material and rewrite history.
|       |
|       +-- legacy_role_rag/
|       |   Notes: broad inherited reference pack; fallback only.
|       |
|       +-- role_rag_rewrite_plan.md
|           Notes: records how the legacy pack is being reshaped for this role.
|
+-- builder/
|   Notes: maintenance and package-building notes for humans.
|   |
|   +-- README.md
|   |   Notes: explains what builder notes belong here.
|   |
|   +-- migration/
|       Notes: structural change history.
|       |
|       +-- codex_app_migration_plan.md
|           Notes: records how this package was adapted for Codex.
|
+-- integrations/
    Notes: app-specific bridge docs.
    |
    +-- codex/
        Notes: documents how this package feeds the repo-local Codex skill.
        |
        +-- README.md
            Notes: package-to-skill mapping for the OpenAI Codex app.
```

## Short Model

- `agent/` is what the AI should read first.
- `assets/` is the structured backing knowledge.
- `builder/` is for humans maintaining the package shape.
- `integrations/` explains how the package connects to Codex.

## Project Context Configuration

- Repo-root `.env` defines `SDLC_AUTOMATION_PROJECT_PATHS`.
- Treat the value as a JSON string array of repo-relative paths under `sdlc_automation\projects`.
- The default examples are `sdlc_automation\projects\example_backend_project`, `sdlc_automation\projects\example_frontend_project`, and `sdlc_automation\projects\example_mobile_project`.
- Use this list as the default project discovery scope when feasibility, architecture, or execution planning depends on concrete projects.

## Information Hub Configuration

- Repo-root `.env` defines `SDLC_AUTOMATION_INFORMATION_HUB_PATHS`.
- Treat the value as a JSON string array of repo-relative paths under `sdlc_automation\information_hub`.
- The default examples are `sdlc_automation\information_hub\analytics`, `sdlc_automation\information_hub\assets`, `sdlc_automation\information_hub\documentation`, and `sdlc_automation\information_hub\reported_issues`.
- Use this list as the default information-hub discovery scope when the task depends on shared documentation, incidents, assets, or analytics.

## Why This Split Exists

- Keeps the inference path small and cheap.
- Keeps structured technical assets available without bloating the active prompt surface.
- Makes Codex integration explicit instead of hidden in scattered files.
- Makes future role packages easier to mirror with the same pattern.
