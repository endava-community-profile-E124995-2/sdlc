# Agent Surface

This folder is the hot path for the Quality and Security and Governance Manager agent.

## Load Order

1. [inference_map.md](inference_map.md)
2. [operating_rules.md](operating_rules.md)
3. [output_contracts.md](output_contracts.md)
4. [source_index.md](source_index.md)
5. `../assets/training/fine_tuning/` for structured corpus support
6. `../assets/knowledge/legacy_role_rag/` only as fallback

## Workspace Context

- Resolve the target project from `projects/registry.yaml` before loading project hub context.
- Load shared cross-project context from `hub/shared/` when reusable policy or issue context is relevant.
- Load role assets only after project and shared-hub context has been checked.

## Role Focus

- independent quality review and verification sufficiency
- security boundary review and control-oriented risk framing
- governance mapping, evidence sufficiency, and exception framing
- release-gate recommendation with explicit handoffs
