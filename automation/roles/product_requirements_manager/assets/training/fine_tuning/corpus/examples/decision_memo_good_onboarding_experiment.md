# Good Example: Decision Memo For Onboarding Experiment

## Context Tags

- `growth`
- `activation`
- `decision`

## Artifact

### Decision

Run a guided onboarding experiment for new self-serve workspaces before committing to a broader setup-flow redesign.

### Context

Activation is below target for self-serve accounts, and recent session reviews show users abandoning setup before completing their first team invite.

### Options considered

1. Guided onboarding experiment focused on the invite step.
2. Full redesign of the setup flow.
3. No product change, only update help content.

### Recommendation

Choose option 1 because it targets the highest-friction step, can ship in a smaller slice, and will generate evidence on whether the invite step is the real activation bottleneck.

### Rationale

- Session review and funnel data both indicate invite-step drop-off.
- A full redesign carries higher cost before the problem is validated deeply enough.
- Help-content-only changes are unlikely to address in-product hesitation.

### Trade-offs

- Smaller experiment means we may not solve all onboarding friction immediately.
- The experiment requires event instrumentation cleanup before launch.

### Risks

- Missing instrumentation could weaken interpretation.
- Activation could be driven by account intent rather than invite-step friction alone.

### Follow-up actions

- Finalize KPI spec for activation and invite completion.
- Add missing invite-step events.
- Review results two weeks after rollout.

## Why This Is Good

- The decision is explicit.
- Alternatives are visible.
- Rationale is evidence-led.
- Risks and follow-up actions are concrete.
