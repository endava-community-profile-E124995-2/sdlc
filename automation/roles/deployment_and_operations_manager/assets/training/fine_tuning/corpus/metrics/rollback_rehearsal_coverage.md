# Metric Card: Rollback Rehearsal Coverage

```yaml
id: metric.rollback_rehearsal_coverage
metric_name: Rollback rehearsal coverage
definition: The share of scoped releases whose rollback steps were reviewed or rehearsed against the current deployment path before launch.
formula_or_logic: rehearsed_or_reviewed_release_count / total_scoped_release_count
owner: Deployment and operations owner with release-manager oversight
data_source:
  - rollback drill records
  - release checklist
  - change management notes
baseline_needed: Compare against recent releases with similar blast radius so teams can tell whether rollback readiness is improving or slipping.
leading_or_lagging: Leading for release resilience because weak rollback preparation increases time to recover when changes misbehave.
anti_patterns:
  - counting stale rollback documents as rehearsal evidence
  - treating engineering discussion as equivalent to a reviewed rollback path
  - excluding partial rollouts or canary reversals from the denominator
interpretation_notes:
  - read with operability readiness because rollback can be documented yet still unsupported operationally
  - low coverage is acceptable only when the change is demonstrably reversible without a special path
```

## Related Artifacts

- `artifact.rollout_plan`
- `artifact.operations_handoff_note`

## Related Risks

- `risk.rollback_readiness_gap`
