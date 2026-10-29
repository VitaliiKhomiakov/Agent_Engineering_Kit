# Go block spacing enforcement

## Outcome and approved design

The user approved strengthening the Go rules, WSL configuration and regression
examples after investigation of a compact CIDR loop. Execute one source-library
maintenance stage inline, using Superpowers through the local adaptations.

Require a blank line between a completed control-flow block and its following
statement, including inside loops. Preserve adjacent operation/result checks,
attached `else` branches and the narrowly supported resource-cleanup `defer`
exception. Replace the current permission to join a configuration guard to the
following assignments. Enable `after-block` alongside `if` and `err`, retain
editing and non-mutating verification commands, and demonstrate rejection of
missing separators before parsing and appending in the nested-loop example.

The existing style owner, verification topic and tooling example remain the
authorities. Whitespace-only alignment of affected current Go examples is in
scope; historical evidence is preserved. No consuming-project migration, new
catalog resource, toolchain upgrade or agent delegation is selected. The initial
implementation stage excluded Git publication; the subsequent user authorization
is recorded below.

## Context and constraints

- Instruction root and execution checkout:
  `/home/vitalii/Documents/Local_Project/AgentsFramework`.
- Canonical design/progress owner: this document, maintained by the coordinator.
- Clean baseline: `c1af6b29fb387097256aa8e84261ac8a9a1516ef`.
- Pre-edit copies and new-path absence records:
  `/tmp/aek-go-block-spacing-fnsq1vu7/baseline/`.
- Preserve the fixture's Go 1.26.1, golangci-lint 2.11.3 and bundled WSL 5.6.0.
  Do not treat these checks as validation of the separate application's Go 1.27.3.
- Use the existing formatting/CI gates and disposable negative probes. No root
  application dependencies or new unit-test framework is needed. Source-library
  defaults select phase-end checks and risk-based independent review; this bounded
  policy/configuration change uses coordinator review with executed probes.

## Progress and acceptance

- [x] BS1 — Establish the approved rule and its tooling contract. Prior isolated
  probes in `/tmp/aek-go-loop-or8f9e5r/` established that `if,err` repairs the first
  missing separator but accepts the remaining missing line before `append`;
  `after-block` rejects that gap. It also rejects the old cohesive configuration
  example, so prose and examples must change together. Official WSL 5.6.0 sources
  define the exception for a direct error check followed by a related `defer`.
- [x] BS2 — Update `standards/go/style.md`, `standards/go/verification.md` and
  `standards/go/examples/style-tooling.md`; align only affected control-block
  separators in current Go examples. Add reproducible nested-loop and exception
  probes and a separate dated evidence record. Added the CIDR fixture and explicit
  cleanup/negative probes; aligned the router illustration and four separators
  in the Gin binding, LangChainGo and Go OTel examples without nonblank changes
  to those three dependency-backed examples.
- [x] BS3 — Validate the pinned configuration and clean fixture, reject each
  missing loop separator independently, verify whitespace-only repair and valid
  operation/error, `else` and related/unrelated `defer` cases. Check affected
  example syntax/tokens/spacing, artifact links, new files and the actual diff;
  complete scoped coordinator review and record evidence limits. The pinned
  configuration, clean fixture and required negative/repair cases passed. An
  initial implicit-capture cleanup probe exposed a real exception limit; the
  final rule requires an explicit receiver/argument for adjacency, and both
  explicit-argument acceptance and captured-closure rejection/repair were checked.
  All 18 current Go source blocks passed formatting/syntax checks; the three
  whitespace-only dependency examples retained identical tokens. All 268 default
  artifacts and the two new documents passed, along with diff checks. Details:
  [dated evidence](../research/2026-10-29-go-block-spacing.md).

Review focus: a separator must survive formatting; a clean `if,err` result alone
must not satisfy the new gate; nested blocks and same-input conditions have no
exemption; the `defer` exception is not permission to attach any cleanup; `else`
and closing outer braces must not acquire artificial separators. Changes to
existing examples must preserve nonblank contents and API/version contracts.

Scoped coordinator review: the style topic owns the rule and its narrow exception;
verification requires matching checks; the single tooling fixture keeps its pins,
commands and executable probes together. The Go entry already routes to these
owners, so no duplicate entry policy or new catalog resource is needed. Historical
records remain unchanged. The final diff contains six existing instruction/example
files and two new source-only records; no unresolved in-scope finding remains.

Status: implementation and verification complete; the user requested committing
and pushing this source-library stage. A consuming project needs its own scoped
adoption/tooling update before the additional gate is active there.

## Publication authorization

On 2026-10-29, the user explicitly requested committing and pushing these changes.
Publish the eight scoped files on the existing `main` branch to `origin/main`
(`VitaliiKhomiakov/Agent_Engineering_Kit`). The remote branch matched the baseline
before publication. The plan before this authorization update is preserved in
`/tmp/aek-go-block-spacing-fnsq1vu7/publication/plan-before-publication.md`.
Record the commit identifier and confirmed push outcome in the publication
handoff; this record does not claim publication before those operations succeed.
