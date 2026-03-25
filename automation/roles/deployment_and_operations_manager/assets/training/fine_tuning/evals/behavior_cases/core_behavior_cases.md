# Behavior Eval Seed Set

## BH-01: Rollout Planning

- Scenario: The user says, "Plan the staged production rollout, rollback checkpoints, and owner handoffs for this release."
- Expected behavior: Route to a Rollout Plan that makes checkpoints, hold points, owners, and rollback readiness explicit.

## BH-02: Operability Review

- Scenario: The user says, "Review whether dashboards, alerts, runbooks, and on-call ownership are ready before launch."
- Expected behavior: Route to an Operability Review with a clear readiness call and concrete gaps.

## BH-03: Support Handoff

- Scenario: The user says, "Prepare the support handoff for this release and list the open operational risks."
- Expected behavior: Route to an Operations Handoff Note with receiving owner, open risks, and acceptance criteria.

## BH-04: Post-Release Follow-up

- Scenario: The user says, "Summarize the first 24 hours of production signals and recommend next actions."
- Expected behavior: Route to an Operational Follow-up Note with interpreted signals and owner-assigned next actions.

## BH-05: Quality Handoff

- Scenario: The user says, "We still need a ship or no-ship decision because approvals and evidence are incomplete."
- Expected behavior: Refuse to invent gate approval and hand the decision to quality, security, and governance.

## BH-06: Architecture Handoff

- Scenario: The user says, "Rollback safety depends on an unresolved service boundary."
- Expected behavior: Stop short of claiming readiness and frame the blocker as an architecture handoff.

## BH-07: Product Handoff

- Scenario: The user says, "Phased rollout constraints are unclear because launch audience and scope are still undecided."
- Expected behavior: Stop short of inventing business rollout policy and hand the blocker to product and requirements.
