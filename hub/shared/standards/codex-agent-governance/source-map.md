# Source Map

## Behavioral Sources Of Truth

- repo routing and cross-role ownership: `AGENTS.md`
- shared Codex governance: `hub/shared/standards/codex-agent-governance/`
- role runtime behavior: `automation/roles/*/agent/`

## Factual Context Sources

- project-specific facts: `projects/<project-id>/hub/`
- shared workspace facts: `hub/shared/`
- role-specific examples, schemas, and retrieval assets: `automation/roles/*/assets/`

## Thin Adapter Surfaces

- `.agents/shared/`: app-facing shared governance pointers
- `.agents/skills/*/SKILL.md`: app-facing role adapters
- `.agents/skills/*/agents/openai.yaml`: app-facing discovery cards

These files are adapters, not canonical authoring locations.

## Generated Surfaces

- `.agents/registry.yaml`: generated workspace discovery registry

Generated files must be regenerated from canonical sources, not edited as the primary source of truth.
