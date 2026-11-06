# Angular reference skill evaluation: 2026-11-06

Decision: retain the current direct Angular routes. Do not add the evaluated
`aek-angular` template, catalog preparation resource or native adoption mapping
at this checkpoint. The candidate worked, but the bounded comparison did not
establish enough incremental value to justify another maintained entry. This is
not a claim that skills are generally ineffective or that the candidate can never
help. The [canonical plan](../plans/2026-11-06-guidance-quality-and-skill-delivery.md)
owns E1 progress and the deferred S3/S4 scope.

## Method and controlled inputs

The coordinator applied installed Superpowers 7.0.1 `writing-skills` reference
retrieval/application checks and `verification-before-completion`, through AEK's
local adaptations. A direct-route baseline preceded candidate evaluation. The
candidate contained 181 words, including metadata: a narrow Angular trigger,
links to the existing Angular entry and Superpowers adaptations, and scope/output
boundaries. It introduced no new Angular rule, example or independent workflow.

The test client was installed Codex CLI 0.167.0, using the saved
`gpt-6-astra` / `high` defaults and existing account. Native `model/list` confirmed
that pair was supported. Eight fresh, ephemeral, read-only invocations reviewed
three small supplied-code scenarios; the component pair was repeated with the
candidate first to reverse its initial order. Prompts within each pair were
identical, including scope, response language/length and prohibition of edits,
installs, plans, builds and further agents.

Both fixtures contained the same 50 files: the current adopted Angular/TypeScript
bundle, adapted entry, declared versions and review inputs. The candidate arm
added only `.agents/skills/aek-angular/SKILL.md`. SHA-256 inventories confirmed
identical shared content and unchanged fixture contents after every run. Angular
20.3.0 was declared; no dependencies or application runtime were installed.
The [S2 runtime results](2026-11-06-angular-component-contracts.md) remain separate.

Process-only client overrides selected one configured Superpowers plugin source
and disabled unrelated plugins/MCP servers; persistent settings were unchanged.
**Limit:** these CLI subjects did not discover/load an installed Superpowers
procedure in their searched skill locations. They read AEK's local adaptations
and used its inline fallback. The coordinator did use the installed Superpowers
skills for the evaluation. The comparison therefore does not establish behavior
in a client session with native Superpowers procedures actively loaded.

## Discovery versus actual use

Native `skills/list` returned 44 entries for the control and 45 for the candidate,
with no discovery errors. The additional entry was enabled, repository-scoped
`aek-angular`; all other metadata was identical. Tool traces show the skill body
was read in all three Angular candidate runs and was not read for the independent
TypeScript helper. This establishes observed implicit use in those runs, not a
general activation rate or proof about explicit invocation/coexistence cases.

This distinction follows the official [Codex customization contract](https://learn.chatgpt.com/docs/customization/overview#skills):
metadata makes a skill discoverable; its body and references are loaded on demand.
Successful parsing or discovery alone was not counted as a task benefit.

## Reviewed outcomes

The coordinator read complete answers and tool traces against the scenario
criteria. These are assessed review responses, not executed Angular behavior.

| Scenario | Criteria met: direct / skill | Completed shell commands: direct / skill | Web searches: direct / skill |
| --- | --- | --- | --- |
| Conditional child, optional projected action and lazy-creation misconception | 4/4 / 4/4 | 6 / 7 | 3 / 2 |
| Directive input updates, exposed aliases, nested Escape, cleanup and SSR limits | 5/5 / 5/5 | 5 / 7 | 1 / 1 |
| Framework-independent TypeScript sum with an explicit valid-input contract | 2/2 / 2/2 | 3 / 9 | 0 / 0 |
| Component scenario, repeated in reverse order | 4/4 / 4/4 | 7 / 8 | 2 / 2 |

Both arms identified the conditional view-query/constructor focus defects,
optional content-query mismatch and false projection laziness. Both directive
reviews identified stale captured input, missing host-directive aliases,
already-handled events and unowned browser listeners; they distinguished an SSR
portability risk from an executed server failure. Both proposed compatible
corrections and relevant checks. Neither invented a material defect in the plain
helper or selected Angular-specific rules for that negative case.

No material task-scope violation was observed. No fixture edits, installations,
builds, plans or delegated agents occurred. The candidate did not recover a missed
technical criterion or show more selective local reading: both arms still loaded
substantial shared guidance, and candidate shell-command counts were higher.
Commands may batch different reads, so their count is not itself a cost measure.

## Usage signal and its limits

These are client-reported token totals, not billed cost. Cached input is a subset
of input. Wall time includes tools and service scheduling; some independent
scenarios overlapped, and shared cache/order effects were not fully controlled.

| Run | Input tokens: direct / skill | Cached input: direct / skill | Output tokens: direct / skill | Seconds: direct / skill |
| --- | --- | --- | --- | --- |
| Component, first | 259264 / 204050 | 212736 / 167936 | 1634 / 1791 | 73.301 / 66.359 |
| Directive | 173423 / 158886 | 139648 / 125312 | 1247 / 1513 | 53.258 / 54.520 |
| Plain TypeScript | 101667 / 102473 | 72576 / 72704 | 430 / 532 | 20.787 / 23.947 |
| Component, repeat | 244237 / 198600 | 202752 / 162432 | 1829 / 2063 | 77.107 / 89.694 |

Lower reported input in the Angular runs is a favorable signal worth retaining;
it is not being dismissed or converted into a claim of zero benefit. However,
outputs increased in every pair, local command counts increased, latency did not
improve consistently, and only one task was replicated. This sample does not
establish general token/cost savings, a reliable causal effect or superiority for
implementation work. No price calculation or statistical significance is claimed.

## Decision and retained evidence

The existing [Angular task table](../../standards/angular.md#read-by-task) already
reaches the authoritative owners and satisfied every evaluated technical criterion.
Under the user's benefit-first condition, keep that working path and defer source
integration. A concrete missed route, a useful manual-invocation requirement, or
a more representative controlled comparison can reopen the candidate. Do not add
duplicate rules to manufacture a difference between the arms.

This bounded pilot does not complete the broader S4 rollout matrix: implementation,
older forms/NgModule setups, route races, real SSR/hydration, missing resources,
overlapping skills, other clients and native Superpowers composition were not
fully evaluated. No native installation into AEK or a consuming project follows
from this record. Runtime compilation of the reviewed snippets was not requested
and is not claimed.

Raw prompts, candidate, fixture snapshots, discovery responses, complete outputs,
tool traces, usage, scoring and source hashes are retained outside active discovery:
`/home/vitalii/.codex/research/aek-guidance-2026-11-06/angular-skill-evaluation/`.
They are evidence, not another progress owner or a skill installation. The stage's
original baseline was `/tmp/aek-angular-eval-2026-11-06-uwihtq0x/baseline.json`;
the retained archive includes its contents and pre-edit copies.
All 82 payload files were verified after copying. The temporary workspace was
removed; the candidate survives only as archived evidence outside skill discovery.
