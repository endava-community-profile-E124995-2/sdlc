# Deployment And Operations Manager

This package is the canonical deployment and operations role definition for the Codex SDLC workspace. The repo-local adapter lives at [`../../../.agents/skills/deployment_and_operations_manager`](../../../.agents/skills/deployment_and_operations_manager), while this folder holds the source-of-truth agent contract and assets.

## Active Surface

- `agent/manifest.md`: package metadata, entrypoint, workspace context model, and validation command
- `agent/inference_map.md`: routing for rollout planning, operability review, support handoff, and post-release follow-up
- `agent/operating_rules.md`: clarify-first behavior, assumptions, and role boundaries
- `agent/output_contracts.md`: response shapes for the four deployment artifacts
- `agent/source_index.md`: minimum supporting sources and workspace context rules

## Backing Assets

- `assets/training/fine_tuning/`: structured corpus, examples, evals, schemas, and validation tooling
- `assets/knowledge/legacy_role_rag/`: fallback reference pack that must not override the active contract
- `builder/migration/`: builder-only migration and packaging notes

## Role Boundaries

- Product and Requirements Manager keeps launch audience, enablement, and business rollout constraints.
- Architecture and Engineering Manager owns technical design, implementation planning, and unresolved runtime design boundaries.
- Quality and Security and Governance Manager owns gate recommendations, evidence sufficiency review, and exception framing.
- Deployment and Operations Manager owns rollout sequencing, rollback readiness, observability, runbooks, support ownership, and post-release operational follow-up.

## Validation

- Package-root validation: `python assets/training/fine_tuning/tooling/validate_seed_corpus.py`
