# Risk Card: Integration Overrun

```yaml
id: risk.integration_overrun
risk_name: Integration overrun
definition: Cross-service coordination, contract changes, or data-flow differences add materially more work than the initial plan recognized.
trigger_signals:
  - one change requires updates in more systems than the first design assumed
  - interface contracts are implicit or versionless
  - dependency owners cannot confirm timing or compatibility
impact_area:
  - schedule
  - quality
  - cross-team alignment
likelihood_notes: Likelihood rises when interface inventories and dependency maps are skipped or kept informal.
mitigation_actions:
  - create an interface inventory before finalizing the execution plan
  - sequence work around owner-confirmed dependencies
  - use canary or staged validation for contract changes
escalation_path:
  - escalate within architecture and engineering when the design spans more systems than expected
  - involve deployment and operations when the integration path changes runtime support needs
related_metric_ids:
  - metric.dependency_burn_down_rate
  - metric.architecture_decision_lead_time
```

## Common Failure Mode

This risk is often hidden behind optimistic sequencing until a late integration environment exposes the real coupling.
