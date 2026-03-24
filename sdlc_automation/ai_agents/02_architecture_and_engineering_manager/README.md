# Architecture And Engineering Manager Agent Builder

This package is the source layout for a skill-oriented OpenAI Codex app agent for the Architecture and Engineering Manager role. The live Codex skill adapter stays repo-local at [`../../../../.agents/skills/architecture_and_engineering_manager`](../../../../.agents/skills/architecture_and_engineering_manager), while this folder holds the agent contract, backing assets, and builder notes that feed it.

## Structure

```text
02_architecture_and_engineering_manager/
  README.md
  agent/
    README.md
    manifest.md
    inference_map.md
    operating_rules.md
    output_contracts.md
    source_index.md
  integrations/
    codex/
      README.md
  builder/
    README.md
    migration/
      codex_app_migration_plan.md
  assets/
    README.md
    knowledge/
    training/
```

## Active Agent Surface

- `agent/manifest.md`: package metadata, entrypoints, and integration pointers
- `agent/inference_map.md`: task routing, load order, escalation, and fallback
- `agent/operating_rules.md`: clarify-first behavior, assumptions, technical ownership, and handoffs
- `agent/output_contracts.md`: output shapes for feasibility briefs, ADRs, execution plans, and handoff notes
- `agent/source_index.md`: exact asset sources to load when the active docs are not enough

## Codex Integration

- `integrations/codex/README.md`: package-to-skill mapping for the OpenAI Codex app adapter
- `../../../../.agents/skills/architecture_and_engineering_manager/`: repo-local skill instructions and adapter card

## Project Context Configuration

- Repo-root `.env` defines `SDLC_AUTOMATION_PROJECT_PATHS`.
- Store the value as a JSON string array of repo-relative paths under `sdlc_automation\projects`.
- The starter list uses `sdlc_automation\projects\example_backend_project`, `sdlc_automation\projects\example_frontend_project`, and `sdlc_automation\projects\example_mobile_project`.
- Use the configured list when technical feasibility, architecture, or execution planning needs project-specific context from the projects area.

## Information Hub Configuration

- Repo-root `.env` defines `SDLC_AUTOMATION_INFORMATION_HUB_PATHS`.
- Store the value as a JSON string array of repo-relative paths under `sdlc_automation\information_hub`.
- The starter list uses `sdlc_automation\information_hub\analytics`, `sdlc_automation\information_hub\assets`, `sdlc_automation\information_hub\documentation`, and `sdlc_automation\information_hub\reported_issues`.
- Use the configured list when technical planning needs shared context from the information hub area.

## Backing Assets

- `assets/training/`: structured corpus, schemas, examples, evals, and validation tooling
- `assets/knowledge/`: legacy fallback reference material and historical rewrite context
- `builder/migration/`: maintenance-only migration notes and packaging history

## Builder Workflow

1. Start with [agent/inference_map.md](agent/inference_map.md).
2. Load [agent/operating_rules.md](agent/operating_rules.md) for behavior constraints.
3. Load [agent/output_contracts.md](agent/output_contracts.md) for response shape.
4. Load [agent/source_index.md](agent/source_index.md) to find the minimum asset material needed.
5. Open files under [assets](assets) only when the active agent docs point to them or coverage is insufficient.
6. Keep [`../../../../.agents/skills/architecture_and_engineering_manager`](../../../../.agents/skills/architecture_and_engineering_manager) aligned whenever the active agent contract changes.

## Validation

- Package-root validation: `python assets/training/fine_tuning/tooling/validate_seed_corpus.py`
- Asset-local validation: `python training/fine_tuning/tooling/validate_seed_corpus.py` from `assets/`
