# Architecture And Engineering Manager Agent Builder

This package is the source layout for a skill-oriented OpenAI Codex app agent for the Architecture and Engineering Manager role. The live Codex skill adapter stays repo-local at [`../../../../.agents/skills/architecture_and_engineering_manager`](../../../../.agents/skills/architecture_and_engineering_manager), while this folder holds the agent contract, backing assets, and builder notes that feed it.

## Active Surface

- `agent/manifest.md`: package metadata, entrypoint, and workspace context model
- `agent/inference_map.md`: routing for feasibility, architecture, execution, and handoff work
- `agent/operating_rules.md`: clarify-first behavior, assumptions, and ownership boundaries
- `agent/output_contracts.md`: response shapes by task type
- `agent/source_index.md`: minimum supporting sources and workspace context rules

## Workspace Context Model

- Project selection starts at `projects/registry.yaml`.
- Detailed project context is loaded from `projects/<project-id>/hub/`.
- Shared context is loaded from `hub/shared/`.
- Role assets are loaded only after project and shared-hub context has been resolved.

## Validation

- Package-root validation: `python assets/training/fine_tuning/tooling/validate_seed_corpus.py`
