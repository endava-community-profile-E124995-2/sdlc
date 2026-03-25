# Risk Card: Gate Readiness Blind Spot

```yaml
id: risk.gate_readiness_blind_spot
risk_name: Gate readiness blind spot
definition: The release path appears close to ready, but a key evidence, exception, or operational dependency is missing from the gate decision.
trigger_signals:
  - the release plan assumes approval before blockers are closed
  - rollback or support readiness is still unresolved near release
  - gate language is vague about what specifically blocks shipment
impact_area:
  - release safety
  - change governance
  - support readiness
likelihood_notes: Likelihood rises when release pressure encourages teams to compress evidence review, exception framing, and operational handoffs into a single late-stage conversation.
mitigation_actions:
  - make the gate scope and recommendation explicit
  - list blockers, evidence status, and required handoffs separately
  - hand operational readiness work to deployment while keeping the gate decision explicit
escalation_path:
  - escalate to deployment and operations when runtime readiness is the unblock path
  - escalate to product or architecture when the gate is blocked by unresolved upstream decisions
related_metric_ids:
  - metric.gate_decision_lead_time
  - metric.evidence_coverage
```

## Common Failure Mode

Teams treat a release as nearly approved even though no one has stated the current no-ship condition.
