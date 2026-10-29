"""Protect independent stack selection and existing aggregate entry contracts."""

from pathlib import Path
import unittest

from tools.check_instruction_artifacts import Checker, markdown


ROOT = Path(__file__).resolve().parents[1]
SHARED_EDITOR_MCP = "standards/editor-mcp.md"
# Existing public topic paths are a compatibility fixture, independent of catalog edges.
TOPICS: dict[str, tuple[str, ...]] = {
    "eino": ("composition", "tools-retrieval", "runtime-recovery", "examples/tool-graph"),
    "llamaindex": ("ingestion-retrieval", "tools-synthesis", "examples/retrieval"),
    "langchain": ("models-tools", "go", "examples/validated-tool", "examples/go-tool"),
    "langgraph": ("state-execution", "recovery-streaming", "examples/resume"),
    "langfuse": ("instrumentation", "privacy-evaluation", "examples/otel-go"),
    "postgresql": ("schema-contracts", "transactions-concurrency", "queries-performance",
                   "migrations-verification", "security-operations", "examples/atomic-reservation",
                   "examples/online-constraint"),
    "docker": ("build-context", "runtime-lifetime", "compose-integration", "development-production",
               "verification-compatibility", "examples/build-secret", "examples/compose-contract",
               "examples/development-production"),
    "unreal-engine": ("cpp-lifetime", "gameplay-blueprints", "build-assets", "mcp-editor",
                      "verification", "runtime-performance", "skills"),
    "godot": ("architecture", "gdscript", "lifecycle-runtime", "assets-export",
              "ui-performance", "interop", "tooling-mcp", "verification"),
    "react": ("components-boundaries", "state-identity", "effects-integrations", "forms-contracts",
              "verification-compatibility", "examples/reservation-form", "examples/latest-result"),
    "nextjs": ("routing-composition", "server-client-security", "data-cache-mutations",
               "rendering-runtime", "verification-migration", "examples/authorized-command", "examples/tagged-read"),
    "javascript": ("modules-structure", "values-state", "async-effects", "verification-compatibility",
                   "examples/input-state", "examples/async-ownership"),
    "nodejs": ("runtime-composition", "io-concurrency", "http-integrations", "lifecycle-verification",
               "examples/bounded-stream", "examples/graceful-server"),
    "typescript": ("contracts-structure", "validation-state", "composition-effects", "toolchain-verification",
                   "examples/validated-command", "examples/typed-operation"),
    "nestjs": ("modules-providers", "transport-contracts", "application-lifecycle", "verification-operations",
               "examples/validated-command", "examples/provider-lifecycle"),
    "typeorm": ("models-mapping", "transactions-lifetime", "queries-relations", "schema-verification",
                "nestjs-integration", "examples/rich-booking"),
    "angular": ("architecture", "reactivity", "change-detection", "boundaries", "styles", "verification"),
    "ngrx": ("state-architecture", "store-selectors", "effects", "entity-router", "signal-store", "verification",
             "examples/store-view-model", "examples/signal-store-request"),
    "php": ("structure", "types-contracts", "state-effects", "verification",
            "examples/input-domain", "examples/resources"),
    "symfony": ("structure-services", "http-validation", "runtime-effects", "verification",
                "examples/request-boundary", "examples/http-client"),
    "doctrine": ("models-mapping", "unit-of-work-transactions", "queries-dbal", "schema-verification",
                 "examples/orm-unit-of-work", "examples/dbal-reservation"),
    "go": ("architecture", "contracts", "concurrency", "resources", "verification", "style",
           "examples/domain", "examples/dependencies", "examples/concurrency", "examples/style-tooling"),
    "gin": ("handlers-binding", "routing-middleware", "runtime", "verification",
            "examples/binding", "examples/middleware"),
    "python": ("structure", "typing-contracts", "execution-resources", "verification",
               "examples/domain", "examples/concurrency"),
    "pydantic": ("validation", "serialization", "lifecycle", "verification",
                 "examples/boundary", "examples/patches"),
    "fastapi": ("transport", "dependencies-lifetime", "runtime-operations", "verification",
                "examples/http-boundary", "examples/lifetime"),
    "sqlalchemy": ("mapping-contracts", "sessions-transactions", "queries-loading",
                   "async-engines", "migrations-verification",
                   "examples/transactional-command", "examples/async-projection"),
    "psycopg": ("queries-contracts", "transactions-lifetime", "async-pooling",
                "compatibility-verification", "examples/typed-query", "examples/owned-transaction"),
}


