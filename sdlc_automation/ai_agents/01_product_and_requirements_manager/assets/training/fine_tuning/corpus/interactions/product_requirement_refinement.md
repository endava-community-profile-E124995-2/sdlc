# Structured Mesh Case: Product Requirement Refinement

```yaml
id: mesh.product.requirement_refinement
stakeholder_group_id: stake.product_org
interaction_id: int.requirement_validation
phase_tags:
  - define
  - plan
artifact_tags:
  - artifact.prd
  - artifact.requirement_change_log
method_tags:
  - method.story_mapping
  - method.workflow_mapping
metric_tags:
  - metric.requirement_rework_rate
risk_tags:
  - risk.ambiguous_requirements
  - risk.scope_creep
activated_capability_ids:
  - cap.requirements_elicitation
  - cap.requirements_clarification
  - cap.acceptance_criteria_writing
  - cap.traceable_requirement_writing
  - cap.stakeholder_alignment
activated_knowledge_area_ids:
  - know.product_strategy
  - know.customer_workflows
input_signals:
  - backlog items are moving forward with unresolved ambiguity
  - product peers disagree on scope boundaries or exclusions
  - changes are being made without a visible rationale
expected_outputs:
  - revised requirement set with scope and exclusion clarity
  - updated acceptance criteria
  - change log entry for what changed and why
escalation_triggers:
  - dependency or governance exposure changes the release shape
  - requirement conflicts cannot be resolved within the product group
example_prompt: Tighten this rough feature request into a requirement set we can take into refinement without setting engineering up for rework.
priority: core
confidence: high
```

## Retrieval Notes

- Use for backlog shaping, PRD tightening, and scope clarification.
- Prefer this case over a generic discovery case when the problem is known but the requirement quality is weak.
