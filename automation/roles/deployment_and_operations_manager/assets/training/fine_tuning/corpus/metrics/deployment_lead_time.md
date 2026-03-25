# Metric Card: Deployment Lead Time

```yaml
id: metric.deployment_lead_time
metric_name: Deployment lead time
definition: The elapsed time between the release package becoming operationally ready for deployment and the rollout completing in the target environment.
formula_or_logic: rollout_completed_at - release_ready_for_deployment_at
owner: Deployment and operations owner with release-manager oversight
data_source:
  - release calendar
  - change records
  - deployment execution logs
baseline_needed: Use a rolling median by release type so teams can distinguish healthy release cadence from avoidable coordination drag.
leading_or_lagging: Leading for delivery predictability and lagging for release execution efficiency.
anti_patterns:
  - starting the clock before upstream blockers or gate inputs are resolved
  - counting aborted or intentionally paused rollouts as completed
  - mixing internal dry runs with production deployments
interpretation_notes:
  - read with rollout coordination risk to distinguish healthy pauses from unmanaged drift
  - shorter lead time is only good when rollback readiness and support ownership remain explicit
```

## Related Artifacts

- `artifact.rollout_plan`

## Related Risks

- `risk.rollout_coordination_drift`
- `risk.support_ownership_gap`
