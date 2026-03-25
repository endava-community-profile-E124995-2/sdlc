# Codex Integration

This folder documents how the Deployment and Operations Manager package feeds the repo-local Codex skill.

## Live Skill Adapter

- Skill instructions: [`../../../../.agents/skills/deployment_and_operations_manager/SKILL.md`](../../../../.agents/skills/deployment_and_operations_manager/SKILL.md)
- Agent card: [`../../../../.agents/skills/deployment_and_operations_manager/agents/openai.yaml`](../../../../.agents/skills/deployment_and_operations_manager/agents/openai.yaml)
- Distilled references: `references/operating-policy.md`, `references/artifact-routing.md`, `references/interaction-cases.md`, and `references/context-variants.md`

## Shared Workspace Configuration

- Read `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH` to find `projects/registry.yaml`.
- Read `SDLC_AUTOMATION_SHARED_HUB_PATH` to find `hub/shared`.

## Source Of Truth

- Runtime behavior starts in `agent/inference_map.md`, `agent/operating_rules.md`, `agent/output_contracts.md`, and `agent/source_index.md`.
- The structured corpus under `assets/training/fine_tuning/` provides artifact contracts, examples, evals, variants, and validation tooling.
- The legacy fallback pack under `assets/knowledge/legacy_role_rag/` widens retrieval coverage only when the structured assets are insufficient.
*** Add File: automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/README.md
# Fine-Tuning Workspace

This is the structured assistant-improvement workspace for the Deployment and Operations Manager role.

## Contents

- `schema/`: canonical schemas for nodes, mesh cases, artifact contracts, metrics, and risks
- `corpus/`: the structured training corpus used for retrieval shaping and fine-tuning examples
- `evals/`: retrieval, behavior, and output-quality seed cases
- `tooling/`: linting and validation support

## Validation

Run:

```bash
python tooling/validate_seed_corpus.py
```
