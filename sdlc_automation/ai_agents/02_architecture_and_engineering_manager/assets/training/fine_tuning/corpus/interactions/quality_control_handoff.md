# Structured Mesh Case: Quality, Security, And Governance Handoff

```yaml
id: mesh.qsg.control_handoff
stakeholder_group_id: stake.quality_security_governance
interaction_id: int.control_review_handoff
phase_tags:
  - define
  - plan
artifact_tags:
  - artifact.cross_role_handoff_note
  - artifact.architecture_decision_record
method_tags:
  - method.risk_review
  - method.handoff_review
metric_tags:
  - metric.plan_volatility
risk_tags:
  - risk.architecture_misalignment
activated_capability_ids:
  - cap.handoff_preparation
  - cap.technical_risk_assessment
  - cap.decision_record_writing
activated_knowledge_area_ids:
  - know.security_constraints
  - know.delivery_governance
  - know.non_functional_requirements
input_signals:
  - security or compliance review changed the design boundary
  - approval or control interpretation is the primary blocker
  - engineering needs a target review question, not another internal debate
expected_outputs:
  - governance-oriented handoff note
  - explicit control question and impacted design area
  - unblock criteria for architecture or execution work
escalation_triggers:
  - product policy decisions must also be revisited
  - operability consequences require deployment and operations review
example_prompt: Security review changed the auth design and we need to hand the decision to governance with the right context.
priority: high
confidence: high
```

## Retrieval Notes

- Use when control interpretation or approval ownership, not technical creativity, is blocking progress.
- Frame the question tightly enough that the receiving role can make a decision.
