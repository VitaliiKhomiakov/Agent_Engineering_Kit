# Project task-skill behavior observations — 2026-10-11

PS-05/PS-06 of the [canonical plan](../plans/2026-10-11-project-skills-reorganization.md)
observe current task entries after PS-04. Results below concern disposable projects,
not deployment in a real consumer. Earlier PS-02 runs retain their recorded inputs;
the changed shared guide and three-entry packaging require current observations.

## Inputs and controlled comparison

Source baseline: `/tmp/aek-ps05-ps63deta/baseline.json`, 278 original file identities
and scoped originals. Durable product inputs and the deterministic builder are in
[behavior fixtures](../../tests/fixtures/project-skills-behavior/README.md), reusing
[the design inputs](../../tests/fixtures/project-skills/ARCHITECTURE.md).
The acceptance oracle is [acceptance.py](../../tests/fixtures/project-skills-behavior/acceptance.py).

Each of design, implementation and review has a fresh control and candidate with
identical product files, canonical task, prompt, model/effort and available
Superpowers. Control omits project-workflows. Candidate adds its guide, inactive
resources and three native skills. Manifest comparison found only three differing
shared files: active AGENTS and optional guide links in the bundled catalog entry
and inactive policy-entry template. All other common contents are byte-identical.
This compares direct rules with task-entry packaging, not an old technology version.
A fourth matched pair checks the small fix with and without project-workflows;
its product inputs and prompt are likewise identical. It was added to distinguish
the present-profile small-fix trigger from the separate missing-profile fallback.

Client: installed Codex CLI 0.162.1. Saved model/effort: gpt-6-astra/high, copied
unchanged into each private runtime; no CLI model override. Superpowers 6.4.2 is
available through an identical explicit AGENTS route to its installed read-only
plugin path for the matched pairs. Native plugin discovery is not asserted. The
separate unavailable-plugin case masks that package path; it is not a matched
performance comparison. No global client/model/plugin settings are changed.

Python 3.12.3 executes standard-library domain tests. mypy 2.1.0 is placed in a
private temporary tools directory via a disposable Python 3.12 container because
host Python has no pip. That directory is mounted read-only in each observation
and supplied through PYTHONPATH. No system/project dependency installation occurs.
The actual FastAPI transport is untouched; these runs do not claim HTTP runtime
acceptance. Domain implementation has a separately accepted bounded design.

## Recorded source identities

| Input | SHA-256 |
| --- | --- |
| `standards/project-skills.md` | `3d8aae1649c829bc1cf92fa10723fc9300fd0dbeb746e763fbb8b4cbb71a1f36` |
| `standards/superpowers.md` | `914705f0bd47d0b5b1fdf08c0dd8fbea6fa03cbef85dd65cc0532d48e040f22e` |
| `templates/skills/aek-design-feature/SKILL.md` | `44d7ab1bd85aef5b357e6c85d15efff0c860f3fdb850a45b7b5d22154c3c4c85` |
| `templates/skills/aek-implement-feature/SKILL.md` | `baaeaf1fe4b04dce113ad746d3bd21bb82ffcd4f79053cf1668c7519142136aa` |
| `templates/skills/aek-review-changes/SKILL.md` | `553c583fff0dbc5f820de0ad044fd83f6558b1f3953795f766ad7b170ce69d60` |
| `tests/fixtures/project-skills-behavior/prepare.py` | `67db15cc66694ed64cfa4637f2617ebb579d8db0f3a31dce680c3c73c2478b6a` |
| `tests/fixtures/project-skills-behavior/acceptance.py` | `a60b77503ad0cc56b4ebf41f6dc0ef8443aa1ec14611d760afd3650f1bbf12ae` |

## Invocation and isolation

Each call uses the installed executable with:

```sh
codex exec --ephemeral --skip-git-repo-check --sandbox workspace-write --json -C /tmp/aek-observation -
```

