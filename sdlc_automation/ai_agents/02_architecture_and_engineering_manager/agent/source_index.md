# Source Index

Use this file to locate the minimum asset material needed after the task is classified.

## Core Asset Sources

- policy: `../assets/training/fine_tuning/corpus/policies/assistant_operating_policy.md`
- canonical ids: `../assets/training/fine_tuning/corpus/ontology/canonical_id_map.md`
- fallback knowledge: `../assets/knowledge/legacy_role_rag/`

## Project Context Roots

- env var: `SDLC_AUTOMATION_PROJECT_PATHS`
- format: JSON string array
- expected entries: repo-relative paths under `sdlc_automation\projects`

## Information Hub Roots

- env var: `SDLC_AUTOMATION_INFORMATION_HUB_PATHS`
- format: JSON string array
- expected entries: repo-relative paths under `sdlc_automation\information_hub`

## Task-Specific Packs

### Technical Feasibility

- artifact: `../assets/training/fine_tuning/corpus/artifacts/technical_feasibility_brief.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/technical_feasibility_assessment.md`
- risk: `../assets/training/fine_tuning/corpus/risks/architecture_misalignment.md`
- metric: `../assets/training/fine_tuning/corpus/metrics/architecture_decision_lead_time.md`

### Architecture Decision

- artifact: `../assets/training/fine_tuning/corpus/artifacts/architecture_decision_record.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/architecture_option_tradeoff.md`
- risk: `../assets/training/fine_tuning/corpus/risks/integration_overrun.md`
- metric: `../assets/training/fine_tuning/corpus/metrics/architecture_decision_lead_time.md`

### Engineering Execution

- artifact: `../assets/training/fine_tuning/corpus/artifacts/engineering_execution_plan.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/engineering_execution_planning.md`
- risk: `../assets/training/fine_tuning/corpus/risks/handoff_loss.md`
- metric: `../assets/training/fine_tuning/corpus/metrics/dependency_burn_down_rate.md`

### Cross-Role Handoff

- artifact: `../assets/training/fine_tuning/corpus/artifacts/cross_role_handoff_note.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/product_intent_gap_handoff.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/quality_control_handoff.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/operability_handoff.md`
- risk: `../assets/training/fine_tuning/corpus/risks/operability_gap.md`

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
