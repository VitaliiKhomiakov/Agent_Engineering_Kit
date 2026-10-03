# Instruction framework refinement

Date: 2026-09-26. Status: accepted for staged implementation.
Change ID: `instruction-framework-refinement`.

The user requested a specification and implementation plan following the project
audit. This is a new improvement part of the rules-only framework; it does not
reopen the [accepted baseline](2026-09-20-agents-framework.md).
The [implementation plan](../plans/2026-09-26-instruction-framework-refinement.md)
owns stage progress and verification results. This specification owns requirements.

## Outcome and scope

An agent can select sufficient instructions for a task, restore the user's saved
orchestration choices, and follow one consistent workflow. Small tasks remain
small. Adoption preserves existing project contracts and planning artifacts.

The deliverables are revised Markdown instructions, TOML templates/catalog,
instruction-only skills, and scoped compatibility evidence. After preparation of
the planning documents, the user instructed implementation to begin. Execute the
agreed stages under the plan's human checkpoints; progress is owned by the plan.

No application, installer, CLI, monitor, workflow engine, new framework skill,
mandatory test suite, or automatic model launch is introduced. Engineering choices
such as strict typing, dependency boundaries, and proportionate verification remain
in force. A live adoption pilot is a separately authorized follow-up.

## Audit basis

