#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_MAP = ROOT / "corpus" / "ontology" / "canonical_id_map.md"
ARTIFACTS_DIR = ROOT / "corpus" / "artifacts"

ID_PATTERN = re.compile(r"`([a-z]+\.[a-z0-9_]+(?:\.[a-z0-9_]+)*)`")
EXAMPLE_REF_PATTERN = re.compile(r"(?:good_example_ref|bad_example_ref):\s*(\S+)")


def load_canonical_ids() -> set[str]:
    return set(ID_PATTERN.findall(CANONICAL_MAP.read_text()))


def collect_unknown_ids(canonical_ids: set[str]) -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.md"):
        if path == CANONICAL_MAP:
            continue
        text = path.read_text()
        unknown_ids = sorted(
            {
                identifier
                for identifier in ID_PATTERN.findall(text)
                if identifier not in canonical_ids and not identifier.startswith("schema.")
            }
        )
        if unknown_ids:
            rel_path = path.relative_to(ROOT)
            errors.append(f"{rel_path}: unknown ids -> {', '.join(unknown_ids)}")
    return errors


def collect_missing_examples() -> list[str]:
    errors: list[str] = []
    for path in ARTIFACTS_DIR.glob("*.md"):
        text = path.read_text()
        for ref in EXAMPLE_REF_PATTERN.findall(text):
            if not (ROOT / ref).exists():
                rel_path = path.relative_to(ROOT)
                errors.append(f"{rel_path}: missing example ref -> {ref}")
    return errors


def main() -> int:
    canonical_ids = load_canonical_ids()
    errors = collect_unknown_ids(canonical_ids)
    errors.extend(collect_missing_examples())

    if errors:
        print("Seed corpus validation failed.")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Seed corpus validation passed.")
    print(f"Canonical IDs loaded: {len(canonical_ids)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
