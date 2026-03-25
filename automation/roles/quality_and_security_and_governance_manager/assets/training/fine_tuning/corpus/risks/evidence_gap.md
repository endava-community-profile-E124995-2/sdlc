# Risk Card: Evidence Gap

```yaml
id: risk.evidence_gap
risk_name: Evidence gap
definition: A recommendation or mapping is being made without enough current, traceable evidence to justify the conclusion.
trigger_signals:
  - required documents or test outputs are missing, stale, or unlinked
  - exception handling is implied instead of documented
  - the review makes strong claims while evidence status remains vague
impact_area:
  - approval quality
  - traceability
  - audit readiness
likelihood_notes: Likelihood rises when teams optimize for quick approval language instead of explicit evidence handling.
mitigation_actions:
  - inventory required evidence for the current scope
  - distinguish missing evidence from future planned evidence
  - require either the evidence itself or a documented exception path before approval language is used
escalation_path:
  - escalate to quality, security, and governance ownership when evidence sufficiency is the main blocker
  - escalate to product, architecture, or deployment when they own the missing input
related_metric_ids:
  - metric.evidence_coverage
  - metric.gate_decision_lead_time
```

## Common Failure Mode

Review notes imply confidence because the team intends to gather evidence later.
