# Risk Card: Handoff Loss

```yaml
id: risk.handoff_loss
risk_name: Handoff loss
definition: Critical context, assumptions, or unblock criteria are lost when work moves between roles or teams.
trigger_signals:
  - downstream owners ask questions already answered earlier
  - open decisions are implied instead of listed
  - release or governance blockers reappear because the receiving role lacks context
impact_area:
  - coordination
  - schedule
  - decision quality
likelihood_notes: Likelihood rises when handoffs are verbal, partial, or mixed with implementation chatter instead of one explicit artifact.
mitigation_actions:
  - create one handoff note with facts, open questions, and unblock criteria
  - link the handoff to the relevant feasibility brief, ADR, or execution plan
  - identify the receiving role and requested action explicitly
escalation_path:
  - escalate to the originating role owner when the handoff note is incomplete
  - involve the receiving role owner when unblock criteria are missing or disputed
related_metric_ids:
  - metric.plan_volatility
  - metric.operability_readiness
```

## Common Failure Mode

Teams treat this as a communication issue when the real problem is that ownership and unblock criteria were never made explicit.
