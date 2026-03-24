# Artifact Contract Schema

## Purpose

Use this schema for artifact-specific quality bars, templates, and exemplars.

## Required Fields

- `id`: Stable artifact contract ID such as `artifact.prd`.
- `artifact_name`: Display name.
- `purpose`: Why the artifact exists.
- `required_sections`: Mandatory sections that must appear.
- `optional_sections`: Useful but not always required sections.
- `minimum_quality_bar`: The shortest serious version that is still acceptable.
- `common_failure_modes`: Patterns that make the artifact weak or misleading.
- `good_example_ref`: Relative path to a good example.
- `bad_example_ref`: Relative path to a bad example.

## Validation Rules

- Contracts must be strict enough to judge output quality.
- `required_sections` should reflect the role, not downstream engineering implementation detail.
- `minimum_quality_bar` should be short enough for lightweight work and strong enough for cross-functional work.
- Failure modes should be observable in generated text.
- Example refs must resolve to real files.

## Example Record

```yaml
id: artifact.decision_memo
artifact_name: Decision memo
purpose: Records a recommendation, the options considered, and why one path is preferred now.
required_sections:
  - decision
  - context
  - options_considered
  - recommendation
  - trade_offs
  - risks
  - follow_up_actions
optional_sections:
  - dependencies
  - open_questions
minimum_quality_bar: A serious memo states the decision, alternatives, rationale, risks, and next action owners.
common_failure_modes:
  - decision is implied rather than explicit
  - no rejected options are shown
  - rationale is only opinion, not evidence
good_example_ref: corpus/examples/decision_memo_good_platform.md
bad_example_ref: corpus/examples/decision_memo_bad_solution_bias.md
```
