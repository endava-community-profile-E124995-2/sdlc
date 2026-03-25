# Structured Mesh Case: Product Rollout Constraint Handoff

```yaml
id: mesh.product.rollout_constraint_handoff
stakeholder_group_id: stake.product_requirements
interaction_id: int.product_rollout_constraint_handoff
phase_tags:
  - plan
  - launch
artifact_tags:
  - artifact.rollout_plan
method_tags:
  - method.sequence_planning
  - method.owner_mapping
metric_tags:
  - metric.deployment_lead_time
risk_tags:
  - risk.rollout_coordination_drift
activated_capability_ids:
  - cap.rollout_planning
  - cap.cross_role_handoff
activated_knowledge_area_ids:
  - know.release_scope
  - know.rollout_strategy
input_signals:
  - phased rollout constraints are unclear because audience or scope decisions are still moving
  - business launch sequencing is being treated as if operations can decide it alone
expected_outputs:
  - rollout-plan-shaped handoff to product with explicit missing business decisions
  - unblock criteria for deployment planning to resume
escalation_triggers:
  - the blocker is actually a gate or architecture question rather than a business rollout choice
example_prompt: Phased rollout constraints are unclear because launch audience and scope are still undecided.
priority: high
confidence: high
```

## Retrieval Notes

- Use when deployment can frame the operational consequence but product still owns the business rollout choice.
