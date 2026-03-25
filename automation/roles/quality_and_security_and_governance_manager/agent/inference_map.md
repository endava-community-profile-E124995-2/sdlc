# Inference Map

Use this file first. It decides task type, load order, escalation, and fallback.

## Load Order

1. `agent/operating_rules.md`
2. `agent/output_contracts.md`
3. `agent/source_index.md`
4. selected asset files from `agent/source_index.md`
5. `assets/knowledge/legacy_role_rag/` only if the structured asset pack does not cover the request

## Task Router

- Quality review and test strategy
  Output shape: Quality Review Note
  Load from `agent/source_index.md`: quality review sources and the selected variant
- Security boundary or risk review
  Output shape: Security Review Note
  Load from `agent/source_index.md`: security review sources and the selected variant
- Governance or control mapping
  Output shape: Governance Mapping Note
  Load from `agent/source_index.md`: governance mapping sources and the regulated variant when applicable
- Release gate assessment
  Output shape: Release Gate Memo
  Load from `agent/source_index.md`: release gate sources, deployment-readiness handoff patterns, and evidence-related cards

## Variant Selection

- Apply one variant after identifying the base task.
- Use `startup`, `scale_up`, `enterprise`, `platform`, `regulated`, `internal_tooling`, or `ai_product` according to environment.
- Do not apply more than one variant unless the request clearly spans two contexts that materially change review behavior.

## Escalation

Escalate or narrow the response when:

- the requested review depends on missing product intent or policy decisions
- evidence or exception handling changes the recommendation materially
- unresolved architecture or deployment ownership blocks a safe answer
- the user asks for approval certainty that the known evidence does not support

## Fallback

- Prefer the structured asset packs before legacy knowledge.
- Use `assets/knowledge/legacy_role_rag/` only to widen coverage, not to override agent rules.
- Keep agent behavior governed by `agent/operating_rules.md` and `agent/output_contracts.md`.
