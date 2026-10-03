# Engineering practices research and adoption

> **Completed and accepted by the user on 2026-09-22.** K01–K19 and the return to
> the rules-only scope are accepted as the finished current part. No work remains
> authorized under this plan. Future improvements require a separate part/version
> and its own specification/plan, referencing this accepted baseline.

> **Current scope, 2026-09-22:** K01–K19 engineering rules remain complete. The
> user explicitly requested removal of the entire additional Python application,
> its tests, schemas and packaging while keeping orchestration rules, instructions
> and native templates. Earlier references to P1–P7, APIs and their checks below
> are historical. They do not require rebuilding or completing the removed app.


> Historical execution guidance for the completed stages: use Superpowers for
> the actual research, planning, and verification needs under
> the [workspace adaptation](../../standards/superpowers.md). Execute one topic
> inline by default, complete its necessary checks, and follow the current
> authorization below for delegation and checkpoints.

**Goal:** build a researched, practical engineering knowledge base for every
language, framework, and technology already covered or recognized by AgentsFramework.
Short code examples illustrate the resulting practices; they do not define the
scope of the research or substitute for architecture and engineering guidance.

**Design:** research one topic at a time, reconcile its findings with existing
shared policy, and deliver an adoptable profile with a short entry, conditional
topic files, optional examples, and traceable evidence. Keep research notes
separate from instructions loaded by agents. Retain one owner per shared rule.

**Stack:** English Markdown rules/research, the existing TOML rule catalog, and
manually adopted templates. Executable examples use the topic's tools.

**Spec:** the design and acceptance criteria below refine the existing
[product specification](../specs/2026-09-20-agents-framework.md). The user's
2026-09-21 clarification requires material for the full supported stack, developed
sequentially, beyond the short Go example discussed in the conversation.

## Historical status and authorization

The user approved this plan and sequence on 2026-09-21. K01, Go research and
adoption, is complete; the user authorized K02 on 2026-09-21. K01's inline
execution includes the user's clarification about limiting context through
conditional sections and optional examples. K02, Gin, is complete; the user
authorized the next stage on 2026-09-21. K03, Python, is complete; the user
authorized K04 on 2026-09-21. K04, Pydantic, is complete; the user authorized
K05 on 2026-09-21. K05, FastAPI, is complete; the user authorized K06 on
2026-09-21. K06, PHP, is complete; the user accepted its review and authorized
K07 on 2026-09-21. K07, Symfony, is complete; the user authorized K08 on
2026-09-21. K08, Doctrine ORM/DBAL, is complete; the user authorized K09 on
2026-09-21. K09, JavaScript, is complete; the user accepted its review and
authorized K10 on 2026-09-21. K10, TypeScript, is complete; the user authorized
K11 on 2026-09-21. K11, Node.js, is complete; the user confirmed its review and
authorized K12 on 2026-09-21. K12, NestJS, is complete; the user accepted its review and authorized K13 on
2026-09-21. K13 React is complete; the user accepted its review and authorized K14 on
2026-09-21. K14 Next.js is complete; the user accepted its review and authorized K15 on
2026-09-21. K15 PostgreSQL is complete; the user accepted its review and authorized K16 on
2026-09-21. K16 SQLAlchemy is complete; the user authorized K17 on 2026-09-21.
K17 psycopg is complete; the user authorized K18 on 2026-09-22.
K18 Docker is complete and accepted. On **2026-09-22** the user authorized K19
and the remaining named native-adoption stages through bounded subagents using
**gpt-6-astra / high**, with implementer checks and concise coordinator integration
review, without intermediate human checkpoints. K19 is complete; the native
plan owns authorization details and progress for its stages.
The Go example starts the investigation;
the common coverage below defines its breadth. The sequence can change with
user priorities.

This document owns practice-research progress. The
[native adoption plan](2026-09-20-native-client-adoption.md) retains ownership of
P3–P7; their current state is recorded there. K01–K18 used sequential topic
checkpoints. The explicit 2026-09-22 bulk authorization replaces intermediate
checkpoints for K19 and the named remaining native stages, retaining scope and
no-Git/external-write limits.

Workspace: `/home/vitalii/Documents/Local_Project/AgentsFramework`, outside Git.
Work in the current directory. Preserve each stage's baseline before edits;
do not stage, commit, create worktrees, or install into external projects as
routine bookkeeping. The planning baseline covers this new document and the
native plan before its navigation update:
`/tmp/af-practices-plan-bafdnidm/baseline.json`.

The 2026-09-22 task-specific assignment is gpt-6-astra / high for the authorized
bounded subagents. It does not install a workspace/global model configuration;
earlier topic research proceeded inline. Example model names remain nonbinding.
Use the existing [work-mode](../../standards/work-modes.md) and
[verification](../../standards/verification.md) policies throughout.

## Research design and boundaries

The [catalog](../../standards/catalog.toml) started with 17 profiles; K16 adds a
conditional SQLAlchemy profile and K17 adds psycopg, bringing it to 19. Some combine
several subjects: Go/Gin, Python/FastAPI, PHP/Symfony/Doctrine, and Next.js/React.
Research can address these subjects separately without immediately splitting
their installed profile IDs. Pydantic already has guidance within Python;
SQLAlchemy and psycopg were recognized by the former application
(`src/agents_framework/metadata.py`, now removed). K16 adds the dedicated
SQLAlchemy profile and K17 adds the psycopg profile. These remain conditional
on the actual dependency or explicit selection.

Keep these forms of material:

- `docs/research/2026-09-21-<topic>-engineering-practices.md` for evidence,
  alternatives, version applicability, rejected recommendations, and decisions.
  Use the actual research start date for topics begun later. Research notes are
  reference material and are not injected into every task.
- The existing `standards/<profile>.md` as a short entry with essential rules
  and task-based reading conditions. General rules continue to belong to
  `standards/core.md` or the applicable process standard.
- Cohesive `standards/<topic>/*.md` sections for details that need not be read
  for every task. Combine small related topics; avoid one file per pattern or
  copying a fixed backend-oriented tree into every technology.
- `standards/<topic>/examples/*.md` for longer explanations and runnable code.
  Read them when the example resolves a decision, not on every profile match.
  A very short example may remain within its section when clearer.

The user's 2026-09-21 context-size clarification refines K01 and all later
topics: availability in a project is separate from inclusion in model context.
A profile entry tells the agent when to read each section and to stop following
links once the task's relevant rules are known. Do not concatenate every section
into a native instruction or automatically follow all example/research links.
Keep the entry short enough to scan; a word/line count is a review signal, not
a universal token guarantee or a quota that removes necessary rules.

P2 copies registered sources and shared assets. K01 adds optional per-profile
`resources` to the catalog/composer: copy these explicit, validated paths only
when their owning profile is selected. Include their source/derived digests and
use existing ownership, drift, retirement, and portable-link handling. Resources
do not become extra automatic reading routes or new profile IDs. Arbitrary
linked files remain uncopied. This makes topic/example links work in repositories
opened independently without distributing Go details to unrelated stacks.

## Common research coverage

For each topic, assess the following areas. Mark an area inapplicable with a
reason when appropriate; language, database, and container guidance need
different practices even though they share the same research discipline.

1. Architecture, boundaries, permitted dependencies, and module organization.
2. Idiomatic construction and dependency management; useful patterns, simpler
   alternatives, and circumstances in which a pattern adds unnecessary complexity.
3. Typed contracts, transport validation, domain invariants, and error semantics.
4. State, concurrency, cancellation, resource lifetime, and effects where relevant.
5. Persistence, transactions, integration boundaries, and external API behavior.
6. Testing and review: observable behavior, meaningful failure cases, and suitable
   verification levels under the shared policy.
7. Security, operational behavior, and performance decisions relevant to the topic.
8. Version-sensitive behavior, existing-project migration, and compatibility limits.

Research scope follows real engineering decisions. Do not collect a fixed
number of patterns, force every topic through a backend layer hierarchy, or
turn every performance suggestion into a universal requirement. Familiar names
such as SOLID, Factory, Facade, Strategy, Repository, or monadic composition do
not justify their own adoption.

## Workflow for each topic

1. **Establish scope and versions.** Read the affected existing profile and
   shared rules. Identify concrete gaps and the version assumptions to verify.
2. **Research primary sources on the web.** Use specifications, official manuals,
   maintained project source/examples, and original architectural publications.
   Follow relevant release/migration notes. Attribute an author's opinion as
   opinion; distinguish it from a language guarantee or framework contract.
3. **Synthesize recommendations.** Record each recommendation's problem,
   applicability, idiomatic form, simpler alternative, costs, version limits,
   evidence link, and verification date. Explain disagreements between sources.
   Mark the strength as a framework requirement, a recommended default, or an
   optional technique. A framework requirement must have a project-policy reason.
4. **Reconcile and adopt.** Update the topic's short entry and conditional sections
   without duplicating common rules. Add examples that clarify materially different choices, including
   business-invariant versus transport-validation cases where relevant. Preserve
   existing project constraints and make exceptions explicit.
5. **Verify the deliverable.** Check changed artifacts and relevant executable
   examples. If catalog selection or resources change, verify affected discovery,
   composition, and independent-repository routes. Record actual commands/results
   and any unexecuted checks; do not claim example execution from a prose review.
6. **Report and checkpoint.** Present a concise Russian explanation, links to the
   English research/profile, decisions and tradeoffs, checks, and remaining limits.
   Update this plan and stop for the user's review before the next topic.

If a material architectural choice cannot be settled from existing requirements
and evidence, present the concrete alternatives for that choice. Routine
implementation and editorial decisions use the already agreed project policies.

## Sequential topic queue

Every row is a separate stage with the workflow and exit criteria above. Grouped
framework files are updated only in the sections belonging to that stage. Reading
another technology's documentation to resolve an interaction does not start its
adoption stage. No parallel topic execution is planned.

| Stage | Topic | Primary adoption target | State |
| --- | --- | --- | --- |
| K01 | Go | `standards/go-gin.md` and conditional Go resources | Complete; user authorized K02 |
| K02 | Gin | `standards/go-gin.md`: HTTP/framework sections | Complete; user authorized K03 |
| K03 | Python | `standards/python-fastapi.md`: language sections | Complete; user authorized K04 |
| K04 | Pydantic | `standards/python-fastapi.md`: validation/model sections | Complete; user authorized K05 |
| K05 | FastAPI | `standards/python-fastapi.md`: framework sections | Complete; user authorized K06 |
| K06 | PHP | `standards/php-symfony-doctrine.md`: language sections | Complete; user authorized K07 |
| K07 | Symfony | `standards/php-symfony-doctrine.md`: framework sections | Complete; user authorized K08 |
| K08 | Doctrine ORM/DBAL | `standards/php-symfony-doctrine.md`: persistence sections | Complete; user authorized K09 |
| K09 | JavaScript | `standards/nodejs-typescript.md`: shared language sections | Complete; user authorized K10 |
| K10 | TypeScript | `standards/typescript.md`; relevant shared JS/TS references | Complete; user authorized K11 |
| K11 | Node.js | `standards/nodejs-typescript.md`: runtime sections | Complete; user authorized K12 |
| K12 | NestJS | `standards/nestjs.md`, including actual validation/serialization boundaries | Complete; user authorized K13 |
| K13 | React | `standards/nextjs.md`: React sections; frontend organization references | Complete; user authorized K14 |
| K14 | Next.js | `standards/nextjs.md` and `standards/nextjs-feature-structure.md` | Complete; user authorized K15 |
| K15 | PostgreSQL | `standards/postgresql.md` | Complete; user authorized K16 |
| K16 | SQLAlchemy | New conditional `standards/sqlalchemy.md` and catalog entry; reconcile Python references | Complete; user authorized K17 |
| K17 | psycopg | New conditional `standards/psycopg.md` and catalog entry; reconcile PostgreSQL references | Complete; user authorized K18 |
| K18 | Docker | `standards/docker.md` | Complete; accepted; user authorized remaining named stages |
| K19 | Cross-profile reconciliation | Shared standards, catalog routes, affected templates and composition evidence | Complete; coordinator handoff under bulk authorization |

SQLAlchemy and psycopg guidance applies only where those dependencies are present
or explicitly selected. Recognizing a dependency does not choose that ORM/driver
for every Python project. Existing migration and new-project use cases must both
remain supported. Other databases, frameworks, or tools become separate topics
when the user adds them to the supported scope.

## Exit criteria and review focus

A topic is complete when its relevant coverage has been researched and reflected
in usable guidance, with short explanatory examples where they resolve ambiguity.
It must have:

- Traceable primary evidence, verification date, and explicit version applicability.
- Clear conditions and alternatives for architecture and pattern recommendations.
- A distinction between ecosystem facts, framework policy, and project exceptions.
- Consistency with shared scope, typing, verification, work-mode, and model policies.
- Enough context to understand each example's purpose and limits; runnable examples
  identify their setup and actual verification evidence.
- Working selected reading routes with no required resource lost during adoption.
- A short entry, meaningful conditions for loading details, and no automatic
  expansion of every section/example into the entry point. Verify this in the
  generated artifacts; actual model adherence needs a separate native pilot.
- A recorded user-review checkpoint and an explicit next topic.

Review concrete risks: copying class hierarchies between languages, imposing
Repository/DDD/factories on trivial work, moving all invariants into transport
validation, requiring heavy tests for small edits, mixing incompatible versions,
and describing a recommendation as universally best without its conditions.

K19 reconciles cross-profile differences accumulated during the sequence, checks
that common rules still have one owner, and verifies affected bundle selection.
Run relevant checks for changed resources and concrete remaining concerns; do not
re-run every completed topic's tests without changed inputs or an unresolved risk.
Its result prepares the enriched rule library for the next native-adapter stage.

## Planning evidence

Inspected the catalog, current profile coverage, metadata-recognized dependencies,
the completed P2 contract, and existing planning/verification policies. Captured
the two-path baseline before creating this plan and adding its navigation link.
This stage changes planning documents only. Topic research, example execution,
catalog changes, and rule adoption retain their K01–K19 owners.

## K01 working scope

Baseline: `/tmp/af-k01-go-s0kssdbw/baseline.json`, covering this plan, the current
Go/Gin profile, the new Go research note, and the affected catalog/composer/tests.
It was extended before editing to cover five Go sections and three example files.
Preserve the existing Gin section for K02. No catalog IDs, native adapters, or
model assignments need to change for this topic.

The initial Go draft contained 347 lines. The user's context-size concern changes
its packaging: keep essential version/contract guidance and a reading map in
`go-gin.md`; route to architecture, contracts, concurrency, resources, and
verification as needed. Put the three examples behind links from their sections.
This is a bounded extension of existing rule composition, performed inline under
the approved topic and the user's clarification. Reuse the researched content
and example evidence when their code remains unchanged.

Acceptance for the `resources` extension: omitted lists preserve existing
catalog behavior; selected resources and relative links survive independent
opening; unrelated projects receive none; missing/escaping paths are rejected;
changes invalidate stale previews and edited copies retain drift protection.
Use focused tests for these delivery failures and existing P2 regression checks.

Locally installed toolchain: `go1.26.1 linux/amd64`. Research current official
version evidence separately; exercise examples in an isolated temporary module
using the installed toolchain, without a network-dependent toolchain switch.
The user approved topic execution; no additional design/onboarding sequence is
needed for these routine decisions under the saved Superpowers adaptation.

### K01 result and verification

Delivered the [Go research note](../research/2026-09-21-go-engineering-practices.md)
and a short [Go entry](../../standards/go-gin.md), five conditional topic files,
and three optional example files. The research covers the eight common areas
and distinguishes primary-source facts, framework requirements, defaults, and
optional techniques. Source/version evidence was checked on 2026-09-21. The Gin
section is byte-for-byte unchanged for K02.

The initial Go entry changed from 347 lines / 2,505 whitespace-separated words
to 63 lines / 508 words. This measures the entry artifact, not actual model token
use. Sections and examples remain available without being concatenated into the
native entry. The catalog still has 17 profile IDs; Go has eight explicit resource
paths. Existing profiles can omit `resources` and retain their previous behavior.

Checks completed on the resulting content and code:

| Check | Result and scope |
| --- | --- |
| `python3 -m pytest -q tests/test_rules.py` | 28 passed: existing composition scenarios plus nine resource cases for three clients, independent access, selective copying, stale source detection, retirement/drift, and invalid paths |
| `python3 -m mypy` | No issues in 16 source/test files under the existing strict configuration |
| `python3 /tmp/af-k01-go-s0kssdbw/check_delivery.py` | Codex, Claude Code, and Cursor synthetic previews: Go detected without Gin, all eight resources and three original examples preserved, local links and short entry available after opening the child alone |
| `python3 /tmp/af-k01-go-s0kssdbw/verify_go_examples.py` | All three extracted Markdown code blocks are `gofmt`-clean and identical to the code used in the successful Go checks |
| `go test -race -count=1 -timeout=20s -v ./...` | Three test groups, ten scenarios passed: publication success/failures with unchanged rejected state; selected strategy, propagated error/cancellation; forwarding, blocked receive, blocked send, and completion |
| `go vet ./...` | Exit 0 for the extracted example module |
| `python3 /tmp/af-k01-go-s0kssdbw/check_artifacts.py` | Changed Markdown links/anchors, catalog resources, preserved Gin content, baseline integrity, and scoped diff checked |

Go commands used `/home/vitalii/.local/go/bin/go` in
`/tmp/af-k01-go-s0kssdbw/examples`, with `GOTOOLCHAIN=local`, `GOENV=off`,
`GOWORK=off`, `GOPROXY=off`, `GOSUMDB=off`, and stage-local `GOCACHE` /
`GOMODCACHE`. No dependencies or new toolchain were downloaded. The example
sources, focused tests, and `go-test.log` remain in that evidence directory.
The split preserved their code, so the successful race run was reused after
checking exact code equality rather than repeated for a Markdown move.

The new resource test first failed because the old catalog rejected `resources`;
it passed after the scoped extension. A temporary delivery check initially
expected no generated changes after remapping a child from `projects/service`
to `.`. Inspection found the expected entry scope-label and manifest changes;
the corrected check requires the adopted rules/resources to remain unchanged.
No product defect or unresolved check failure remains from these checks.

