# Artifact Contract: Decision Memo

```yaml
id: artifact.decision_memo
artifact_name: Decision memo
purpose: Make a recommendation explicit, compare alternatives, and record why one path is preferred now.
required_sections:
  - decision
  - context
  - options_considered
  - recommendation
  - rationale
  - trade_offs
  - risks
  - follow_up_actions
optional_sections:
  - dependencies
  - assumptions
  - unresolved_questions
minimum_quality_bar: A serious memo names the decision, rejected options, rationale, key risks, and next actions.
common_failure_modes:
  - the decision is implied rather than stated
  - alternatives are missing
  - rationale is only opinion
  - risks are softened into generic cautions
good_example_ref: corpus/examples/decision_memo_good_onboarding_experiment.md
bad_example_ref: corpus/examples/decision_memo_bad_solution_bias.md
```

## Template

1. Decision
2. Context
3. Options considered
4. Recommendation and rationale
5. Trade-offs and risks
6. Follow-up actions and owners
