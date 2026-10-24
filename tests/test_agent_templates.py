"""Fixed role-template contracts; not a YAML parser, installer or client eval."""

from pathlib import Path
import re
import tempfile
import tomllib
import unittest

from tests.test_project_skill_adoption import ROOT
from tests.test_project_skill_portability import portable_candidate, snapshot, write_fixture
from tools.check_instruction_artifacts import Checker


ROLES = ("architect", "implementer", "reviewer")
CLIENTS = ("codex", "claude", "cursor")


def adapter_path(client: str, role: str) -> str:
    suffix = "toml" if client == "codex" else "md"
    return f".{client}/agents/af-{role}.{suffix}"


def read_adapter(text: str, client: str) -> tuple[dict[str, object], str]:
    if client == "codex":
        values = dict[str, object](tomllib.loads(text))
        body = values.pop("developer_instructions")
        if not isinstance(body, str):
            raise ValueError("Instructions must be text")
        return values, body
    # Only the intentionally simple scalar subset used in these six templates.
    match = re.fullmatch(r"---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if match is None:
        raise ValueError("Missing frontmatter delimiters")
    values = {}
    allowed = {"name", "description", "model", "effort", "tools", "readonly"}
    for line in match[1].splitlines():
        field = re.fullmatch(r"([a-z]+): ([^\n]+)", line)
        if field is None or field[1] not in allowed or field[1] in values:
            raise ValueError("Unsupported or duplicate frontmatter field")
        key, value = field.groups()
        if key == "readonly":
            if value not in {"true", "false"}:
                raise ValueError("readonly must be Boolean")
            values[key] = value == "true"
        else:
            # No quoting, collections, comments, tags or multiline YAML here.
            if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 _.,;=/\[\]-]*", value):
                raise ValueError("Unsupported scalar syntax")
            values[key] = value
    if not {"name", "description", "model"} <= values.keys():
        raise ValueError("Missing native metadata")
    return values, match[2]


def body_route(candidate: dict[str, bytes], client: str, role: str, layout: str) -> str:
    metadata, instructions = read_adapter(candidate[adapter_path(client, role)].decode(), client)
    if metadata.get("name") != f"af-{role}":
        raise ValueError("Wrong native identity")
    routes = re.findall(r"`([^`]*templates/agents/[^`]+\.md)`", instructions)
    expected = f"{layout + '/' if layout != '.' else ''}templates/agents/{role}.md"
    if routes != [expected]:
        raise ValueError("Wrong shared role route")
    if expected not in candidate:
        raise ValueError("Missing shared role body")
    return expected


