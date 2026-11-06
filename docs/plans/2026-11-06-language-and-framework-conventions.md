# Language and framework conventions

Date: 2026-11-06. Status: maintenance complete; user authorized commit and push.
Current item: none.
One authorized maintenance stage covers research, instruction additions and
their integration checks. The checked result was presented to the user, who then
requested committing and pushing it.

## Outcome and scope

Extend the completed PHP standards work to other languages already represented
in AEK. Identify official specifications, style recommendations and interoperability
contracts, add missing practical guidance, and explicitly resolve differences
between language, framework and project conventions.

The inventory covers standalone Python, Go, JavaScript and TypeScript; GDScript,
C# and C++ in the existing Godot/Unreal contexts; and SQL/PL/pgSQL under PostgreSQL.
PHP remains in scope only for composition with the shared resolution policy and
Symfony's contribution/application distinction. Existing HTML/SCSS, configuration,
tool-command and visual-script subjects do not introduce new language profiles.
No unsupported language, framework, formatter, runtime or tool upgrade is selected.

Workspace/instruction root, repository and execution checkout:
`/home/vitalii/Documents/Local_Project/AgentsFramework`. This is the canonical
combined design, plan and handoff; the coordinator owns progress and edits.
The selected method is inline under [work modes](../../standards/work-modes.md).
There is no configured workspace delegation record, so the current session retains
the work under [model configuration](../../standards/model-configuration.md).
The initial authorization covered research and instruction changes. After the
checked result was delivered, the user explicitly authorized committing and pushing
this scope on 2026-11-06. Delivery targets the existing `main` branch and `origin/main`.

The clean baseline is `d63e297adb0cfc380d1e16179ac0f4a69428b1ab`.
Original contents of 23 potentially affected tracked paths and prior absence of
six new paths are recorded in
`/tmp/aek-language-conventions-2026-11-06-_vyh0o5l/baseline.json` and `before/`.
Capture any additional affected path before editing; preserve historical evidence.

## Design and ownership

- Add convention resolution to `standards/core.md`, next to readable layout.
  Distinguish language/runtime contracts, scoped framework requirements, explicit
  project policy and fallback style advice. Contributor guides are not automatically
  application-wide rules. A style exception cannot remove a required runtime/API
  contract; use the actual target version and preserve compatibility.
- Add `conventions.md` topics for Python, JavaScript, TypeScript and PostgreSQL.
  Route from their entries and declare those four resources in the catalog.
  Reuse existing type, module, effect and verification owners rather than duplicating
  their policies. Keep framework links conditional without adding profile dependencies.
- Extend existing Go style, GDScript and Godot interop owners. Go already has
  substantive style/tooling rules; preserve its pinned examples. Godot's C# and
  native code keep their own conventions instead of inheriting GDScript/Python rules.
- Extend Unreal C++ and build topics for engine-specific conventions, including
  C# build scripts. Keep C++ Core Guidelines distinct from ISO language rules and
  engine lifetime/reflection contracts. No generic C++/C# profile is introduced.
- Put Angular, React, NestJS and Next.js differences in their existing structure,
  component or routing owners, with concise task-table routes. Preserve Angular 20,
  Godot 4.7, UE 5.8, Symfony 7.4 and PostgreSQL 16/18 reference boundaries; rolling
  documentation does not upgrade fixtures or targets.
- Link PHP to the shared resolution policy and clarify Symfony's scoped style
  source in its existing structure owner. Do not redo the accepted PHP-FIG policy.
- Extend the existing compatibility inventory in `tests/test_profile_selection.py`
  for the four new topics. Record dated source evidence and limits in
  `docs/research/2026-11-06-language-and-framework-conventions.md`.

A single universal formatting preset would contradict documented ecosystem
differences. A broad copy of each vendor's contribution rules would import
unrelated repository constraints. The selected owner-based additions preserve
usable defaults and the precise conditions of exceptions. These are routine
maintenance decisions within the user's requested scope, not a new architecture.

## Acceptance and review focus

- Every language in the stated inventory has a reachable standards/conventions
  owner; existing detailed rules are reused. Sources distinguish formal semantics,
  recommended style, scoped interoperability contracts and AEK policy.
- Project formatter choices remain usable, framework-required names/exports remain
  intact, and conflicting recommendations are resolved only in their relevant scope.
  Preserve public/wire/serialized names, toolchain limits and generated files.
- Concrete cases include Python names versus Pydantic aliases; TS compiler-repository
  conventions versus application code; React component/Hook names; Angular filenames;
  Next.js special files/default exports; conditional Nest Swagger filename matching;
  Godot versus Unreal C# indentation; engine C++ versus general advice; and PostgreSQL
  identifier folding versus the SQL standard.
