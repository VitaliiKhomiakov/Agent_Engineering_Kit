# Framework readiness review

Date: 2026-09-27. Status: complete; static library readiness confirmed after corrections; target runtime unverified.

## Goal and boundaries

Assess whether a new or existing target can receive coherent coding, architecture,
pattern/structure and especially agent-orchestration guidance. Review the actual
entry → catalog → selected rules/templates → role handoff path; correct concrete
library defects. Keep instruction quality, portable artifacts and observed client
behavior as separate claims.

Canonical review record: this file. Workspace/checkout:
`/home/vitalii/Documents/Local_Project/AgentsFramework`. Baseline and disposable
checks: `/tmp/af-final-review-al4yt0kv/`. User requested this final audit and does
not want target application yet. No target installation, agent/model invocation,
engine session or Git mutation is part of this review. Git metadata was unavailable
during the preceding merge request; files remain the evidence source.

## Review approach

- Inspect common policy, profile selection, architecture/pattern owners and entry
  contracts. Cover Python services/small tools, Go packages, React feature layout
  and Unreal's engine model; validate all catalog paths and local route structure.
- Check orchestration selection/role contracts against current primary client
  documentation, including permission, model/effort, context, nesting and limits.
- Assemble disposable selected bundles with inactive orchestration resources;
  validate required local references without relying on source archives or a parent.
- Walk through inline/delegated, disabled-role, conflicting-model, overlapping-write,
  and checkpoint scenarios. Reuse prior import/update/recovery acceptance; no repeat
  of unrelated engine/runtime examples or broad benchmarking.

## Findings and corrections

| Finding | Consequence | Resolution |
| --- | --- | --- |
| F1: catalog did not enumerate orchestration support templates or itself | A catalog-only bundle omitted the routing example, model skills and native-role examples referenced by required rules; import depended on manual discovery beyond the manifest | Add the catalog asset and seven existing model-configuration resources, preserving inactive locations, schema and profile identities |
| F2: model-configuration still assigned adoption provenance to entry/passport | Conflicting owners could produce duplicate/outdated import state after the new adoption record was introduced | Route provenance to adoption.md while retaining operational constraints in local entries/passports |
| F3: optional source-archive links had no precise omission treatment | A minimal bundle could retain dangling evidence links or expand into unrelated historical documents | Clarify source-reference adaptation for optional evidence; required local routes must remain reachable |
| F4: conditional cross-profile routes were underspecified during copy | The React-only bundle check found a link from the JavaScript entry to absent NestJS | Adapt only routes whose conditions are inapplicable; include the profile closure when the condition actually applies |

These are source-library corrections. They add no default model assignment,
mandatory agent, installed role or executable importer. The architecture and
pattern rules continue to select components by actual need and technology.

## Current client evidence

Primary documentation retrieved on 2026-09-27:

