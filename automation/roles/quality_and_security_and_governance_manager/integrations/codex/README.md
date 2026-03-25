# Codex Integration

This folder documents how the Quality and Security and Governance Manager package feeds the repo-local Codex skill.

## Live Skill Adapter

- invocation token: `$quality-and-security-and-governance-manager`
- registry entry: [`../../../../.agents/registry.yaml`](../../../../.agents/registry.yaml)
- shared governance: [`../../../../.agents/shared/README.md`](../../../../.agents/shared/README.md)
- skill instructions: [`../../../../.agents/skills/quality_and_security_and_governance_manager/SKILL.md`](../../../../.agents/skills/quality_and_security_and_governance_manager/SKILL.md)
- agent card: [`../../../../.agents/skills/quality_and_security_and_governance_manager/agents/openai.yaml`](../../../../.agents/skills/quality_and_security_and_governance_manager/agents/openai.yaml)

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
