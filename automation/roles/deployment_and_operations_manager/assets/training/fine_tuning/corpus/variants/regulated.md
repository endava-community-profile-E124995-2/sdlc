# Context Variant: Regulated

## Use When

Use when change control, auditability, evidence, or contractual release constraints materially affect the deployment path.

## Overrides

- raise the threshold for silent assumptions about rollback approval, operating evidence, and handoff ownership
- make change-window conditions and controlled checkpoints explicit
- escalate sooner when gate or exception questions bleed into deployment work

## Risks To Emphasize

- `risk.rollback_readiness_gap`
- `risk.support_ownership_gap`
