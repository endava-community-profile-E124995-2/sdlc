# Structured Mesh Case: Executive Strategy Alignment

```yaml
id: mesh.exec.strategy_alignment
stakeholder_group_id: stake.exec_leadership
interaction_id: int.strategy_alignment
phase_tags:
  - discover
  - decide
  - plan
artifact_tags:
  - artifact.strategy_brief
  - artifact.roadmap_item
  - artifact.decision_memo
method_tags:
  - method.option_analysis
  - method.rice
metric_tags:
  - metric.revenue_impact
  - metric.adoption_rate
risk_tags:
  - risk.wrong_problem
  - risk.scope_creep
activated_capability_ids:
  - cap.problem_framing
  - cap.outcome_definition
  - cap.strategic_prioritization
  - cap.decision_framing
  - cap.executive_communication
activated_knowledge_area_ids:
  - know.product_strategy
  - know.unit_economics
input_signals:
  - leaders want a recommendation but the business problem is underspecified
  - multiple initiatives compete for the same quarter
  - roadmap pressure is rising faster than evidence quality
expected_outputs:
  - strategy brief with recommendation and explicit trade-offs
  - sequencing rationale for the roadmap item
  - open assumptions that could change the recommendation
escalation_triggers:
  - budget or compliance constraints materially change the preferred option
  - executive stakeholders disagree on what success means
example_prompt: We need an executive-ready recommendation on whether to prioritize self-serve onboarding or enterprise workflow controls next quarter.
priority: core
confidence: high
```

## Retrieval Notes

- Use when the task is recommendation-heavy and leadership-facing.
- Prefer this case when the user asks for a business case, roadmap rationale, or executive trade-off memo.
