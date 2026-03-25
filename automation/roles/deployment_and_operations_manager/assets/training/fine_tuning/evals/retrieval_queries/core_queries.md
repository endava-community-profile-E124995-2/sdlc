# Retrieval Eval Seed Set

## Purpose

Use these prompts to verify that retrieval returns the right interaction cases, artifact contracts, and operational cards.

## Queries

### RQ-01: Rollout Planning

- Prompt: Plan the staged production rollout, rollback checkpoints, and owner handoffs for this release.
- Expected retrieval:
  - `mesh.release.rollout_planning`
  - `artifact.rollout_plan`
  - `risk.rollout_coordination_drift`

### RQ-02: Operability Review

- Prompt: Review whether dashboards, alerts, runbooks, and on-call ownership are ready before launch.
- Expected retrieval:
  - `mesh.operations.operability_review`
  - `artifact.operability_review`
  - `metric.operability_readiness`

### RQ-03: Support Handoff

- Prompt: Prepare the support handoff for this release and list the open operational risks.
- Expected retrieval:
  - `mesh.operations.support_handoff`
  - `artifact.operations_handoff_note`
  - `risk.support_ownership_gap`

### RQ-04: Post-Release Follow-up

- Prompt: Summarize the first 24 hours of production signals and recommend next actions.
- Expected retrieval:
  - `mesh.operations.post_release_follow_up`
  - `artifact.operational_follow_up_note`
  - `metric.incident_restore_time`

### RQ-05: Quality Handoff

- Prompt: We still need a ship or no-ship decision because approvals and evidence are incomplete.
- Expected retrieval:
  - `mesh.quality.gate_handoff`
  - `artifact.operability_review`
  - `know.release_governance`

### RQ-06: Architecture Handoff

- Prompt: Rollback safety depends on an unresolved service boundary.
- Expected retrieval:
  - `mesh.architecture.runtime_boundary_handoff`
  - `artifact.operability_review`
  - `know.rollback_requirements`

### RQ-07: Product Handoff

- Prompt: Phased rollout constraints are unclear because launch audience and scope are still undecided.
- Expected retrieval:
  - `mesh.product.rollout_constraint_handoff`
  - `artifact.rollout_plan`
  - `know.rollout_strategy`
