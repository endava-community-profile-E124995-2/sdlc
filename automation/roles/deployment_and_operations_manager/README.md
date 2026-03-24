# Deployment And Operations Manager

This package is the canonical deployment and operations role definition for the Codex SDLC workspace. The repo-local adapter lives at [`../../../.agents/skills/deployment_and_operations_manager`](../../../.agents/skills/deployment_and_operations_manager), while this folder holds the source-of-truth agent contract and assets.

## Active Surface

- `agent/manifest.md`: package metadata, entrypoint, and workspace context model
- `agent/inference_map.md`: routing for release planning, rollout, operability, and operations handoff work
- `agent/operating_rules.md`: clarify-first behavior, assumptions, and role boundaries
- `agent/output_contracts.md`: response shapes by task type
- `agent/source_index.md`: minimum supporting sources and workspace context rules
