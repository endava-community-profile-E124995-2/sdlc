# Artifact Contract Schema

## Purpose

Use this schema for artifact-specific quality bars, templates, and exemplars.

## Required Fields

- `id`: Stable artifact contract ID such as `artifact.quality_review_note`.
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
- `required_sections` should reflect the role, not downstream delivery work the role does not own.
- `minimum_quality_bar` should be short enough for lightweight work and strong enough for cross-functional work.
- Failure modes should be observable in generated text.
- Example refs must resolve to real files.
