# Migration Checklist

## Phase 1: Inventory

- Confirm the legacy `role_rag` pack is preserved as baseline reference.
- Identify all stakeholders, interactions, capabilities, knowledge areas, artifacts, methods, metrics, and risks that need canonical IDs.
- Mark duplicates and near-duplicates before creating new IDs.

## Phase 2: Canonicalization

- Add or update canonical IDs in `corpus/ontology/canonical_id_map.md`.
- Replace legacy raw labels with canonical IDs in structured records.
- Add aliases only when they improve recall without creating ambiguity.

## Phase 3: Structured Rebuild

- Convert long inventory sections into atomic files or record blocks.
- Add schema-compliant mesh cases for high-frequency stakeholder interactions first.
- Add operational cards for high-signal metrics and risks.

## Phase 4: Contracts And Examples

- Create artifact contracts for the most common assistant outputs.
- Attach one good example and one bad example to each major artifact.
- Check that every example demonstrates the operating policy rather than contradicting it.

## Phase 5: Variants

- Add context variants only after the base artifact and interaction behavior is stable.
- Keep variant overrides small and explicit.
- Do not let variants fork the ontology vocabulary.

## Phase 6: Evals And Hardening

- Add retrieval queries for each new high-priority mesh case.
- Add behavior cases for ambiguity, pressure, evidence quality, governance, and role boundaries.
- Run lint checks for broken references, unknown IDs, and duplicate labels before merging.
