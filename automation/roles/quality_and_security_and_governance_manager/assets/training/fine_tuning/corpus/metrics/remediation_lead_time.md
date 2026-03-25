# Metric Card: Remediation Lead Time

```yaml
id: metric.remediation_lead_time
metric_name: Remediation lead time
definition: The elapsed time between a material review finding being raised and the agreed remediation being implemented or formally accepted as an exception.
formula_or_logic: remediation_resolution_date - finding_open_date
owner: Security lead or engineering manager for the affected scope
data_source:
  - review findings log
  - issue tracker
  - exception register
baseline_needed: A rolling median by severity or control family so slow paths can be distinguished from normal approval cycles.
leading_or_lagging: Leading for release risk because long remediation cycles often delay safe release decisions.
anti_patterns:
  - closing findings administratively without a real remediation or exception
  - starting the clock before the finding is scoped enough to act on
  - comparing unrelated severities as if they had the same expected timeline
interpretation_notes:
  - pair with evidence coverage to separate slow remediation from missing review inputs
  - long lead time can be legitimate when architecture changes are required
```

## Related Artifacts

- `artifact.security_review_note`
- `artifact.governance_mapping_note`

## Related Risks

- `risk.security_boundary_drift`
- `risk.evidence_gap`
