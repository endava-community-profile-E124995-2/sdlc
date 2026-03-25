# Canonical ID Map

## Scope

This is the seed canonical ID map for the rewritten Quality and Security and Governance Manager corpus. It covers the IDs used by the structured interaction cases, operating policy, artifact contracts, metric cards, risk cards, and eval assets in this migration slice.

## Stakeholder Group IDs

- `stake.product_requirements`: Product managers, analysts, and requirements owners.
- `stake.architecture_engineering`: Architects, engineering leads, and implementation owners.
- `stake.quality_security_governance`: Quality, security, compliance, privacy, and governance stakeholders.
- `stake.deployment_operations`: Release, SRE, operations, and supportability stakeholders.

## Interaction IDs

- `int.quality_review`
- `int.security_review`
- `int.governance_mapping`
- `int.release_gate_assessment`
- `int.product_policy_handoff`
- `int.architecture_boundary_handoff`
- `int.deployment_readiness_handoff`

## Mesh Case IDs

- `mesh.quality.verification_strategy_review`
- `mesh.security.boundary_review`
- `mesh.governance.control_mapping`
- `mesh.release.gate_assessment`
- `mesh.product.policy_gap_handoff`
- `mesh.architecture.boundary_handoff`
- `mesh.deployment.readiness_handoff`

## Capability IDs

- `cap.verification_assessment`
- `cap.test_strategy_review`
- `cap.security_boundary_analysis`
- `cap.control_mapping`
- `cap.evidence_assessment`
- `cap.exception_framing`
- `cap.release_gate_evaluation`
- `cap.cross_role_handoff`
- `cap.risk_assessment`
- `cap.approval_gap_detection`

## Knowledge Area IDs

- `know.quality_expectations`
- `know.test_strategy`
- `know.security_constraints`
- `know.control_frameworks`
- `know.evidence_requirements`
- `know.release_governance`
- `know.system_boundaries`
- `know.operability_expectations`
- `know.exception_management`

## Artifact IDs

- `artifact.quality_review_note`
- `artifact.security_review_note`
- `artifact.governance_mapping_note`
- `artifact.release_gate_memo`

## Method IDs

- `method.evidence_review`
- `method.control_traceability`
- `method.risk_review`
- `method.exception_review`
- `method.gate_decision_review`
- `method.handoff_preparation`
- `method.boundary_analysis`
- `method.verification_scope_check`

## Metric IDs

- `metric.defect_escape_rate`
- `metric.remediation_lead_time`
- `metric.evidence_coverage`
- `metric.gate_decision_lead_time`

## Risk IDs

- `risk.verification_gap`
- `risk.security_boundary_drift`
- `risk.evidence_gap`
- `risk.gate_readiness_blind_spot`

## Glossary IDs

- `term.release_gate`: A recommendation on whether a change should proceed, pause, or block based on known evidence, exceptions, and blockers.
- `term.control_mapping`: Traceability from a control or policy requirement to the affected system behavior and evidence.
- `term.exception`: A documented deviation from the expected control or quality bar that still needs explicit handling or approval.
- `term.evidence_sufficiency`: The degree to which the available review inputs are strong enough to support a recommendation.

## Naming Rules

- Use the canonical ID in structured records and evals.
- Use aliases only to improve retrieval recall.
- When a raw label from a fallback pack does not map cleanly, prefer the closest canonical node plus a clarifying note instead of minting a vague new label.