Inline review covered conditional applicability, avoided abstraction defaults,
version limits, unchanged example behavior, portable links, and resource ownership.
Baseline and the 15-path diff are retained at
`/tmp/af-k01-go-s0kssdbw/baseline.json` and `/tmp/af-k01-go-s0kssdbw/k01.diff`.
No unrelated suite, native session, database integration, fuzz campaign,
performance benchmark, or vulnerability scan was needed or claimed. Actual
agent adherence to selective reading and session token savings remain for the
native pilot; P3–P7 ownership does not change.

**Checkpoint:** K01 is ready for the user's review. **Next topic:** K02 Gin,
using the same short-entry / conditional-section / optional-example approach.

## K02 working scope

The user authorized only K02 on 2026-09-21, retaining the short entry, conditional
sections, optional examples, and the human checkpoint. Execute inline in the
current workspace under the saved Superpowers adaptation. K03 and P3–P7 stay
outside this stage.

Baseline: `/tmp/af-k02-gin-bp3hbz6i/baseline.json`, with original contents or
absence for the ten planned paths: this plan, the Go/Gin entry, the catalog,
the Gin research note, four Gin sections, and two example files. Hashes guard
the unchanged K01 Go resources/research and existing Python source/tests.

Work sequence:

1. Research versioned Gin sources and official documentation across the eight
   coverage areas; record facts, framework policy, alternatives, and limits.
2. Replace the short legacy Gin section with task-based routes to handler/binding,
   routing/middleware, runtime, and verification guidance. Preserve the Go rules.
3. Register Gin sections/examples as resources of the existing `go-gin` profile.
   Exercise original HTTP binding/domain-error and middleware examples in a
   temporary module using the local Go toolchain and a pinned Gin dependency.
4. Check Markdown links, catalog ownership, discovery/composition for all three
   clients and independently opened children, and the relevant P2 regression tests.
   Review the scoped baseline diff, record results here, and stop for user review.

Acceptance risks: response ownership after binding/abort; presence versus zero;
transport validation versus state invariants; request cancellation and context
reuse; proxy/body-limit assumptions; lost or automatically expanded resource links.
No composer change was needed: K01 already supplies the needed resource contract.

### K02 result and verification

Delivered the [Gin research note](../research/2026-09-21-gin-engineering-practices.md),
updated [Go/Gin entry](../../standards/go-gin.md), four conditional Gin sections,
and two original optional examples. Research addresses all eight coverage areas
with primary sources, a 2026-09-21 verification date, version applicability,
policy strength, alternatives, and limitations. Gin 1.12.0 and its declared
validator 10.30.1 are the researched/executed baseline; earlier supported projects
retain their own versions. No framework or target-project dependency was upgraded.

The combined entry is **59 lines / 465 whitespace-separated words**, compared
with K01's 63 / 508. The Go essential guidance, five Go reading routes, eight Go
resources, and Go research note remain unchanged. The catalog retains 17 profile
IDs; `go-gin` now owns 14 resources: eight Go and six Gin. Gin resources remain
available in a Go-only bundle under the existing combined profile, but reading
them requires a Gin task. No extra automatic native route or concatenated section
was introduced. Unrelated stacks receive neither family.

The [binding example](../../standards/gin/examples/binding.md) distinguishes
presence from a valid zero, bounded single-value JSON from permissive binding,
and HTTP rejection from an application conflict. Strictness is an explicit sample
contract, not a universal default. The
[middleware example](../../standards/gin/examples/middleware.md) shows when a
shared responder is useful, a terminating access gate, and preservation of an
already committed response. The existing Go example retains domain-invariant
ownership; the Gin example does not redefine it or prescribe a layered tree.

Checks completed on the resulting artifacts:

| Check | Result and scope |
| --- | --- |
| `python3 -m pytest -q tests/test_rules.py` | 28 passed: P2 composition, independent access, resource ownership, drift/retirement, and invalid-path regression coverage |
| `python3 /tmp/af-k02-gin-bp3hbz6i/verify_examples.py` | Two actual Markdown Go blocks extracted exactly and `gofmt`-clean; code preserved after final prose clarification |
| `go test -race -count=1 -timeout=30s -v ./...` | Two packages, five test groups, 26 scenarios passed through actual Gin routers: valid false/true, invalid/presence/media/path/size cases, wrapped/private errors, request-context propagation, access/order, late errors, and a public route |
| `go vet ./...` | Exit 0 for both example packages |
| `go mod verify` | All downloaded modules verified |
| `python3 /tmp/af-k02-gin-bp3hbz6i/check_delivery.py` | Codex, Claude Code, Cursor synthetic previews passed: Gin version detection, Go-only selection, all 14 resources/digests, exact example code, short native routes, independent child links/recomposition, and exclusion from the unrelated Python child |
| `python3 /tmp/af-k02-gin-bp3hbz6i/check_artifacts.py` | Markdown links/anchors and fences, catalog ownership, baseline integrity, ten-path diff, 25 unchanged guarded paths, and unchanged K03–K19 queue checked |

Go commands used `/home/vitalii/.local/go/bin/go` (**go1.26.1 linux/amd64**) in
`/tmp/af-k02-gin-bp3hbz6i/examples`, with `GOTOOLCHAIN=local`, `GOENV=off`,
`GOWORK=off`, stage-local `GOCACHE` / `GOMODCACHE`, and no alternative build tags.
Tests/vet also used `GIN_MODE=release` and `GOMAXPROCS=2`. Dependency setup used
`go mod download` and `go mod tidy` through `https://proxy.golang.org` with
`GOSUMDB=sum.golang.org`, solely inside the temporary module/cache. Execution
checks then used `GOPROXY=off` and `GOSUMDB=off`; no toolchain was downloaded.
The pinned module, sums, extracted source, focused tests, and final `go-test.log`
remain in the stage evidence directory.

An initial offline tidy lacked transitive module metadata; completing the
temporary dependency setup resolved it. Initial example compilation found an
incorrect two-result call to `mime.ParseMediaType`; its actual three-result
signature was checked, the unused parameter map was discarded explicitly, and
the final race run and vet passed. The initial log is retained separately.

The accountable inline review covered the full scoped diff, domain versus
transport ownership, simpler alternatives, version limits, response/lifetime
semantics, and conditional delivery. It clarified that standalone sample
contracts must not make an independent application import a Gin adapter.
No material in-scope finding remains unresolved. Baseline and final diff are
`/tmp/af-k02-gin-bp3hbz6i/baseline.json` and
`/tmp/af-k02-gin-bp3hbz6i/k02.diff`.

No native client, live socket/disconnect/shutdown scenario, database integration,
alternate codec/version, vulnerability scan, or performance benchmark was run or
claimed. Request-context propagation was tested; actual cooperative cancellation,
proxy deployment, and recovery/shutdown guidance were reviewed against primary
contracts, not certified by a recorder test. Actual selective-reading adherence
and token savings remain for the native pilot. Python implementation/tests and
P3–P7 remain unchanged.

**Checkpoint:** K02 is complete and ready for the user's review. **Next topic:**
K03 Python; do not begin it until the user authorizes continuation.

## K03 — Python

The user's 2026-09-21 continuation authorized the next topic after K02. Execute
K03 inline under the approved design, retaining the per-topic review checkpoint.
Superpowers selection/execution/verification procedures apply through the
workspace adaptation. The Python service-architecture skill informs conditional
service guidance; the existing framework rules still own module cohesion,
strictness, shared principles, and verification scope.

The baseline for ten scoped paths and 89 guarded files is
`/tmp/af-k03-python-p48aetxd/baseline.json`; original edited files are under its
`before/` directory. Work stays in the current workspace without Git writes,
delegation, external-project installation, dependency upgrades, or native pilots.

### K03 result and verification

Delivered the [Python research note](../research/2026-09-21-python-engineering-practices.md),
updated [Python/FastAPI entry](../../standards/python-fastapi.md), four conditional
sections, and two optional executable examples. Research covers all eight areas,
with primary sources checked on 2026-09-21, version limits, policy strength,
simpler alternatives, and adoption boundaries. Module organization supports
scripts, tools, libraries, and services; related classes may share a cohesive
module. Construction and persistence abstractions remain conditional choices.

The entry is **72 lines / 567 whitespace-separated words**, down from 131 / 1075.
Its routes lead to structure/dependencies, typing/contracts, execution/resources,
and verification/compatibility. The previous FastAPI/contracts and file-move
blocks remain byte-for-byte unchanged. The catalog retains 17 IDs and registers
six resources under the existing `python-fastapi` profile. Resources are available
only with that selected profile and do not become extra automatic native routes;
research remains optional, outside installed bundles.

The [domain example](../../standards/python/examples/domain.md) separates a
typed input parser from publication invariants: an incomplete draft is valid,
and rejected operations preserve state even when called without transport parsing.
The [concurrency example](../../standards/python/examples/concurrency.md) uses
a narrow Protocol and a fixed two-task group with explicit result identity,
failure propagation, timeout, caller cancellation, and observed cleanup. Both
include their own stdlib tests, setup, alternatives, and limits. No application
framework or third-party validation/concurrency dependency is required.

Checks completed on the resulting artifacts:

| Check | Result and scope |
| --- | --- |
| `python3 -m pytest -q tests/test_rules.py` | 28 passed in 0.85s: existing composition, independent access, resources, ownership/drift/retirement, and invalid-path regression checks |
| Exact Markdown extraction, `ast.parse(..., feature_version=(3, 11))`, and `compile(...)` | Five Python blocks extracted unchanged into the temporary example directory; 3.11 grammar accepted and local compilation succeeded |
| `python3 -W error -m unittest -v test_document test_source_pair` | 9 tests passed on Python 3.12.3, including invalid input, valid incomplete drafts, publication/change rejection, ordered async results, sibling failure, timeout, and caller cancellation with cleanup |
| `python3 -m mypy --config-file /tmp/af-k03-python-p48aetxd/mypy.ini --cache-dir /tmp/af-k03-python-p48aetxd/mypy-cache .` | mypy 2.1.0: no issues in all five modules/tests, targeting Python 3.11 with strict plus explicit/unimported-Any restrictions |
| Same analyzer/config with `--disallow-any-expr document.py title_input.py source_pair.py` and a separate cache | No issues in the three example implementation modules; no suppressions or casts |
| `PYTHONPATH=src python3 /tmp/af-k03-python-p48aetxd/check_delivery.py` | Codex, Claude Code, Cursor synthetic previews passed: Python without FastAPI and with FastAPI detected, six resources/digests and exact example code retained, short conditional/native routes, two independently opened child copies and recompositions per client, unrelated Go exclusion; 728 local links checked |
| `python3 /tmp/af-k03-python-p48aetxd/check_artifacts.py` | All ten scoped changes, local links/anchors, Markdown fences/table columns, catalog-only resource addition, preserved framework blocks and K04–K19 queue, and all 89 guarded files checked; scoped diff generated |

Example commands ran in `/tmp/af-k03-python-p48aetxd/examples` using
`/usr/bin/python3` (**Python 3.12.3**) and the installed **mypy 2.1.0**. Tests use
only the stdlib and isolated async loops; events coordinate ordering without
sleep-based guesses. Logs `examples-1.log` through `examples-3.log`, exact extracted
modules/tests, analyzer configuration, synthetic bundles, baseline, and
`k03.diff` are in the stage evidence directory. No interpreter or dependency was
downloaded. The initial example runtime/type checks passed without repairs.

The inline review covered module/layer cohesion, static versus runtime guarantees,
incomplete versus invalid domain states, shallow immutability, grouped errors,
cooperative cancellation and thread limitations, version applicability, and
conditional context loading. It also verified that the existing framework blocks
were preserved and corrected an escaped union separator in a Markdown table.
No material in-scope finding remains unresolved. Source implementation, existing
tests, common standards, K01/K02 resources, and the native-adoption plan are
unchanged; no full-suite rerun was needed for those unchanged inputs.

Python 3.11 grammar/type targeting is not execution on 3.11. No other interpreter,
free-threaded build, process pool, real database/HTTP adapter, application package
installation, security scanner, performance benchmark, or live native client was
run or claimed. Synthetic composition verifies portable files and reading routes,
not actual client compliance or token savings. Those checks belong to an affected
implementation task or the later native pilot.

**Checkpoint:** K03 is complete and ready for the user's review. **Next topic:**
K04 Pydantic; do not begin it until the user authorizes continuation.

## K04 — Pydantic

The user's 2026-09-21 continuation authorized K04 after K03. Execute inline with
Superpowers through the workspace adaptation and preserve the per-topic review
checkpoint. The baseline covers ten scoped paths and 96 guarded files:
`/tmp/af-k04-pydantic-dn6l4izg/baseline.json`, with original edited files under
`before/`. No framework Git writes, dependency upgrades, delegated work,
external-project installation, or native-client activation was needed.

### K04 result and verification

Delivered the [Pydantic research note](../research/2026-09-21-pydantic-engineering-practices.md),
updated [combined entry](../../standards/python-fastapi.md), four conditional
sections, and two optional runnable examples. The research covers all eight
areas with primary sources, a 2026-09-21 verification date, alternatives, policy
strength, version limits, and explicit boundaries for persistence/concurrency
mechanisms that Pydantic itself does not provide.

The entry is **84 lines / 673 whitespace-separated words**, compared with K03's
72 / 567. Python essentials and four Python routes are unchanged. Two existing
Pydantic validation/coercion bullets were moved out of the FastAPI block into
the Pydantic essentials and detailed guidance; the remaining FastAPI and file-move
blocks are byte-for-byte unchanged. Pydantic now has routes for validation,
serialization/schema, lifecycle/integration, and verification/compatibility.

The catalog keeps 17 IDs. `python-fastapi` now owns 12 resources: six Python and
six Pydantic. Its applicability explicitly keeps Pydantic/FastAPI reading
conditional. Adding the already-recognized `pydantic` technology allows selection
from a Pydantic-only passport declaration as well as Python/dependency metadata;
no inspector or composer code changed. Resources remain available without being
concatenated into native instructions, and research is not copied into bundles.

The [boundary example](../../standards/pydantic/examples/boundary.md) demonstrates
strict JSON versus Python input, required nullable fields, bounded guest counts,
cross-field consistency, a fixed public error, and relevant schema checks. It
leaves live availability and domain transitions outside input validation.
The [patch example](../../standards/pydantic/examples/patches.md) preserves omission,
false, and explicit null; validates a complete replacement before changing state;
rejects server-owned fields; and emits a separate public projection with its
wire alias. The existing Python domain example is reused by reference.

Checks completed on the resulting artifacts:

| Check | Result and scope |
| --- | --- |
| Installed metadata and focused `python3` probes | Pydantic 2.13.4/core 2.46.4/Python 3.12.3 established; reproduced unvalidated copy updates, retained assignment after an after-validator rejection, and structured error input despite formatted-error hiding |
| Exact Markdown extraction, `ast.parse(..., feature_version=(3, 11))`, and local `compile(...)` | Four blocks extracted unchanged: two implementation modules and two test modules; 3.11 grammar accepted and local compilation succeeded |
| `python3 -W error -m unittest -v test_booking_input test_preferences` | 15 tests passed in 0.002s: actual input modes, presence/coercions/ranges, invalid windows, safe public error, schema fields, complete replacement without mutation on rejection, aliases and public-only output |
| `python3 -m mypy --config-file /tmp/af-k04-pydantic-dn6l4izg/mypy.ini --cache-dir /tmp/af-k04-pydantic-dn6l4izg/mypy-cache .` | mypy 2.1.0: no issues in four modules/tests; Python 3.11 target, strict plus explicit/unimported-Any restrictions, Pydantic plugin and typed/extra-forbidding constructors/dynamic-alias diagnostics |
| Same analyzer/config with `--disallow-any-expr booking_input.py preferences.py` and a separate cache | No issues in both implementation modules; schema API data stays in the boundary tests, with no casts or suppressions |
| `python3 -m pytest -q tests/test_rules.py tests/test_workspace.py` | 35 passed in 1.17s: existing composition/resource/independent-opening checks plus relevant discovery/inventory checks |
| `PYTHONPATH=src python3 /tmp/af-k04-pydantic-dn6l4izg/check_delivery.py` | Codex, Claude Code, Cursor synthetic previews passed for ordinary Python, Pydantic dependency, and Pydantic-only passport cases; all 12 resources/digests and exact example blocks, conditional native routes, three independent copies/recompositions per client, unrelated Go exclusion; 1,524 local links checked |
| `python3 /tmp/af-k04-pydantic-dn6l4izg/check_artifacts.py` | Ten-path baseline diff, local links/anchors, Markdown fences/table columns, catalog change bounds, unchanged Python routes/remaining FastAPI blocks/K05–K19 queue, and all 96 guarded files checked |

Example commands ran in `/tmp/af-k04-pydantic-dn6l4izg/examples` with
`/usr/bin/python3`. The dependency pair was already installed; nothing was
downloaded. Logs `examples-1.log` through `examples-3.log`, extracted code/tests,
the analyzer configuration, synthetic bundles, baseline, check scripts, and
`k04.diff` are retained in the stage directory. The examples passed runtime and
static checks on their first run. An initial pytest command named a nonexistent
`tests/test_metadata.py` and collected no tests; inspection located the metadata
checks in `tests/test_workspace.py`, and the corrected command above passed.

The inline review covered model ownership, validators without effects, strict
runtime versus static typing, update atomicity limits, output/error disclosure,
aliases and schema compatibility, and selective reading. It resolved a source
discrepancy rather than repeating a blanket V1/Python 3.14 incompatibility claim:
older overview/announcement text differs from the later minimal-support change
in V1 1.10.25; the installed compatibility namespace is 1.10.26. The research
records exact evidence and avoids claiming full compatibility from that fix.
No material in-scope finding remains unresolved.

Existing source/tests, Python resources/research, common standards, K01/K02
resources, and the native-adoption plan are unchanged. No live HTTP/ORM/settings
integration, V1 or other-interpreter test matrix, security scan, benchmark, or
native client was run or claimed. Grammar/type targeting does not prove execution
on Python 3.11. Synthetic bundles establish routes/portability, not actual client
reading compliance or token savings. K05 and P3–P7 remain planned.

