# Review remediation (2026-10-23)

Status: awaiting user review; follow-ups B8/C9/C1, reviews 1–4 and the fifth
review's fixes complete; all six decisions accepted by the final review.
The coordinator owns this record; the delegated implementer updates it under that
ownership, and the coordinator applied the final-review edits. Earlier plans,
research runs and example evidence stay historical.

## Outcome and boundaries

Apply verified findings A1–E24 from five independent read-only reviews of HEAD
`8173afb`. Check each finding against the current files before changing anything,
and confirm vendor facts against official versioned documentation first. Executed
example code keeps its recorded semantics, so clarifications go in prose.
Architectural choices take the smallest resolution consistent with current owners
and are flagged for user review. No staging, commits, branches or worktrees.

- **Instruction root, repository and execution checkout:**
  `/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
- **Canonical task:** this document.
- **Execution:** inline by the implementer; read-only vendor-fact research was delegated.
- **Baseline:** HEAD `8173afb`, clean working tree, 117 tests OK, zero artifact errors.

## Progress

- [x] R1 — Blocking and contradiction items (A1, A2, B1–B4, C1).
- [x] R2 — Wording fixes across core, templates and stacks.
- [x] R3 — Vendor-fact items confirmed by dated official evidence.
- [x] R4 — De-duplication and structural items, with explicit partial scope below.
- [x] R5 — Verification run; results are in the final report to the coordinator.

## Decisions for user review

### A1/B7: root entry templates

`MIGRATION.md` "Entry and passport templates" now owns each template's role:

- `policy-entry.md` is the bundled catalog `entry`.
- `AGENTS.root.md`, `AGENTS.project.md` and the passport/workspace templates are
  read from the identified source and are not bundled.
- One root template is chosen per launch scope.
- A copy that is deliberately bundled must be passed to the checker explicitly,
  because the selected-bundle scan covers only catalog templates.

Rationale: this matches the current catalog and checker without changing bundle
contents. Registering the templates in the catalog was the alternative. It was
rejected because it would change the bundle closure for existing adoptions.

The content drift was reduced as follows:

- `AGENTS.root.md` gained a selected-routes placeholder and marks its stack links
  as illustrative. It also gained the task-template route and "Role definitions do
  not authorize invocation".
- `policy-entry.md` gained the size/cohesion route and "a local fix does not
  authorize a rewrite".

The remaining difference is deliberate: the root template is a fuller skeleton.

### A2: adoption task before one exists

Until application creates the canonical adoption task, the preparation preview
carries decisions, questions and evidence outside the target. Application then
creates the task in the target's agreed planning store before dependent writes.
The source plan is never that task. This is recorded in MIGRATION "Import inputs
and boundaries" and the ARCHITECTURE owner table.

### A6: MIGRATION step systems

- Steps 1–5 remain the procedure.
- Phases 1–3 are their detailed reference, and phase 4 is step 5's record update.
- Former Phase 5 is now "Separate follow-up", outside adoption.

No sections were moved. No inbound anchors to phases 4 and 5 existed.

### E11: MCP provider checklist

No shared owner was created. Each engine topic received the provider-independent
items it lacked, labelled as local policy:

- Godot gained one mutation owner, the difference between submission, completion
  and saving, and bounded waits.
- Unreal gained pre-adoption provider checks, the `EnableAnalytics` default and
  non-native provider qualification.

Option left to the user: extract a shared provider checklist, for example a core
section, and route both engines to it.

### D1: union variant interfaces

The TypeScript rule was relaxed instead of changing the executed examples:

- The union uses a `type` alias.
- A variant gets a named interface when it is reused, referenced on its own or
  non-trivial.
- Small single-use variants may stay inline.

This matches the TypeScript research ("aliases for unions") and the React/Next.js
examples. Please review it as a policy change.

### Other recorded choices

- **B4/B12:** a missing routing record or an absent
  `agents.max_concurrent_threads_per_session` in delegated mode now exits 2 (not
  evaluated). This follows "Missing/unconfigured record" and "where available" in
  model configuration.
- **E17:** "Do not add a node solely to look up another node" was read as "do not
  make a helper a Node only to look up nodes". Please confirm the intended meaning.

## Skipped or partial findings

- **A12:** already handled. MIGRATION states that other clients need a verified
  native skill mapping and use direct source reading until then.
- **A17:** not moved. Rename and retirement notes sit beside the update procedure
  that uses them; collecting them would scatter that procedure.
- **B11:** documentation now describes in-memory candidate rendering. The tests
  were kept as determinism/sentinel guards.
- **B15:** skipped. A lighter Cursor implementer needs a verified Cursor model
  selector.
- **B21:** skipped. The `servce` typo is a planted fixture for the 2026-10-11
  behavior trials (commit `430f1ff`). Flat/custom tests deliberately check only
  the design native reference.
- **C4:** the entries' own applicability lines were kept. The Python and Pydantic
  repetitions became a single route.
- **C6:** prose was reworded. The executed `k16_` tables and `K16_PG_SOCKET` are
  retained and now explained as fixture names from the recorded run; the Doctrine
  `composer.json` descriptions "for K08" are also retained.
- **D3:** skipped. Compact entry essentials are a library-wide pattern, not
  full-policy copies, and the `nodejs.md` heading anchor is used by the
  `nodejs-typescript` compatibility aggregate.
- **D7:** skipped. Research records no reason for the TypeScript versions; they
  reflect which harness was at hand.

## Follow-up: completed partial findings

The coordinator asked for B8, C9 and C1 to be finished.

- [x] **B8:** `architect.md`, `implementer.md` and `reviewer.md` are regrouped under
  "Inputs and authority", "Boundaries", "Procedure" and "Return". Their earlier
  clarifications are kept. A word-multiset comparison against snapshots taken
  after the second review pass (scratchpad `b8/`) showed no directive text added
  or removed by the regrouping itself; only order and headings changed. Against
  `8173afb`, earlier passes did change `reviewer.md` authority text (see "Fifth
  review" below). Adapter routes are unchanged and the adapter, portability and
  adoption tests pass.
- [x] **C9:** `php/verification.md#class-and-file-moves` now owns the general PHP
  rule: with or without an ORM, a move alone authorizes no DDL or data-schema
  migration, and registrations are checked only for integrations present.
  `doctrine/schema-verification.md` remains the Doctrine owner. These files now
  route instead of restating the rule: `php.md`, `symfony.md`,
  `symfony/verification.md`, `php-symfony-doctrine.md` (link target only),
  `doctrine.md` and `doctrine/models-mapping.md`.