The prompt is stdin; each fresh process has a 600-second bound. The reused PS-02
bubblewrap boundary starts with `--ro-bind / / --proc /proc --dev /dev`; it binds
a private client runtime at the normal runtime path, keeps installed packages,
plugins, skills and rules read-only, masks the source checkout and host `/tmp`,
and binds only the selected fixture at `/tmp/aek-observation`. A read-only
`/tmp/check-tools` supplies the analyzer. Native workspace-write sandbox and
approval checks remain enabled. PYTHONDONTWRITEBYTECODE prevents incidental caches.
For the Superpowers-absent case its installed package directory is additionally
masked before client startup. Model access uses the existing authenticated client;
credentials and full configuration are not research artifacts.

Local manifests retain pre-run file hashes. Compare actual changed/added/deleted
files after each run. Inspect emitted commands for skill/topic reads, excess work,
Git/setup/delegation and source-path access; a completed turn alone is not task
acceptance. Client JSON telemetry, where present, is reported as such; unknown
internal reads, hidden reasoning or monetary costs are not inferred.

## Prompts and expected outcomes

Every prompt ends: “Work inline. Do not delegate, install tools, change configuration
or perform Git writes. Preserve unrelated files. Report actual rules used, checks
and limits.” The operation-specific text below is identical within each pair.

- Design: “Complete CANCEL-DESIGN in docs/plans/cancel.md using applicable project
  instructions. This authorizes the design document only, not application
  implementation. Keep the existing task as the only design/progress record.”
- Implementation: “Implement the accepted CANCEL-IMPLEMENT design in
  docs/plans/cancel.md using applicable project instructions. Complete its domain
  acceptance and report the result; HTTP integration remains outside scope.”
- Review: “Review the changes from baseline/domain.py to app/domain.py against
  docs/plans/cancel.md and applicable project instructions. This is review-only:
  do not change project files. Report located consequential findings and evidence
  in your response.”
- Unrelated candidate: “Correct servce to service in README.md only. Preserve every
  other file.”
- Small fix, with and without optional profile: “Fix Inventory.reserve so True and False are
  rejected with ValueError('invalid_quantity') without changing stock, as specified
  in docs/plans/cancel.md. Preserve valid positive integer behavior. This is a
  settled small fix, not a new feature design.”
- Explicit review without Superpowers: “Use $aek-review-changes to review the changes
  from baseline/domain.py to app/domain.py against docs/plans/cancel.md. Superpowers
  is unavailable in this observation: use the existing direct-reference fallback.
  This is review-only: do not change project files. Report located consequential
  findings and evidence in your response.”

Design acceptance requires actual owners, atomic/idempotent cancellation, immutable
identity, missing-ID compatibility, technical rule-to-decision mapping, alternatives
and proposed checks in the existing task only. Implementation requires the agreed
domain operation, three executed acceptance tests, strict typing and unchanged HTTP.
The review seed returns stock repeatedly; expected findings locate that defect,
while accepting E1 (intentional in-memory storage/one lock). Neither review case
may fix files. A small fix must reject bool without expanding into cancellation,
design or setup. The unrelated case may change only the exact README typo.

Initial oracle checks ran before client execution: implementation seed produced
three missing-method errors; review seed produced two failures (repeated/concurrent
stock return) with the missing-ID case passing. These expected failures establish
that the checks distinguish the intended behavior and seeded defect.

## Initial discovery limitation

A model-free `skills/list` probe discovered all three AEK entries as enabled repo
skills and returned no protocol error, but no Superpowers entries. Files were
present at the installed source path; availability alone did not make them part of
the native skill catalog. The initial control completed a design without observed
installed Superpowers reads; its candidate was interrupted after selecting the AEK
design skill. Those outputs remain partial evidence in `initial-unrouted/`, not the
matched Superpowers-present comparison. The runner and its active child were stopped.

The fixture now gives both sides the same explicit route to the one installed
Superpowers 6.4.2 source, requiring local adaptations first and honest fallback if
unavailable. No plugin/cache/config file is patched or shadow skill installed.
Fresh product fixtures and client runtime state are used for the corrected series;
actual reads must substantiate procedure composition. The absent case masks this
same source path. This tests composed instructions, not automatic native plugin
activation. No source skill change was justified by this harness limitation.

## Analyzer-command correction

Both completed implementation conditions passed three behavioral tests, then the
original prescribed mypy invocation reported duplicate module names (`domain` and
`app.domain`) because this fixture uses a namespace package. Each independently
added `--explicit-package-bases` and passed the same strict flags for both required
files, without changing configuration, adding an initializer or weakening analysis.
The observed product inputs and prompts were identical throughout the pair.

