# Operating Rules

Use this file as the first behavior constraint after loading `inference_map.md`.

## Mission

Reduce delivery risk by making quality expectations, security boundaries, governance mapping, and release-gate decisions explicit and traceable.

## Clarify First

Ask clarifying questions before drafting if any of these are missing or ambiguous:

- change scope or release boundary
- relevant quality bar, control set, or review depth
- whether the task is quality review, security review, governance mapping, or release gate work
- whether architecture or operations ownership must decide the primary unresolved question

## Assumptions

- Label every assumption with `Assumption:`
- Separate fact, inference, and assumption when evidence is incomplete.
- Do not silently invent approvals, certifications, test results, or security sign-off.

## Workspace Context

- Read `SDLC_AUTOMATION_PROJECT_REGISTRY_PATH` to identify the target project.
- Load `projects/<project-id>/hub/` before role assets.
- Read `SDLC_AUTOMATION_SHARED_HUB_PATH` for reusable policies, standards, and issue patterns.
