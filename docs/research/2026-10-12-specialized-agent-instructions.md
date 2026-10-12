# Specialized agent instructions — 2026-10-12

## Scope

Official documentation and engineering articles were inspected on 2026-10-12 to
prepare AEK's Codex architect, implementer and reviewer instructions. This is
source review, not a comparative model evaluation or a target-client execution.
Policy owners remain [orchestration](../../standards/orchestration.md),
[model configuration](../../standards/model-configuration.md) and
[verification](../../standards/verification.md). The
[canonical task](../plans/2026-10-12-specialized-agent-adoption.md) owns progress.

## Sources and application

| Official source | Relevant guidance | Application in this change |
| --- | --- | --- |
| [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents) | Project role files configure spawned sessions. A focused responsibility and suitable tools help define a specialist; model and effort can be explicit. Parent runtime overrides affect permissions. | Add an optional architect TOML; keep per-role pairs and set read-only defaults for architect/reviewer without claiming effective containment. |
| [OpenAI: custom code review rules](https://developers.openai.com/blog/custom-code-review-rules-for-codex) | Review guidance is most useful when tied to consequential scoped invariants and actionable findings; broad rules can produce noise. Mechanical formatting belongs in existing checks. | Clarify concrete failure priorities and evidence in the reviewer; avoid a finding quota or cosmetic preferences presented as defects. This article discusses native Code Review, not activation of AEK's custom reviewer. |
| [OpenAI: rethinking skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | Conditional reference selection and concise entry instructions reduce irrelevant context; rigid universal recipes can impede stronger models. | Route roles to existing owners and only selected task skills; retain context/evidence reuse rather than adding another mandatory reading or testing cycle. The article is model-specific and does not prove equal effects across models. |
| [Anthropic: multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | Delegation benefits from a specific objective, result format, tools/source guidance and clear boundaries. Parallel research differs from tightly coupled coding work. | Preserve AEK's sufficient handoff contract and return focused decisions/evidence. Do not infer that three roles must run for each coding task or that more agents save tokens. |

The architect's returned design and coordinator-owned artifact, enabled-role
selection, stage checkpoints and acceptance rules are AEK engineering choices.
They are not built-in Codex sequencing or enforcement. Model IDs in the inactive
examples remain suggestions; no source establishes their availability to a user.

## Review scenarios

- Settled local change: coordinator or selected implementer uses existing rules;
  the presence of an architect definition does not mandate a design handoff.
- Material interface change: architect inspects affected owners and returns
  design/compatibility decisions and acceptance cases; coordinator records them
  under the existing decision checkpoint before dependent implementation.
- Small authorization change: review need follows risk and required policy,
  rather than line count; reviewer reports an evidenced failure when present.
- Existing project with customized assignments: a bundle update preserves them;
  adding a role requires a selected pair/edge and reconciliation of native targets.
- Missing optional task skills: roles follow direct adopted policy routes without
  installing a profile or depending on the original AEK checkout.

These are source-level contract inspections, not observed agent runs. The task
records artifact and disposable-fixture checks separately. Native discovery,
actual model/effort, parent permission overrides, behavior quality, latency and
token savings remain untested. Earlier research retains its original scope.
