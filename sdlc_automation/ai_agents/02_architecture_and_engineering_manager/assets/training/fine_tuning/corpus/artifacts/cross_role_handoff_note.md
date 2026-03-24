# Artifact Contract: Cross-Role Handoff Note

```yaml
id: artifact.cross_role_handoff_note
artifact_name: Cross-role handoff note
purpose: Move unresolved work to the correct SDLC role without losing technical context, constraints, or unblock criteria.
required_sections:
  - target_role
  - trigger_for_handoff
  - known_facts_and_constraints
  - open_questions_or_unresolved_decisions
  - requested_action
  - unblock_criteria
optional_sections:
  - supporting_artifacts
  - timeline_pressure
  - risk_if_delayed
minimum_quality_bar: A serious handoff note names the receiving role, why the handoff is required, what is already known, what remains unresolved, and how work can resume.
common_failure_modes:
  - the target role is implied rather than stated
  - facts and assumptions are mixed together
  - the requested action is vague
  - unblock criteria are missing
good_example_ref: corpus/examples/cross_role_handoff_note_good_security_boundary.md
bad_example_ref: corpus/examples/cross_role_handoff_note_bad_vague_escalation.md
```

## Template

1. Target role
2. Trigger for handoff
3. Known facts and constraints
4. Open questions or unresolved decisions
5. Requested action
6. Unblock criteria
