# Client orchestration capabilities — 2026-10-04

Read for a relevant client capability or enforcement question. This is dated
source evidence, not portable runtime configuration. Shared policy remains in
[orchestration](../../standards/orchestration.md) and
[model configuration](../../standards/model-configuration.md). Earlier research
retains its original versions and outcomes; this note does not rewrite it.

## Documented comparison

Official pages were inspected on 2026-10-04. Documentation availability does not
establish support in a particular account, installed version or exposed harness.

| Capability | Codex | Claude Code | Cursor |
| --- | --- | --- | --- |
| Context and continuation | Subagent threads and steering are documented; a universal fresh/fork/resume parameter contract is not established by the cited page. Use the actual exposed tools. | Non-fork agents start fresh; forks inherit conversation, tools and model. Resume retains prior context; built-in Explore/Plan are one-shot. | Isolated subagent context; resume by agent ID retains context. A general fork switch is not established here. |
| Nesting | Validate the actual harness and selected edges; no universal depth inferred here. | Version/mode-dependent depth controls; forks cannot create further forks. | Since 2.5, children may spawn one further level, subject to Task access/policies. |
| Capacity | `agents.max_concurrent_threads_per_session` counts open spawned threads, excluding the primary; an idle retained thread is not synonymous with running work. | Running-agent limit differs from nesting depth; resume can exceed that spawn limit. | No universal running/thread-slot limit established by this page; inspect the exposed interface. |
| Restrictions | Custom agents support `sandbox_mode`; live parent overrides can supersede file defaults. | Tool allow/deny lists and permission modes; parent mode can supersede agent mode. | `readonly` restricts edits and state-changing shell commands. |
| Model and instruction context | Explicit spawn values override worker defaults; custom agents carry developer instructions. Required project context still needs a verified handoff. | Non-fork model configuration differs from fork inheritance. Built-in Explore/Plan skip CLAUDE.md; required rules need explicit supply. | Model selection may be substituted by plan/admin constraints. Complete project-instruction inheritance is not established here. |

Sources: [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents),
[Codex configuration](https://learn.chatgpt.com/docs/config-file/config-reference),
[Claude Code subagents](https://code.claude.com/docs/en/sub-agents),
[Cursor subagents](https://cursor.com/docs/subagents).

Claude's fork cache sharing can favor work needing the parent's context; this
does not establish a general cost advantage or authorize inherited history under
our selected policy. Cursor describes context startup overhead. Fresh context is
our isolation choice, not a token-savings guarantee. Sources: the Claude and Cursor
pages above. None of these documents demonstrates savings for this library.

## Local observation and limits

Read-only version commands in the source checkout returned:

| Command | Observed version | Evidence limit |
| --- | --- | --- |
| `codex --version` | `codex-cli 0.160.0` | Exit 0, with a read-only-filesystem warning about PATH aliases; no permissions changed |
| `claude --version` | `2.1.287 (Claude Code)` | Version only; no agent invocation |
| `cursor --version` | `3.22.12`, commit `3a92974361033b2051526321308c2740fe5912c0`, x64 | Editor binary; separate Cursor Agent CLI was not found on PATH |

The current session exposes `spawn_agent` with explicit fresh/history choices,
`followup_task`, `send_message`, `interrupt_agent`, `list_agents` and `wait_agent`.
Its schema restricts model/effort overrides on full-history forks; there is no
exposed close operation. These are inspected tool descriptions, not an execution
test or a universal contract for the locally installed CLI. The installed
Superpowers 6.4.2 Codex reference differs on full-history override support; actual
tool schemas and permissions take precedence. No plugin files were changed.

No workers, target clients, model pilots, native permission tests, cache benchmark
or paid comparison were run. Runtime model/effort, effective role restrictions,
instruction loading, slot reclamation and token savings remain unverified.
An idle worker, retained thread, pending shell tool and completed assignment must
be distinguished using available evidence before ownership transfer or cleanup.
The framework routing record cannot enforce those states or client permissions.

## Application to this library

Use only verified client controls during an authorized adoption. Keep selected
pairs and permissions; unknown capability is a reported limit, not permission to
invent a parameter or substitute a model. Supply essential task rules once, then
expand context for a concrete missing dependency. A built-in role that omits entry
files still needs those rules. Preserve evidence provenance and distinguish saved
agreement from actual execution. These are local engineering requirements.

When this optional note is omitted from a bundle, adapt its routes under the
[catalog contract](../../standards/catalog.md#assemble-a-portable-bundle) to labelled
source references through adoption provenance; do not create author-machine links.
