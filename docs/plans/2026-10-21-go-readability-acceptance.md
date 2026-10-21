# Go readability acceptance correction

## Task and state

**Goal:** Connect AEK's canonical Go readability convention to implementation,
existing review and coordinator acceptance, including adopted instructions.
**Design basis:** The user's compact/grouped router example, cases A–E and bounded
source-framework correction request of 2026-10-21.
**Status:** Correction and validation complete; awaiting user review.
**Execution:** Inline in the current checkout. No delegation, tooling installation,
downstream edits, staging, commits, branches, pushes or releases.

Instruction root and execution checkout:
`/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
This document is the canonical plan, evidence and progress owner; the coordinator
maintains it. No source-root model-routing selection is installed or needed.
The clean pre-edit revision is `f8b43b83bc2ae6f7a0fddeef86337f70daa668d8`.
Exact originals and this document's prior absence are recorded in
`/tmp/aek-go-readability-20261021-b5l0dwck/baseline.json` and `originals/` beside it.
The revision is a durable reference for the originally clean tracked paths;
temporary copies remain available through this review.

## Global constraints

- Keep detailed spacing rules and code illustrations in `standards/go/style.md`.
  They are AEK conventions, not a claim about Go language requirements.
- Preserve tightly related operations/checks and cohesive groups; no mechanical
  blank-line quotas, compulsory extraction, comments or Gin dependency.
- Use existing verification, review, evidence reuse and adoption owners. No new
  agent, review round, per-function report or parallel acceptance checklist.
- Preserve unrelated rules and local customization boundaries. Changes to
  acceptance expectations require assessing old evidence, not rewriting history.
- Separate source inspection, user-supplied observations, automated artifact
  checks, manual scenario assessment and actual native/model behavior.

## Progress

- [x] GRA-1: Identify owners, delivery routes, current gaps and tooling tradeoffs.
- [x] GRA-2: Clarify the canonical rule and connect scoped readability acceptance
  through Go entry/verification, shared verification, roles and orchestration.
- [x] GRA-3: Assess A–E, check artifacts and affected adoption/native routes,
  review the scoped diff, and present the result for user review.

GRA-1 through GRA-3 are complete; the current checkpoint is user review.
No implementation item or required check remains open in this bounded stage.
The implementation diff was inspected against the original baseline. Detailed
grouping rules remain in Go style; shared policies and roles route to the check.

## Investigation and uncertainty

The supplied investigation reports that both implementer and reviewer read the
rule and inspected/authored the compact function, tooling passed, and the
coordinator accepted the step. The original transcript and downstream files were
not supplied here; those observations are attributed to the user's investigation.
They establish an application/acceptance gap in that execution, not missing
discovery. They do not establish motives or a belief that gofmt was sufficient.

The current source already has a stronger spacing rule than the quoted sentence
and an explicit formatter/readability distinction. The correction builds on that
state rather than treating the older quotation as the entire current policy.

| Question | Confirmed source state before this correction |
| --- | --- |
| Canonical rule precision | `standards/go/style.md#readable-flow-and-spacing` already separates steps and keeps immediate checks together. Its guard-to-normal-work phrase can imply a break inside one configuration phase; the router counterexample is absent. |
| Implementation check | Shared implementer instructions require applicable rules and checks, but do not explicitly require inspection of final formatted code or separate readability evidence at handoff. |
| Binding style versus preference | The shared reviewer already permits findings for binding style violations. Shared verification and the optional project review result emphasize consequences without an explicit readability acceptance route. |
| Clean review without coverage | A generic clean result has no required statement covering the applicable semantic check. There is no automated review-output validator. This is insufficient evidence, not permission to violate the existing rule. |
| Coordinator acceptance | Orchestration requires scoped changes/evidence/risk review, but does not explicitly require coverage of a profile's readability check. |
| Native loading | All six implementer/reviewer adapters for Codex, Claude Code and Cursor explicitly request the matching shared body from the supplied instruction root. This confirms a source route, not actual client loading or compliance. |
| New integrations | The `go` catalog profile includes style and verification. Shared verification/orchestration and role bodies are already available through required profiles. Entries route to selected profiles; native adapters are activated only for selected roles. |
| Existing integrations | MIGRATION already compares last accepted adapted contents, current local contents and the new adapted candidate. Shared-body changes affect referencing adapters even without adapter-byte changes. |
| Overlap/conflict | The existing style/verification wording partially repeats grouping detail. The correction keeps the detailed convention in style and puts its check in verification, while retaining the distinction between a binding requirement and an optional preference. |

### Source ownership and downstream paths

The downstream `standards/go/style.md`, `standards/go/verification.md` and
`templates/agents/{implementer,reviewer}.md` correspond to the same bundle-relative
source paths. They are copied/adapted under the recorded bundle location, normally
`.agents-framework/`; they are not generated runtime code.

The current coordinator policy owner is `standards/orchestration.md`. There is no
source `standards/project-orchestration.md` in this checkout. The reported downstream
name requires checking that project's adopted provenance and active routes; it is
not authority to rename or overwrite a locally adapted file.

