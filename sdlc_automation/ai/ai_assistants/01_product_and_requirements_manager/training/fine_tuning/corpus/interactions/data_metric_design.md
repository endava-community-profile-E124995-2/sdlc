# Structured Mesh Case: Data Metric Design

```yaml
id: mesh.data.metric_design
stakeholder_group_id: stake.data_analytics
interaction_id: int.outcome_review
phase_tags:
  - define
  - learn
artifact_tags:
  - artifact.kpi_spec
  - artifact.post_launch_review
method_tags:
  - method.experiment_design
  - method.option_analysis
metric_tags:
  - metric.adoption_rate
  - metric.activation_rate
  - metric.retention_rate
risk_tags:
  - risk.missing_instrumentation
activated_capability_ids:
  - cap.outcome_definition
  - cap.outcome_review_facilitation
  - cap.decision_framing
  - cap.cross_functional_communication
activated_knowledge_area_ids:
  - know.product_analytics
  - know.event_instrumentation
  - know.experimentation
input_signals:
  - the team has a goal but no precise success metric
  - instrumentation feasibility is unclear
  - stakeholders are using vanity metrics as proof of value
expected_outputs:
  - KPI spec with metric definitions and baselines
  - instrumentation questions and gaps
  - recommendation on leading and lagging measures
escalation_triggers:
  - no trustworthy data source exists
  - metric definition would mislead decision-making without additional event work
example_prompt: Define success metrics for this launch and tell us what instrumentation we are missing before we commit to them.
priority: high
confidence: high
```

## Retrieval Notes

- Use when the task is metric definition, KPI cleanup, or post-launch interpretation.
- Prefer this case over generic analytics discussion when the user needs measurement decisions.
