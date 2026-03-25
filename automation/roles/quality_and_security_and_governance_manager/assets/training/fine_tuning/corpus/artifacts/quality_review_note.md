# Artifact Contract: Quality Review Note

```yaml
id: artifact.quality_review_note
artifact_name: Quality Review Note
purpose: Assess whether the planned validation approach, evidence, and quality expectations are strong enough for the current change scope.
required_sections:
  - scope_reviewed
  - quality_expectations
  - evidence_reviewed
  - major_risks_and_validation_gaps
  - recommendation
  - required_handoffs_or_unblockers
optional_sections:
  - validation_checkpoints
  - assumption_log
  - release_impact
minimum_quality_bar: A serious review note names the scope, expected quality bar, evidence reviewed, the main validation gaps, the recommendation, and any required handoff.
common_failure_modes:
  - quality expectations are generic and not tied to the change scope
  - evidence is implied but not named
  - risks are listed without explaining why they change the recommendation
  - the note stops at warnings and never says what must happen next
good_example_ref: corpus/examples/quality_review_note_good_execution_plan.md
bad_example_ref: corpus/examples/quality_review_note_bad_checklist_only.md
```

## Template

1. Scope reviewed
2. Quality expectations
3. Evidence reviewed
4. Major risks and validation gaps
5. Recommendation
6. Required handoffs or unblockers
