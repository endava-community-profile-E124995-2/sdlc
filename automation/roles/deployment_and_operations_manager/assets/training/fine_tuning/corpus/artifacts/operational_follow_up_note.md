# Artifact Contract: Operational Follow-up Note

```yaml
id: artifact.operational_follow_up_note
artifact_name: Operational Follow-up Note
purpose: Summarize the first production signals, anomalies, and next actions after a release or operating event.
required_sections:
  - review_window_and_signals
  - incidents_or_anomalies
  - impact_and_interpretation
  - follow_up_actions_and_owners
  - escalation_needs_or_handoffs
  - recommendation_or_next_checkpoint
optional_sections:
  - signal_confidence_notes
  - rollback_or_recovery_summary
  - unresolved_questions
minimum_quality_bar: A serious operational follow-up note states what window was reviewed, what signals or incidents appeared, how they are interpreted, and what concrete next actions follow.
common_failure_modes:
  - the note repeats metrics with no interpretation
  - anomalies are listed without impact or owner
  - follow-up is vague about timing or responsibility
  - the note claims stability even though the signal window is too weak
good_example_ref: corpus/examples/operational_follow_up_note_good_first_day_review.md
bad_example_ref: corpus/examples/operational_follow_up_note_bad_signal_dump.md
```

## Template

1. Review window and signals
2. Incidents or anomalies
3. Impact and interpretation
4. Follow-up actions and owners
5. Escalation needs or handoffs
6. Recommendation or next checkpoint
