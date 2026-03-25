# Linting Rules

## Goal

Keep the structured deployment corpus internally consistent and safe for retrieval and fine-tuning use.

## Rules

- Every backtick-wrapped canonical ID must resolve in `corpus/ontology/canonical_id_map.md`.
- Every artifact contract must resolve both `good_example_ref` and `bad_example_ref`.
- Interaction cases must stay role-correct and must not take product, architecture, or quality-gate ownership unless they are explicitly framing a handoff.
- Metric and risk cards should stay operational and measurable, not aspirational.
- Variants should override emphasis, not redefine the role.
