# Fine-Tuning Workspace

This is the structured assistant-improvement workspace for the Product and Requirements Manager role.

## Contents

- `schema/`: canonical schemas for nodes, mesh cases, artifact contracts, metrics, and risks.
- `corpus/`: the structured training corpus used for retrieval shaping and fine-tuning examples.
- `evals/`: retrieval, behavior, and output-quality seed cases.
- `tooling/`: linting and validation support.
- `role_rag_rewrite_plan.md`: migration plan from the legacy role RAG into this structured workspace.

## Validation

Run:

```bash
python3 tooling/validate_seed_corpus.py
```
