# Shared Tool And Context Rules

This is a thin adapter for the canonical tool and context rules.

Canonical source: [tool-access-rules.md](../../hub/shared/standards/codex-agent-governance/tool-access-rules.md)

- read `.env` before resolving workspace context
- resolve project and shared hubs before role assets
- use `.artifacts/` for ephemeral run output
