# RAG and tool workflow instruction design

Date: **2026-10-29**. Status: **implemented in catalog profiles**.
Evidence: [dated research and source register](../research/2026-10-29-rag-tools-engineering.md).
Progress and check results: [canonical task](../plans/2026-10-29-rag-tools-research.md).

The user authorized integrating the researched instructions into AEK. The rules
now live in the owners below; this document records design and ownership instead
of maintaining a second operational copy. Source review and runtime validation
retain their separate limits.

## Accepted design constraints

- Write the policies in English; support Go, Python, Node.js and other stacks
  without requiring a language, storage engine or combined framework stack.
- Treat the described intent → clarification → retrieval → answer → verification
  → delivery sequence as an example. A direct lookup, ordinary retrieval-and-answer
  path or more complex iterative workflow is valid when it meets the actual goal.
  Preserve data dependencies and required access, evidence and delivery guarantees.
- Keep application-owned decisions separate from model-visible tool calls.
  Schemas do not establish authorization or factual correctness.
- Give each rule one owner, with short task-based entry routes. Keep examples,
  library choices, source research and framework-specific details conditional.
- Preserve core, verification and work-mode ownership. Application tool guidance
  grants no new permissions to the coding assistant.
- Use catalog schema 1. Profiles are optional; dependencies make rules available
  without requiring their recursive reading or installing application packages.

## Implemented ownership

| Profile or concern | Policy owner |
| --- | --- |
| Retrieval-augmented generation entry | [RAG](../../standards/rag.md) |
| Model tool and application workflow entry | [LLM tools](../../standards/llm-tools.md) |
| Goal, source authority, language contract and responsibilities | [Application architecture](../../standards/llm/architecture.md) |
| Conditional frameworks, libraries and Go alternatives | [Library selection](../../standards/llm/libraries.md) |
| Parsing, chunking, embeddings, updates and deletion | [Corpus lifecycle](../../standards/rag/ingestion.md) |
| Lookup/search, filters, fusion, reranking and context | [Retrieval](../../standards/rag/retrieval.md) |
| Tool definitions, search schema and evidence envelope | [Tool contracts](../../standards/llm-tools/contracts.md) |
| Database/web/enterprise access and confidentiality | [Source access](../../standards/llm-tools/source-access.md) |
| Budgets, retries, cancellation, approval and uncertain effects | [Execution](../../standards/llm-tools/execution.md) |
| Flexible stages, route decisions and completion | [Illustrative workflows](../../standards/llm-tools/workflows.md) |
| Claim support, citations, streaming and answer delivery | [Answer checks](../../standards/llm/answers.md) |
| Online/offline distinction, metrics, telemetry and acceptance cases | [Evaluation](../../standards/llm/evaluation.md) |
| LlamaIndex and LlamaIndex.TS integration | [LlamaIndex](../../standards/llamaindex.md) |
| LangChain language/version contracts | [LangChain](../../standards/langchain.md) |
| Graph state, reducers, checkpoints and interrupts | [LangGraph](../../standards/langgraph.md) |
| SDK/server compatibility, OTel, privacy and experiments | [Langfuse](../../standards/langfuse.md) |

Shared `standards/llm/` files are resources of the profiles that need them, not an
extra mandatory profile. The catalog's dependencies preserve common availability:
`rag` and `llm-tools` use `core`; `llamaindex` uses both; `langchain` and
`langgraph` use `llm-tools`; `langfuse` uses `core` and shared evaluation only.
Languages, hosts, storage and sibling vendor frameworks remain separate selections.

## Integration acceptance

The catalog must expose the six entries and all their required resources.
Prepared Go, Python and Node.js bundles must keep the selected guidance reachable
without implicitly selecting unrelated languages or frameworks. Generic tools
remain usable without RAG; tracing remains usable without a graph or retrieval.
Native entry templates reuse their existing selected-profile route expansion.

Check artifact links/schema, profile closure, the illustrative JSON contract and
new-file whitespace. Review the scoped changes against the original proposal,
including source authority, freshness, access revocation, citation support,
cancellation, uncertain outcomes and bounded completion. Application execution,
SDK interoperability, retrieval quality and model behavior require separate
project-specific evidence and are not claimed by library artifact checks.
