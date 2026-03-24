# Artifact Routing

Use this reference to choose the right output shape and load the minimum supporting material.

## Active Agent Sources

- [agent/output_contracts.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/agent/output_contracts.md)
- [agent/source_index.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/agent/source_index.md)

## Source Precedence

1. [operating-policy.md](operating-policy.md)
2. relevant artifact contract
3. relevant interaction case
4. relevant metric, risk, and variant card
5. canonical ontology data
6. legacy role knowledge only as fallback

## Task Routing

### Discovery and Problem Framing

- Primary artifact: discovery brief
- Output target: problem statement, target user or segment, evidence summary, assumptions and unknowns, next validation step
- Source files:
  - [discovery_brief.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/artifacts/discovery_brief.md)
  - [inference_map.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/agent/inference_map.md)

### Requirements Definition Or Refinement

- Primary artifact: PRD
- Output target: scope, exclusions, business rules, functional requirements, non-functional requirements, acceptance criteria, dependencies, risks, open questions
- Source files:
  - [prd.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/artifacts/prd.md)
  - [product_requirement_refinement.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/interactions/product_requirement_refinement.md)
  - [engineering_requirement_clarification.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/interactions/engineering_requirement_clarification.md)

### Prioritization And Decision Support

- Primary artifact: decision memo
- Output target: options considered, recommendation, rationale, trade-offs, risks, follow-up actions
- Source files:
  - [decision_memo.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/artifacts/decision_memo.md)
  - [sales_priority_pressure.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/interactions/sales_priority_pressure.md)

### Launch Or Rollout Readiness

- Output target: audience, release scope, rollout approach, enablement needs, monitoring plan, fallback expectations
- Source files:
  - [assistant_operating_policy.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/policies/assistant_operating_policy.md)
  - [inference_map.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/agent/inference_map.md)

### Metrics And Post-Launch Review

- Primary interaction: metric design
- Output target: metric definition, baseline need, instrumentation gaps, interpretation notes, next action
- Source files:
  - [data_metric_design.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/interactions/data_metric_design.md)
  - [adoption_rate.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/metrics/adoption_rate.md)

### Governance, Compliance, Or Control-Heavy Work

- Primary output: traceable requirement mapping with approval questions and risks
- Source files:
  - [grc_compliance_requirement_mapping.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/interactions/grc_compliance_requirement_mapping.md)
  - [regulated.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/variants/regulated.md)
  - [prd.md](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/corpus/artifacts/prd.md)

## Legacy Fallback

Use the legacy pack only when the structured assets do not cover the request well enough:

- [legacy_role_rag](../../../../sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/knowledge/legacy_role_rag)

