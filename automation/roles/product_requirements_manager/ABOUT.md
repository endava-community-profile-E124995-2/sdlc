# About This Agent Package

This folder is the builder/source package for a skill-oriented OpenAI Codex app agent that plays the Product and Requirements Manager role.

It is organized so the small, active agent contract stays easy to load, while heavier training and legacy material stays behind it as backing assets.

## ASCII Map

```text
01_product_and_requirements_manager/
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
|   |   Notes: task router; decides what kind of product work this is.
|   |
|   +-- operating_rules.md
|   |   Notes: behavior rules, escalation boundaries, assumption handling.
|   |
|   +-- output_contracts.md
|   |   Notes: required output shapes for discovery, PRDs, rollout, metrics, etc.
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
|   |       Notes: organized training/eval package for this role.
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
|       |   Notes: broad older reference pack; fallback only.
|       |
|       +-- role_rag_rewrite_plan.md
|           Notes: explains how the old pack was reshaped into structured assets.
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
- `assets/` is the knowledge base behind the agent.
- `builder/` is for humans maintaining the package shape.
- `integrations/` explains how the package connects to Codex.

## Project Context Configuration

- Repo-root `.env` defines `SDLC_AUTOMATION_PROJECT_PATHS`.
- Treat the value as a JSON string array of repo-relative paths under `sdlc_automation\projects`.
- The default examples are `sdlc_automation\projects\example_backend_project`, `sdlc_automation\projects\example_frontend_project`, and `sdlc_automation\projects\example_mobile_project`.
- Use this list as the default project discovery scope when the task depends on one or more concrete projects.

## Information Hub Configuration

- Repo-root `.env` defines `SDLC_AUTOMATION_INFORMATION_HUB_PATHS`.
- Treat the value as a JSON string array of repo-relative paths under `sdlc_automation\information_hub`.
- The default examples are `sdlc_automation\information_hub\analytics`, `sdlc_automation\information_hub\assets`, `sdlc_automation\information_hub\documentation`, and `sdlc_automation\information_hub\reported_issues`.
- Use this list as the default information-hub discovery scope when the task depends on shared docs, assets, analytics, or reported issues.

## Why This Split Exists

- Keeps the inference path small and cheap.
- Keeps training and legacy content available without bloating the active prompt surface.
- Makes Codex integration explicit instead of hidden in scattered files.
- Makes future role packages easier to mirror with the same pattern.
