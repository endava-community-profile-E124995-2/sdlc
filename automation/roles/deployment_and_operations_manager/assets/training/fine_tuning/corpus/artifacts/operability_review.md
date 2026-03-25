# Artifact Contract: Operability Review

```yaml
id: artifact.operability_review
artifact_name: Operability Review
purpose: Make runtime readiness explicit by reviewing monitoring, rollback, runbooks, and support ownership for a scoped release or service change.
required_sections:
  - runtime_scope_reviewed
  - readiness_expectations
  - monitoring_and_alerting_status
  - runbook_and_support_ownership_status
  - gaps_and_risks
  - recommendation
optional_sections:
  - reviewed_evidence
  - release_window_notes
  - required_handoffs
minimum_quality_bar: A serious operability review states what was reviewed, what readiness bar applies, what is ready or missing, and whether the current operating posture is adequate.
common_failure_modes:
  - the review lists tools without saying whether they are sufficient
  - runbook and ownership status are missing or implied
  - the note drifts into gate approval instead of naming the quality handoff
  - runtime design blockers are described without naming architecture as the owner
good_example_ref: corpus/examples/operability_review_good_prelaunch_readiness.md
bad_example_ref: corpus/examples/operability_review_bad_checkboxes_only.md
```

## Template

1. Runtime scope reviewed
2. Readiness expectations
3. Monitoring and alerting status
4. Runbook and support ownership status
5. Gaps and risks
6. Recommendation
