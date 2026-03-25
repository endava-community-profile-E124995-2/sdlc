# Artifact Routing

Use this reference to choose the right output shape and load the minimum supporting material.

## Active Agent Sources

- [agent/output_contracts.md](../../../../automation/roles/quality_and_security_and_governance_manager/agent/output_contracts.md)
- [agent/source_index.md](../../../../automation/roles/quality_and_security_and_governance_manager/agent/source_index.md)

## Source Precedence

1. [operating-policy.md](operating-policy.md)
2. relevant artifact contract
3. relevant interaction case
4. relevant metric, risk, and variant card
5. canonical ontology data
6. legacy role knowledge only as fallback

## Task Routing

### Quality Review

- Primary artifact: Quality Review Note
- Output target: reviewed scope, quality bar, reviewed evidence, validation gaps, recommendation, and unblockers
- Source files:
  - [quality_review_note.md](../../../../automation/roles/quality_and_security_and_governance_manager/assets/training/fine_tuning/corpus/artifacts/quality_review_note.md)
  - [verification_strategy_review.md](../../../../automation/roles/quality_and_security_and_governance_manager/assets/training/fine_tuning/corpus/interactions/verification_strategy_review.md)

### Security Review

- Primary artifact: Security Review Note
- Output target: reviewed boundary, threat and control context, risks, evidence gaps, follow-up, escalation, and recommendation
- Source files:
  - [security_review_note.md](../../../../automation/roles/quality_and_security_and_governance_manager/assets/training/fine_tuning/corpus/artifacts/security_review_note.md)
  - [security_boundary_review.md](../../../../automation/roles/quality_and_security_and_governance_manager/assets/training/fine_tuning/corpus/interactions/security_boundary_review.md)

### Governance Mapping

- Primary artifact: Governance Mapping Note
- Output target: control source, affected behavior, evidence status, approval or exception questions, risks, and next step
- Source files:
  - [governance_mapping_note.md](../../../../automation/roles/quality_and_security_and_governance_manager/assets/training/fine_tuning/corpus/artifacts/governance_mapping_note.md)
  - [governance_control_mapping.md](../../../../automation/roles/quality_and_security_and_governance_manager/assets/training/fine_tuning/corpus/interactions/governance_control_mapping.md)

### Release Gate

- Primary artifact: Release Gate Memo
- Output target: release scope, gate recommendation, blockers, evidence and exception status, handoffs, and unblock criteria
- Source files:
  - [release_gate_memo.md](../../../../automation/roles/quality_and_security_and_governance_manager/assets/training/fine_tuning/corpus/artifacts/release_gate_memo.md)
  - [release_gate_assessment.md](../../../../automation/roles/quality_and_security_and_governance_manager/assets/training/fine_tuning/corpus/interactions/release_gate_assessment.md)

### Handoff Patterns

- Product handoff source:
  - [product_policy_gap_handoff.md](../../../../automation/roles/quality_and_security_and_governance_manager/assets/training/fine_tuning/corpus/interactions/product_policy_gap_handoff.md)
- Architecture handoff source:
  - [architecture_boundary_handoff.md](../../../../automation/roles/quality_and_security_and_governance_manager/assets/training/fine_tuning/corpus/interactions/architecture_boundary_handoff.md)
- Deployment handoff source:
  - [deployment_readiness_handoff.md](../../../../automation/roles/quality_and_security_and_governance_manager/assets/training/fine_tuning/corpus/interactions/deployment_readiness_handoff.md)

## Legacy Fallback

Use the legacy pack only when the structured assets do not cover the request well enough:

- [legacy_role_rag](../../../../automation/roles/quality_and_security_and_governance_manager/assets/knowledge/legacy_role_rag)

