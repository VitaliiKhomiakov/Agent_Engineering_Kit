# Maintaining instruction artifacts

Read when checking changes to this source library or reproducing an affected
example. Check selection and evidence reuse remain owned by
[verification policy](../../standards/verification.md). This procedure does not
add application dependencies or require running every technology's examples.

## Artifact checker

Run from the source root with Python 3.11+; only the standard library is used:

```sh
python3 tools/check_instruction_artifacts.py
python3 tools/check_instruction_artifacts.py AGENTS.md standards/core.md
python3 tools/check_instruction_artifacts.py docs/maintenance/verification.md
python3 -m unittest discover -s tests -p 'test_instruction_artifacts.py'
python3 -m unittest discover -s tests -p 'test_profile_selection.py'
python3 -m unittest discover -s tests -p 'test_project_skill_adoption.py'
python3 -m unittest discover -s tests -p 'test_project_skill_portability.py'
python3 -m unittest discover -s tests -p 'test_agent_templates.py'
python3 -m unittest discover -s tests -p 'test_model_routing.py'
git diff --check
```

The checker reads files without changing them or contacting external URLs.
Exit 0 means the selected checks passed; exit 1 reports artifact errors as
`file:line: message`; invalid command arguments exit 2. Inspect new/untracked
files separately because `git diff --check` does not include them.

| Invocation | Scope |
| --- | --- |
| No paths | Full source catalog; root `.md` files and `.md`, `.mdc`, `.toml` files under `standards/` and `templates/` |
| Explicit file paths | Full source catalog plus only those file bodies; paths resolve from `--root`, not the current directory |
| `--root DIR` | Source/target instruction root; the default is this tool's checkout |
| `--bundle-dir DIR` | Bundle directory relative to `--root`, default `.`; a non-default directory requires explicit profiles |
| Repeatable `--profile ID` | Shared assets, required and selected profiles with transitive dependencies; their documents, present catalog templates, root `.md` files and existing `.agents-framework/adoption.md` |

Historical `docs/` bodies are opt-in. A checked document's local targets must
exist, and a linked heading is inspected even when that target's body was not
selected. Outgoing links in that target are not recursively scanned. Explicit
paths replace the default body selection in either source or bundle mode;
catalog resource checks always run for the applicable closure.

Policy validation also runs regardless of body selection. Bundle
`standards/policy-defaults.toml` must be complete, and a present instruction-root
`.agents-framework/policy.toml` may contain sparse overrides. Both use the
[policy contract](../../standards/policy-configuration.md), independently of catalog
schema 1. The checker validates field types, known keys/schema, enums, positive
integer thresholds (excluding Booleans), ascending two-value ranges and the merged
growth thresholds. Defaults must be valid even when an override supplies another
value; errors identify the file and field without changing it. Semantic field
diagnostics use line 1, while syntax diagnostics include TOML parser detail.

Older catalogs without either policy asset and with no policy files/override keep
legacy artifact behavior. Declared missing assets still fail; an override or one
asset without both defaults and the contract reports partial setup. Defaults and
the contract must remain inside the selected bundle; overrides resolve from the
instruction root even for a flat/custom bundle. This is semantic file validation,
not proof of agent behavior, progress accuracy or native client loading.

The catalog check covers schema version, consumed field types, unique profile
IDs, dependency references/cycles and resource existence. It is not a schema
validator for every applicability hint. In bundle mode unselected resource paths
and dependency graphs are not required; IDs and consumed field types remain
unambiguous across the catalog. Catalog templates are client alternatives:
source mode requires all declared templates; bundle mode checks those present.
Whether the correct client entry was installed still needs adoption review.

For a prepared bundle, select its actual profiles, for example:

```sh
python3 tools/check_instruction_artifacts.py --root /tmp/prepared-bundle --profile nestjs
python3 tools/check_instruction_artifacts.py --root /tmp/nested-target --bundle-dir .agents-framework --profile angular --profile ngrx
python3 tools/check_instruction_artifacts.py --root /tmp/nested-target --bundle-dir .agents-framework --profile angular AGENTS.md .agents-framework/adoption.md
```