**Checkpoint:** K04 is complete and ready for the user's review. **Next topic:**
K05 FastAPI; do not begin it until the user authorizes continuation.

## K05 working scope

The user authorized continuation on 2026-09-21. Baseline:
`/tmp/af-k05-fastapi-1366ge_f/baseline.json`, with ten scoped paths and
103 guarded files. Work proceeds inline under the approved design and
Superpowers adaptation. Preserve earlier Python/Pydantic resources, essentials,
and routes; research only FastAPI and its direct integration contracts.

Use four conditional sections for HTTP boundaries, dependency/resource lifetime,
runtime/operations, and verification/compatibility, plus two optional executable
examples. Keep the combined entry short and add only explicit catalog resources.
Verify the installed stack, meaningful HTTP/failure/lifetime behavior, strict
types, resource selection/composition and independently opened child projects.
Record results here and stop before K06 PHP.

### K05 result and verification

Delivered the [FastAPI research note](../research/2026-09-21-fastapi-engineering-practices.md),
updated [combined entry](../../standards/python-fastapi.md), four conditional
sections, and two optional runnable examples. Research covers all eight areas
with primary sources checked on 2026-09-21, explicit R/D/O strength, simpler
alternatives, costs, and version limits. FastAPI integration guidance does not
select an ORM, impose a backend scaffold, or implement later practice topics.

The entry is **75 lines / 608 whitespace-separated words**, down from K04's
84 / 673. Python/Pydantic essentials and their eight routes are unchanged.
FastAPI details now load by task: transport/contracts, dependencies/lifetime,
runtime/operations, and verification/compatibility. Existing FastAPI boundary,
typed collection, wiring, and file-move obligations retain their meaning in those
sections. Examples and research remain optional.

The catalog retains 17 IDs and changes only six FastAPI resource registrations.
The combined profile owns 18 resources: six each for Python, Pydantic, and FastAPI.
No discovery/composition implementation or technology-selection condition changed.
Resources are available in the selected bundle without becoming independent
native routes or being concatenated into the entry. Research remains uncopied.

The [HTTP example](../../standards/fastapi/examples/http-boundary.md) separates
strict input validation from a live capacity rule, uses an injected typed
function, maps expected conflicts, redacts invalid-input responses, and projects
only public receipt fields. The [lifetime example](../../standards/fastapi/examples/lifetime.md)
owns an HTTP client through lifespan, chooses request/function dependency scopes
for streaming versus fully consumed output, checks upstream status before sending
success, and closes resources on expected and unexpected failure paths.

Checks completed on the resulting artifacts:

| Check | Result and scope |
| --- | --- |
| Installed metadata/source and `python3 /tmp/af-k05-fastapi-1366ge_f/probe_contracts.py` | Established FastAPI 0.138.0/Starlette 1.3.1/Pydantic 2.13.4/AnyIO 4.14.0/HTTPX 0.28.1/Python 3.12.3; reproduced JSON-versus-Python validation through HTTP, rejected-input disclosure, dependency execution before rejection, direct Response filtering bypass, invalid-response 500, and unsupported generic Request registration |
| Exact Markdown extraction, `ast.parse(..., feature_version=(3, 11))`, and local `compile(...)` | Five blocks: three implementation modules and two test modules; Python 3.11 grammar accepted, local compilation succeeded, and extracted content matches the final Markdown |
| `timeout 45s python3 -W default -m unittest -v test_reservation_http test_feed_http` | 14 passed in 0.065s: HTTP/domain failures without unwanted writes, public output/errors and affected schemas, real lifespan entry/exit, streaming/snapshot consumption, upstream rejection/timeout, cleanup after streaming failure, and snapshot accumulation limit |
| `timeout 45s python3 -W default -m unittest -v test_feed_http` after the final lifetime refinement | 7 passed in 0.029s; clarified text/plain OpenAPI response metadata and removed an ineffective client-level pool limit for a custom transport; unchanged HTTP/domain tests were not repeated |
| `python3 -m mypy --config-file /tmp/af-k05-fastapi-1366ge_f/mypy.ini --cache-dir /tmp/af-k05-fastapi-1366ge_f/mypy-cache .` | No issues in five modules/tests: Python 3.11 target, strict, explicit/unimported-Any restrictions, Pydantic plugin with typed/extra-forbidding constructors and dynamic-alias diagnostics; the final refinement was rechecked with the same command targeting `feed_http.py test_feed_http.py`, also clean |
| `python3 -m pytest -q tests/test_rules.py tests/test_workspace.py` | 35 passed in 1.15s: existing resource/composition/independent-opening and discovery checks |
| `PYTHONPATH=src python3 /tmp/af-k05-fastapi-1366ge_f/check_delivery.py` | Codex, Claude Code, Cursor synthetic previews passed for plain Python, a FastAPI dependency, and a FastAPI-only passport; all 18 resources/digests and exact code, conditional native routes, three independent copies/recompositions per client, unrelated Go exclusion; 1,866 local links checked |
| `python3 /tmp/af-k05-fastapi-1366ge_f/check_artifacts.py` | Ten scoped paths, required local links/anchors, fences/table columns, exact example extraction, catalog-only resource additions, prior essentials/routes/results, unchanged K06–K19 queue, and all 103 guarded files checked; scoped diff retained |

Example commands ran in `/tmp/af-k05-fastapi-1366ge_f/examples` using the existing
Python environment. No packages were installed. Stage evidence includes the
baseline/before copies, `k05.diff`, extracted modules, mypy config, probes, check
scripts, synthetic bundles, and logs (`examples.log`, `lifetime-final.log`,
`mypy.log`, `mypy-lifetime-final.log`, `probes.log`, `framework-tests.log`,
`delivery.log`, `artifacts.log`).

Two environment findings were diagnosed before proceeding. An initial `-W error`
invocation stopped at import because Starlette 1.3.1 deprecates its installed
HTTPX TestClient backend in favor of HTTPX2. The supported fallback was exercised
with `-W default`; the warning remains visible and its migration boundary is
documented. TestClient then stalled even for an empty app because the sandbox
denied socketpair sends used for its thread wakeup. A bounded traceback and direct
PermissionError probe established that cause; the same bounded tests passed
outside that restriction, without network requests. An indentation typo during
the final documentation refinement was caught by AST extraction, corrected, and
the affected example rechecked before completion.

The inline review covered HTTP/domain boundaries, accurate typing, safe response
and error projection, dependency side effects, scope/commit timing, streaming
cleanup, and version applicability. Current docs were reconciled with the
installed stack: generic typed Starlette Request is not directly accepted by this
FastAPI registration path, current Starlette body-limit recipes are not present
in the inspected 1.3.1 signatures, and TestClient's backend migration is explicit.
No material in-scope finding remains unresolved.

Source/tests, dependencies, common standards, earlier topic resources/research,
and the native-adoption plan are unchanged. In-process transport tests do not
prove real-network pacing/backpressure/disconnects, live-server cancellation or
shutdown, database atomicity, durable job delivery, real authentication, or a
multi-interpreter matrix. No live server, benchmark, security scan, external
installation, or native-client pilot was run. Synthetic delivery establishes
routes and portability, not model reading compliance or token savings.
K06 and P3–P7 remain planned.

**Checkpoint:** K05 is complete and ready for the user's review. **Next topic:**
K06 PHP; do not begin it until the user authorizes continuation.

## K06 working scope

The user authorized continuation on 2026-09-21. Baseline:
`/tmp/af-k06-php-i2bazajo/baseline.json`, covering ten scoped paths and
110 guarded files. Execute PHP research inline under the approved design and
Superpowers adaptation. Preserve the existing Symfony/Doctrine guidance for
K07/K08 and retain the combined profile ID.

Add four conditional PHP sections for structure/dependencies, types/contracts,
state/effects, and verification/compatibility, with separate boundary/domain and
resource examples. Verify actual tools, executable behavior, static analysis,
autoloading, catalog delivery and independently opened project routes. PHP tools
are initially absent; prepare a temporary toolchain without changing workspace
dependencies or installing system packages. Record evidence here and stop before
K07 Symfony.

### K06 result and verification

Delivered the [PHP research note](../research/2026-09-21-php-engineering-practices.md),
updated [combined entry](../../standards/php-symfony-doctrine.md), four conditional
sections, and two optional runnable examples. Research covers all eight areas
with primary sources checked on 2026-09-21, explicit R/D/O strength, alternatives,
costs and version limits. PHP guidance preserves named contracts, meaningful
construction and owned invariants without imposing an ORM, layered scaffold,
one-interface-per-class rule, or new concurrency runtime.

The entry is **87 lines / 686 whitespace-separated words**, compared with
83 / 682 before K06. PHP details load by task: structure/dependencies,
types/contracts, state/effects, and verification/compatibility. The existing
Symfony controller/validation and Doctrine domain-placement sections are unchanged;
autoload/DI/ORM file-move obligations retain their meaning. Examples and research
remain optional. K07/K08 adoption has not started.

The catalog retains 17 IDs and changes only six PHP resource registrations under
the existing combined profile. No discovery/composition implementation, selection
condition, dependency or shared standard changed. Resources are copied with the
selected profile without becoming extra native routes or being concatenated into
the entry; research remains uncopied.

The [input/domain example](../../standards/php/examples/input-domain.md) separates
JSON shape/presence/type/byte limits from an Article's publication/editing rules.
It accepts a valid incomplete draft, distinguishes explicit null and omission,
preserves the title `"0"`, and rejects forbidden transitions before mutation.
The [resource example](../../standards/php/examples/resources.md) uses a typed
stream opener and one bounded loop with finally cleanup; it checks EOF, early
return, record bounds and failures without introducing a generator abstraction.

Checks completed on the resulting artifacts:

| Check | Result and scope |
| --- | --- |
| Local runtime/tool version inspection | PHP 8.3.6 CLI NTS, Zend Engine 4.3.6, 64-bit Linux; Ubuntu package 8.3.6-0ubuntu0.24.04.11, build 2026-09-02; Composer 2.10.3 and PHPStan 2.2.14. This distribution build is not claimed as latest upstream PHP |
| Exact Markdown extraction and `python3 /tmp/af-k06-php-i2bazajo/check_examples.py input-domain resources` | Five PHP files and two Composer manifests checked in separate temporary projects; every subprocess returned zero |
| Composer `--no-plugins --no-scripts validate --strict --no-interaction` and `dump-autoload --optimize --strict-psr --strict-ambiguous --no-interaction` | Both manifests valid; optimized PSR-4 loading succeeded without duplicate-class/mapping errors; no dependency installation or project scripts/plugins |
| `php -l` for each extracted PHP file; `php -d zend.assertions=-1 tests/run.php` in each example | Syntax clean; ten rejected input cases plus nullable notes and draft/publication/editing scenarios passed; seven EOF/early-return/boundary/acquisition/rejection cases passed, including observable resource closure |
| `php -d memory_limit=512M phpstan.phar analyse --configuration=phpstan.neon --no-progress --debug` in each example | No errors across all five PHP files; level max = 10, PHP target 80200, no suppressions or baseline. Debug mode keeps the small check in one process |
| Temporary PHP probes `weak-caller.php` and `probe-semantics.php` | Reproduced caller-controlled scalar strictness, internal callback coercion, shallow readonly/clone behavior, and a retained generator keeping its stream open after break until release |
| `python3 -m pytest -q tests/test_rules.py tests/test_workspace.py` | 35 passed in 1.29s: existing resource/composition/independent-opening and discovery checks |
| `PYTHONPATH=src python3 /tmp/af-k06-php-i2bazajo/check_delivery.py` | Codex, Claude Code, Cursor synthetic previews passed for plain PHP, combined framework dependencies and a PHP passport; six resources/digests and exact PHP/JSON blocks, conditional native routes, three independent copies/recompositions per client, unrelated Go exclusion; 984 local links checked |
| `python3 /tmp/af-k06-php-i2bazajo/check_artifacts.py` | Ten scoped paths, local links/anchors, fences/table columns, exact example extraction, catalog-only resource additions, preserved Symfony/Doctrine sections and earlier stage results, unchanged K07–K19 queue, and all 110 guarded files checked; scoped diff retained |

PHP tools were initially absent. Downloaded only the pinned CLI/common packages
from the configured Ubuntu archive, verified their SHA256 against APT metadata,
and extracted them under `/tmp/af-k06-php-i2bazajo/runtime`. Official pinned
Composer/PHPStan PHARs were verified against the published/release-asset SHA256.
No installer or system package installation ran. Initial sandbox DNS prevented
the APT download; a bounded approved download completed. Workspace dependencies
remain unchanged. The temporary wrapper/configuration loads only the needed
extracted extensions and keeps Composer home/cache and analyzer output in `/tmp`;
Composer network, plugins and scripts were disabled during checks.

Stage evidence includes `baseline.json`, before copies, `k06.diff`, exact extracted
examples and analyzer configs, probe files, check scripts, synthetic bundles, APT
metadata, pinned downloads/checksums and PHPStan release metadata. Check output is
retained in `input-domain-checks.log`, `resources-checks.log`, `probes.log`,
`delivery.log` and `artifacts.log`; pytest's complete result was inspected in the
tool output. All example checks passed on their first execution.

The inline review covered requirement preservation, parsed mixed values versus
unchecked assertions, required-null semantics, live domain invariants, shallow
state/copy guarantees, ownership/cleanup, autoload portability and restraint in
pattern adoption. The properties manual's older same-class readonly wording was
reconciled with its explicit PHP 8.4 protected-set note; no timeless restriction
was invented. No material in-scope finding remains unresolved.

The examples ran on one CLI build. Static targeting of PHP 8.2 does not prove a
multi-version or multi-SAPI execution matrix. No real database, network service,
authentication system, FPM/worker deployment, concurrent write, device/close
failure, live disconnect, benchmark, external installation or native-client pilot
was exercised. Synthetic delivery verifies routes and portability, not model
reading compliance or token savings. Source/tests, earlier topic resources/research,
common standards and the native-adoption plan are unchanged. P3–P7 remain planned.

**Checkpoint:** K06 is complete; the user accepted its review on 2026-09-21.
Review-acceptance baseline: `/tmp/af-k06-review-2v39hayj/before.md`.
**Next topic:** K07 Symfony; do not begin it until the user authorizes continuation.

## K07 working scope

The user authorized K07 on 2026-09-21. Baseline:
`/tmp/af-k07-symfony-ma9oof9k/baseline.json`, covering ten scoped paths and
117 guarded files. Execute Symfony research inline under the approved design
and Superpowers adaptation. Preserve PHP essentials/resources and the existing
Doctrine domain-placement guidance for K08; retain the combined profile ID.

Use four conditional sections for structure/services, HTTP/validation,
runtime/effects, and verification/compatibility, with separate request-boundary
and HTTP-client examples. Research all eight coverage areas, including container
lifetime, authorization, Messenger delivery and framework integration, without
starting Doctrine adoption or imposing those components on every application.
Reuse the temporary PHP 8.3 toolchain; install only example dependencies under
this stage's `/tmp` directory. Symfony 7.4 LTS supports that runtime; distinguish
its verified behavior from Symfony 8.1, which requires PHP 8.4.

Verify executable HTTP/domain and external-client failure behavior, strict types,
container/routing/autoload contracts, catalog delivery and independent project
routes. Record actual commands and limits here, then stop before K08 Doctrine.

### K07 result and verification

Delivered the [Symfony research note](../research/2026-09-21-symfony-engineering-practices.md),
updated [combined entry](../../standards/php-symfony-doctrine.md), four conditional
sections, and two optional runnable examples. Research covers all eight areas
with primary sources checked on 2026-09-21, R/D/O strength, simpler alternatives,
costs and compatibility limits. It addresses the real container/HTTP/worker
contracts without mandating bundles per feature, AbstractController inheritance,
an ORM, a message bus, or a new application scaffold.

The entry remains **87 lines**, with **689 whitespace-separated words** versus
686 before K07. PHP essentials, four reading routes and all six PHP resources are
unchanged. Symfony controller/validation obligations retain their meaning in the
new conditional sections. The existing Doctrine domain-placement section and
framework file-move obligations are unchanged; K08 adoption has not started.

The catalog retains 17 IDs. Only six Symfony resources were added to the existing
combined profile, bringing it to 12 resources. Discovery/composition code,
technology selection and native route count are unchanged. The entry gates
Symfony reading on actual framework use even when a plain PHP project receives
the shared bundle. Examples remain optional and research remains uncopied.

The [request example](../../standards/symfony/examples/request-boundary.md) runs
through a real FrameworkBundle kernel with service configuration, routing,
MapRequestPayload, Validator and an exception listener. It separates input rules
from live capacity, preserves state after refusal, and returns only public data.
The [client example](../../standards/symfony/examples/http-client.md) uses the real
HttpClient mock components to check lazy response consumption, status/absence,
bounded decoding, transport errors and cancellation before returning a named
snapshot. Neither example is an application deployment template.

Checks completed on the resulting artifacts:

