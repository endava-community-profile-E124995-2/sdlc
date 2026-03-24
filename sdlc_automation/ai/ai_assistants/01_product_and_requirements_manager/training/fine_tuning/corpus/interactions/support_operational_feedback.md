# Structured Mesh Case: Support Operational Feedback

```yaml
id: mesh.support.operational_feedback
stakeholder_group_id: stake.support_operations
interaction_id: int.operational_improvement
phase_tags:
  - deliver
  - launch
  - learn
artifact_tags:
  - artifact.risk_review
  - artifact.post_launch_review
  - artifact.roadmap_item
method_tags:
  - method.premortem
  - method.workflow_mapping
metric_tags:
  - metric.defect_escape_rate
  - metric.customer_satisfaction
risk_tags:
  - risk.support_burden_spike
  - risk.missing_instrumentation
activated_capability_ids:
  - cap.support_issue_analysis
  - cap.risk_assessment
  - cap.risk_mitigation_planning
  - cap.workflow_mapping
  - cap.feedback_synthesis
activated_knowledge_area_ids:
  - know.release_governance
  - know.customer_workflows
input_signals:
  - support volume spikes after release
  - incident or defect patterns suggest product or rollout gaps
  - operations teams rely on manual workarounds
expected_outputs:
  - issue pattern summary
  - improvement recommendation with priority rationale
  - launch or support-readiness actions
escalation_triggers:
  - incident severity indicates a release or governance failure
  - manual workarounds create material operational risk
example_prompt: Support volume spiked after release and operations is relying on workarounds. Summarize the likely product issues and what we should do next.
priority: high
confidence: high
```

## Retrieval Notes

- Use when support and operations signals need to become product decisions.
- Prefer this case over a generic bug triage framing when the issue is systemic and cross-functional.