The tool does not detect layout or parse adoption metadata to select it. When both
layouts are present, only the explicitly selected bundle supplies the catalog and
resources. Bundle directories must exist, be relative, contain no `..` component
and resolve inside the instruction root; absolute paths and symlink escapes fail
as argument errors. Catalog resources must remain inside the bundle; document
links and explicit inputs must remain inside the project. A catalog symlink cannot
escape the bundle. This does not add an external-filesystem link mode.

Follow the [catalog contract](../../standards/catalog.md): adapt omitted optional
research and inapplicable cross-profile routes to labelled source references or
reachable source URLs. A dangling Markdown link still fails; the checker does
not silently exempt history links or remove required routes. Include non-root
installed entry files explicitly when they are outside catalog resources.

## Supported syntax and link bases

- Local inline Markdown links/images support relative paths, root-relative `/`
  paths, percent-encoded characters, fragments, angle-bracket destinations and
  optional double-quoted titles. Link labels may wrap across adjacent lines;
  destinations must stay on one line without parentheses. HTTP(S), protocol-relative
  and mailto destinations are skipped, not checked for availability or authority.
- Heading anchors use ATX headings (`#` through `######`), lowercase letters,
  spaces replaced by hyphens, punctuation stripped except underscores/hyphens,
  and numeric suffixes for duplicates. Inline code/link contents remain in the
  heading label. Simple HTML `a` anchors with a sole `id` or `name` attribute are
  supported; custom anchors do not change heading numbering.
- Backtick/tilde fences use at least three matching characters, indented by at
  most three spaces. Closing fences must use the same character and at least
  the opening length. This repository check requires a closing fence even though
  CommonMark permits an open fence through end of file. Code blocks and same-line
  inline code are excluded from link checks.
- Reference-link definitions/uses, HTML hyperlink tags, quoted fences and
  unmatched inline-link syntax produce an unsupported-syntax diagnostic. This is
  also true of content indented by four spaces or a tab inside a list: list
  containers are not parsed, so these lines must not silently count as code.
  An opening fence indented by one to three spaces while list context is active
  is also rejected before that context is reset. This conservative check does not
  resolve container-relative indentation; use a top-level fence or an outdented
  paragraph to end list context before a standalone indented fence.
  Flatten such lists before relying on this checker. Standalone indented code
  remains excluded. Quoted fences are detected before stripping inline code.
  A bounded repository checker is not a CommonMark renderer: multiline code spans,
  complex heading markup, escaped delimiters, Setext headings and other Markdown
  extensions need manual review or a tested parser extension before relying on
  their results. Bare paths in code spans are instructions, not checked links.
- Catalog paths resolve from the selected bundle root. Explicit inputs, diagnostics
  and root-relative Markdown URLs resolve from `--root`. Other Markdown links
  normally resolve from their containing directory.
- Source mode means no `--profile` and bundle `.`. Only in this mode, exactly
  `templates/policy-entry.md`, `templates/AGENTS.root.md` and `templates/PLANS.md`
  use the intended installed root as their link base and map a leading relative
  `.agents-framework/` prefix to the source bundle. Targets and fragments are still
  checked. This virtual source check never applies to root AGENTS, arbitrary
  documents, native installed files or selected target bundles. Inactive target
  copies of these templates need file-relative links; installed copies need routes
  from their final locations. No fake adopted directory is needed in the source.
- Paths escaping the project, including symlink escapes, fail; local query strings
  are unsupported. Native installed paths outside the default scan need explicit
  selection for supported Markdown/TOML checks. Code-span paths, TOML developer
  instructions and native imports need focused installation-route review; a passing
  Markdown check does not validate those mechanisms or actual client discovery.

TOML is parsed with `tomllib`. YAML, embedded program semantics, external-source
correctness, instruction consistency and actual client loading need their own
affected checks. The checker cannot establish them.

