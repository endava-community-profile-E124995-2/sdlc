# Output Quality Eval Seed Set

## OQ-01: Technical Feasibility Brief Quality

- Required pass signals:
  - names the requested change and the current system context
  - separates constraints from assumptions
  - ends with a clear next technical step
- Fail if:
  - feasibility is asserted without technical evidence
  - the current architecture is not described

## OQ-02: Architecture Decision Record Quality

- Required pass signals:
  - decision statement is explicit
  - more than one option is compared
  - trade-offs and system impacts are visible
- Fail if:
  - only one option is presented
  - the rationale is pure preference

## OQ-03: Engineering Execution Plan Quality

- Required pass signals:
  - workstreams are sequenced
  - dependencies have owners or clear notes
  - validation and handoffs are explicit
- Fail if:
  - the plan is a flat task list with no sequencing logic
  - testing is deferred to a generic end phase

## OQ-04: Cross-Role Handoff Note Quality

- Required pass signals:
  - target role is explicit
  - facts are separated from unresolved questions
  - unblock criteria are concrete
- Fail if:
  - the requested action is vague
  - the note assumes the receiving role already knows the context
