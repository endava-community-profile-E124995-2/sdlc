# Context Variant: AI Product

## Use When

Use for systems where model behavior, confidence, verification, and human review materially affect the technical design.

## Overrides

- Require explicit distinction between model output, application behavior, and human validation.
- Treat evaluation design and failure-mode review as part of architecture and execution quality.
- Ask for confidence handling, fallback behavior, and escalation paths early.
- Avoid claiming deterministic behavior where the underlying system is probabilistic.

## Risks To Emphasize

- `risk.architecture_misalignment`
- `risk.integration_overrun`
- `risk.operability_gap`
