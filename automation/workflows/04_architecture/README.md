# Architecture Workflow

## Required Inputs

- approved product intent
- affected systems or repos
- constraints and non-functional expectations

## Role Handoffs

- primary: Architecture and Engineering Manager
- upstream dependency: Product and Requirements Manager for unresolved intent gaps
- downstream handoff: Quality and Security and Governance Manager for Security Review Note, Governance Mapping Note, or Quality Review Note when controls, evidence, or verification sufficiency become primary
- downstream handoff: Deployment and Operations Manager for Rollout Plan or Operability Review when rollback, observability, runbooks, or support ownership become primary

## Expected Artifacts

- feasibility brief
- architecture decision record
- interface and dependency notes
- downstream quality handoff when approval, control interpretation, or evidence sufficiency must be reviewed independently
- downstream deployment handoff when runtime readiness work must move into operational ownership

## Output Location

- `projects/<project-id>/hub/technology/`
- `projects/<project-id>/hub/decisions/`
