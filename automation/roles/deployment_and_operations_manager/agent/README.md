# Agent Surface

This folder is the hot path for the Deployment and Operations Manager agent.

## Load Order

1. [inference_map.md](inference_map.md)
2. [operating_rules.md](operating_rules.md)
3. [output_contracts.md](output_contracts.md)
4. [source_index.md](source_index.md)
5. selected structured asset files from `../assets/training/fine_tuning/`
6. `../assets/knowledge/legacy_role_rag/` only as fallback

## Workspace Context

- Read `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH` from the repo-root `.env` to identify the target project.
- Load `projects/<project-id>/hub/` as the primary project context before role assets.
- Read `SDLC_AUTOMATION_SHARED_HUB_PATH` from the repo-root `.env` for reusable release, operations, incident, and standards context.
- Use `SDLC_AUTOMATION_ACTIVE_PROJECTS` only as an optional narrowing filter when several projects are attached.
