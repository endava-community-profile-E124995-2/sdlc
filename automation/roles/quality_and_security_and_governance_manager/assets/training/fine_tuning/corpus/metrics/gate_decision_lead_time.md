# Metric Card: Gate Decision Lead Time

```yaml
id: metric.gate_decision_lead_time
metric_name: Gate decision lead time
definition: The elapsed time between a release boundary becoming ready for review and a documented gate recommendation being published.
formula_or_logic: gate_recommendation_publish_date - gate_ready_for_review_date
owner: Quality, security, and governance review owner
data_source:
  - release calendar
  - gate review queue
  - decision records
baseline_needed: A rolling median from recent comparable release boundaries so teams can separate healthy review from avoidable queue delay.
leading_or_lagging: Leading for release predictability because delayed gate decisions often delay release planning and exception handling.
anti_patterns:
  - starting the clock before the release scope is stable enough to review
  - treating informal verbal guidance as a documented recommendation
  - hiding blocked reviews outside the tracked queue
interpretation_notes:
  - read with evidence coverage to distinguish slow review from incomplete inputs
  - shorter lead time is only good when blockers and exceptions are still made explicit
```

## Related Artifacts

- `artifact.release_gate_memo`
- `artifact.governance_mapping_note`

## Related Risks

- `risk.gate_readiness_blind_spot`
- `risk.evidence_gap`
