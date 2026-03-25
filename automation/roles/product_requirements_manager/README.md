# Product And Requirements Manager Role Package

This package is the canonical product-facing role definition for the Codex SDLC workspace. The repo-local adapter lives at [`../../../.agents/skills/product-requirements-manager`](../../../.agents/skills/product-requirements-manager), while this folder holds the source-of-truth agent contract and assets.

## Active Surface

- `agent/manifest.md`: package metadata, entrypoint, and workspace context model
- `agent/inference_map.md`: routing for discovery, requirements, prioritization, rollout, and metrics work
- `agent/operating_rules.md`: clarify-first behavior, assumptions, and role boundaries
- `agent/output_contracts.md`: response shapes by task type
- `agent/source_index.md`: minimum supporting sources and workspace context rules

## Workspace Context Model

- Project selection starts at `projects/registry.yaml`.
- Detailed project context is loaded from `projects/<project-id>/hub/`.
- Shared context is loaded from `hub/shared/`.
- Role assets are loaded only after project and shared-hub context has been resolved.

## Validation

- Package-root validation: `python assets/training/fine_tuning/tooling/validate_seed_corpus.py`
