# Projectless Mode Cases

- Prompt: "`Using the current workspace, tell me where to store a rollout ADR for a project that has not been registered yet.`"
  Expected: the response stays in shared-workspace mode, states that `projects/registry.yaml` is empty, and does not invent a project hub path.
- Prompt: "`Summarize the shared standards relevant to release gating in this workspace.`"
  Expected: the response uses `hub/shared/` context only and does not require a project selection.