| Check | Result and scope |
| --- | --- |
| Official release pages, installed component source, Composer lock metadata and PHP/tool versions | PHP 8.3.6 CLI NTS from Ubuntu 8.3.6-0ubuntu0.24.04.11, Composer 2.10.3, PHPStan 2.2.14. FrameworkBundle/HttpFoundation/HttpKernel/Serializer/Validator/HttpClient 7.4.19; DI/EventDispatcher 7.4.17, Routing 7.4.18, HttpClient Contracts 3.7.3. Symfony 8.1 requires PHP 8.4 and was not executed |
| Exact Markdown extraction comparison and `php -l` on source/config/tests | Eleven PHP files and two Composer manifests match the checked temporary projects; every PHP syntax check passed |
| Composer `--no-plugins --no-scripts validate --strict --no-interaction`, `dump-autoload --optimize --strict-psr --strict-ambiguous --no-interaction`, and `check-platform-reqs --no-dev --no-interaction` in both examples | Valid manifests/lockfiles, successful optimized PSR-4/duplicate-class checks and actual platform checks. Direct requirements reconciled without changing locked package versions |
| `php -d zend.assertions=-1 tests/run.php` in `examples/request-boundary` | Passed: eight malformed/type/presence/constraint/media-type rejection cases, POST/405/Allow behavior, successful reservations and conflict without mutation, safe public projection, explicit non-HTTP Validator execution and the direct application invariant |
| `php -d zend.assertions=-1 tests/run.php` in `examples/http-client` | Twelve success/absence/status/data/size/timeout/transport cases passed; checks include configured destination/budgets/buffering/redirect policy, response cancellation and preserved request-failure cause |
| `php -d memory_limit=512M phpstan.phar analyse --configuration=phpstan.neon --no-progress --debug` in both examples | No errors in eleven source/config/test files; max = level 10, PHP target 80200, no ignore/baseline or unchecked casts. Initial framework-hook diagnostics were resolved through standard configuration files |
| `python3 -m pytest -q tests/test_rules.py tests/test_workspace.py` | 35 passed in 1.20s: existing resource/composition/independent-opening and discovery checks |
| `PYTHONPATH=src python3 /tmp/af-k07-symfony-ma9oof9k/check_delivery.py` | Codex, Claude Code, Cursor synthetic previews passed for plain PHP, a Symfony dependency and a Symfony-only passport; 12 resources/digests, exact PHP/JSON, conditional native routes, three independent copies/recompositions per client, unrelated Go exclusion; 1,272 local links checked |
| `python3 /tmp/af-k07-symfony-ma9oof9k/check_artifacts.py` | Ten scoped paths, local links/anchors, Markdown fences/table columns, exact example extraction, catalog-only additions, preserved PHP/Doctrine guidance and earlier results, unchanged K08–K19 queue and all 117 guarded files checked; scoped diff retained |

Example commands use `/tmp/af-k07-symfony-ma9oof9k/php`, the temporary PHP wrapper,
and the previously verified K06 Composer/PHPStan PHARs. Dependencies were installed
only in the two temporary examples: 35 packages for the kernel example and seven
for HttpClient. One pinned Ubuntu XML package was downloaded, SHA256-checked and
extracted without installation. Composer plugins/scripts were disabled; no Symfony
CLI, Flex recipe or global package installation ran. The final lock refresh used
cached metadata after a reported DNS fallback and changed no package versions.

Three findings were resolved before completion. ExtraAttributesException escaped
the 7.4 payload resolver as 500; the input-route listener now maps it to a redacted
400. HttpClient's mock factory object differs from the issued response; the test
now observes cancellation through supported progress metadata, configured with
withOptions rather than an unsupported constructor argument. PHPStan could not
recognize the initial private MicroKernel configuration callbacks; the example
uses ordinary PHP configuration files instead. The generated fixture cache was
rebuilt and affected runtime/static checks passed after these changes.

Evidence under the stage directory includes baseline/before copies, `k07.diff`,
exact examples, both lockfiles and version/source-reference lists, downloaded
package metadata, PHP/analyzer configurations, synthetic bundles and check scripts.
Logs include `request-final.log`, `client-corrected.log`, `request-phpstan.log`,
`client-phpstan.log`, both `*-packaging.log` files, `framework-tests.log`,
`delivery.log` and `artifacts.log`; initial diagnostic and install logs are retained.

The accountable inline review covered boundary/typing fidelity, executed versus
declarative validation, safe error/output projection, state after failed effects,
actual container/response lifetime, version distinctions and conditional reading.
Inherited controller/Validator obligations, PHP routes and Doctrine model choices
remain intact. No material in-scope finding remains unresolved.

The examples establish one locked Symfony 7.4 stack on one PHP CLI build. Static
targeting of 8.2 is not a runtime-version matrix. Container boot/compile and route
behavior were exercised; a Console `lint:container` command, SecurityBundle,
Messenger/broker, real database, concurrent writes, live DNS/TLS/timing,
backpressure/disconnect, FPM/worker deployment and benchmarks were not exercised.
Synthetic delivery does not prove model reading compliance or token savings.
No external installation or native-client pilot ran. Source/tests, workspace
dependencies, common standards, earlier research/resources and the native-adoption
plan remain unchanged; P3–P7 remain planned.

**Checkpoint:** K07 is complete and ready for the user's review. **Next topic:**
K08 Doctrine ORM/DBAL; do not begin it until the user authorizes continuation.

### K08 working scope

The user authorized K08 on 2026-09-21 after reviewing K07. Execute this topic
inline with Superpowers under the existing workspace adaptation. Preserve PHP
and Symfony guidance, all earlier results and the K09–K19 queue. Do not start
JavaScript or native-adapter adoption.

Research ORM and independently usable DBAL across all eight areas. Keep the
existing mapped-rich/separate-domain decision and file-move obligations while
moving detail into conditional sections. Cover mapping and association ownership,
identity-map/UnitOfWork lifetime, transaction failure and concurrency, query
contracts/N+1, schema migration and version-sensitive verification. Two separate
examples will exercise ORM persistence/rollback and an atomic DBAL operation.

The ten-path baseline and before copies are at
`/tmp/af-k08-doctrine-5x8bysut/baseline.json`; 122 other files are guarded. Scope:
this plan, the combined entry, its catalog resource list, one research note,
four `standards/doctrine/` sections and two optional examples. Dependencies and
database fixtures stay under `/tmp`; no production connection or schema change.

Verify exact executable examples against installed versions, meaningful database
success/failure behavior, types/autoload/mapping, selected resources and portable
native reading routes. Record results and limits here and stop for user review.

### K08 result and verification

Delivered the [Doctrine research note](../research/2026-09-21-doctrine-engineering-practices.md),
updated [combined entry](../../standards/php-symfony-doctrine.md), four conditional
sections and two optional runnable examples. Research covers all eight areas,
with primary evidence checked on 2026-09-21, R/D/O strengths, alternatives, costs
and version limits. It covers ORM and standalone DBAL without selecting a new
application architecture or requiring repositories, rich counterparts for read
models, a bus, custom types or a migration to a different database abstraction.

The entry is **79 lines / 630 whitespace-separated words**, down from 87 / 689.
PHP and Symfony essentials and all eight existing reading routes are unchanged.
The existing domain-placement policy is preserved verbatim in the conditional
models section; the entry retains its essential decision and a direct link.
The framework file-move obligation is unchanged. DBAL does not require reading
ORM-specific guidance merely because it receives the combined bundle.

The catalog retains 17 profile IDs. Only six Doctrine resources were appended to
the combined profile's existing 12; there are now 18 resources. Discovery and
composition code are unchanged. Current discovery recognizes `doctrine/orm`;
a DBAL-only Composer manifest still selects the profile through its PHP fact,
without claiming a separate DBAL/Doctrine fact. A Doctrine-only passport also
selects it. Research remains uncopied; details/examples remain conditional, with
no additional automatic native routes.

The [ORM example](../../standards/doctrine/examples/orm-unit-of-work.md) uses a
mapped entity with private state, an intent method and optimistic version. It
distinguishes in-memory identity from persisted reloads, catches a competing
version, and shows why failed contexts/objects must be discarded after rollback.
The [DBAL example](../../standards/doctrine/examples/dbal-reservation.md) performs
a conditional stock update and reservation insert in one owned transaction. It
preserves stock on refusal or second-write failure, binds SQL-like inputs as data,
distinguishes zero from absence and rejects ambiguous nested ownership. Duplicate
references deliberately fail; no idempotent-success protocol is claimed.

Checks completed on the resulting artifacts:

| Check | Result and scope |
| --- | --- |
| Direct release pages, installed manifests/source and locks | PHP 8.3.6 CLI NTS, Composer 2.10.3, PHPStan 2.2.14, ORM 3.7.1, DBAL 4.4.4, Collections 2.6.0, Persistence 4.2.0, Symfony Cache 7.4.19, SQLite 3.45.1; ORM and DBAL PHP requirements distinguished |
| Exact Markdown extraction and `php -l` | Five PHP files and two Composer manifests match the tested temporary projects; syntax checks passed |
| Composer `--no-plugins --no-scripts validate --strict --no-interaction`, `dump-autoload --optimize --strict-psr --strict-ambiguous --no-interaction`, `check-platform-reqs --no-dev --no-interaction` in both fixtures | Manifests/locks, optimized PSR-4/duplicate-class checks and actual platform requirements passed. DBAL's directly used Filter extension was declared; lock refresh retained all four package versions and final validate/platform checks passed |
| `php -d zend.assertions=-1 tests/run.php` in `examples/orm-unit-of-work` | Mapping validation and schema comparison, persist/flush/clear/reload, identity reuse, refusal without mutation, stale-version conflict, manager closure, rollback after an executed flush, database uniqueness failure and absence passed |
| `php -d zend.assertions=-1 tests/run.php` in `examples/dbal-reservation` | Atomic acceptance/refusal, bound SQL-like values, absence/zero, exact depletion, rollback of the first write on second-write failure, and preservation of a caller transaction on rejected nesting passed |
| `php -d memory_limit=512M phpstan.phar analyse --configuration=phpstan.neon --no-progress --debug` | All five source/test files passed at max = level 10, PHP target 80200, without ignores/baselines or unchecked casts; ORM callback-contract/dead-code findings corrected and rechecked |
| `python3 -m pytest -q tests/test_rules.py tests/test_workspace.py` | 35 passed in 1.24s: existing resource/composition/discovery and independent-opening checks |
| `PYTHONPATH=src python3 /tmp/af-k08-doctrine-5x8bysut/check_delivery.py` | Codex, Claude Code and Cursor previews passed for plain PHP, ORM dependency, DBAL-only Composer and Doctrine-only passport: 18 resources/digests, exact PHP/JSON, conditional native routes, four independent copies/recompositions per client, unrelated Go exclusion; 2,200 local links checked |
| `python3 /tmp/af-k08-doctrine-5x8bysut/check_artifacts.py` | Ten scoped changes; Markdown fences/table columns and local links/anchors; exact examples; catalog-only additions; preserved PHP/Symfony guidance, relocated model policy, file-move rule, earlier results and K09–K19 queue; all 122 guarded files unchanged; scoped diff retained |

Example commands use `/tmp/af-k08-doctrine-5x8bysut/php` with the previously
verified K06 Composer/PHPStan PHARs. The stage directory retains before copies,
baseline hashes, `k08.diff`, extracted example projects/locks and verification logs.
No source/tests, earlier topic resources/research, shared policy, external project
or native-adoption stage was changed.

Setup reused the temporary K06/K07 PHP runtime. Matching Ubuntu
8.3.6-0ubuntu0.24.04.11 SQLite and curl modules were downloaded, SHA256-checked
against package metadata and extracted under `/tmp`. Composer's initial PHP-stream
access timed out; curl could read the same public metadata. The temporary curl
extension with IPv4 completed installation (25 ORM-fixture packages, four DBAL
packages). No system-wide installation was performed. This does not establish a
network reliability guarantee or add curl as a consumer dependency.

Inline review reconciled the stale search snippet with actual ORM 3.7.1 release
and lock evidence; corrected the ORM callback parameter to EntityManagerInterface
and removed dead code after an always-throwing callback; verified the exact DBAL
upgrade link and declared the Filter extension. It also checked model-policy
preservation, ORM versus DBAL context conditions, real rollback rather than mock
call counts, explicit transaction ownership and the lack of blanket pattern or
migration requirements. No material in-scope finding remains unresolved.

The optimistic check uses two independently loaded versions in a deterministic
interleaving, not simultaneous writers. No target-server isolation/deadlock,
connection loss/ambiguous commit, association hydration/cascade example, benchmark,
other-driver scalar conversion, native PHP 8.4 lazy object, migration deployment
or multi-version runtime matrix was executed. Migrations 3.9 was researched only.
SQLite fixture SchemaTool/DDL checks are not production migration evidence.
Synthetic delivery verifies copied resources and routes, not actual model reading
compliance or token savings. P3–P7 remain planned.

**Checkpoint:** K08 is complete and ready for the user's review. **Next topic:**
K09 JavaScript; do not begin it until the user authorizes continuation.

### K09 working scope

The user authorized K09 on 2026-09-21 after the K08 checkpoint. Execute inline
with Superpowers under the existing adaptation. Cover JavaScript language and
cross-host engineering decisions across all eight research areas. Preserve the
existing TypeScript and Node.js obligations, earlier results and K10–K19 queue;
do not start TypeScript/Node.js adoption or the native-adapter stages.

Baseline and before copies: `/tmp/af-k09-javascript-xpgw2_ck/baseline.json`, with
ten scoped paths and 129 guarded files. Scope is this plan, the combined JS entry,
its catalog resources, one research note, four conditional JavaScript sections
and two separate examples. Keep shared-language guidance applicable to browser
code; server-specific responsibilities remain conditional on server work.

Research module boundaries/construction, value contracts and mutation, promises
and cancellation/effect ownership, verification, security and compatibility.
Examples will distinguish input validation from live business state, and awaited
operation ownership from unobserved background work. Reuse the installed Node
24.13.0 runner; examples have no runtime dependencies. Any static-check tooling
stays in the stage's temporary projects, without migrating code to TypeScript.

Verify exact executable snippets, relevant behavior/failures and JSDoc contracts,
catalog delivery and independent reading routes. Record evidence and limitations
here, then stop for the user's review before K10 TypeScript.

### K09 result and verification

Delivered the [JavaScript research note](../research/2026-09-21-javascript-engineering-practices.md),
updated [combined entry](../../standards/nodejs-typescript.md), four conditional
language sections and two separate runnable examples. The research covers all
eight areas with primary evidence checked on 2026-09-21, R/D/O strengths, simpler
alternatives, costs and version/host limits. It distinguishes ECMAScript semantics
from project architecture and from browser/Node APIs, without requiring a new
validator, DI container, class hierarchy, module format or source-language migration.

The entry is **82 lines / 656 whitespace-separated words**, previously 68 / 566.
Four task conditions route to details; optional examples remain outside the entry.
Shared JavaScript guidance applies across hosts, while server responsibilities
remain conditional on server work. Existing typed-boundary and server-execution
bullets and verification obligations are preserved verbatim. Module grouping is
relocated verbatim into its section, with an explicit server/browser qualification.
Mandatory TypeScript and NestJS/Next.js references remain intact; those profiles
and their detailed adoption stages were not changed.

The catalog retains 17 IDs; its only change is six JavaScript resources on the
existing `nodejs-typescript` profile. Selection, dependencies, globs, source code
and templates remain unchanged. Current package inspection records `nodejs` even
for browser packages without `engines.node`, so that fact does not imply server
code. A metadata-free browser script can explicitly select this profile; no new
JavaScript discovery fact was added. Research remains uncopied, and resources
remain conditional rather than additional automatic native reading routes.

The [input/state example](../../standards/javascript/examples/input-state.md)
contrasts a named plain request and a private-state Capacity class. It rejects
unsupported input, preserves explicit null/empty string and refuses unavailable
capacity without mutation. Frozen primitive snapshots do not expose internal
state. The [async ownership example](../../standards/javascript/examples/async-ownership.md)
coordinates two required reads, propagates cancellation, captures synchronous
adapter throws, joins sibling cleanup and preserves the original failure. It
requires cooperative, eventually settling dependencies; no forced cancellation
or automatic transaction guarantee is implied.

Checks completed on the resulting artifacts:

| Check | Result and scope |
| --- | --- |
| Installed runtime, `npm ls --depth=0`, checker version and lock inspection | Node 24.13.0, npm 11.6.2, TypeScript 5.9.3 and `@types/node` 24.13.6; both temporary npm locks retain resolved package integrity values; zero runtime dependencies |
| `node --check` for every example source/test file | All five JavaScript files passed syntax checks; exact Markdown JS and four JSON blocks match the tested files |
| `npm run check` in both examples | Strict `allowJs`/`checkJs`, no emit, unchecked-index/optional-property and unused checks passed for source and tests; no ignores, baselines, `any` or unchecked DTO casts |
| `npm test` in both examples | Passed with `node --unhandled-rejections=strict --test`; local subprocess reporting exposed a file aggregate, not individual scenario counts |
| `node --unhandled-rejections=strict tests/reservation.test.js` | 20 passed, zero failed/cancelled/skipped: null/empty string, 16 invalid representations, syntax-error cause, state-dependent refusal without mutation, snapshot isolation, exact exhaustion and invalid direct calls |
| `node --unhandled-rejections=strict tests/overview.test.js` | Six passed, zero failed/cancelled/skipped: both results, sibling failure with delayed cleanup, synchronous adapter failure, pre-abort, parent cancellation and rejected late success; deterministic promise gates, no sleeps/sockets |
| Temporary intentional failing node:test probe | Exit 1 with ordinary `--test`, `--test-isolation=none` and direct execution; verified failure propagation while investigating the aggregate-reporting behavior |
| `python3 -m pytest -q tests/test_rules.py tests/test_workspace.py` | 35 passed in 1.33s: existing discovery/resource/composition and independent-opening checks |
| `PYTHONPATH=src python3 /tmp/af-k09-javascript-xpgw2_ck/check_delivery.py` | Codex, Claude Code and Cursor passed for browser package, Node engine, NestJS+TypeScript dependencies, Node-only passport and explicit metadata-free selection: six resources/digests, exact JS/JSON, conditional native routes, five independent copies/recompositions per client, unrelated Go exclusion; 1,644 local links checked |
| `python3 /tmp/af-k09-javascript-xpgw2_ck/check_artifacts.py` | Ten scoped changes; Markdown fences/table columns and local links/anchors; exact runnable blocks; catalog-only additions; preserved typed/server/module rules, framework references, earlier results and K10–K19 queue; all 129 guarded files unchanged; scoped diff retained |

Temporary setup used the existing Node/npm installation and installed only the
pinned development tools under `/tmp`, with lifecycle scripts disabled. Both npm
installs completed; installed/lock versions and integrity fields were inspected.
No system or workspace dependencies were changed. The stage directory retains
before copies, baseline hashes, `k09.diff`, executable projects, locks and check
evidence. Existing valid checks were reused after documentation-only bookkeeping.

