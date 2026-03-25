# Structured Mesh Case: Operability Review

```yaml
id: mesh.operations.operability_review
stakeholder_group_id: stake.deployment_operations
interaction_id: int.operability_review
phase_tags:
  - launch
  - learn
artifact_tags:
  - artifact.operability_review
method_tags:
  - method.readiness_review
  - method.observability_gap_analysis
  - method.rollback_check
metric_tags:
  - metric.operability_readiness
  - metric.rollback_rehearsal_coverage
risk_tags:
  - risk.rollback_readiness_gap
  - risk.observability_blind_spot
  - risk.support_ownership_gap
activated_capability_ids:
  - cap.observability_review
  - cap.rollback_readiness_assessment
  - cap.runbook_preparation
  - cap.operational_risk_assessment
activated_knowledge_area_ids:
  - know.operability_expectations
  - know.observability_requirements
  - know.runbook_quality
  - know.support_ownership
input_signals:
  - dashboards, alerts, runbooks, or on-call ownership need a readiness review before launch
  - release safety depends on runtime controls outside the code change itself
  - the team needs a clear readiness call on whether operations can safely receive the change
expected_outputs:
  - operability review with concrete readiness gaps and recommendation
  - explicit owner or handoff callout when the blocker belongs elsewhere
escalation_triggers:
  - ship or no-ship approval still belongs to quality
  - runtime readiness depends on unresolved architecture boundaries
example_prompt: Review whether dashboards, alerts, runbooks, and on-call ownership are ready before launch.
priority: core
confidence: high
```

## Retrieval Notes

- Use when the primary task is to evaluate operational readiness, not to write the full release sequence.