- Profile bundles include their new topics while preserving independent selection,
  legacy aggregate compatibility and optional framework dependencies. Entry files route
  instead of repeating policy. Prior research, examples and external-source exclusions
  remain intact.
- Scoped artifact/catalog checks, relevant existing profile tests, whitespace,
  new-file inspection and coordinator review pass. Report unavailable source/version
  evidence without treating a live page as a tested runtime contract.

## Progress

- [x] R1 — Complete the language/framework inventory and primary-source review;
  identify existing coverage, gaps, source authority and version limits.
- [x] I1 — Add the shared resolution rule, language topics, framework-specific
  refinements and catalog/entry/test routes; retain single ownership and scope.
- [x] V1 — Check artifacts/catalog and independent bundle selection, inspect the
  diff/new files and source exclusions, and record outcomes and evidence limits.

## Verification boundary

Run `tools/check_instruction_artifacts.py` with all changed/new Markdown and TOML
paths explicitly, including this plan and the research note. Run
`python3 -m unittest discover -s tests -p 'test_profile_selection.py'` for the four
new topic resources. Run the required strict Python analyzer on the affected
profile-selection test and its imported checker under the
[maintenance gate](../maintenance/verification.md#checker-type-verification).
Inspect `git diff --check`, check new files separately and
compare changed paths with the captured baseline. Perform one coordinator review
of the selection/exception scenarios above and retain successful evidence for
unchanged inputs. Follow [proportionate verification](../../standards/verification.md).

No executable example or tool configuration is planned to change. These checks
establish instruction-artifact and bundle integrity, not formatter conformance,
runtime behavior or measured agent compliance. No separate language builds or
new test campaign are required for unchanged examples.

## Executed checks and review

Completed on 2026-11-06 against the implementation in this checkout:

| Check | Result and scope |
| --- | --- |
| `python3 tools/check_instruction_artifacts.py` with the 28 changed/new Markdown and TOML paths from the baseline inventory | 28 artifacts, 0 errors; includes full source-catalog validation, the new topics, plan and research. Log: `/tmp/aek-language-conventions-2026-11-06-_vyh0o5l/artifact-check.log`. |
| `python3 -m unittest discover -s tests -p 'test_profile_selection.py'` | 43 tests passed; covers resource inclusion, independent selection and existing aggregate compatibility. |
| `python3 -m mypy --strict --disallow-any-explicit --disallow-any-unimported --python-version 3.11 --explicit-package-bases --cache-dir /tmp/aek-mypy-language-conventions-cache tools/check_instruction_artifacts.py tests/test_profile_selection.py` | mypy 2.1.0: no issues in 2 source files. |
| `git diff --check`, plus separate `git diff --no-index --check /dev/null <path>` for each new file | No whitespace errors in tracked changes or the six new files. |
| Baseline, scope and source-exclusion comparison | Exactly 23 tracked changes and 6 new files; original copies match their hashes and baseline commit. HEAD/index unchanged. All 384 tracked/untracked nonignored paths scanned: no excluded-source references. |

Coordinator review covered the actual tracked diff and all new files against the
acceptance criteria. Convention resolution stays in core; language entries route
to four new topics, and framework details remain in their existing owners. Catalog
dependencies, strict typing, existing spacing rules, example source and pinned
versions are preserved. The only Python edit extends the existing topic inventory;
it keeps the surrounding tuple layout and adds no execution logic.

The concrete conflict cases are covered: preserve Python aliases and Go wire tags;
do not import compiler-contributor architecture into TypeScript applications;
retain React names and Next.js route exports; keep Nest suffix matching conditional
on plugin configuration; preserve Angular suffix choices, engine-specific C# layout,
Unreal reflected names, SQL identifiers and Symfony template boundaries. No
unresolved in-scope finding remains. This was an inline coordinator review; no
independent-agent review or agent-behavior benchmark is claimed.

Successful implementation/test/analyzer evidence remains valid after this final
progress-only update. Check the updated plan's links/whitespace separately; no
repeat language builds or unchanged profile-test run is needed.

## Handoff

The shared rule, four language topics, engine/framework refinements and their
entry/catalog/compatibility routes are complete. The
[research record](../research/2026-11-06-language-and-framework-conventions.md)
owns dated primary sources and retrieval limits, including the Nest source fallback,
Epic version-query access and unavailable Godot core C++ contribution page.
These limits do not imply new runtime or full standards-conformance evidence.
No executable example changed and no application/engine build was run.

The maintenance stage is complete and the user authorized its commit and push.
No Git writes were performed before that authorization. The delivery pre-edit
record, including this plan's prior contents and hashes of all 29 task files, is
`/tmp/aek-language-conventions-delivery-n06cy4ou/`. Existing implementation check
results remain applicable; only this authorization/handoff text changed afterward.
The final delivery response reports the actual commit and remote verification.
Original contents remain available at the recorded baseline location.
