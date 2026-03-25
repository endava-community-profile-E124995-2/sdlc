# Gate And Exception Patterns

## Common Review Patterns

- Gate cannot pass when required evidence is absent or stale.
- Exceptions should state the specific control gap, time bound, and owner.
- Release readiness depends on both evidence sufficiency and downstream operational acceptance.

## Anti-Patterns

- using a generic "ship with caution" statement instead of a concrete gate recommendation
- implying an approval exists because a mitigation is planned
- conflating unresolved architecture debate with completed security review
