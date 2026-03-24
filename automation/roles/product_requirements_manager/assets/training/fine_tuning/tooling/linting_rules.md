# Linting Rules

## Canonical Reference Rules

- Every structured record must use canonical IDs from `corpus/ontology/canonical_id_map.md`.
- No mesh case may introduce a raw skill, stakeholder, metric, or risk label that lacks a canonical ID.
- IDs must be lowercase, stable, and dot-scoped.

## Schema Completeness Rules

- Every role node must satisfy `schema/role_node_schema.md`.
- Every mesh case must satisfy `schema/mesh_case_schema.md`.
- Every artifact contract must satisfy `schema/artifact_contract_schema.md`.
- Every metric card must satisfy `schema/metric_card_schema.md`.
- Every risk card must satisfy `schema/risk_card_schema.md`.

## Duplication Rules

- Canonical names must be unique.
- Near-duplicates must be merged under one canonical name with aliases.
- Summary-only content should not duplicate the same operational guidance already present in canonical records.

## Link Integrity Rules

- Every example reference in an artifact contract must resolve to a real file.
- Every `related_ids` entry must resolve to a real canonical ID.
- Every retrieval eval expected target must exist.

## Content Quality Rules

- `when_to_use` and `when_not_to_use` must be specific enough to guide retrieval.
- `example_prompt` in a mesh case must sound like a realistic user request.
- Metrics must include a baseline note and at least one anti-pattern.
- Risks must include trigger signals and mitigation actions.
- Variant packs must only override depth, governance, cadence, stakeholder emphasis, or risk weighting, not redefine the base ontology.

## Assistant Behavior Rules

- The corpus must preserve explicit assumption labeling.
- The corpus must preserve refusal and escalation boundaries for legal, compliance, security, finance, and implementation ownership.
- No artifact example should normalize vague scope, hidden assumptions, or untestable acceptance criteria.
