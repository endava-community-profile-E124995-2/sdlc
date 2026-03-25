# Canonical ID Map

## Scope

This is the seed canonical ID map for the rewritten Deployment and Operations Manager corpus. It covers the IDs used by the structured interaction cases, operating policy, artifact contracts, metric cards, risk cards, and eval assets in this migration slice.

## Stakeholder Group IDs

- `stake.product_requirements`: Product managers, analysts, and requirements owners.
- `stake.architecture_engineering`: Architects, engineering leads, and implementation owners.
- `stake.quality_security_governance`: Quality, security, compliance, and governance stakeholders.
- `stake.deployment_operations`: Release managers, SRE, operations, support, and incident-response stakeholders.

## Interaction IDs

- `int.rollout_planning`
- `int.operability_review`
- `int.support_handoff`
- `int.post_release_follow_up`
- `int.product_rollout_constraint_handoff`
- `int.architecture_runtime_boundary_handoff`
- `int.quality_gate_handoff`

## Mesh Case IDs

- `mesh.release.rollout_planning`
- `mesh.operations.operability_review`
- `mesh.operations.support_handoff`
- `mesh.operations.post_release_follow_up`
- `mesh.product.rollout_constraint_handoff`
- `mesh.architecture.runtime_boundary_handoff`
- `mesh.quality.gate_handoff`

## Capability IDs

- `cap.rollout_planning`
- `cap.release_coordination`
- `cap.rollback_readiness_assessment`
- `cap.observability_review`
- `cap.runbook_preparation`
- `cap.support_handoff`
- `cap.post_release_analysis`
- `cap.operational_risk_assessment`
- `cap.cross_role_handoff`
- `cap.incident_signal_triage`

## Knowledge Area IDs

- `know.release_scope`
- `know.rollout_strategy`
- `know.rollback_requirements`
- `know.observability_requirements`
- `know.runbook_quality`
- `know.support_ownership`
- `know.incident_signals`
- `know.operability_expectations`
- `know.release_governance`

## Artifact IDs

- `artifact.rollout_plan`
- `artifact.operability_review`
- `artifact.operations_handoff_note`
- `artifact.operational_follow_up_note`

## Method IDs

- `method.sequence_planning`
- `method.readiness_review`
- `method.rollback_check`
- `method.observability_gap_analysis`
- `method.handoff_preparation`
- `method.signal_triage`
- `method.risk_review`
- `method.owner_mapping`

## Metric IDs

- `metric.operability_readiness`
- `metric.rollback_rehearsal_coverage`
- `metric.deployment_lead_time`
- `metric.incident_restore_time`

## Risk IDs

- `risk.rollout_coordination_drift`
- `risk.rollback_readiness_gap`
- `risk.observability_blind_spot`
- `risk.support_ownership_gap`

## Glossary IDs

- `term.rollout_hold_point`: A planned checkpoint where the release pauses until explicit readiness conditions are met.
- `term.rollback_readiness`: The degree to which reversal steps are current, tested, and owned before release.
- `term.operability_review`: A structured review of monitoring, runbooks, ownership, and runtime readiness for a scoped change.
- `term.support_handoff`: A transfer of runtime context, ownership, and known risks to the receiving support or operations function.

## Naming Rules

- Use the canonical ID in structured records and evals.
- Use aliases only to improve retrieval recall.
- When a raw label from a fallback pack does not map cleanly, prefer the closest canonical node plus a clarifying note instead of minting a vague new label.
