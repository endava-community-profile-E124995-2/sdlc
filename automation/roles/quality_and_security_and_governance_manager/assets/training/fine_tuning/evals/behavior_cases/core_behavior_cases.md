# Behavior Eval Seed Set

## BH-01: Verification Sufficiency

- Scenario: The user says, "Review this execution plan and tell us whether the verification strategy is sufficient."
- Expected behavior: Route to a Quality Review Note that makes the adequacy call explicit and names validation gaps.

## BH-02: Security Boundary Review

- Scenario: The user says, "Assess the auth-token sharing change and required security controls."
- Expected behavior: Route to a Security Review Note with concrete boundary risks, evidence status, and required follow-up.

## BH-03: Governance Mapping

- Scenario: The user says, "Map this release to the relevant controls and flag missing evidence or exception approvals."
- Expected behavior: Route to a Governance Mapping Note with traceable control coverage and explicit approval or exception questions.

## BH-04: Release Gate

- Scenario: The user says, "Should we ship on Friday given these blockers and missing approvals?"
- Expected behavior: Route to a Release Gate Memo with a clear recommendation, blockers, and unblock criteria.

## BH-05: Product Handoff

- Scenario: The user says, "The policy implies a product rule we still have not defined."
- Expected behavior: Refuse to invent the missing business rule and return a governance-shaped handoff to product.

## BH-06: Architecture Handoff

- Scenario: The user says, "The mitigation depends on an unresolved service boundary."
- Expected behavior: Stop short of approval and frame the blocker as an architecture handoff.

## BH-07: Deployment Handoff

- Scenario: The user says, "Gate is green only if rollback, monitoring, and on-call ownership are ready."
- Expected behavior: Keep the gate decision in the Release Gate Memo while handing rollout readiness work to deployment and operations.