- [x] **C1:** PostgreSQL keeps `**/*.sql`. A rendered glob exists only after the
  profile is selected. In a PostgreSQL project a changed SQL file is the
  schema/query work its `when` covers. Migration and query paths vary too much to
  narrow without false negatives. The rationale is recorded in `catalog.md`. No test
  or documentation referenced the glob string apart from the catalog entry.

## Second follow-up: re-review of decisions 1–6

An independent re-review accepted decision 6 (E17) and asked for changes to
decisions 1–5. Each point was verified against the files before editing. The
decision texts above record the first-pass state; this section supersedes them
where they differ.

- [x] **Decision 1 (A1/B7):** `templates/policy-entry.md` is now the single owner
  of the policy block. It absorbed the lines only `AGENTS.root.md` had: existing
  code as evidence, construction/DI and SOLID/KISS, bounded size exceptions,
  passport entry, delivery route, Git-free root and no preloading. It also marks
  engine routes as select-only. `AGENTS.root.md` is reduced to a skeleton: insert
  the block, and use the project map as its `$projects`. Two HTML anchors keep the
  historical links from a 2026-09-26 spec and a 2026-10-04 plan resolving. So no
  parity test is needed.
- [x] **Decision 1, choice rule:** MIGRATION "Entry and passport templates" now
  says: an existing root entry gets the policy-entry block merged into it; a
  multi-project workspace with no root entry uses `AGENTS.root.md`; a single
  project with no root entry uses the block as root `AGENTS.md`; an independently
  opened repository gets the rebased block plus `AGENTS.project.md`.
  `AGENTS.project.md` states that the language rule comes with the block.
  MIGRATION's layout link points to that section, and the checker wording now says
  "a separate explicit-path run". `catalog.md` limits bundled templates to catalog
  `templates`. Limit: `policy-entry.md` is now 89 physical lines, above the soft
  40–70 root-guideline range; the policy content is critical and not truncated.
- [x] **Decision 2 (A2):** the preview proposes the task path and store, and the
  user agrees them there; the planning policy adopted in the same application does
  not decide it. Creation is a target write, seeded from the preview, after which
  the preview is historical. Step 1 lists the task among create actions. Step 3
  protects it and treats an existing file at the path as a collision. The adoption
  record allows "to be created at <path>".
- [x] **Decision 3 (A6):** "Phases 1–4"; phase 3 maps to steps 1, 4 and 5. Phase 4
  restores the client activation report and names the existing-or-new record.
