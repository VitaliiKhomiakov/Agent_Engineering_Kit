# Project purpose and native agent orchestration research

Date: 2026-09-20. Status: capability research and design rationale.
Product decisions are now owned by the
[specification](../specs/2026-09-20-agents-framework.md), with progress in the
[delivery plan](../plans/2026-09-20-native-client-adoption.md). Read them for the
agreed scope; the proposals below preserve the research context and evidence.

This note records the user's clarified purpose, verified client capabilities,
and the recommendations used to update the draft standard. The research did not
activate configuration or establish end-to-end subscription/runtime behavior.

## User requirements

Agent_Engineering_Kit should adopt development rules in new and existing projects,
selecting relevant architecture, design, coding, testing, and review guidance
for their languages, frameworks, databases, and other technologies. Model
orchestration is a central part of adoption.

Each deployment configures roles **inside one selected client**, such as Codex
or Claude Code. It uses the installed CLI and the user's existing subscription
and sign-in. Coordinating work between different clients is outside this scope.
Support for multiple providers means separate native adapters; usable models
still depend on the selected client and account.

The user needs model and reasoning-effort choices by responsibility, including
design, planning, architecture, exploration, implementation, testing, and review.
The supplied model names illustrate choices; they are not saved assignments.
Future releases must not require editing a fixed model list in the framework.

One workspace may contain several independent repositories with local
instructions. Workspace rules should govern their shared policy. Adoption must
work both from the workspace and when a repository is opened independently.

Two requested capabilities are a terminal configurator assisted by an AI model
and visibility into which model each running subagent uses. Design patterns,
including Factory, Facade, Strategy, and appropriate monadic composition, should
be considered when useful, with no obligation to introduce them.

## Evidence and limits

Read-only local inspection confirmed:

| Component | Installed version | Evidence inspected |
| --- | --- | --- |
| Codex CLI | 0.155.1 | Version, command help, generated app-server JSON schemas |
| Claude Code | 2.1.275 | Version and command help |
| Superpowers | 6.4.1 | Installed skills and the existing compatibility adaptation |

Official documentation was checked against these versions. No subscription
model call, authenticated catalog request, or end-to-end role activation was
performed. No CLI upgrade, login change, or target configuration was applied.
Documented capability does not establish availability for this account.

## Native roles and reasoning effort

| Concern | Codex | Claude Code |
| --- | --- | --- |
| Project role definitions | `.codex/agents/<role>.toml` | `.claude/agents/<role>.md`, YAML frontmatter and Markdown instructions |
| Model selection | `model` | `model` |
| Reasoning selection | `model_reasoning_effort` | `effort` |
| Native inspection | Agent threads through `/agent` | Tasks and subagents through `/tasks` |

