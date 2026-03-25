# Codex App Migration Plan

## Summary

- Persist the Deployment and Operations Manager role as a repo-local Codex skill at `.agents/skills/deployment_and_operations_manager`.
- Keep this agent package split into a thin active layer under `agent/` and a broader structured corpus under `assets/`.
- Use the live skill as a thin runtime adapter that loads shared governance from `.agents/shared/` and distilled role references on demand instead of copying the full corpus into the skill.
- Align repo routing so release-planning, rollout-readiness, operations handoff, and post-release review work land on this role rather than remaining mixed into product, architecture, or quality surfaces.

## Decisions

- Skill name: `deployment-and-operations-manager`
- Display name: `Deployment and Operations Manager`
- Placement: repo-local only in v1
- Activation: hybrid auto plus explicit invocation
- Shared governance source: `hub/shared/standards/codex-agent-governance/`
- Source-of-truth runtime behavior: `agent/inference_map.md` and the structured corpus under `assets/training/fine_tuning/corpus`
- Fallback knowledge: `assets/knowledge/legacy_role_rag`

## Target Deliverables

1. `.agents/skills/deployment_and_operations_manager/SKILL.md`
2. `.agents/skills/deployment_and_operations_manager/agents/openai.yaml`
3. `.agents/skills/deployment_and_operations_manager/references/operating-policy.md`
4. `.agents/skills/deployment_and_operations_manager/references/artifact-routing.md`
5. `.agents/skills/deployment_and_operations_manager/references/interaction-cases.md`
6. `.agents/skills/deployment_and_operations_manager/references/context-variants.md`
7. `.agents/shared/`
8. `.agents/registry.yaml`
9. `AGENTS.md`
10. package README updates and the structured deployment corpus under `assets/training/fine_tuning/`

## Implementation Rules

- Keep the skill instruction-only in v1.
- Distill runtime behavior into the skill and reference files instead of copying the full corpus.
- Read shared governance before role-specific docs when the task depends on routing, handoffs, or project selection.
- Preserve role boundaries:
  - use this role for rollout planning, rollback readiness, observability, runbooks, support handoff, and post-release operational follow-up
  - do not use this role to replace product launch framing, architecture ownership, or quality gate ownership
- Load only the reference file needed for the current task.
- Apply no more than one context variant unless the request clearly spans multiple environments.
- Regenerate `.agents/registry.yaml` whenever the deployment adapter, manifest, or invocation token changes.

## Verification

- Run `python assets/training/fine_tuning/tooling/validate_seed_corpus.py`.
- Run `python automation/tooling/generate_agent_registry.py`.
- Run `python automation/tooling/validate_codex_agent_workspace.py`.
- Verify the skill is discoverable from the repo root in Codex app.
- Verify explicit invocation with `$deployment-and-operations-manager`.
- Verify implicit routing for rollout planning, operability review, support handoff, and post-release follow-up.
- Verify the role hands back to product, architecture, or quality when ownership is outside deployment and operations.

## Maintenance Notes

- Update the deployment adapter and `.agents/registry.yaml` whenever the manifest or shared governance pack changes.
- Treat `.agents/skills/deployment_and_operations_manager` as an adapter surface, not as the canonical authoring location.
