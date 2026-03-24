# Interaction Cases

Use this reference when the request is driven by a specific stakeholder interaction or a repeated cross-functional pressure pattern.

Active agent source: [agent/source_index.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/agent/source_index.md)

## Product Requirement Refinement

- Use when the problem is known but the requirement set is weak.
- Signals:
  - backlog items are moving forward with unresolved ambiguity
  - peers disagree on scope or exclusions
  - changes are being made without visible rationale
- Expected outputs:
  - revised requirement set
  - updated acceptance criteria
  - change log of what changed and why
- Source: [product_requirement_refinement.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/interactions/product_requirement_refinement.md)

## Engineering Requirement Clarification

- Use when engineering says the story is too vague, especially around edge cases, failures, dependencies, or non-functional needs.
- Expected outputs:
  - clarified requirements and acceptance criteria
  - dependency notes
  - explicit non-functional expectations and open questions
- Boundary:
  - clarify intent, rules, and constraints
  - do not take final architecture ownership
- Source: [engineering_requirement_clarification.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/interactions/engineering_requirement_clarification.md)

## Sales Priority Pressure

- Use when commercial pressure is distorting prioritization.
- Signals:
  - a deal-driven ask is being framed as roadmap critical
  - request volume is being confused with validated demand
  - evidence quality is weaker than stakeholder pressure
- Expected outputs:
  - recommendation with explicit evidence quality
  - separation of customer request from product need
  - follow-up discovery or segmentation recommendation
- Source: [sales_priority_pressure.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/interactions/sales_priority_pressure.md)

## Data Metric Design

- Use when the team needs KPI cleanup, launch metrics, or post-launch interpretation.
- Expected outputs:
  - metric definitions and baselines
  - instrumentation questions and gaps
  - leading and lagging measure guidance
- Source: [data_metric_design.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/interactions/data_metric_design.md)

## Compliance Requirement Mapping

- Use when policy, privacy, auditability, or approval-driven traceability shapes the work.
- Expected outputs:
  - traceable requirement mapping
  - policy-driven constraints
  - explicit approval questions and risk notes
- Boundary:
  - do not replace legal or compliance judgment
- Source: [grc_compliance_requirement_mapping.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/interactions/grc_compliance_requirement_mapping.md)

