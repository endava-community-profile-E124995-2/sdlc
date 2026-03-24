---
name: product-requirements-manager
description: Thin adapter for product discovery, requirements shaping, prioritization, rollout readiness, and metrics work. Canonical logic lives under automation/roles/product_requirements_manager.
---

# Product and Requirements Manager

This skill is a thin repo-local adapter.

## Source Of Truth

- [agent/inference_map.md](../../../automation/roles/product_requirements_manager/agent/inference_map.md)
- [agent/operating_rules.md](../../../automation/roles/product_requirements_manager/agent/operating_rules.md)
- [agent/output_contracts.md](../../../automation/roles/product_requirements_manager/agent/output_contracts.md)
- [agent/source_index.md](../../../automation/roles/product_requirements_manager/agent/source_index.md)

## Workspace Context

- Read `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH` for `projects/registry.yaml`.
- Resolve project-specific context from `projects/<project-id>/hub/`.
- Read `SDLC_AUTOMATION_SHARED_HUB_PATH` for `hub/shared/`.

