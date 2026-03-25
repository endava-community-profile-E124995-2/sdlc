# Output Quality Eval Seed Set

## OQ-01: Quality Review Note Quality

- Required pass signals:
  - names the reviewed scope and expected quality bar
  - shows what evidence was reviewed
  - ends with a clear adequacy recommendation and unblockers
- Fail if:
  - the note is only a checklist with no judgment
  - evidence is implied rather than named

## OQ-02: Security Review Note Quality

- Required pass signals:
  - the boundary reviewed is explicit
  - risks are tied to controls or residual-risk posture
  - missing evidence and follow-up are explicit
- Fail if:
  - the note gives generic warnings without a concrete boundary
  - the note reads like approval while open questions remain

## OQ-03: Governance Mapping Note Quality

- Required pass signals:
  - a specific control or policy is mapped to affected behavior
  - evidence and missing evidence are distinguished
  - approval or exception questions are explicit
- Fail if:
  - the note only lists policy names
  - the next step ignores the owning role

## OQ-04: Release Gate Memo Quality

- Required pass signals:
  - the release boundary is explicit
  - the gate recommendation is direct
  - blockers, evidence status, and unblock criteria are separate and concrete
- Fail if:
  - the memo implies "ship with caution" instead of deciding
  - handoffs have no clear unblock condition