class AgentTemplateChecks(unittest.TestCase):
    def test_source_inventory_and_native_contracts(self) -> None:
        checker = Checker(ROOT)
        selected = checker.catalog_files(("model-configuration",))
        self.assertFalse(checker.diagnostics)
        for role in ROLES:
            common = ROOT / f"templates/agents/{role}.md"
            self.assertIn(common, selected)
            self.assertTrue(common.is_file())
            for client in CLIENTS:
                source = ROOT / "templates" / adapter_path(client, role).lstrip(".")
                self.assertIn(source, selected)
                metadata, instructions = read_adapter(source.read_text(), client)
                self.assertEqual(metadata["name"], f"af-{role}")
                self.assertIn(f"`.agents-framework/templates/agents/{role}.md`", instructions)
                if role != "implementer":
                    if client == "codex":
                        self.assertEqual(metadata["sandbox_mode"], "read-only")
                    elif client == "claude":
                        self.assertEqual(metadata["tools"], "Read, Grep, Glob")
                    else:
                        self.assertIs(metadata["readonly"], True)

    def test_frontmatter_rejects_unsupported_syntax(self) -> None:
        # Otherwise-complete fixtures, so each rejection comes from its named defect.
        complete = "name: af-reviewer\ndescription: Review scope\nmodel: fixture-model\n"
        self.assertEqual(read_adapter(f"---\n{complete}---\nbody", "claude")[1], "body")
        for text, message in ((complete + "body", "delimiters"),
                              (f"---\n{complete}name: two\n---\nbody", "duplicate"),
                              (f"---\n{complete}tools: [one, two]\n---\nbody", "scalar syntax"),
                              (f"---\n{complete}readonly: maybe\n---\nbody", "readonly must be Boolean")):
            with self.subTest(text=text), self.assertRaisesRegex(ValueError, message):
                read_adapter(text, "claude")

    def test_all_clients_layouts_and_independent_roots(self) -> None:
        for client in CLIENTS:
            for layout in (".agents-framework", ".", "rules/aek"):
                with self.subTest(client=client, layout=layout), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp) / "independently-opened-child"
                    candidate = portable_candidate(("fastapi",), layout, client=client)
                    write_fixture(root, candidate)
                    checker = Checker(root, bundle_dir=layout)
                    for role in ROLES:
                        route = body_route(candidate, client, role, layout)
                        checker.check_file(root / route)
                        self.assertTrue((root / route).resolve().is_relative_to(root.resolve()))
                    self.assertFalse(checker.diagnostics, checker.diagnostics)
                    native = {name for name in candidate if name.startswith(f".{client}/agents/")}
                    self.assertEqual(native, {adapter_path(client, role) for role in ROLES})
                    prefix = "" if layout == "." else layout + "/"
                    for source_client in CLIENTS:
                        self.assertFalse(any(name.startswith(f"{prefix}templates/{source_client}/agents/")
                                             for name in candidate))
                    self.assertFalse(any(name.startswith(f"{prefix}templates/skills/") for name in candidate))
                    self.assertEqual("CLAUDE.md" in candidate, client == "claude")
                    if client != "codex":
                        self.assertFalse(any(name.startswith(".agents/skills/") for name in candidate))
                    for other in set(CLIENTS) - {client}:
                        self.assertFalse(any(name.startswith(f".{other}/agents/") for name in candidate))

    def test_missing_wrong_and_stale_body_routes_are_rejected(self) -> None:
        for client in CLIENTS:
            original = portable_candidate(("fastapi",), "rules/aek", client=client)
            route = body_route(original, client, "architect", "rules/aek")
            native = adapter_path(client, "architect")
            for failure in ("missing", "wrong-role", "stale-prefix"):
                with self.subTest(client=client, failure=failure):
                    candidate = original.copy()
                    if failure == "missing":
                        del candidate[route]
                    elif failure == "wrong-role":
                        candidate[native] = candidate[native].replace(b"agents/architect.md", b"agents/reviewer.md")
                    else:
                        candidate[native] = candidate[native].replace(b"rules/aek/", b".agents-framework/")
                    with self.assertRaisesRegex(ValueError, "shared role"):
                        body_route(candidate, client, "architect", "rules/aek")

    def test_selected_pairs_disabled_roles_and_write_free_preparation(self) -> None:
        # Deliberately different from example values; not model availability evidence.
        pairs = {"implementer": ("fixture-model", "medium")}
        for client in CLIENTS:
            for roles in ((), ("implementer",)):
                with self.subTest(client=client, roles=roles), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp) / "target"
                    before = snapshot(Path(tmp))
                    candidate = portable_candidate(("fastapi",), ".agents-framework",
                                                   client=client, roles=roles, pairs=pairs)
                    self.assertEqual(snapshot(Path(tmp)), before)
                    native = {name for name in candidate if name.startswith(f".{client}/agents/")}
                    self.assertEqual(native, {adapter_path(client, role) for role in roles})
                    for role in roles:
                        metadata, _ = read_adapter(candidate[adapter_path(client, role)].decode(), client)
                        expected = "fixture-model[effort=medium]" if client == "cursor" else "fixture-model"
                        self.assertEqual(metadata["model"], expected)
                        if client != "cursor":
                            key = "model_reasoning_effort" if client == "codex" else "effort"
                            self.assertEqual(metadata[key], "medium")
                    sentinel = {f".{client}/agents/custom-local.md": b"local instructions\n",
                                "LOCAL_SETTINGS.txt": b"preserve local model and comments\n"}
                    self.assertTrue(set(candidate).isdisjoint(sentinel))
                    write_fixture(root, {**candidate, **sentinel})
                    before = snapshot(root)
                    repeated = portable_candidate(("fastapi",), ".agents-framework",
                                                  client=client, roles=roles, pairs=pairs)
                    self.assertEqual(candidate, repeated)
                    self.assertEqual(snapshot(root), before)

    def test_body_update_keeps_one_source_for_all_adapters(self) -> None:
        candidate = portable_candidate(("fastapi",), ".agents-framework")
        for client in ("claude", "cursor"):
            other = portable_candidate(("fastapi",), ".agents-framework", client=client)
            for role in ROLES:
                candidate[adapter_path(client, role)] = other[adapter_path(client, role)]
        for role in ROLES:
            routes = {body_route(candidate, client, role, ".agents-framework") for client in CLIENTS}
            self.assertEqual(len(routes), 1)
            route = routes.pop()
            candidate[route] += b"\nFixture revision marker.\n"
            for client in CLIENTS:
                self.assertEqual(body_route(candidate, client, role, ".agents-framework"), route)
                self.assertNotIn(b"Fixture revision marker", candidate[adapter_path(client, role)])


if __name__ == "__main__":
    unittest.main()