- [x] **Decision 4 (E11):** a new shared topic, `standards/editor-mcp.md`, is
  registered as a resource of both `unreal-engine` and `godot`. It owns
  provider-independent local policy: adoption inspection and authenticated
  loopback preference; disabling telemetry where supported, whatever the vendor
  default; version recording and qualification with fallbacks; connection and
  identity checks, and one mutation owner; batch reporting, the difference between
  submission, completion and saving, bounded waits, and recovery before retry.
- [x] **Decision 4, engine topics:** they keep vendor specifics and link to the
  shared topic. Unreal now says to disable `EnableAnalytics` where supported. That
  vendor fact was rechecked 2026-10-23 and added to the Unreal research addendum.
  Unreal qualification remains scoped to non-native providers. The shared file does
  not link to either engine topic, so a single-engine bundle has no dangling route.
  Tests: the Godot closure test now includes the shared file, a new test checks
  that each engine alone selects it and core does not, and the combined-engine
  test is unchanged. No pushback: a shared owner removes the drift that parity
  would only police.
- [x] **Decision 5 (D1):** the entry `typescript.md` and `contracts-structure.md`
  route union variants to the composition-effects rule. That rule defines "reused"
  (referenced by name, or the same shape in more than one type) and "non-trivial"
  (besides the discriminant, more than two fields or an inline nested object; a
  named-contract field counts once). It recommends composing unions, and points to
  the TypeScript example instead of React/Next. `reservation-form.md` gained a
  prose note that `Outcome` restates variants and how new code would compose them;
  its executed code is unchanged and was not re-run.
- [x] **Decision 6 (E17):** accepted; the missing comma between the Godot links
  is fixed.

## Third follow-up: decisions 1 and 2 (2026-10-24)

The third review accepted decisions 3–5. All points below were verified and
applied; none were pushed back.

- [x] **Nested entries (decision 1):** a single nested file serves every launch
  scope, so the entry rule now distinguishes them. A repository entered only
  through the workspace root uses `AGENTS.project.md` with local constraints and
  routes, under `instructions.local_guideline_lines`. A repository also opened on
  its own as the launch root carries the rebased policy-entry block, under
  `instructions.root_guideline_lines` for that scope, and records it as a
  deliberate duplicate derived from policy-entry with drift checks. This is
  recorded in the MIGRATION table, the Phase 3 exception and `AGENTS.project.md`.
  It relies only on recorded discovery evidence: the 2026-09-20 orchestration
  research says Codex composes instructions toward the current directory with a
  repository boundary, and ARCHITECTURE says a parent outside the discovery
  boundary cannot be assumed to load. No new vendor behavior is claimed. Phase 3's
  Cursor placeholder paragraph, which had split the language-rule paragraph, now
  follows it.
- [x] **policy-entry (decision 1):** `$routes` is defined in the template note as
  the selected profiles' entry routes with their catalog `when` conditions. The
  condition "database, driver and container profiles apply only when used" is
  restored. The two overlaps the reviewer named were merged without losing a
  condition; the file was 92 lines then and is 94 after the fifth review, accepted
  under the soft range.
- [x] **Decision 2:** step 1 now lists task creation only when no canonical
  adoption task exists and the user names none.
- [x] **Minor fixes on accepted items:** MIGRATION's Phase 4 line is wrapped.
  Unreal grounds native non-overlap in the provider contract plus the shared rules.
  Long prose in `editor-mcp.md` and `mcp-editor.md` is reflowed without splitting
  links or code spans; a word-multiset comparison against pre-edit snapshots
  showed no text change, and three link-only URL lines remain long. The TypeScript
  "reused" rule now says "restated in more than one type", and the composition
  example uses the neutral name `RequestResult`.

## Final review (2026-10-24)

The fourth independent review accepted decisions 1–6 and the minor fixes. The
coordinator applied its three optional Minor notes in `MIGRATION.md`:

- [x] The deliberate-duplicate row names the concrete comparison: both copies in
  the adoption record's managed scope, compared under Repeat and update.
- [x] A repository opened on its own may use a supported native import of the
  adapted block instead of an inline copy, matching `ARCHITECTURE.md`.
- [x] The long Phase 3 prose line is wrapped.

## Fifth review (2026-10-24)

Two independent reviews of the full diff returned "with fixes", with no Critical
items. Every point was verified before editing; one optional point was skipped.

- [x] **R1:** `check_model_routing.py` now records an absent native ceiling and
  raises not-evaluated only after the default-role and role-file checks, so a
  definite conflict exits 1. A new test covers three cases: absent ceiling with a
  wrong role pair exits 1; with an invalid `--default-role` it exits 1; with
  everything else consistent it exits 2. `docs/maintenance/verification.md` states
  the precedence.
