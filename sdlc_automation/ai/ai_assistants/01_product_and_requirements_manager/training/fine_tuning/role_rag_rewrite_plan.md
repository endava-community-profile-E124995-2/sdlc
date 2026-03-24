# Product and Requirements Manager Role RAG Rewrite Plan

## Objective

Convert `knowledge/legacy_role_rag` from a broad reference pack into a production-grade retrieval and fine-tuning corpus for the Product and Requirements Manager assistant.

## Current State Summary

- The current pack has strong coverage across role scope, stakeholders, artifacts, methods, metrics, risks, and relationship patterns.
- The main weakness is that it behaves more like a taxonomy library than an assistant-ready operating corpus.
- Retrieval precision is limited by long list-heavy documents, repeated content, and inconsistent naming between files.
- The relationship mesh declares retrieval metadata conventions, but the actual cases do not instantiate those fields in a structured way.
- Several mesh labels are not canonical ontology entries, which weakens grounding and makes maintenance harder.
- The pack contains good reasoning guidance, but that guidance is scattered instead of being expressed as one assistant runtime policy.

## Target Outcomes

- Retrieval returns small, high-signal chunks instead of giant inventories.
- Every retrieved skill, stakeholder, artifact, metric, and risk resolves to a stable canonical ID.
- The assistant has explicit behavior rules for clarifying, escalating, structuring outputs, and handling uncertainty.
- Artifact generation is backed by templates, worked examples, and anti-examples.
- The corpus supports both RAG and fine-tuning through consistent schemas and eval coverage.

## Primary Problems To Fix

1. Metadata is documented but not implemented in the mesh.
2. Canonical naming is inconsistent across ontology and mesh layers.
3. Documents are too large and list-dense for precise retrieval.
4. Repetition and compressed summary sections add noise to embeddings.
5. Metrics and risks are mostly labels, not operational decision assets.
6. Tools and cadences are generic and not expressed as usable operating contracts.
7. Context-specific variants like startup, enterprise, platform, regulated, and AI product are not modeled as distinct assistant modes.
8. There is no visible linting or eval layer for this role pack.

## Target Corpus Shape

The rewritten corpus should separate reference data, operating policy, templates, exemplars, and evaluation assets.

