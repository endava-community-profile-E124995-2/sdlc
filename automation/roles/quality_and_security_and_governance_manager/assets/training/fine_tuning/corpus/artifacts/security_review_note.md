# Artifact Contract: Security Review Note

```yaml
id: artifact.security_review_note
artifact_name: Security Review Note
purpose: Assess whether a proposed change respects the intended security boundary, controls, and residual-risk posture.
required_sections:
  - boundary_reviewed
  - threat_and_control_context
  - identified_risks
  - evidence_and_gap_status
  - required_follow_up
  - escalation_points
  - recommendation
optional_sections:
  - assumptions
  - exception_candidates
  - dependency_notes
minimum_quality_bar: A serious security review note names the reviewed boundary, the control context, the concrete risks, the available evidence, the required follow-up, and the recommendation.
common_failure_modes:
  - security concerns are generic and not tied to a specific boundary
  - control expectations are implied instead of named
  - missing evidence is hidden behind vague mitigation language
  - the note acts as approval even though open risks or questions remain
good_example_ref: corpus/examples/security_review_note_good_token_boundary.md
bad_example_ref: corpus/examples/security_review_note_bad_generic_warning.md
```

## Template

1. Boundary reviewed
2. Threat and control context
3. Identified risks
4. Evidence and gap status
5. Required follow-up
6. Escalation points
7. Recommendation
