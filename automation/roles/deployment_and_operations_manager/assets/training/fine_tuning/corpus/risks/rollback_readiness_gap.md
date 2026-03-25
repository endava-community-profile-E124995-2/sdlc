# Risk Card: Rollback Readiness Gap

```yaml
id: risk.rollback_readiness_gap
risk_name: Rollback readiness gap
definition: The release has a nominal rollback path, but the steps, owners, or prereqs are outdated, unreviewed, or untested for the current deployment path.
trigger_signals:
  - rollback instructions exist only in engineering discussion or stale documents
  - dependencies required for reversal have no named owner
  - canary, feature-flag, or database rollback behavior is assumed rather than checked
impact_area:
  - recovery speed
  - release safety
  - customer or employee trust
likelihood_notes: Likelihood rises when release teams optimize for forward progress and postpone rollback rehearsal until after rollout begins.
mitigation_actions:
  - make rollback expectations explicit in the rollout plan
  - verify the current rollback path against the actual release scope and environment
  - attach rollback ownership and rehearse or review the plan before launch
escalation_path:
  - escalate to architecture when rollback depends on unresolved service or data-boundary design
  - escalate to quality when a gate or exception decision is being made without rollback clarity
related_metric_ids:
  - metric.rollback_rehearsal_coverage
  - metric.operability_readiness
```

## Common Failure Mode

The team says the release is reversible, but no one can confidently execute the current rollback path under time pressure.