Target `AGENTS.md` is adapted from `templates/policy-entry.md` and, where selected,
`templates/AGENTS.root.md`/`AGENTS.project.md`. Source-root `AGENTS.md` governs this
library and must not be exported. Both root entry templates already route to
shared verification, and selected Go routes reach `standards/go.md`.
Native adapters instruct the role to load its adapted common body, which routes
to verification and the task's relevant profiles. No native syntax or model
settings need changes.

## Chosen design and ownership

| Changed file | Responsibility |
| --- | --- |
| `standards/go/style.md` | Canonical semantic grouping requirement, positive examples and compact-router counterexample explanation |
| `standards/go/verification.md` | Small Go readability check, scoped evidence example and tooling boundary |
| `standards/go.md` | Entry route for implementation and review to the Go check |
| `standards/verification.md` | Common readability acceptance/evidence requirement and applicability of previous evidence |
| `templates/agents/implementer.md`, `templates/agents/reviewer.md` | Role-specific routes into that acceptance owner, without copying Go rules |
| `standards/orchestration.md` | Coordinator route to the acceptance requirement |
| `standards/project-skills.md` | Optional review result routes to the same requirement |
| This document | Investigation, design, dated sources, scenario assessment and stage evidence |

The user's design constraints settle the material choices. This is a bounded
extension of existing instruction routes, using the local Superpowers adaptations;
no additional design approval, new lifecycle or separate specification is needed.
Existing root templates, native adapters, catalog and MIGRATION remain unchanged
because their existing routes and managed-content update procedure carry the fix.

## Tooling assessment — source review on 2026-10-21

| Approach | Fit and limits |
| --- | --- |
| Canonical instructions plus an explicit acceptance check | Selected. Identifies semantic phases, preserves cohesive statements and makes coverage reviewable within the existing handoff. It depends on agent/human judgment; no instruction can guarantee future compliance. |
| Additional whitespace linting | Not adopted. It can enforce selected syntactic approximations, but does not identify the purpose of each phase. Introducing it would add configuration and compatibility decisions without replacing this check. |

