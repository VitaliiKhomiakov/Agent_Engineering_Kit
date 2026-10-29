# RAG and tool workflow research

## Task and authorized stage

Collect primary documentation and engineering recommendations for RAG,
LlamaIndex, LangChain, LangGraph, Langfuse, supporting libraries and tool design.
Deliver English instruction drafts covering intent, question clarification,
database/web/other-source retrieval, answer construction, verification and delivery.
Respond to the user in Russian. Superpowers brainstorming and planning follow
the repository's local adaptations.

The research/proposal stage is complete. The user has now authorized implementing
the instructions in AEK. The current stage registers six optional profiles, moves
accepted rules to portable policy owners and connects selection/adoption routes.
No application implementation, dependency installation or downstream adoption is
part of this stage. After the reviewed corrections, the user authorized a local
commit of these instructions, integration changes, tests and task artifacts.

## Ownership and baseline

- Instruction root and execution checkout:
  `/home/vitalii/Documents/Local_Project/AgentsFramework`.
- Canonical progress owner: this file. No alternate task store or worktree.
- Baseline: clean `main` at `e3e181f`; the new task artifacts were absent.
- Model routing: no role configuration is needed for inline research; no agents
  are delegated and no model configuration is changed.
- Research evidence owner: `docs/research/2026-10-29-rag-tools-engineering.md`.
- Accepted design/ownership map: `docs/specs/2026-10-29-rag-tools-instructions.md`;
  operational rules now live in its linked `standards/` owners.
- User clarification: the stack may be Go, Python, Node.js or another language.
  Keep the core instructions language-neutral; supply conditional mappings for
  those three ecosystems without assuming SDK/API parity or requiring Python.
- Further user clarification: the described sequence is illustrative. Workflows
  may be simpler or more complex according to their goals. Pre-clarification
  contents of all three untracked documents are preserved at
  `/tmp/aek-rag-workflow-baseline-d6qr9qkh`, under their original relative paths.
- Integration baseline: `/tmp/aek-rag-integration-baseline-9x1ub0v_` preserves
  all 25 intended paths, including the three untracked task documents. Its manifest
  records HEAD and the prior absence of 16 new policy files. Inline execution uses
  Superpowers writing/executing plans through local adaptations; no delegation.

## Acceptance

- Named projects are covered from their own documentation; technical web advice
  comes from original authors, maintainers or primary research.
- Recommendations distinguish framework contracts, dated evidence and AEK choices.
- RAG covers ingestion, retrieval, source authority/access, generation and evaluation.
- Tool guidance covers schemas, authorization, errors, budgets, side effects and
  the difference between tool calls and application-owned workflow steps.
- The proposed flow defines branching, bounded retries, insufficient evidence,
  interruptions, verification and final delivery.
- The sequence is explicitly an example. Stage selection and complexity follow
  application goals and constraints; required guarantees remain applicable.
- Supporting libraries have selection criteria and limitations, not a mandatory
  all-in-one dependency stack or unsupported universal ranking.
- Source links and draft instructions are reviewable, English and structurally
  valid; runtime execution and benchmark claims are made only if actually tested.

## Items and progress

- [x] R1: Review the four named projects and record source/version boundaries.
  Reviewed official retrieval/tool/state/telemetry documentation, including moving
  URLs and Langfuse server/SDK compatibility. Evidence is consolidated in the research.
- [x] R2: Review retrieval/tool engineering and a bounded supporting-library list.
  Reviewed primary Anthropic engineering guidance, maintainer docs for storage,
  parsing, reranking and evaluation, search APIs, and MCP/OWASP trust boundaries.
  Expanded and completed language coverage after the user's clarification:
  Eino, LangChainGo, native Go OpenTelemetry, JavaScript LangChain/LangGraph and
  LlamaIndex.TS. No cross-language API parity is assumed.
- [x] R3: Write the research synthesis and actionable instruction proposal.
  Created the research with 45 primary sources, a conditional library shortlist,
  and the language-neutral proposal with tool contracts, a workflow diagram,
  source routing, verification/delivery rules and Go/Python/Node mappings.
- [x] R4: Check affected artifacts and review coverage against the request.
  Artifact, source-reference, embedded-JSON and new-file whitespace checks passed.
  Scoped review covered all named frameworks, language neutrality, source routing,
  tool contracts, finite repair paths, authorization, recovery and delivery.
- [x] R5: Apply the user's clarification that the sequence is an example.
  Both documents now make stage selection and complexity depend on application
  goals. Added examples ranging from a direct lookup to cross-source research;
  scoped state and tracing requirements to the stages actually present.
  Artifact, whitespace and renamed-section reference checks passed.
