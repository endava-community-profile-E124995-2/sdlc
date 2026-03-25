# Quality Workflow

## Required Inputs

- execution plan or change scope
- relevant controls, risk posture, and release gate expectations
- target test and review depth
- available evidence, known gaps, and exception requests

## Role Handoffs

- primary: Quality and Security and Governance Manager
- upstream dependency: Architecture and Engineering Manager for unresolved technical boundary questions
- upstream dependency: Product and Requirements Manager when policy interpretation depends on missing business rules
- downstream handoff: Deployment and Operations Manager when gate outcomes depend on rollout, rollback, monitoring, or support-readiness work

## Expected Artifacts

- Quality Review Note
- Security Review Note
- Governance Mapping Note
- Release Gate Memo

## Output Location

- `projects/<project-id>/hub/issues/`
- `projects/<project-id>/hub/decisions/`
- `hub/shared/standards/` when a reusable control or policy is identified
