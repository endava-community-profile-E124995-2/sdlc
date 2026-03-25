# Response Format

- Keep answers concise and task-shaped.
- Separate `Fact:`, `Inference:`, and `Assumption:` when certainty differs.
- Do not present proposed code, approvals, rollout readiness, or completed execution as already done unless it has actually happened.
- When a durable artifact is required, name the target location explicitly:
  - project-specific durable records go under `projects/<project-id>/hub/`
  - reusable cross-project governance or standards go under `hub/shared/standards/`
- When handing work to another role, use the shared handoff contract rather than free-form prose.
