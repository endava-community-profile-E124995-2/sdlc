# Codex App Migration Plan

## Summary

- Persist the Architecture and Engineering Manager role as a repo-local Codex skill at `.agents/skills/architecture_and_engineering_manager`.
- Keep this agent package split into a thin active layer under `agent/` and broader source material under `assets/`.
- Use the Codex skill as a thin runtime adapter that loads distilled references on demand instead of embedding the full corpus.
- Add a repo-root `AGENTS.md` rule that routes architecture ownership and engineering planning work to the skill without turning the whole repository into a single-role prompt.

## Decisions

- Skill name: `architecture-and-engineering-manager`
- Display name: `Architecture and Engineering Manager`
- Placement: repo-local only in v1
- Activation: hybrid auto plus explicit invocation
- Source-of-truth runtime behavior: `agent/inference_map.md` and the structured corpus under `assets/training/fine_tuning/corpus`
- Fallback knowledge: `assets/knowledge/legacy_role_rag`

## Target Deliverables

1. `.agents/skills/architecture_and_engineering_manager/SKILL.md`
2. `.agents/skills/architecture_and_engineering_manager/agents/openai.yaml`
3. `.agents/skills/architecture_and_engineering_manager/references/operating-policy.md`
4. `.agents/skills/architecture_and_engineering_manager/references/artifact-routing.md`
5. `.agents/skills/architecture_and_engineering_manager/references/interaction-cases.md`
6. `.agents/skills/architecture_and_engineering_manager/references/context-variants.md`
7. `AGENTS.md`
8. README updates in this agent package so the Codex-facing adapter is discoverable, the active-layer structure is clear, and stale links are removed

## Implementation Rules

- Keep the skill instruction-only in v1.
- Distill runtime behavior into the skill and reference files instead of copying the full archived training corpus.
- Preserve role boundaries:
  - use this role for technical feasibility, architecture decisions, implementation planning, dependency sequencing, and technical handoffs
  - do not use this role to replace product intent ownership, governance approvals, or runtime operations ownership
- Load only the reference file needed for the current task.
- Apply no more than one context variant unless the request clearly spans multiple environments.

## Execution Order

1. Store this migration plan in `builder/migration/`.
2. Create the repo-local Codex skill structure.
3. Distill the operating policy, routing rules, interaction cases, and variants into skill references.
4. Add repo-root routing guidance in `AGENTS.md`.
5. Extract broad knowledge and training material into `assets/`.
6. Update agent docs to reflect the thin active layer and the backing asset material.
7. Validate the asset corpus and smoke-check the new skill files.

## Verification

- Run `python sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/tooling/validate_seed_corpus.py`
- Verify the skill is discoverable from the repo root in Codex app.
- Verify explicit invocation with `$architecture-and-engineering-manager`.
- Verify implicit routing for feasibility analysis, ADR drafting, engineering planning, and cross-role handoffs.
- Verify the skill preserves boundaries against product ambiguity, approval decisions, and operations ownership.

## Maintenance Notes

- Update the skill references when the source agent map, policy, contracts, or interaction cases materially change.
- Keep the full corpus, evals, and tooling under `assets/` inside this agent package.
- Treat the Codex skill as the app-facing adapter, not as the replacement authoring location.

