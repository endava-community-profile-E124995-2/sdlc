# Interaction Cases

Use this reference when the request is driven by a specific stakeholder interaction or a repeated cross-functional pressure pattern.

Active agent source: [agent/source_index.md](../../../../automation/roles/deployment_and_operations_manager/agent/source_index.md)

## Rollout Planning

- Use when the release scope exists and the team needs a concrete rollout sequence with checkpoints and owners.
- Expected outputs:
  - rollout plan
  - explicit hold points and rollback expectations
- Source: [rollout_planning.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/interactions/rollout_planning.md)

## Operability Review

- Use when the team needs an explicit view on monitoring, runbooks, rollback readiness, or support ownership before launch.
- Expected outputs:
  - operability review
  - explicit readiness gaps and recommendation
- Boundary:
  - evaluate runtime readiness
  - do not invent gate approval or missing runtime design
- Source: [operability_review.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/interactions/operability_review.md)

## Support Handoff

- Use when a release or operational event must be transferred to a receiving support or on-call function.
- Expected outputs:
  - operations handoff note
  - explicit owner, open risks, and acceptance criteria
- Source: [support_handoff.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/interactions/support_handoff.md)

## Post-Release Follow-up

- Use when production signals exist and the team needs operational interpretation and next actions.
- Expected outputs:
  - operational follow-up note
  - interpreted anomalies and owner-assigned next steps
- Source: [post_release_follow_up.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/interactions/post_release_follow_up.md)

## Product Rollout Constraint Handoff

- Use when business rollout policy, audience choice, or enablement timing blocks safe deployment planning.
- Expected outputs:
  - rollout-planning handoff to product
  - explicit missing business decisions and unblock criteria
- Boundary:
  - do not invent rollout policy or audience segmentation
- Source: [product_rollout_constraint_handoff.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/interactions/product_rollout_constraint_handoff.md)

## Architecture Runtime Boundary Handoff

- Use when deployment can identify a rollback or runtime risk but the mitigation depends on an unresolved design boundary.
- Expected outputs:
  - operability review that names the architecture blocker
  - clear design question and unblock criteria
- Source: [architecture_runtime_boundary_handoff.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/interactions/architecture_runtime_boundary_handoff.md)

## Quality Gate Handoff

- Use when the user is asking for ship or no-ship approval, evidence sufficiency, or exception handling that deployment does not own.
- Expected outputs:
  - deployment-oriented readiness note with an explicit handoff to quality
  - clear statement of known operational inputs and missing gate ownership
- Source: [quality_gate_handoff.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/interactions/quality_gate_handoff.md)

