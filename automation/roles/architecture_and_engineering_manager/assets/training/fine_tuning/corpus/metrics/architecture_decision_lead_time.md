# Metric Card: Architecture Decision Lead Time

```yaml
id: metric.architecture_decision_lead_time
metric_name: Architecture decision lead time
definition: The elapsed time between a well-scoped architecture question entering planning and a documented decision being published.
formula_or_logic: decision_publish_date - decision_ready_date
owner: Architecture lead or engineering manager
data_source:
  - architecture backlog
  - ADR repository
  - planning board timestamps
baseline_needed: A rolling median from recent comparable decisions so teams can distinguish normal review time from avoidable delay.
leading_or_lagging: Leading for delivery predictability because delayed design decisions usually delay implementation sequencing.
anti_patterns:
  - starting the clock before the decision question is scoped
  - calling verbal alignment a published decision
  - hiding blocked decisions outside the tracked queue
interpretation_notes:
  - read together with plan volatility to separate healthy debate from churn
  - a shorter lead time is only good when trade-offs and impacts are still documented
```

## Related Artifacts

- `artifact.technical_feasibility_brief`
- `artifact.architecture_decision_record`

## Related Risks

- `risk.architecture_misalignment`
- `risk.integration_overrun`
