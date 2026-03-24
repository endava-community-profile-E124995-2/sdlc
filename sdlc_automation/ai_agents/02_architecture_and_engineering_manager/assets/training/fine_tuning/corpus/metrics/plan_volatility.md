# Metric Card: Plan Volatility

```yaml
id: metric.plan_volatility
metric_name: Plan volatility
definition: The rate at which committed workstreams, dependency order, or target interfaces change after an execution plan is published.
formula_or_logic: material_plan_changes / planning_period
owner: Engineering manager
data_source:
  - execution plan revisions
  - change log
  - sprint or milestone planning records
baseline_needed: A recent baseline helps distinguish healthy refinement from churn caused by weak design inputs.
leading_or_lagging: Leading for delivery instability.
anti_patterns:
  - treating untracked verbal changes as zero volatility
  - counting routine status updates as material scope change
  - using volatility alone without checking why changes occurred
interpretation_notes:
  - high volatility can reflect missing product inputs, weak architecture decisions, or unmanaged dependency changes
  - pair with handoff and architecture metrics before assigning blame
```

## Related Risks

- `risk.handoff_loss`
- `risk.architecture_misalignment`
