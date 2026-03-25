# Migration Checklist

## Phase 1: Inventory

- Confirm the legacy `role_rag` pack is preserved as baseline reference.
- Identify all stakeholders, interactions, capabilities, knowledge areas, artifacts, methods, metrics, and risks that need canonical IDs.
- Mark duplicates and near-duplicates before creating new IDs.

## Phase 2: Canonicalization

- Add or update canonical IDs in `corpus/ontology/canonical_id_map.md`.
- Replace raw labels with canonical IDs in structured records.
- Add aliases only when they improve recall without creating ambiguity.

## Phase 3: Structured Rebuild

- Convert broad deployment guidance into artifact contracts, interaction cases, examples, metrics, and risks.
- Add handoff cases back to product, architecture, and quality for the most common ownership boundaries.
- Keep the fallback pack separate from the active role contract.

## Phase 4: Contracts And Examples

- Create artifact contracts for the four core output shapes.
- Attach one good example and one bad example to each artifact.
- Check that every example demonstrates owners, readiness evidence, handoff logic, and operational traceability.

## Phase 5: Variants

- Add context variants only after the base deployment behavior is stable.
- Keep variant overrides small and explicit.
- Do not let variants fork the ontology vocabulary.

## Phase 6: Evals And Hardening

- Add retrieval queries for each new high-priority case.
- Add behavior cases for ambiguity, release gates, runtime blockers, and ownership boundaries.
- Run lint checks for broken references and unknown IDs before merging.
