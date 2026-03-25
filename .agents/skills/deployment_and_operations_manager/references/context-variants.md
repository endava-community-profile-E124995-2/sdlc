# Context Variants

Use this reference after identifying the base task. Apply one variant unless the request clearly spans two environments.

Active agent source: [agent/source_index.md](../../../../automation/roles/deployment_and_operations_manager/agent/source_index.md)

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
- coordination strictness
- checkpoint expectations
- stakeholder emphasis
- risk weighting

## Regulated Override

When the work is regulated:

- raise the threshold for silent assumptions
- require explicit checkpoint ownership and rollback clarity
- prefer explicit gate handoffs when approvals or evidence matter
- escalate sooner when deployment work is being asked to absorb governance decisions

## Sources

- [startup.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/variants/startup.md)
- [scale_up.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/variants/scale_up.md)
- [enterprise.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/variants/enterprise.md)
- [platform.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/variants/platform.md)
- [regulated.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/variants/regulated.md)
- [internal_tooling.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/variants/internal_tooling.md)
- [ai_product.md](../../../../automation/roles/deployment_and_operations_manager/assets/training/fine_tuning/corpus/variants/ai_product.md)

