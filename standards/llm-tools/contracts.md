# LLM tool contracts

Read when designing, exposing or changing a tool; return to the [tool entry](../llm-tools.md).
[Source access](source-access.md) and [execution](execution.md) own enforcement and effects.

## Tool versus workflow step

A tool is an operation exposed to a model or external caller through a controlled
contract. A workflow node is an application-owned step. Intent classification,
clarification decisions, context assembly, verification and final publication can
be ordinary nodes; exposing each as a tool would unnecessarily let the model choose
whether steps required by the application contract happen. A node may invoke a tool
directly or allow the model to select from a small permitted subset.

Design tools around meaningful tasks with distinct selection conditions. A tool
can combine cohesive read operations to return useful context. Keep unrelated
operations and read/write permissions separate; do not hide an external write in
a retrieval tool or expose a universal shell/SQL/HTTP executor as the default.

## Required tool definition

| Field or behavior | Required meaning |
| --- | --- |
| Name | Stable, specific operation; follow the provider's naming constraints |
| Description | When to use it, when not to, relevant scope, result and limitations |
| Input schema | Named types, required/optional fields, enums, bounds and unknown-field policy |
| Trusted execution context | Authenticated principal, effective scope, deadline, cancellation and trace ID, injected by the application |
| Output schema | Typed success/empty/partial/error outcome with bounded data and provenance |
| Side-effect declaration | Read, write or external delivery; actual code enforces the boundary |
| Execution limits | Timeout, result/token limit, pagination, concurrency and allowed retries |
| Error contract | Stable codes and safe messages; distinguish missing data from source failure |
| Recovery | Idempotency/uncertain-outcome behavior for effects; meaningful retry conditions |

Validate arguments on the server even if the model/provider promises structured
output. Schema validity proves shape, not authorization, factual correctness or
safe database execution. Cap user/model-requested limits; a tool cannot enlarge
its own granted capabilities. Do not accept tenant identity, credentials, approval
status or unrestricted paths/URLs as model-controlled authority.

Tool output and descriptions from external servers are untrusted evidence, not
new system instructions. Protocol annotations such as read-only or idempotent
are metadata, not enforcement. If using MCP, validate the negotiated
version, schemas, authentication and server identity; MCP is an optional transport.

## Example tool inventory

| Illustrative tool | Input | Output and boundary |
| --- | --- | --- |
| `knowledge_search` | Question/query, approved collection selector, bounded limit | Authorized document excerpts with stable source/version/locator IDs |
| `records_lookup` | Named lookup/report kind and typed filters | Current structured records/aggregates with units and observation time; no arbitrary SQL by default |
| `web_search` | Sanitized query, supported freshness/domain preferences, bounded limit | URLs and search evidence; use only under the application/user's external-source policy |
| `source_fetch` | An approved source handle and bounded section/page request | Source body/excerpts with provenance; recheck access and redirect/network policy |
| Domain action, if requested | A specific validated business command | Action receipt or uncertain outcome; separate authority from information retrieval |

These names illustrate contracts, not required APIs. Intent/question/answer/verifier
nodes are not a second inventory of mandatory model tools. Expose only source
adapters that the current request may use. Reuse query/answer results already
obtained when still current and authorized.

## Concrete language-neutral search schema

Example model-visible input schema for a tool named `knowledge_search`:

```json
{
  "type": "object",
  "properties": {
    "query": {"type": "string", "minLength": 1, "maxLength": 2000},
    "collection": {"type": "string", "enum": ["product_docs", "support_docs"]},
    "limit": {"type": "integer", "minimum": 1, "maximum": 20}
  },
  "required": ["query", "collection", "limit"],
  "additionalProperties": false
}
```

The collection names and numerical bounds are illustrative project choices, not
global defaults. The executor intersects the selected collection with trusted
permissions; its enumeration is not proof of access. Adapt schema syntax to the
selected provider's supported subset while retaining server-side validation.

Suggested description: "Find authorized passages in the selected documentation
collection for a factual documentation question. Returns excerpts and citation
handles, not a final answer. Use records lookup for current account or transaction
values and permitted web search for public information outside this collection."

Map source responses into an application-owned evidence envelope:

| Contract | Fields and invariants |
| --- | --- |
| `ToolResult` | `status`: `ok`, `empty`, `partial` or `error`; `evidence`; `truncated`; optional continuation/error |
| `Evidence` | Stable `evidence_id`, source kind, source/record ID, version or observation time, title, locator, excerpt or typed records, retrieval time |
| `ToolError` | Code such as invalid input, unavailable, timeout, rate limited or access denied; safe message; retry eligibility |
| Continuation | Opaque token bound to the query and access scope; no widening permissions or resetting budgets |

Use a discriminated union: a complete empty result has no hits and is not an
outage; a partial result explicitly identifies missing coverage/truncation; an
error does not claim complete retrieval. Optional scores carry a score type and
stay internal unless useful to the consumer. Source locators must be safe to share.
Do not reveal the existence of forbidden records through detailed error messages;
separate internal diagnostic codes from the user-visible policy.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee.

[LlamaIndex tools](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/tools/),
[LangChain Python tools](https://docs.langchain.com/oss/python/langchain/tools),
[LangChain JavaScript tools](https://docs.langchain.com/oss/javascript/langchain/tools),
[Writing effective tools](https://www.anthropic.com/research/writing-tools-for-agents),
[MCP tools, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/server/tools),
[OWASP prompt injection guidance](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html).
