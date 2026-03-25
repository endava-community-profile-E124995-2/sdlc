# Codex Integration

This folder documents how the Quality and Security and Governance Manager package feeds the repo-local Codex skill.

## Live Skill Adapter

- Skill instructions: [`../../../../.agents/skills/quality_and_security_and_governance_manager/SKILL.md`](../../../../.agents/skills/quality_and_security_and_governance_manager/SKILL.md)
- Agent card: [`../../../../.agents/skills/quality_and_security_and_governance_manager/agents/openai.yaml`](../../../../.agents/skills/quality_and_security_and_governance_manager/agents/openai.yaml)
- Distilled references: `references/operating-policy.md`, `references/artifact-routing.md`, `references/interaction-cases.md`, and `references/context-variants.md`

## Shared Workspace Configuration

- Read `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH` to find `projects/registry.yaml`.
- Read `SDLC_AUTOMATION_SHARED_HUB_PATH` to find `hub/shared`.

## Source Of Truth

- Runtime behavior starts in `agent/inference_map.md`, `agent/operating_rules.md`, `agent/output_contracts.md`, and `agent/source_index.md`.
- The structured corpus under `assets/training/fine_tuning/` provides artifact contracts, examples, evals, variants, and validation tooling.
- The legacy fallback pack under `assets/knowledge/legacy_role_rag/` widens retrieval coverage only when the structured assets are insufficient.
