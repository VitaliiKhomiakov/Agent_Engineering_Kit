# Go spacing enforcement

## Agreed outcome and scope

The user approved tightening the Go readability rule after reviewing adjacent
independent guards in `files.go` and `policies.go` in the separate Medical &
Pharmaceutical Intelligence project. Independent checks must be visually separate
even when they validate the same object; an operation and its immediate error
check remain together. Add a compatible automated spacing check to the library's
inactive tooling example, with positive and negative evidence.

One authorized stage, executed inline in the current source checkout. Update the
rule owner, its verification procedure and existing example, then check and review
the coherent result. No consumer import, consumer source edits, toolchain upgrade,
active root tooling or delegation are selected. Git writes were not selected for
implementation; the user's subsequent publication request is recorded below.

## Ownership, baseline and constraints

- Instruction root and execution checkout:
  `/home/vitalii/Documents/Local_Project/AgentsFramework`.
- This document is the canonical design, plan and progress owner.
- Clean tracked baseline: commit `1f84eda1dcecb4dac92700b7ba0dccb45968618e`.
  Scoped original copies and new-path absence records:
  `/tmp/aek-go-spacing-ctv_dc8e/baseline/`.
- [Style](../../standards/go/style.md) owns spacing semantics;
  [Go verification](../../standards/go/verification.md) owns adoption and checks;
  [the tooling example](../../standards/go/examples/style-tooling.md) owns runnable
  configuration and reproduction. Preserve those owners and existing entry routes.
- Preserve the example's Go 1.26.1 / golangci-lint 2.11.3 pins and historical
  evidence. Record this run separately in `docs/research/2026-10-29-go-spacing.md`.
- Narrow `wsl_v5` checks must reject adjoining guards while accepting immediate
  error checks. Syntax-based lint does not prove all semantic step boundaries.
  No blanket line-count, return-spacing or all-linter policy is introduced.

## Progress

- [x] G1 — Confirm the pinned linter contract and probe a narrow configuration.
  The checksum-verified 2.11.3 binary contains WSL 5.6.0. Configuration validation
  and the clean fixture pass; adjoining guards and a detached direct `err != nil`
  check fail with the intended WSL diagnostics, while formatting alone passes.
  An adjacent operation/error check passes. `errors.Is` predicates are a measured
  analyzer limit, not evidence that every error-check form is enforced.
- [x] G2 — Tighten the rule and verification procedure; update the existing
  configuration, examples and reproducible spacing probes without stale exceptions.
  Added the guard rule, required format/spacing gates, a narrow WSL configuration,
  scoped repair command and positive/negative probes. Also separated nine adjoining
  guards in the existing Go domain, Eino, LangChainGo and Go OTel examples; their
  originals were captured before editing. This consistency extension changes only
  blank lines, not their APIs, dependencies or historical runtime claims.
- [x] G3 — Run the changed fixture's applicable checks, artifact/link checks and
  `git diff --check`; inspect new files and the scoped diff, record evidence and
  resolve in-scope findings before handoff.
  Passed: official schema validation, 22 final fixture command checks, four
  example formatting/token/syntax/guard checks, 268 default artifacts and both new
  task/evidence documents. `git diff --check` and separate new-file whitespace
  inspection passed. The scoped coordinator review covered the policy, narrow
  configuration, repair/CI commands, evidence limits and all changed examples;
  no unresolved in-scope finding remains. See the
  [dated evidence](../research/2026-10-29-go-spacing.md).

## Acceptance and review focus

Consecutive standalone guards of one input are separated; `else if` remains part
of its conditional; assignment/error-check pairs remain adjacent. The automated
check must expose the reported failure shape that `gofmt` accepts, with no claim
that a clean linter proves purpose-based grouping. Existing naming/error rules and
non-mutating CI behavior remain valid. Required tooling adoption is explicit and
version-compatible; the example remains inactive until adopted in a target.

Status: complete; the user requested publication of the source-library stage. The seven
modified files retain their pre-stage copies; both new files were inspected
separately. Historical evidence, catalog/profile selection and native templates
were preserved. No catalog or checker behavior changed, so their unchanged unit
suites were not repeated. Runtime/tool/cache cleanup leaves the scoped baseline,
probe scripts and logs available through handoff.

Consumer import is a separate scope: Medical & Pharmaceutical Intelligence still
has its previous adopted copy and application code. Applying these rules there
requires the existing adoption procedure and its supported toolchain checks;
the source change does not claim that adoption has occurred.

## Publication authorization

On 2026-10-29 the user explicitly requested a push. This authorizes committing the
seven changed standards/examples and the two new task/evidence documents, then a
normal push of the current `main` to `origin/main` in
`VitaliiKhomiakov/Agent_Engineering_Kit`. The reviewed implementation and its check
evidence remain applicable; only this authorization/status note changed afterward.
The pre-publication plan is preserved in
`/tmp/aek-go-spacing-ctv_dc8e/publication/plan-before-publication.md`.
The resulting commit and remote verification belong in the publication handoff.