Checked against the official [Python 3.11 TOML API](https://docs.python.org/3.11/library/tomllib.html),
[CommonMark fences](https://spec.commonmark.org/0.31.2/#fenced-code-blocks) and
[GitHub section links](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links)
on 2026-10-04. The syntax subset above defines the tool's limits, not a claim of
complete renderer equivalence.

Profile-selection tests exercise the real catalog's independent/combined stacks,
excluded optional technologies and retained legacy resource paths/heading anchors.
Run their relevant scenarios when changing profile dependencies, resources or
compatibility entries. Prepared target bundles still need their own reference checks.

Project-skill adoption tests prepare a fixed FastAPI instruction fixture from the
real selected templates, check its bundle and selected native skills separately,
and reject unadapted/broken required references. They distinguish selecting the
two-template bundle from installing just one native entry. Flat/custom cases
check the design native reference only; these tests are neither a general installer
nor client behavior evidence.

Portability tests cover five representative selections across contained, flat and
custom layouts, independently opened child paths, active planning literals, a
Claude import and Codex role references. They preserve fixed local sentinels and
check write-free preparation and identical repeated candidates. These are syntax
and file-state observations, not client activation or an automated update engine.

Agent-template tests cover the three shared role bodies and Codex/Claude/Cursor
adapters, catalog closure, body/policy routes in contained/flat/custom bundles,
missing/wrong/stale routes, selected-pair fixtures, disabled/single-agent choices
and write-free repeated preparation. The Markdown adapter helper accepts only the
templates' small unquoted scalar frontmatter subset; it rejects unsupported syntax
and is neither a general YAML parser nor native schema validation. Codex uses
`tomllib`. These tests do not prove semantic instruction following, client loading,
effective permissions or actual model execution. Review role-body parity separately.
The offline model-routing checker below remains Codex-only.

When modifying the checker or tests, run their focused unittest suites and the
[strict Python analyzer](../../standards/python/typing-contracts.md#strict-static-contracts).
The checked analyzer baseline is mypy 2.1.0, installed outside the repository:

```sh
python -m mypy --strict --disallow-any-explicit --disallow-any-unimported --python-version 3.11 --explicit-package-bases --cache-dir /tmp/aek-mypy-cache tools/check_instruction_artifacts.py tools/check_model_routing.py tests/test_instruction_artifacts.py tests/test_model_routing.py tests/test_profile_selection.py tests/test_project_skill_adoption.py tests/test_project_skill_portability.py tests/test_agent_templates.py
```

## Offline model-routing agreement

The separate standard-library checker implements a bounded check of the
[model configuration contract](../../standards/model-configuration.md#routing-format-version-2).
Run it against an already prepared target instruction root:

```sh
python3 tools/check_model_routing.py --root /tmp/prepared-target
python3 tools/check_model_routing.py --root /tmp/prepared-target --default-role implementer
```

It reads `.agents-framework/model-routing.toml`, `.codex/config.toml` and
`.codex/agents/*.toml` from that root, regardless of the bundle layout. It checks
configured schema 2, explicit enabled pairs, role flags, mode/ceiling invariants,
edge endpoints, duplicate/self edges, cycles and reachable parents. Enabled roles
without an incoming edge remain unspawnable by policy; the checker does not grant
them an edge. Native checks compare the coordinator, enabled specialist overrides,
delegation switch and active concurrency ceiling. Required role metadata must be
nonempty. Disabled recorded definitions and duplicate recorded native names fail.
Role IDs supported by this filename mapping contain letters, digits, `_` or `-`.
Symlink escapes outside the instruction root fail.

Worker defaults have no implicit mapping in the framework contract. Pass
`--default-role` only when the intended default is an explicitly selected enabled
specialist. Otherwise the output states that defaults were not compared. In
single-agent mode, inactive positive native limits/defaults need not match zero.
Unrelated custom roles/settings are not acquired or removed. All role TOML must
parse and supply names for collision inspection; custom role semantics are not
validated. The command never writes files or activates templates.

Exit 0 means these selected project-local fields agree, 1 reports invalid input
or a conflict, and 2 means invalid arguments or agreement not evaluated (including
unconfigured/legacy/unknown schemas and unsupported native clients or ID mappings).
Incomplete configured records fail; no missing pair is inferred from defaults.
The source template is deliberately unconfigured and must not be activated to
make this command pass. Use disposable configured fixtures for source maintenance.

This is not a full native schema validator or effective-configuration resolver.
Global/managed/profile/environment/CLI overrides, alternate registration paths,
trust/loading, account model availability, supported efforts, nesting, permission
enforcement and runtime telemetry need separate evidence. Allowed edges remain
instruction policy. A passing result cannot certify provider execution or retire
definitions outside the inspected project directory. Claude Code and Cursor have
no semantic adapter in this tool. Native field mappings follow the dated
[Codex evidence](../research/2026-10-12-specialized-agent-instructions.md);
recheck the installed client contract when that mapping changes.

The [disposable update/recovery exercise](../research/2026-10-13-update-recovery-check.md)
records manual file outcomes under the migration procedure. It is separate from
automated fixture tests and does not establish an executable update engine.

## Reproduce an affected executable example

The example Markdown owns its source, manifests and configuration. Select just
the affected fixture; do not install these stacks in the library. Run this from
the source root, with `nest`, `react` or `fastapi` as the selector:

```sh
aek_example_dir=$(mktemp -d /tmp/aek-example-XXXXXX)
python3 - "$aek_example_dir" nest <<'PY'
from pathlib import Path
import re
import sys

documents = {
    "nest": ["standards/nestjs/examples/validated-command.md"],
    "react": ["standards/react/examples/reservation-form.md",
              "standards/react/examples/latest-result.md"],
    "fastapi": ["standards/fastapi/examples/lifetime.md"],
}
destination = Path(sys.argv[1]).resolve()
pattern = re.compile(
    r"^(?:#{2,3} )?`?((?:[\w.-]+/)*[\w.-]+\.(?:json|mjs|ts|tsx|py))`?:?"
    r"\n\n```[^\n]*\n(.*?)^```[ \t]*$", re.MULTILINE | re.DOTALL,
)
count = 0
for document in documents[sys.argv[2]]:
    for match in pattern.finditer(Path(document).read_text(encoding="utf-8")):
        target = (destination / match[1]).resolve()
        if not target.is_relative_to(destination):
            raise ValueError("fixture path escapes destination")
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("x", encoding="utf-8") as output:
            output.write(match[2])
        count += 1
if count == 0:
    raise ValueError("no named fixture blocks found")
print(f"Extracted {count} files to {destination}")
PY
```

| Fixture | Retained setup and checks | Evidence boundary |
| --- | --- | --- |
| Nest (10 files) | [Pinned manifest, TypeScript/lint configuration and commands](../../standards/nestjs/examples/validated-command.md#setup-and-checks); install and run in the extracted directory | Emitted JavaScript and in-process Fastify request injection; no real backend |
| React (9 files) | [Shared setup](../../standards/react/examples/reservation-form.md#reproduce-in-a-temporary-directory), then [latest-result commands](../../standards/react/examples/latest-result.md#reproduce) | Type/lint checks and DOM tests under jsdom; no browser or remote service |
| FastAPI (2 files) | [Lifetime fixture](../../standards/fastapi/examples/lifetime.md) plus the temporary environment below | Strict types and in-memory HTTP transport tests; no real network/backpressure |

For FastAPI, run inside the extracted directory. These pins reproduce the recorded
fixture scope, not a recommendation to upgrade a consuming project:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install fastapi==0.138.0 starlette==1.3.1 httpx==0.28.1 anyio==4.14.0 pydantic==2.13.4 mypy==2.1.0
cat > mypy.ini <<'EOF'
[mypy]
python_version = 3.11
strict = true
disallow_any_explicit = true
disallow_any_unimported = true
plugins = pydantic.mypy

[pydantic-mypy]
init_typed = true
init_forbid_extra = true
warn_required_dynamic_aliases = true
EOF
.venv/bin/python -W default -m unittest -v test_feed_http
.venv/bin/python -m mypy feed_http.py test_feed_http.py
```

Python needs working `venv`/pip support; Node fixtures need the version specified
in their manifests. Do not work around missing setup by installing into this
repository. Keep each generated lockfile/resolved package list through its check
and review; record versions, commands, results and limits in the task's evidence
owner. Manifest pins do not freeze transitive dependencies. The historical
temporary environments were removed, so a new resolution is not an exact replay
of an old lockfile. Record the known Starlette TestClient warning separately from
test failures. After recording results, remove the exact temporary fixture/tool
directories and caches created for the task, including their dependency files.

## Maintenance triggers and evidence

Revisit an affected rule for a changed API contract, changed supported target
version, broken source link or reported issue. Check the applicable official
versioned documentation; a new release alone does not trigger fixture upgrades.
Record the review date, source and applicable version separately from runtime
versions actually executed. Preserve earlier results with their original limits.

A wording/link edit usually needs scoped artifact and consistency checks. A
changed executable contract also needs its focused runtime/static checks; syntax
or type success alone does not prove behavior. Real-backend or real-client claims
require those environments. Do not turn the default artifact command into an
all-stack runtime suite or an agent-adoption certification.
