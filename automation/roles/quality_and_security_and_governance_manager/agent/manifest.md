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
validation_command: not_yet_defined
status: active_agent_package
```
