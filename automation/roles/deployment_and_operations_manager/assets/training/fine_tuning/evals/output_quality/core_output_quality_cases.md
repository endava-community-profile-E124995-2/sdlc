# Output Quality Eval Seed Set

## OQ-01: Rollout Plan Quality

- Required pass signals:
  - names the release scope, environment, and rollout sequence
  - includes hold points, owners, and rollback expectations
  - separates open operational risks from confirmed readiness
- Fail if:
  - the plan is just a prose status update
  - rollback or owner logic is implied rather than explicit

## OQ-02: Operability Review Quality

- Required pass signals:
  - the reviewed runtime scope and readiness bar are explicit
  - monitoring, runbook, and ownership status are distinguished
  - the recommendation is direct and role-correct
- Fail if:
  - the review is only a list of tools
  - the note drifts into gate approval or architecture invention

## OQ-03: Operations Handoff Note Quality

- Required pass signals:
  - the receiving owner or team is explicit
  - required runtime materials and open risks are concrete
  - the handoff has acceptance or unblock criteria
- Fail if:
  - no owner is named
  - the note assumes support will infer what remains open

## OQ-04: Operational Follow-up Note Quality

- Required pass signals:
  - the review window and signals are explicit
  - anomalies are interpreted, not just listed
  - follow-up actions have owners or timing
- Fail if:
  - the note is only a metric dump
  - the recommendation claims stability without enough signal context