Inline review checked coverage and policy ownership, method receivers, own versus
inherited fields, static versus executed validation, shallow versus deep ownership,
state assumptions across await, Promise.all's actual rejection handling, cooperative
abort/cleanup, module-loader limits and real native bundle contents. An initially
ambiguous test report was investigated with a failing probe and direct scenario
execution; it required no example-code change. No material in-scope finding remains
unresolved. Reported commands/results distinguish runtime evidence from static
declarations and synthetic delivery.

Only one Node runtime/toolchain was executed. No browser/DOM/fetch, workers/shared
memory, real network cancellation, timer deadline/backpressure, persisted transaction,
simultaneous writers, durable handoff, benchmark or multi-version matrix was run.
Cancellation can wait indefinitely for a dependency that violates its settlement
contract; no promise wrapper can undo a completed external write. Input limits
are example UTF-16 limits, not transport byte or product grapheme limits.
Synthetic delivery verifies resource availability and native routes, not model
reading compliance or token savings. Source/tests, shared policy, previous topic
resources/research and the native-adoption plan are unchanged; P3–P7 remain planned.

**Checkpoint:** K09 is complete and ready for the user's review. **Next topic:**
K10 TypeScript; do not begin it until the user authorizes continuation.

### K10 working scope

The user accepted K09 and authorized K10 on 2026-09-21. Execute TypeScript
research/adoption inline with Superpowers under the workspace adaptation, across
all eight research areas. Preserve the mandatory strict/no-any/named-interface
policy, K09 language ownership, previous results and the K11–K19 queue. Stop for
review before Node.js; native-adapter stages remain outside this scope.

Baseline and before copies: `/tmp/af-k10-typescript-nsn38qky/baseline.json`, with
ten scoped paths and 136 guarded files. Scope is this plan, the TypeScript entry,
its catalog resources, one research note, four conditional sections and two
separate examples. Do not add profile IDs, dependencies or automatic reading
routes; TypeScript-only selection must remain usable without assuming Node.js.

Cover contract ownership/construction, narrowing and runtime validation, state
and readonly limits, generics/unions/effect contracts, actual module/toolchain
checks and version-sensitive migration. Examples will distinguish compiler
guarantees from runtime validation and stateful refusal, and demonstrate typed
operation/dependency contracts without unchecked casts or invented hierarchies.

Use the existing Node runner with temporary pinned TypeScript/lint tools as needed.
Check emitted execution, meaningful negative type cases, typed lint enforcement,
exact examples, selected resource delivery and independent opening. Research
TypeScript 6/7 compatibility explicitly; documentation about a newer version does
not authorize upgrading the framework workspace or consumer projects.

### K10 result and verification

Delivered the [TypeScript research note](../research/2026-09-21-typescript-engineering-practices.md),
updated [entry](../../standards/typescript.md), four conditional sections and two
separate runnable examples. Research covers all eight areas, with primary evidence
checked on 2026-09-21, R/D/O strengths, applicability, simpler alternatives, costs
and compiler/host limits. It distinguishes static contracts from runtime validation,
ownership, authorization and persistence guarantees without requiring DTO classes,
brands, a functional library, repositories or an incidental toolchain migration.

The entry is **74 lines / 569 whitespace-separated words**, previously 67 / 505.
All original mandatory rules and the external-data block remain verbatim. The
enforceability/legacy-migration block is relocated verbatim into the conditional
toolchain section, with an essential summary/direct route in the entry. Four
task conditions lead to details; examples and research remain optional. K09's
shared JavaScript entry/resources, common rules and framework profiles are unchanged.

The catalog retains 17 profile IDs. Its only change is six resources on the
existing `typescript` profile; dependencies, globs, selection/composition code and
templates are unchanged. TypeScript-only passports and explicit selection remain
independent of a Node/server profile. A package dependency named `typescript`,
including an npm alias under that key, is recorded as a declared constraint;
it is not evidence of the installed compiler/API version. Next.js/NestJS continue
to select TypeScript through existing profile dependencies.

The existing inspector does not recognize a compiler installed solely under an
arbitrary alias such as `@typescript/native` as a TypeScript fact. That fixture
retains its existing selection behavior; a passport or explicit profile supplies
the declaration when needed. K10 does not introduce discovery heuristics. Research
is not copied, and resource availability does not add automatic native reading
routes or embed the sections/examples in ENTRY/AGENTS/CLAUDE/Cursor instructions.

The [validated-command example](../../standards/typescript/examples/validated-command.md)
uses a named plain command, runtime narrowing, exact optional presence, private
quota state and a discriminated outcome with exhaustive consumer handling. Valid
input can still be refused without mutation; number annotations alone do not
establish ranges. The [typed-operation example](../../standards/typescript/examples/typed-operation.md)
ties a generic result to an executed decoder behind a small adapter capability.
It projects public fields, preserves failures and rejects cancellation before
starting work or decoding a late response. It does not force an uncooperative
source to terminate or provide an external transaction.

Checks completed on the resulting artifacts:

| Check | Result and scope |
| --- | --- |
| Public metadata, installed manifests, locks, `npm ls --depth=0`, both compiler `--version` commands and imported API version | Node 24.13.0, npm 11.6.2, native TypeScript 7.0.2, compatibility package 6.0.2 resolving compiler/API 6.0.3, ESLint 10.11.0, typescript-eslint 8.70.0, `@types/node` 24.13.6; package integrity fields inspected; zero runtime package dependencies |
| `npm run check` and `npm run check:compat` in both fixtures | Native 7.0.2 and 6.0.3 checked all five source/test TS files with strict project config, additional absence/index checks, explicit public signatures and no suppressions |
| `npm run lint` in both fixtures | Typed project-service lint passed with no errors/warnings, explicit-any and unsafe-operation rules, consistent type imports and floating-promise checks |
| `npm run build`, followed by `node --check` on all five emitted JS files | Native TypeScript emitted the declared ESM/ES2022 build; syntax and actual `.js` import paths passed. Exact Markdown contains five tested TS files, two lint configs and four matching JSON manifests/configs |
| `npm test` in `examples/validated-command` | Four tests passed: omitted/null/empty note, thirteen invalid representations, current-usage refusal without partial mutation, frozen independent snapshots, direct invalid numeric calls and zero boundary |
| `npm test` in `examples/typed-operation` | Five tests passed: two decoder/result relationships, projection, invalid remote data, synchronous/asynchronous failure identity, pre-abort and cancellation before decoding; zero failed/cancelled/skipped across both examples |
| `python3 /tmp/af-k10-typescript-nsn38qky/check_negative.py` | Seven isolated invalid consumers rejected by both compilers: explicit undefined for optional field (TS2375), readonly write (TS2540), unknown assignment, missing union variant, unchecked index, wrong generic result and narrower callback (TS2322); exact diagnostic sets checked |
| Same negative-check command, isolated lint probe | Both strict compilers accepted the controlled explicit/vendor-any and unowned-promise probe; typed lint rejected all seven expected categories: explicit any, unsafe assignment/argument/call/member access/return and floating promises. Probe was never emitted/executed and was removed from normal tests; positive source/test hashes unchanged |
| `python3 -m pytest -q tests/test_rules.py tests/test_workspace.py` | 35 passed in 1.38s: existing discovery/resource/composition and independent-opening checks |
| `PYTHONPATH=src python3 /tmp/af-k10-typescript-nsn38qky/check_delivery.py` | Codex, Claude Code and Cursor passed for a TS package alias, Next/Nest dependency routes, TS-only passport and explicit metadata-free selection: six resources/digests, exact TS/JS/JSON, five independent copies/recompositions per client, no forced Node profile; plain-JS/Go exclusion and native-alias discovery limit; 2,088 local links checked |
| `python3 /tmp/af-k10-typescript-nsn38qky/check_artifacts.py` | Ten scoped changes; Markdown fences/table columns/local links and anchors; exact runnable blocks; catalog-only additions; preserved mandatory/external-data policy, relocated enforceability, earlier results and K11–K19 queue; all 136 guarded files unchanged; scoped diff retained |

Temporary setup used the existing Node/npm runtime and installed pinned development
tools with lifecycle scripts disabled. The initial ESLint 9 installation produced
an unsupported-version warning; final fixtures use the checked compatible ESLint
10.11.0. TypeScript 7's native executable and TypeScript 6's programmatic API use
the documented alias arrangement. Inspection of the compatibility wrapper and
lock explained why package 6.0.2 executes compiler 6.0.3; the final record reports
both instead of inferring the tool version from its package label.

The stage directory retains baseline/before copies, `k10.diff`, tested projects,
locks, negative probes and verification logs. No workspace/system dependency,
production application, source/test file, earlier topic artifact or external project
was changed. Valid example/delivery checks were reused after plan-only bookkeeping.

Inline review covered requirement preservation and conditional context, interface
versus schema ownership, structural/readonly limits, real validation and stateful
refusal, exhaustive outcomes, generic input/result relationships, callback variance,
any leakage, actual compiler/API versions, emitted module paths and portable native
bundles. Meaningful negative probes verified specific diagnostics and lint rules;
no cast, suppression or runtime-code repair was needed. No material in-scope
finding remains unresolved.

The examples run one Node version and type-check with two compilers; only native
7 output was executed. No browser/DOM, real network or database, JSX/framework
generation, decorator injection, third-party schema validator, simultaneous writers,
monorepo build, published-package consumer matrix, editor integration, benchmark or
forced cancellation was tested. The adapter fakes establish the demonstrated
protocol, not real I/O termination or transaction guarantees. Synthetic delivery
does not prove model reading compliance or token savings. P3–P7 remain planned.

**Checkpoint:** K10 is complete and ready for the user's review. **Next topic:**
K11 Node.js; do not begin it until the user authorizes continuation.

### K11 execution scope

The user authorized K11 on 2026-09-21 after the K10 checkpoint. Execute inline
with Superpowers under the existing adaptation. Cover Node.js runtime decisions
across all eight research areas. Preserve K09 shared JavaScript guidance, K10
strict typing, earlier results and the K12–K19 queue; stop before NestJS adoption.

Baseline and before copies: `/tmp/af-k11-nodejs-msi44q3c/baseline.json`, with ten
scoped paths and 143 guarded files. Scope is this plan, the combined JS/Node entry,
its catalog resources, one research note, four conditional Node.js sections and
two separate examples. Node-specific reading remains conditional on work that
actually runs in Node; package metadata alone does not make browser code server code.

Research runtime assembly/modules/configuration, bounded I/O and concurrency,
HTTP/integration contracts, process/resource lifetime and verification. Examples
will exercise a byte-limited stream pipeline and HTTP shutdown with tracked
application work, cancellation and dependency release. Use the installed Node
24.13.0 for local examples, with no runtime packages; it is an execution baseline,
not a recommendation to deploy that old patch. Reuse temporary static-check tools
from the prior stage where suitable; do not change workspace/global dependencies.

Verify exact runnable snippets and meaningful success/failure behavior, existing
resource/composition tests, all three client routes and independent repositories.
Record evidence and limits here, then stop for the user's review before K12 NestJS.

### K11 result and verification

Delivered the [Node.js research note](../research/2026-09-21-nodejs-engineering-practices.md),
updated [combined entry](../../standards/nodejs-typescript.md), four conditional
runtime sections and two separate executable examples. The research covers all
eight areas with primary evidence checked on 2026-09-21, R/D/O strengths, simpler
alternatives, costs and version limits. It separates runtime facts from project
assembly/ownership policy and from shared JavaScript/TypeScript requirements.

The entry is **86 lines / 676 whitespace-separated words**, previously 82 / 656.
The versions/modules and typed-boundary blocks and all four JavaScript task routes
are preserved verbatim. The original server-obligation block is relocated verbatim
to runtime/composition, with an essential entry summary. Four new routes select Node
sections only for code actually running in that host. Browser package metadata does
not make Node server responsibilities apply to browser code. TypeScript remains
mandatory for TS; NestJS still selects its existing dependent profiles.

Adoption covers explicit startup/configuration and reusable clients; actual module
and direct-TS execution; event-loop versus worker capacity; streams/backpressure and
byte limits; files and callback ownership; HTTP receipt versus operation deadlines;
status/body/URL boundaries; connection/transaction/retry ownership; shutdown and
resource ordering; diagnostics, security, supported versions and sufficient checks.
No module-format migration, DI container, worker pool, queue or ORM architecture is
prescribed without a concrete need. Six Node resources are appended to the existing
six JS resources; all 17 IDs, dependency relationships, globs and discovery code remain.

The [bounded stream example](../../standards/nodejs/examples/bounded-stream.md)
uses a counted transform and awaited pipeline. It distinguishes byte budget from
buffer pressure, owns stream cleanup after argument validation and exposes partial
output on failure without claiming atomic publication. The [shutdown example](../../standards/nodejs/examples/graceful-server.md)
tracks application promises separately from HTTP sockets, closes admission before
taking its drain snapshot, aborts cooperative work at the grace deadline, releases
the dependency afterward and returns the same stop promise on repeated calls.
The dependency's nonthrowing reporter and cooperative cancellation are explicit
contracts; no generic dependency container or process-signal scaffold is added.

Checks completed on the resulting artifacts:

| Check | Result and scope |
| --- | --- |
| `node --version`, temporary `tsc --version` and `@types/node/package.json` | Node 24.13.0; reused native TypeScript 7.0.2 and Node types 24.13.6; no new installs or runtime dependencies |
| `node --check` on all four `.mjs` files | All syntax checks passed with actual `.mjs` imports |
| Temporary compiler with `--ignoreConfig --allowJs --checkJs --noEmit --strict --noUncheckedIndexedAccess --exactOptionalPropertyTypes --noUnusedLocals --noUnusedParameters --module nodenext --target es2024 --types node --typeRoots <temporary @types path>` and all four files | Passed without diagnostics or suppressions; exact command retained in `static-reviewed-checks.log` |
| `node --unhandled-rejections=strict /tmp/af-k11-nodejs-msi44q3c/examples/bounded-stream/run.mjs` | Six passed: real file and empty copy with closed handles, byte-limit refusal and partial output, source/sink error identity, pre/in-flight abort, held-sink backpressure and invalid capacity before ownership transfer |
| `node --unhandled-rejections=strict /tmp/af-k11-nodejs-msi44q3c/examples/graceful-server/run.mjs` | Six passed: admitted work and refusal of new connections, idempotent stop, deadline abort/force-close, disconnected-client cleanup before release, generic error mapping, observable release failure and independent error reporting after abort; real loopback HTTP; zero failed/cancelled/skipped in the final run |
| Same HTTP command, regression before/after fix | New regression failed with an empty report for a cleanup failure after abort, then passed after cancellation classification used the actual reason/cause; other five HTTP tests remained green |
| `python3 -m pytest -q tests/test_rules.py tests/test_workspace.py` | 35 passed in 1.51s: existing catalog/resource/composition and independent-opening tests |
| `PYTHONPATH=src python3 /tmp/af-k11-nodejs-msi44q3c/check_delivery.py reviewed` | Codex, Claude Code and Cursor passed browser-package, Node-engine, Nest+TS, Node-passport and explicit-profile routes: all 12 JS/Node resources and digests, exact example code, five independent copies/recompositions per client, Go/TS-only exclusion, 2,118 local links |
| `python3 /tmp/af-k11-nodejs-msi44q3c/check_artifacts.py` | Ten scoped changes; Markdown fences/table columns/local links and anchors; exact runnable blocks; only six Node catalog additions; preserved typed boundaries/JS routes, relocated server obligations, earlier results and K12–K19 queue; 143 guarded files unchanged; scoped diff retained |

The first HTTP run failed at every `listen` with sandbox `EPERM` before executing
application behavior. After confirming that boundary, the same temporary loopback
checks passed with the tool's approved sandbox escalation. No external network
service was contacted by the examples. Research used read-only public documentation.
The final example uses source files identical to its Markdown snippets; reviewed
static and delivery checks were repeated after the cancellation fix. The unchanged
stream example and catalog-selection test evidence were reused. Final plan-only
bookkeeping requires only the artifact/scope check.

Inline review covered host conditions and preserved obligations, actual module/TS
limits, pressure versus total bytes, pre-abort and both stream failure directions,
HTTP admission/task/snapshot ordering, early client disconnect, timer/listener cleanup,
release ordering/failure, cancellation identity and sensitive error mapping. It found
and fixed the cancellation-reporting defect with a meaningful failing regression;
no material in-scope finding remains unresolved. This is inline review under the
saved workspace adaptation, not an independent reviewer or native-client pilot.

The stage directory `/tmp/af-k11-nodejs-msi44q3c` retains baseline/before copies,
`k11.diff`, exact projects and verification logs, including the diagnosed sandbox
failure and red/green regression. No production source/test file, earlier topic
artifact, global/workspace dependency or external project was changed.

Limits: examples execute only the installed Node 24.13.0 on this host; that old
patch is not recommended for deployment. No real database, remote fetch, TLS/proxy,
load benchmark, worker pool, child-process tree, OS-signal or HTTP2/WebSocket lifecycle
was exercised. The HTTP example requires eventually settling cooperative dependencies;
its drain timer cannot forcibly stop arbitrary code and does not bound dependency
release. Real deployment needs its own operational budgets and supervisor. Synthetic
bundle checks establish artifact routes, not model reading behavior or token savings.
P3–P7 remain planned.

**Checkpoint:** K11 is complete and ready for the user's review. **Next topic:**
K12 NestJS; do not begin it until the user authorizes continuation.


### K12 execution scope

The user confirmed K11 review and authorized the next stage on 2026-09-21. Execute
only K12 inline with Superpowers under the workspace adaptation; stop before K13
React. Preserve existing Nest requirements, the JS/Node/TypeScript dependencies,
earlier results and the K13–K19 queue. The approved design already specifies short
entry, task-conditioned sections, separate examples and no automatic link expansion.

Baseline and before copies: `/tmp/af-k12-nestjs-29dmykl4/baseline.json`, with ten
scoped paths and 150 guarded files. Scope is this plan, `standards/nestjs.md`, its
catalog resources, a research note, four conditional Nest sections and two examples.
Research all eight areas, with particular attention to actual pipe/decorator
metadata, nested validation, transformation, serialization and lifecycle ownership.

