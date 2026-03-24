# Risk Card: Ambiguous Requirements

```yaml
id: risk.ambiguous_requirements
risk_name: Ambiguous requirements
definition: Requirements are worded in a way that allows materially different interpretations of behavior, scope, or acceptance conditions.
trigger_signals:
  - engineering asks repeated clarification questions
  - business rules are implied instead of stated
  - acceptance criteria do not cover edge conditions or exclusions
  - change requests appear late because intent was interpreted differently
impact_area:
  - delivery predictability
  - quality
  - cross-functional alignment
likelihood_notes: Likelihood rises when stakeholder pressure compresses definition time or when multiple teams own adjacent parts of the workflow.
mitigation_actions:
  - rewrite requirements with explicit actors, rules, exclusions, and acceptance criteria
  - label assumptions and unresolved questions
  - map dependencies and non-functional expectations early
  - run requirement walkthroughs before delivery commitment
escalation_path:
  - escalate to product leadership when ambiguity changes scope or priority
  - involve engineering or compliance owners when technical or governance interpretation is disputed
related_metric_ids:
  - metric.requirement_rework_rate
  - metric.cycle_time
```

## Common Failure Mode

This risk is often mistaken for an engineering execution problem when the actual issue is poor requirement definition.
