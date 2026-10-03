# Angular and NgRx engineering rules

## Outcome and design

Prepare reusable Angular/NgRx coding and architecture rules from official
documentation, covering Store, Effects, Entity, Router Store, SignalStore, Angular
signals, Observable flows, selector memoization, OnPush, feature boundaries,
services, modules, components and styles. This document owns design, work and
verification; source findings belong to the companion research note.

Extend the existing short-entry/topic-section format with independent `angular`
and `ngrx` catalog profiles. Angular requires the existing TypeScript profile;
NgRx requires Angular but Angular does not require NgRx. Retain local state,
SignalStore and classic Store as explicit choices with one authoritative owner
per datum. No migration, package installation in the library or application
architecture selection is implied by publishing these rules.

## Context and constraints

- Workspace and execution directory: `/home/vitalii/Documents/Local_Project/AgentsFramework`.
- Canonical plan: `docs/plans/2026-09-29-angular-ngrx-rules.md` (this file).
- One coherent documentation stage, executed inline; no delegation/model setup.
- Superpowers brainstorming, writing-plans, executing-plans and verification
  follow `standards/superpowers.md` adaptations for ordinary documentation.
- Direct mode, no Git writes or worktree. Git metadata is unavailable in this
  environment; original file copies and prior absence are recorded under
  `/tmp/af-angular-ngrx-20260929-baseline/manifest.json`.
- English standards follow the library convention; user reports are Russian.
- Use primary sources; distinguish moving documentation from installed versions,
  framework mechanisms from our architectural policy, and examples from executed
  application verification. Do not prescribe preview APIs to older projects.
- Read only relevant sections during adoption; research/examples are optional.

## Authorized stage: complete documentation package

Status: complete; package ready for user review.

- [x] Inspect existing profiles, catalog semantics and verification policy.
- [x] Study official Angular, NgRx and RxJS documentation; record sources and
  version-sensitive decisions in the research note.
- [x] Write Angular and NgRx entries, topic sections and focused examples.
- [x] Register resources and conditional routes in the catalog, README,
  TypeScript entry and project architecture passport.
- [x] Check TOML, resources, dependency closure, local links and scoped changes;
  review technical claims against sources and report executable-check limits.

Acceptance: every requested concern has an actionable owner; plain Angular does
not pull NgRx or React rules; Store-only and SignalStore-only tasks reach the
right sections; older Angular/NgRx APIs remain version-gated. Review race/error
recovery, mutation breaking OnPush/memoization, injection lifetime, nested route
parameters, SSR isolation, and styling boundaries. Examples must state their
scope and not be claimed as compiled or executed without evidence.

## Evidence and handoff

Delivered two entries, twelve topic sections and two examples. Updated five
existing integration files (README, TOML catalog, catalog semantics, TypeScript
entry and architecture passport), with this plan and the
[research note](../research/2026-09-29-angular-ngrx-engineering-practices.md).
Total scope: 23 files. No existing Angular/NgRx content was overwritten.

Checks on the completed rules/examples:

- Python `tomllib` parsing and catalog inspection: all 23 profile IDs unique;
  all 174 source/resource paths exist; dependency references exist and are acyclic.
  Angular/NgRx directory resources exactly match their catalog declarations.
- Dependency-closure assertions: Angular includes TypeScript/core and excludes
  NgRx/NestJS/Next.js; NgRx includes Angular and excludes NestJS/Next.js. Conditional
  package routes preserve Store-only and SignalStore-only application choices.
- Markdown inspection: 124 local link targets exist; fenced blocks are balanced.
- `/tmp/af-angular-ngrx-check/node_modules/.bin/ngc -p /tmp/af-angular-ngrx-check/tsconfig.json`:
  exit 0 on six extracted TypeScript blocks, strict types/templates and library checks.
- `node /tmp/af-angular-ngrx-check/check-examples.mjs`: four cases passed, zero
  failures/skips. Covers selector identity/immutability, stale-read cancellation,
  error recovery, isolated injectors and destruction cleanup.
- One accountable inline review against the baseline and acceptance criteria:
  scope, source-backed mechanisms, version limits, data ownership, race/reset
  handling, optional package routing and examples reviewed; no unresolved findings.
  The scoped diff is `/tmp/af-angular-ngrx-review.diff` (captured before this
  reporting-only plan update). No additional reviewer was required for this
  documentation package under the project's Superpowers adaptations.

Verification used Angular 20.3.0, NgRx 20.0.1, TypeScript 5.9.3, RxJS 7.8.2 and
Node 24.13.0 in a temporary harness with install scripts disabled. The source
research also covers newer moving manuals; no v22 execution is claimed. No
browser/E2E/SSR test, live HTTP adapter, full bootstrap, Entity/Router Store or
classic Effects runtime check was performed. These limitations are explicit in
the research and do not imply application adoption or performance guarantees.

Final checkpoint: inspect the complete package. No application implementation,
dependency migration, commit or deployment is a subsequent authorized stage.
