# Structured Mesh Case: Security Boundary Review

```yaml
id: mesh.security.boundary_review
stakeholder_group_id: stake.quality_security_governance
interaction_id: int.security_review
phase_tags:
  - define
  - plan
  - deliver
artifact_tags:
  - artifact.security_review_note
method_tags:
  - method.boundary_analysis
  - method.risk_review
  - method.evidence_review
metric_tags:
  - metric.remediation_lead_time
  - metric.evidence_coverage
risk_tags:
  - risk.security_boundary_drift
  - risk.evidence_gap
activated_capability_ids:
  - cap.security_boundary_analysis
  - cap.control_mapping
  - cap.evidence_assessment
  - cap.risk_assessment
activated_knowledge_area_ids:
  - know.security_constraints
  - know.system_boundaries
  - know.control_frameworks
input_signals:
  - the request changes identity, access, data flow, or trust boundaries
  - security questions are about controls and residual risk, not feature scope
expected_outputs:
  - security review note with concrete boundary risks
  - evidence gaps and required follow-up
escalation_triggers:
  - the control question depends on missing business rules
  - a system-boundary decision is still unresolved
example_prompt: Assess the auth-token sharing change and required security controls.
priority: core
confidence: high
```

## Retrieval Notes

- Use when a change crosses or reshapes a security-sensitive boundary and the assistant must reason about controls, risks, and follow-up.
