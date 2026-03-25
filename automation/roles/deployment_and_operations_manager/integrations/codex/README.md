# Codex Integration

This folder documents how the Deployment and Operations Manager package feeds the repo-local Codex skill.

## Live Skill Adapter

- invocation token: `$deployment-and-operations-manager`
- registry entry: [`../../../../.agents/registry.yaml`](../../../../.agents/registry.yaml)
- shared governance: [`../../../../.agents/shared/README.md`](../../../../.agents/shared/README.md)
- skill instructions: [`../../../../.agents/skills/deployment_and_operations_manager/SKILL.md`](../../../../.agents/skills/deployment_and_operations_manager/SKILL.md)
- agent card: [`../../../../.agents/skills/deployment_and_operations_manager/agents/openai.yaml`](../../../../.agents/skills/deployment_and_operations_manager/agents/openai.yaml)

## Shared Workspace Configuration

- Read `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH` to find `projects/registry.yaml`.
- Read `SDLC_AUTOMATION_SHARED_HUB_PATH` to find `hub/shared`.
- Resolve project hub and shared hub before role assets.

## Source Of Truth

- Runtime behavior starts in `agent/inference_map.md`, `agent/operating_rules.md`, `agent/output_contracts.md`, and `agent/source_index.md`.
- The structured corpus under `assets/training/fine_tuning/` provides artifact contracts, examples, evals, variants, and validation tooling.
- The legacy fallback pack under `assets/knowledge/legacy_role_rag/` widens retrieval coverage only when the structured assets are insufficient.

## Update Rule

When the manifest, shared governance pack, or repo-local adapter changes, regenerate `.agents/registry.yaml` and rerun `automation/tooling/validate_codex_agent_workspace.py`.
