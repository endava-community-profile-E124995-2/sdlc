# Structured Mesh Case: Sales Priority Pressure

```yaml
id: mesh.sales.priority_pressure
stakeholder_group_id: stake.sales_presales
interaction_id: int.prioritization
phase_tags:
  - discover
  - decide
  - plan
artifact_tags:
  - artifact.decision_memo
  - artifact.roadmap_item
method_tags:
  - method.option_analysis
  - method.wsjf
metric_tags:
  - metric.revenue_impact
  - metric.adoption_rate
risk_tags:
  - risk.wrong_problem
  - risk.scope_creep
activated_capability_ids:
  - cap.feedback_synthesis
  - cap.strategic_prioritization
  - cap.decision_framing
  - cap.stakeholder_alignment
  - cap.executive_communication
activated_knowledge_area_ids:
  - know.product_strategy
  - know.unit_economics
input_signals:
  - a deal-driven ask is being positioned as roadmap-critical
  - evidence quality is weaker than stakeholder pressure
  - customer request volume is being confused with validated demand
expected_outputs:
  - prioritization recommendation with explicit evidence quality
  - distinction between customer request and validated product need
  - follow-up discovery or segmentation recommendation
escalation_triggers:
  - contractual commitments or revenue dependency materially alter the recommendation
  - customer-specific asks threaten general product direction
example_prompt: Sales wants this enterprise request on the roadmap now because of one strategic account. Frame the decision and push back if the evidence is weak.
priority: core
confidence: high
```

## Retrieval Notes

- Use when commercial pressure is distorting prioritization.
- Keep the analysis evidence-led and explicit about exceptions.
