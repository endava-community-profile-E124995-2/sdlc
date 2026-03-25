# Risk Card: Verification Gap

```yaml
id: risk.verification_gap
risk_name: Verification gap
definition: The planned or available validation evidence is too weak to support confidence in the reviewed change scope.
trigger_signals:
  - critical paths are described but not mapped to explicit tests
  - known failure modes have no named validation approach
  - the recommendation relies on planned testing rather than completed evidence
impact_area:
  - release quality
  - regression risk
  - confidence in review outcome
likelihood_notes: Likelihood rises when execution plans mention testing as a phase but do not tie it to concrete risk areas.
mitigation_actions:
  - identify missing validation evidence explicitly
  - require targeted tests or checkpoints for the highest-risk paths
  - hand off to product or architecture when the missing validation target depends on unresolved intent or design
escalation_path:
  - escalate to product when missing business rules change what must be validated
  - escalate to architecture when the test target depends on unresolved system boundaries
related_metric_ids:
  - metric.defect_escape_rate
  - metric.evidence_coverage
```

## Common Failure Mode

Teams describe a broad test phase and call the plan sufficient even though the riskiest failure paths remain untested.