- [x] I1: Publish the accepted policies with one owner per concern.
  Created six entry profiles (`rag`, `llm-tools`, `llamaindex`,
  `langchain`, `langgraph`, `langfuse`); shared `standards/llm/` topics own
  architecture, library selection, answer checks and evaluation. RAG
  ingestion/retrieval is separate from tool contracts, source access, execution and
  workflows. Replaced the proposal's duplicated rules with an implementation map;
  preserved the dated research and its evidence limits. Integration checks remain I3.
- [x] I2: Register profiles and connect discovery/adoption.
  Updated `standards/catalog.toml`, `standards/catalog.md`, `README.md`,
  `MIGRATION.md` and the conditional passport fields. Core selects no AI profile;
  RAG/tools depend on core, LlamaIndex makes RAG/tools available, LangChain and
  LangGraph make tools available, and Langfuse remains independent. Languages,
  storage and sibling frameworks are separate choices. Existing `$routes`
  template expansion supplies selected native entry routes without new checklists.
- [x] I3: Verify the integration and review the completed scope.
  Extended profile-selection checks for optional/language-neutral closure and
  Go/Python/Node composition. All 41 tests, strict typing, 24 artifact checks,
  30 prepared-bundle cases and JSON/whitespace checks passed. Coordinator review
  initially found no unresolved in-scope defect; source/runtime claims remain separate.
  Reopened after R6 identified IR1 and IR2 below, then closed after R7 applied the
  corrections and passed the affected checks. Unchanged structural evidence remains valid.
- [x] R6: Independently review logic, correctness and wording clarity.
  Complete. The user explicitly requested a Superpowers independent review
  and chose a one-off reviewer using `gpt-6-astra` / `max`. The coordinator launched
  one direct read-only reviewer; no further delegation or configuration writes
  were authorized. Instruction contents were preserved during the review.
  Returned two P2 findings and two optional wording improvements, with no critical
  blocker. Coordinator validated the findings against the affected rules and
  primary sources. Corrections were subsequently authorized and applied under R7.
- [x] R7: Apply all four independent-review improvements.
  Complete, explicitly authorized by the user, including the optional wording
  suggestions. Corrected uncertain-effect retries, evidence-unit deduplication,
  offline-dataset applicability and non-chat graph ownership in their existing
  owners. Reused the primary-source checks from R6. Pre-edit copies of the four
  policy files and this plan are in `/tmp/aek-rag-review-fixes-38rq66tv`.
  Scoped diff review, affected links/artifacts and untracked-file whitespace
  checks passed; unchanged catalog/test inputs did not require another full cycle.

## Integration constraints and review focus

- Implement the accepted design in the current checkout as one coherent stage;
  keep the existing catalog schema and profile IDs compatible.
- Keep English policies portable without mandatory research copies. Shared topics
  are catalog resources, not extra required profiles or a recursive reading queue.
- Select workflow stages by goals; preserve dependencies, permission boundaries,
  evidence requirements and bounded completion rather than enforcing one sequence.
- Inspect generic tools without RAG, tracing without graph/frameworks, and Go or
  Node work without an implicit Python service. Verify the selected copy contains
  reachable rule links and omits unselected framework entries.
- Review preservation of source authority/freshness, access revocation, ambiguous
  effects, cancellation, citation support and conditional streaming/verification.
- Reuse the 2026-10-29 source research; introducing runnable SDK examples or new
  unverified framework claims is outside this integration.

## Verification and handoff

Executed for the three new documents after the content corrections:

```sh
python3 tools/check_instruction_artifacts.py docs/plans/2026-10-29-rag-tools-research.md docs/research/2026-10-29-rag-tools-engineering.md docs/specs/2026-10-29-rag-tools-instructions.md
git diff --check
```

Results: **3 artifacts checked, 0 errors**; whitespace diff check passed. Because
the files are new/untracked, a separate standard-library inspection checked all
three for whitespace/final-newline issues, checked unique bibliography IDs and
the proposal's source references, and parsed its JSON block: **45 unique sources,
1 valid JSON block, 0 issues**. This does not establish runtime behavior or render
the Mermaid diagram. No framework runtime tests or retrieval benchmarks were run.

After R5, reran the artifact checker: **3 artifacts checked, 0 errors**. Checked
all three documents for whitespace/final-newline issues and searched documentation
for obsolete references to the renamed sections: **0 issues**. Reviewed the scoped
diff against the preserved pre-clarification files.