```text
01_product_and_requirements_manager/
  runtime/
    inference_map.md
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
        stakeholders/
        interactions/
        artifacts/
        methods/
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

## Required Schemas

### 1. Canonical role node schema

Each ontology node should include:

- `id`
- `node_type`
- `name`
- `aliases`
- `definition`
- `when_to_use`
- `when_not_to_use`
- `related_ids`
- `priority`
- `confidence`
- `source_file`

### 2. Mesh case schema

Each stakeholder-interaction case should include:

- `id`
- `stakeholder_group_id`
- `interaction_id`
- `phase_tags`
- `artifact_tags`
- `method_tags`
- `metric_tags`
- `risk_tags`
- `activated_capability_ids`
- `activated_knowledge_area_ids`
- `input_signals`
- `expected_outputs`
- `escalation_triggers`
- `example_prompt`
- `priority`
- `confidence`

### 3. Artifact contract schema

Each artifact type should include:

- `id`
- `artifact_name`
- `purpose`
- `required_sections`
- `optional_sections`
- `minimum_quality_bar`
- `common_failure_modes`
- `good_example_ref`
- `bad_example_ref`

### 4. Metric card schema

Each metric should include:

- `id`
- `metric_name`
- `definition`
- `formula_or_logic`
- `owner`
- `data_source`
- `baseline_needed`
- `leading_or_lagging`
- `anti_patterns`
- `interpretation_notes`

### 5. Risk card schema

Each risk should include:

- `id`
- `risk_name`
- `definition`
- `trigger_signals`
- `impact_area`
- `likelihood_notes`
- `mitigation_actions`
- `escalation_path`
- `related_metric_ids`

## Planned Workstreams

### Workstream 1: Canonical ontology normalization

- Assign stable IDs to every capability, knowledge area, behavior, specialization, stakeholder, interaction, artifact, method, metric, and risk.
- Remove duplicate labels and merge near-duplicates under one canonical name with aliases.
- Replace raw string references in the mesh with canonical IDs.
- Add a lightweight glossary for overloaded terms like requirement, backlog, launch, adoption, and roadmap.

### Workstream 2: Corpus chunking and deduplication

- Break large markdown inventories into atomic retrieval units.
- Keep each chunk focused on one concept, one contract, or one scenario.
- Remove repeated "Simplified Master List" sections from the main retrieval corpus.
- Move compressed summaries into separate reference-only files if they still have value.

### Workstream 3: Assistant operating policy

- Create one policy file that defines how the assistant should behave.
- Include clarifying-question rules.
- Include assumption labeling rules.
- Include escalation triggers.
- Include output formatting rules by task type.
- Include source precedence rules when multiple chunks are retrieved.
- Include explicit refusal and handoff rules for legal, security, compliance, finance, and implementation ownership boundaries.

### Workstream 4: Artifact contracts and exemplars

- Turn high-value outputs into contract-driven assets.
- Add templates for discovery brief, strategy brief, PRD, decision memo, launch brief, KPI spec, and post-launch review.
- Add one good example and one failure-pattern example for each major artifact.
- Tag each example by context such as B2B workflow, platform, enterprise, or regulated work.

### Workstream 5: Operational metrics and risks

- Convert metric lists into metric cards with formulas, prerequisites, and interpretation guidance.
- Convert risk lists into risk cards with triggers, impact, mitigation, and escalation.
- Link each artifact type to the metrics and risks most likely to matter.
- Link launch and post-launch artifacts back to expected outcomes and evidence rules.

### Workstream 6: Context variants

- Add variant packs for startup, scale-up, enterprise, platform, regulated, internal tooling, and AI product contexts.
- Each variant should override stakeholders, artifact depth, governance level, and cadence expectations.
- Keep the general ontology stable while layering context-specific behavior on top.

### Workstream 7: Evals and linting

- Add lint checks for missing IDs, missing aliases, broken references, duplicate labels, and non-canonical mesh references.
- Add retrieval evals to verify the right chunks are returned for realistic prompts.
- Add behavior evals for ambiguity, scope pressure, weak evidence, regulated changes, missing instrumentation, and sales-driven roadmap distortion.
- Add output evals for PRDs, decision memos, risk reviews, and launch readiness summaries.

## Migration Sequence

### Phase 1: Inventory and normalization

- Freeze the current pack as the baseline.
- Produce canonical ID maps for all existing nodes.
- Identify duplicates, near-duplicates, and missing canonical definitions.
- Exit criterion: every concept has one canonical name and stable ID.

### Phase 2: Structured mesh rebuild

- Rebuild `06_relationship_mesh.md` into structured case records.
- Attach actual metadata fields instead of only describing the convention.
- Validate all case references against ontology IDs.
- Exit criterion: every case passes schema validation.

### Phase 3: Policy and contract layer

- Create the assistant operating policy.
- Create artifact contracts for major outputs.
- Add worked examples and anti-examples.
- Exit criterion: high-frequency tasks have both policy and artifact support.

### Phase 4: Metrics, risks, and variants

- Convert metric and risk lists into operational cards.
- Add context variants for common product environments.
- Exit criterion: the assistant can adapt depth and governance behavior by context.

### Phase 5: Evals and release hardening

- Add retrieval, behavior, and output eval suites.
- Add linting and migration checklists.
- Run regression checks against representative user prompts.
- Exit criterion: the pack is measurable, maintainable, and safe to evolve.

## Proposed First Deliverables

1. `assistant_operating_policy.md`
2. `canonical_id_map.md`
3. `mesh_case_schema.md`
4. `artifact_contracts/discovery_brief.md`
5. `artifact_contracts/prd.md`
6. `artifact_contracts/decision_memo.md`
7. `metrics/adoption_rate.md`
8. `risks/ambiguous_requirements.md`
9. `evals/retrieval_queries/core_queries.md`
10. `tooling/linting_rules.md`

## Suggested Fine-Tuning Example Families

- Clarify ambiguous product requests before drafting requirements.
- Refuse to treat stakeholder demands as validated needs without evidence.
- Convert discovery evidence into problem framing and next validation steps.
- Turn rough feature requests into scoped, testable requirement sets.
- Produce decision memos that include options, trade-offs, and explicit rationale.
- Surface missing metrics and instrumentation before claiming success criteria.
- Escalate appropriately when compliance, legal, security, or budget ambiguity changes the recommendation.
- Push back on implementation detail ownership while still helping define intent and constraints.

## Success Metrics For This Rewrite

- Retrieval precision improves for stakeholder-specific and artifact-specific prompts.
- Duplicate or conflicting ontology terms drop to near zero.
- Every mesh case validates against schema and canonical IDs.
- The assistant asks better clarifying questions under ambiguity.
- Generated artifacts meet output contracts more consistently.
- Eval pass rates remain stable as the corpus evolves.

## Immediate Next Step

Start with canonical ID mapping and a structured rewrite of the relationship mesh. That is the highest-leverage change because it fixes grounding, reduces naming drift, and creates the backbone needed for policy, exemplars, and evals.

## Execution Status

### Completed in this rewrite slice

- Created schema files for role nodes, mesh cases, artifact contracts, metric cards, and risk cards.
- Added a seed canonical ID map covering stakeholder groups, interactions, mesh cases, capabilities, knowledge areas, artifacts, methods, metrics, risks, and glossary terms.
- Added an assistant operating policy with clarification, assumption, escalation, and boundary rules.
- Rebuilt the mesh into structured case records for executive strategy alignment, product requirement refinement, engineering requirement clarification, data metric design, compliance requirement mapping, sales priority pressure, customer success adoption barriers, and support operational feedback.
- Added artifact contracts for discovery briefs, PRDs, and decision memos, each with good and bad examples.
- Added an operational metric card for adoption rate and a risk card for ambiguous requirements.
- Added context variants for startup, scale-up, enterprise, platform, regulated, internal tooling, and AI product modes.
- Added retrieval, behavior, and output-quality eval seed sets plus linting and migration guidance.

### Verified

- Canonical ID references in the new `fine_tuning` corpus resolve cleanly.
- Artifact example references resolve cleanly.
