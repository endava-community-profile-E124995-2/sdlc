# Good Example: Architecture Decision Record

## Decision statement

Split webhook delivery into a dedicated delivery service instead of extending the billing monolith.

## Architectural context

Webhook retries, backoff, signature rotation, and provider-specific failure handling are now shared across billing, provisioning, and audit events. The monolith owns business rules well, but its release cadence and failure domain are misaligned with delivery concerns.

## Options considered

1. Extend the monolith with another webhook module.
2. Create a dedicated webhook delivery service with a stable publish contract.
3. Keep the monolith and add a job wrapper around the current implementation.

## Recommendation

Choose option 2.

## Rationale and trade-offs

It creates a clean delivery boundary, isolates retry load, and gives multiple producers one contract. The trade-off is new service ownership, deployment overhead, and contract versioning work.

## Impact on systems and teams

- Billing and provisioning publish to one delivery contract.
- Platform team must provision service runtime and secret rotation support.
- Deployment and operations will need runbooks and alerting for the new service.

## Follow-up actions

- Write interface contracts for event publish and retry callbacks.
- Prepare an execution plan for incremental producer migration.
