# Structured Mesh Case: Compliance Requirement Mapping

```yaml
id: mesh.grc.compliance_requirement_mapping
stakeholder_group_id: stake.grc
interaction_id: int.governance_approval
phase_tags:
  - define
  - govern
artifact_tags:
  - artifact.prd
  - artifact.risk_review
  - artifact.requirement_change_log
method_tags:
  - method.workflow_mapping
  - method.option_analysis
metric_tags:
  - metric.requirement_rework_rate
risk_tags:
  - risk.compliance_exposure
  - risk.ambiguous_requirements
activated_capability_ids:
  - cap.business_rule_identification
  - cap.traceable_requirement_writing
  - cap.risk_assessment
  - cap.change_control
  - cap.cross_functional_communication
activated_knowledge_area_ids:
  - know.compliance_requirements
  - know.approval_governance
  - know.security_constraints
input_signals:
  - legal or compliance stakeholders ask how a policy requirement maps into product behavior
  - approval depends on documented traceability and change rationale
  - the team is unsure whether a rule is functional, non-functional, or operational
expected_outputs:
  - traceable requirement mapping
  - identified policy-driven constraints
  - explicit approval questions and risk notes
escalation_triggers:
  - legal interpretation remains ambiguous
  - a compliance requirement materially changes scope, timing, or rollout posture
example_prompt: Translate these privacy and auditability requirements into product requirements we can review with compliance and engineering.
priority: core
confidence: high
```

## Retrieval Notes

- Use when controls, approvals, or policy mapping are part of the task.
- Do not use this case to replace legal or compliance judgment.
