# Canonical Role Node Schema

## Purpose

Use this schema for ontology nodes that represent capabilities, knowledge areas, behaviors, stakeholders, interactions, artifacts, methods, metrics, risks, and glossary terms.

## Required Fields

- `id`: Stable canonical identifier such as `cap.rollout_planning` or `stake.deployment_operations`.
- `node_type`: One of `capability`, `knowledge_area`, `stakeholder_group`, `interaction`, `artifact`, `method`, `metric`, `risk`, or `glossary_term`.
- `name`: Canonical display label.
- `aliases`: Alternate labels, acronyms, and company-specific variants.
- `definition`: Short, precise meaning of the node.
- `when_to_use`: Conditions that make the node relevant.
- `when_not_to_use`: Conditions that make the node misleading or low-value.
- `related_ids`: Canonical IDs that commonly co-occur.
- `priority`: One of `core`, `high`, `medium`, or `contextual`.
- `confidence`: One of `high`, `medium`, or `low`.
- `source_file`: The source corpus file that owns the definition.

## Validation Rules

- IDs must be lowercase and dot-scoped.
- `name` must be unique across the role pack.
- `aliases` should contain only true synonyms or close operational variants.
- `definition` must describe the node, not a workflow that happens to use it.
- `when_to_use` and `when_not_to_use` must be concrete enough to guide retrieval and generation.
- `related_ids` must resolve to existing canonical IDs.
