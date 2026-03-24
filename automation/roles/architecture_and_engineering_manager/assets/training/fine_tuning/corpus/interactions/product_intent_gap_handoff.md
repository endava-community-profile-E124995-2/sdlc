# Structured Mesh Case: Product Intent Gap Handoff

```yaml
id: mesh.product.intent_gap_handoff
stakeholder_group_id: stake.product_requirements
interaction_id: int.cross_role_handoff
phase_tags:
  - define
artifact_tags:
  - artifact.cross_role_handoff_note
method_tags:
  - method.handoff_review
metric_tags:
  - metric.plan_volatility
risk_tags:
  - risk.handoff_loss
activated_capability_ids:
  - cap.handoff_preparation
  - cap.current_state_analysis
activated_knowledge_area_ids:
  - know.delivery_governance
  - know.non_functional_requirements
input_signals:
  - the team keeps discovering new scope while planning technical work
  - acceptance criteria or business rules are still unstable
  - engineering cannot make a safe design call from the current inputs
expected_outputs:
  - explicit return-to-product handoff
  - missing business inputs and open decisions
  - unblock criteria for technical work to resume
escalation_triggers:
  - unresolved external control obligations also require governance review
example_prompt: Requirements are still ambiguous and the team keeps discovering new scope. Draft the handoff back to product.
priority: high
confidence: high
```

## Retrieval Notes

- Use when the right answer is to stop inventing scope and hand the work back to product ownership.
- Preserve the known technical facts so the next round starts from reality, not from scratch.
