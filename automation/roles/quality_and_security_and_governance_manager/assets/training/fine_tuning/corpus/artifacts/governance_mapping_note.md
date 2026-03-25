# Artifact Contract: Governance Mapping Note

```yaml
id: artifact.governance_mapping_note
artifact_name: Governance Mapping Note
purpose: Trace a control or policy requirement to affected behavior, known evidence, missing evidence, and the decisions or approvals still required.
required_sections:
  - control_or_policy_source
  - affected_behavior
  - evidence_status
  - approval_or_exception_questions
  - risks_and_escalation_points
  - recommended_next_step
optional_sections:
  - traceability_notes
  - dependency_notes
  - assumption_log
minimum_quality_bar: A serious governance mapping note names the source control, what behavior it affects, what evidence exists, what approvals or exceptions are open, and what needs to happen next.
common_failure_modes:
  - policy names are dropped without mapping them to behavior
  - evidence is described as sufficient without showing what exists
  - approval questions are left implicit
  - the next step ignores which role actually owns the unresolved decision
good_example_ref: corpus/examples/governance_mapping_note_good_release_controls.md
bad_example_ref: corpus/examples/governance_mapping_note_bad_policy_name_drop.md
```

## Template

1. Control or policy source
2. Affected behavior
3. Evidence status
4. Approval or exception questions
5. Risks and escalation points
6. Recommended next step
