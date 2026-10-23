"""Read-only agreement check for AEK routing v2 and project-local Codex files."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import tomllib


class NotEvaluated(Exception):
    """A known limitation must not be reported as successful agreement."""


def table(value: object, field: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{field}: expected a table")
    return {str(key): item for key, item in value.items()}


def text(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field}: expected a nonempty string")
    return value


def boolean(value: object, field: str) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"{field}: expected a Boolean")
    return value


def integer(value: object, field: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError(f"{field}: expected a nonnegative integer")
    return value


def contained(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError(f"{relative}: path outside root")
    return path


def read(root: Path, relative: str) -> dict[str, object]:
    path = contained(root, relative)
    try:
        return table(tomllib.loads(path.read_text(encoding="utf-8")), relative)
    except (OSError, UnicodeError, ValueError) as error:
        raise ValueError(f"{relative}: {error}") from error


@dataclass(frozen=True)
class Pair:
    model: str
    effort: str


def pair(data: dict[str, object], effort_key: str, field: str) -> Pair:
    return Pair(text(data.get("model"), f"{field}.model"),
                text(data.get(effort_key), f"{field}.{effort_key}"))


@dataclass(frozen=True)
class Selection:
    roles: dict[str, Pair]
    disabled: frozenset[str]
    mode: str
    ceiling: int


def validate_graph(raw: object, roles: dict[str, Pair]) -> None:
    if not isinstance(raw, list):
        raise ValueError("orchestration.allowed_edges: expected an array")
    edges: set[tuple[str, str]] = set()
    for value in raw:
        edge = text(value, "allowed edge")
        parts = edge.split("->")
        if len(parts) != 2 or any(char.isspace() for char in edge):
            raise ValueError(f"invalid edge: {edge}")
        parent, child = parts
        if parent not in roles or child not in roles:
            raise ValueError(f"edge endpoints must be enabled: {edge}")
        if parent == child:
            raise ValueError(f"self edge: {edge}")
        if (parent, child) in edges:
            raise ValueError(f"duplicate edge: {edge}")
        edges.add((parent, child))
    remaining = set(roles)
    while remaining:
        roots = {role for role in remaining if not any(
            parent in remaining and child == role for parent, child in edges)}
        if not roots:
            raise ValueError("allowed_edges: cycle")
        remaining -= roots
    reachable = {"orchestrator"}
    while added := {child for parent, child in edges if parent in reachable} - reachable:
        reachable |= added
    if any(parent not in reachable for parent, _ in edges):
        raise ValueError("allowed_edges: parent unreachable from orchestrator")


def selection(data: dict[str, object]) -> Selection:
    version = integer(data.get("schema_version"), "schema_version")
    if version != 2:
        raise NotEvaluated(f"routing schema {version}; only configured schema 2 is supported")
    status = text(data.get("status"), "status")
    if status == "unconfigured":
        raise NotEvaluated("routing is unconfigured; no saved agreement to check")
    if status != "configured":
        raise ValueError("status: expected configured or unconfigured")
    if data.get("scope") != "workspace":
        raise ValueError("scope: expected workspace")
    client = text(data.get("client"), "client")
    if client not in {"codex", "claude-code", "cursor"}:
        raise ValueError("client: unknown client")
    if client != "codex":
        raise NotEvaluated(f"{client}: native mapping is not implemented by this checker")
    roles: dict[str, Pair] = {}
    disabled: set[str] = set()
    for name, raw in table(data.get("roles"), "roles").items():
        if not re.fullmatch(r"[A-Za-z0-9_-]+", name):
            raise NotEvaluated(f"role ID {name!r}: unsupported filename mapping")
        role = table(raw, f"roles.{name}")
        if boolean(role.get("enabled"), f"roles.{name}.enabled"):
            roles[name] = pair(role, "reasoning_effort", f"roles.{name}")
        else:
            disabled.add(name)
    if "orchestrator" not in roles:
        raise ValueError("roles.orchestrator: must be enabled with an explicit pair")
    scheme = table(data.get("orchestration"), "orchestration")
    mode = text(scheme.get("mode"), "orchestration.mode")
    ceiling = integer(data.get("max_subagents"), "max_subagents")
    validate_graph(scheme.get("allowed_edges"), roles)
    if mode == "single-agent":
        if ceiling != 0 or len(roles) != 1 or scheme["allowed_edges"] != []:
            raise ValueError("single-agent mode requires zero ceiling, no specialists and no edges")
    elif mode == "delegated":
        if ceiling == 0:
            raise ValueError("delegated mode requires a positive ceiling")
    else:
        raise ValueError("orchestration.mode: expected single-agent or delegated")
    return Selection(roles, frozenset(disabled), mode, ceiling)


def native_roles(root: Path, chosen: Selection) -> None:
    directory = contained(root, ".codex/agents")
    by_name: dict[str, Path] = {}
    known = set(chosen.roles) | chosen.disabled
    for path in sorted(directory.glob("*.toml")):
        data = read(root, str(path.relative_to(root)))
        name = text(data.get("name"), f"{path.name}.name")
        if name not in {f"af-{role}" for role in known}:
            continue
        if name in by_name:
            raise ValueError(f"{path}: duplicate native name {name}")
        by_name[name] = path
        if name.removeprefix("af-") in chosen.disabled:
            raise ValueError(f"{path}: disabled role remains discoverable: {name}")
    for role in chosen.disabled:
        if contained(root, f".codex/agents/af-{role}.toml").exists():
            raise ValueError(f"af-{role}: disabled role path remains discoverable")
    for role, expected in chosen.roles.items():
        if role == "orchestrator":
            continue
        relative = f".codex/agents/af-{role}.toml"
        data = read(root, relative)
        if data.get("name") != f"af-{role}":
            raise ValueError(f"{relative}: name must be af-{role}")
        for field in ("description", "developer_instructions"):
            text(data.get(field), f"{relative}.{field}")
        if pair(data, "model_reasoning_effort", relative) != expected:
            raise ValueError(f"{relative}: model/reasoning pair differs from saved role")


ROUTING_RECORD = ".agents-framework/model-routing.toml"


def check(root: Path, default_role: str | None) -> None:
    if not contained(root, ROUTING_RECORD).exists() and not (root / ROUTING_RECORD).is_symlink():
        raise NotEvaluated(f"{ROUTING_RECORD} is missing; no saved agreement to check")
    chosen = selection(read(root, ROUTING_RECORD))
    config = read(root, ".codex/config.toml")
    if pair(config, "model_reasoning_effort", ".codex/config.toml") != chosen.roles["orchestrator"]:
        raise ValueError(".codex/config.toml: coordinator model/reasoning pair differs")
    agents = table(config.get("agents"), ".codex/config.toml agents")
    enabled = boolean(agents.get("enabled"), "agents.enabled")
    if enabled != (chosen.mode == "delegated"):
        raise ValueError("agents.enabled: differs from saved mode")
    # Definite conflicts found by later checks take precedence over this limitation.
    pending: NotEvaluated | None = None
    if enabled:
        if "max_concurrent_threads_per_session" not in agents:
            pending = NotEvaluated("agents.max_concurrent_threads_per_session is absent; "
                                   "native ceiling agreement not evaluated")
        else:
            ceiling = integer(agents.get("max_concurrent_threads_per_session"), "native ceiling")
            if ceiling != chosen.ceiling:
                raise ValueError("native ceiling differs from max_subagents")
    if default_role is not None:
        if default_role == "orchestrator" or default_role not in chosen.roles:
            raise ValueError("--default-role must name an enabled specialist")
        expected = chosen.roles[default_role]
        for key, value in (("default_subagent_model", expected.model),
                           ("default_subagent_reasoning_effort", expected.effort)):
            if agents.get(key) != value:
                raise ValueError(f"agents.{key}: differs from explicit default role {default_role}")
    native_roles(root, chosen)
    if pending is not None:
        raise pending


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True, help="target instruction root")
    parser.add_argument("--default-role", help="explicit expected role for native worker defaults")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    try:
        check(root, args.default_role)
    except NotEvaluated as error:
        print(f"Agreement not evaluated: {error}")
        return 2
    except ValueError as error:
        print(f"Agreement error: {error}")
        return 1
    defaults = f"defaults compared to {args.default_role}" if args.default_role else "defaults not compared"
    print(f"Saved Codex agreement passed ({defaults}). Project-local files only; "
          "runtime loading, overrides, model availability and effective permissions are not verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
