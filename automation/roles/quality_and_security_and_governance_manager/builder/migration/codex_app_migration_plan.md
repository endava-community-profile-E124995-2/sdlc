# Codex App Migration Plan

## Summary

- Persist the Quality and Security and Governance Manager role as a repo-local Codex skill at `.agents/skills/quality_and_security_and_governance_manager`.
- Keep this agent package split into a thin active layer under `agent/` and a broader structured corpus under `assets/`.
- Use the live skill as a thin runtime adapter that loads distilled references on demand instead of copying the full corpus into the skill.
- Align repo routing so quality, security, governance, evidence, and release-gate requests land on this role rather than remaining mixed into product or deployment surfaces.

## Decisions

- Skill name: `quality-and-security-and-governance-manager`
- Display name: `Quality and Security and Governance Manager`
- Placement: repo-local only in v1
- Activation: hybrid auto plus explicit invocation
- Source-of-truth runtime behavior: `agent/inference_map.md` and the structured corpus under `assets/training/fine_tuning/corpus`
- Fallback knowledge: `assets/knowledge/legacy_role_rag`

## Target Deliverables

1. `.agents/skills/quality_and_security_and_governance_manager/SKILL.md`
2. `.agents/skills/quality_and_security_and_governance_manager/agents/openai.yaml`
3. `.agents/skills/quality_and_security_and_governance_manager/references/operating-policy.md`
4. `.agents/skills/quality_and_security_and_governance_manager/references/artifact-routing.md`
5. `.agents/skills/quality_and_security_and_governance_manager/references/interaction-cases.md`
6. `.agents/skills/quality_and_security_and_governance_manager/references/context-variants.md`
7. `AGENTS.md`
8. package README updates and the structured quality corpus under `assets/training/fine_tuning/`

## Implementation Rules

- Keep the skill instruction-only in v1.
- Distill runtime behavior into the skill and reference files instead of copying the full corpus.
- Preserve role boundaries:
  - use this role for independent quality review, security boundary review, control mapping, evidence sufficiency, exception framing, and release-gate recommendation
  - do not use this role to replace product discovery, architecture ownership, or deployment ownership
- Load only the reference file needed for the current task.
- Apply no more than one context variant unless the request clearly spans multiple environments.

## Verification

- Run `python assets/training/fine_tuning/tooling/validate_seed_corpus.py`.
- Verify the skill is discoverable from the repo root in Codex app.
- Verify explicit invocation with `$quality-and-security-and-governance-manager`.
- Verify implicit routing for quality review, security review, governance mapping, and release-gate work.
- Verify the role hands back to product, architecture, or deployment when ownership is outside independent assurance.
