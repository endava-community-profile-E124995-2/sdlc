# Knowledge Layer

This folder holds role knowledge sources.

## Subfolders

- `legacy_role_rag/`: the original broad role taxonomy and reference pack.

## Builder Rule

Treat the legacy pack as:

- source material for migration
- fallback retrieval coverage
- a way to widen domain recall

Do not treat it as the primary runtime control layer. Runtime behavior should come from the structured training corpus and runtime inference map.
