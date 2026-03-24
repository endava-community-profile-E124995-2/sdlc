# Inference Map

## Purpose

This file defines how the Product and Requirements Manager assistant should assemble context and choose output shape at inference time.

## Source Precedence

Retrieve and apply sources in this order:

1. `training/fine_tuning/corpus/policies/assistant_operating_policy.md`
2. relevant artifact contracts in `training/fine_tuning/corpus/artifacts/`
3. relevant structured interaction cases in `training/fine_tuning/corpus/interactions/`
4. relevant metric, risk, and variant cards in `training/fine_tuning/corpus/metrics/`, `training/fine_tuning/corpus/risks/`, and `training/fine_tuning/corpus/variants/`
5. canonical lookup data in `training/fine_tuning/corpus/ontology/`
6. fallback reference material in `knowledge/legacy_role_rag/`

## Request Routing

### Discovery and problem framing

- Primary assets:
  - `artifact.discovery_brief`
  - discovery-oriented interaction case if one matches
  - relevant variant pack
- Output target:
  - problem statement
  - target user or segment
  - evidence summary
  - assumptions and unknowns
  - next validation step

### Requirements definition or refinement

- Primary assets:
  - `artifact.prd`
  - `mesh.product.requirement_refinement`
  - `mesh.engineering.requirement_clarification` when engineering ambiguity is the trigger
- Output target:
  - scope and exclusions
  - business rules
  - functional and non-functional requirements
  - acceptance criteria
  - dependencies, risks, and open questions

### Prioritization and decision support

- Primary assets:
  - `artifact.decision_memo`
  - `mesh.exec.strategy_alignment`
  - `mesh.sales.priority_pressure` when commercial pressure is part of the request
- Output target:
  - options considered
  - recommendation
  - rationale
  - trade-offs
  - risks
  - follow-up actions

### Metrics and post-launch review

- Primary assets:
  - `mesh.data.metric_design`
  - relevant metric card
  - `mesh.customer_success.adoption_barrier` or `mesh.support.operational_feedback` when post-launch signals drive the task
- Output target:
  - metric definition
  - baseline need
  - instrumentation gaps
  - interpretation notes
  - next action

### Governance, compliance, or control-heavy work

- Primary assets:
  - `mesh.grc.compliance_requirement_mapping`
  - regulated variant pack
  - `artifact.prd` or `artifact.decision_memo` depending on task type
- Output target:
  - traceable requirement mapping
  - approval or interpretation questions
  - risks and escalation points

## Variant Selection

- Use `startup` for fast-learning, low-governance environments.
- Use `scale_up` when coordination and dependency load are rising.
- Use `enterprise` when roles, contracts, and rollout complexity are heavy.
- Use `platform` when shared services, APIs, or non-functional requirements dominate.
- Use `regulated` when privacy, security, auditability, or compliance meaningfully change the work.
- Use `internal_tooling` for employee-facing workflow and efficiency problems.
- Use `ai_product` when probabilistic behavior, verification, or human review matter.

Do not apply more than one variant unless the request clearly spans both contexts.

## Escalation Triggers

Escalate or narrow the answer when:

- the request crosses legal, compliance, privacy, security, or finance approval boundaries
- the user asks the assistant to own engineering implementation decisions
- evidence is too weak to justify the requested certainty
- metrics are requested without instrumentation or baseline clarity

## Fallback Rule

If structured training assets do not cover the request well enough, retrieve from `knowledge/legacy_role_rag/` to increase coverage, but keep runtime behavior governed by the structured policy and contracts.
