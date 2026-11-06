# Readable code and PHP standards

Date: 2026-11-06. Status: implementation and verification complete.
Current item: none; R1, I1 and V1 are complete. After receiving the checked result,
the user authorized committing and pushing the completed changes.

## Task contract

Make human-readable source layout an explicit requirement for every language,
and give PHP tasks a practical selection policy for PHP-FIG standards beyond
autoloading. Keep technical detail in its canonical owner and preserve existing
project conventions, supported versions and conditional framework selection.

Workspace/instruction root, repository and execution checkout:
`/home/vitalii/Documents/Local_Project/AgentsFramework`. This document is the
canonical combined design, plan and handoff; the coordinator owns its progress.
Work is inline in the current checkout under [work modes](../../standards/work-modes.md).
The user's follow-up authorizes staging, committing and an ordinary push to
`origin/main`. No branch, worktree or forced history update is selected.
Model selection retains the existing session under
[model configuration](../../standards/model-configuration.md); no delegation is selected.

The clean tracked baseline is commit
`b69e3f6cc9d40318f758db3bb529ed32cfb76163`. Original contents of the six affected
tracked files and prior absence of the three new files were captured before edits
in `/tmp/aek-readable-php-2026-11-06-euarn8ht/baseline.json` and its `before/` directory.

## Decisions and scope

- `standards/core.md` owns shared source layout. Its task route and
  `standards/verification.md` connect the rule to ordinary implementation/review.
  Language owners retain syntax, indentation, line-length and more specific
  spacing conventions; no universal number of spaces or mandatory formatter is added.
- A new `standards/php/fig-standards.md` owns PHP-FIG selection. `standards/php.md`
  routes formatting and relevant interoperability tasks there;
  `standards/php/verification.md` routes the appropriate checks. Existing
  PSR-4 construction/autoload guidance stays in `standards/php/structure.md`.
- Prefer a versioned PER Coding Style baseline for new PHP code without an
  established convention. Preserve an existing PSR-12 or framework/project
  baseline. Interface standards are selected by an actual boundary, not installed
  as a bundle. PHP 8.2+ guidance does not authorize newer syntax or dependencies.
- Add the PHP topic to `standards/catalog.toml` and the existing PHP compatibility
  inventory in `tests/test_profile_selection.py`. No profile dependency changes.
- Record primary-source findings and evidence limits in
  [the research note](../research/2026-11-06-readable-code-and-php-standards.md).
  Retain the existing source-exclusion constraint and historical evidence.

Putting all formatting details in core would conflict with language syntax and
tools. Repeating the shared requirement in every profile would create multiple
owners. The selected split keeps a common acceptance requirement and task-specific
details. Requiring every PSR would add unrelated architecture and dependencies.
These are local maintenance choices within the user's requested scope.

## Acceptance and review focus

- Changed human-maintained code has consistent indentation and wrapping,
  separate meaningful phases, and cohesive local groups. Passing a formatter
  alone does not establish semantic readability.
- Go tabs, Python/GDScript spacing, attached annotations/doc comments, compact
  idiomatic expressions and generated artifacts are not broken by a uniform
  layout prescription. Scope remains the changed code and meaningful surroundings.
- PHP rules distinguish PSR-1, PSR-4, PER/PSR-12 and optional interface contracts.
  PER 3.1 release evidence is dated; PSR-12 is not incorrectly called deprecated.
  Deprecated and draft standards are not introduced as new mandatory baselines.
- Existing framework HTTP/container APIs remain valid. Selected PSR interfaces
  retain their semantics and installed package compatibility; the standard's
  name does not authorize a new subsystem, wrapper or package upgrade.
- PHP and legacy aggregate selection include the new topic; unrelated profiles
  remain independent. All affected links, catalog entries and whitespace pass.

## Progress

- [x] R1 — Inspect current owners and official sources; establish the gaps,
  standards status, selected release and conditional scope.
- [x] I1 — Add the shared rule, PHP topic, entry/check routes and bundle inventory;
  preserve existing owners and historical evidence.
- [x] V1 — Run scoped artifact/catalog checks and existing profile-selection tests;
  inspect the complete diff and new files, check source exclusions, and record
  the acceptance result and limits.

## Verification boundary

Run `tools/check_instruction_artifacts.py` with the eight changed/new Markdown or
TOML paths explicitly, including this plan and the research note. Run
`python3 -m unittest discover -s tests -p 'test_profile_selection.py'` because
the PHP resource inventory changes. Inspect the actual diff with
`git diff --check`, check the three new files separately, and confirm that changes
are limited to the captured paths. Perform one coordinator review against the
criteria above, including source-exclusion and rule ownership checks.

This is instruction-library maintenance. No executable PHP examples, runtime
dependencies or formatter configurations change. Runtime/formatter conformance
and agent behavior are not established by artifact or catalog checks.

## Handoff

Implementation and verification cover the nine planned paths:

- The artifact command above checked eight Markdown/TOML artifacts and the source
  catalog with zero errors.
- `python3 -m unittest discover -s tests -p 'test_profile_selection.py'` passed
  all 43 existing tests, including PHP independence and legacy aggregate selection
  with the extended topic inventory.
- `git diff --check` passed. Separate `git diff --no-index --check` inspection
  against `/dev/null` found no whitespace defects in the three new files.
- The scope check found only the six planned tracked edits and three additions;
  HEAD remained at the recorded baseline and the Git index remained empty.
  The source-exclusion scan covered 378 tracked/new files with zero matches.

The coordinator reviewed the tracked diff, new topic and evidence against the
acceptance criteria. Core owns the general requirement; language owners retain
tabs/spaces, declaration attachment and specific block-spacing decisions. Short
cohesive expressions remain allowed and generated output is outside manual layout
edits. PHP preserves PSR-4 ownership, existing style choices and native framework
contracts while making applicable interoperability semantics discoverable. The
catalog adds availability without new dependencies or a recursive reading queue.
No material in-scope finding remains.

The source documents do not constitute a tool conformance run or demonstrate
improved agent behavior. Runtime examples, package versions and formatter
configurations were not changed; the earlier evidence retains its original scope.
The final report update changes this plan only; its scoped artifact/whitespace
check does not invalidate the profile-test evidence. No further stage is proposed.
