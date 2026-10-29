# Practical LLM framework guidance

## Goal and authorization

Expand the approved RAG/tool library with practical Eino guidance for Go and
deeper LangChain/LangChainGo, LlamaIndex, LangGraph and Langfuse instructions.
The user authorized implementation followed by an independent review for factual
errors, unnecessary complexity and missing precision. Resolve confirmed in-scope
findings before handoff. Respond in Russian; artifacts remain English.

This is a new expansion after the completed and committed
[RAG foundation](2026-10-29-rag-tools-research.md). This file is its sole progress
owner. Use Superpowers planning, inline execution and review through the local
adaptations. Work in the current checkout. The implementation/review scope initially
excluded Git delivery; the user subsequently authorized committing and pushing the
completed changes. Downstream adoption and persistent model/agent configuration
remain outside this task.

## Scope and baseline

- Instruction root and checkout:
  `/home/vitalii/Documents/Local_Project/AgentsFramework`.
- Clean starting HEAD: `b246689`. Pre-edit contents/absence for the intended paths
  are recorded in `/tmp/aek-framework-depth-xgvusasj/manifest.json`, with original
  files in that directory's `baseline/` subtree (nine present, twenty absent).
- Existing shared RAG/tool rules retain ownership. Entries route to detailed
  topics; examples are conditional. Do not duplicate the full common policies.
- Add `eino` as a Go-specific optional profile, with `go` and `llm-tools` available;
  RAG remains separately selected for actual retrieval work. Keep LangChainGo
  guidance within the existing LangChain profile's explicit Go route without
  implying Python/JavaScript API parity or requiring Go for other consumers.
- Split details by responsibility: composition, tools/retrieval, state/recovery,
  source ingestion/synthesis, instrumentation/privacy and bounded examples.
- Use simple, verified offline fixtures for real library boundaries. No paid model
  calls, source uploads or live observability service are required. Dependencies
  and runtime files belong in temporary fixture directories, not the library root.
- Source reviews and executed examples need separate version/evidence records.
  Preserve the actual project stack; a fixture pin is not an upgrade instruction.
- Workflow sequences remain examples, from simple calls to more complex flows.
  Required permissions, evidence and bounded completion remain applicable.

## Items

- [x] D1: Review the official contracts needed for the added topics and examples.
  Dated official sources, release-source checks and fixture pins are in the
  [research record](../research/2026-10-29-llm-framework-depth.md). Actual runtime
  versions and untested integration boundaries are distinct from source review.
- [x] D2: Write the detailed topics and bounded executable examples.
  Add the Eino entry/topics; expand the existing four vendor entries with routes
  to their details. Cover LangChainGo separately within its language route.
  Preserve useful existing entry anchors and common-policy ownership.
- [x] D3: Verify the examples and register the profile/resource integration.
  All six local fixtures pass their behavioral checks; both Python fixtures pass
  strict mypy. Go race tests and `go vet` pass for all three Go fixtures. Catalog
  registration and 43 profile-selection tests pass; strict mypy passes for the
  changed project test file. The checker reports 28 artifacts and zero errors;
  33 prepared bundles (11 selections in three layouts) pass. Scoped diff and all
  twenty new files pass whitespace checks. Six embedded code blocks match their
  executed fixture sources byte for byte.
  Check meaningful local success/failure boundaries in temporary Go, Python and
  Node environments; record exact tested versions and limits. Update catalog,
  selection guidance, README and focused profile tests; check artifacts, selected
  portable bundles, applicable strict/static checks and new-file whitespace.
- [x] D4: Obtain the requested independent review and resolve findings.
  Reviewer `/root/framework_depth_review`, fresh context, `gpt-6-astra` / `max`,
  inspected all 29 paths against the frozen hashes. Two bounded findings were
  confirmed and repaired; see the outcome below. No critical findings or need
  for broader restructuring were reported.
  One fresh-context read-only reviewer, `gpt-6-astra` / `max`, reusing the user's
  explicit selection in this session. Direct coordinator-to-reviewer edge only;
  one concurrent worker, no child delegation. No configuration writes. Supply
  baseline, exact scope, user constraints and valid evidence. Check reported
  inaccuracies, unnecessary abstractions and ambiguous rules; fix confirmed
  in-scope issues and rerun only affected checks.

## Acceptance and review focus

- Each detailed topic gives actionable rules and actual API/version boundaries,
  with enough precision to implement a tool or integration without copying an
  unrelated language's tutorial. No unsupported cross-language parity claims.
