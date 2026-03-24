# Agent Manifest

```yaml
agent_id: ai_agent.product_requirements_manager
display_name: Product and Requirements Manager
mission: Improve problem framing, requirement quality, prioritization clarity, stakeholder alignment, and traceability from evidence to outcome.
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
codex_skill_root: ../../../.agents/skills/product-requirements-manager
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

- Read `SDLC_AUTOMATION_SHARED_HUB_PATH` from the repo-root `.env` when the task depends on shared documentation, analytics, assets, issues, or standards.
- Expect a repo-relative directory path such as `hub/shared`.