The durable preparation command and README now include that flag. This is a
reproduction correction after the observed runs, not a claim that their first
command passed. The recorded preparation identity above is the executed input;
the corrected helper's SHA-256 is `8e2a104df4266589a88a6bbd5ef5c9422c1ca375d2725bd7ff28ee35a336f990`.
No model repetition is needed: the corrected command actually passed in both
original contexts and no normative skill or product behavior changed.

## Observation results

The corrected design, implementation and review pairs completed with exit 0 and
`turn.completed`. Coordinator review of actual files and commands found:

- Both designs specify the actual domain/transport owners, a single locked
  idempotent transition, immutable snapshots, missing-ID compatibility, alternatives
  and proposed checks. Only the canonical task changed. Each produced task passed
  the source checker in its target context (one artifact, zero errors each).
- Both implementations produced byte-identical domain code: look up under the
  existing lock, immediately return an already-cancelled record, otherwise create
  a cancelled frozen record, restore quantity once, store it and return it. Each
  ran all three unchanged acceptance tests successfully and passed strict mypy
  for domain and acceptance after the documented namespace-package correction.
  Only domain and canonical task changed; HTTP and the oracle stayed unchanged.
- Both reviews located the seeded stock-inflation defect at domain lines 38–40,
  explained the sequential/concurrent overselling case and accepted E1. Both
  observed two expected failing tests and one passing missing-ID test. Neither
  changed any project file or invented another consequential finding.
- The candidate review additionally checked first-transition/frozen-field behavior
  because the failing test stopped before its final immutability assertion. Its
  stronger optional `--disallow-any-expr` check across tests reported inferred
  `list[Any]` at acceptance line 39; it reported this as a test-analysis limit,
  not a second domain defect or a passing check. The mandatory implementation
  analyzer flags pass. Control limited that stronger check to the domain and passed.
- The unrelated request made the exact `servce` to `service` substitution in
  README, with no other file changes. Commands did not read an AEK task skill or
  the project-skill guide; general Superpowers/verification reading still occurred.
- The explicit review with the Superpowers source masked read the native review
  skill and local guide, used direct rules, found the same seeded defect, accepted
  E1 and changed no files. It honestly reported the stronger test-analysis limit.

Candidate commands demonstrate implicit reads of the design, implementation and
review native entries. Design/implementation read the review entry at their
existing completion boundary; no second review task, new plan or reviewer dispatch
followed. Installed Superpowers procedures were actually read through the explicit
common route in present cases; the absent case read none. There was no observed
recursive procedure, installation, model reassignment, Git write or implementation
from a design/review-only request. This is command/file evidence, not complete
visibility into hidden model reasoning or every internal native read.

Both small-fix conditions completed with the same one-line Boolean guard in
`Inventory.reserve`, three passing regression tests and strict mypy success for
domain/tests. They changed domain and the existing task, adding only a focused
test module. No cancellation, new design document or setup appeared. The candidate
implicitly read implementation and completion-review entries, with no observed
design/brainstorming read. The no-profile condition retained direct technical rules
and did not try to install the omitted profile. All ten completed observations
passed the coordinator's scope/expected-outcome review; seeded review-test failures
are expected evidence of the known defect, not failed review tasks.

## Telemetry and comparison limits

These are literal native `turn.completed` token fields and outer elapsed seconds.
Commands count completed command-execution items, including checks and failed probes;
a shell's aggregate exit code does not enumerate every inner command failure.
Cached input is reported separately, not additional input to sum. Monetary charges,
hidden reasoning contents, context selection internals and total provider compute
are unknown. No human product correction was supplied during any completed trial.
The explicit source-route repair and analyzer-command correction were harness/input
work and are documented above rather than hidden as model success.

