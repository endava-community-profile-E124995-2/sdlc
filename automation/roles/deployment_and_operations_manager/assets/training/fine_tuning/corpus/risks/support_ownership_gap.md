# Risk Card: Support Ownership Gap

```yaml
id: risk.support_ownership_gap
risk_name: Support ownership gap
definition: A release is handed over without a clear receiving team, escalation path, or runtime boundary for who handles incidents and follow-up work.
trigger_signals:
  - the handoff note names no receiving owner or acceptance condition
  - support expectations differ between engineering, release, and on-call teams
  - incident responders lack access, runbooks, or escalation contacts for the change
impact_area:
  - incident response
  - customer support quality
  - accountability
likelihood_notes: Likelihood rises when releases span teams and environments but ownership is implied instead of formally handed over.
mitigation_actions:
  - identify the receiving owner and acceptance criteria in the handoff note
  - list required dashboards, runbooks, access, and escalation paths explicitly
  - use operational follow-up to confirm ownership held through the first release window
escalation_path:
  - escalate to product when support posture depends on phased rollout or enablement decisions
  - escalate to quality when release pressure is trying to bypass unresolved ownership gaps
related_metric_ids:
  - metric.operability_readiness
  - metric.incident_restore_time
```

## Common Failure Mode

Everyone assumes someone else will respond when the release misbehaves, and the first incident exposes the gap.
