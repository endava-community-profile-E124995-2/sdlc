# Agent Manifest

```yaml
agent_id: ai_agent.architecture_and_engineering_manager
display_name: Architecture and Engineering Manager
mission: Reduce technical ambiguity by turning approved product intent into feasible architectures, implementation plans, dependency sequencing, and explicit cross-role handoffs.
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
codex_skill_root: ../../../../.agents/skills/architecture_and_engineering_manager
project_paths_env_var: SDLC_AUTOMATION_PROJECT_PATHS
project_paths_format: json_string_array_of_repo_relative_paths
information_hub_paths_env_var: SDLC_AUTOMATION_INFORMATION_HUB_PATHS
information_hub_paths_format: json_string_array_of_repo_relative_paths
validation_command: python assets/training/fine_tuning/tooling/validate_seed_corpus.py
status: active_agent_package
```

## Agent Priorities

- Keep the hot path in `agent/` concise and inference-oriented.
- Prefer active agent docs before opening asset material.
- Prefer structured asset packs over legacy list-heavy sources.
- Use `assets/knowledge/legacy_role_rag` only as fallback coverage.

## Project Context

- Read `SDLC_AUTOMATION_PROJECT_PATHS` from the repo-root `.env` when the task depends on concrete project scope.
- Expect a JSON string array of repo-relative `sdlc_automation\projects\...` paths.

## Information Hub Context

- Read `SDLC_AUTOMATION_INFORMATION_HUB_PATHS` from the repo-root `.env` when the task depends on shared documentation, analytics, assets, or reported issues.
- Expect a JSON string array of repo-relative `sdlc_automation\information_hub\...` paths.
