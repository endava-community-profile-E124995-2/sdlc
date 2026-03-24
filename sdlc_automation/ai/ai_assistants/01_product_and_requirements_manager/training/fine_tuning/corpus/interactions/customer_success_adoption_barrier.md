# Structured Mesh Case: Customer Success Adoption Barrier

```yaml
id: mesh.customer_success.adoption_barrier
stakeholder_group_id: stake.customer_success
interaction_id: int.adoption_planning
phase_tags:
  - launch
  - learn
artifact_tags:
  - artifact.launch_brief
  - artifact.post_launch_review
method_tags:
  - method.customer_interviews
  - method.workflow_mapping
metric_tags:
  - metric.adoption_rate
  - metric.retention_rate
  - metric.customer_satisfaction
risk_tags:
  - risk.adoption_risk
  - risk.support_burden_spike
activated_capability_ids:
  - cap.feedback_synthesis
  - cap.adoption_barrier_analysis
  - cap.training_needs_identification
  - cap.rollout_planning
  - cap.outcome_review_facilitation
activated_knowledge_area_ids:
  - know.customer_workflows
  - know.product_analytics
input_signals:
  - customer success reports confusion, workarounds, or low habit formation
  - onboarding completion and repeat usage are weak
  - enablement gaps are affecting adoption
expected_outputs:
  - adoption barrier summary
  - rollout or enablement adjustments
  - post-launch learning actions tied to metrics
escalation_triggers:
  - retention impact suggests a broader product-value gap
  - rollout risk materially exceeds support capacity
example_prompt: Customer Success says users are not adopting the new workflow after launch. Diagnose the likely barriers and recommend next actions.
priority: high
confidence: high
```

## Retrieval Notes

- Use when the problem is post-launch value realization, not initial requirement drafting.
- Tie recommendations to measurable adoption signals and user workflow friction.
