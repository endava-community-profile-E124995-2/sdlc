# Workspace Tooling

This folder stores workspace-level tooling that applies across role packages.

## Scripts

- `generate_agent_registry.py`: generates `.agents/registry.yaml` from canonical role manifests and repo-local skill adapters
- `validate_codex_agent_workspace.py`: validates shared governance, adapter parity, routing tokens, and generated registry consistency

Run these scripts from the repo root.
