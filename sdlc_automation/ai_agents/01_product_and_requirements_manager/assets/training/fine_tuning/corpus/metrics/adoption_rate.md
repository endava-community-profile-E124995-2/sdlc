# Metric Card: Adoption Rate

```yaml
id: metric.adoption_rate
metric_name: Adoption rate
definition: The share of the intended target population that reaches meaningful usage of the feature, workflow, or product within a defined period.
formula_or_logic: adopted_target_users / total_target_users_in_scope
owner: Product manager with analytics support
data_source:
  - product event instrumentation
  - account or user segmentation data
baseline_needed: A pre-launch or pre-change baseline, plus a precise definition of the target population in scope.
leading_or_lagging: Usually lagging for outcome claims, but can act as a near-term signal when paired with activation milestones.
anti_patterns:
  - counting mere exposure or access as adoption
  - measuring all users instead of the intended segment
  - claiming adoption success before event coverage is validated
interpretation_notes:
  - read together with activation and retention when adoption can be shallow or one-time
  - low adoption may reflect poor rollout, weak enablement, weak value, or segmentation mismatch rather than one root cause
```

## Related Artifacts

- `artifact.launch_brief`
- `artifact.kpi_spec`
- `artifact.post_launch_review`

## Related Risks

- `risk.adoption_risk`
- `risk.missing_instrumentation`
