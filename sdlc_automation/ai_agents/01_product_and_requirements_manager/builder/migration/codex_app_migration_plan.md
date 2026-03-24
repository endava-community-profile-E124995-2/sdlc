# Codex App Migration Plan

## Summary

- Persist the Product and Requirements Manager role as a repo-local Codex skill at `.agents/skills/product-requirements-manager`.
- Keep this agent package split into a thin active layer under `agent/` and broader source material under `assets/`.
- Use the Codex skill as a thin runtime adapter that loads distilled references on demand instead of embedding the full corpus.
- Add a repo-root `AGENTS.md` that lightly routes product and requirements work to the skill without turning the whole repository into a PM-only prompt.

## Decisions

- Skill name: `product-requirements-manager`
- Display name: `Product and Requirements Manager`
- Placement: repo-local only in v1
- Activation: hybrid auto plus explicit invocation
- Source-of-truth runtime behavior: `agent/inference_map.md` and the structured corpus under `assets/training/fine_tuning/corpus`
- Fallback knowledge: `assets/knowledge/legacy_role_rag`

## Target Deliverables

1. `.agents/skills/product-requirements-manager/SKILL.md`
2. `.agents/skills/product-requirements-manager/agents/openai.yaml`
3. `.agents/skills/product-requirements-manager/references/operating-policy.md`
4. `.agents/skills/product-requirements-manager/references/artifact-routing.md`
5. `.agents/skills/product-requirements-manager/references/interaction-cases.md`
6. `.agents/skills/product-requirements-manager/references/context-variants.md`
7. `AGENTS.md`
8. README updates in this agent package so the Codex-facing adapter is discoverable, the active-layer structure is clear, and stale links are removed

## Implementation Rules

- Keep the skill instruction-only in v1.
- Distill runtime behavior into the skill and reference files instead of copying the full archived training corpus.
- Preserve role boundaries:
  - use this role for discovery, requirements, prioritization, rollout readiness, metrics, and governance-sensitive requirement mapping
  - do not use this role as the owner of architecture, implementation design, coding, or approval decisions
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

- Run `python sdlc_automation/ai_agents/01_product_and_requirements_manager/assets/training/fine_tuning/tooling/validate_seed_corpus.py`
- Verify the skill is discoverable from the repo root in Codex app.
- Verify explicit invocation with `$product-requirements-manager`.
- Verify implicit routing for product discovery, PRD refinement, prioritization, launch readiness, and metric design.
- Verify the skill preserves boundaries on architecture ownership and approval decisions.

## Maintenance Notes

- Update the skill references when the source agent map, policy, contracts, or interaction cases materially change.
- Keep the full corpus, evals, and tooling under `assets/` inside this agent package.
- Treat the Codex skill as the app-facing adapter, not as the replacement authoring location.

