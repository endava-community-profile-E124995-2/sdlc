---
name: architecture-and-engineering-manager
description: Thin adapter for technical feasibility, architecture design, engineering execution planning, dependency sequencing, and cross-role technical handoffs. Canonical logic lives under automation/roles/architecture_and_engineering_manager.
---

# Architecture And Engineering Manager

This skill is a thin repo-local adapter.

## Shared Governance

- [shared precedence](../../shared/precedence.md)
- [shared source map](../../shared/source-map.md)
- [shared escalation rules](../../shared/escalation-rules.md)
- [shared handoff contracts](../../shared/handoff-contracts.md)
- [shared project-selection policy](../../shared/project-selection-policy.md)

Read the shared governance files first when the task depends on workspace routing, project selection, or handoffs.

## Canonical Source

- [agent/inference_map.md](../../../automation/roles/architecture_and_engineering_manager/agent/inference_map.md)
- [agent/operating_rules.md](../../../automation/roles/architecture_and_engineering_manager/agent/operating_rules.md)
- [agent/output_contracts.md](../../../automation/roles/architecture_and_engineering_manager/agent/output_contracts.md)
- [agent/source_index.md](../../../automation/roles/architecture_and_engineering_manager/agent/source_index.md)

Read those files first. Do not treat this adapter as the source of truth.

## Workspace Context

- Read `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH` for `projects/registry.yaml`.
- Resolve project-specific context from `projects/<project-id>/hub/`.
- Read `SDLC_AUTOMATION_SHARED_HUB_PATH` for `hub/shared/`.
- Load role assets only after project and shared-hub context has been resolved.

## When To Use

Use this skill for:

- technical feasibility analysis
- architecture decisions and interface design
- engineering execution planning and dependency sequencing
- cross-role technical handoffs

Do not use this skill as the primary owner for product discovery, business prioritization, governance approval decisions, or runtime operations planning.

## Output Expectations

- Keep facts, inferences, and `Assumption:` labels separate.
- Tie recommendations to concrete project context and constraints.
- Identify dependencies, risks, and required handoffs explicitly.
- Route durable design artifacts into the selected project's `hub/technology/` or `hub/decisions/` areas when the task needs a persistent record.

## Update Rule

- When shared governance or the canonical role docs change, update this adapter, the agent card, and regenerate `.agents/registry.yaml`.
