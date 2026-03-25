# Structured Mesh Case: Governance Control Mapping

```yaml
id: mesh.governance.control_mapping
stakeholder_group_id: stake.quality_security_governance
interaction_id: int.governance_mapping
phase_tags:
  - define
  - govern
artifact_tags:
  - artifact.governance_mapping_note
method_tags:
  - method.control_traceability
  - method.evidence_review
  - method.exception_review
metric_tags:
  - metric.evidence_coverage
risk_tags:
  - risk.evidence_gap
activated_capability_ids:
  - cap.control_mapping
  - cap.evidence_assessment
  - cap.approval_gap_detection
  - cap.exception_framing
activated_knowledge_area_ids:
  - know.control_frameworks
  - know.evidence_requirements
  - know.release_governance
  - know.exception_management
input_signals:
  - a control or policy must be mapped to concrete system behavior
  - the review needs traceability and missing-evidence framing
expected_outputs:
  - governance mapping note with traceable control coverage
  - explicit approval or exception questions
escalation_triggers:
  - the control implication depends on missing product rules
  - the remediation path depends on unresolved architecture boundaries
example_prompt: Map this release to the relevant controls and flag missing evidence or exception approvals.
priority: core
confidence: high
```

## Retrieval Notes

- Use when the work is primarily about traceability, evidence sufficiency, and unresolved approval or exception questions.
