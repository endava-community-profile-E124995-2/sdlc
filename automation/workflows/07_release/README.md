# Release Workflow

## Required Inputs

- approved change set
- release scope and target environment
- Release Gate Memo and rollback expectations

## Role Handoffs

- primary: Deployment and Operations Manager
- upstream dependencies: Architecture and Engineering Manager and Quality and Security and Governance Manager
- upstream gate input: Quality and Security and Governance Manager for exception framing, evidence sufficiency, and release-gate recommendation

## Expected Artifacts

- rollout plan
- release checklist
- rollback and communication notes
- explicit gate prerequisite tracking when release approval is not yet satisfied

## Output Location

- `projects/<project-id>/hub/technology/`
- `projects/<project-id>/hub/issues/`
