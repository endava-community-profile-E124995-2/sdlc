# Asset Packs

This folder contains the heavier source material that does not belong in the small active `agent/` surface.

## Contents

- `knowledge/`: fallback reference material and legacy rewrite context
- `training/`: structured corpus, schemas, examples, evals, and validation tooling

## Usage

- Treat this folder as backing source material for `../agent` and the repo-local Codex skill.
- Keep routing, operating rules, output contracts, and package metadata in `../agent`.
- Keep migration and maintenance-only notes in `../builder`.
- Validate the asset corpus with `python training/fine_tuning/tooling/validate_seed_corpus.py` when working from this folder, or `python assets/training/fine_tuning/tooling/validate_seed_corpus.py` when working from the package root.
