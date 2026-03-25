# Artifact Routing

Use this reference to choose the right output shape and load the minimum supporting material.

## Active Agent Sources

- [agent/output_contracts.md](../../../../automation/roles/deployment_and_operations_manager/agent/output_contracts.md)
- [agent/source_index.md](../../../../automation/roles/deployment_and_operations_manager/agent/source_index.md)

## Source Precedence

1. [operating-policy.md](operating-policy.md)
2. relevant artifact contract
3. relevant interaction case
4. relevant metric, risk, and variant card
5. canonical ontology data
6. legacy role knowledge only as fallback

## Task Routing

### Rollout Planning

- Primary artifact: Rollout Plan
- Output target: release scope, rollout sequence, rollback readiness, monitoring and communication expectations, owners, hold points, and open operational risks
- Source files:
  - [rollout_plan.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/artifacts/rollout_plan.md)
  - [rollout_planning.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/interactions/rollout_planning.md)

### Operability Review

- Primary artifact: Operability Review
- Output target: reviewed runtime scope, readiness expectations, monitoring status, runbook and support ownership status, gaps, and recommendation
- Source files:
  - [operability_review.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/artifacts/operability_review.md)
  - [operability_review.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/interactions/operability_review.md)

### Support Handoff

- Primary artifact: Operations Handoff Note
- Output target: receiving owner, current state, required runbooks and access, open risks, and acceptance criteria
- Source files:
  - [operations_handoff_note.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/artifacts/operations_handoff_note.md)
  - [support_handoff.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/interactions/support_handoff.md)

### Post-Release Follow-up

- Primary artifact: Operational Follow-up Note
- Output target: review window, incidents or anomalies, interpretation, owner-assigned follow-up, and next checkpoint
- Source files:
  - [operational_follow_up_note.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/artifacts/operational_follow_up_note.md)
  - [post_release_follow_up.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/interactions/post_release_follow_up.md)

### Handoff Patterns

- Product handoff source:
  - [product_rollout_constraint_handoff.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/interactions/product_rollout_constraint_handoff.md)
- Architecture handoff source:
  - [architecture_runtime_boundary_handoff.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/interactions/architecture_runtime_boundary_handoff.md)
- Quality handoff source:
  - [quality_gate_handoff.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/interactions/quality_gate_handoff.md)

## Legacy Fallback

Use the legacy pack only when the structured assets do not cover the request well enough:

- [legacy_role_rag](../../../../automation/roles/deployment_and_operations_manager/assets/knowledge/legacy_role_rag)