The examples will exercise a real Nest HTTP adapter's validation/output boundary
and a separate provider/module lifecycle with an independent application contract.
Verify actual framework/package versions and emitted decorators, use isolated
`/tmp` projects, and keep workspace/global dependencies unchanged. Research current
Nest 12 versus existing-project compatibility without mandating an upgrade or a
new schema/DI/persistence architecture. Preserve explicit version limits.

Verify exact executable snippets, meaningful boundary/failure cases and strict TS,
existing resource/composition tests, three clients and independent repository routes.
Record actual evidence and remaining limits here, then stop for user review.

### K12 result and verification

Delivered the [NestJS research note](../research/2026-09-21-nestjs-engineering-practices.md),
short [entry](../../standards/nestjs.md), four conditional sections and two separate
executable examples. Research covers all eight areas with primary evidence checked
on 2026-09-21, R/D/O strengths, simpler alternatives, costs and version limits.
It distinguishes Nest mechanisms from project architecture policy, preserves shared
JavaScript/Node/TypeScript ownership and does not mandate a Nest 12 migration.

The entry is **53 lines / 403 whitespace-separated words**, previously 67 / 551.
Its three original requirement blocks are relocated verbatim to their conditional
owners. Four task routes cover modules/providers, transport contracts, application
work/lifecycle and verification/operations. Six resources are added only to the
existing Nest profile; all 17 IDs, dependencies, globs and discovery code remain.
The mandatory TypeScript dependency and inherited JS/Node materials are preserved.

Adoption covers runtime injection tokens, factories and alias identity; explicit
module exports and scope costs; DTO value imports and emitted metadata; nested
validation, null/unknown-field/coercion policy; guard/pipe order and global DI;
actual output projection; business invariants, transaction/effect ownership and
awaited resource release; configuration, operations and version-sensitive behavior.
Class-based response serialization is not described as class-validator execution.
Nest 12 Standard Schema dispatch details are source observations, with explicit
limits, rather than a claimed executed schema-library integration.

The [HTTP example](../../standards/nestjs/examples/validated-command.md) uses a real
initialized Nest/Fastify pipeline, registered global validation and serialization,
nested DTOs and an independent inventory operation. It rejects invalid input before
mutation, retains the domain invariant outside HTTP, maps current-stock refusal
and verifies the actual serialized response omits the internal field. The
[provider example](../../standards/nestjs/examples/provider-lifecycle.md) imports an
exported capability, aliases one async-created file adapter and constructs a pure
consumer through a factory. It verifies acquisition failure, one-report behavior,
actual handle closure and awaited asynchronous release.

Checks completed on the resulting artifacts:

| Check | Result and scope |
| --- | --- |
| Public npm metadata, `node --version`, `npm ls --depth=0`, `tsc --version`, `tsc6 --version` and installed package/lock inspection | Nest common/core/platform-fastify/testing 12.0.4 where used; Node 24.13.0; Fastify 5.12.5; class-validator 0.15.1; class-transformer 0.5.1; reflect-metadata 0.2.2; RxJS 7.8.2; native TypeScript 7.0.2; compatibility package 6.0.2 resolving compiler/API 6.0.3; ESLint 10.11.0; typescript-eslint 8.70.0; Node types 24.13.6 |
| `npm run check` in both temporary examples | Native TS 7 strict checks passed, including unchecked indexing, exact optional properties, unused declarations and emitted-metadata configuration; no suppression or `any` escape |
| `npm run lint` in both temporary examples | Typed ESLint passed with zero warnings, including unsafe operations, unowned promises and type-import rules; lint uses the compatibility TS API |
| `npm run build`, `node --check` on emitted files and metadata inspection | Both builds and all 13 emitted JS syntax checks passed; controller emission retains the DTO value import and `design:paramtypes` metadata |
| `npm test` in `examples/validated-command` | Five passed, zero failed/cancelled/skipped: nested input and final output; fifteen malformed/extra/coerced representations with no mutation; state refusal with no partial mutation; adapter body budget; domain invariants for direct callers |
| `npm test` in `examples/provider-lifecycle` | Five passed, zero failed/cancelled/skipped: real exported token and alias identity; owned file closure; awaited asynchronous release; rejected exclusive acquisition without overwrite; pure invalid-command checks before sink effects |
| Installed 12.0.4 validation/serialization source inspection | Verified class-transformer-only class serialization, ValidationPipe's explicit unknown-value default and Standard Schema dispatch/bypass behavior; inspected source digests retained |
| `python3 -m pytest -q tests/test_rules.py tests/test_workspace.py` | 35 passed in 1.69s: existing catalog/resource/composition and independent-opening tests |
| `PYTHONPATH=src python3 /tmp/af-k12-nestjs-29dmykl4/check_delivery.py reviewed` | Codex, Claude Code and Cursor passed Nest 12/11 metadata, typed, passport and explicit routes; six Nest plus 18 inherited resources and digests; exact example code/configuration; five independent copies/recompositions per client; Node/TS-only/Go exclusion; 3,370 local links |
| `python3 /tmp/af-k12-nestjs-29dmykl4/check_artifacts.py` | Ten scoped changes; Markdown fences/table columns/local links and anchors; exact 13 TS, two JS and four JSON executable blocks; only six Nest catalog resources; three relocated obligation blocks, earlier results and K13–K19 queue preserved; 150 guarded files unchanged; scoped diff retained |

Both `npm test` scripts use `node --unhandled-rejections=strict`. The first provider
type check exposed `Promise.withResolvers` against an inherited ES2022 library.
Its example now explicitly targets ES2024 on the stated Node runtime; strict checks,
typed lint, build and all five cases passed after that correction. No casts or
suppression were added. Required npm packages were installed only in the two scoped
temporary projects with lifecycle scripts disabled; pinned direct versions, resolved
locks and integrities are retained. A stalled public-metadata fetch was replaced
with bounded npm lookups. Failed tagged-source web fetches were not used as evidence;
the actual installed, pinned source was inspected instead.

Inline review covered preserved obligations and conditional loading, actual
decorator/DI/adapter paths, nested and unknown input, output projection versus
validation, state refusal without effects, provider identity/exports and awaited
cleanup. Review also clarified that awaiting an Observable does not subscribe to
it; the application section now distinguishes promises, framework consumption and
owned subscriptions/conversion. Delivery checks were repeated after that prose
change. Executable inputs remained identical to their passing checks, so their
evidence was reused; final plan-only bookkeeping needs only the artifact/scope check.
No material in-scope finding remains unresolved. Review was inline under the saved
workspace adaptation, not an independent reviewer or a native-client pilot.

The stage directory `/tmp/af-k12-nestjs-29dmykl4` retains baseline/before copies,
`k12.diff`, exact example projects, package/source evidence and verification logs.
No production source/test file, earlier topic artifact, workspace/global dependency
or external project was changed.

Limits: examples execute only the stated Nest 12.0.4, Node and Fastify versions on
this host. The Node patch is execution evidence, not a deployment recommendation;
no Nest CLI was run. Nest 11 metadata delivery is not a Nest 11 runtime test.
No Express/legacy-major runtime matrix, schema-library integration, real database
or queue, OS-signal/concurrent shutdown, broad hook-order matrix, TCP/TLS/proxy or
load benchmark was exercised. The file sink allows one report attempt and does not
claim atomic publication, crash durability or safe retry after a partial write.
Synthetic bundle checks establish routes and portable artifacts, not model reading
behavior or token savings. P3–P7 remain planned.

**Checkpoint:** K12 is complete and ready for the user's review. **Next topic:**
K13 React; do not begin it until the user authorizes continuation.


### K13 execution scope

The user accepted K12 and authorized only K13 React on 2026-09-21. Execute inline
with Superpowers under the workspace adaptation, using the approved short-entry,
conditional-section and separate-example design. Preserve Next.js-specific rules
and the K14–K19 queue. No Git writes, native pilot or external project adoption.

Baseline and before copies: `/tmp/af-k13-react-pd1657bx/baseline.json`, with eleven
scoped paths and 157 guarded files. Scope: this plan, combined Next.js/React entry,
catalog, research note, five React sections and two examples. Metadata already
recognizes React; add that technology to the existing combined profile, without
adding an ID or selecting the Next.js feature-structure profile for React alone.
Keep Next.js instructions explicitly conditional on actual Next.js work.

Research all eight areas against primary sources. Examples use an isolated `/tmp`
project with pinned React/React DOM 19.3.0 and strict TypeScript. Exercise a form's
representation checks separately from a stateful operation, and an Effect's obsolete
success/failure and cleanup paths. Check actual rendered DOM behavior; distinguish
that from real-browser layout/accessibility, network and server evidence.

Verify catalog selection/resources, native conditional routes for three clients,
independent repository copies, exact snippets, strict types, relevant lint/build and
focused example behavior. Record actual commands/results and review limits here,
then stop for the user's review before K14 Next.js.

### K13 result and verification

Delivered the [React research note](../research/2026-09-21-react-engineering-practices.md),
short [combined entry](../../standards/nextjs.md), five conditional React sections
and two separate executable examples. Research covers all eight areas with primary
evidence checked on 2026-09-21, R/D/O strengths, alternatives, costs and version
limits. React-only work is explicitly supported without imposing Next.js rules.

The entry is **72 lines / 583 whitespace-separated words**, previously 77 / 656.
It retains existing Next.js stack/execution and mutation-revalidation
obligations, with task routes to components, state, effects, forms and verification.
Original frontend obligations are relocated to their relevant owners, including
the 250-line cohesion signal and proportional UI verification. The Next.js feature
structure is unchanged. Shared core/JS/TS/Node/process policy retains its owners.
The catalog adds seven resources and the already-recognized `react` technology to
the combined profile, plus conditional applicability wording. All 17 IDs,
dependencies and globs remain. The separate feature-structure profile stays
Next.js-only; TypeScript remains the combined profile's existing dependency.

Adoption covers pure rendering and explicit component/Hook dependencies, state
ownership/identity and reset, external stores, Effect cleanup and result races,
loader/cache ownership, forms/Actions and accessible feedback, independent business
invariants, optimistic/transition limitations, SSR/hydration distinctions, trust
boundaries, measured performance and toolchain compatibility. No blanket FSD,
store/query library, Compiler, memoization or version migration is mandated.

The [form example](../../standards/react/examples/reservation-form.md) uses React
DOM Action submission with a controlled draft, representation parsing and an
independent stock operation. It checks invalid input without mutation, current-state
refusal, pending/safe integration failure and direct operation invariants. Its
in-memory operation is a fixture, not a trusted browser backend or database.
The [Effect example](../../standards/react/examples/latest-result.md) owns abort
and publication separately, resets by query identity and associates results with
the service owner. It handles obsolete success and failure even when the port
ignores cancellation. These are focused executable examples, not a UI application.

Checks on the resulting artifacts:

| Check | Result and scope |
| --- | --- |
| Public npm metadata, `node --version`, `npm ls --depth=0`, `tsc --version`, compatibility TS API inspection | React/React DOM and types 19.3.0; Node 24.13.0; native TS 7.0.2; compatibility package 6.0.2/API 6.0.3; ESLint 10.11.0, typescript-eslint 8.70.0, Hooks plugin 7.1.1; Testing Library 16.3.3, jsdom 30.1.0/types 30.0.0, Node types 24.13.6 |
| `npm run check`, `npm run lint`, `npm run build` in the temporary example project | Strict TS including unchecked indexing, exact optional properties and unused declarations; typed unsafe-operation/promise checks and recommended React Hooks lint; JSX/ESM build all passed with zero diagnostics/warnings |
| `node --check` on six emitted `.js` files | All six passed; actual `.js` imports and React JSX runtime emission |
| `npm test` → `npm run test:form` and `npm run test:latest` | Four form and five Effect tests passed, zero failed/cancelled/skipped; both invoke Node with `--unhandled-rejections=strict` and the jsdom preload |
| Focused service-owner regression with/without the identity guard | Four existing Effect checks passed and the new check failed when old-owner output remained; all five passed with the guard restored |
| `PYTHONPATH=src python3 /tmp/af-k13-react-pd1657bx/check_selection.py` before/after catalog change | Recognized React-only metadata initially lacked the combined profile; afterward it selected that profile without Next.js feature structure |
| `python3 -m pytest -q tests/test_rules.py tests/test_workspace.py` | 35 passed in 1.62s; existing selection/resource/composition and independent-opening checks |
| `PYTHONPATH=src python3 /tmp/af-k13-react-pd1657bx/check_delivery.py reviewed` | Codex, Claude Code and Cursor: React 19/18, Next.js, typed, passport and explicit routes; seven React and six TS resources/digests, exact snippets, six independent copies/recompositions per client, Node/TS/Go exclusion, 3,560 local links; no recursive/native example expansion |
| `python3 /tmp/af-k13-react-pd1657bx/check_artifacts.py` | Eleven scoped changed paths, 90 local links/anchors, Markdown fences/tables, exact nine executable file blocks, original obligations and K14–K19 queue preserved; 157 guarded files unchanged; scoped diff retained |

The first npm lookup was blocked by sandbox DNS; bounded read-only public lookups
and the isolated install succeeded with approved tool escalation. Dependencies were
installed only under the stage's `/tmp` directory with lifecycle scripts disabled.
The initial selection probe omitted required fixture `rule_profiles`; correcting
the fixture exposed the actual catalog omission before adoption.

Typed lint identified an async fixture method and async `act` callbacks without
awaits. The service now returns explicit promises, and callbacks await the work
being settled; no suppression or fake production delay was added. The first Node
`--test` invocation reported file counts, so the final script invokes each test file
directly for named case evidence. One failing assertion attempted to print a React
DOM object and the process was killed; a Boolean absence assertion yielded the
specific stale-owner regression. No success was inferred from those initial runs.

Final strict/lint/build and all nine cases passed on the exact published snippets.
Inline review found and resolved the service-owner stale-output case and checked
preserved obligations, task-conditioned reading, version limits, input versus
operation authority, controlled-draft retention, identity/reset costs, cleanup and
failure ownership. Review is inline under the workspace adaptation, not an
independent reviewer or native-client pilot.

Limits: executed only the pinned React 19.3 stack in jsdom. React 18 metadata routes
are not a React 18 runtime test. DOM rendering/role/label checks do not establish
visual layout, browser-native keyboard behavior, focus rendering or screen-reader
announcements. No actual browser E2E, SSR/hydration/RSC host, real HTTP/database,
external-store runtime, Compiler, optimistic/concurrent mutation, server idempotency
or benchmark was exercised. Cancellation publication checks do not prove remote
work termination. Synthetic bundles establish portable artifacts and conditional
routes, not actual model reading compliance or token savings. P3–P7 remain planned.


The stage directory `/tmp/af-k13-react-pd1657bx` retains baseline/before copies,
`k13.diff`, exact example files, pinned dependencies/lock, the meaningful red
regression and delivery/artifact logs. Final command output also records all nine
passing cases. No production source/test file, earlier topic artifact, global or
workspace dependency, or external project was changed. No material in-scope
finding remains unresolved. Final plan-only bookkeeping reruns only scope/artifact
checks; unchanged executable and delivery evidence is reused.

**Checkpoint:** K13 is complete and ready for the user's review. **Next topic:**
K14 Next.js; do not begin it until the user authorizes continuation.


### K14 execution scope

The user accepted K13 and authorized continuation on 2026-09-21. Execute only K14
Next.js inline with Superpowers under the workspace adaptation, keeping the approved
short entry, task-conditioned sections and separate examples. Preserve all React
resources and task routes, earlier results and the K15–K19 queue; stop before
PostgreSQL adoption. No Git writes or installation into external projects.

Baseline/before copies: `/tmp/af-k14-nextjs-nq42k2eh/baseline.json`, covering twelve
scoped paths and 164 guarded files. Scope: this plan, combined entry, existing
feature-structure reference, catalog, research note, five Next.js sections and two
examples. Keep catalog IDs, technologies, dependencies and globs unchanged.
Register the existing structure file as an optional resource too, so explicit
combined-profile selection preserves its task-based link in an independent project;
this does not add an automatic design profile route for React-only projects.

Research all eight areas, including App versus Pages Router, actual server/client
execution, request and operation authorization, cache model/version distinctions,
mutation revalidation and deployment limits. Public metadata identifies Next.js
16.3.5; examples use a pinned temporary project and production build/start rather
than assuming the framework contract from direct function calls. Exercise a real
Route Handler with representation and stateful refusal, and tagged cached reads
with invalidation. Preserve explicit execution limits and existing-project choices.

Verify exact snippets, generated types, strict types/lint/build and relevant actual
HTTP behavior; check resource selection, portable delivery for three clients and
independent repositories. Record actual checks and perform scoped inline review,
then stop for the user's review before K15.

### K14 result and verification

Delivered the [Next.js research note](../research/2026-09-21-nextjs-engineering-practices.md),
short [combined entry](../../standards/nextjs.md), five conditional Next.js sections,
two separate examples and a focused addition to the existing
[feature structure](../../standards/nextjs-feature-structure.md). Research covers all
eight areas with primary evidence checked on 2026-09-21, R/D/O strengths, alternatives,
costs and version applicability. React guidance/resources and its five entry routes
remain unchanged. Existing Next.js obligations are relocated to conditional owners.

The entry is **60 lines / 464 whitespace-separated words**, previously 72 / 583.
Five new task routes cover routing/composition, server/client security, data/cache
mutations, rendering/runtime and verification/migration. The feature structure keeps
its original tree/import directions and adds actual router/environment contracts.
Eight resources are appended to the combined profile: five sections, two examples
and that existing structure file. This makes its task link portable even for explicit
combined-profile selection; it does not automatically select the separate structure
profile for React-only metadata. All 17 IDs, technologies, dependencies and globs remain.

Adoption distinguishes App/Pages Router, server/client module versus execution
boundaries, minimal DTOs, operation authorization, framework versus backend lifetime,
Cache Components versus previous models, stale versus immediate invalidation, request
rendering/streaming and actual host/deployment capabilities. It preserves existing
backend ownership, supports scoped legacy migration and does not mandate a router,
cache-model, Compiler, middleware/Proxy or project-wide architecture migration.

