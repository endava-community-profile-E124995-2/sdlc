---
name: deployment-and-operations-manager
description: Thin adapter for release planning, rollout, operability, and support handoff work. Canonical logic lives under automation/roles/deployment_and_operations_manager.
---

# Deployment And Operations Manager

This skill is a thin repo-local adapter.

## Canonical Source

- [agent/inference_map.md](../../../automation/roles/deployment_and_operations_manager/agent/inference_map.md)
- [agent/operating_rules.md](../../../automation/roles/deployment_and_operations_manager/agent/operating_rules.md)
- [agent/output_contracts.md](../../../automation/roles/deployment_and_operations_manager/agent/output_contracts.md)
- [agent/source_index.md](../../../automation/roles/deployment_and_operations_manager/agent/source_index.md)

Read those files first. Do not treat this adapter as the source of truth.

## Workspace Context

- Read `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH` for `projects/registry.yaml`.
- Resolve project-specific context from `projects/<project-id>/hub/`.
- Read `SDLC_AUTOMATION_SHARED_HUB_PATH` for `hub/shared/`.
- Load role assets only after project and shared-hub context has been resolved.

## When To Use

Use this skill for:

- release planning and rollout sequencing
- operational readiness, rollback, and runbook framing
- deployment risk review and post-release follow-up
- support handoff and post-release ownership checks

Do not use this skill as the primary owner for product discovery, architecture design, implementation planning, or governance approval decisions.

## Output Expectations

- Tie rollout guidance to concrete project artifacts and owners.
- State assumptions and unresolved dependencies explicitly.
- Define monitoring, rollback, and support expectations when relevant.
- Name the handoff target when product, architecture, or quality owns the blocker.
- Route durable operations artifacts into the selected project's `hub/technology/`, `hub/issues/`, or `hub/decisions/` areas as appropriate.
