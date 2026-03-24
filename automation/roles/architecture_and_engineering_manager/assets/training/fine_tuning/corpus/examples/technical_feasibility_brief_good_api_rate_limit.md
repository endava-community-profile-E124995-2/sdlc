# Good Example: Technical Feasibility Brief

## Requested change

Add tenant-scoped rate limiting across the public API and async worker entrypoints.

## Current system context

The API gateway can apply tenant identity at request time, but the worker fleet only receives job-level metadata after enqueue. Shared retry queues also make per-tenant enforcement inconsistent once work leaves the gateway.

## Technical constraints and assumptions

- Assumption: tenant identity can be propagated into job headers without breaking existing consumers.
- Redis is already available for shared counters, but current key patterns are endpoint-scoped, not tenant-scoped.
- Background jobs triggered by internal maintenance tasks must bypass customer limits.

## Feasibility assessment

Feasible in the current architecture, but not as a gateway-only change. The design needs one shared rate-limit policy module and a worker-side enforcement hook so sync and async entrypoints behave consistently.

## Key risks and unknowns

- Worker retry semantics may double-count usage if counters are incremented before idempotency checks.
- Some internal job producers may not carry tenant identity today.

## Recommended next step

Draft an ADR for a shared rate-limit policy service and confirm worker header propagation before implementation planning.
