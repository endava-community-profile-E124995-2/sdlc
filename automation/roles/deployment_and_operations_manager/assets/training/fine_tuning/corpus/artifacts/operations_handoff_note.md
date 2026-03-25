# Artifact Contract: Operations Handoff Note

```yaml
id: artifact.operations_handoff_note
artifact_name: Operations Handoff Note
purpose: Transfer runtime context, ownership expectations, and open risks to the receiving support or operations function for a scoped release or incident path.
required_sections:
  - handoff_trigger_and_release_context
  - receiving_owner_or_team
  - known_facts_and_current_state
  - required_runbooks_dashboards_or_access
  - open_risks_and_pending_actions
  - acceptance_or_unblock_criteria
optional_sections:
  - communication_contacts
  - escalation_path
  - review_window
minimum_quality_bar: A serious handoff note names the receiving owner, current state, required runtime materials, remaining risks, and what must happen before the handoff is accepted.
common_failure_modes:
  - the note names work but not the receiving owner
  - open risks are listed without an action or acceptance condition
  - dashboards or runbooks are referenced without saying whether they already exist
  - the note assumes support will infer escalation paths
good_example_ref: corpus/examples/operations_handoff_note_good_support_transition.md
bad_example_ref: corpus/examples/operations_handoff_note_bad_no_owner.md
```

## Template

1. Handoff trigger and release context
2. Receiving owner or team
3. Known facts and current state
4. Required runbooks, dashboards, or access
5. Open risks and pending actions
6. Acceptance or unblock criteria