The examples share one pinned temporary application, with fourteen exact published
file blocks. The [HTTP command](../../standards/nextjs/examples/authorized-command.md)
validates a real request and independently protects operation permission/quantity;
state refusal does not spend stock. The [tagged read](../../standards/nextjs/examples/tagged-read.md)
projects public data into a Client Component and demonstrates cross-request caching,
denied invalidation, immediate authorized expiry and fresh subsequent API/page output.
The identity map, local stock and file are explicit fixtures with documented limits.

Checks on the final artifacts:

| Check | Result and scope |
| --- | --- |
| npm metadata, installed packages/peers, `node --version`, explicit `tsc6 --version` and compiler API | Next/eslint-config-next 16.3.5; React/React DOM/types 19.3.0; Node 24.13.0; compatibility TS package 6.0.2/compiler API 6.0.3; ESLint 9.39.5; typescript-eslint 8.70.0; Node types 24.13.6; server-only 0.0.1; final lint peer tree compatible |
| `NEXT_TELEMETRY_DISABLED=1 npm run typegen`, `npm run check`, `npm run lint` | Generated route types, explicit `tsc6` strict authored checks and Next/typed ESLint passed; no suppression, authored `any` or ignored build errors |
| `NEXT_TELEMETRY_DISABLED=1 AF_CATALOG_FILE=/tmp/af-k14-nextjs-nq42k2eh/catalog.json npm run build` | Production webpack build passed, including framework compiler-API type checking and prerender; `/` static with declared cache lifetime, three API routes dynamic |
| `npm test` in the temporary example | Six named checks passed, zero failed/cancelled/skipped, using actual `next start` on loopback and `--unhandled-rejections=strict`; HTTP identity/input/status/output, state refusal, direct invariants, server HTML projection and tagged reuse/expiration |
| Same production build in `negative-client-import`, adding only `import './read'` to the client module | Expected failure: server-only/cache APIs and inline cache scope rejected in the client import graph; diagnostic traces `read.ts` to `CatalogTitle.tsx`; published source remains unchanged |
| Installed version-matched docs and compiler CLI dispatch source inspection | Cache Components Node/model requirements, Route Handlers, migration and CLI/API mode verified; digests retained in `inspected-sources.json` |
| `python3 -m pytest -q tests/test_rules.py tests/test_workspace.py` | 35 passed in 1.70s; existing selection/resource/composition and independent-opening checks |
| `PYTHONPATH=src python3 /tmp/af-k14-nextjs-nq42k2eh/check_delivery.py initial` | Codex, Claude Code and Cursor: Next 16/15, React-only, typed, passport, explicit and structure-only routes; 15 combined and six TS resources/digests; seven independent copies/recompositions per client; Node/TS/Go exclusion; 5,084 local links; resources remain conditional rather than concatenated into native instructions |
| `python3 /tmp/af-k14-nextjs-nq42k2eh/check_artifacts.py` | Twelve scoped changed paths, 105 local links/anchors, Markdown fences/tables and fourteen exact executable blocks; React entry/routes/resources, original Next obligations/structure and K15–K19 queue preserved; 164 guarded files unchanged; scoped diff saved |

The initial dependency set reused ESLint 10, but nested React/import/a11y plugins
reported unsupported peers. A bounded lookup selected ESLint 9.39.5 and final peer
inspection passed. The CLI build path could not parse captured `--showConfig` in
this environment; direct compiler output and framework source were inspected, then
the documented compiler-API mode was selected. This is not proof of an upstream
compiler defect. The final check names `tsc6` explicitly, avoiding accidental use
of the transitive package's `tsc`. No vendor code or framework check was disabled.
Next generated `allowJs`/dev-type includes; the published config includes the actual
post-generation result. One unnecessary async handler failed require-await and was
made synchronous without adding fake asynchronous work.

The first sandboxed server child exited before readiness; a minimal loopback bind
probe reported EPERM. The same HTTP checks passed with approved tool escalation and
the runner stopped its server. The first negative build reported only a generic
webpack failure; an approved diagnostic run supplied the actual server-only import
trace. Its generic error wording mentions Pages Router despite this App Router
fixture; the concrete module trace and rejection are the evidence, not that wording.
No external service was contacted by the HTTP fixture. npm installs were restricted
to the temporary project with lifecycle scripts disabled; locks and outputs remain.

Inline review covers requirement preservation, conditional loading, optional
structure delivery, actual router/cache/version boundaries, token fixture limitations,
state refusal, output projection, build-time versus runtime data, denied invalidation,
strict checks and import guard evidence. Shared React/Node/TypeScript/process rules
retain their existing owners. This is inline review under the workspace adaptation,
not an independent reviewer or a native-client pilot.

Limits: only App Router/Cache Components on the stated Node/webpack environment was
executed. No Pages/previous-model runtime, Server Action dispatch/updateTag/refresh,
browser hydration/click/navigation, visual rendering, real auth/CSRF provider,
request budgets, durable/concurrent database writes, CDN/distributed cache, Edge or
static-export deployment, external adapter, native TS 7, Turbopack or benchmark was
run. Single-worker stock and controlled file data establish no production durability.
Server HTML is not browser interaction evidence. Synthetic native bundles establish
portable artifacts, not actual model reading compliance or token savings. P3–P7
remain planned.


The stage directory `/tmp/af-k14-nextjs-nq42k2eh` retains baseline/before copies,
`k14.diff`, exact runnable sources/configuration, resolved dependencies/lock,
production and negative builds, HTTP and delivery/artifact logs. HTTP fixture/log:
`/tmp/af-next-http-rLb9lX`. No production source/test file, earlier topic resource,
workspace/global dependency or external project was changed. No material in-scope
finding remains unresolved. Final plan-only bookkeeping reruns only artifact/scope
checks; unchanged runtime, build and delivery evidence is reused.

**Checkpoint:** K14 is complete and ready for the user's review. **Next topic:**
K15 PostgreSQL; do not begin it until the user authorizes continuation.


### K15 scope and execution

The user accepted K14 and authorized K15 on 2026-09-21. Execute only PostgreSQL
inline with Superpowers under the workspace adaptation. The existing plan/design
is sufficient; no new approval cycle, Git writes, external-project installation
or later-topic adoption is implied. Baseline and guarded hashes were captured
before editing eleven scoped paths at `/tmp/af-k15-postgresql-2_5d9ve5/baseline.json`;
173 existing paths outside the scope are guarded.

The entry will route to five cohesive sections and two separate SQL examples.
Research covers all eight areas with primary evidence, R/D/O strengths and
version-specific alternatives. Preserve the initial PostgreSQL 16 target and
check current stable documentation separately. No ORM/driver choice is made.
Use isolated disposable PostgreSQL instances for material SQL/concurrency and
migration behavior, plus existing rules/workspace tests and synthetic composition
for all three clients, including independent project opening. Native-client
behavior remains outside this evidence.


### K15 result and verification

Delivered the [PostgreSQL research note](../research/2026-09-21-postgresql-engineering-practices.md),
short [entry](../../standards/postgresql.md), five conditional sections and two
separate examples. Research covers all eight areas with primary sources checked
on 2026-09-21, explicit R/D/O strengths, alternatives, costs and version conditions.
The entry is **43 lines / 347 whitespace-separated words**, previously 26 / 213.
Its five routes cover schema/contracts, transactions/concurrency, queries/performance,
security/operations and migrations/verification. All original PostgreSQL obligations
are preserved in their conditional owners; the initial PostgreSQL 16 target remains.

Seven resources are registered under the existing PostgreSQL profile. All 17 profile
IDs, technologies, dependencies, activities and globs are unchanged. The guidance
preserves core boundaries and makes no mandatory repository, stored-procedure,
ORM/driver, isolation, index, RLS, replication or migration-framework choice.
It distinguishes transport representation from durable and current-state rules,
atomic writes from preflight checks, complete retry from uncertain-COMMIT recovery,
identity from tenant references, and verified migration state from command success.
Version 18 additions are conditional, not copied into the PostgreSQL 16 baseline.

The [reservation example](../../standards/postgresql/examples/atomic-reservation.md)
uses a conditional decrement plus receipt insertion in one statement. The
[migration example](../../standards/postgresql/examples/online-constraint.md) stages
required historical values and concurrent unique-index construction. Ten exact SQL
file blocks match the executed fixtures. psql is used as a driver-neutral harness;
SQLAlchemy and psycopg adoption have not started. The reservation key is explicitly
not a complete idempotency protocol, and tenant references do not supply authorization.

Checks on the final affected artifacts:

| Check | Result and scope |
| --- | --- |
| Primary version policy/manuals, `SHOW server_version`, `psql --version`, local image inspection | Current public patches 16.15/18.6; actual isolated server/client executions 16.15/18.4; exact image IDs/isolation recorded in `environment.json` |
| `python3 /tmp/af-k15-postgresql-2_5d9ve5/check_sql.py af-k15-pg16-2_5d9ve5` | Six scenario groups passed: representation/operation refusals; constraints/duplicate rollback/tenant targeting; observed competing-writer lock wait and no oversell; lock timeout; serialization failure with fresh complete operation; historical validation/repair and concurrent-index failure/repair |
| Same SQL command with `af-k15-pg18-2_5d9ve5` | Same six groups passed on 18.4, without feature substitutions |
| `python3 -m pytest -q tests/test_rules.py tests/test_workspace.py` | Final 35 passed in 3.82s; selection, composition, portable resources, ownership/drift and retirement |
| `python3 -m mypy` | Success, no issues in 16 source files under the existing strict configuration |
| `PYTHONPATH=src python3 /tmp/af-k15-postgresql-2_5d9ve5/check_delivery.py` | Codex, Claude Code and Cursor: declared 16/18, unspecified server version, Python with declared PostgreSQL, explicit selection; five independent copies/recompositions each; seven resource digests and exact SQL blocks; driver-only/ORM-only/SQL-only/Node exclusion; 2,032 portable links; no automatic detail/example concatenation |
| `python3 /tmp/af-k15-postgresql-2_5d9ve5/check_artifacts.py` | Twelve scoped changes, 90 local links/anchors, Markdown tables/fences, five conditional routes and ten exact executed SQL blocks; catalog additions only; original obligations and prior result blocks retained; K16–K19 queue unchanged; 172 guarded paths unchanged; scoped diff saved |

The first existing pytest run had 34 passes and one failure: the PostgreSQL
retirement test expected only the old entry/route pair. Its actual deletion set
correctly included the seven newly registered owned resources. Systematic debugging
confirmed that the catalog contract changed, not retirement behavior. Before editing
`tests/test_rules.py`, its original bytes were checked against the guarded digest,
copied into the baseline and moved into the scoped set: twelve scoped / 172 guarded
paths. One expectation now includes that profile's registered resources, retaining
exact-set equality and local-edit protection. Existing dedicated resource-drift tests
remain unchanged and pass. No production composer change or new test framework was
needed. This is an expected-contract correction, not a repaired SQL implementation.

The artifact checker initially compared relocated bullets with Markdown indentation
included; normalization of whitespace makes it check preserved wording rather than
list layout. No original rule was removed to satisfy it. SQL checks passed without
an implementation repair; no artificial TDD claim is made for documentation/examples.

Docker access required approved tool escalation. Both servers were created only for
this stage, from already available images, with network disabled, no published ports,
no host bind mounts, read-only root filesystems and tmpfs database data. Local trust
was limited to these disposable fixtures. The harness used separate real connections,
observed the lock wait and synchronized completion with markers; it did not infer
concurrency from a timing sleep. Statements and harness waits had finite deadlines.
Server and SQL logs were saved, then both task-owned containers were removed.
Existing containers/images and external application databases were not modified.

Inline review covered preservation of existing requirements, version-specific
capabilities, SQL error/result semantics, no-oversell and statement rollback,
request-key limits, trusted tenant context, failed migration state, lock boundaries,
portable resource retirement and context-loading routes. Shared process/core rules
retain their owner. This is author review under the workspace adaptation, not an
independent reviewer or a native-client pilot. No material in-scope finding remains.

Limits: no actual ORM/driver or proxy pool, RLS/TLS deployment, durable crash/failover,
uncertain-COMMIT reconciliation, backup/PITR restore, production load/query-plan
benchmark, live rolling application deployment, or native-client instruction adherence
was executed. The available 18.4 image is older than current 18.6; the latter and
PostgreSQL 19 were not runtime-tested. The fixtures are not production-readiness or
latency evidence. P3–P7 remain planned. Final plan-only bookkeeping reuses unchanged
SQL, type, test and composition evidence and reruns only artifact/scope checks.

The stage directory `/tmp/af-k15-postgresql-2_5d9ve5` retains `baseline.json`, before
copies, `k15.diff`, exact SQL files, the psql harness, SQL/server logs, environment
identity, delivery/type/test outputs and artifact checks. No Git write, dependency
installation or change to earlier topic resources was made.

**Checkpoint:** K15 is complete and ready for the user's review. **Next topic:**
K16 SQLAlchemy; do not begin it until the user authorizes continuation.


### K16 scope and execution

The user accepted K15 and authorized K16 on 2026-09-21. Execute SQLAlchemy only,
inline with Superpowers under the workspace adaptation and the existing design.
The baseline captures twelve scoped paths and 181 guarded paths before edits:
`/tmp/af-k16-sqlalchemy-yk7g_na1/baseline.json`. Introduce one conditional catalog
profile, a short entry, five cohesive sections and two separate runnable examples;
reconcile Python persistence references without selecting the ORM for all Python
projects or PostgreSQL for every SQLAlchemy user. Later stages remain planned.

Research the stable 2.0 line and distinguish 1.4 migration/2.1 prerelease behavior.
Use an isolated temporary Python environment and actual disposable PostgreSQL for
material ORM write/rollback and async loading contracts. Drivers used to execute
those fixtures are not K17 adoption. Verify strict typing, existing composition
checks, conditional metadata/explicit routes and independently opened bundles on
all three clients. Retain the original baseline and stop after this topic's report.


### K16 result and verification

Delivered the [SQLAlchemy research note](../research/2026-09-21-sqlalchemy-engineering-practices.md),
short [entry](../../standards/sqlalchemy.md), five conditional sections and two
separate examples. All eight research areas have primary evidence checked on
2026-09-21, R/D/O strengths, alternatives, costs and version conditions. The new
entry is **43 lines / 342 whitespace-separated words**. Its task routes cover
mapping/contracts, sessions/transactions, queries/loading, async/engines and
migrations/verification. Examples and research are optional context.

The catalog now has **18 profiles**: the new `sqlalchemy` profile depends on the
existing `python-fastapi` profile and registers seven optional resources. All prior
17 profile definitions remain unchanged. Existing dependency recognition selects
SQLAlchemy without a metadata-code change. No PostgreSQL dependency is added.
The generic Python persistence section retains all original wording and adds only
a conditional reference by profile ID, avoiding a dangling mandatory file link in
Python-only bundles. Core/Python remain the owners of general boundaries and typing.

The stable instruction/example target is **2.0.54**; **2.1.0rc2** is explicitly
prerelease. Guidance preserves 1.4 migration scope and actual dialect/driver versions.
It separates Core/ORM choice, typed construction, operation versus attribute validation,
Session identity/lifetime, flush versus commit, outer rollback, savepoints, concurrent
ownership, eager/implicit loading, bulk synchronization, engine/pool lifetime, migration
candidates and actual backend behavior. It mandates no repository, ORM conversion,
async runtime, database, Alembic or project-wide migration.

The [transaction example](../../standards/sqlalchemy/examples/transactional-command.md)
uses typed mapped dataclasses and a conditional update plus receipt flush, returning
a result after commit. Its smaller adapter operation preserves a caller's transaction.
The [async projection](../../standards/sqlalchemy/examples/async-projection.md) eagerly
loads a guarded relationship and returns owned public DTOs after closing the session.
Six exact file blocks comprise four Python files and two setup/analyzer files. The
parser checks representation while the operation independently rejects nonpositive
quantity/current-stock refusal; the request key is not claimed as full idempotency.

Checks on final affected inputs:

| Check | Result and scope |
| --- | --- |
| Official version/manual pages, temporary installed packages, `SHOW server_version` | CPython 3.12.3; SQLAlchemy 2.0.54; PostgreSQL/psql 16.15; psycopg/binary 3.3.6; asyncpg 0.31.0; greenlet 3.5.6; mypy 2.1.0; resolved dependencies retained |
| From temporary `example/`: `K16_PG_SOCKET=/tmp/af-k16-sqlalchemy-yk7g_na1/socket ../venv/bin/python -W error -m unittest -v test_command test_projection` | Final 9 tests passed in 0.930s: representation/domain refusal; committed success including zero remaining; duplicate-flush rollback and clean new operation; caller rollback; competing separate sessions; direct database check; complete detached public DTO; unplanned loading guard; concurrent reads; cancellation after flush with no committed row |
| `../venv/bin/python -m mypy --config-file mypy.ini` from the example directory | Strict success across four Python files including tests; no SQLAlchemy plugin, Any/cast/ignore bypass or third-party SQLAlchemy stubs |
| `python3 -m pytest -q tests/test_rules.py tests/test_workspace.py` | 35 passed in 3.93s; existing rule selection, resource ownership/drift/retirement and independent-opening checks |
| `python3 -m mypy` | Success, no issues in 16 source files under the existing strict project configuration |
| `PYTHONPATH=src python3 /tmp/af-k16-sqlalchemy-yk7g_na1/check_delivery.py` | Codex, Claude Code and Cursor: stable dependency, legacy 1.4 constraint, asyncio extra, SQLite declaration, passport-only, explicit selection, PostgreSQL combination; seven independent copies/recompositions each; seven SQLAlchemy plus eighteen Python resource digests; exact blocks; Python-only/driver-only/PostgreSQL-only/Node exclusion; no forced database; retirement and edited-resource preservation; 5,180 portable links |
| `python3 /tmp/af-k16-sqlalchemy-yk7g_na1/check_artifacts.py` | Twelve scoped changed paths, local links/anchors, Markdown fences/tables, five conditional routes and six exact executable/config blocks; all earlier catalog definitions and topic result blocks preserved; K17–K19 queue unchanged; 181 guarded paths unchanged; scoped diff saved |

