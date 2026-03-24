# Retrieval Eval Seed Set

## Purpose

Use these prompts to verify that retrieval returns the right interaction cases, artifact contracts, and operational cards.

## Queries

### RQ-01: Technical Feasibility

- Prompt: Turn this approved PRD into a technical feasibility brief for tenant-scoped API rate limiting.
- Expected retrieval:
  - `mesh.product.approved_change_feasibility`
  - `artifact.technical_feasibility_brief`
  - `risk.architecture_misalignment`

### RQ-02: Architecture Trade-Off

- Prompt: Choose between extending the monolith and splitting a service for billing webhooks.
- Expected retrieval:
  - `mesh.architecture.option_tradeoff`
  - `artifact.architecture_decision_record`
  - `risk.integration_overrun`

### RQ-03: Execution Planning

- Prompt: Break this approved design into implementation workstreams, dependencies, and test checkpoints.
- Expected retrieval:
  - `mesh.engineering.execution_planning`
  - `artifact.engineering_execution_plan`
  - `metric.dependency_burn_down_rate`

### RQ-04: Product Handoff

- Prompt: Requirements are still ambiguous and the team keeps discovering new scope. Draft the handoff back to product.
- Expected retrieval:
  - `mesh.product.intent_gap_handoff`
  - `artifact.cross_role_handoff_note`
  - `risk.handoff_loss`

### RQ-05: Governance Handoff

- Prompt: Security review changed the auth design and we need to hand the decision to governance with the right context.
- Expected retrieval:
  - `mesh.qsg.control_handoff`
  - `artifact.cross_role_handoff_note`
  - `know.security_constraints`

### RQ-06: Operations Handoff

- Prompt: We need rollout, observability, rollback, and support readiness before release. Prepare the handoff to deployment and operations.
- Expected retrieval:
  - `mesh.ops.operability_handoff`
  - `artifact.cross_role_handoff_note`
  - `risk.operability_gap`
