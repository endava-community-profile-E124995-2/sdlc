# Retrieval Eval Seed Set

## Purpose

Use these prompts to verify that retrieval returns the right mesh cases, artifact contracts, and operational cards.

## Queries

### RQ-01: Sales Pressure Versus Product Need

- Prompt: A strategic account wants a custom workflow next quarter and Sales says we have to prioritize it now. Frame the decision and push back if the evidence is weak.
- Expected retrieval:
  - `mesh.sales.priority_pressure`
  - `artifact.decision_memo`
  - `risk.wrong_problem`

### RQ-02: Compliance Mapping

- Prompt: Turn these privacy and auditability requirements into product requirements we can review with compliance and engineering.
- Expected retrieval:
  - `mesh.grc.compliance_requirement_mapping`
  - `artifact.prd`
  - `risk.compliance_exposure`

### RQ-03: Engineering Clarification

- Prompt: Engineering says the story is too vague and the acceptance criteria miss edge cases. Tighten it without writing the technical design.
- Expected retrieval:
  - `mesh.engineering.requirement_clarification`
  - `artifact.prd`
  - `risk.ambiguous_requirements`

### RQ-04: Adoption Diagnosis

- Prompt: Customer Success says users are not adopting the new workflow after launch. Diagnose the barrier and recommend next actions.
- Expected retrieval:
  - `mesh.customer_success.adoption_barrier`
  - `metric.adoption_rate`
  - `artifact.post_launch_review`

### RQ-05: Executive Trade-Off

- Prompt: Write an executive-ready recommendation on whether we should prioritize self-serve onboarding or enterprise workflow controls next quarter.
- Expected retrieval:
  - `mesh.exec.strategy_alignment`
  - `artifact.strategy_brief`
  - `artifact.decision_memo`

### RQ-06: Metric Definition

- Prompt: Define the success metrics for this launch and tell us what instrumentation is missing before we commit to them.
- Expected retrieval:
  - `mesh.data.metric_design`
  - `metric.adoption_rate`
  - `risk.missing_instrumentation`
