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

### Discovery

- artifact: `../assets/training/fine_tuning/corpus/artifacts/discovery_brief.md`
- examples: `../assets/training/fine_tuning/corpus/examples/discovery_brief_good_b2b_workflow.md`

### Requirements

- artifact: `../assets/training/fine_tuning/corpus/artifacts/prd.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/product_requirement_refinement.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/engineering_requirement_clarification.md`
- risk: `../assets/training/fine_tuning/corpus/risks/ambiguous_requirements.md`

### Prioritization

- artifact: `../assets/training/fine_tuning/corpus/artifacts/decision_memo.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/exec_strategy_alignment.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/sales_priority_pressure.md`

### Metrics And Post-Launch Review

- interaction: `../assets/training/fine_tuning/corpus/interactions/data_metric_design.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/customer_success_adoption_barrier.md`
- interaction: `../assets/training/fine_tuning/corpus/interactions/support_operational_feedback.md`
- metric: `../assets/training/fine_tuning/corpus/metrics/adoption_rate.md`

### Governance And Compliance

- interaction: `../assets/training/fine_tuning/corpus/interactions/grc_compliance_requirement_mapping.md`
- variant: `../assets/training/fine_tuning/corpus/variants/regulated.md`
- artifact: `../assets/training/fine_tuning/corpus/artifacts/prd.md`
- artifact: `../assets/training/fine_tuning/corpus/artifacts/decision_memo.md`

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
