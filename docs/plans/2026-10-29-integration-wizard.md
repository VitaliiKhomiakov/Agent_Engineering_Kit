# Integration wizard and first-use guidance

## Outcome and authorization

The user selected an instruction-only wizard in the AI client's conversation and
authorized implementing it plus rewriting README so a reader immediately understands
how to start and work with the framework. The agreed menu covers an existing project,
a new project, an update and a check of an existing adoption. It should discover
existing technologies before asking the user to fill gaps, prepare concrete changes,
apply within authorization and report actual progress/results.

This is source-library maintenance in
`/home/vitalii/Documents/Local_Project/AgentsFramework`, in the current checkout.
This file is the single task/specification/progress owner. Execute inline using
Superpowers writing-skills/planning/verification with local adaptations. No new
installer, TUI, model runtime, persistent skill installation, target adoption or
Git delivery was part of the initial implementation request. No delegation is needed for this bounded
instruction change; model-routing settings remain untouched.

Clean starting HEAD: `cbe1d0b`. Original contents/absence for the three existing
files and this new plan are recorded in
`/tmp/aek-integration-wizard-b1_3jynf/manifest.json`, with copies in `baseline/`.

## Ownership and decisions

- `templates/skills/aek-integrate-project/SKILL.md` owns the conversation/menu,
  question cadence, progress presentation and dispatch into the adoption procedure.
  Use available question controls, with numbered text as a portable fallback.
  Keep the public skill name and source-first invocation; no invented slash command
  or promise that opening a chat automatically registers a native skill.
- `MIGRATION.md` remains the procedure owner. Add narrowly scoped read-only checking
  and stack-evidence rules there, so the wizard does not become a competing importer.
  Preserve preparation-only boundaries, existing authorization, task/model choices,
  ownership-aware updates, recovery and the distinction between files and activation.
- README owns first-use instructions and ordinary user-facing examples: launch,
  menu expectations, review/apply, daily development, updates/checks and navigation.
  Keep artifacts in English and conversation in Russian, as previously agreed.
- Menu choices establish operation intent, not blanket write permission. Opening
  the menu, inspecting or checking an adoption cannot create target records/settings.
  Existing explicit application authorization is reused without redundant questions.
- Discovery is scoped to actual projects/components and evidence. Distinguish
  observed use, inference and requested future choices; manifests alone establish
  declared dependencies. Skip dependencies/generated/examples outside relevant scope,
  avoid executing project scripts and do not infer an entire framework from a suffix.
- Full imports retain the existing model-selection step. A read-only check reports
  current agreement/unknowns without performing first-use setup or rewriting records.

## Work and acceptance

- [x] W1: Implement the wizard and align its procedure routes.
  Four actions, source/target/client resolution, evidence-based stack questions,
  repeat/update reuse, bounded check-only mode, preview/apply and truthful progress.
- [x] W2: Rewrite README around starting and continuing work.
  Copyable source-aware prompt, explained menu, application request, ordinary
  development/review requests and update/check paths. Preserve technology navigation.
- [x] W3: Verify the changed instructions and complete coordinator review.
  Check Markdown/routes and skill frontmatter, walk through the scenarios below
  against actual disposable fixture files, confirm preparation/checking leaves
  those files unchanged and exercise applicable existing catalog/adoption checks.
  Inspect the full diff and new-file whitespace; report evidence limits honestly.

## Scenario focus

| Input or condition | Expected behavior |
| --- | --- |
| Open wizard with source known, target/action unknown | Present four actions, then request only missing inputs; no target writes |
| Existing mixed Go/Node workspace with sample dependencies | Identify actual components with evidence; do not promote examples or dependency directories into the application stack |
| New project path does not exist | Gather intended technologies; keep proposed facts distinct; preparation does not create the directory |
| Update with existing profiles, model choices and a local edit | Reuse facts and compare managed content; no reset of local edits or repeated setup questionnaire |
| Check-only request with invalid/missing installed routes | Report checked scope, findings and unknown activation; no repair, task creation or model setup |
| Explicit bounded apply request already supplied | Prepare/check the concrete scope and use existing authorization, without adding a mandatory confirmation layer |
| Missing source/client controls or interrupted work | Use applicable read-only/fallback paths, name unresolved scope and actual partial progress; no invented UI, success or timeout approval |

The baseline skill already routes import/update safely but has no menu, interaction
recipe or dedicated check-only trigger. This is source-inspection evidence, not a
claimed baseline model evaluation. Verification uses proportionate artifact
checks and coordinator-led fixture walkthroughs; no cross-client activation or
independent model-behavior guarantee is implied.

## Evidence and handoff

Implementation handoff: **W1–W3 complete; submitted for user review**. The skill guides the four
actions, MIGRATION owns stack evidence and read-only checks, and README leads with
a copyable launch request and explains ordinary work after adoption.

Validation at this change boundary:

- `python3 -B tools/check_instruction_artifacts.py README.md MIGRATION.md templates/skills/aek-integrate-project/SKILL.md docs/plans/2026-10-29-integration-wizard.md`:
  four artifacts and source catalog checked, zero errors.
- `python3 -B -m unittest tests.test_project_skill_adoption`: 10 tests passed.
  Existing checks cover selected instruction bundles and adapted native routes;
  they are not evaluations of the wizard's conversation.
- The skill's YAML frontmatter parsed successfully with `yaml.safe_load`; its
  name, description bounds and nonempty body passed the format checks.
- Coordinator-led walkthroughs used actual temporary Go/Node manifests and source
  files. The proposed `go`/`nodejs` selection resolved the required JavaScript/core
  resources without selecting sample-only LlamaIndex or dependency-directory
  LangChain. Version requirements were distinguished from installed runtimes.
- New-project preparation built a known fixture candidate in memory without
  creating its target. An existing adoption's B/C/N comparison had `N == B` and
  a locally edited C, so the preview retained C and the existing model/profile
  choices. This is a scoped inspection, not an automated merge implementation.
- A check-only run found the single injected `missing-runbook.md` link in
  `LOCAL_RULES.md` (expected diagnostic, exit 1). Fixture hashes, file/directory
  modification times and path sets stayed unchanged throughout inspection and
  preparation. Logs: `/tmp/aek-integration-wizard-b1_3jynf/check-only.log` and
  `walkthrough-results.txt` in the same directory; fixtures are disposable evidence.
- Scoped diff/instruction review covered menu dispatch, missing inputs, existing
  permission, cancellation/recovery, source availability and question-control
  fallback. It clarified check-only handling to avoid a new technology-selection
  questionnaire and kept the general conflict inventory outside the stack subsection.
- `git diff --check` and a separate new-plan whitespace check passed.

No native client activation, live UI or independent model behavior was evaluated;
the wizard is an instruction contract run by the coding agent. At implementation
handoff, no target import, native settings change, commit or push had been performed.
No evidence from the previous
framework-depth task was reopened.

## Authorized Git delivery

On 2026-10-29, after the implementation handoff, the user explicitly requested a
commit and push of these changes. Delivery covers README.md, MIGRATION.md,
`templates/skills/aek-integrate-project/SKILL.md` and this canonical plan in the
current `main` checkout. Use an ordinary push to `origin/main` at
`git@github.com:VitaliiKhomiakov/Agent_Engineering_Kit.git`. Existing verification
evidence remains applicable to unchanged inputs; check the amended plan and staged
scope before committing. This authorization does not permit a forced update.
