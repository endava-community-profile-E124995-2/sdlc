# About This Role Package

This folder is the canonical Quality and Security and Governance Manager package for the workspace-first Codex SDLC model.

## Structure

- `agent/`: active docs Codex should read first
- `assets/`: backing notes and role-specific guidance
- `builder/`: maintenance notes for humans
- `integrations/`: mapping to the repo-local skill adapter

## Design Intent

- Keep `agent/` small and decisive so routing and boundaries stay stable.
- Store repeatable review behavior, contracts, examples, and evals under `assets/training/fine_tuning/`.
- Keep `assets/knowledge/legacy_role_rag/` as fallback-only reference material for retrieval expansion.