- [x] **R2:** `reviewer.md` again says "spawn another reviewer" and now carries
  the implementer's conditional further-delegation line. Recorded `reviewer.md`
  authority changes against `8173afb`: the spawn wording (blanket ban in pass 1,
  restored here with the conditional line); a coordinator-supplied diff, new-file
  list and baseline when tools cannot list changes (B3); and write-producing
  checks requested from the coordinator instead of an unspecified executor (B2).
- [x] **R3:** `typeorm/nestjs-integration.md` restores the obligation: "Ensure one
  of those paths actually runs in the deployed process."
- [x] **R4:** "Reused" now means consumers need to refer to the variant by itself,
  or the same variant meaning is restated within the same contract, module or
  feature. The React note now says "within the same reservation feature" and still
  reads correctly.
- [x] **R5:** in `godot/tooling-mcp.md`, the GdUnit4 row covers only the
  scene/input runner and editor test inspector; C# goes only to GdUnit4Net. GUT's
  default is labelled local policy based on the project READMEs.
- [x] **Minor fixes in `standards/`:** Unreal "By default" restored. The
  `work-modes.md` saved-assignment sentence covers the coordinator's pair. Python
  "where used or explicitly selected". The Godot resource-loading rationale now
  quotes "store the path of the script they use" and cites the proposals.
  Policy-label leftovers in `typescript.md` and `mcp-editor.md` fixed.
  `catalog.md` wording fixed. Next.js: the mutation bullet merged into its
  existing section. `authorized-command.md`: "must map".
  `nextjs-feature-structure.md`: "Proxy (`middleware` before 16.0)". Godot
  undo/unsaved cited to EditorUndoRedoManager and running-code-in-editor
  (re-fetched 2026-10-24). Go wording wrapped.
- [x] **Minor fixes outside `standards/`:** `policy-entry.md` absorbed "GDScript
  does not select Python/Node application profiles" and "cleanup". MIGRATION: a
  launch-root repository records its duplicate even under the merge row; an
  explicit import agrees the proposed task path unless it is unresolved or
  collides; the source-plan rule has one owner (Prepare and apply); "Ready for
  review" lines are readiness criteria, not extra checkpoints. The read-only
  design-result rule moved to `project-skills.md`, and the skill links to it.
  `AGENTS.root.md` anchors carry a pointer and a removal instruction. The test
  comment no longer claims a trivial property.
- [x] **Traceability of tool/test changes:** B13: the checker skips fences whose
  backtick info string contains a backtick, with a test. B18: `examples/` in the
  default scan, with a test. B9: `assertRaisesRegex` with complete fixtures. B10:
  specific failure fragments. B14: a shipped-template agreement test. B4/B12 and
  R1: routing exit semantics and tests. E11: the shared editor-MCP selection test.
- Skipped (optional): a `Promise.catch` alternative for React `use`. The
  2026-10-23 research found the current react.dev page offers only an Error
  Boundary, so no vendor evidence supports adding it.

## 2026-10-23 vendor evidence used

Checked through official pages or package sources on 2026-10-23. Earlier research
runs are unchanged.

### Node 24.13.0

