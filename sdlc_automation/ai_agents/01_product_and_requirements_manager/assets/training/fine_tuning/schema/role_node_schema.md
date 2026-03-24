# Canonical Role Node Schema

## Purpose

Use this schema for ontology nodes that represent capabilities, knowledge areas, behaviors, specializations, stakeholders, interactions, artifacts, methods, metrics, risks, and glossary terms.

## Required Fields

- `id`: Stable canonical identifier such as `cap.problem_framing` or `stake.exec_leadership`.
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
id: cap.problem_framing
node_type: capability
name: Problem framing
aliases:
  - problem definition
  - issue framing
definition: Turns rough requests or symptoms into a clear problem statement with users, impact, and uncertainty.
when_to_use:
  - stakeholder asks for a solution before the problem is explicit
  - evidence is scattered and needs synthesis into one statement
when_not_to_use:
  - the problem is already validated and the work is now implementation planning
related_ids:
  - cap.customer_research
  - artifact.discovery_brief
  - risk.wrong_problem
priority: core
confidence: high
source_file: corpus/ontology/canonical_id_map.md
```