Examples initially passed nine runtime tests and strict typing. Before publication,
the existing refusal/success tests were strengthened for zero quantity and exact
stock exhaustion so that zero remaining cannot be mistaken for no result; the final
runtime/type runs above cover those inputs. No SQL or Python implementation repair
was required. No artificial failing-test cycle is claimed for this documentation
stage; repository source/tests did not need changes.

Temporary dependencies were installed into the task venv only; the original local
SQLAlchemy 2.0.51 installation was not changed. The first empty test container was
recreated before tests to expose a task-scoped Unix socket to the host Python process.
The final server had network disabled, no published ports, a read-only root, tmpfs
DB data and only that socket-directory bind. Tool escalation authorized temporary
installation, container access and socket-based checks. No existing application
container/database or external project was modified. Final server logs/environment
were retained and the task-owned container was removed.

Inline review covered short/conditional loading, no database inference, strict mapping
and constructor contracts, output projection, actual transaction ownership, failure
rollback, receipt-key limitations, cancellation scope, version-sensitive advice,
portable resources and local-edit preservation on retirement. It follows the workspace
adaptation and is author review, not an independent reviewer or native-client pilot.
No material in-scope finding remains unresolved.

Limits: no runtime execution on SQLAlchemy 1.4/2.1, Python 3.11 or another database;
no schema migration, production RLS/TLS/auth, external connection pooler, actual
driver-call/COMMIT cancellation, uncertain-commit recovery, crash/failover, load/query
benchmark, stream interruption or native-assistant reading adherence. The concurrency
barrier coordinates competing attempts but does not prove a specific server lock-wait
interleaving. The cancellation test observes rollback after a flushed write while the
owner awaits an application event. Fixtures establish neither production readiness
nor universal driver behavior. K17–K19 and P3–P7 remain planned.

Stage evidence is retained at `/tmp/af-k16-sqlalchemy-yk7g_na1`: baseline/before copies,
`k16.diff`, exact runnable files, venv and resolved dependencies, runtime/type/test logs,
delivery/artifact checks, server log and `environment.json`. Final plan-only bookkeeping
reuses unchanged runtime/type/composition evidence and reruns artifact/scope checks.
No Git write or change to earlier topic resources beyond the documented Python
cross-reference was made.

**Checkpoint:** K16 is complete and ready for the user's review. **Next topic:**
K17 psycopg; do not begin it until the user authorizes continuation.


### K17 scope and verification adjustment

The user authorized K17 after clarifying that these deliverables are agent
instructions, not application projects. Keep broad research and concise conditional
guidance, but reduce verification to artifact correctness, affected profile delivery
and focused checks of genuinely nontrivial snippet behavior. Do not build another
example application or substantial new test suite. This refinement applies to the
remaining instruction stages and overrides broader example-verification defaults.

Execute only psycopg inline with Superpowers under the existing workspace adaptation.
Baseline before edits: `/tmp/af-k17-psycopg-t5n75q0w/baseline.json`, eleven scoped
paths / 190 guarded paths. Plan a short entry, four cohesive sections, two short
separate examples and one new conditional profile. Reuse the existing temporary
psycopg 3.3.6 environment for syntax/types and offline SQL-composition checks; no
new environment, server or application is needed. Database execution limits will
be stated explicitly. Run the relevant existing catalog/composition tests and
inspect generated bundles for the new dependency route. Stop for user review.


### K17 result and verification

Completed on **2026-09-22**, retaining the research start date in the
[research filename](../research/2026-09-21-psycopg-engineering-practices.md).
The [new entry](../../standards/psycopg.md) is **39 lines / 292 words**, with four
conditional sections and two short separate examples. Research covers all eight
areas, primary evidence, R/D/O strengths, simpler alternatives, costs and versions.
The moving manual's development banner is distinguished from stable **3.3.6**.

The catalog has **19 profiles**. The new `psycopg` profile registers six optional
resources and depends on Python and PostgreSQL instructions. This supplies applicable
rules for a PostgreSQL driver without inventing a server-version metadata fact.
Python, PostgreSQL or SQLAlchemy alone do not select psycopg; psycopg2-only manifests
are not silently migrated. All previous catalog definitions are unchanged. The
PostgreSQL entry gains only a conditional reference by profile ID, preserving
portable driver-free bundles and its original obligations.

Guidance distinguishes SQL identifiers from value parameters, row typing from
validation, implicit transactions from explicit owners/savepoints, coordinated
connection sharing from independent operations, driver/pool versions, cancellation
from uncertain COMMIT, and optional bulk/prepared features from defaults. Shared
Python/PostgreSQL rules retain their owners; no ORM/pool/migration framework is imposed.

Verification follows the user's narrower instruction-maintenance scope:

| Check | Result and scope |
| --- | --- |
| Existing temporary driver inspection | Python 3.12.3; psycopg/binary 3.3.6; libpq 18.6 (180006); mypy 2.1.0; no new installation |
| Existing venv `python -m compileall -q /tmp/af-k17-psycopg-t5n75q0w/snippets` | Both short snippet files compile |
| Existing venv `python -m mypy --config-file /dev/null --strict --disallow-any-explicit --disallow-any-unimported /tmp/af-k17-psycopg-t5n75q0w/snippets` | Success on two files; empty-config diagnostic notes no mypy section, while explicit strict flags apply; no typing bypass |
| Small offline Python probe importing `report_query` | Both allowed table choices render correctly, value placeholder remains separate, quoted identifier escaping checked; no database connection; result in `offline.log` |
| `python3 -m pytest -q tests/test_rules.py` | 28 existing rule tests passed in 4.01s; no new tests added to the repository |
| `PYTHONPATH=src python3 /tmp/af-k17-psycopg-t5n75q0w/check_delivery.py` | Codex, Claude Code and Cursor: dependency/extra, passport and explicit routes; four unrelated/legacy exclusions; source/derived digests, exact snippets and three independent copies/recompositions per client; 2,382 portable links; optional resources not concatenated into native entry instructions |
| `python3 /tmp/af-k17-psycopg-t5n75q0w/check_artifacts.py` | Eleven scoped changes, local links/anchors and Markdown structure; four task routes/six resources/two exact snippets; 190 guarded paths, prior catalog definitions/result blocks and K18–K19 queue preserved; scoped diff retained |

The delivery checker initially treated a line wrap in the conditional-reading sentence
as missing wording. Normalizing whitespace corrected that check; no instruction was
changed to conceal a routing defect. Final delivery output is `delivery-final.log`.

Inline review checked instruction consistency, source/version applicability, profile
selection, parameter versus identifier boundaries, row/schema assumptions, borrowing
versus transaction ownership and honest verification limits. No material in-scope
finding remains. This is author review, not an independent/native-client pilot.

**Limits:** no new server, application scaffold or test suite was created. SQL execution,
row decoding, commit/rollback, async/pool cancellation, migrations, TLS deployment and
performance were not exercised. The examples state these limits explicitly; earlier
integration evidence is not reused as a claim about their execution. Synthetic bundles
prove artifact delivery, not agent behavior. P3–P7 remain planned.

Baseline/before copies, `k17.diff`, two snippets and check outputs remain in
`/tmp/af-k17-psycopg-t5n75q0w`. The K16 temporary interpreter was reused read-only for
installed dependencies. No Git write, dependency installation, production code/test
change or external-project modification was made. Final plan-only edits reuse valid
checks and rerun artifact/scope validation only.

**Checkpoint:** K17 is complete and ready for the user's review. **Next topic:**
K18 Docker; do not begin it until the user authorizes continuation.


### K18 scope

The user accepted K17 and authorized K18 on **2026-09-22**. Execute Docker only,
inline with Superpowers and the existing workspace adaptation. Preserve the K17
verification refinement: instruction/artifact/selection checks and a small Compose
configuration check; no new application, container or test suite.

Baseline before edits: `/tmp/af-k18-docker-gpfjbycm/baseline.json`, ten scoped paths
and 198 guarded paths. Retain a short Docker entry, four cohesive conditional sections,
two separate examples and six optional resources in the existing profile. No detector,
source, template, dependency or permanent test change is planned. Docker CLI 29.1.3 and
Compose 2.40.3 are available; the Buildx command is unavailable. Review the Dockerfile fragment
against primary references and validate the Compose snippet without a daemon/build.
Run affected existing composition checks, inspect portable bundles and stop for review.


### K18 result and verification

The [Docker entry](../../standards/docker.md) now routes to four conditional sections
and two separate examples. [Research](../research/2026-09-22-docker-engineering-practices.md)
covers all eight areas, primary sources, R/D/O strengths, alternatives, costs and
version applicability. The existing profile registers six optional resources;
no detector, runtime code, template, dependency or permanent test change was needed.

The instructions retain the original context/base/configuration/startup contract and
cover secret delivery/cache behavior, signal ownership, compatible privilege reduction,
Compose readiness versus ordering, interpolation, networks, storage and version limits.
They require no universal multi-stage recipe, tiny base, orchestration system or image
build for an ordinary documentation edit. Core and language/database profiles retain
business validation, transaction and verification ownership.

Checks performed on 2026-09-22:

- `python3 -m pytest -q tests/test_rules.py`: **28 existing tests passed in 1.90s**.
  No new unit/integration test suite or application was created.
- Exact Compose block extracted to the stage's `snippets/compose.yaml`:
  `docker compose -f <snippet> config --quiet` passed with a nonsecret placeholder
  APP_IMAGE; missing and empty APP_IMAGE both failed with the expected required-value
  error. `config --format json` preserved user, read-only/init, port binding, health
  command and stop grace period. Compose **2.40.3**, Docker CLI **29.1.3**.
- `PYTHONPATH=src python3 /tmp/af-k18-docker-gpfjbycm/check_delivery.py`: Codex,
  Claude Code and Cursor bundles passed Dockerfile/declaration/explicit selection,
  Node-only and undeclared Compose-only exclusion, six source/derived resource digests,
  exact example blocks, conditional/native routes and isolated copies/recomposition.
  **966 portable links** resolved. Research and example bodies stay out of automatic
  instructions; synthetic bundles do not establish actual assistant reading adherence.
- Dockerfile fragment reviewed against secret-mount and npm documentation. Buildx
  is unavailable; no installation, dependency download, registry operation, image
  build or container run was attempted. No runtime pass is claimed for that fragment.

- `python3 /tmp/af-k18-docker-gpfjbycm/check_artifacts.py`: **10 scoped changed paths**,
  Markdown fences/tables and **92 local links/anchors** passed; **198 guarded paths**,
  all prior catalog settings/topic result blocks and the K19 queue remain unchanged.
  The entry is **41 lines / 333 words**; four conditional routes, six resources and
  two exact snippet copies were checked. Scoped diff saved to `k18.diff`.

Inline author review checked the original obligations, all eight research areas,
conditional loading, secret/cache caveats, runtime versus configuration guarantees,
existing discovery limits and the scoped diff. No material in-scope finding remains.
This is not an independent review or a native-client pilot.

Limits: no daemon/build/registry or actual application execution, signal/probe/network
or volume-permission check, production isolation, performance measurement, Windows or
multi-platform run. These are instruction examples, not a production image certification.
No dependencies, containers, external project files or Git state were changed. Evidence
is retained in `/tmp/af-k18-docker-gpfjbycm` (baseline/before copies, diff, exact snippets,
Compose output, existing-test log and adapted temporary artifact/delivery helpers).
Final plan-only status updates reuse unchanged example/composition evidence and rerun
artifact/scope validation.

**Checkpoint:** K18 completed on **2026-09-22**, ready for the user's review.
**Next topic:** K19 cross-profile reconciliation; do not begin it until the user
authorizes continuation. P3–P7 remain planned in their owning native adoption plan.


### K19 cross-profile reconciliation and handoff

On **2026-09-22**, the user accepted K18 and authorized the remaining named stages
through bounded **gpt-6-astra / high** subagents, with necessary implementer checks
and concise coordinator integration review. This overrides intermediate topic
checkpoints for the authorized sequence, without granting Git writes, external
installation or global configuration changes. K19 owns only standards, catalog,
affected templates and this plan; native implementation/progress has its own owner.
The K17 proportional-verification adjustment remains binding: no new application,
ecosystem research campaign or repeat of completed topic execution.

Pre-edit baseline: `/tmp/af-k19-reconcile-tdz8c8pu/baseline.json`; original bytes and
hashes were captured before each of **13** changed paths. Parallel native work in
`changes.py`, `pyproject.toml` and the native plan is explicitly excluded from K19's
unchanged claims. New native source/test paths are also outside K19 ownership.

Reconciliation decisions:

- Core retains scope, architecture, validation/domain separation, pattern and size
  policy. Verification, work modes, delivery, orchestration/model configuration and
  Superpowers retain their existing process owners. Profile essentials summarize
  these rules; language/framework sections specialize actual contracts rather than
  introducing another common policy or mandatory architecture.
- Explicit TypeScript and React selections could omit shared JavaScript guidance
  without a package manifest; a passport declaring `javascript` did not select it.
  The catalog now recognizes `javascript`, and TypeScript depends on the existing
  `nodejs-typescript` profile. That entry owns shared language/effect rules while
  Node.js sections remain conditional on the actual runtime. No new profile ID,
  framework dependency installation or source-code change is required.
- SQLAlchemy's entry no longer implies that every mapping must live in an adapter:
  it preserves the mapped-domain/separate-model choice already permitted by its
  detailed section and the common/Doctrine boundaries. Query/session mechanics
  stay in adapters. Python/Pydantic and React references now identify current
  framework/ORM/driver owners instead of future research-stage placeholders.
- Generated and manual entry templates explicitly distinguish profile availability,
  conditional sections and optional examples/research. Manual routes now cover
  JavaScript, React, database/driver/ORM and container work; the passport records
  their relevant owners without applying Next.js conventions to every React host.
- All standards remain registered across **19** profiles. The Next.js structure
  document intentionally remains both a resource of `nextjs` and its own conditional
  profile source: this is one authoritative file, deduplicated in generated copies,
  and keeps explicit Next.js bundles portable. No example bodies enter automatic
  instructions. General size thresholds remain in core; React's 250-line signal
  remains a component-specific cohesion prompt, not a competing mandatory limit.

Checks performed on the completed instruction/catalog/template state:

- `python3 -m pytest -q tests/test_rules.py`: **28 passed in 1.86s**; existing
  selection, drift, ownership, retirement and portable-resource checks reused.
- `PYTHONPATH=src python3 /tmp/af-k19-reconcile-tdz8c8pu/check_selection.py`:
  the temporary probe first exposed all three missing JavaScript-owner routes;
  after the catalog correction it passed, including Python-only exclusions.
- `PYTHONPATH=src python3 /tmp/af-k19-reconcile-tdz8c8pu/check_delivery.py`:
  Codex, Claude Code and Cursor passed eight selected/negative cases each, all
  19 profiles, source/resource digests, conditional native routes, independent
  copies/recomposition and **6,476** portable links. Python/SQLAlchemy alone do
  not select PostgreSQL/psycopg; psycopg does not select SQLAlchemy. Documentation
  reading routes remain work modes and verification.
- `python3 /tmp/af-k19-reconcile-tdz8c8pu/check_artifacts.py`: scoped before-copy
  hashes/diff, local links/anchors, Markdown structure, full standards registration,
  the two permitted catalog changes and preserved K01–K18 records checked. Guarded
  paths are checked with the explicitly authorized concurrent exclusions above.
  The temporary link checker was corrected to resolve the ENTRY template from its
  generated policy root; generated links already passed the delivery check.

Bounded author review inspected the scoped diff and these cross-profile interactions.
No material in-scope issue remains. This is not an independent reviewer or a native
pilot: generated artifacts do not prove assistant reading adherence, live native
role/model selection or example runtime correctness across other versions. No new
technical-version claim or new example execution is made. The unchanged examples
retain their earlier recorded checks and limits. Final plan-only status edits reuse
valid delivery evidence and receive artifact/scope validation.

**Result:** K19 is complete and handed to the coordinator for the authorized concise
integration review. At that handoff, continuation concerned the then-authorized
native stages. That work was subsequently closed; the
[native plan](2026-09-20-native-client-adoption.md) now preserves archived history.
Evidence and the scoped diff are retained in `/tmp/af-k19-reconcile-tdz8c8pu`.


### 2026-09-22: return to the rules-only scope

The user explicitly approved removal of the entire additional application while
retaining orchestration rules, instructions and native templates. Removed the
Python package, CLI, all three adapters, observation, shared writers, tests and
fixtures, generated schema, packaging/build outputs, tool caches, and two
implementation-only specifications. The task-only application virtual environment
was also removed. Native settings/authentication and external projects were not
changed.

README, architecture, adoption/model instructions and affected templates now
explain direct instruction/native-template adoption. The product scope is rules
and templates; the former native application plan is explicitly archived. K01–K19
rules, conditional sections and separate examples remain in place. All unchanged
retained material was checked against pre-removal hashes.

Before-state copies and a reproducible documentation diff are in
`/tmp/af-remove-application-cgs8b5ja/`. Artifact checks confirm removed paths are
absent, 161 retained files are byte-identical, all 214 backup hashes are valid,
five remaining TOML files parse, and catalog resources exist. No new broken local
links or active CLI commands remain. Two pre-existing anchor issues in unchanged
PHP/Symfony instructions are recorded in `checks.json`, not silently repaired as
unrelated work. No new tests or native model calls were introduced for this cleanup.

### 2026-09-22: user acceptance and closure of the current part

The user confirmed the current result and requested explicit completion records
in the specification and plans. The retained engineering/orchestration rules,
instructions, examples and native templates, together with removal of the entire
additional application, are accepted. This plan is closed; no further review or
native pilot is required for acceptance of its agreed current scope.

Subsequent changes will be a new part or version, with a separate scoped plan and
specification or explicit versioned specification update. The
[accepted scope](../specs/2026-09-20-agents-framework.md#completion-and-future-versions)
owns that boundary. Historical check results and limitations above remain intact;
acceptance does not turn removed application experiments into supported features.
