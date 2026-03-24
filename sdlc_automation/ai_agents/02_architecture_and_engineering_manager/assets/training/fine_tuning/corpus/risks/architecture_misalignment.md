# Risk Card: Architecture Misalignment

```yaml
id: risk.architecture_misalignment
risk_name: Architecture misalignment
definition: The proposed design conflicts with the current system boundaries, platform standards, or non-functional constraints in ways that will surface late and expensively.
trigger_signals:
  - a design assumes service boundaries that do not exist
  - the same change is being modeled differently across teams
  - platform constraints appear only after implementation planning starts
impact_area:
  - delivery predictability
  - reliability
  - cross-team coordination
likelihood_notes: Likelihood rises when architecture decisions are delayed or when feasibility work skips current-state analysis.
mitigation_actions:
  - map current system boundaries and interface owners first
  - record the design decision and rejected options explicitly
  - surface non-functional constraints before sequencing implementation
escalation_path:
  - escalate to architecture and engineering ownership when the system model is inconsistent
  - hand to quality, security, and governance when the misalignment is driven by control requirements
related_metric_ids:
  - metric.architecture_decision_lead_time
  - metric.plan_volatility
```

## Common Failure Mode

Teams mistake this for normal delivery slippage when the real issue is that the design never fit the system they actually have.
