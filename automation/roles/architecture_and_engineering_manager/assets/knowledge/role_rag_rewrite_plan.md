# Architecture And Engineering Manager Role RAG Rewrite Plan

## Objective

Convert `assets/knowledge/legacy_role_rag` from a broad inherited reference pack into a production-grade retrieval and fine-tuning corpus for the Architecture and Engineering Manager agent.

## Current State Summary

- The legacy pack still provides useful technical vocabulary, stakeholder coverage, and risk language.
- The main weakness is that it behaves more like a static taxonomy than an assistant-ready operating corpus.
- Retrieval precision is limited by long list-heavy documents, repeated content, and mixed role boundaries.
- Several useful architecture and engineering concepts exist only as broad prose, not as structured cases or contracts.
- The runtime contract now lives in the thin `agent/` layer and the structured training corpus, so the legacy pack must remain fallback-only.

## Target Outcomes

- Retrieval returns small, high-signal chunks instead of giant inventories.
- Every retrieved stakeholder, artifact, metric, and risk resolves to a stable canonical ID.
- The assistant has explicit behavior rules for clarifying, escalating, structuring outputs, and handling cross-role handoffs.
- Technical artifact generation is backed by templates, worked examples, and anti-examples.
- The corpus supports both RAG and fine-tuning through consistent schemas and eval coverage.

## Primary Problems To Fix

1. Metadata is documented but not implemented as structured interaction cases.
2. Canonical naming is inconsistent across ontology and mesh layers.
3. Documents are too large and list-dense for precise retrieval.
4. Repetition adds noise to embeddings and weakens handoff accuracy.
5. Metrics and risks need to become operational decision assets instead of loose labels.
6. The pack needs explicit refusal and handoff rules across product, governance, and operations boundaries.

## Target Corpus Shape

The rewritten corpus should separate reference data, operating policy, technical templates, exemplars, and evaluation assets.

```text
02_architecture_and_engineering_manager/
  agent/
    inference_map.md
  assets/
    knowledge/
      legacy_role_rag/
    training/
      fine_tuning/
        role_rag_rewrite_plan.md
        schema/
          role_node_schema.md
          mesh_case_schema.md
          artifact_contract_schema.md
        corpus/
          ontology/
          interactions/
          artifacts/
          metrics/
          risks/
          policies/
          variants/
          examples/
        evals/
          retrieval_queries/
          behavior_cases/
          output_quality/
        tooling/
          linting_rules.md
          migration_checklist.md
```

## Planned Workstreams

- Canonical ontology normalization for architecture, execution, and handoff concepts.
- Structured rebuild of high-frequency engineering interaction cases.
- Operating policy that preserves technical ownership and explicit cross-role handoffs.
- Artifact contracts for feasibility briefs, ADRs, execution plans, and handoff notes.
- Metric and risk cards that help architecture and planning decisions stay measurable.
- Variant packs that adapt depth, governance, cadence, and risk weighting by context.
- Eval suites and linting that catch broken references, drift, and boundary failures.

## Success Metrics For This Rewrite

- Retrieval precision improves for architecture- and planning-specific prompts.
- Duplicate or conflicting ontology terms drop to near zero.
- Every structured case validates against schema and canonical IDs.
- The assistant routes ambiguous business intent back to product instead of inventing missing scope.
- The assistant routes control questions and operability work to the correct downstream role.

## Immediate Next Step

Keep migrating the most reused architecture and execution patterns out of the legacy pack into structured corpus records, while preserving the legacy pack as fallback-only reference material.

