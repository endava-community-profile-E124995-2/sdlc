# Metric Card: Evidence Coverage

```yaml
id: metric.evidence_coverage
metric_name: Evidence coverage
definition: The share of required review inputs for a given scope that are present, current, and traceable when the recommendation is made.
formula_or_logic: current_traceable_required_evidence_items / total_required_evidence_items
owner: Quality, security, or governance reviewer for the active scope
data_source:
  - review checklist
  - linked test or control evidence
  - exception register
baseline_needed: A baseline by review type so teams can compare quality reviews, security reviews, governance mapping, and release-gate decisions consistently.
leading_or_lagging: Leading because weak evidence coverage often predicts rework, exceptions, or delayed release decisions.
anti_patterns:
  - counting stale documents as current evidence
  - treating planned evidence as available evidence
  - claiming 100 percent coverage while unresolved exceptions still exist
interpretation_notes:
  - evidence coverage is only useful when the required evidence set is explicit
  - lower coverage can be acceptable only when the missing items are openly handled through a documented exception path
```

## Related Artifacts

- `artifact.quality_review_note`
- `artifact.security_review_note`
- `artifact.governance_mapping_note`
- `artifact.release_gate_memo`

## Related Risks

- `risk.evidence_gap`
- `risk.gate_readiness_blind_spot`
