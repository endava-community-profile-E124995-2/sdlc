# Metric Card: Dependency Burn-Down Rate

```yaml
id: metric.dependency_burn_down_rate
metric_name: Dependency burn-down rate
definition: The share of critical implementation dependencies resolved by a given checkpoint in the engineering plan.
formula_or_logic: resolved_critical_dependencies / total_critical_dependencies_in_plan
owner: Engineering manager or technical program owner
data_source:
  - execution plan tracker
  - dependency review notes
  - delivery board status
baseline_needed: A baseline from recent work of similar size so late dependency resolution is visible before schedule slip becomes obvious.
leading_or_lagging: Leading because unresolved dependencies usually predict schedule volatility and integration risk.
anti_patterns:
  - counting unknown dependencies as non-critical
  - marking dependencies resolved before contract, access, or owner confirmation exists
  - tracking only external dependencies and ignoring cross-team internal blockers
interpretation_notes:
  - read together with integration risk and handoff notes
  - a high burn-down rate is weak if validation or operations handoffs are still unresolved
```

## Related Artifacts

- `artifact.engineering_execution_plan`
- `artifact.cross_role_handoff_note`

## Related Risks

- `risk.integration_overrun`
- `risk.handoff_loss`
