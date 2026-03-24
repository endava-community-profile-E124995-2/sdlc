# Canonical Role Node Schema

## Purpose

Use this schema for ontology nodes that represent capabilities, knowledge areas, behaviors, specializations, stakeholders, interactions, artifacts, methods, metrics, risks, and glossary terms.

## Required Fields

- `id`: Stable canonical identifier such as `cap.architecture_optioning` or `stake.architecture_engineering`.
- `node_type`: One of `capability`, `knowledge_area`, `behavior`, `specialization`, `stakeholder_group`, `interaction`, `artifact`, `method`, `metric`, `risk`, or `glossary_term`.
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
- `priority` reflects retrieval importance, not org prestige.
- `confidence` reflects definition maturity, not business certainty.

## Example Record

```yaml
id: cap.architecture_optioning
node_type: capability
name: Architecture optioning
aliases:
  - design optioning
  - technical trade-off analysis
definition: Compares viable technical approaches and makes the trade-offs, impacts, and recommendation explicit.
when_to_use:
  - more than one design path can satisfy the request
  - service boundaries or interfaces are the main decision point
when_not_to_use:
  - the design is already chosen and the work is now execution sequencing
related_ids:
  - cap.decision_record_writing
  - artifact.architecture_decision_record
  - risk.architecture_misalignment
priority: core
confidence: high
source_file: corpus/ontology/canonical_id_map.md
```
