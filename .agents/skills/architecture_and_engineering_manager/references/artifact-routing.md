# Artifact Routing

Use this reference to choose the right output shape and load the minimum supporting material.

## Active Agent Sources

- [agent/output_contracts.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/agent/output_contracts.md)
- [agent/source_index.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/agent/source_index.md)

## Source Precedence

1. [operating-policy.md](operating-policy.md)
2. relevant artifact contract
3. relevant interaction case
4. relevant metric, risk, and variant card
5. canonical ontology data
6. legacy role knowledge only as fallback

## Task Routing

### Technical Feasibility Assessment

- Primary artifact: technical feasibility brief
- Output target: requested change, current system context, constraints, feasibility assessment, risks, and next step
- Source files:
  - [technical_feasibility_brief.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/artifacts/technical_feasibility_brief.md)
  - [technical_feasibility_assessment.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/interactions/technical_feasibility_assessment.md)

### Architecture Decision

- Primary artifact: architecture decision record
- Output target: decision statement, options, rationale, trade-offs, impacts, and follow-up work
- Source files:
  - [architecture_decision_record.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/artifacts/architecture_decision_record.md)
  - [architecture_option_tradeoff.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/interactions/architecture_option_tradeoff.md)

### Engineering Execution Planning

- Primary artifact: engineering execution plan
- Output target: implementation goal, sequencing, dependencies, risks, validation, and handoffs
- Source files:
  - [engineering_execution_plan.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/artifacts/engineering_execution_plan.md)
  - [engineering_execution_planning.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/interactions/engineering_execution_planning.md)

### Cross-Role Handoff

- Primary artifact: cross-role handoff note
- Output target: target role, trigger, known facts, open decisions, requested action, and unblock criteria
- Source files:
  - [cross_role_handoff_note.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/artifacts/cross_role_handoff_note.md)
  - [product_intent_gap_handoff.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/interactions/product_intent_gap_handoff.md)
  - [quality_control_handoff.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/interactions/quality_control_handoff.md)
  - [operability_handoff.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/interactions/operability_handoff.md)

## Legacy Fallback

Use the legacy pack only when the structured assets do not cover the request well enough:

- [legacy_role_rag](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/knowledge/legacy_role_rag)

