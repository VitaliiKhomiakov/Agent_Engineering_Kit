# LlamaIndex

Apply only where LlamaIndex or LlamaIndex.TS is used, with the [core rules](core.md).
Select the actual language separately. The catalog makes [RAG](rag.md) and
[tool guidance](llm-tools.md) available; read only the topics the task needs.
Library adoption does not choose an agent loop or an additional framework.

## Read by task

| Task touches | Read |
| --- | --- |
| Loaders, document identity, updates or embeddings | [Corpus lifecycle](rag/ingestion.md) and integration rules below |
| Retrieval, postprocessing or response synthesis | [Retrieval](rag/retrieval.md) and integration rules below |
| Function/query-engine tool adapter | [Tool contracts](llm-tools/contracts.md) and integration rules below |
| Citation output or quality evaluation | [Answer checks](llm/answers.md) or [evaluation](llm/evaluation.md) |

## Integration

Select LlamaIndex when its loaders, indexing/retrieval or synthesis components
solve the actual data problem. Keep ingestion transformations and document identity
explicit; verify docstore/vector-store update behavior for the chosen integration.
Use retrieval and postprocessing independently when the application already owns
answer composition, avoiding an accidental additional LLM synthesis step.

Python `FunctionTool` wraps a function and `QueryEngineTool` exposes a query engine.
Treat their outputs according to whether they contain retrieved evidence or an
already synthesized answer; retain underlying provenance for final checks. A
`CitationQueryEngine` helps expose sources but does not certify every claim. Use workflow agents only when that agent loop is the selected owner.

For Node.js, use LlamaIndex.TS's actual package contracts and supported connectors.
Do not copy Python imports or assume feature parity. No equivalent Go package is
established by the cited documentation; Go can use native retrievers, a deliberately selected
service API or another framework without depending on LlamaIndex.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee.

[LlamaIndex ingestion pipeline](https://developers.llamaindex.ai/python/framework/module_guides/loading/ingestion_pipeline/),
[LlamaIndex querying](https://developers.llamaindex.ai/python/framework/understanding/rag/querying/),
[LlamaIndex tools](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/tools/),
[LlamaIndex agents](https://developers.llamaindex.ai/python/framework/understanding/agent/),
[CitationQueryEngine](https://developers.llamaindex.ai/python/examples/query_engine/citation_query_engine/),
[LlamaIndex.TS](https://developers.llamaindex.ai/typescript/framework/).
