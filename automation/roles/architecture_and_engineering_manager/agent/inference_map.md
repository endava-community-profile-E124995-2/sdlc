# Inference Map

Use this file first. It decides task type, load order, escalation, and fallback.

## Load Order

1. `agent/operating_rules.md`
2. `agent/output_contracts.md`
3. `agent/source_index.md`
4. selected asset files from `agent/source_index.md`
5. `assets/knowledge/legacy_role_rag/` only if the structured asset pack does not cover the request

## Task Router

- Technical feasibility assessment
  Output shape: Technical Feasibility Brief
  Load from `agent/source_index.md`: feasibility sources, current-state constraints, and the selected variant
- Architecture optioning and decision records
  Output shape: Architecture Decision Record
  Load from `agent/source_index.md`: architecture-decision sources, interface or dependency packs, and the selected variant
- Engineering implementation planning
  Output shape: Engineering Execution Plan
  Load from `agent/source_index.md`: execution-planning sources, sequencing material, risk cards, and the selected variant
- Boundary or ownership transition
  Output shape: Cross-Role Handoff Note
  Load from `agent/source_index.md`: handoff sources and the target-role-specific interaction case

## Variant Selection

- Apply one variant after identifying the base task.
- Use `startup`, `scale_up`, `enterprise`, `platform`, `regulated`, `internal_tooling`, or `ai_product` according to environment.
- Do not apply more than one variant unless the request clearly spans two contexts that materially change behavior.

## Escalation

Escalate or narrow the response when:

- business intent, scope, priority, or acceptance criteria are too weak for technical planning and must return to product ownership
- control interpretation, security posture, compliance mapping, or formal approval gates must move to quality, security, and governance ownership
- rollout, observability, supportability, rollback, SLOs, or runbook ownership must move to deployment and operations ownership
- the user asks for code delivery when the missing technical design or handoff boundary must be resolved first

## Fallback

- Prefer the structured asset packs before legacy knowledge.
- Use `assets/knowledge/legacy_role_rag/` only to widen coverage, not to override agent rules.
- Keep agent behavior governed by `agent/operating_rules.md` and `agent/output_contracts.md`.
