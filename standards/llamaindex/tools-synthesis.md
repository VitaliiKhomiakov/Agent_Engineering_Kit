# LlamaIndex tools and answer synthesis

Read when exposing LlamaIndex functionality as a tool or producing answers.
Apply [tool contracts](../llm-tools/contracts.md) and [answer checks](../llm/answers.md)
without assuming that a framework wrapper establishes either contract.

## Choose the output boundary

| Surface | Output to account for |
| --- | --- |
| Retriever and node postprocessors | Evidence nodes/scores; the application can compose the answer |
| Query engine | May retrieve and synthesize an answer, depending on configuration/response mode |
| Python `FunctionTool` | A function exposed as a tool, with generated or supplied metadata/schema |
| Python `QueryEngineTool` | A query-engine result exposed as a tool; often already synthesized |

Before calling a query engine, make the synthesis model, response mode and budget
explicit. If the application already owns generation, use retrieval directly or
an intentionally selected no-synthesis configuration. Do not pay for a hidden
second generation step merely to recover text from a tool result.

At the tool boundary, keep model-facing content separate from underlying evidence.
For Python tool outputs, inspect `ToolOutput` and its raw result rather than
retaining only a string conversion. Query-engine response objects can carry
`source_nodes`; preserve those through adapters when required for attribution.
Do not assume every tool, streaming response or custom engine has the same shape.
Define the adapter contract and the no-source/empty/error behavior explicitly.

`FunctionTool` schema inference does not authorize an operation or validate every
business rule. Inject trusted dependencies using the selected API or an
application-owned wrapper. Keep sync/async behavior explicit so a blocking loader
or tool does not stall the application's event loop.

## Citations and orchestration

A `CitationQueryEngine` can organize source chunks for citation-oriented output.
Check that cited identifiers resolve to the actual evidence and support each
material claim; source-bearing output is not a factual correctness certificate.
Preserve provenance even if another model reformulates the query-engine answer.

Use LlamaIndex workflow agents only when that runtime is the chosen owner of the
agent loop. A loader, retriever or function tool does not require one. For TypeScript,
verify LlamaIndex.TS exports, lifecycle and connector support independently; Python
class names or examples are not evidence of TypeScript or Go API parity.

## Contract references

[Querying](https://developers.llamaindex.ai/python/framework/understanding/rag/querying/),
[tools](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/tools/),
[CitationQueryEngine](https://developers.llamaindex.ai/python/examples/query_engine/citation_query_engine/),
[LlamaIndex.TS](https://developers.llamaindex.ai/typescript/framework/).
These integration surfaces were source-reviewed; the retrieval fixture executes
neither model synthesis nor a citation engine.
