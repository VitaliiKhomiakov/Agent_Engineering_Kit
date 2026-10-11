# Development feasibility: personal utility before new infrastructure

**Checked:** 2026-10-07.
**Addendum:** 2026-10-08, sandbox feasibility and read-only environment preflight.
**Scope:** Repository inspection and primary-source review. No target-client
pilot, external evaluation run, Context7 query, service installation or consuming
project change was performed. This is a proposal, not evidence of measured AEK
benefit. Portfolio decisions and progress belong to the
[development roadmap](../plans/2026-10-07-development-roadmap.md).

## Intended use and evaluation question

The owner wants better everyday work with coding agents first; reuse by other
developers is a secondary opportunity. Evaluate additions against this question:
does a small, maintainable change remove a demonstrated source of mistakes or
repeated work without introducing a larger recurring burden?

During this assessment, the owner clarified that no critically important problem
has been noticed and no very deep analysis has yet been performed. Consequently,
there is no established demand for a new diagnostic, retrieval layer or service.
The first recommendation is observation during normal work, not a feature build.

The accepted [library scope](../specs/2026-09-20-agents-framework.md) removed a
separate application, adapters and CLI. New tooling is not inherently forbidden,
but recreating that product is not the default response to this request.
No current session transcripts or target-project outcomes were supplied for this
assessment. Described failure modes are hypotheses unless tied to inspected files.

## Current capability and remaining uncertainty

Baseline: `a725cf28cb4e399e64c13dc421e63ea7cc4ae580`.
The catalog has 35 profiles, seven marked required. `standards/` contains 182
Markdown files; file/line counts describe the library, not per-task context cost.
The source artifact checker returned `Checked 206 artifacts; 0 error(s).` during
the preceding investigation in this session, before this document set was added.

