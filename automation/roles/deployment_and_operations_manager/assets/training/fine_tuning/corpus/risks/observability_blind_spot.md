# Risk Card: Observability Blind Spot

```yaml
id: risk.observability_blind_spot
risk_name: Observability blind spot
definition: A change reaches production without enough dashboards, alerts, or signal interpretation guidance to detect and explain runtime problems quickly.
trigger_signals:
  - the plan references logs but not actionable dashboards or alerts
  - post-release monitoring depends on ad hoc manual checking
  - on-call responders lack context for what good or bad looks like after rollout
impact_area:
  - incident detection
  - mean time to restore
  - support burden
likelihood_notes: Likelihood rises when monitoring is treated as a final checklist item rather than a first-class release dependency.
mitigation_actions:
  - define the critical signals, thresholds, and dashboards before rollout
  - document how to interpret the first release window and what actions follow key signals
  - confirm the receiving on-call or support owner can use the monitoring surface
escalation_path:
  - escalate to architecture when required telemetry depends on unresolved system changes
  - escalate to product when missing monitoring reflects unclear success or blast-radius assumptions
related_metric_ids:
  - metric.operability_readiness
  - metric.incident_restore_time
```

## Common Failure Mode

The release is live, but the team cannot tell quickly whether user impact is growing, stable, or already resolved.
