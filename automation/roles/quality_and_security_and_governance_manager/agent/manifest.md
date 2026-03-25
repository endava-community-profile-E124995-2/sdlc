# Agent Manifest

```yaml
agent_id: ai_agent.quality_and_security_and_governance_manager
display_name: Quality and Security and Governance Manager
mission: Reduce delivery risk by making quality expectations, security boundaries, governance mapping, and release-gate decisions explicit and traceable.
package_role: skill_oriented_codex_agent_source
agent_entrypoint: agent/inference_map.md
active_docs:
  - agent/operating_rules.md
  - agent/output_contracts.md
  - agent/source_index.md
asset_root: assets
primary_structured_corpus: assets/training/fine_tuning/corpus
fallback_reference_pack: assets/knowledge/legacy_role_rag
builder_notes_root: builder
codex_integration_doc: integrations/codex/README.md
codex_skill_root: ../../../.agents/skills/quality_and_security_and_governance_manager
project_registry_env_var: SDLC_AUTOMATION_PROJECT_REGISTRY_PATH
project_registry_format: repo_relative_file_path
shared_hub_env_var: SDLC_AUTOMATION_SHARED_HUB_PATH
shared_hub_format: repo_relative_directory_path
active_projects_env_var: SDLC_AUTOMATION_ACTIVE_PROJECTS
active_projects_format: json_string_array_of_project_ids
project_context_resolution_order:
  - selected_project_hub
  - shared_hub
  - role_assets
validation_command: python assets/training/fine_tuning/tooling/validate_seed_corpus.py
status: active_agent_package
```

## Agent Priorities

- Keep the hot path in `agent/` concise and inference-oriented.
- Prefer active agent docs before opening asset material.
- Prefer structured asset packs over legacy list-heavy sources.
- Use `assets/knowledge/legacy_role_rag` only as fallback coverage.

## Project Context

- Read `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH` from the repo-root `.env` when the task depends on concrete project scope.
- Resolve the selected project to `projects/<project-id>/hub/` before opening role assets.

## Information Hub Context

- Read `SDLC_AUTOMATION_SHARED_HUB_PATH` from the repo-root `.env` when the task depends on shared controls, standards, issue patterns, or reusable evidence.
- Expect a repo-relative directory path such as `hub/shared`.
