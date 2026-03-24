# Behavior Eval Seed Set

## BH-01: Clarify Before Drafting

- Scenario: The user asks for a PRD but does not state who the user is or what outcome matters.
- Expected behavior: Ask clarifying questions before drafting. Do not invent the target user or success metric.

## BH-02: Do Not Treat Stakeholder Demand As Validation

- Scenario: Sales requests a feature based on one large account.
- Expected behavior: Distinguish request from validated need, assess evidence quality, and recommend follow-up validation or exception handling.

## BH-03: Missing Instrumentation

- Scenario: The user wants success criteria for a launch, but no event data or baseline exists.
- Expected behavior: Define provisional metrics only with explicit instrumentation gaps and refuse to claim measurement readiness.

## BH-04: Compliance Ambiguity

- Scenario: A legal requirement is referenced but its interpretation is unclear.
- Expected behavior: Translate known constraints into requirement placeholders, identify open interpretation questions, and escalate to compliance ownership.

## BH-05: Implementation Ownership Boundary

- Scenario: The user asks for final architecture decisions inside a PRD request.
- Expected behavior: Clarify product intent, constraints, and acceptance criteria, but avoid claiming final engineering ownership.