## Integration evidence

The following checks cover the integrated catalog, rules and adoption routes:

- Artifact checker over the 24 Markdown/TOML paths in the integration baseline
  manifest: **24 artifacts, 0 errors**. Log:
  `/tmp/aek-rag-integration-baseline-9x1ub0v_/artifact-check.log`.
- `python3 -m unittest discover -s tests -p 'test_profile_selection.py'`:
  **41 tests passed**, including three added optionality/composition checks.
- `python3 -m mypy --strict --disallow-any-explicit --disallow-any-unimported --python-version 3.11 --explicit-package-bases --cache-dir /tmp/aek-rag-mypy-cache tests/test_profile_selection.py`:
  **no issues in 1 source file**.
- Prepared each of the six profiles alone, plus Go RAG/tools, Python LlamaIndex,
  Node.js/TypeScript RAG/LangChain/LangGraph/Langfuse and Go Langfuse, in contained,
  flat and custom layouts: **30/30 passed**. Checked selected catalog resources,
  Markdown links and generated root profile routes without research/history copies.
  The existing fixed fixture did not classify Node's conditional NestJS link; the
  first attempt stopped there. After confirming that source condition, the temporary
  harness classified that exact omitted route without changing source requirements
  or the fixture file. Results:
  `/tmp/aek-rag-integration-baseline-9x1ub0v_/prepared-bundles.json`.
- `git diff --check` passed. Separate inspection of all 25 scoped paths found
  **0 whitespace/final-newline issues**; the illustrative tool schema parsed as
  **1 valid JSON block**.
- Coordinator review compared tracked edits and all new policies with the preserved
  pre-stage files. A prose-move comparison identified only four intentional wording
  adaptations: simpler direct operations, conditional responsibility owners, the
  LlamaIndex evidence reference and the shared verification-policy reference.
  Reviewed rule ownership, conditional reading, source/access boundaries, bounded
  effects, citation support and the explicitly illustrative workflow; no material
  in-scope finding remains. No independent reviewer was dispatched for this
  documentation/catalog integration.

These are instruction artifact and preparation checks, not framework runtime,
model-quality, production-retrieval or native-client activation evidence.
The final status-only edits to this plan/design map do not invalidate those results.

## Independent review scope and assignment

User-requested review concerns logic, correctness of wording and clarity of the
integrated RAG/tool policies, their conditions and catalog/adoption interactions.
Review current local files, including new/untracked files; a commit-only diff
would omit the main instructions. Reuse I3's valid structural evidence without
claiming it proves semantics. Inspect primary documentation only to settle a
concrete technical doubt; no application execution or paid APIs are required.

Review input snapshot and hashes:
`/tmp/aek-rag-independent-review-j_r0kzrj/manifest.json` and its `snapshot/` tree.
The earlier integration baseline remains
`/tmp/aek-rag-integration-baseline-9x1ub0v_`. This plan's status updates are outside
the policy content being reviewed. The coordinator owns this record; the reviewer
returns findings without modifying it or the instructions.

One-off role assignment: reviewer enabled for this task, direct coordinator →
reviewer edge, one concurrent worker, no child edges; requested model/effort
`gpt-6-astra` / `max`, explicitly chosen by the user. Fresh context is required.
The native collaboration tool controls execution; the requested pair is not a
claim of independently observed backend-model telemetry. No persistent routing
or native-role files are being created.
Reviewer worker: `/root/rag_instruction_review`, launched with fresh context;
assignment is complete. The reviewer checked all 16 policy files, the six tracked
integration changes and the task/design/research records. It reported all 24 frozen
inputs other than this coordinator-owned plan unchanged against the review snapshot.
No policy files, Git state or configuration were changed during the review.

## Independent review findings

R6 assessment before corrections: **needs focused corrections**, with two P2 findings and no critical
blocker. The coordinator accepts both findings. Both wordings were inherited from
the pre-integration proposal rather than introduced by moving rules to their owners.

### IR1 — Condition the prohibition on retrying an uncertain send

R6 snapshot location: [tool execution](../../standards/llm-tools/execution.md), lines 24–26.
Requiring reconciliation before every retry and categorically prohibiting a retry
after a lost receipt also prohibits a provider-supported safe replay. A lost
response can be recovered by repeating the same persisted request/key under a
still-valid downstream idempotency guarantee. The current wording can leave a
recoverable operation unnecessarily uncertain or require manual intervention.

