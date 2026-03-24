# Artifact Contract: Product Requirements Document

```yaml
id: artifact.prd
artifact_name: Product requirements document
purpose: Translate a validated problem into a testable, traceable requirement set that aligns cross-functional delivery.
required_sections:
  - problem
  - goals
  - users_or_actors
  - scope
  - out_of_scope
  - business_rules
  - functional_requirements
  - non_functional_requirements
  - acceptance_criteria
  - dependencies
  - risks
  - metrics
  - open_questions
optional_sections:
  - rollout_notes
  - change_log
  - glossary
minimum_quality_bar: A serious PRD states the problem, users, scope boundaries, rules, requirements, acceptance criteria, dependencies, risks, metrics, and open questions.
common_failure_modes:
  - implementation detail replaces product intent
  - scope and exclusions are blurred
  - acceptance criteria are not testable
  - metrics are named without instrumentation feasibility
good_example_ref: corpus/examples/prd_good_platform_permissions.md
bad_example_ref: corpus/examples/prd_bad_vague_scope.md
```

## Template

1. Problem and goals
2. Users and actors
3. Scope and exclusions
4. Business rules
5. Functional requirements
6. Non-functional requirements
7. Acceptance criteria
8. Dependencies and risks
9. Metrics and instrumentation gaps
10. Open questions