- Examples exercise relevant library APIs without requiring a complete production
  system. Clearly name omitted backend/model/server guarantees and required
  application-owned authorization, cancellation and data contracts.
- Eino distinguishes components, Chain/Graph/Workflow and ADK; streaming ownership
  and the selected interrupt/checkpoint API are explicit.
- LangGraph separates state/reducers/checkpoints from external effects and covers
  resume, cancellation and public streaming according to the actual contract.
- LlamaIndex distinguishes document/node identity, ingestion/store behavior,
  retrieval-only output and synthesis/tool/citation output.
- LangChain distinguishes runtime schemas, trusted context, tool-call/result
  pairing, structured output and the separate Go implementation.
- Langfuse covers SDK/server compatibility, OTel mapping/lifetime, privacy across
  exporters and experiments without implying a correct answer from a trace.
- Optional reading/profile choices remain portable; shared guidance and historical
  research are not copied into every entry or used as an unconditional reading list.
- Independent review covers both new and modified files, not just committed Git
  history. Its result and any repairs are recorded here without another task ledger.

## Evidence and handoff

Baseline and executable fixture directories are under
`/tmp/aek-framework-depth-xgvusasj`. The original worktree was clean, and the scope
is the 29 paths in its manifest. The follow-up Git delivery authorization is recorded
above; the completed implementation and review retain their original evidence.
Resolved dependencies stay in this disposable directory. Code in each Markdown
example is copied from its executed fixture, with explicit limits in that example.

Checks: `python3 -m unittest tests.test_profile_selection` (43 tests); strict mypy
with explicit/unimported `Any` forbidden and Python 3.11 for the changed project
test, Python 3.12 for the two fixture files; `go test -race ./...` and `go vet ./...`
in each Go fixture; `node --test tool.test.mjs`; Python unittest for `retrieval`
and `resume`; the artifact checker on all 28 scoped Markdown/TOML paths;
`git diff --check` and new-file `--no-index --check` comparisons.

The disposable `check_portability.py` builds five standalone vendor selections
and six language/RAG combinations in `.agents-framework`, `.`, and `rules/aek`.
It explicitly adapts the pre-existing Node entry's optional NestJS/TypeScript
routes when those profiles are omitted, following its “when used” conditions;
no blanket missing-link exemption or repository helper change was introduced.
The first fixture attempt exposed those missing harness classifications; the
corrected preparation passed all 33 cases. Results: `bundle-checks.json` and
`artifact-check.txt` in the temporary evidence directory. This is portability
evidence for prepared instructions, not native-client activation or live adoption.

## Independent review and repairs

- Important: the LlamaIndex evidence adapter accepted an empty node ID, allowing
  distinct chunks with the same source/revision to share a deduplication key.
  Both coordinator and reviewer reproduced two inputs becoming one output with
  pinned LlamaIndex. The adapter now rejects the empty identity before deduplication
  and preserves valid IDs. A focused regression plus the previous two tests pass;
  strict mypy passes on the corrected fixture.
- Minor severity, mandatory local acceptance: three Go fixtures lacked blank-line
  grouping at independent phases. Added the required separation, keeping each
  operation with its immediate checks, and declaration comments where applicable.
  Reviewed the diffs and `gofmt` output; executable behavior is unchanged, so prior
  race/vet results remain valid. No new helpers, dependencies or abstractions.

Pre-fix reviewed contents are preserved in `review-repair-baseline/` under the
temporary evidence directory. Embedded example blocks remain aligned with their
fixture sources. The coordinator accepts the reviewer’s declined areas: live
provider/schema behavior, real backend authorization/vector updates, crash/effect
recovery and Langfuse ingestion/prompts/experiments are explicitly outside executed
coverage. Additional languages/production applications and unchanged shared policy
were not reopened. No unresolved in-scope finding remains; the coordinator verifies
the focused fixes without restarting the independent review.

Final affected verification: six repaired/example/evidence artifacts pass the
checker with zero errors; `git diff --check` and all twenty new-file whitespace
checks pass. All six embedded blocks match their fixtures. The three Go repairs
retain identical executable lines after excluding blank/comment-only lines and
pass `gofmt`; the LlamaIndex behavioral/static reruns are recorded above. Unchanged
catalog/profile/bundle evidence remains valid.

Current state: **implementation and review complete**. The user authorized a
follow-up commit and ordinary push to `origin/main`; its Git result is reported in
the conversation. The preceding local RAG foundation commit is part of that branch's
history and will accompany the new commit if it is still absent from the remote.
