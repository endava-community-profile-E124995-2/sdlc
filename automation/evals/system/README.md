# System Smoke Evals

This folder holds workspace-level smoke prompts for the repo-local Codex agents.

## Coverage

- explicit invocation
- implicit routing
- mixed-role handoffs
- projectless mode behavior

## Execution

- run the prompts manually in Codex from the repo root
- compare the selected role and handoff behavior with the expectations in these files
- run `python automation/tooling/validate_codex_agent_workspace.py` alongside the manual smoke pass