[Go Code Review Comments](https://go.dev/wiki/CodeReviewComments#Gofmt) distinguishes
mechanical formatting from other style concerns. The user reports a local gofmt
comparison preserving both router variants; that reported execution is not a run
performed in this checkout.

[wsl's documentation](https://github.com/bombsimon/wsl) and
[check definitions](https://github.com/bombsimon/wsl/blob/main/CHECKS.md) describe
statement/variable-based adjacency checks and configurable counts. For example,
`assign` restricts what can precede assignments without a blank line, while
`after-block` separates block statements. **Inference from these definitions:**
such rules can split the valid router configuration guard from its related
assignments. Shared identifiers also do not establish that two operations have
the same purpose. This is a documented-contract assessment, not executed linter
diagnostics for the examples.

[golangci-lint settings](https://golangci-lint.run/docs/linters/configuration/#wsl_v5)
exposes `wsl_v5` with options such as `branch-max-lines`, `case-max-lines` and
statement/variable adjacency. Its old `wsl` entry is deprecated. Neither a line
threshold nor an enabled whitespace analyzer is semantic acceptance evidence.
No linter is installed, mandated, reconfigured or version-upgraded here. Any future
project-specific adoption remains subject to
[Go tooling adoption](../../standards/go/verification.md#formatting-and-lint-adoption):
inspect the actual pinned toolchain/analyzers, demonstrate the exact diagnostic,
check compatible groups and false positives, resolve overlapping rules and retain
the semantic check. Existing tooling examples and their dated run records remain
unchanged.

## Validation plan and evidence boundary

- Manually assess A–E against the revised canonical rule, recording reasons here.
  Repository tests explicitly identify themselves as artifact/adoption fixtures,
  not model evaluations. No semantic instruction-following harness was found in
  the relevant tools/tests and maintenance documentation.
- Run the artifact checker for source files and this new plan, including links
  and anchors; inspect the new file separately from `git diff --check`.
- Run the existing agent-template and project-skill portability suites and
  focused Go/Gin/legacy profile tests. They cover native body routes, portable
  bundle layouts and local sentinels, not real client execution.
- Review the actual diff for single ownership, scoped acceptance, no new review
  cycle, no forced Gin and preservation of existing update/customization rules.
- A Go/gofmt/linter executable was not found on PATH or the usual checked local
  Go locations. No toolchain installation is needed for the instruction change;
  report the formatter reproduction limit rather than inventing an executed result.

## Scenario assessment and results

### Manual policy assessment

This is the coordinator's documented assessment of the supplied scenarios against
the revised [canonical rule](../../standards/go/style.md#readable-flow-and-spacing).
It is not an automated regression test, independent reviewer evaluation or model
compliance experiment. A–D assume changed code without an accepted exception.

| Case | Finding required? | Reason under the revised rule |
| --- | --- | --- |
| A — supplied compact `livenessRouter` | Yes | Creation, configuration, route registration and final-result delivery are distinct purposes. Missing separators occur after `gin.New()`, after `RedirectTrailingSlash = false`, and after the `GET` registration. One located finding can identify all three boundaries. No separator is required between the configuration guard and its related assignments. |
| B — supplied grouped router, now the canonical illustration | No | The four phases are visible, configuration remains cohesive, and the early error return stays inside its guard. The final result is a distinct phase in this multi-step function. |
| C — `result, err := buildResult()` immediately followed by its error guard | No | The operation and its immediate failure handling are one step. Neither `if` nor the guarded return independently demands a blank line. |
| D — the canonical two timeout assignments | No | Both statements configure related timeout fields in one small cohesive step. Their separate statements/lines do not imply separate phases. |
| E — unchanged or moved code with previous evidence | Conditional evidence assessment; no automatic style finding | Reuse an identified check if its code, relevant context, criterion and coverage still apply, mapping moved paths. If the clarified rule changes acceptance expectations or prior coverage is unknown, perform only the missing scoped inspection. A previous generic clean review or gofmt result is insufficient by itself; an actual rule violation found in the affected scope requires resolution. No repository-wide reformat follows. |

These decisions follow purpose and immediate operation/check relationships, not
statement counts, block endings or line thresholds. Missing evidence in E is an
acceptance gap, not proof of a code defect. The old guard-to-normal-work phrase
was replaced so it cannot be read as requiring a separator inside B's
configuration phase. The original read/error-check/transform example remains.

### Executed checks

The following checks ran on 2026-10-21 against this stage's eight changed source
documents, with the remaining tracked source at the recorded baseline:

| Check | Result and scope |
| --- | --- |
| `python3 -B tools/check_instruction_artifacts.py` | Exit 0; 222 artifacts, 0 errors. Checks source catalog, selected Markdown/TOML syntax and supported local links/anchors; does not execute Go or evaluate meaning. |
| `python3 -B tools/check_instruction_artifacts.py docs/plans/2026-10-21-go-readability-acceptance.md` | Exit 0; 1 artifact, 0 errors, including the affected recheck after adding scenario/check results. Final status-only text preserves those checked links/anchors. |
| Focused unittest command below | Exit 0; 14 tests passed in 10.307 seconds. Existing fixtures cover native adapters/common bodies for all three clients, contained/flat/custom layouts, Go selection, legacy resources/anchors and local-file sentinels. |
| `git diff --check`, scoped diff and separate new-file inspection | Exit 0 for the diff check; the new plan was read separately. Status contains only the eight intended tracked modifications and this new plan; no unrelated changes. |

```sh
python3 -B -m unittest -q tests.test_agent_templates tests.test_project_skill_portability tests.test_profile_selection.ProfileSelectionChecks.test_go_does_not_select_gin tests.test_profile_selection.ProfileSelectionChecks.test_gin_includes_go tests.test_profile_selection.ProfileSelectionChecks.test_legacy_aggregates_retain_all_family_resources tests.test_profile_selection.ProfileSelectionChecks.test_legacy_bookmarks_remain_resolvable
```

The coordinator's scoped diff review found no unresolved acceptance violation:
the canonical rule covers A–D without a syntactic blank-line mandate; E follows
the shared evidence owner; generic roles/coordination and the optional project
review result point to the same acceptance boundary. Detailed Go rules/examples
remain in one file. All modified operational files already belong to catalog
profiles, so no new resource declaration or Gin dependency is needed. Existing
root entry routes and six native implementer/reviewer adapter routes remain
intact. MIGRATION's B/C/N comparison, common-body update handling and local
ownership boundaries were inspected and remain unchanged.

The resolved source default is `review.independent = "risk_based"`. This bounded
instruction correction uses coordinator review; no extra reviewer was selected
solely for whitespace. No independent semantic review or live client/model
evaluation is claimed. The fixture suites do not establish a general update
engine, safe merging of arbitrary local customizations or runtime rule loading.

The new router is the user's grouped illustration, retaining its statements
and grouping with tab indentation; the compact case differs only in its three blank lines. No Go
behavior or existing executable tooling example changed. Go/gofmt and wsl were
not executed: the local formatter comparison remains attributed to the user,
and the whitespace-linter assessment is based on primary documentation.

Only the user review checkpoint remains. No further stage or downstream update
has been started.

## Delivery to integrated projects

New integrations select `go` (or a selection depending on it) and include the
changed existing resources. Follow normal native-body/entry adaptation and check
references from the target instruction root. Gin remains a separate selection.

Existing projects use the authorized
[repeat/update procedure](../../MIGRATION.md#repeat-and-update). Preview the changed
Go owners, shared verification, common roles and applicable coordinator/review
routes together. Compare B/C/N, preserve local exceptions and customizations,
reconcile overlapping edits, retain recoverable originals, and update accepted
contents only after relevant checks pass. Embedded older role instructions need
the [shared-body reconciliation](../../MIGRATION.md#model-selection-step), not a
blind source overwrite. Recheck active routes for a renamed downstream coordinator
document. Do not change models or enable roles to deliver this correction.

Assess previous readability evidence against the clarified requirement. An old
clean formatter/review result without relevant coverage cannot establish this
check. Revisit only the affected acceptance scope; unchanged/moved code with
still-applicable evidence does not trigger a formatting sweep. The source change
does not automatically update an existing target or prove native activation.
