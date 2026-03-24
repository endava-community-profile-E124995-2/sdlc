# Artifact Contract: Engineering Execution Plan

```yaml
id: artifact.engineering_execution_plan
artifact_name: Engineering execution plan
purpose: Turn an approved technical direction into sequenced workstreams, dependency order, validation checkpoints, and role handoffs.
required_sections:
  - implementation_goal
  - architecture_summary
  - workstreams_and_sequencing
  - dependencies
  - risks_and_mitigations
  - validation_plan
  - handoffs_and_unblockers
optional_sections:
  - staffing_notes
  - release_slices
  - tracking_metrics
minimum_quality_bar: A serious execution plan explains what is being built, the order of work, the critical dependencies, the main risks, how it will be validated, and where handoffs occur.
common_failure_modes:
  - work is listed without sequencing logic
  - dependencies are incomplete or ownerless
  - validation is reduced to a generic test placeholder
  - handoffs to other roles are implied instead of explicit
good_example_ref: corpus/examples/engineering_execution_plan_good_incremental_delivery.md
bad_example_ref: corpus/examples/engineering_execution_plan_bad_big_bang.md
```

## Template

1. Implementation goal
2. Architecture summary
3. Workstreams and sequencing
4. Dependencies
5. Risks and mitigations
6. Validation plan
7. Handoffs and unblockers
