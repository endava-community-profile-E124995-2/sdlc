# Artifact Contract: Rollout Plan

```yaml
id: artifact.rollout_plan
artifact_name: Rollout Plan
purpose: Turn release scope, sequencing, rollback, and owner expectations into an explicit operating plan for a named deployment path.
required_sections:
  - release_scope_and_target_environment
  - rollout_sequence_and_checkpoints
  - rollback_readiness
  - monitoring_and_communication_plan
  - owners_dependencies_and_hold_points
  - open_operational_risks_and_handoffs
optional_sections:
  - deployment_window
  - phased_rollout_notes
  - recheck_trigger
minimum_quality_bar: A serious rollout plan names the scope, sequence, checkpoints, rollback expectations, owners, and the open risks or handoffs that could still stop the release.
common_failure_modes:
  - the plan reads like status prose without checkpoint logic
  - rollback is reduced to a generic sentence with no owner or trigger
  - dependencies are implied instead of confirmed or marked as assumptions
  - the plan hides another role's blocker inside vague readiness language
good_example_ref: corpus/examples/rollout_plan_good_staged_release.md
bad_example_ref: corpus/examples/rollout_plan_bad_missing_hold_points.md
```

## Template

1. Release scope and target environment
2. Rollout sequence and checkpoints
3. Rollback readiness
4. Monitoring and communication plan
5. Owners, dependencies, and hold points
6. Open operational risks and handoffs