- **D4:** [TypeScript](https://nodejs.org/download/release/v24.13.0/docs/api/typescript.html)
  says only erasable syntax is stripped, `--experimental-transform-types` covers the
  rest, imports need explicit `.ts` extensions, and `tsconfig.json` is ignored.
- **C17:** [globals](https://nodejs.org/download/release/v24.13.0/docs/api/globals.html)
  says `fetch` is unflagged in 18 and stable in 21, and `AbortSignal.timeout` was
  added in 17.3/16.14.
- **D6:** `https://nodejs.org/dist/index.json` has no 24.13.6 runtime. The research
  record names `@types/node` 24.13.6.

### Next.js 16

- **D14/D15:** the
  [Proxy reference](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
  and [16 upgrade guide](https://nextjs.org/docs/app/guides/upgrading/version-16)
  say middleware was renamed `proxy`, `proxy` runs only on Node.js, a `runtime`
  config throws, and Edge stays on `middleware`.

### React, NgRx and typescript-eslint

- **D16:** [React `use`](https://react.dev/reference/react/use) cannot be called
  in try/catch; rejection goes to an Error Boundary.
- **D18:** the [NgRx Entity adapter](https://ngrx.io/guide/entity/adapter) has
  `setMany` add/replace and `upsertMany` add/update without partial updates.
  `ngrx/platform@20.0.1` merges shallowly.
- **D5:** [typescript-eslint no-floating-promises](https://typescript-eslint.io/rules/no-floating-promises/)
  defaults `ignoreVoid` to `true`.

### NestJS and TypeORM

- **D9:** [NestJS lifecycle](https://docs.nestjs.com/fundamentals/lifecycle-events)
  says shutdown hooks run on `app.close()` or on signals after
  `enableShutdownHooks()`.
- **D9:** `nestjs/typeorm` `TypeOrmCoreModule.onApplicationShutdown` destroys the
  DataSource (tags 11.0.0 and 12.0.2).

### PHP, Pydantic and Go

- **C11:** the [PHP manual](https://www.php.net/manual/en/language.types.declarations.php)
  says "Function calls from within internal functions will not be affected by the
  strict_types declaration."
- **C3:** [Pydantic validators](https://pydantic.dev/docs/validation/latest/concepts/validators/)
  (latest; the repository's executed baseline is 2.13.4) say plain validators skip
  internal type validation and wrap validators may not call the handler.
- **C14:** [Go 1.27 notes](https://go.dev/doc/go1.27) say the HTTP/1 Response.Body
  drains on close up to a conservative limit. The go1.26.x `client.go` has only
  the reuse warning.

### PostgreSQL image

- **C16:** docker-library/postgres `18/trixie/Dockerfile` sets
  `PGDATA=/var/lib/postgresql/18/docker` and `VOLUME /var/lib/postgresql`.
  The 17 image keeps `/var/lib/postgresql/data`.

### Godot 4.7

All pages are under `https://docs.godotengine.org/en/4.7/`.

- **E5:** `classes/class_fileaccess.html` warns about object deserialization.
  `tutorials/scripting/resources.html` says resource files store their script
  path. Script-on-load risk is stated only in godot-proposals #4925 and #10968,
  so the rule is labelled local policy.
- **E6:** `class_object.html#class-object-private-method-init`,
  `class_resource.html` and `resources.html` say the Inspector needs defaults and
  C# needs a parameterless constructor.
- **E7:** `engine_details/engine_api/gdextension/gdextension_file.html` and
  `tutorials/scripting/cpp/about_godot_cpp.html`.
- **E8:** `tutorials/scripting/c_sharp/diagnostics/GD0001.html`,
  `c_sharp_basics.html` and `c_sharp_differences.html`.
- **E13:** the docs are silent. Engine issues #78587 and #93424 are cited as issue
  evidence only.
- **E14:** `tutorials/export/exporting_projects.html` and
  `best_practices/version_control_systems.html`.
- **E15:** `class_object.html` (connect note) and `class_callable.html`.
- **E16:** `tutorials/migrating/upgrading_to_godot_4.5.html`.
- **E17:** `class_object.html`.
- **E18:** `gdscript_basics.html`. That typed Dictionary needs 4.4 is official;
  emit-time non-checking is implied by "it's up to you to emit the correct values".
- **E3:** `class_editorundoredomanager.html` and `running_code_in_the_editor.html`.
- **E19:** the GUT and GdUnit4 project READMEs (not vendor docs).

### Unreal Engine 5.8

- **E1:** dev.epicgames.com honors `?application_version=5.8`. A version missing a
  page returns an empty shell.
- **E20:** [Object pointers](https://dev.epicgames.com/documentation/en-us/unreal-engine/object-pointers-in-unreal-engine?application_version=5.8)
  and [FGCObject API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/FGCObject?application_version=5.8).
  That `GetReferencerName` is pure virtual is unconfirmed; the wording does not
  depend on it.
- **E21:** [Interfaces](https://dev.epicgames.com/documentation/en-us/unreal-engine/interfaces-in-unreal-engine?application_version=5.8).
- **E22:** [Build operations](https://dev.epicgames.com/documentation/en-us/unreal-engine/build-operations-cooking-packaging-deploying-and-running-projects-in-unreal-engine?application_version=5.8).
- **E23 and E11:** [Unreal MCP](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-mcp-in-unreal-editor?application_version=5.8)
  says "clients should not issue overlapping Tool calls" and
  `ModelContextProtocol.EnableAnalytics` defaults to true. A dated addendum is in
  the Unreal skills research record.

## Checks

- `python3 tools/check_instruction_artifacts.py` ran with defaults and with
  explicit edited `docs/` paths.
- The unittest suite ran, followed by `git diff --check`.
- New-file inspection covered this plan.
- Strict mypy was unavailable on 2026-10-23 (`No module named mypy`). On
  2026-10-24 the coordinator ran mypy 2.1.0 from an isolated scratchpad venv with
  the documented flags: "Success: no issues found in 8 source files". The
  implementer re-ran it after the fifth-review tool/test edits with the same
  result.
- Executed examples were not re-run: only their prose changed.
