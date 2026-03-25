# Metric Card: Defect Escape Rate

```yaml
id: metric.defect_escape_rate
metric_name: Defect escape rate
definition: The rate at which defects tied to the reviewed change scope are discovered after the review or release gate said the change was acceptable.
formula_or_logic: post_release_defects_for_scope / total_released_changes_in_scope
owner: Quality lead or engineering quality owner
data_source:
  - defect tracker
  - release records
  - incident review notes
baseline_needed: A rolling baseline for comparable change types so teams can distinguish normal noise from weak verification.
leading_or_lagging: Lagging because it measures missed issues after release.
anti_patterns:
  - mixing unrelated incidents into the reviewed scope
  - using raw defect counts without normalizing for release volume
  - blaming the metric on teams without checking evidence quality first
interpretation_notes:
  - read with evidence coverage to distinguish weak review inputs from execution mistakes
  - a short-term spike after better detection does not always mean review quality worsened
```

## Related Artifacts

- `artifact.quality_review_note`
- `artifact.release_gate_memo`

## Related Risks

- `risk.verification_gap`
- `risk.gate_readiness_blind_spot`