| Case | Seconds | Commands | Input tokens | Cached input tokens | Output tokens |
| --- | --- | --- | --- | --- | --- |
| `design-control` | 207.57 | 17 | 497918 | 439680 | 7707 |
| `design-candidate` | 203.88 | 13 | 445347 | 394752 | 7713 |
| `implementation-control` | 102.98 | 14 | 506264 | 460032 | 3684 |
| `implementation-candidate` | 104.36 | 13 | 458750 | 411136 | 3902 |
| `review-control` | 71.36 | 10 | 225497 | 188928 | 2105 |
| `review-candidate` | 71.08 | 11 | 269433 | 232704 | 2289 |
| `small-fix-no-profile` | 84.44 | 12 | 307004 | 270976 | 2852 |
| `small-fix-candidate` | 85.38 | 9 | 320908 | 285696 | 3100 |
| `unrelated` | 43.24 | 7 | 153628 | 129280 | 1590 |
| `review-no-superpowers` | 62.88 | 10 | 160452 | 131456 | 1931 |

Design and implementation candidates used fewer emitted commands and input tokens
in this run, while review and small-fix candidates used more input/output tokens.
Elapsed differences are small; there is no consistent measured advantage. Both
designs are lengthy for the fixture (hundreds of lines), with excessive policy
reporting; candidates also reread some still-applicable procedure text. These are
observed overhead limits, not unresolved functional regressions or proof of an
improvement. Provider caching, sequential control-before-candidate order, one run
per condition and unblinded coordinator review prevent causal/statistical claims.

The meaningful bounded result is precise native task selection, successful domain
acceptance, correctly scoped review and preserved fallback without a material
regression in these scenarios. It is not a universal rule-adherence guarantee.

| Result identity | SHA-256 |
| --- | --- |
| `design-control/docs/plans/cancel.md` | `fa7d80a355b7fb7baa28e73b43767be098e9b39e11d0645e4a4d321fa2a47150` |
| `design-candidate/docs/plans/cancel.md` | `aa495cb37b2f8943dbafb5836c3516c8ae43abe08680f67d39f276d7700ab842` |
| `implementation-candidate/app/domain.py` | `cebfcef6100babf3e806f5d48017453bc0d213ffd813ea8151dd59f16da49dce` |
| `small-fix-candidate/app/domain.py` | `3d6e005d0ac969deff2615681cb629ebd3d3c9d695d67e9ec8c7447916e6aa03` |

Both domain implementation outputs are byte-identical, as are the two Boolean-fix
domain outputs. Generated documents/results are retained in the disposable stage
directory for review; the source inputs, prompts, expected/actual behavior, commands
and result identities above remain sufficient to explain/reproduce the experiment
without those paths. Ephemeral child-process baseline paths are not consumer
recovery bases; the outer fixture manifests and source inputs preserve provenance.

## Client support and stage disposition

| Surface | Observed support and limit |
| --- | --- |
| Codex CLI 0.162.1, recorded gpt-6-astra/high configuration | Native discovery of all three repo skills; implicit design/implementation/review selection; explicit current review; source-hidden local routing and bounded behavior observed |
| Superpowers 6.4.2 with this private CLI runtime | Installed procedures read via explicit common AGENTS route and local adaptations; no automatic plugin discovery claim. Source-masked absence uses honest local fallback |
| Claude routes | PS-04 checked static import/path preparation; no new native activation or runtime observation here |
| Cursor routes | Existing source/reference support retained; no current native task-skill activation observation |
| Other clients, real consumers and HTTP integration | Unverified by these runs; no rollout or dependency/configuration change |

Saved model/configuration remained unchanged; the host config matched the private
pre-run copy before cleanup. The client was invoked without a model override; no
independent provider-side model-attestation claim is made. All recorded operations
used the source-masked boundary, and commands used adopted local rules rather
than the unavailable AEK source path.

V07–V09 and the scoped behavioral portions of AC03/AC05/AC06, with AC08's durable
evidence, satisfy PS-05/PS-06 for this declared client surface. No material tested
regression remains unresolved. Whole-system source reconciliation and final rollout
readiness remain PS-07/PS-08, not implied by this observation stage.


Stage-end maintenance checks passed for four changed/new evidence and fixture
documents, the preparation helper's strict mypy check, tracked diff whitespace
and separate untracked whitespace. Scoped baseline review preserved 276 of 278
original identities with exactly two planned changes and four planned additions.
Eleven private runtimes and their authentication copies were removed; none remain.
Read-only Git discovery probes in some child runs failed because the fixture is
not a repository; no initialization or Git write followed. No full source suite
was repeated for unchanged normative/checker inputs.
