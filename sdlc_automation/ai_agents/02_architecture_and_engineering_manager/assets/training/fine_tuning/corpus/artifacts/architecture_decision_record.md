# Artifact Contract: Architecture Decision Record

```yaml
id: artifact.architecture_decision_record
artifact_name: Architecture decision record
purpose: Compare meaningful technical options, record the chosen design, and preserve the trade-offs and impacts.
required_sections:
  - decision_statement
  - architectural_context
  - options_considered
  - recommendation
  - rationale_and_trade_offs
  - impact_on_systems_and_teams
  - follow_up_actions
optional_sections:
  - rejected_assumptions
  - rollback_considerations
  - review_signals
minimum_quality_bar: A serious ADR names the decision, compares real options, explains why the chosen path wins now, and makes downstream impacts explicit.
common_failure_modes:
  - only one option is documented
  - the chosen path has no rationale beyond preference
  - trade-offs are omitted or softened
  - impacts on interfaces, dependencies, or teams are missing
good_example_ref: corpus/examples/architecture_decision_record_good_service_split.md
bad_example_ref: corpus/examples/architecture_decision_record_bad_single_option.md
```

## Template

1. Decision statement
2. Architectural context
3. Options considered
4. Recommendation
5. Rationale and trade-offs
6. Impact on systems and teams
7. Follow-up actions
