# Codex Integration

This folder documents how the Architecture and Engineering Manager package feeds the OpenAI Codex app skill.

## Live Skill Adapter

- Skill instructions: [`../../../../.agents/skills/architecture_and_engineering_manager/SKILL.md`](../../../../.agents/skills/architecture_and_engineering_manager/SKILL.md)
- Agent card: [`../../../../.agents/skills/architecture_and_engineering_manager/agents/openai.yaml`](../../../../.agents/skills/architecture_and_engineering_manager/agents/openai.yaml)

## Package Mapping

- `../../agent/inference_map.md`: task routing and minimum-load order
- `../../agent/operating_rules.md`: behavior rules, escalation, ownership, and handoffs
- `../../agent/output_contracts.md`: output shape selection
- `../../agent/source_index.md`: minimum asset loading strategy
- `../../assets/`: backing corpus and legacy fallback material

## Shared Workspace Configuration

- The package and the repo-local skill should both read `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH` to find `projects/registry.yaml`.
- The package and the repo-local skill should both read `SDLC_AUTOMATION_SHARED_HUB_PATH` to find `hub/shared`.
- Project-specific hub context should be resolved before shared-hub context, and both should resolve before role assets.

## Update Rule

When the active agent surface changes, update the repo-local skill references in `.agents/skills/architecture_and_engineering_manager` in the same change.
