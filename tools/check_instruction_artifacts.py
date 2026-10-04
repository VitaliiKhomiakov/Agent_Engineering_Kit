"""Read-only checks for the documented instruction-library Markdown/TOML subset."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import html
from pathlib import Path
import re
from collections.abc import Sequence
import tomllib
from urllib.parse import unquote, urlsplit


ARTIFACT_SUFFIXES = {".md", ".mdc", ".toml"}
# These source templates describe paths from their installed workspace root.
ROOT_LINK_TEMPLATES = {"templates/policy-entry.md", "templates/AGENTS.root.md", "templates/PLANS.md"}
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
INLINE_CODE = re.compile(r"(`+)(.+?)\1(?!`)")
LINK = re.compile(r"!?\[([^\[\]\n]*(?:\n[^\[\]\n]+)*)\]\(([^()\n]*)\)")
DESTINATION = re.compile(r'(?:<([^<>]+)>|([^\s<>]+))(?:\s+"[^"\n]*")?')
POLICY_ENUMS = {
    "verification.timing": {"phase_end", "task_end"},
    "review.independent": {"risk_based", "on_request"},
}
POLICY_INTEGERS = {
    "verification.diagnostic_reset_after_stalled_attempts",
    "size.function_review_lines", "size.class_review_lines", "size.file_review_lines",
    "size.growth_review_from_lines", "size.documented_review_above_lines",
    "size.react_component_review_lines",
}
POLICY_RANGES = {"instructions.root_guideline_lines", "instructions.local_guideline_lines"}
POLICY_FIELDS = set(POLICY_ENUMS) | POLICY_INTEGERS | POLICY_RANGES


@dataclass(frozen=True)
class Diagnostic:
    path: Path
    line: int
    message: str


@dataclass(frozen=True)
class Link:
    line: int
    target: str


@dataclass(frozen=True)
class Document:
    anchors: frozenset[str]
    links: tuple[Link, ...]
    diagnostics: tuple[Diagnostic, ...]


@dataclass(frozen=True)
class Profile:
    name: str
    source: str
    resources: tuple[str, ...]
    dependencies: tuple[str, ...]
    required: bool
    line: int


def string(value: object) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError("expected a nonempty string")
    return value


def strings(value: object) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise ValueError("expected an array of strings")
    return tuple(string(item) for item in value)


def table(value: object) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError("expected a table")
    return {string(key): item for key, item in value.items()}


def positive_integer(value: object, field_name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise ValueError(f"{field_name}: expected a positive integer, not Boolean")
    return value


def validate_policy(data: dict[str, object], *, complete: bool) -> dict[str, int]:
    """Validate fields and return numeric values for merged growth constraints."""
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        raise ValueError("schema_version: expected integer 1")
    present: set[str] = set()
    numbers: dict[str, int] = {}
    groups = {name.split(".")[0] for name in POLICY_FIELDS}
    for group, raw in data.items():
        if group == "schema_version":
            continue
        if group not in groups:
            raise ValueError(f"{group}: unknown policy field")
        if not isinstance(raw, dict):
            raise ValueError(f"{group}: expected a table")
        for key, value in table(raw).items():
            name = f"{group}.{key}"
            if name not in POLICY_FIELDS:
                raise ValueError(f"{name}: unknown policy field")
            present.add(name)
            if name in POLICY_ENUMS:
                if not isinstance(value, str) or value not in POLICY_ENUMS[name]:
                    raise ValueError(f"{name}: expected one of {', '.join(sorted(POLICY_ENUMS[name]))}")
            elif name in POLICY_INTEGERS:
                numbers[name] = positive_integer(value, name)
            else:
                if not isinstance(value, list) or len(value) != 2:
                    raise ValueError(f"{name}: expected exactly two positive integers in ascending order")
                lower = positive_integer(value[0], name)
                upper = positive_integer(value[1], name)
                if lower >= upper:
                    raise ValueError(f"{name}: expected strictly ascending range")
    if complete and (missing := POLICY_FIELDS - present):
        raise ValueError(f"{sorted(missing)[0]}: missing required policy field")
    return numbers


def validate_growth(numbers: dict[str, int]) -> None:
    if numbers["size.growth_review_from_lines"] > numbers["size.documented_review_above_lines"]:
        raise ValueError("size.growth_review_from_lines: cannot exceed size.documented_review_above_lines")


def markdown(path: Path, text: str) -> Document:
    anchors: set[str] = set()
    heading_anchors: set[str] = set()
    links: list[Link] = []
    issues: list[Diagnostic] = []
    visible_lines: list[str] = []
    fence = ""
    opening = 0
    for number, line in enumerate(text.splitlines(), 1):
        visible_lines.append("")
        marker = FENCE.match(line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = ""
            continue
        if marker:
            fence, opening = marker[1], number
            continue
        if line.startswith(("    ", "\t")):
            continue
        heading = re.match(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if heading:
            label = LINK.sub(lambda match: match[1], heading[1])
            label = re.sub(r"<[^>]*>", "", html.unescape(label))
            slug = re.sub(r"[^\w\- ]", "", label.lower()).replace(" ", "-")
            candidate, suffix = slug, 0
            while candidate in heading_anchors:
                suffix += 1
                candidate = f"{slug}-{suffix}"
            anchors.add(candidate)
            heading_anchors.add(candidate)
        visible = INLINE_CODE.sub("", line)
        visible_lines[-1] = visible
        anchors.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']\s*>', visible))
    visible_text = "\n".join(visible_lines)
    for match in LINK.finditer(visible_text):
        number = visible_text.count("\n", 0, match.start()) + 1
        destination = DESTINATION.fullmatch(match[2].strip())
        if destination:
            links.append(Link(number, html.unescape(destination[1] or destination[2])))
        else:
            issues.append(Diagnostic(path, number, "unsupported link destination; use a simple inline link"))
    rest_text = LINK.sub(lambda match: "\n" * match[0].count("\n"), visible_text)
    for number, rest in enumerate(rest_text.splitlines(), 1):
        if re.search(r"\]\(|\]\[|^ {0,3}\[[^]]+\]:|<a\s+[^>]*href=|^\s*>\s*(?:`{3,}|~{3,})", rest):
            issues.append(Diagnostic(path, number, "unsupported Markdown link/fence syntax"))
    if fence:
        issues.append(Diagnostic(path, opening, "unclosed fence"))
    return Document(frozenset(anchors), tuple(links), tuple(issues))


class Checker:
    def __init__(self, root: Path, bundle_dir: str = ".", *, source_mode: bool = True) -> None:
        self.root = root.resolve()
        directory = Path(bundle_dir)
        if directory.is_absolute() or ".." in directory.parts:
            raise ValueError("bundle directory must be relative to root without traversal")
        self.bundle_root = (self.root / directory).resolve()
        if not self.bundle_root.is_relative_to(self.root):
            raise ValueError("bundle directory outside root")
        if not self.bundle_root.is_dir():
            raise ValueError("bundle directory does not exist or is not a directory")
        self.source_mode = source_mode and directory == Path(".")
        self.diagnostics: list[Diagnostic] = []
        self.documents: dict[Path, Document] = {}

    def error(self, path: Path, line: int, message: str) -> None:
        self.diagnostics.append(Diagnostic(path, line, message))

    def local_path(self, base: Path, target: str) -> Path:
        path = (base / target).resolve()
        if not path.is_relative_to(self.root):
            raise ValueError(f"path outside root: {target}")
        return path

    def document(self, path: Path) -> Document:
        if path not in self.documents:
            self.documents[path] = markdown(path, path.read_text(encoding="utf-8"))
        return self.documents[path]

    def bundle_path(self, target: str) -> Path:
        if Path(target).is_absolute():
            raise ValueError(f"bundle path must be relative: {target}")
        path = (self.bundle_root / target).resolve()
        if not path.is_relative_to(self.bundle_root):
            raise ValueError(f"path outside bundle: {target}")
        return path

    def catalog_files(self, selected: Sequence[str]) -> set[Path]:
        path = self.bundle_root / "standards/catalog.toml"
        line = 1
        try:
            path = self.bundle_path("standards/catalog.toml")
            text = path.read_text(encoding="utf-8")
            data = table(tomllib.loads(text))
            if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
                raise ValueError("expected catalog schema_version = 1")
            shared = strings(data.get("assets", []))
            templates = tuple(string(value) for value in table(data.get("templates", {})).values())
            raw_profiles = data.get("profiles")
            if not isinstance(raw_profiles, list):
                raise ValueError("expected profiles array")
            headers = [i for i, row in enumerate(text.splitlines(), 1) if re.match(r"^\s*\[\[profiles\]\]", row)]
            profiles: dict[str, Profile] = {}
            for index, raw in enumerate(raw_profiles):
                line = headers[index] if index < len(headers) else 1
                item = table(raw)
                name = string(item.get("id"))
                required = item.get("required", False)
                if not isinstance(required, bool):
                    raise ValueError(f"profile {name}: required must be boolean")
                profile = Profile(name, string(item.get("source")), strings(item.get("resources", [])),
                                  strings(item.get("dependencies", [])), required, line)
                if name in profiles:
                    self.error(path, line, f"duplicate profile: {name}")
                profiles[name] = profile
        except (OSError, RuntimeError, UnicodeError, ValueError) as exc:
            self.error(path, line, f"invalid catalog: {exc}")
            return set()

        included: set[str] = set()
        active: list[str] = []

        def visit(name: str, origin: int) -> None:
            if name not in profiles:
                self.error(path, origin, f"unknown dependency: {name}")
            elif name in active:
                self.error(path, origin, "dependency cycle: " + " -> ".join([*active, name]))
            elif name not in included:
                active.append(name)
                for dependency in profiles[name].dependencies:
                    visit(dependency, profiles[name].line)
                active.pop()
                included.add(name)

        for name in selected:
            if name not in profiles:
                self.error(path, 1, f"unknown profile: {name}")
        roots = set(selected) | {p.name for p in profiles.values() if p.required} if selected else set(profiles)
        for name in sorted(roots):
            if name in profiles:
                visit(name, profiles[name].line)
        resources = [(name, 1) for name in shared]
        for name in sorted(included):
            profile = profiles[name]
            resources.extend((resource, profile.line) for resource in (profile.source, *profile.resources))
        files = {path}
        for name in templates:
            # Catalog templates are client alternatives; selected bundles need only copied ones.
            candidate = self.bundle_root / name
            if not selected or candidate.exists() or candidate.is_symlink():
                resources.append((name, 1))
        for name, origin in resources:
            try:
                resource = self.bundle_path(name)
                if not resource.is_file():
                    self.error(path, origin, f"missing resource: {name}")
                else:
                    files.add(resource)
            except (OSError, RuntimeError, ValueError) as exc:
                self.error(path, origin, str(exc))
        return files

    def check_file(self, path: Path) -> None:
        try:
            path = self.local_path(self.root, str(path))
            if not path.is_file():
                self.error(path, 1, "missing input")
                return
            if path.suffix == ".toml":
                if path != self.bundle_root / "standards/catalog.toml":
                    tomllib.loads(path.read_text(encoding="utf-8"))
                return
            if path.suffix not in ARTIFACT_SUFFIXES:
                self.error(path, 1, "unsupported input type; select Markdown or TOML files")
                return
            document = self.document(path)
            self.diagnostics.extend(document.diagnostics)
            virtual_root = self.source_mode and path.relative_to(self.root).as_posix() in ROOT_LINK_TEMPLATES
            base = self.root if virtual_root else path.parent
            for link in document.links:
                self.check_link(path, base, link, virtual_root=virtual_root)
        except (OSError, RuntimeError, UnicodeError, ValueError) as exc:
            self.error(path, 1, str(exc))

    def check_policy(self) -> None:
        defaults = self.bundle_root / "standards/policy-defaults.toml"
        contract = self.bundle_root / "standards/policy-configuration.md"
        override = self.root / ".agents-framework/policy.toml"
        path = defaults
        try:
            defaults_present = defaults.exists() or defaults.is_symlink()
            contract_present = contract.exists() or contract.is_symlink()
            override_present = override.exists() or override.is_symlink()
            # Genuinely older bundles have neither assets nor a project override.
            if not (defaults_present or contract_present or override_present):
                return
            if not defaults_present or not contract_present:
                if override_present:
                    path = override
                elif defaults_present:
                    path = defaults
                else:
                    path = contract
                raise ValueError("partial policy setup: both standards/policy-defaults.toml and standards/policy-configuration.md are required")
            path = contract
            if not self.bundle_path("standards/policy-configuration.md").is_file():
                raise ValueError("partial policy setup: policy-configuration.md must be a file")
            path = defaults
            values = validate_policy(table(tomllib.loads(
                self.bundle_path("standards/policy-defaults.toml").read_text(encoding="utf-8"),
            )), complete=True)
            validate_growth(values)
            if override_present:
                path = override
                changes = validate_policy(table(tomllib.loads(
                    self.local_path(self.root, ".agents-framework/policy.toml").read_text(encoding="utf-8"),
                )), complete=False)
                values.update(changes)
                validate_growth(values)
        except (OSError, RuntimeError, UnicodeError, ValueError) as exc:
            self.error(path, 1, f"invalid policy: {exc}")

    def check_link(self, source: Path, base: Path, link: Link, *, virtual_root: bool = False) -> None:
        try:
            url = urlsplit(link.target)
            if url.scheme in {"http", "https", "mailto"} or link.target.startswith("//"):
                return
            if url.scheme or url.query:
                raise ValueError(f"unsupported local URL: {link.target}")
            target_path = unquote(url.path)
            if virtual_root and target_path.startswith(".agents-framework/"):
                target_path = target_path.removeprefix(".agents-framework/")
            target = self.local_path(self.root if target_path.startswith("/") else base,
                                     target_path.lstrip("/")) if target_path else source
            if not target.exists():
                self.error(source, link.line, f"missing link target: {link.target}")
            elif url.fragment:
                if target.suffix not in {".md", ".mdc"}:
                    raise ValueError(f"unsupported fragment target: {link.target}")
                if unquote(url.fragment) not in self.document(target).anchors:
                    self.error(source, link.line, f"missing fragment: {link.target}")
        except (OSError, RuntimeError, UnicodeError, ValueError) as exc:
            self.error(source, link.line, str(exc))


@dataclass
class Options(argparse.Namespace):
    root: str = str(Path(__file__).resolve().parents[1])
    bundle_dir: str = "."
    profile: list[str] = field(default_factory=list)
    paths: list[str] = field(default_factory=list)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=Options.root, help="source/target instruction root (default: this checkout)")
    parser.add_argument("--bundle-dir", default=".", help="relative bundle directory within root; non-default requires --profile")
    parser.add_argument("--profile", action="append", default=[], help="select a bundle profile; repeatable")
    parser.add_argument("paths", nargs="*", metavar="PATH", help="files relative to root; replaces default document scan")
    args = parser.parse_args(argv, namespace=Options())
    if Path(args.bundle_dir) != Path(".") and not args.profile:
        parser.error("non-default --bundle-dir requires explicit --profile selection")
    try:
        checker = Checker(Path(args.root), args.bundle_dir, source_mode=not args.profile)
    except (OSError, RuntimeError, ValueError) as exc:
        parser.error(str(exc))
    catalog_files = checker.catalog_files(args.profile)
    checker.check_policy()
    if args.paths:
        files = {checker.root / name for name in args.paths}
    elif args.profile:
        files = {p for p in catalog_files if p.suffix in ARTIFACT_SUFFIXES}
        files.update(p for p in checker.root.glob("*.md") if p.is_file())
        adoption = checker.root / ".agents-framework/adoption.md"
        if adoption.exists() or adoption.is_symlink():
            files.add(adoption)
    else:
        files = {p for p in checker.root.glob("*.md") if p.is_file()}
        for directory in ("standards", "templates"):
            files.update(p for p in (checker.root / directory).rglob("*") if p.is_file() and p.suffix in ARTIFACT_SUFFIXES)
    for path in sorted(files):
        checker.check_file(path)
    for issue in checker.diagnostics:
        location = str(issue.path.relative_to(checker.root)) if issue.path.is_relative_to(checker.root) else str(issue.path)
        print(f"{location}:{issue.line}: {issue.message}")
    print(f"Checked {len(files)} artifacts; {len(checker.diagnostics)} error(s).")
    return 1 if checker.diagnostics else 0


if __name__ == "__main__":
    raise SystemExit(main())
