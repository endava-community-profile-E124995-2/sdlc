---
name: quality-and-security-and-governance-manager
description: Thin adapter for quality review, security review, governance mapping, and release-gate work. Canonical logic lives under automation/roles/quality_and_security_and_governance_manager.
---

# Quality And Security And Governance Manager

This skill is a thin repo-local adapter.

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

- quality review and test-readiness checks
- security review and control mapping
- governance-sensitive requirement traceability
- release-gate recommendations and exception framing

Do not use this skill as the primary owner for product discovery, architecture design, implementation planning, or runtime operations.

## Output Expectations

- Make findings traceable to project or shared-hub evidence.
- Separate fact, inference, and `Assumption:` explicitly.
- Call out required approvals, exceptions, and unresolved control gaps.
- Route detailed artifacts into the selected project's `hub/issues/` or `hub/decisions/` areas when the task requires durable records.
