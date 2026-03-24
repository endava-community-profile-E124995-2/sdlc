# Structured Mesh Case: Architecture Option Trade-Off

```yaml
id: mesh.architecture.option_tradeoff
stakeholder_group_id: stake.architecture_engineering
interaction_id: int.architecture_optioning
phase_tags:
  - define
  - plan
artifact_tags:
  - artifact.architecture_decision_record
  - artifact.engineering_execution_plan
method_tags:
  - method.option_analysis
  - method.interface_inventory
  - method.risk_review
metric_tags:
  - metric.architecture_decision_lead_time
  - metric.plan_volatility
risk_tags:
  - risk.architecture_misalignment
  - risk.integration_overrun
activated_capability_ids:
  - cap.architecture_optioning
  - cap.interface_contract_design
  - cap.decision_record_writing
  - cap.technical_risk_assessment
activated_knowledge_area_ids:
  - know.system_architecture
  - know.service_boundaries
  - know.integration_patterns
  - know.data_flow
input_signals:
  - multiple design paths remain viable
  - service boundaries or interface contracts are the main decision point
  - trade-offs will affect multiple teams or systems
expected_outputs:
  - ADR with real options
  - interface and dependency impacts
  - follow-up actions for the chosen path
escalation_triggers:
  - approval gates or security posture dominate the unresolved decision
  - operability concerns make deployment and operations the primary owner
example_prompt: Choose between extending the monolith and splitting a service for billing webhooks.
priority: core
confidence: high
```

## Retrieval Notes

- Use when the main work is choosing between technical options, not restating product intent.
- Always make trade-offs explicit and document why the rejected paths lost.
