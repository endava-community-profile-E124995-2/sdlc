# Agent Surface

This folder is the hot path for the Architecture and Engineering Manager agent. It should stay short, explicit, and cheaper to load than the asset packs behind it.

## Load Order

1. [inference_map.md](inference_map.md)
2. [operating_rules.md](operating_rules.md)
3. [output_contracts.md](output_contracts.md)
4. [source_index.md](source_index.md)
5. `../assets/` only as needed

## Responsibilities

- classify the technical task type
- define the output shape
- define when to ask clarifying questions
- define ownership boundaries and handoffs
- point to the minimum asset material needed for full coverage

## Project Context

- Shared project discovery comes from `SDLC_AUTOMATION_PROJECT_PATHS` in the repo-root `.env`.
- Treat the value as a JSON string array of repo-relative paths under `sdlc_automation\projects`.

## Information Hub Context

- Shared information-hub discovery comes from `SDLC_AUTOMATION_INFORMATION_HUB_PATHS` in the repo-root `.env`.
- Treat the value as a JSON string array of repo-relative paths under `sdlc_automation\information_hub`.

## Codex Relationship

- Package entrypoint: [inference_map.md](inference_map.md)
- Codex app adapter: [`../../../../../.agents/skills/architecture_and_engineering_manager/SKILL.md`](../../../../../.agents/skills/architecture_and_engineering_manager/SKILL.md)
- Backing asset packs: [../assets](../assets)
- Builder notes: [../builder](../builder)
