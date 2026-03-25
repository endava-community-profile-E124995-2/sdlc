# Context Variant: AI Product

## Use When

Use when probabilistic behavior, model drift, or human-review workflows materially change release and operational readiness.

## Overrides

- raise the bar for signal interpretation and rollback triggers because output quality may degrade before hard failures appear
- make monitoring windows and responder expectations explicit
- highlight where operational follow-up needs human-review or safety oversight input

## Risks To Emphasize

- `risk.observability_blind_spot`
- `risk.rollback_readiness_gap`
