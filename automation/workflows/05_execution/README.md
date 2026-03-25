# Execution Workflow

## Required Inputs

- approved architecture decision
- scoped work items
- dependency order and validation goals

## Role Handoffs

- primary: Architecture and Engineering Manager
- downstream handoff: Quality and Security and Governance Manager for Quality Review Note or Security Review Note when validation, controls, or evidence questions are primary
- downstream handoff: Deployment and Operations Manager for Rollout Plan or Operability Review when rollout sequence, rollback, observability, or support ownership become primary

## Expected Artifacts

- engineering execution plan
- repo ownership map
- dependency sequence and validation checkpoints
- downstream assurance handoff when release-gate evidence must be prepared
- downstream deployment handoff when the release path must be operationalized

## Output Location

- `projects/<project-id>/hub/technology/`
- `projects/<project-id>/hub/decisions/`
