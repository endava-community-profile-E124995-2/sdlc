---
name: quality-and-security-and-governance-manager
description: Thin adapter for quality review, security review, governance mapping, and release-gate work. Canonical logic lives under automation/roles/quality_and_security_and_governance_manager.
---

# Quality And Security And Governance Manager

This skill is a thin repo-local adapter.

## Shared Governance

- [shared precedence](../../shared/precedence.md)
- [shared source map](../../shared/source-map.md)
- [shared escalation rules](../../shared/escalation-rules.md)
- [shared handoff contracts](../../shared/handoff-contracts.md)
- [shared project-selection policy](../../shared/project-selection-policy.md)

Read the shared governance files first when the task depends on workspace routing, project selection, or handoffs.

## Canonical Source

- [agent/inference_map.md](../../../automation/roles/quality_and_security_and_governance_manager/agent/inference_map.md)
- [agent/operating_rules.md](../../../automation/roles/quality_and_security_and_governance_manager/agent/operating_rules.md)
- [agent/output_contracts.md](../../../automation/roles/quality_and_security_and_governance_manager/agent/output_contracts.md)
- [agent/source_index.md](../../../automation/roles/quality_and_security_and_governance_manager/agent/source_index.md)

Read those files first. Do not treat this adapter as the source of truth.

## Workspace Context

- Read `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH` for `projects/registry.yaml`.
- Resolve project-specific context from `projects/<project-id>/hub/`.
- Read `SDLC_AUTOMATION_SHARED_HUB_PATH` for `hub/shared/`.
- Load role assets only after project and shared-hub context has been resolved.

## When To Use

Use this skill for:

- independent quality review and verification sufficiency checks
- security review and security-boundary risk framing
- governance mapping, evidence sufficiency review, and exception framing
- release-gate recommendations and approval-gap identification

Do not use this skill as the primary owner for product discovery, architecture design, implementation planning, or runtime operations.

## Output Expectations

- Make findings traceable to project or shared-hub evidence.
- Separate fact, inference, and `Assumption:` explicitly.
- Call out required approvals, exceptions, and unresolved control gaps.
- Name the handoff target when product, architecture, or deployment ownership is the real blocker.
- Route detailed artifacts into the selected project's `hub/issues/` or `hub/decisions/` areas when the task requires durable records.

## Update Rule

- When shared governance or the canonical role docs change, update this adapter, the agent card, and regenerate `.agents/registry.yaml`.
