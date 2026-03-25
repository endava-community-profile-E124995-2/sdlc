from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def parse_scalar(value: str):
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1].replace('\\"', '"')
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("\\'", "'")
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def parse_simple_yaml(text: str) -> dict:
    root: dict = {}
    stack: list[tuple[int, dict]] = [(-1, root)]

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        content = raw_line.strip()

        if content.startswith("- "):
            continue

        if ":" not in content:
            continue

        key, value = content.split(":", 1)
        key = key.strip()
        value = value.strip()

        while len(stack) > 1 and indent <= stack[-1][0]:
            stack.pop()

        current = stack[-1][1]
        if not value:
            child: dict = {}
            current[key] = child
            stack.append((indent, child))
        else:
            current[key] = parse_scalar(value)

    return root


def parse_markdown_front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8").lstrip("\ufeff")
    match = re.search(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    if not match:
        raise ValueError(f"Missing front matter in {path}")
    return parse_simple_yaml(match.group(1))


def parse_markdown_fenced_yaml(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"```yaml\r?\n(.*?)\r?\n```", text, re.DOTALL)
    if not match:
        raise ValueError(f"Missing fenced yaml block in {path}")
    return parse_simple_yaml(match.group(1))


def relative_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def build_registry(root: Path = ROOT) -> dict:
    agents: dict = {}
    manifest_paths = sorted((root / "automation" / "roles").glob("*/agent/manifest.md"))

    for manifest_path in manifest_paths:
        manifest = parse_markdown_fenced_yaml(manifest_path)
        role_root = manifest_path.parents[1]
        skill_root = (role_root / manifest["codex_skill_root"]).resolve()
        skill_path = skill_root / "SKILL.md"
        openai_card_path = skill_root / "agents" / "openai.yaml"

        skill_meta = parse_markdown_front_matter(skill_path)
        openai_card = parse_simple_yaml(openai_card_path.read_text(encoding="utf-8"))

        role_name = skill_meta["name"]
        agents[role_name] = {
            "display_name": manifest["display_name"],
            "directory_name": skill_root.name,
            "canonical_role_root": relative_path(role_root),
            "manifest_path": relative_path(manifest_path),
            "skill_root": relative_path(skill_root),
            "skill_instruction_path": relative_path(skill_path),
            "openai_card_path": relative_path(openai_card_path),
            "invocation_token": f"${role_name}",
            "short_description": openai_card["interface"]["short_description"],
            "allow_implicit_invocation": openai_card["policy"]["allow_implicit_invocation"],
            "validation_command": manifest["validation_command"],
            "status": manifest["status"],
        }

    return {
        "version": 1,
        "generated_by": "automation/tooling/generate_agent_registry.py",
        "agents": agents,
    }


def render_scalar(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    escaped = str(value).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def render_registry(registry: dict) -> str:
    lines = [
        f"version: {registry['version']}",
        f"generated_by: {render_scalar(registry['generated_by'])}",
        "agents:",
    ]

    for key, entry in sorted(registry["agents"].items()):
        lines.append(f"  {key}:")
        for field, value in entry.items():
            lines.append(f"    {field}: {render_scalar(value)}")

    return "\n".join(lines) + "\n"


def main() -> int:
    registry_path = ROOT / ".agents" / "registry.yaml"
    registry = build_registry(ROOT)
    registry_path.write_text(render_registry(registry), encoding="utf-8")
    print(f"Wrote {relative_path(registry_path)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
