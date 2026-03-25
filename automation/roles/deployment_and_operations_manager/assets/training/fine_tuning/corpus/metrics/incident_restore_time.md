# Metric Card: Incident Restore Time

```yaml
id: metric.incident_restore_time
metric_name: Incident restore time
definition: The elapsed time between a release-linked incident being recognized and service being restored to the agreed operating state.
formula_or_logic: service_restored_at - incident_recognized_at
owner: Incident commander or on-call operations owner
data_source:
  - incident timeline
  - paging system
  - status updates and recovery notes
baseline_needed: A baseline from comparable incident classes is required before claiming operational follow-up is improving recovery speed.
leading_or_lagging: Lagging for incident response health and leading for future runbook and rollback investment.
anti_patterns:
  - measuring from the first symptom when no one knew an incident existed yet
  - stopping the clock before user impact is actually resolved
  - averaging incomparable incident severities into one headline number
interpretation_notes:
  - read with follow-up notes to separate slow recovery from poor signal interpretation
  - long restore time may reflect rollback gaps, ownership confusion, or weak observability rather than one root cause
```

## Related Artifacts

- `artifact.operational_follow_up_note`

## Related Risks

- `risk.observability_blind_spot`
- `risk.support_ownership_gap`