| Concern | Existing owner/capability | Actual gap or uncertainty |
| --- | --- | --- |
| Select applicable rules | [Catalog reading contract](../../standards/catalog.md#read-for-the-current-task), profile task tables and target entries | No measured evidence that another selector would outperform these routes |
| Safe adoption/update | [MIGRATION](../../MIGRATION.md#prepare-and-apply), integration skill and accepted contents | An explicit read-only health-check entry is absent; usefulness as a repeated operation is unmeasured |
| Preserve local modifications | [B/C/N comparison](../../MIGRATION.md#repeat-and-update) and recovery contract | Semantic impact can be explained within the existing proposal; no separate update engine is needed |
| Validate artifacts | Python checker, policy validation and selected-profile tests | These do not observe discovery, adherence or user outcome; the documented limitation is intentional |
| Measure real use | [Bounded pilot](../../MIGRATION.md#phase-4-bounded-pilot) already defines measures and boundaries | README records no completed post-change live pilot; reusable scenario/report support is a modest addition |
| Investigate a bad session | Superpowers `diagnosing-superpowers`, when that plugin and suitable transcript access are available | A new session-debugging product would overlap; adoption facts can complement that skill |
| Record versions/evidence | Dated research, example reproduction and explicit evidence limits | Maintaining a second source-freshness database has no demonstrated return |
| Plans and resumption | Canonical task policy and existing OpenSpec/Spec Kit compatibility | Another planner or task database would duplicate established ownership |

## Primary research: usefulness is not automatic

**Gloaguen et al., revision 3, 2026-09-29.** The study evaluates context files
on SWE-bench Lite and CTXbench. It reports no general improvement in success and
over 20% average inference-cost growth. Its analysis associates instructions with
more testing and exploration. The evaluation focuses on Python; success-rate
results do not establish effects on all architectural, security or collaboration
requirements. These results do not measure AEK or the owner's current model.
They justify testing incremental guidance, not deleting mandatory constraints.
[Paper and limitations](https://arxiv.org/html/2602.11988v3).

**Lulla et al., revision 2, 2026-03-30.** Across 124 pull requests in ten
repositories, the study reports lower median runtime and output-token use with
AGENTS.md. It explicitly leaves comprehensive semantic correctness evaluation
out of scope, using a manual sanity check instead. This supports a possible
efficiency benefit but does not establish better code or guaranteed total-cost
savings. [Paper and methods](https://arxiv.org/html/2601.20404v2).

**Local inference:** Different tasks, contents and measurement designs can yield
different outcomes. Neither paper supports a universal instruction-length limit,
an AEK savings percentage, or a claim that a new skill must help. Measure task
acceptance and contract preservation before interpreting efficiency. A small
personal pilot is directional evidence, not a general benchmark result.

## Reusable ideas from existing projects

These are documented capabilities reviewed on the date above, not locally tested
integrations. Moving documentation must be rechecked before implementation of an
affected API or client-specific contract.

| Source | Relevant documented idea | Appropriate AEK reuse and limit |
| --- | --- | --- |
| [Context7 API guide](https://context7.com/docs/api-guide) | Task-oriented retrieval and version-specific context; direct search and explicit library selection are available | Use the existing service for a demonstrated documentation question; confirm source/version match and keep retrieval optional |
| [Context7 team rules](https://context7.com/docs/howto/rules) | Global and library-specific rules accompany retrieved docs; Pro/Enterprise feature | Inspiration for scoped guidance, not a replacement for local authority, task permissions or AEK conditions |
| [Context7 library configuration](https://context7.com/docs/library-owners) | `context7.json` controls included/excluded sources and versions; root Markdown is included by default | A later distribution experiment would need explicit exclusions for source-maintenance instructions/history and retrieval-quality checks |
| [Ruler](https://github.com/intellectronica/ruler) | Central rules, client distribution and dry-run previews; combined rule output | Reuse the usability idea. A new installer, unconditional concatenation and parallel ownership would conflict with AEK's present design |
| [Anthropic skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | Baseline/candidate runs, verifiable expectations and variance reporting | Use comparable runs and evidence-backed grading; no need to copy its execution machinery or mandatory run cadence |
| [Promptfoo coding-agent evaluation](https://www.promptfoo.dev/docs/guides/evaluate-coding-agents/) | Evaluate an actual agent harness and inspect intermediate actions as well as outputs | Optional later automation if manual repeated runs become a burden; do not add an SDK or service to a documentation library now |
| [Spec Kit analyze](https://github.github.com/spec-kit/reference/agentic-sdd.html) | Read-only consistency checks across requirements, plan and tasks | Reuse the checking principle under existing artifact owners; no second planning system |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) | Scenario-based requirements and change artifacts | Preserve existing native task stores; no migration merely to conduct this pilot |
| [Serena](https://github.com/oraios/serena) | Symbol-level code navigation and editing | Consider for a target codebase with a demonstrated navigation problem, not as an AEK source-library dependency |

## Candidate decisions and cheapest alternatives

Effort categories are relative scope estimates, not delivery dates or measured
cost. Every live run remains subject to its selected task and resource envelope.

| Candidate | Decision | Cheapest useful form | Burden / rejection condition |
| --- | --- | --- | --- |
| Observe one real task | Recommend first | Existing client's normal task plus a compact evidence report | Low extra setup; stop at an honest result if traces are insufficient |
| Reusable pilot scenarios/report | Specify now | Markdown protocol and optional case templates | Small documentation change; do not create a large cross-stack fixture suite |
| Controlled comparison | Conditional on an observed problem and one candidate fix | Same task/state/client/model with current and candidate instructions | Model runs cost time/resources; reject aggregate efficiency claims if quality or comparability is unknown |
| Read-only adoption diagnosis | Specify as a conditional workstream | One manual report using existing owners/checker | Low implementation, ongoing format/client drift; do not repeat before every coding task |
| `aek-doctor` skill | Conditional packaging after useful diagnosis | Thin opt-in source skill, no new policy engine | Extra discovery metadata/overlap; defer when direct procedure access is sufficient |
| `aek-context` skill | Defer | Existing entry/task routes; correct the affected route if it fails | Another selector can repeat reading, omit conditions or disagree with owners |
| Own context MCP/vector index | Do not schedule | Local Markdown/search, optional existing Context7 | Runtime, indexing, transport and provenance burden without a measured retrieval problem |
| Semantic update summary | Fold into existing integration only when needed | B/C/N proposal with rule, affected scope and retained exception | Do not create a second version/ownership record or new update skill |
| Background freshness monitor | Defer | Recheck official affected contracts on change as already required | Notifications and source churn without demonstrated version failures |
| Rule ablation | Conditional controlled experiment | Change one optional instruction or route in a disposable pilot treatment | Never disable mandatory project gates/permissions; do not auto-edit accepted standards |
| Public packaging/Context7 listing | Defer until personal reuse works | Sanitized examples and documented source-skill use | Publishing, support, indexing and compatibility become ongoing work |

## Alternatives considered

**A — use the current library unchanged.** Lowest maintenance cost and a valid
outcome if ordinary work exposes no meaningful problem. It leaves the uncertainty
about benefit unresolved but creates no new burden.

**B — evidence first, minimal reusable support. Recommended.** Observe one actual
task, diagnose a specific adoption problem if present, and compare one proposed
correction only when necessary. Package a procedure as a skill after evidence of
reuse. Preserve current rule ownership and existing tools.

**C — tool platform first.** Implement a resolver, doctor CLI, MCP, telemetry and
automatic updates together. This creates dependencies and multiple sources of
truth before the user's bottleneck is known. It is not justified for this scope.

## Decision gates

- **Pilot gate:** Select one target/client and an ordinary bounded task with
  independently checkable acceptance; obtain the actual execution scope first.
- **Comparison gate:** Identify an observed problem and one candidate change.
  Baseline and treatment retain the same binding user requirements and gates.
  If no improvement hypothesis exists, finish the observation without an A/B run.
- **Diagnostic gate:** A specific adoption uncertainty or recurring health-check
  need must exist. Perform the smallest manual inspection before adding a skill.
- **Packaging gate:** The diagnostic yields a verified actionable finding, or a
  useful evidence-backed clean report, and a recurring reuse case exists. A
  one-off need can remain an ordinary procedure without `aek-doctor`.
- **Automation gate:** Repeated measured manual effort and stable inputs must
  justify automating one operation. A new MCP/backend requires its own design.
- **Rollout gate:** All binding acceptance checks pass; the owner reviews the
  benefit/burden tradeoff and explicitly selects adoption beyond the pilot.

Unknown outcomes remain unknown. Failing to demonstrate benefit is a valid
reason to stop; it does not reopen accepted historical stages or authorize a
replacement feature. The proposed specifications define concrete acceptance and
stop conditions without treating this research as runtime evidence.

## Sandbox feasibility addendum — 2026-10-08

**New input:** The owner created
`/home/vitalii/Documents/Local_Projects/AEK_TEST` and allowed a freely selected
technology combination for tests, either scheduled or provisioned as the final
step. This continuation selects scheduling. Read-only inspection found an empty
directory and Python 3.12.3 available. FastAPI, Pydantic, Starlette, HTTPX, pytest
and Uvicorn distributions were absent from the inspected interpreter; other
virtual environments were not inventoried. Nothing was installed or deployed.

**Decision:** Use one Python 3.12/FastAPI/Pydantic v2 reservation API. A pure
domain module and thin HTTP boundary expose incorrect coercion, stock/state
invariants, incomplete tests and unnecessary architecture. An idempotent
cancellation task provides independently checkable behavior beyond a health
endpoint. This is a plausible diagnostic substrate, not a measured AEK benefit.

| Alternative | Judgment for this investigation |
| --- | --- |
| Pure Python function | Cheapest for typing/domain checks, but cannot assess HTTP/Pydantic integration or routing among these profiles |
| Python + FastAPI + Pydantic | Selected: installed Python, bounded HTTP/domain boundary, no external infrastructure |
| Database-backed or frontend/backend application | Adds migration, service and build variables without a current question requiring them; defer |
| Multiple language/framework fixtures | Larger maintenance and interpretation burden; add only to reproduce a concrete uncovered issue |

The source library already contains stack rules and historical example evidence.
The sandbox's incremental purpose is an independent adopted target and fresh
task observation, not duplication of every existing technology check. The seed
can be reused for diagnostic copies; no permanent source fixture suite or new
catalog resource is warranted at this stage.

### Official contracts reviewed for the proposed setup

- [Python 3.12 venv documentation](https://docs.python.org/3.12/library/venv.html)
  describes isolated environments. Use per-project environments and reproduce
  them from recorded dependencies, not by copying environment directories.
- [FastAPI testing guide](https://fastapi.tiangolo.com/tutorial/testing/)
  describes its Starlette/HTTPX TestClient and pytest use. In-process HTTP tests
  are sufficient for the selected request/response contract; no running server
  or Uvicorn installation is necessary for this fixture's acceptance.
- [FastAPI lifespan testing](https://fastapi.tiangolo.com/advanced/testing-events/)
  describes using TestClient as a context manager to run lifecycle handling.
- [Pydantic strict-mode documentation](https://pydantic.dev/docs/validation/latest/concepts/strict_mode/)
  describes strict validation and Python/JSON differences. Validate actual HTTP
  input as well as pure domain behavior; do not infer the HTTP contract solely
  from a direct model-validation call.

These are documentation reviews, not an executed compatible package matrix.
FastAPI/Pydantic pages are moving references; the attempted version-specific
Pydantic page and FastAPI source-page retrieval did not yield usable content.
Before installation, verify exact candidate releases and dependency contracts,
pin the resolved environment and record the actually tested versions. No update
to the source library's historical examples is implied. Context7 remains optional
for a later version-sensitive question, not required to set up the sandbox.

### Benefit and overengineering gate

The owner-supplied directory reduces risk to real projects and makes reproduction
easier. It does not supply a real user bottleneck. Provision one seed, observe
one cancellation task, and stop at a reasoned outcome before adding infrastructure.
Repeated cancellation must restore stock only once; malformed requests must leave
state unchanged. These are meaningful correctness checks rather than token-count
proxies. Passing them proves only the checked application's behavior.

Keep setup evidence, a fresh-session observation and any controlled comparison
distinct. A synthetic broken route can test diagnostic correctness but cannot
establish recurring demand for a new skill. Before promoting a claimed everyday
improvement, check it on a suitable ordinary task. If there is no material finding,
retain the library and leave doctor/context/MCP development deferred.

## Execution requirement update — 2026-10-08

During authorized setup the owner required all project execution in Docker.
This supersedes the host-venv proposal and the earlier decision to omit containers.
Docker Compose now runs the API, tests and analyzer; Uvicorn adds a real HTTP
listener to the selected fixture. This is a user requirement, not a benefit claim
or a reason to add unrelated database/frontend services.

The prepared package set uses FastAPI 0.138.0/Pydantic 2.13.4 and resolved
Starlette 1.7.0/HTTPX2 2.13.1. Official release pages and installed package metadata
were checked; [Starlette 1.7.0](https://pypi.org/project/starlette/1.7.0/)
documents HTTPX2 for TestClient. The [Compose service contract](https://docs.docker.com/reference/compose-file/services/)
and [up/wait command](https://docs.docker.com/reference/cli/docker/compose/up/)
inform runtime configuration and bounded readiness checks. Actual commands,
versions, corrections and results belong to the execution plan and sandbox
evidence; these source reviews do not establish a completed pilot.


## Skill library assessment — 2026-10-11

**Current decision: create no new skills in this stage.** Retain the three
existing inactive AEK skill templates and reuse applicable Superpowers procedures.
Specialized skills below are conditional future options, not scheduled deliverables.

**Subsequent scope clarification, 2026-10-11:** The statement above records the
completed observation stage. The owner subsequently requested design and planning
for skills distributed into consuming projects. The [new specification](../specs/2026-10-11-project-skills-reorganization.md)
defines that proposed reorganization and its verification gates. This does not
retroactively establish skill efficacy in the earlier pilot or start implementation.

The owner asked whether AEK needs skills for languages, technologies, architecture,
coding and review. Keep the existing technology rules as authoritative reference
owners; reuse Superpowers for development procedures. Add an AEK skill only when
it packages a recurring task with distinct inputs, steps and acceptance that these
owners do not already make convenient. This is a recommendation, not authorization
to create or activate a skill library.

### Current source inventory

AEK already contains three inactive skill templates: `aek-integrate-project`,
`aek-model-setup` and `aek-model-reassign`. Each routes to a procedure owner.
Technology entries provide essentials and task-specific reading tables, while
Superpowers adaptations select design, implementation, debugging and review
procedures. Creating separate generic Python/FastAPI/coding/review skills would
add overlapping routing and maintenance rather than an established capability gap.

### Vendor evidence

| Source checked on 2026-10-11 | Documented recommendation | AEK implication |
| --- | --- | --- |
| [OpenAI skill guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | Narrow skill triggers, short discovery descriptions, progressive disclosure and conditional reading; accumulated recipes can overconstrain newer models | Do not install a broad catalog of generic skills by default. Its model-specific observations are not universal performance guarantees |
| [OpenAI skill construction](https://learn.chatgpt.com/docs/build-skills) | Metadata supports discovery; the full skill loads when selected | Evaluate selection separately from task execution |
| [OpenAI review rules](https://developers.openai.com/blog/custom-code-review-rules-for-codex) | Scoped, consequential repository invariants belong in AGENTS.md; mechanical checks belong in CI; test triggering, safe and unrelated examples | A separate review skill is not required merely to apply project rules during review |
| [Anthropic extension guide](https://code.claude.com/docs/en/features-overview) | Distinguishes persistent instructions, path-specific rules, on-demand skills, isolated subagents and hooks | Choose packaging by loading/operation needs rather than creating one skill per technology or role |
| [Anthropic skills](https://code.claude.com/docs/en/skills) | Skills can hold reference knowledge or an explicit procedure; isolated execution needs an actionable task | A language knowledge skill is possible, but it is not mandatory and must not duplicate AEK's source of truth |
| [OpenAI skill evaluation](https://developers.openai.com/blog/eval-skills) | Assess skill behavior with explicit expectations and recorded runs | Verify both appropriate activation and useful output before rollout |

The vendor documentation does not establish that every architecture, coding or
review task needs its own skill. Skills also do not create permissions, guarantee
instruction adherence or make an assessment independent. Client-specific metadata
and discovery behavior need validation in the selected installed client.

### Recommended allocation

| Concern | Owner now | Condition for a new skill |
| --- | --- | --- |
| Language/framework rules | Existing standards and profile task routes | Repeated discovery failure that cannot be fixed by a smaller route correction; optional thin entry must keep the same authoritative content |
| Architecture | Architecture/passport and core rules, plus Superpowers brainstorming for a design change | A recurring specialized result, such as a compatibility assessment across services, with distinct acceptance |
| Ordinary coding | Task acceptance, stack rules, existing project checks and applicable Superpowers execution/debugging | A concrete repeatable procedure such as an expand/contract schema migration or framework-version migration |
| Code review | Verification owner, project-specific invariants and Superpowers review procedure when warranted | A specialized review with a distinct failure model, such as API backward compatibility, permissions or database rollout |
| Framework adoption and model setup | Existing three inactive templates and their procedure owners | Improve demonstrated problems in those entries rather than creating competing installers |
| Agent observation/diagnostics | Existing pilot/diagnostic plans | Repeated useful manual operation that warrants convenient invocation; the existing gates still apply |

Names such as `aek-api-compatibility-review` or `aek-database-migration` are examples
of possible future boundaries, not planned files or approved implementations.
Do not multiply a language-by-phase matrix of skills. A chosen procedure should
select only the relevant technology references; a generic Python edit must not
trigger database, deployment or architecture-migration workflows.

Before introducing a candidate, define its trigger and non-triggers, inputs,
authoritative references, observable output, supported client/version and checks.
Compare a matching task, a safe counterexample and an unrelated task. Test missing
inputs and a conflict with local instructions. Use current behavior as baseline,
change one candidate at a time, preserve mandatory rules and inspect outcomes.
Measure unnecessary activations, missed activations, material defects and human
corrections; time/token comparisons require comparable runs and real telemetry.
Treat a model's preference for its own output as insufficient evidence of benefit.

### Evidence from the selected pilot

The 2026-10-11 unblinded cancellation run used the existing adopted instructions
and installed Superpowers procedures. All 38 domain/HTTP tests and strict mypy
passed, and a separate real HTTP probe checked twelve concurrent cancellations,
stock preservation and the public contract. No new AEK technology/coding/review
skill was added. This establishes feasibility for one task; it does not isolate
AEK or Superpowers contributions or compare alternative skills.

The source [pilot outcome](../plans/2026-10-07-agent-behavior-pilot.md#stage-a-completed-in-unblinded-mode--2026-10-11)
retains the fixture description, task contract, observed versions, check results
and evidence limits inside AEK; the pilot plan owns progress. This record remains
understandable after deletion of the disposable workspace, although raw logs are
not archived here. The model/client version, effort, native loading and token-cost
evidence remain unknown. Keep these limits when deciding whether to add a skill
or claim efficiency improvements.
