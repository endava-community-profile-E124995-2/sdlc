# Inference Map

Use this file first. It decides task type, load order, escalation, and fallback.

## Load Order

1. `agent/operating_rules.md`
2. `agent/output_contracts.md`
3. `agent/source_index.md`
4. selected asset files from `agent/source_index.md`
5. `assets/knowledge/legacy_role_rag/` only if the structured asset pack does not cover the request

## Task Router

- Release planning and rollout design
  Output shape: Rollout Plan
  Load from `agent/source_index.md`: rollout-planning sources, readiness cards, and the selected variant
- Operational readiness and runbook review
  Output shape: Operability Review
  Load from `agent/source_index.md`: operability-review sources, rollback and observability cards, and the selected variant
- Support handoff or ownership transition
  Output shape: Operations Handoff Note
  Load from `agent/source_index.md`: support-handoff sources, owner-mapping material, and the selected variant
- Post-release signal review
  Output shape: Operational Follow-up Note
  Load from `agent/source_index.md`: operational-follow-up sources, incident-signal cards, and the selected variant

## Variant Selection

- Apply one variant after identifying the base task.
- Use `startup`, `scale_up`, `enterprise`, `platform`, `regulated`, `internal_tooling`, or `ai_product` according to environment.
- Do not apply more than one variant unless the request clearly spans two contexts that materially change behavior.

## Escalation

Escalate or narrow the response when:

- gate recommendation, evidence sufficiency, or exception framing belong to quality, security, and governance ownership
- launch audience, business rollout constraints, or enablement posture belong to product ownership
- rollback safety, runtime topology, or service-boundary design questions belong to architecture ownership
- the user asks for delivery certainty that the known operational evidence does not support

## Handoff Rules

- When release approval, control interpretation, evidence sufficiency, or exception framing are the primary blockers, hand off to quality, security, and governance instead of treating the release as approved.
- When rollout scope, audience segmentation, enablement timing, or business launch constraints are the primary blocker, hand off to product and requirements.
- When rollout work depends on unresolved runtime design, service boundaries, or interface guarantees, hand off to architecture and engineering.

## Fallback

- Prefer the structured asset packs before legacy knowledge.
- Use `assets/knowledge/legacy_role_rag/` only to widen coverage, not to override agent rules.
- Keep agent behavior governed by `agent/operating_rules.md` and `agent/output_contracts.md`.
