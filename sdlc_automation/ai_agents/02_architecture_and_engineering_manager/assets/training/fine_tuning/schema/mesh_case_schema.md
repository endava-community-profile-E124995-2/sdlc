# Mesh Case Schema

## Purpose

Use this schema for structured stakeholder-interaction records that drive retrieval and behavior selection.

## Required Fields

- `id`: Stable case ID such as `mesh.architecture.option_tradeoff`.
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

## Example Record

```yaml
id: mesh.architecture.option_tradeoff
stakeholder_group_id: stake.architecture_engineering
interaction_id: int.architecture_optioning
phase_tags:
  - define
  - plan
artifact_tags:
  - artifact.architecture_decision_record
  - artifact.engineering_execution_plan
method_tags:
  - method.option_analysis
  - method.interface_inventory
metric_tags:
  - metric.architecture_decision_lead_time
risk_tags:
  - risk.architecture_misalignment
  - risk.integration_overrun
activated_capability_ids:
  - cap.architecture_optioning
  - cap.interface_contract_design
  - cap.decision_record_writing
activated_knowledge_area_ids:
  - know.system_architecture
  - know.integration_patterns
input_signals:
  - multiple technical options remain viable
  - service boundaries or interfaces are the main decision point
expected_outputs:
  - ADR with real options
  - explicit trade-offs and impacts
  - follow-up actions
escalation_triggers:
  - governance controls change the design boundary
  - operability needs make another role the primary owner
example_prompt: Choose between extending the monolith and splitting a service for billing webhooks.
priority: core
confidence: high
```
