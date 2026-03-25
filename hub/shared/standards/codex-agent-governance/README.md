# Codex Agent Governance

This folder is the canonical shared-governance pack for repo-local Codex app agents in this workspace.

## Purpose

- define cross-role instruction precedence
- separate behavioral source of truth from factual context
- standardize handoffs, validation, and project selection
- keep `.agents/shared/` thin and app-facing

## Canonical Rule

- Durable cross-role governance belongs here.
- Repo-local files under `.agents/shared/` are thin adapters and should summarize or point back here.
- Role-specific behavior still belongs in `automation/roles/*/agent/`.

## Contents

- `precedence.md`
- `source-map.md`
- `response-format.md`
- `escalation-rules.md`
- `handoff-contracts.md`
- `validation-checklist.md`
- `tool-access-rules.md`
- `project-selection-policy.md`

## Update Rule

When the cross-role operating model changes, update this folder first, then update `.agents/shared/`, affected role adapters, `.agents/registry.yaml`, and workspace validation outputs in the same change.
