# Project Selection Policy

- If the user names a project, use that project.
- Otherwise, use `SDLC_AUTOMATION_ACTIVE_PROJECTS` only when it narrows the choice to exactly one project.
- Otherwise, inspect `projects/registry.yaml` for an unambiguous project only when the task clearly requires project-specific context.
- If the task is general and no project can be resolved, operate in shared-workspace mode.
- If the task requires project-specific output and multiple projects are plausible, ask the user instead of guessing.
- When `projects/registry.yaml` is empty, shared-workspace mode is the default and project-scoped outputs must be framed as pending project selection.
