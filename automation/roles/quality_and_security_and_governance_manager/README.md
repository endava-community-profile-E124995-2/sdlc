# Quality And Security And Governance Manager

This package is the canonical quality, security, and governance role definition for the Codex SDLC workspace. The repo-local adapter lives at [`../../../.agents/skills/quality_and_security_and_governance_manager`](../../../.agents/skills/quality_and_security_and_governance_manager), while this folder holds the source-of-truth agent contract and assets.

## Active Surface

- `agent/manifest.md`: package metadata, entrypoint, and workspace context model
- `agent/inference_map.md`: routing for quality review, security review, governance mapping, and release gate work
- `agent/operating_rules.md`: clarify-first behavior, assumptions, and role boundaries
- `agent/output_contracts.md`: response shapes by task type
- `agent/source_index.md`: minimum supporting sources and workspace context rules

## Backing Assets

- `assets/training/fine_tuning/`: structured corpus, examples, evals, schemas, and validation tooling
- `assets/knowledge/legacy_role_rag/`: fallback reference pack that must not override the active contract
- `builder/migration/`: builder-only migration and packaging notes

## Role Boundaries

- Product and Requirements Manager keeps discovery, requirements, prioritization, and compliance-sensitive requirement shaping.
- Architecture and Engineering Manager owns technical design, dependency sequencing, and implementation planning.
- Quality and Security and Governance Manager owns independent assurance, control interpretation support, evidence sufficiency review, exception framing, and release-gate recommendation.
- Deployment and Operations Manager owns rollout, rollback, observability, runbooks, and runtime support readiness.
