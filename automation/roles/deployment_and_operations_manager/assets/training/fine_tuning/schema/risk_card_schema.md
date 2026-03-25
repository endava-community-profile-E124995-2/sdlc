# Risk Card Schema

## Purpose

Use this schema for risks that need operational handling instead of list-style mention.

## Required Fields

- `id`
- `risk_name`
- `definition`
- `trigger_signals`
- `impact_area`
- `likelihood_notes`
- `mitigation_actions`
- `escalation_path`
- `related_metric_ids`

## Validation Rules

- Risks must be expressed as failure modes, not vague concerns.
- `trigger_signals` should be observable in planning, release, or runtime behavior.
- `impact_area` should state what actually gets harmed.
- `mitigation_actions` must be concrete actions the role can initiate or request.
- `related_metric_ids` must resolve to canonical metrics.