Codex roles contain `name`, `description`, and `developer_instructions`.
Explicit model/effort values in a custom agent file take precedence over spawn
arguments; remaining values can come from spawn settings, agent defaults, or
the parent. Set and validate the pair together. See
[Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

Claude Code supports per-role model and effort settings. Invocation parameters
can override the role's model; environment settings can alter or force model
selection. `/tasks` reports the model and explicitly specified effort on the
installed version. Built-in Explore and Plan agents skip `CLAUDE.md`, so roles
that require the project policy need an explicit instruction-loading design.
See [Claude Code subagents](https://code.claude.com/docs/en/sub-agents).

Effort labels are client- and model-dependent. The Codex schema advertises
`supportedReasoningEfforts` per model and represents effort as a string. Claude
Code also constrains effort by model and can apply environment or managed
limits. The configurator should validate each selection, report overrides, and
avoid silently translating one client's effort levels into another's. See
[Codex app-server](https://developers.openai.com/codex/app-server/) and
[Claude Code model configuration](https://code.claude.com/docs/en/model-config).

Proposed responsibilities are independently configurable:

| Role | Responsibility |
| --- | --- |
| Orchestrator | Own the task, delegation, stage transitions, and user checkpoints |
| Architect | Design boundaries, contracts, and architectural decisions |
| Planner | Produce an actionable plan when separate planning is useful |
| Explorer | Investigate the relevant code and constraints |
| Implementer | Make the assigned change and provide evidence |
| Test runner | Design or assess tests and investigate results when delegated |
| Reviewer | Independently assess a stable, completed scope |

The user's preference is to make strong models available for design, planning,
architecture, and review, with separate choices for coding and testing. A
responsibility need not create another agent for every task. In particular,
running a deterministic test command alone does not require another model.
Role availability should not create duplicate planning or repeated test suites.

The adapter must also distinguish a custom reviewer role from a client's native
review command; configuring one does not prove the other uses the same model.

## User-provided orchestration schemes as configurable profiles

The user confirmed the project interpretation and asked whether their example
schemes can become a configurable feature. They are useful inputs for reusable,
editable profiles. They still do not select an active client or model assignment
for this workspace.

A proposed profile separates three concerns:

- Role assignments: the coordinator and available specialist roles, with a model
  and supported effort for each role.
- Delegation structure: which role may launch another, the concurrency ceiling,
  and any supported nesting limit.
- Work progression: conditions for using each role, dependencies between steps,
  required outputs, review findings returned for correction, and user checkpoints.

In the user's flat scheme, the main coordinator launches architect, explorer,
implementer, test runner, and reviewer as direct children. A task can still
proceed through exploration, design/planning, implementation, testing, and review
in sequence. A task-order arrow does not imply that the preceding worker must
spawn the next worker. Parallel work requires independent inputs and ownership;
the presence of several branches alone does not make their work independent.

The other supplied scheme can describe implementation followed by testing and
review, or a literal hierarchy of nested workers. The configurator should show
this distinction explicitly. Claude Code currently documents nested delegation
with a configurable depth limit; the adapter must check the installed version
and active limits before accepting a nesting-dependent profile. See
[nested Claude Code subagents](https://code.claude.com/docs/en/sub-agents#let-subagents-spawn-their-own-subagents).

Recommended initial behavior: offer the supplied coordinator-based scheme as
an editable starting point. Let the user add or disable optional roles, select
models/efforts from the client catalog, and choose task conditions and ordering.
Preserve the scheme when a model assignment changes. Keep mandatory project
checks and explicit user checkpoints when a preset changes.

Native role files configure agents; merely creating them does not execute a
fixed pipeline. The proposed first version supplies the selected progression
and handoff contract to the coordinator through project instructions and scoped
skills. That is model-directed execution and needs pilot verification. Any
claim of mechanically enforced ordering requires a separate supported execution
control and evidence that it enforces the transitions.

## Workspace policy and nested repositories

Three mechanisms must be handled separately: instruction discovery, native
configuration precedence, and model selection during agent creation.

Codex composes project instructions toward the current directory, with nearer
instructions taking precedence. Its project boundary is typically a repository
root; a parent workspace outside that boundary must not be assumed loaded.
Configuration also has its own precedence and trust requirements. See
[Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
and [configuration basics](https://learn.chatgpt.com/docs/config-file/config-basic).

Claude Code composes instructions from its supported locations; a root file is
not an enforceable top-level policy merely because it is higher in the tree.
The documented native `AGENTS.md` support starts at 2.1.277, after the installed
2.1.275. For that installation, a `CLAUDE.md` importing `@AGENTS.md` is an
appropriate compatibility route. JSON settings follow separate precedence.
See [Claude Code memory](https://code.claude.com/docs/en/memory) and
[settings precedence](https://code.claude.com/docs/en/settings#settings-precedence).

Recommendation: give shared policy one owner, record repository exceptions,
and generate supported entry points that make the applicable policy reachable.
During adoption, identify conflicting local instructions and prepare a concrete
reconciliation. Validate both workspace and standalone repository entry points;
recheck generated files for later drift. Do not claim that a generated prompt
can override client or managed controls. Requirements needing enforcement also
need suitable deterministic checks, such as dependency or type checks.

## Showing the model used by a subagent

Use the client's existing task/thread view first. A dedicated terminal emulator
is not a prerequisite. An optional monitor should distinguish:

| Displayed value | Meaning |
| --- | --- |
| Selected | The user's saved role/model/effort choice |
| Configured | The client's reported settings for the active thread |
| Runtime reported | A response or event identifies the model used for an operation |
| Unknown | Available evidence does not establish the value |

The local Codex schema exposes agent role, parent thread, model, and effort.
Its thread model/effort fields explicitly describe configuration, not per-turn
execution telemetry. Spawn events also carry requested settings. The separate
`model/rerouted` event reports substitutions. A monitor must preserve these
distinctions instead of labeling every configured model as execution evidence.
See [Codex app-server](https://developers.openai.com/codex/app-server/).

Claude Code provides structured output and agent execution metadata. Its SDK
documents `resolvedModel` and `modelsUsed` for agent results, and assistant
messages can identify a response model and parent tool call. A start hook alone
does not prove the resolved model; session model-switch hooks are not complete
evidence for every fallback. See the
[TypeScript SDK reference](https://code.claude.com/docs/en/agent-sdk/typescript)
and [hooks reference](https://code.claude.com/docs/en/hooks).

A proposed display is: role, task, status, configured model, configured effort,
runtime-reported model when available, and any mismatch. Missing telemetry must
remain visible. Do not expose internal chain-of-thought; effort is a setting.

## Terminal configurator and changing model catalogs

Recommended approach: extend the existing framework-owned
[model-routing TOML](../../templates/framework/model-routing.toml) into a
versioned neutral contract, then render settings through one selected adapter.
Codex output remains TOML; Claude agent output remains Markdown with YAML.
There is no requirement to make both clients consume the same native format.

Three implementation options have different costs:

| Option | Benefit | Limitation |
| --- | --- | --- |
| Instruction-only setup skills | Smallest extension of the current project | Validation and discovery depend on the executing agent |
| Terminal wizard plus native adapters | Repeatable inspection, validation, and targeted configuration changes | Requires maintaining client capabilities and file mappings |
| Wizard plus live monitoring client | Adds a unified view of tasks and reported models | Adds streaming, lifecycle, and version compatibility work |

The second option best fits the clarified goal. Monitoring can follow after
native configuration works reliably.

Proposed flow:

1. Inspect the workspace, nested repositories, existing rules, installed client
   version, and supported native capabilities.
2. Select the client and use its existing authentication. The first AI-assisted
   setup necessarily runs under the model that starts that setup session.
3. Obtain supported model IDs and effort options from native capabilities. For
   Codex, `model/list` provides a catalog. Claude's SDK documents
   `supportedModels()`; using it as a local catalog bridge with the installed
   CLI and subscription requires a focused compatibility check. Until verified,
   allow selection from the native model UI or entry of a native ID and label
   unverified availability explicitly. Do not invent a `claude models` command.
4. Let the AI propose relevant profiles and role assignments from inspected
   facts. Deterministically validate its structured proposal and show the
   resulting configuration changes. Reuse choices the user already supplied.
5. Apply authorized field-level changes, preserving unrelated settings, custom
   roles, comments, and local modifications. Report collisions or partial writes.
6. Check saved/native agreement, then verify the active assignments in a fresh
   session or through a supported reload. File writes alone do not switch models
   already running.

Use native sign-in without copying tokens or requesting new API credentials.
Both clients document subscription authentication; Claude's `--bare` mode omits
the normal subscription credential path and is unsuitable for this design. See
[Codex authentication](https://developers.openai.com/codex/auth/),
[Claude Code authentication](https://code.claude.com/docs/en/authentication), and
[programmatic CLI usage](https://code.claude.com/docs/en/headless).

The catalog is observed data, separate from saved assignments. Record its
client/version and observation time, supported efforts, and whether an entry is
an alias or pinned ID. Refreshing it may propose an upgrade but must not silently
reassign roles. Unsupported or unavailable choices require an explicit
resolution. A catalog entry still does not guarantee a successful call under
current account limits.

## Rule profiles and design patterns

Compose only relevant guidance: shared engineering rules, language constraints,
framework conventions, database/infrastructure concerns, and declared project
exceptions. Existing projects need an inventory and incremental migration;
new projects need initial architecture and configuration. Neither should load
the entire rule library for every task.

For each pattern, describe the problem it solves, a trigger, simpler alternatives,
and verification of its benefit. A Facade may simplify an established subsystem
boundary; Strategy may separate genuinely interchangeable behavior. Factory
guidance should retain its existing justification requirement. Monadic
composition belongs in language-specific guidance where Option/Result or
effectful composition already fits the code; it is not a universal class
architecture requirement. These are proposed framework policies, not client
features.

## Changes implied for draft 0.2

The current [architecture](../../ARCHITECTURE.md),
[orchestration standard](../../standards/orchestration.md), and
[model setup contract](../../standards/model-configuration.md) already provide
useful foundations: scoped rules, saved selections, native-file consistency,
conditional delegation, and stage checkpoints.

The clarified goal calls for these additions:

- Separate client adapters and version/capability detection; existing native
  templates cover Codex only.
- Independently configurable design/planning/exploration/testing roles beyond
  the existing orchestrator, implementer, and optional reviewer.
- Database and technology profiles, plus conditional pattern guidance.
- Explicit nested-repository policy reconciliation and drift checks.
- A terminal configurator with validated catalog-driven selections; existing
  setup/reassignment skills are instruction-only templates.
- Assignment verification and optional runtime reporting with honest unknowns.

Superpowers remains a development workflow toolkit. Its role is to help analyze,
plan, implement, and review work under the adopted project policy. Native adapters
and deterministic tooling own configuration mechanics. Keep the existing
[Superpowers 6.4.1 adaptation](../../standards/superpowers.md) and proportionate
verification instead of making every role a mandatory workflow stage.

The delivery plan now owns the configuration-contract and adapter work. Its
subsequent pilot should cover each selected client on a temporary
target: initial setup, partial reassignment, unsupported effort, nested policy
loading, manual-setting conflicts, unchanged unrelated configuration, and no
repeat onboarding on an ordinary later task. Run a small live delegation only
when that pilot is authorized; confirm assignment evidence and the expected
stage checkpoint. The current evidence does not replace that pilot.
