from __future__ import annotations

import sys
from pathlib import Path

from generate_agent_registry import ROOT, build_registry, parse_simple_yaml


CANONICAL_GOVERNANCE_FILES = [
    "README.md",
    "precedence.md",
    "source-map.md",
    "response-format.md",
    "escalation-rules.md",
    "handoff-contracts.md",
    "validation-checklist.md",
    "tool-access-rules.md",
    "project-selection-policy.md",
]


def relative_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def add_missing_file_errors(errors: list[str], root: Path, base: Path, filenames: list[str], label: str) -> None:
    for name in filenames:
        target = base / name
        if not target.exists():
            errors.append(f"Missing {label}: {relative_path(target)}")


def main() -> int:
    errors: list[str] = []

    registry_path = ROOT / ".agents" / "registry.yaml"
    if not registry_path.exists():
        errors.append("Missing generated registry: .agents/registry.yaml")
    else:
        actual_registry = parse_simple_yaml(registry_path.read_text(encoding="utf-8"))
        expected_registry = build_registry(ROOT)
        if actual_registry != expected_registry:
            errors.append("Generated registry is out of sync. Re-run automation/tooling/generate_agent_registry.py.")

    add_missing_file_errors(
        errors,
        ROOT,
        ROOT / "hub" / "shared" / "standards" / "codex-agent-governance",
        CANONICAL_GOVERNANCE_FILES,
        "canonical governance file",
    )
    add_missing_file_errors(
        errors,
        ROOT,
        ROOT / ".agents" / "shared",
        CANONICAL_GOVERNANCE_FILES,
        "shared adapter file",
    )

    agents_md = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    for role_name, entry in build_registry(ROOT)["agents"].items():
        token = entry["invocation_token"]
        if token not in agents_md:
            errors.append(f"AGENTS.md does not mention {token}.")

        role_root = ROOT / entry["canonical_role_root"]
        integration_readme = role_root / "integrations" / "codex" / "README.md"
        integration_text = integration_readme.read_text(encoding="utf-8")

        if token not in integration_text:
            errors.append(f"{relative_path(integration_readme)} does not mention {token}.")
        if ".agents/registry.yaml" not in integration_text:
            errors.append(f"{relative_path(integration_readme)} does not mention .agents/registry.yaml.")
        if ".agents/shared/README.md" not in integration_text:
            errors.append(f"{relative_path(integration_readme)} does not mention .agents/shared/README.md.")

        skill_path = ROOT / entry["skill_instruction_path"]
        skill_text = skill_path.read_text(encoding="utf-8")
        if "../../shared/precedence.md" not in skill_text:
            errors.append(f"{relative_path(skill_path)} does not reference shared governance.")

        openai_card_path = ROOT / entry["openai_card_path"]
        openai_text = openai_card_path.read_text(encoding="utf-8")
        if token not in openai_text:
            errors.append(f"{relative_path(openai_card_path)} default prompt does not mention {token}.")
        if ".agents/shared" not in openai_text:
            errors.append(f"{relative_path(openai_card_path)} default prompt does not mention .agents/shared.")

    if "Codex Agent Governance" not in readme:
        errors.append("README.md does not describe Codex Agent Governance.")
    if ".agents/registry.yaml" not in readme:
        errors.append("README.md does not mention .agents/registry.yaml.")

    eval_readme = ROOT / "automation" / "evals" / "system" / "README.md"
    if not eval_readme.exists():
        errors.append("Missing automation/evals/system/README.md.")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Workspace Codex agent validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