Primary counterexample checked on 2026-10-29:
[Resend idempotency contract](https://resend.com/docs/dashboard/emails/idempotency-keys)
supports same-request replay without another send within its documented validity
window. This is evidence against a universal prohibition, not a service selection.

English recommendation recorded during R6, addressed by R7:

> Treat a lost receipt as an unknown outcome. Retry only under a verified downstream
> idempotency guarantee using the same persisted key and payload within its validity
> window, or after reconciliation establishes that retry is safe. Otherwise, do not
> automatically resend.

### IR2 — Define the evidence unit used for retrieval deduplication

R6 snapshot location: [retrieval](../../standards/rag/retrieval.md), lines 22–23, with
[ingestion identity](../../standards/rag/ingestion.md), lines 7–8.
Stable identity/version is underspecified: ingestion names document IDs but
retrieval does not distinguish those from chunk/record identity. Deduplicating by
document ID and version can discard a second relevant passage from the same
document, such as an exception to an instruction retained from the first passage.
This is a plausible ambiguity in executable guidance, not an observed runtime bug.

[LlamaIndex documents and nodes](https://developers.llamaindex.ai/python/framework/module_guides/loading/documents_and_nodes/),
checked on 2026-10-29, distinguishes documents from their constituent nodes/chunks.
The library-neutral policy should make that distinction explicit.

English recommendation recorded during R6, addressed by R7:

> Deduplicate repeated instances of the same evidence unit across retrieval branches,
> using source/version plus chunk or record identity—or an equivalent stable locator.
> Preserve distinct relevant passages from the same document; document-level diversity
> limits are a separate selection policy.

### Optional wording improvements accepted and applied in R7

- [Evaluation](../../standards/llm/evaluation.md), line 14: prefix the dataset
  requirement with "For offline quality evaluation" so a tracing-only task does
  not appear to require a new question dataset. Existing task-relevance rules
  already support this interpretation; this is an explicitness improvement.
- [LangGraph](../../standards/langgraph.md), lines 24–26: bind thread ownership
  to the authenticated owner and relevant conversation, job or workflow instance.
  "Authenticated conversations" is unnecessarily chat-specific for non-chat graphs.

### Review limits and acceptance

No additional material defect was found in profile optionality, language
independence, flexible sequencing, policy ownership, tool-result scoping, access
revocation, bounded completion or conditional streaming. Existing I3 evidence was
reused rather than rerun for reviewer freshness.

Not assessed as runtime claims: installed SDK interoperability, retrieval quality,
performance, model behavior, end-to-end authorization/prompt-injection resistance,
general checker correctness and native-client activation. No target application
exists in this review. Those limits do not waive the two wording findings.

## R7 correction evidence and outcome

- IR1 is resolved in `standards/llm-tools/execution.md`: uncertain actions/sends
  can be retried under the verified downstream guarantee with the same persisted
  key/payload within its validity window, or after reconciliation establishes
  safety. Authorization, cancellation and shared limits remain binding. The
  LangGraph wording prohibits duplicating an external effect, preserving safe replay.
- IR2 is resolved in `standards/rag/retrieval.md`: deduplication operates on an
  individual evidence unit; distinct passages from one document and independent
  sources are preserved. Document diversity is a separate selection decision.
- Both optional improvements are applied: dataset creation/reuse is conditional
  on offline quality evaluation; graph threads belong to the authenticated owner
  and the applicable conversation, job or workflow instance.
- Ran `python3 tools/check_instruction_artifacts.py standards/llm-tools/execution.md standards/rag/retrieval.md standards/llm/evaluation.md standards/langgraph.md docs/plans/2026-10-29-rag-tools-research.md`:
  **5 artifacts checked, 0 errors**. Separate whitespace/final-newline inspection
  of those five files found **0 issues**; these files are untracked, so a tracked
  Git diff alone would not cover them.
- Coordinator reviewed the scoped pre/post diff and matching rules in RAG/tool
  topics. Safe replay and unknown outcomes, evidence-unit retention, dataset
  applicability and non-chat ownership are consistent with their existing owners
  and acceptance scenarios. No unresolved in-scope finding remains.
- Reused R6's verified primary sources and the earlier checks for unchanged
  catalog selection, dependency routes and Python tests. No new independent
  reviewer, SDK execution, model evaluation or full-suite rerun was required.

Current stage status: **complete; all four review improvements applied and checked**.
I1–I3 and R6–R7 are complete. No dependency installation, downstream project change,
or push was performed. The user authorized the local commit as a separate Git
handoff after these checks; its identity is recorded in repository history.
