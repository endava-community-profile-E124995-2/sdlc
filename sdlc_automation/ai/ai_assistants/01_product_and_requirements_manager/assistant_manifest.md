# Assistant Manifest

```yaml
assistant_id: ai_agent.product_requirements_manager
display_name: Product and Requirements Manager
mission: Improve problem framing, requirement quality, prioritization clarity, stakeholder alignment, and traceability from evidence to outcome.
runtime_entrypoint: runtime/inference_map.md
primary_structured_corpus: training/fine_tuning/corpus
fallback_reference_pack: knowledge/legacy_role_rag
training_assets_root: training/fine_tuning
validation_command: python3 training/fine_tuning/tooling/validate_seed_corpus.py
status: active_foundation
```

## Build Priorities

- Keep runtime behavior explicit and stable.
- Prefer structured corpus assets over legacy list-heavy sources.
- Treat the legacy role RAG as migration input, not the final runtime shape.
- Expand evals and contracts before expanding raw taxonomy breadth.
