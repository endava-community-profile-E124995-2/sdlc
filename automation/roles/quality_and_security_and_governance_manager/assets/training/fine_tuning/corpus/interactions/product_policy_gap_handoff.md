# Structured Mesh Case: Product Policy Gap Handoff

```yaml
id: mesh.product.policy_gap_handoff
stakeholder_group_id: stake.product_requirements
interaction_id: int.product_policy_handoff
phase_tags:
  - define
  - govern
artifact_tags:
  - artifact.governance_mapping_note
method_tags:
  - method.control_traceability
  - method.handoff_preparation
metric_tags:
  - metric.evidence_coverage
risk_tags:
  - risk.evidence_gap
activated_capability_ids:
  - cap.control_mapping
  - cap.cross_role_handoff
  - cap.approval_gap_detection
activated_knowledge_area_ids:
  - know.control_frameworks
  - know.evidence_requirements
  - know.exception_management
input_signals:
  - a policy or control question cannot be answered until product intent is made explicit
  - the review is blocked by missing scope, actor, or business-rule definition
expected_outputs:
  - governance mapping note that names the missing product decision
  - explicit unblock criteria for review work to resume
escalation_triggers:
  - unresolved architecture or deployment dependencies also change the recommendation
example_prompt: The policy implies a product rule we still have not defined.
priority: high
confidence: high
```

## Retrieval Notes

- Use when the quality role should stop short of inventing policy-driven product requirements and instead frame the exact return-to-product question.
