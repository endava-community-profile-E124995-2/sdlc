# Structured Mesh Case: Release Gate Assessment

```yaml
id: mesh.release.gate_assessment
stakeholder_group_id: stake.quality_security_governance
interaction_id: int.release_gate_assessment
phase_tags:
  - launch
  - govern
artifact_tags:
  - artifact.release_gate_memo
method_tags:
  - method.gate_decision_review
  - method.evidence_review
  - method.exception_review
metric_tags:
  - metric.gate_decision_lead_time
  - metric.evidence_coverage
risk_tags:
  - risk.gate_readiness_blind_spot
  - risk.evidence_gap
activated_capability_ids:
  - cap.release_gate_evaluation
  - cap.evidence_assessment
  - cap.exception_framing
  - cap.approval_gap_detection
activated_knowledge_area_ids:
  - know.release_governance
  - know.evidence_requirements
  - know.operability_expectations
  - know.exception_management
input_signals:
  - the team needs a pass, pause, or block recommendation for a named release boundary
  - evidence, exceptions, or blockers are still in motion
expected_outputs:
  - release gate memo with an explicit decision
  - blockers, evidence status, and unblock criteria
escalation_triggers:
  - rollout readiness belongs to deployment and operations
  - the gate question depends on missing product or architecture decisions
example_prompt: Should we ship on Friday given these blockers and missing approvals?
priority: core
confidence: high
```

## Retrieval Notes

- Use when a release boundary exists and the main task is to make the current gate recommendation explicit.
