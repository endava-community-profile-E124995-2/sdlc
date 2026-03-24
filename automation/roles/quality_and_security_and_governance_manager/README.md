# Quality And Security And Governance Manager

This package is the canonical quality, security, and governance role definition for the Codex SDLC workspace. The repo-local adapter lives at [`../../../.agents/skills/quality_and_security_and_governance_manager`](../../../.agents/skills/quality_and_security_and_governance_manager), while this folder holds the source-of-truth agent contract and assets.

## Active Surface

- `agent/manifest.md`: package metadata, entrypoint, and workspace context model
- `agent/inference_map.md`: routing for quality review, security review, governance mapping, and release gate work
- `agent/operating_rules.md`: clarify-first behavior, assumptions, and role boundaries
- `agent/output_contracts.md`: response shapes by task type
- `agent/source_index.md`: minimum supporting sources and workspace context rules
