# Context Variant: Platform

## Use When

Use when shared services, infrastructure dependencies, or downstream tenant impact dominate the rollout shape.

## Overrides

- treat blast-radius control and rollback readiness as first-class parts of the rollout plan
- make observability expectations explicit for upstream and downstream dependencies
- call out where support ownership crosses team boundaries

## Risks To Emphasize

- `risk.rollback_readiness_gap`
- `risk.observability_blind_spot`