| Finding | Current evidence | Consequence |
| --- | --- | --- |
| Reading and packaging dependencies are ambiguous | [Catalog](../../standards/catalog.toml): `core` transitively depends on delivery, Superpowers, orchestration and model setup | A reader can mistake bundled availability for mandatory loading |
| Saved configuration is incomplete | [Routing template](../../templates/framework/model-routing.toml) contains three pairs and a concurrency limit; [architecture](../../ARCHITECTURE.md#workspace-model-routing) describes a wider selection | Client, disabled roles and delegation choices lack a common representation |
| Missing profile triggers setup at entry | [Root template](../../templates/AGENTS.root.md#session-entry-and-work-mode) and [setup procedure](../../standards/model-configuration.md#first-use-behavior) | An ordinary task can trigger unrelated onboarding |
| Integration mixes policy with helper internals | [Superpowers policy](../../standards/superpowers.md#plans-and-helper-compatibility) | Routine skill selection encounters details of scripts it may never use |
| Existing native plans can require relocation | [Planning template](../../templates/PLANS.md#native-artifact-systems) | Continuing an existing project task can be blocked by workspace layout policy |
| Two section links are stale | [PHP structure](../../standards/php/structure.md) and [Symfony structure](../../standards/symfony/structure-services.md) | Readers cannot follow the intended domain-model placement reference |

The audit parsed all five TOML files and found their catalog resources present.
The root AGENTS template has 105 physical / 89 nonempty lines. The transitive
`core` entry closure has 1,092 physical lines if treated as mandatory reading;
that is a structural measurement, not observed token consumption. Existing
integration evidence targets Superpowers 6.4.1; 6.4.2 is also available in the
audit environment. Availability does not establish compatibility or activation.

## Design choice

Use explicit reading semantics and a compact common workflow with conditional
references. Merely shortening paragraphs would leave the selection ambiguities;
adding a programmatic orchestrator would exceed the accepted product scope.
Keep Superpowers as the selected toolkit, with adaptations scoped to actual use.

### R1. Separate bundled resources from reading requirements

Document catalog semantics in a new `standards/catalog.md`, linked from the catalog
and adoption documentation. Keep catalog `schema_version = 1` and existing IDs,
paths and dependency edges: no installer/parser contract is being added.

- `dependencies`, `resources`, `assets` and template paths identify resources
  needed to assemble a portable bundle; they do not recursively command reading.
- `required = true` identifies shared policy available in an adopted bundle. Its
  relevance is still governed by the task and `when` condition.
- `activities`, `technologies` and `globs` are applicability hints; the actual
  stack and task resolve broad matches. `when` describes the reading trigger.
- A profile's entry routes select detail sections; examples and research remain
  optional. A link alone is not an instruction to open its target.

Align catalog prose, entry templates and migration guidance. In particular,
React in JavaScript must not acquire TypeScript obligations merely because the
bundled `nextjs` profile depends on `typescript`. Python without FastAPI/Pydantic
must not acquire their requirements. Planning does not imply delegation or setup.

### R2. Define a complete, minimal saved selection

Document routing format version 2 in `standards/model-configuration.md`, with the
inactive template as its example. It remains an instruction-level record.

| Field | Contract |
| --- | --- |
| `schema_version` | Integer `2` for the revised format |
| `status` | `unconfigured` or `configured`; neither value proves runtime activation |
| `scope` | `workspace` |
| `client` | `codex`, `claude-code`, or `cursor`; required for configured state |
| `max_subagents` | Nonnegative integer excluding the coordinator; zero in single-agent mode |
| `orchestration.mode` | `single-agent` or `delegated` |
| `orchestration.allowed_edges` | List of `parent->child` role IDs; empty in single-agent mode |
| `roles.<id>.enabled` | Explicit Boolean; orchestrator is enabled; specialists are optional |
| `roles.<id>.model`, `reasoning_effort` | Explicit chosen pair for each enabled role in configured state |

An unconfigured example may omit undecided fields. Example pairs are suggestions;
they never satisfy consent. Disabled roles may retain a prior pair for later reuse
but cannot be invoked. There is no fixed whitelist of model names.

Single-agent mode has no enabled specialists. Delegated mode has a positive ceiling;
edges reference enabled roles, originate in the coordinator's reachable graph,
and contain no self-edges or cycles. Nested delegation requires an explicit edge
and verified client support. A permitted edge does not require spawning a worker
or authorize work outside the task. Task order and correction stages remain in
the task plan; this format does not introduce a workflow language.

The selected rule revision belongs in adoption provenance in the entry/passport,
not in a competing model-policy store. Correct architecture descriptions accordingly.
Native mapping covers enabled roles, selected pairs and supported concurrency
controls. Unsupported controls remain instruction policy with a reported limit.
Disabling a role reconciles its managed native definition without deleting unrelated
roles. No setting change grants a new permission or proves an active model switch.

Version 1 remains readable. Preserve its recorded pairs and limit; do not invent
its missing client, enablement or edges, silently migrate it, or repeat onboarding.
During authorized setup/reassignment, obtain only material missing choices and
write version 2 after native agreement checks. Ordinary work can continue inline
when it does not require those missing choices. Unknown schema versions require
targeted clarification before editing the record, not a speculative rewrite.

### R3. Permit ordinary work without implicit onboarding

| Situation | Required behavior |
| --- | --- |
| Profile absent or unconfigured; task can run inline | Use the current session, apply relevant engineering rules and continue; no mandatory model questionnaire, profile write or delegation |
| User requests setup/reassignment | Run the corresponding skill, reuse explicit choices, ask only for missing material information |
| Task requires an unconfigured delegated role | Clarify its necessary choice before spawning; continue independent inline work |
| Configured profile is consistent | Reuse it; no repeated setup after a new task/session or compaction |
| Saved pair is unsupported or active settings differ | Expose the mismatch; do not claim conformity or silently replace the pair; resolve it before work requiring that assignment |

Using the current session with no configured selection is not an implicit saved
assignment. No automatic global or project-native configuration write follows
from reading AGENTS. A read-only inspection of the record may establish state;
it must not become a recurring full configuration audit.

### R4. Simplify common prompts and isolate compatibility detail

Preserve one detailed owner for each process rule: work modes, verification,
delivery, orchestration and model configuration. Root/role instructions retain
short critical constraints and explicit routes, not parallel complete procedures.

Add a task-to-section route table to `standards/core.md`. Bring the root AGENTS
template near the existing 40–70 substantive-line guideline while retaining
permission boundaries, work preservation, task scope, essential engineering rules
and completion evidence. Report justified exceptions rather than compressing lines
or removing safeguards to hit a quota. Line counts are not token savings.

Keep `standards/superpowers.md` focused on selection, authority and the necessary
adaptations. Move version-specific helper contracts and existing inspection limits
to `standards/superpowers/compatibility.md`. Register that file as a catalog resource;
read it only when using those helpers or resolving version compatibility. Preserve
the 6.4.1 evidence date. Inspect relevant available 6.4.2 contracts before adding
claims about that version; never infer a live pilot from source inspection.

No duplicate/shadow skills or plugin-cache patches. An unsupported helper may be
bypassed by directly reading a scoped task and reviewing its actual changes.
The fallback does not skip acceptance checks or add commits, repeated tests or
another progress ledger. Superpowers absence permits ordinary instruction-guided
work; report a missing capability only where the task actually requires it.

### R5. Preserve canonical native planning artifacts

Default new plain Markdown plans to workspace `docs/plans/`. Preserve an existing
OpenSpec/Spec Kit/native store in its supported location, including inside a nested
repository. A workspace navigation file points to it and carries no second task
checklist. The task handoff names the canonical store, workspace and implementation
checkout separately; changing cwd or creating a worktree does not change ownership.

Relocation is a distinct requested migration, not a prerequisite for an unrelated
task. Verify actual native tool paths when those tools are used. A genuinely
inaccessible canonical artifact remains a specific access obstacle; do not create
a divergent replacement. Independently opened projects retain reachable local
instructions and their native task entry, without assuming parent discovery.

### R6. Repair navigation and report readiness precisely

Change the two stale references to
`../doctrine/models-mapping.md#domain-model-placement`. Validate edited relative
links and anchors. For templates intended for relocation, document and check their
target base rather than classifying every source-relative mismatch as broken.

Keep accepted historical plans intact. New results belong in the new plan.
Readiness reporting distinguishes artifact checks, static compatibility inspection
and observed client execution. Library completion requires R1–R6 and the static
scenarios below. It does not require installation or a paid model call.

## Acceptance scenarios

| ID | Scenario | Expected evidence |
| --- | --- | --- |
| A1 | Small documentation edit; no routing file | Entry permits inline work and relevant artifact checks without setup or a persistent plan |
| A2 | Python-only fix; JavaScript React fix; substantive inline plan | Route walkthrough excludes unused frameworks, TS-only obligations and unrelated model/delegation setup |
| A3 | Configured single-agent workspace | Explicit client/pair, no enabled specialists, zero ceiling and no edges; native mapping is described |
| A4 | Configured delegated workspace; reviewer disabled | Enabled pairs/edges/ceiling agree; no reviewer spawn or accidental inherited role assignment |
| A5 | Legacy v1, partial setup, unsupported pair or unknown schema | Existing values preserved; no invented choice, automatic migration or false activation claim |
| A6 | Ordinary skill use versus helper/version investigation | Common policy suffices for the former; compatibility detail is conditional; applicable constraints survive delegation |
| A7 | Existing nested native task resumed from workspace, project or worktree | One canonical store/progress owner; no forced relocation or duplicate editable task |
| A8 | Revised bundle and documentation | TOML parses, resources and affected anchors resolve, policy owners agree, critical constraints survive shortening |

For each static scenario, record the input, expected reading/action path and any
remaining ambiguity. These walkthroughs establish instruction consistency, not
measured agent compliance. Do not build a new testing product around them.

## Follow-up adoption evidence

After the library changes, a separately authorized pilot can select one actual
project, one client/version and the user's model choices. Exercise a small inline
task, one justified delegation when configured, the selected stage checkpoint,
and resumption from the canonical task artifact. Observe loading and model/effort
through supported controls; record unavailable telemetry as unknown. Other clients
remain unverified until separately exercised. No percentage cost saving or universal
compatibility claim follows from file-size reduction or one successful task.
