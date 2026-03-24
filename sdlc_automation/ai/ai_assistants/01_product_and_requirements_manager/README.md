# Product And Requirements Manager Assistant

This folder is organized as an assistant builder workspace rather than a loose document drop.

## Structure

```text
01_product_and_requirements_manager/
  README.md
  assistant_manifest.md
  runtime/
    README.md
    inference_map.md
  knowledge/
    README.md
    legacy_role_rag/
  training/
    README.md
    fine_tuning/
```

## What Lives Where

- `runtime/`: inference-time routing, response shaping, and retrieval precedence.
- `knowledge/legacy_role_rag/`: the original broad role reference pack kept as a fallback knowledge source.
- `training/fine_tuning/`: the structured corpus, schemas, examples, evals, and tooling used to improve the assistant.

## Builder Workflow

1. Use [runtime/inference_map.md](/Users/bviljevac/ai-projects/codex_automation_sdlc/sdlc_automation/ai/ai_assistants/01_product_and_requirements_manager/runtime/inference_map.md) to define how requests should be routed at inference time.
2. Use [interaction_map/individual/interact_product_and_requirements_manager.md](/Users/bviljevac/ai-projects/codex_automation_sdlc/sdlc_automation/ai/interaction_map/individual/interact_product_and_requirements_manager.md) to drive Plan Mode intake with staged option prompts before drafting a plan.
3. Use [training/fine_tuning/corpus](/Users/bviljevac/ai-projects/codex_automation_sdlc/sdlc_automation/ai/ai_assistants/01_product_and_requirements_manager/training/fine_tuning/corpus) as the primary structured source for assistant behavior.
4. Use [knowledge/legacy_role_rag](/Users/bviljevac/ai-projects/codex_automation_sdlc/sdlc_automation/ai/ai_assistants/01_product_and_requirements_manager/knowledge/legacy_role_rag) as fallback coverage and migration source material.
5. Validate corpus integrity with `python3 training/fine_tuning/tooling/validate_seed_corpus.py`.

## Current State

- Runtime layout is now explicit.
- Legacy reference material is separated from structured training assets.
- Fine-tuning assets include schemas, contracts, structured mesh cases, examples, evals, and validation tooling.
