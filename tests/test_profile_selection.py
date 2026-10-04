"""Protect independent stack selection and existing aggregate entry contracts."""

from pathlib import Path
import unittest

from tools.check_instruction_artifacts import Checker, markdown


ROOT = Path(__file__).resolve().parents[1]
# Existing public topic paths are a compatibility fixture, independent of catalog edges.
TOPICS: dict[str, tuple[str, ...]] = {
    "postgresql": ("schema-contracts", "transactions-concurrency", "queries-performance",
                   "migrations-verification", "security-operations", "examples/atomic-reservation",
                   "examples/online-constraint"),
    "docker": ("build-context", "runtime-lifetime", "compose-integration", "development-production",
               "verification-compatibility", "examples/build-secret", "examples/compose-contract",
               "examples/development-production"),
    "unreal-engine": ("cpp-lifetime", "gameplay-blueprints", "build-assets", "mcp-editor",
                      "verification", "runtime-performance", "skills"),
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
    "go": ("architecture", "contracts", "concurrency", "resources", "verification",
           "examples/domain", "examples/dependencies", "examples/concurrency"),
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

    def test_unchanged_controls_do_not_select_application_stacks(self) -> None:
        controls = {"postgresql", "docker", "unreal-engine"}
        for profile in controls:
            with self.subTest(profile=profile):
                self.assert_topics(self.selected(profile), {profile},
                                   (controls - {profile}) | {"php", "symfony", "doctrine", "python",
                                    "pydantic", "fastapi", "go", "gin", "javascript", "nodejs", "typescript",
                                    "react", "nextjs", "nestjs", "angular", "ngrx", "typeorm"})

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
