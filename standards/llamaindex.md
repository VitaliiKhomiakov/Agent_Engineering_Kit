# LlamaIndex

Apply only where LlamaIndex or LlamaIndex.TS is used, with the [core rules](core.md).
Select the actual language separately. The catalog makes [RAG](rag.md) and
[tool guidance](llm-tools.md) available; read only the topics the task needs.
Library adoption does not choose an agent loop or an additional framework.

## Read by task

| Task touches | Read |
| --- | --- |
| Loaders, identity, updates, embeddings or retrieval output | [Ingestion and retrieval](llamaindex/ingestion-retrieval.md), with affected [corpus](rag/ingestion.md)/[retrieval](rag/retrieval.md) rules |
| Synthesis, citations or function/query-engine tools | [Tools and synthesis](llamaindex/tools-synthesis.md) |
| Citation output or quality evaluation | [Answer checks](llm/answers.md) or [evaluation](llm/evaluation.md) |
| A small executable retrieval boundary | [Retrieval-only fixture](llamaindex/examples/retrieval.md) |

## Integration

Select LlamaIndex when its loaders, indexing/retrieval or synthesis components
solve the actual data problem. The topics above distinguish source identity and
store updates, retrieval-only output, model synthesis and tool/citation adapters.
Use workflow agents only when that agent loop is the selected owner.

For Node.js, use LlamaIndex.TS's actual package contracts and supported connectors.
Do not copy Python imports or assume feature parity. No equivalent Go package is
established by the cited documentation; Go can use native retrievers, a deliberately selected
service API or another framework without depending on LlamaIndex.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee. The
retrieval fixture records its own package pin and limited executed coverage.

[LlamaIndex ingestion pipeline](https://developers.llamaindex.ai/python/framework/module_guides/loading/ingestion_pipeline/),
[LlamaIndex querying](https://developers.llamaindex.ai/python/framework/understanding/rag/querying/),
[LlamaIndex tools](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/tools/),
[LlamaIndex agents](https://developers.llamaindex.ai/python/framework/understanding/agent/),
[CitationQueryEngine](https://developers.llamaindex.ai/python/examples/query_engine/citation_query_engine/),
[LlamaIndex.TS](https://developers.llamaindex.ai/typescript/framework/).