- [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
  documents project role TOML with name, description, developer instructions and
  optional model/effort settings. The retained native role examples match these
  documented fields; target-version discovery still needs observation.
- [Codex configuration](https://learn.chatgpt.com/docs/config-file/config-reference)
  documents agents.enabled, explicit worker defaults and the concurrency limit
  excluding the primary thread. Framework edge policy remains a separate constraint.
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents) documents
  model/effort fields and instruction-loading differences: built-in Explore/Plan
  omit CLAUDE.md and custom agents can opt out. Explicitly supplying applicable
  policy in a handoff is therefore a necessary supported scenario.
- [Cursor subagents](https://prod.cursor.com/docs/subagents) documents project and
  compatibility role locations and model selectors with per-model parameters.
  The framework correctly requires collision checks and verified client mappings.

This evidence supports native-format guidance, not account model availability,
active settings or successful orchestration in an installed client. The full set
of architect/planner/explorer/test roles is described as responsibilities;
ready native examples cover implementer and reviewer, with other role definitions
prepared only when selected.


## Engineering and architecture assessment

| Area | Inspected decision contract | Assessment |
| --- | --- | --- |
| Coding | Core typed boundaries, invariant ownership, cohesion, explicit effects and proportionate verification | Coherent shared guidance; project gates and meaningful safeguards remain binding |
| Architecture | Core dependency direction and passport facts/targets, Python capability boundaries, Go packages | Structure follows actual responsibilities; small scripts/libraries do not require a service scaffold |
| Patterns | Concrete conditions and simpler alternatives for Factory, Strategy, Facade, Adapter, DI, Repository and Result composition | Patterns are conditional design choices, not classes to manufacture for catalog compliance |
| Frontend | React ownership and compact feature layout; conditional Next.js/server/client sections | Applicable sections are selected by actual stack; bundled TypeScript does not make a JavaScript project typed |
| Unreal | Engine-managed creation, lifecycle, reflection, assets/editor state and scoped runtime sections | The engine integration model remains explicit; backend patterns are not automatic defaults |
| Import | Concrete preparation, active conflict replacement, ownership, repeat/update/recovery and source lookup | Complete instruction procedure; native installation remains a target operation |

This is a contract/route review with representative deep inspections, not a fresh
line-by-line technical audit of every language example or proof that all future
architectural decisions will be correct. Existing technology research and prior
example checks remain the dated evidence for unchanged technical details.

## Orchestration scenarios

These are instruction walkthroughs grounded in `standards/orchestration.md`,
`standards/model-configuration.md`, the role templates and task/entry templates.
No model was spawned to simulate compliance.

| Scenario | Required and documented outcome |
| --- | --- |
| O1: absent or unconfigured routing | Ordinary work remains inline; no invented model choice, onboarding or delegation |
| O2: configured single-agent mode | No specialist spawn; zero framework ceiling and empty edges; native disabling only through supported controls |
| O3: permitted implementer handoff | Enabled endpoints, allowed edge, explicit pair, task permission and capacity all checked; template values alone grant nothing |
| O4: disabled reviewer | No anonymous/default-model substitute; routine review stays with coordinator, required independence needs an authorized enabled assignment |
| O5: nested delegation | A task dependency does not create a spawn edge; nesting needs an explicit edge and actual client support |
| O6: cycles, self-edges or unknown endpoints | Invalid routing is resolved before dependent spawning; a report to the coordinator is not a reverse spawn edge |
| O7: concurrency at capacity | The ceiling limits concurrent work; useful independent ownership is required, not a target number of agents |
| O8: two writers touch the same state | Coordinate or isolate ownership; do not rely on parallel branch checks as integration evidence |
| O9: saved pair differs from active session | Report the mismatch/unknown state; do not claim successful model switching or silently substitute |
| O10: fresh worker lacks parent context | Supply applicable policy, scope, paths, canonical task, stage, permissions, baseline and evidence; disable history inheritance when supported |
| O11: review requests corrections | Use bounded correction handoffs and revisit affected evidence; no automatic repeated full review/test campaign |
| O12: checkpoint or inaccessible task store | Workers stay within the authorized stage; report access gaps rather than creating a second task record |

Ready native role examples cover implementer and optional reviewer. Other named
responsibilities can remain with the coordinator or receive client-specific roles
when explicitly selected. The default inline mode is deliberate; importing rules
alone does not enable multi-agent execution. Edge restrictions and workflow order
are instruction policy unless native enforcement was separately verified.

## Verification and remaining boundary

PASS: `python3 /tmp/af-final-review-al4yt0kv/check.py` checked:

- 20 unique profiles, existing dependency graph without cycles, and 156 existing
  catalog paths. Profile changes are limited to model-configuration resources;
  existing identities, dependencies and applicability remain unchanged.
- 164 rule/template/document artifacts, 586 local links/fragments, seven TOML
  files/blocks including the catalog and four YAML frontmatters.
- Three disposable bundles: Python-only (42 files), JavaScript React (59 files)
  and Blueprint Unreal (30 files). Required local references stay inside each
  bundle after explicit source-evidence and inapplicable-route adaptation.
- Inactive model-routing, native config and role examples agree on their suggested
  model/effort pairs and concurrency; the record remains unconfigured and the
  reviewer disabled. Bundling creates no active `.codex/` or `.agents/` directory.

The first bundle attempt failed specifically on the React → absent NestJS link;
inspection confirmed an inapplicable conditional route, leading to F4. The updated
bundle check passed. No actual required dependency was removed to suppress failure.
The temporary script and bundles are evidence fixtures, not a new runtime importer
or permanent test suite. `checks.json` and the scoped `changes.diff` are retained
with originals in the baseline directory.

Changed library files: `standards/catalog.toml`, `standards/catalog.md`,
`standards/model-configuration.md`; this review record is new. Scoped review found
no unresolved blocking issue in the inspected contracts after F1–F4. Final report
text changes no checked rule/template inputs or local links; no extra final rerun.

**Conclusion:** the library can supply coherent coding, structure, pattern and
orchestration instructions through the documented import. A coordinator must still
adapt concrete project facts and activate an explicitly selected client/role scheme.
Actual instruction discovery, adherence, model availability, isolation controls,
checkpoint behavior and resumption require a scoped real-client pilot. No target
application was performed, as requested. Static evidence does not justify a
promise of error-free generated code or guaranteed autonomous agent behavior.
