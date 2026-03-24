# Context Variant: AI Product

## Use When

Use for features or products where model behavior, confidence, verification, and human review materially affect the experience.

## Overrides

- Require explicit distinction between model output, product behavior, and human validation.
- Treat evaluation design and failure-mode review as part of requirement quality.
- Ask for confidence handling, fallback behavior, and escalation paths early.
- Avoid claiming deterministic behavior where the underlying system is probabilistic.

## Risks To Emphasize

- `risk.wrong_problem`
- `risk.ambiguous_requirements`
- `risk.missing_instrumentation`
