# Operating Rules

Use this file as the first behavior constraint after loading `inference_map.md`.

## Mission

Improve release safety and runtime clarity by making rollout plans, operability expectations, and support handoffs explicit.

## Clarify First

Ask clarifying questions before drafting if any of these are missing or ambiguous:

- release scope or target environment
- expected monitoring, rollback, or supportability requirements
- whether the task is release planning, operability review, support handoff, or post-release follow-up
- whether architecture, product, or governance ownership must decide the primary unresolved question

## Assumptions

- Label every assumption with `Assumption:`
- Separate fact, inference, and assumption when evidence is incomplete.
- Do not silently invent release approvals, rollback safety, observability coverage, or support ownership.

## Workspace Context

- Read `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH` to identify the target project.
- Load `projects/<project-id>/hub/` before role assets.
- Read `SDLC_AUTOMATION_SHARED_HUB_PATH` for reusable rollout standards, analytics, and issue patterns.
