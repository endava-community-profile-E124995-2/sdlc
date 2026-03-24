# Canonical ID Map

## Scope

This is the seed canonical ID map for the rewritten Architecture and Engineering Manager corpus. It covers the IDs used by the structured interaction cases, operating policy, artifact contracts, metric cards, risk cards, and eval assets in this migration slice.

## Stakeholder Group IDs

- `stake.product_requirements`: Product managers, analysts, and requirements owners.
- `stake.architecture_engineering`: Architects, engineering managers, leads, and implementation owners.
- `stake.platform_shared_services`: Platform, infrastructure, and shared service stakeholders.
- `stake.quality_security_governance`: Quality, security, compliance, and governance stakeholders.
- `stake.deployment_operations`: Release, SRE, operations, and supportability stakeholders.

## Interaction IDs

- `int.feasibility_assessment`
- `int.architecture_optioning`
- `int.interface_design`
- `int.execution_planning`
- `int.dependency_sequencing`
- `int.cross_role_handoff`
- `int.control_review_handoff`
- `int.operability_review_handoff`

## Mesh Case IDs

- `mesh.product.approved_change_feasibility`
- `mesh.architecture.option_tradeoff`
- `mesh.engineering.execution_planning`
- `mesh.product.intent_gap_handoff`
- `mesh.qsg.control_handoff`
- `mesh.ops.operability_handoff`

## Capability IDs

- `cap.feasibility_assessment`
- `cap.current_state_analysis`
- `cap.architecture_optioning`
- `cap.interface_contract_design`
- `cap.integration_planning`
- `cap.execution_planning`
- `cap.dependency_sequencing`
- `cap.implementation_slicing`
- `cap.non_functional_analysis`
- `cap.technical_risk_assessment`
- `cap.handoff_preparation`
- `cap.decision_record_writing`

## Knowledge Area IDs

- `know.system_architecture`
- `know.service_boundaries`
- `know.integration_patterns`
- `know.data_flow`
- `know.non_functional_requirements`
- `know.security_constraints`
- `know.delivery_governance`
- `know.observability_requirements`
- `know.dependency_topology`

## Artifact IDs

- `artifact.technical_feasibility_brief`
- `artifact.architecture_decision_record`
- `artifact.engineering_execution_plan`
- `artifact.cross_role_handoff_note`

## Method IDs

- `method.system_context_mapping`
- `method.option_analysis`
- `method.interface_inventory`
- `method.dependency_mapping`
- `method.increment_slicing`
- `method.risk_review`
- `method.handoff_review`

## Metric IDs

- `metric.architecture_decision_lead_time`
- `metric.dependency_burn_down_rate`
- `metric.plan_volatility`
- `metric.operability_readiness`

## Risk IDs

- `risk.architecture_misalignment`
- `risk.integration_overrun`
- `risk.handoff_loss`
- `risk.operability_gap`

## Glossary IDs

- `term.adr`: A durable record of an architecture decision, why it was chosen, and what it changes.
- `term.feasibility`: Evidence-based judgment about whether a requested change fits the current system and constraints.
- `term.handoff`: A role transition note that preserves facts, open questions, and unblock criteria.
- `term.service_boundary`: The technical edge where responsibility, contracts, and failure handling change.
- `term.execution_plan`: A sequenced implementation plan that names dependencies, validation, and handoffs.

## Naming Rules

- Use the canonical ID in structured records and evals.
- Use aliases only to improve retrieval recall.
- When a raw label from the legacy pack does not map cleanly, prefer the closest canonical node plus a clarifying note instead of minting a vague new label.
