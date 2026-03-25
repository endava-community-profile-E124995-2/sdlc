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

### Quality Review

- artifact: `../assets/training/fine_tuning/corpus/artifacts/quality_review_note.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/verification_strategy_review.md`
- risk: `../assets/training/fine_tuning/corpus/risks/verification_gap.md`
- metric: `../assets/training/fine_tuning/corpus/metrics/defect_escape_rate.md`

### Security Review

- artifact: `../assets/training/fine_tuning/corpus/artifacts/security_review_note.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/security_boundary_review.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/architecture_boundary_handoff.md`
- risk: `../assets/training/fine_tuning/corpus/risks/security_boundary_drift.md`
- metric: `../assets/training/fine_tuning/corpus/metrics/remediation_lead_time.md`

### Governance Mapping

- artifact: `../assets/training/fine_tuning/corpus/artifacts/governance_mapping_note.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/governance_control_mapping.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/product_policy_gap_handoff.md`
- risk: `../assets/training/fine_tuning/corpus/risks/evidence_gap.md`
- metric: `../assets/training/fine_tuning/corpus/metrics/evidence_coverage.md`

### Release Gate

- artifact: `../assets/training/fine_tuning/corpus/artifacts/release_gate_memo.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/release_gate_assessment.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/deployment_readiness_handoff.md`
- risk: `../assets/training/fine_tuning/corpus/risks/gate_readiness_blind_spot.md`
- metric: `../assets/training/fine_tuning/corpus/metrics/gate_decision_lead_time.md`

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
