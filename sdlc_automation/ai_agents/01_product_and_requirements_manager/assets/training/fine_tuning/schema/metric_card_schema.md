# Metric Card Schema

## Purpose

Use this schema for metrics that should survive retrieval, drafting, and review without turning into vanity measures.

## Required Fields

- `id`
- `metric_name`
- `definition`
- `formula_or_logic`
- `owner`
- `data_source`
- `baseline_needed`
- `leading_or_lagging`
- `anti_patterns`
- `interpretation_notes`

## Validation Rules

- Metrics must be defined precisely enough that two analysts would instrument them the same way.
- `owner` should indicate the team or function accountable for interpretation.
- `baseline_needed` should say what comparison is necessary before claiming impact.
- `anti_patterns` must name misuse patterns, not generic warnings.
- `interpretation_notes` should explain common confounders.
