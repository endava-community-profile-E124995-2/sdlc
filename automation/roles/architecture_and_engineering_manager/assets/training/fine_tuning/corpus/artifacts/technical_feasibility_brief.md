# Artifact Contract: Technical Feasibility Brief

```yaml
id: artifact.technical_feasibility_brief
artifact_name: Technical feasibility brief
purpose: Assess whether an approved change fits the current architecture, constraints, and delivery posture before deeper design or implementation planning.
required_sections:
  - requested_change
  - current_system_context
  - technical_constraints_and_assumptions
  - feasibility_assessment
  - key_risks_and_unknowns
  - recommended_next_step
optional_sections:
  - candidate_approaches
  - dependency_notes
  - handoff_needed
minimum_quality_bar: A serious brief names the requested change, current technical context, the main constraints, the feasibility call, the main risks, and the next action.
common_failure_modes:
  - current-state architecture is not described
  - feasibility is asserted without evidence or constraints
  - risks are generic and not tied to the affected systems
  - the next step is missing or belongs to another role without saying so
good_example_ref: corpus/examples/technical_feasibility_brief_good_api_rate_limit.md
bad_example_ref: corpus/examples/technical_feasibility_brief_bad_wishful_thinking.md
```

## Template

1. Requested change
2. Current system context
3. Technical constraints and assumptions
4. Feasibility assessment
5. Key risks and unknowns
6. Recommended next step