class ProfileSelectionChecks(unittest.TestCase):
    def selected(self, *profiles: str) -> set[str]:
        checker = Checker(ROOT)
        paths = checker.catalog_files(profiles)
        self.assertEqual(checker.diagnostics, [])
        return {path.relative_to(ROOT).as_posix() for path in paths}

    def assert_topics(self, paths: set[str], included: set[str], excluded: set[str]) -> None:
        for family in included:
            with self.subTest(included=family):
                self.assertIn(f"standards/{family}.md", paths)
                for topic in TOPICS[family]:
                    self.assertIn(f"standards/{family}/{topic}.md", paths)
        for family in excluded:
            with self.subTest(excluded=family):
                self.assertNotIn(f"standards/{family}.md", paths)
                self.assertFalse(any(path.startswith(f"standards/{family}/") for path in paths))

    def test_php_does_not_select_framework_or_orm(self) -> None:
        paths = self.selected("php")
        self.assert_topics(paths, {"php"}, {"symfony", "doctrine", "go", "gin"})
        self.assertNotIn("standards/php-symfony-doctrine.md", paths)

    def test_ai_profiles_are_optional_and_do_not_choose_a_language_or_store(self) -> None:
        profiles = {"rag", "llm-tools", "llamaindex", "langchain", "langgraph", "langfuse"}
        base = self.selected("core")
        for profile in profiles:
            with self.subTest(profile=profile):
                self.assertNotIn(f"standards/{profile}.md", base)
                paths = self.selected(profile)
                self.assertIn(f"standards/{profile}.md", paths)
                self.assert_topics(paths, set(), {"python", "go", "javascript", "typescript",
                                                 "nodejs", "fastapi", "gin", "postgresql", "docker"})
                self.assertFalse(any(path.startswith("docs/") for path in paths))

    def test_tools_graphs_and_tracing_do_not_require_retrieval_or_sibling_vendors(self) -> None:
        for profile in ("llm-tools", "langchain", "langgraph", "langfuse"):
            with self.subTest(profile=profile):
                paths = self.selected(profile)
                for unselected in {"rag", "llamaindex", "langchain", "langgraph", "langfuse"} - {profile}:
                    self.assertNotIn(f"standards/{unselected}.md", paths)
                self.assertNotIn("standards/rag/ingestion.md", paths)
                self.assertIn("standards/llm/evaluation.md", paths)
                if profile == "langfuse":
                    self.assertNotIn("standards/llm-tools.md", paths)
                    self.assertNotIn("standards/llm-tools/execution.md", paths)
                else:
                    self.assertIn("standards/llm-tools/contracts.md", paths)
                    self.assertIn("standards/llm-tools/execution.md", paths)

    def test_ai_guidance_composes_with_the_selected_application_language(self) -> None:
        for language in ("go", "python", "nodejs"):
            with self.subTest(language=language):
                paths = self.selected(language, "rag", "llm-tools")
                self.assertEqual(paths, self.selected(language) | self.selected("rag") |
                                 self.selected("llm-tools"))
                self.assertIn("standards/rag/retrieval.md", paths)
                self.assertIn("standards/llm-tools/workflows.md", paths)
                self.assertIn("standards/llm/answers.md", paths)
                for other in {"go", "python", "nodejs"} - {language}:
                    self.assertNotIn(f"standards/{other}.md", paths)

    def test_eino_selects_go_and_tools_without_retrieval_or_other_vendors(self) -> None:
        paths = self.selected("eino")
        self.assertNotIn("standards/eino.md", self.selected("core"))
        self.assert_topics(paths, {"eino", "go"},
                           {"llamaindex", "langchain", "langgraph", "langfuse", "python", "nodejs"})
        self.assertIn("standards/llm-tools/contracts.md", paths)
        self.assertIn("standards/llm-tools/execution.md", paths)
        self.assertNotIn("standards/rag.md", paths)
        self.assertNotIn("standards/rag/retrieval.md", paths)
        self.assertEqual(self.selected("eino", "rag"), paths | self.selected("rag"))
        self.assertFalse(any(path.startswith("docs/") for path in paths))

    def test_vendor_details_and_examples_stay_in_their_selected_profile(self) -> None:
        profiles = {"eino", "llamaindex", "langchain", "langgraph", "langfuse"}
        for profile in profiles:
            with self.subTest(profile=profile):
                self.assert_topics(self.selected(profile), {profile}, profiles - {profile})
        for profile in ("rag", "llm-tools"):
            self.assert_topics(self.selected(profile), set(), profiles)

    def test_project_workflows_add_only_task_resources(self) -> None:
        expected = {"standards/project-skills.md",
                    "templates/skills/aek-design-feature/SKILL.md",
                    "templates/skills/aek-review-changes/SKILL.md"}
        self.assertEqual(self.selected("project-workflows") - self.selected("core"), expected)

    def test_bundle_keeps_role_bodies_without_preparation_templates(self) -> None:
        checker = Checker(ROOT)
        selection = checker.catalog_selection(("core",))
        self.assertFalse(checker.diagnostics, checker.diagnostics)
        bundle = {path.relative_to(ROOT).as_posix() for path in selection.bundle_files}
        source = {path.relative_to(ROOT).as_posix() for path in selection.source_files}
        for role in ("architect", "implementer", "reviewer"):
            self.assertIn(f"templates/agents/{role}.md", bundle)
            for client, suffix in (("codex", "toml"), ("claude", "md"), ("cursor", "md")):
                path = f"templates/{client}/agents/af-{role}.{suffix}"
                self.assertIn(path, source)
                self.assertNotIn(path, bundle)
        for path in ("templates/codex/config.toml", "templates/codex/README.md",
                     "templates/framework/model-routing.toml", "templates/policy-entry.md",
                     "templates/claude/policy-bridge.md", "templates/cursor/rule-route.mdc",
                     "templates/skills/aek-model-setup/SKILL.md",
                     "templates/skills/aek-model-reassign/SKILL.md"):
            self.assertIn(path, source)
            self.assertNotIn(path, bundle)
        self.assertTrue(bundle.isdisjoint(source))

    def test_workflow_copy_selection_adds_guide_without_skill_duplicates(self) -> None:
        checker = Checker(ROOT)
        base = checker.catalog_selection(("core",))
        workflow = checker.catalog_selection(("project-workflows",))
        self.assertFalse(checker.diagnostics, checker.diagnostics)
        self.assertEqual(workflow.bundle_files - base.bundle_files,
                         {ROOT / "standards/project-skills.md"})
        self.assertEqual(workflow.source_files - base.source_files,
                         {ROOT / "templates/skills/aek-design-feature/SKILL.md",
                          ROOT / "templates/skills/aek-review-changes/SKILL.md"})

    def test_project_workflows_preserve_selected_stack_closures(self) -> None:
        additions = {"standards/project-skills.md",
                     "templates/skills/aek-design-feature/SKILL.md",
                     "templates/skills/aek-review-changes/SKILL.md"}
        for selection in (("fastapi",), ("react", "typescript"), ("angular",),
                          ("ngrx",), ("go",), ("unreal-engine",), ("godot",)):
            with self.subTest(selection=selection):
                original = self.selected(*selection)
                self.assertTrue(original.isdisjoint(additions))
                self.assertEqual(self.selected(*selection, "project-workflows"),
                                 original | additions)

    def test_unchanged_controls_do_not_select_application_stacks(self) -> None:
        controls = {"postgresql", "docker", "unreal-engine", "godot"}
        for profile in controls:
            with self.subTest(profile=profile):
                self.assert_topics(self.selected(profile), {profile},
                                   (controls - {profile}) | {"php", "symfony", "doctrine", "python",
                                    "pydantic", "fastapi", "go", "gin", "javascript", "nodejs", "typescript",
                                    "react", "nextjs", "nestjs", "angular", "ngrx", "typeorm"})

    def test_godot_adds_only_its_engine_resources_to_core(self) -> None:
        expected = {"standards/godot.md", SHARED_EDITOR_MCP}
        expected.update(f"standards/godot/{topic}.md" for topic in TOPICS["godot"])
        self.assertEqual(self.selected("godot") - self.selected("core"), expected)

    def test_engines_share_one_editor_mcp_owner(self) -> None:
        # Available to each engine alone, without core selecting it.
        for engine in ("godot", "unreal-engine"):
            with self.subTest(engine=engine):
                self.assertIn(SHARED_EDITOR_MCP, self.selected(engine))
        self.assertNotIn(SHARED_EDITOR_MCP, self.selected("core"))

    def test_engine_profiles_compose_only_when_selected(self) -> None:
        self.assertEqual(self.selected("godot", "unreal-engine"),
                         self.selected("godot") | self.selected("unreal-engine"))

    def test_symfony_includes_php_without_selecting_doctrine(self) -> None:
        self.assert_topics(self.selected("symfony"), {"php", "symfony"}, {"doctrine"})

    def test_doctrine_includes_php_without_selecting_symfony(self) -> None:
        self.assert_topics(self.selected("doctrine"), {"php", "doctrine"}, {"symfony"})

    def test_php_stack_composes_without_selecting_legacy_aggregate(self) -> None:
        paths = self.selected("php", "symfony", "doctrine")
        self.assert_topics(paths, {"php", "symfony", "doctrine"}, {"go", "gin"})
        self.assertNotIn("standards/php-symfony-doctrine.md", paths)

    def test_go_does_not_select_gin(self) -> None:
        paths = self.selected("go")
        self.assert_topics(paths, {"go"}, {"gin", "php"})
        self.assertNotIn("standards/go-gin.md", paths)

    def test_gin_includes_go(self) -> None:
        self.assert_topics(self.selected("gin"), {"go", "gin"}, {"php"})

    def test_python_does_not_select_validation_web_or_persistence(self) -> None:
        paths = self.selected("python")
        self.assert_topics(paths, {"python"}, {"pydantic", "fastapi", "sqlalchemy", "psycopg"})
        self.assertNotIn("standards/python-fastapi.md", paths)

    def test_pydantic_includes_python_without_web_or_persistence(self) -> None:
        self.assert_topics(self.selected("pydantic"), {"python", "pydantic"},
                           {"fastapi", "sqlalchemy", "psycopg"})

    def test_fastapi_includes_python_and_pydantic_without_persistence(self) -> None:
        paths = self.selected("fastapi")
        self.assert_topics(paths, {"python", "pydantic", "fastapi"}, {"sqlalchemy", "psycopg"})
        self.assertNotIn("standards/python-fastapi.md", paths)

    def test_sqlalchemy_does_not_select_web_validation_or_postgresql(self) -> None:
        paths = self.selected("sqlalchemy")
        self.assert_topics(paths, {"python", "sqlalchemy"}, {"fastapi", "pydantic", "psycopg", "postgresql"})
        self.assertNotIn("standards/python-fastapi.md", paths)

    def test_psycopg_retains_postgresql_without_web_or_validation(self) -> None:
        paths = self.selected("psycopg")
        self.assert_topics(paths, {"python", "psycopg"}, {"fastapi", "pydantic", "sqlalchemy"})
        self.assertIn("standards/postgresql.md", paths)
        self.assertNotIn("standards/python-fastapi.md", paths)

    def test_browser_javascript_does_not_select_host_or_typed_frameworks(self) -> None:
        self.assert_topics(self.selected("javascript"), {"javascript"},
                           {"nodejs", "typescript", "nestjs", "angular", "nextjs"})

    def test_browser_typescript_does_not_select_node_or_frameworks(self) -> None:
        paths = self.selected("typescript")
        self.assert_topics(paths, {"javascript", "typescript"}, {"nodejs", "nestjs", "angular", "nextjs"})
        self.assertNotIn("standards/nodejs-typescript.md", paths)

    def test_node_javascript_does_not_select_typescript(self) -> None:
        self.assert_topics(self.selected("nodejs"), {"javascript", "nodejs"}, {"typescript", "nestjs"})

    def test_node_typescript_composes_without_frameworks(self) -> None:
        self.assert_topics(self.selected("nodejs", "typescript"), {"javascript", "nodejs", "typescript"},
                           {"nestjs", "angular", "nextjs"})

    def test_angular_does_not_select_node_or_ngrx(self) -> None:
        self.assert_topics(self.selected("angular"), {"javascript", "typescript", "angular"},
                           {"nodejs", "ngrx", "nestjs", "nextjs"})

    def test_ngrx_retains_angular_without_selecting_node(self) -> None:
        self.assert_topics(self.selected("ngrx"), {"javascript", "typescript", "angular", "ngrx"}, {"nodejs"})

    def test_nest_includes_node_and_typescript_without_typeorm(self) -> None:
        self.assert_topics(self.selected("nestjs"), {"javascript", "nodejs", "typescript", "nestjs"},
                           {"typeorm", "angular"})

    def test_typeorm_does_not_select_node_or_nest(self) -> None:
        self.assert_topics(self.selected("typeorm"), {"javascript", "typescript", "typeorm"}, {"nodejs", "nestjs"})

    def test_typeorm_can_select_node_host_separately(self) -> None:
        self.assert_topics(self.selected("typeorm", "nodejs"), {"javascript", "typescript", "typeorm", "nodejs"},
                           {"nestjs"})

    def test_angular_and_nest_share_typescript_resources(self) -> None:
        combined = self.selected("angular", "nestjs")
        self.assert_topics(combined, {"javascript", "typescript", "nodejs", "angular", "nestjs"}, {"ngrx", "typeorm"})
        self.assertEqual(combined, self.selected("angular") | self.selected("nestjs"))

    def test_legacy_next_keeps_node_resources_and_compatibility_entry(self) -> None:
        paths = self.selected("nextjs")
        self.assert_topics(paths, {"javascript", "nodejs", "typescript", "react", "nextjs"}, set())
        self.assertIn("standards/nextjs-framework.md", paths)
        self.assertIn("standards/nextjs-feature-structure.md", paths)
        self.assertIn("standards/nodejs-typescript.md", paths)

    def assert_next_framework(self, paths: set[str]) -> None:
        self.assert_topics(paths, {"javascript", "react"}, set())
        self.assertIn("standards/nextjs-framework.md", paths)
        self.assertIn("standards/nextjs-feature-structure.md", paths)
        for topic in TOPICS["nextjs"]:
            self.assertIn(f"standards/nextjs/{topic}.md", paths)
        self.assertNotIn("standards/nextjs.md", paths)
        self.assertNotIn("standards/nodejs-typescript.md", paths)

    def test_react_javascript_excludes_next_typescript_and_node(self) -> None:
        self.assert_topics(self.selected("react"), {"react", "javascript"},
                           {"nextjs", "nextjs-framework", "typescript", "nodejs"})

    def test_react_typescript_excludes_next_and_node(self) -> None:
        self.assert_topics(self.selected("react", "typescript"), {"react", "javascript", "typescript"},
                           {"nextjs", "nextjs-framework", "nodejs"})

    def test_next_javascript_does_not_select_typescript_or_node(self) -> None:
        paths = self.selected("nextjs-framework")
        self.assert_next_framework(paths)
        self.assert_topics(paths, set(), {"typescript", "nodejs"})

    def test_next_typescript_does_not_select_node(self) -> None:
        paths = self.selected("nextjs-framework", "typescript")
        self.assert_next_framework(paths)
        self.assert_topics(paths, {"typescript"}, {"nodejs"})

    def test_next_node_host_can_be_selected_without_typescript(self) -> None:
        paths = self.selected("nextjs-framework", "nodejs")
        self.assert_next_framework(paths)
        self.assert_topics(paths, {"nodejs"}, {"typescript"})

    def test_feature_structure_uses_narrow_next_profile(self) -> None:
        paths = self.selected("nextjs-feature-structure")
        self.assert_next_framework(paths)
        self.assert_topics(paths, set(), {"typescript", "nodejs"})

    def test_legacy_aggregates_retain_all_family_resources(self) -> None:
        for profile, families in (("php-symfony-doctrine", {"php", "symfony", "doctrine"}),
                                  ("go-gin", {"go", "gin"}),
                                  ("python-fastapi", {"python", "pydantic", "fastapi"}),
                                  ("nodejs-typescript", {"javascript", "nodejs"})):
            with self.subTest(profile=profile):
                paths = self.selected(profile)
                self.assertIn(f"standards/{profile}.md", paths)
                self.assert_topics(paths, families, set())

    def test_legacy_bookmarks_remain_resolvable(self) -> None:
        # Public headings captured before separation, not derived from the new entries.
        expected = {
            "php-symfony-doctrine": {
                "php--symfony--doctrine", "php-essentials", "read-by-task",
                "symfony-essentials", "doctrine-essentials",
                "framework-integration-during-file-moves", "basis",
            },
            "go-gin": {"go--gin", "essential-guidance", "read-by-task", "gin-essentials", "evidence"},
            "python-fastapi": {"python--fastapi", "essential-guidance", "read-by-task",
                               "pydantic-essentials", "fastapi-essentials", "evidence"},
            "nodejs-typescript": {"nodejs--javascript--typescript", "versions-and-modules", "read-by-task",
                                  "typed-boundaries", "server-execution-and-responsibility", "verification", "basis"},
            "nextjs": {"nextjs--react", "essential-react-rules", "read-by-task",
                       "nextjs-only-versions-and-task-routes", "basis"},
        }
        for profile, anchors in expected.items():
            with self.subTest(profile=profile):
                path = ROOT / "standards" / f"{profile}.md"
                self.assertLessEqual(anchors, markdown(path, path.read_text(encoding="utf-8")).anchors)


if __name__ == "__main__":
    unittest.main()
