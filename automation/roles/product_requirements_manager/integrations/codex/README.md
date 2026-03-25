# Codex Integration

This folder documents how the Product and Requirements Manager package feeds the repo-local Codex skill.

## Live Skill Adapter

- invocation token: `$product-requirements-manager`
- registry entry: [`../../../../.agents/registry.yaml`](../../../../.agents/registry.yaml)
- shared governance: [`../../../../.agents/shared/README.md`](../../../../.agents/shared/README.md)
- skill instructions: [`../../../../.agents/skills/product-requirements-manager/SKILL.md`](../../../../.agents/skills/product-requirements-manager/SKILL.md)
- agent card: [`../../../../.agents/skills/product-requirements-manager/agents/openai.yaml`](../../../../.agents/skills/product-requirements-manager/agents/openai.yaml)

## Package Mapping

- `../../agent/inference_map.md`: task routing and minimum-load order
- `../../agent/operating_rules.md`: behavior rules, escalation, and boundaries
- `../../agent/output_contracts.md`: output shape selection
- `../../agent/source_index.md`: minimum asset loading strategy
- `../../assets/`: backing corpus and legacy fallback material

## Shared Workspace Configuration

- Read `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH` to find `projects/registry.yaml`.
- Read `SDLC_AUTOMATION_SHARED_HUB_PATH` to find `hub/shared`.
- Resolve project hub and shared hub before role assets.

## Update Rule

When the manifest, shared governance pack, or repo-local adapter changes, regenerate `.agents/registry.yaml` and rerun `automation/tooling/validate_codex_agent_workspace.py`.
