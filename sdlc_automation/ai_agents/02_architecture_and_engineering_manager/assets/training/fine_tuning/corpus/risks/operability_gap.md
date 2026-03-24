# Risk Card: Operability Gap

```yaml
id: risk.operability_gap
risk_name: Operability gap
definition: The implementation path is technically viable, but release safety, observability, rollback, or support readiness is not prepared for runtime ownership.
trigger_signals:
  - dashboards, alerts, or runbooks are still undefined near release
  - rollback expectations exist only in engineering discussion
  - support teams have no clear operational boundary or escalation path
impact_area:
  - release safety
  - incident response
  - support burden
likelihood_notes: Likelihood rises when engineering plans treat runtime readiness as an afterthought instead of an owned handoff.
mitigation_actions:
  - identify required operational artifacts early in the execution plan
  - hand off explicit rollout, observability, rollback, and support requirements to deployment and operations
  - verify readiness before release candidates are treated as shippable
escalation_path:
  - escalate to deployment and operations ownership when runtime readiness is the primary blocker
  - return to product when supportability requires scope reduction or phased rollout changes
related_metric_ids:
  - metric.operability_readiness
  - metric.dependency_burn_down_rate
```

## Common Failure Mode

Teams call the feature done because code is merged even though the runtime organization cannot safely operate it.
