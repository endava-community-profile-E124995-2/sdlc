# Mesh Case Schema

## Purpose

Use this schema for structured stakeholder-interaction records that drive retrieval and behavior selection.

## Required Fields

- `id`: Stable case ID such as `mesh.quality.verification_strategy_review`.
- `stakeholder_group_id`: Canonical stakeholder group ID.
- `interaction_id`: Canonical interaction ID.
- `phase_tags`: Lifecycle phases such as `discover`, `define`, `decide`, `plan`, `deliver`, `launch`, `learn`, or `govern`.
- `artifact_tags`: Canonical artifact IDs most likely to be produced.
- `method_tags`: Canonical method IDs most likely to be used.
- `metric_tags`: Canonical metric IDs relevant to success or health.
- `risk_tags`: Canonical risk IDs relevant to the case.
- `activated_capability_ids`: Canonical capability IDs expected to activate.
- `activated_knowledge_area_ids`: Canonical knowledge-area IDs expected to activate.
- `input_signals`: Common signals or triggers that indicate the case is active.
- `expected_outputs`: What the assistant should usually produce.
- `escalation_triggers`: What changes the recommendation or requires handoff.
- `example_prompt`: One representative user prompt.
- `priority`: One of `core`, `high`, `medium`, or `contextual`.
- `confidence`: One of `high`, `medium`, or `low`.

## Validation Rules

- All referenced IDs must exist in the canonical ID map.
- `phase_tags` must use lifecycle labels only.
- `artifact_tags`, `method_tags`, `metric_tags`, and `risk_tags` should be short and selective.
- `input_signals`, `expected_outputs`, and `escalation_triggers` must be scenario-specific, not generic filler.
- `example_prompt` should sound like a real request from product, engineering, governance, or operations stakeholders.
