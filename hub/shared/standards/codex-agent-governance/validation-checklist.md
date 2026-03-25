# Validation Checklist

## Shared Governance

- the canonical governance pack exists under `hub/shared/standards/codex-agent-governance/`
- `.agents/shared/` exists and points back to the canonical governance pack

## Role Adapter Parity

- every active role package has `agent/manifest.md`
- every active role package has a repo-local `SKILL.md`
- every repo-local skill has an `agents/openai.yaml`
- every repo-local skill is represented in `.agents/registry.yaml`

## Routing And Boundaries

- `AGENTS.md` routes all live roles
- mixed-domain requests have an explicit handoff rule
- deployment and operations is treated as a first-class role, not an unowned fallback

## Validation And Evals

- every active role has a validation command
- workspace registry validation passes
- system eval prompts cover explicit invocation, implicit routing, handoffs, and projectless mode
