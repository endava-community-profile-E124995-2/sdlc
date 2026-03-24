# Metric Card: Operability Readiness

```yaml
id: metric.operability_readiness
metric_name: Operability readiness
definition: The share of required runtime artifacts and operational controls completed before a release candidate is handed to deployment and operations.
formula_or_logic: completed_operability_requirements / total_required_operability_requirements
owner: Deployment and operations owner with engineering input
data_source:
  - release checklist
  - runbook tracker
  - observability and alerting setup records
baseline_needed: A baseline from recent releases helps identify whether the team is handing off too late or underprepared.
leading_or_lagging: Leading for release safety and support burden.
anti_patterns:
  - marking observability ready because logs exist without dashboards or alerts
  - ignoring rollback or on-call documentation
  - counting release artifacts as complete before the receiving role reviews them
interpretation_notes:
  - this metric is strongest when paired with deployment handoff notes
  - high readiness should still be checked against actual rollback and alerting drills
```

## Related Risks

- `risk.operability_gap`
- `risk.handoff_loss`
