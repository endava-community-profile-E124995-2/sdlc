# Instruction Precedence

## Behavioral Instruction Order

1. Codex runtime system, developer, and tool policies
2. repo-root `AGENTS.md`
3. `.agents/shared/*.md`
4. `.agents/skills/*/SKILL.md`
5. `automation/roles/*/agent/*.md`
6. role asset material under `automation/roles/*/assets/`

Lower layers may add detail but must not override higher-layer rules.

## Context Resolution Order

1. explicit project named by the user
2. `SDLC_AUTOMATION_ACTIVE_PROJECTS` when it narrows to one project
3. `projects/<project-id>/hub/`
4. `hub/shared/`
5. this shared governance pack
6. role-specific asset material
7. legacy fallback packs

## Projectless Mode

When no project can be resolved, stay in shared-workspace mode. Do not invent project ids, project hubs, or project-specific output locations.
