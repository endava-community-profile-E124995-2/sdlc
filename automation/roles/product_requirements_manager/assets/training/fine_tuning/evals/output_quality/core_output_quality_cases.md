# Output Quality Eval Seed Set

## OQ-01: Discovery Brief Quality

- Required pass signals:
  - names a real target user or segment
  - separates evidence from assumptions
  - ends with a next validation step
- Fail if:
  - starts with a feature instead of a problem
  - has no evidence source

## OQ-02: PRD Quality

- Required pass signals:
  - has clear scope and out-of-scope
  - includes business rules and acceptance criteria
  - names dependencies, risks, and metrics
- Fail if:
  - implementation detail replaces product intent
  - success metrics are vague or uninstrumented without caveat

## OQ-03: Decision Memo Quality

- Required pass signals:
  - decision is explicit
  - alternatives are shown
  - rationale includes evidence and trade-offs
  - follow-up actions are concrete
- Fail if:
  - recommendation is pure opinion
  - risks are generic filler

## OQ-04: KPI Spec Quality

- Required pass signals:
  - metric definition is precise
  - formula or logic is present
  - baseline need is named
  - anti-patterns or caveats are stated
- Fail if:
  - adoption is treated as mere exposure
  - no instrumentation dependency is acknowledged
