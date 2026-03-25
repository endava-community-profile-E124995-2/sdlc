# Inference Map

Use this file first. It decides task type, load order, escalation, and fallback.

## Load Order

1. `agent/operating_rules.md`
2. `agent/output_contracts.md`
3. `agent/source_index.md`
4. selected asset files from `agent/source_index.md`
5. `assets/knowledge/legacy_role_rag/` only if the structured asset pack does not cover the request

## Task Router

- Discovery and problem framing
  Output shape: discovery brief
  Load from `agent/source_index.md`: discovery sources and the selected variant
- Requirements definition or refinement
  Output shape: PRD or tightened requirement set
  Load from `agent/source_index.md`: requirements sources and engineering-clarification cases when ambiguity is implementation-adjacent
- Prioritization and decision support
  Output shape: decision memo
  Load from `agent/source_index.md`: prioritization sources, especially sales-pressure or exec-alignment cases when present
- Launch or rollout readiness
  Output shape: rollout summary
  Load from `agent/output_contracts.md` plus the relevant variant and monitoring-oriented asset sources
- Metrics and post-launch review
  Output shape: KPI or outcome review
  Load from `agent/source_index.md`: metric-design sources and post-launch signal cases
- Governance, compliance, or control-heavy work
  Output shape: traceable requirement mapping or governance-shaped decision memo
  Load from `agent/source_index.md`: compliance mapping sources and the regulated variant
  Boundary: keep policy-driven requirement mapping here, but hand off to quality, security, and governance when approval, control interpretation, evidence sufficiency, exception framing, or release-gate recommendations are the primary outcome

## Variant Selection

- Apply one variant after identifying the base task.
- Use `startup`, `scale_up`, `enterprise`, `platform`, `regulated`, `internal_tooling`, or `ai_product` according to environment.
- Do not apply more than one variant unless the request clearly spans two contexts that materially change behavior.

## Escalation

Escalate or narrow the response when:

- legal, compliance, privacy, security, or finance interpretation changes the recommendation
- the request tries to hand this role final architecture or implementation ownership
- evidence is too weak for the requested certainty
- success criteria depend on instrumentation or baselines that do not exist

## Fallback

- Prefer the structured asset packs before legacy knowledge.
- Use `assets/knowledge/legacy_role_rag/` only to widen coverage, not to override agent rules.
- Keep agent behavior governed by `agent/operating_rules.md` and `agent/output_contracts.md`.
