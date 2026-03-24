# Interaction Cases

Use this reference when the request is driven by a specific stakeholder interaction or a repeated cross-functional pressure pattern.

Active agent source: [agent/source_index.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/agent/source_index.md)

## Technical Feasibility Assessment

- Use when product intent is approved enough to explore feasibility, but the technical shape is not yet credible.
- Signals:
  - the affected systems or dependencies are not yet mapped
  - the team needs to know whether the change fits the current architecture
  - hidden constraints may invalidate the request or delivery shape
- Expected outputs:
  - feasibility summary
  - architecture and dependency notes
  - explicit unknowns and next technical step
- Source: [technical_feasibility_assessment.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/interactions/technical_feasibility_assessment.md)

## Architecture Option Trade-Off

- Use when the team must choose between materially different design paths.
- Expected outputs:
  - ADR with options and trade-offs
  - interface and dependency impacts
  - follow-up work and decision consequences
- Source: [architecture_option_tradeoff.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/interactions/architecture_option_tradeoff.md)

## Engineering Execution Planning

- Use when the architecture direction is known and the team needs concrete sequencing, dependencies, and validation planning.
- Expected outputs:
  - phased implementation plan
  - dependency order and risk notes
  - validation checkpoints and handoffs
- Source: [engineering_execution_planning.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/interactions/engineering_execution_planning.md)

## Product Intent Gap Handoff

- Use when product intent is too weak for technical design to proceed safely.
- Expected outputs:
  - explicit return-to-product handoff
  - missing business inputs
  - unblock criteria for technical work to resume
- Source: [product_intent_gap_handoff.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/interactions/product_intent_gap_handoff.md)

## Quality, Security, And Governance Handoff

- Use when control interpretation, approval gates, or security posture dominate the unresolved issue.
- Expected outputs:
  - governance-oriented handoff note
  - design question framed for the target reviewers
  - impact and unblock criteria
- Source: [quality_control_handoff.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/interactions/quality_control_handoff.md)

## Deployment And Operations Handoff

- Use when observability, runbooks, rollback, SLOs, or support readiness become the primary open work.
- Expected outputs:
  - deployment and operations handoff note
  - operability gaps and required artifacts
  - readiness conditions for implementation or release
- Source: [operability_handoff.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/interactions/operability_handoff.md)

