# Good Example: Cross-Role Handoff Note

## Target role

Quality, Security, and Governance Manager

## Trigger for handoff

Security review rejected the current token-sharing approach for cross-service impersonation.

## Known facts and constraints

- The current design uses short-lived service tokens for internal calls.
- Two downstream services still require end-user context for audit trails.
- Delivery sequencing is blocked until the approved impersonation boundary is clear.

## Open questions or unresolved decisions

- Is user-context delegation allowed for these service pairs under current control policy?
- What audit evidence is mandatory if delegation is allowed?

## Requested action

Interpret the control boundary and define the acceptable impersonation pattern.

## Unblock criteria

Architecture can resume once the allowed pattern and required audit controls are explicit.
