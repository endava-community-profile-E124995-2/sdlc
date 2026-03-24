# Context Variants

Use this reference after identifying the base task. Apply one variant unless the request clearly spans two environments.

Active agent source: [agent/source_index.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/agent/source_index.md)

## Variant Selection

- `startup`: fast-learning, low-governance environments
- `scale_up`: rising coordination load and cross-team dependencies
- `enterprise`: heavy role structure, contracts, and rollout complexity
- `platform`: shared services, APIs, and non-functional requirements dominate
- `regulated`: privacy, security, auditability, legal, or industry regulation materially changes the work
- `internal_tooling`: employee-facing workflow and efficiency problems
- `ai_product`: probabilistic behavior, verification, and human review matter

## What Variants Change

- artifact depth
- governance strictness
- cadence expectations
- stakeholder emphasis
- risk weighting

## Regulated Override

When the work is regulated:

- raise the threshold for silent assumptions
- require traceability from policy or control to product behavior
- prefer explicit approval questions, exception handling, and change-control notes
- escalate sooner when legal or compliance interpretation is unclear

## Sources

- [overview.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/variants/overview.md)
- [regulated.md](../../../../sdlc_automation/ai_agents/02_architecture_and_engineering_manager/assets/training/fine_tuning/corpus/variants/regulated.md)

