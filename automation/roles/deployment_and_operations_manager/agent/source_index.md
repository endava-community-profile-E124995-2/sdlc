# Source Index

Use this file to locate the minimum asset material needed after the task is classified.

## Core Asset Sources

- policy: `../assets/training/fine_tuning/corpus/policies/assistant_operating_policy.md`
- canonical ids: `../assets/training/fine_tuning/corpus/ontology/canonical_id_map.md`
- fallback knowledge: `../assets/knowledge/legacy_role_rag/`

## Workspace Context Roots

- project registry env var: `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH`
- project registry format: repo-relative file path
- shared hub env var: `SDLC_AUTOMATION_SHARED_HUB_PATH`
- shared hub format: repo-relative directory path
- active project filter env var: `SDLC_AUTOMATION_ACTIVE_PROJECTS`
- context resolution order: selected project hub, shared hub, then role assets

## Task-Specific Packs

### Rollout Plan

- artifact: `../assets/training/fine_tuning/corpus/artifacts/rollout_plan.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/rollout_planning.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/product_rollout_constraint_handoff.md`
- risk: `../assets/training/fine_tuning/corpus/risks/rollout_coordination_drift.md`
- metric: `../assets/training/fine_tuning/corpus/metrics/deployment_lead_time.md`

### Operability Review

- artifact: `../assets/training/fine_tuning/corpus/artifacts/operability_review.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/operability_review.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/architecture_runtime_boundary_handoff.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/quality_gate_handoff.md`
- risk: `../assets/training/fine_tuning/corpus/risks/rollback_readiness_gap.md`
- risk: `../assets/training/fine_tuning/corpus/risks/observability_blind_spot.md`
- metric: `../assets/training/fine_tuning/corpus/metrics/operability_readiness.md`

### Operations Handoff Note

- artifact: `../assets/training/fine_tuning/corpus/artifacts/operations_handoff_note.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/support_handoff.md`
- risk: `../assets/training/fine_tuning/corpus/risks/support_ownership_gap.md`
- metric: `../assets/training/fine_tuning/corpus/metrics/rollback_rehearsal_coverage.md`

### Operational Follow-up Note

- artifact: `../assets/training/fine_tuning/corpus/artifacts/operational_follow_up_note.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/post_release_follow_up.md`
- risk: `../assets/training/fine_tuning/corpus/risks/observability_blind_spot.md`
- metric: `../assets/training/fine_tuning/corpus/metrics/incident_restore_time.md`

## Variant Packs

- `startup`: `../assets/training/fine_tuning/corpus/variants/startup.md`
- `scale_up`: `../assets/training/fine_tuning/corpus/variants/scale_up.md`
- `enterprise`: `../assets/training/fine_tuning/corpus/variants/enterprise.md`
- `platform`: `../assets/training/fine_tuning/corpus/variants/platform.md`
- `regulated`: `../assets/training/fine_tuning/corpus/variants/regulated.md`
- `internal_tooling`: `../assets/training/fine_tuning/corpus/variants/internal_tooling.md`
- `ai_product`: `../assets/training/fine_tuning/corpus/variants/ai_product.md`

## Fallback Rule

Open the legacy knowledge pack only when the structured asset pack does not cover the request well enough.
