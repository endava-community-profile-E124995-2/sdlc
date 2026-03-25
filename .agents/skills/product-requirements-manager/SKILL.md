---
name: product-requirements-manager
description: Thin adapter for product discovery, requirements shaping, prioritization, rollout readiness, and metrics work. Canonical logic lives under automation/roles/product_requirements_manager.
---

# Product and Requirements Manager

This skill is a thin repo-local adapter.

## Shared Governance

- [shared precedence](../../shared/precedence.md)
- [shared source map](../../shared/source-map.md)
- [shared escalation rules](../../shared/escalation-rules.md)
- [shared handoff contracts](../../shared/handoff-contracts.md)
- [shared project-selection policy](../../shared/project-selection-policy.md)

Read the shared governance files first when the task depends on workspace routing, project selection, or handoffs.

## Canonical Source

- [agent/inference_map.md](../../../automation/roles/product_requirements_manager/agent/inference_map.md)
- [agent/operating_rules.md](../../../automation/roles/product_requirements_manager/agent/operating_rules.md)
- [agent/output_contracts.md](../../../automation/roles/product_requirements_manager/agent/output_contracts.md)
- [agent/source_index.md](../../../automation/roles/product_requirements_manager/agent/source_index.md)

Read those files first for role-specific behavior. Do not treat this adapter as the source of truth.

## Workspace Context

- Read `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH` for `projects/registry.yaml`.
- Resolve project-specific context from `projects/<project-id>/hub/`.
- Read `SDLC_AUTOMATION_SHARED_HUB_PATH` for `hub/shared/`.
- Load role assets only after project and shared-hub context has been resolved.

## When To Use

Use this skill for:

- product discovery and problem framing
- PRD drafting or refinement and acceptance criteria shaping
- prioritization, launch readiness, and metrics design
- compliance-sensitive requirement mapping and stakeholder alignment

Do not use this skill as the primary owner for architecture, implementation design, coding, debugging, or approval decisions.

## Output Expectations

- Tie recommendations to concrete product context and available evidence.
- Separate fact, inference, and `Assumption:` explicitly.
- Call out missing business decisions, approvals, and downstream technical handoffs.
- Route durable product artifacts into the selected project's `hub/product/` area or `hub/shared/standards/` when the output becomes reusable policy.

## Update Rule

- When shared governance or the canonical role docs change, update this adapter, the agent card, and regenerate `.agents/registry.yaml`.

