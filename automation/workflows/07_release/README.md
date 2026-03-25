# Release Workflow

## Required Inputs

- approved change set
- release scope and target environment
- Release Gate Memo and operating expectations

## Role Handoffs

- primary: Deployment and Operations Manager
- upstream dependencies: Architecture and Engineering Manager and Quality and Security and Governance Manager
- upstream gate input: Quality and Security and Governance Manager for exception framing, evidence sufficiency, and release-gate recommendation

## Expected Artifacts

- Rollout Plan
- Operations Handoff Note when runtime ownership must transfer during or immediately after release
- rollback, communication, and gate-prerequisite tracking embedded in the Rollout Plan

## Output Location

- `projects/<project-id>/hub/technology/`
- `projects/<project-id>/hub/issues/`
