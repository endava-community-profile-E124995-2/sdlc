# Codex-Driven SDLC Workspace

This repository is a workspace for running an automated, role-based SDLC process with OpenAI Codex. It is organized around three first-class concepts:

- `automation/`: the Codex automation engine, role packages, workflows, templates, and operating guides
- `projects/`: attached project records and local attachment metadata for linked repos
- `hub/shared/`: reusable cross-project context such as standards, analytics, issues, assets, and portfolio views

## Workspace Model

- Attached product repos are linked, not embedded. Committed metadata lives in this repo, while machine-specific checkout bindings live in ignored `attachment.local.yaml` files under each project.
- Shared context is split by scope. Cross-project material belongs in `hub/shared/`; detailed product and technical context belongs in `projects/<project-id>/hub/`.
- Role packages under `automation/roles/` are canonical. Repo-local skill adapters under `.agents/skills/` should remain thin pointers to those sources.

## Onboarding A Project

1. Add an entry to `projects/registry.yaml`.
2. Create `projects/<project-id>/project.yaml`.
3. Create the project hub skeleton under `projects/<project-id>/hub/`.
4. Optionally create an untracked `projects/<project-id>/attachment.local.yaml` from the example template.

## Context Resolution Order

Codex tasks should resolve context in this order:

1. selected project hub
2. shared hub
3. role package assets
