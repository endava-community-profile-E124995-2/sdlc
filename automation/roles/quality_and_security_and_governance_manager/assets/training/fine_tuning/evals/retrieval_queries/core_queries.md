# Retrieval Eval Seed Set

## Purpose

Use these prompts to verify that retrieval returns the right interaction cases, artifact contracts, and operational cards.

## Queries

### RQ-01: Quality Review

- Prompt: Review this execution plan and tell us whether the verification strategy is sufficient.
- Expected retrieval:
  - `mesh.quality.verification_strategy_review`
  - `artifact.quality_review_note`
  - `risk.verification_gap`

### RQ-02: Security Review

- Prompt: Assess the auth-token sharing change and required security controls.
- Expected retrieval:
  - `mesh.security.boundary_review`
  - `artifact.security_review_note`
  - `risk.security_boundary_drift`

### RQ-03: Governance Mapping

- Prompt: Map this release to the relevant controls and flag missing evidence or exception approvals.
- Expected retrieval:
  - `mesh.governance.control_mapping`
  - `artifact.governance_mapping_note`
  - `metric.evidence_coverage`

### RQ-04: Release Gate

- Prompt: Should we ship on Friday given these blockers and missing approvals?
- Expected retrieval:
  - `mesh.release.gate_assessment`
  - `artifact.release_gate_memo`
  - `risk.gate_readiness_blind_spot`

### RQ-05: Product Handoff

- Prompt: The policy implies a product rule we still have not defined.
- Expected retrieval:
  - `mesh.product.policy_gap_handoff`
  - `artifact.governance_mapping_note`
  - `risk.evidence_gap`

### RQ-06: Architecture Handoff

- Prompt: The mitigation depends on an unresolved service boundary.
- Expected retrieval:
  - `mesh.architecture.boundary_handoff`
  - `artifact.security_review_note`
  - `know.system_boundaries`

### RQ-07: Deployment Handoff

- Prompt: Gate is green only if rollback, monitoring, and on-call ownership are ready.
- Expected retrieval:
  - `mesh.deployment.readiness_handoff`
  - `artifact.release_gate_memo`
  - `know.operability_expectations`
