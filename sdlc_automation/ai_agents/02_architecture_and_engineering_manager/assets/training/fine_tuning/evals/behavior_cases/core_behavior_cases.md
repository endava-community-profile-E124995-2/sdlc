# Behavior Eval Seed Set

## BH-01: PRD To Technical Plan

- Scenario: The user says, "Turn this approved PRD into a technical plan."
- Expected behavior: Route to an Engineering Execution Plan and preserve sequencing, dependencies, validation, and handoffs.

## BH-02: Architecture Trade-Off

- Scenario: The user says, "Choose between extending the monolith and splitting a service."
- Expected behavior: Route to an Architecture Decision Record with real options, trade-offs, and follow-up actions.

## BH-03: Product Handoff For Ambiguity

- Scenario: The user says, "Requirements are still ambiguous."
- Expected behavior: Refuse to invent missing business rules and return a Cross-Role Handoff Note to product ownership.

## BH-04: Governance Handoff

- Scenario: The user says, "Security review changed the auth design."
- Expected behavior: Route to a Cross-Role Handoff Note for quality, security, and governance with the impacted design boundary and open control question.

## BH-05: Operations Handoff

- Scenario: The user says, "We need rollout, observability, rollback, and support readiness."
- Expected behavior: Route to a Cross-Role Handoff Note for deployment and operations and make the operability gaps explicit.
