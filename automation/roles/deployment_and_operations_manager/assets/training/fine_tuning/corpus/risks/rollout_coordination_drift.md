# Risk Card: Rollout Coordination Drift

```yaml
id: risk.rollout_coordination_drift
risk_name: Rollout coordination drift
definition: A rollout plan exists, but checkpoint timing, owner alignment, or dependency sequencing drifts enough that the release no longer matches the documented plan.
trigger_signals:
  - hold points move informally in chat instead of the plan
  - dependencies or approvals are assumed closed without explicit owner confirmation
  - the release window is compressed without updating communication or rollback expectations
impact_area:
  - release predictability
  - cross-team coordination
  - customer or internal user impact
likelihood_notes: Likelihood rises when release pressure encourages teams to treat the rollout plan as status prose instead of an operational control surface.
mitigation_actions:
  - update the rollout plan with explicit checkpoints, owners, and hold conditions
  - separate confirmed dependencies from assumptions
  - restate communication and rollback triggers whenever sequencing changes
escalation_path:
  - escalate to product when business rollout constraints or audience decisions are still moving
  - escalate to quality when gate or approval dependencies are the unresolved blocker
related_metric_ids:
  - metric.deployment_lead_time
```

## Common Failure Mode

Teams believe they are following the plan even though the real release sequence has changed enough to invalidate the original readiness assumptions.
