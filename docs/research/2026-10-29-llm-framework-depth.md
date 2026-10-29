# Practical framework contracts and example evidence

Date: **2026-10-29**. This record supplements the earlier
[RAG/tool research](2026-10-29-rag-tools-engineering.md); it does not replace its
historical evidence. Progress and independent review belong to the
[expansion plan](../plans/2026-10-29-llm-framework-depth.md).

## Scope and method

Review official documentation and selected release source for the specific APIs
needed by the deeper Eino, LangChain/LangChainGo, LlamaIndex, LangGraph and Langfuse
topics. Common access/evidence/effect rules remain in the shared RAG/tool profiles.
Framework facts below are sourced; decisions about scope, complexity and required
application checks are local engineering policy.

Use small offline fixtures at real library boundaries. A source review is not an
executed integration. Local fixture success is not a production interoperability,
quality or durability guarantee. No provider/model calls, source uploads or live
Langfuse server were used. Dependencies were installed in disposable fixture
environments, without adding application dependencies to the library checkout.

## Contract findings and sources

| Area | Reviewed contract and resulting guidance |
| --- | --- |
| Eino composition | Distinguish component calls, sequential Chain, Graph routing, Workflow field/dependency mapping and ADK agent execution. Use only the surface needed by the task. [Chain/Graph guide](https://www.cloudwego.io/docs/eino/core_modules/chain_and_graph_orchestration/chain_graph_introduction/), [Workflow v0.9.22](https://github.com/cloudwego/eino/blob/v0.9.22/compose/workflow.go), [ADK guide](https://www.cloudwego.io/docs/eino/core_modules/eino_adk/agent_preview/). |
| Eino tools | Inferred schemas, JSON conversion and actual business validation are separate. Standard text and enhanced result interfaces differ. [Tool creation](https://www.cloudwego.io/docs/eino/core_modules/components/tools_node_guide/how_to_create_a_tool/), [v0.9.22 implementation](https://github.com/cloudwego/eino/blob/v0.9.22/components/tool/utils/invokable_func.go). |
| Eino streams/recovery | Invocation modes can adapt or aggregate streams; graph and ADK resume APIs are distinct. Their durable-store/effect behavior needs the actual selected integration. [Streaming guide](https://www.cloudwego.io/docs/eino/core_modules/chain_and_graph_orchestration/stream_programming_essentials/), [graph checkpoints](https://www.cloudwego.io/docs/eino/core_modules/chain_and_graph_orchestration/checkpoint_interrupt/), [graph resume source](https://github.com/cloudwego/eino/blob/v0.9.22/compose/resume.go), [ADK runner](https://github.com/cloudwego/eino/blob/v0.9.22/adk/runner.go). |
| LangChain | Tool schemas, context injection and structured-output strategies depend on language and API. Provider support is distinct from local schema validation. [Python tools](https://docs.langchain.com/oss/python/langchain/tools), [JS tools](https://docs.langchain.com/oss/javascript/langchain/tools), [Python structured output](https://docs.langchain.com/oss/python/langchain/structured-output), [JS structured output](https://docs.langchain.com/oss/javascript/langchain/structured-output). |
| LangChainGo | `tools.Tool` accepts/returns strings and does not itself require a schema. Provider tool definitions and call/result messages are separate surfaces. [Tool v0.1.15](https://github.com/tmc/langchaingo/blob/v0.1.15/tools/tool.go), [LLM options](https://github.com/tmc/langchaingo/blob/v0.1.15/llms/options.go), [message types](https://github.com/tmc/langchaingo/blob/v0.1.15/llms/generatecontent.go). |
| LlamaIndex ingestion | Preserve source/node identity; verify docstore/vector-store behavior. Absence-based deletion requires the complete authoritative set for the isolated store scope, not an incremental batch. [Ingestion guide](https://developers.llamaindex.ai/python/framework/module_guides/loading/ingestion_pipeline/), [document management example](https://developers.llamaindex.ai/python/examples/ingestion/document_management_pipeline/), [v0.14.25 pipeline source](https://github.com/run-llama/llama_index/blob/v0.14.25/llama-index-core/llama_index/core/ingestion/pipeline.py). |
| LlamaIndex outputs | Retriever evidence, synthesized query-engine responses and tool strings are different boundaries. Preserve source nodes through adapters; validate citations. [Querying](https://developers.llamaindex.ai/python/framework/understanding/rag/querying/), [tools](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/tools/), [citation engine](https://developers.llamaindex.ai/python/examples/query_engine/citation_query_engine/). |
| LangGraph state | Reducers define merges; types alone do not validate input. Checkpointers and cross-thread stores have distinct roles. [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api), [persistence](https://docs.langchain.com/oss/python/langgraph/persistence). |
| LangGraph recovery | A resumed interrupted node starts again. Approval/authentication and external-effect safety remain application responsibilities. Streaming modes and newer event-streaming APIs have version-specific shapes. [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts), [checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers), [streaming](https://docs.langchain.com/oss/python/langgraph/streaming). |
| Langfuse export | Match SDK/server and data model. Native Go OTel is a tracing route, not SDK feature parity; inspect supported transport/attributes and exporter lifecycle. [Compatibility](https://langfuse.com/docs/compatibility), [native OTel](https://langfuse.com/integrations/native/opentelemetry), [Go OTel](https://opentelemetry.io/docs/languages/go/). |
| Langfuse data | A masking hook covers specific fields/exporters; local experiment input can still leave the process. Prompt versions and experiment/evaluator versions need attribution. [Masking](https://langfuse.com/docs/observability/features/masking), [prompts](https://langfuse.com/docs/prompt-management/overview), [SDK experiments](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk), [OTel experiments](https://langfuse.com/integrations/native/opentelemetry/experiments). |

## Version boundaries observed

The Langfuse compatibility page on this date lists server v4, Python SDK v5 and
JS/TS SDK v6. The latter SDK majors require Cloud or self-hosted server v4.59.0+;
their runtime floors are Python 3.11+ and Node.js 22+. The page separately announces
the Cloud legacy cutover for **2026-11-16**. These are dated source observations,
not an SDK/server deployment tested here. Recheck the matrix when adopting;
permanent rules point to the actual deployment contract rather than freezing this
snapshot. [Compatibility source](https://langfuse.com/docs/compatibility).

The current LangGraph Python docs distinguish the v2 stream shape from the newer
v1.2 event-streaming API. The fixture intentionally uses `invoke` and its
`__interrupt__` result, which remains documented, rather than requiring streaming
for a pause/resume demonstration. [Interrupt API](https://docs.langchain.com/oss/python/langgraph/interrupts).

Go module metadata/source was inspected at Eino v0.9.22, LangChainGo v0.1.15 and
OTel SDK v1.47.0. LangChainGo declares Go 1.24.4; the OTel release declares Go
1.26.0. None of these fixture selections authorizes changing a consuming project's
supported runtime or dependencies. LlamaIndex Python and TypeScript, and LangChain
Python/JS/Go, are not treated as interchangeable APIs.

## Executed fixture evidence

Runtime: Linux amd64; Go **1.26.1**, Node.js **24.13.0**, npm **11.6.2**,
Python **3.12.3**, mypy **2.1.0**. Package installation used public registries.
Examples contain the executed code, minimal pinned manifests and reproduction
commands. Generated lockfiles/module sums and the resolved Python environment
were retained in the temporary evidence directory named in the plan.

| Fixture | Selected packages | Local checks and what they establish |
| --- | --- | --- |
| [Eino tool/graph](../../standards/eino/examples/tool-graph.md) | `github.com/cloudwego/eino v0.9.22` | `go test -race`: typed tool/schema construction, graph invocation, malformed/range/empty input, canceled context and backend denial |
| [LangChain JS tool](../../standards/langchain/examples/validated-tool.md) | `@langchain/core 1.3.1`, `zod 4.3.6` | `node --test`: successful/empty result, rejected schema/tenant argument and propagated backend denial |
| [LangChainGo adapter](../../standards/langchain/examples/go-tool.md) | `github.com/tmc/langchaingo v0.1.15` | `go test -race`: interface compatibility, JSON/field/trailing-data validation, bound scope, cancellation and backend denial |
| [LlamaIndex retrieval](../../standards/llamaindex/examples/retrieval.md) | `llama-index-core 0.14.25` | Three Python tests after review: preserve distinct chunks from one source, collapse an identical hit, handle no hits, reject missing provenance and empty node identity |
| [LangGraph resume](../../standards/langgraph/examples/resume.md) | `langgraph 1.2.18`, `langgraph-checkpoint 4.3.1`, `langchain-core 1.7.1` | One Python test: pause, approve/reject, node restart, invalid resume value, empty new in-memory saver |
| [Go OTel](../../standards/langfuse/examples/otel-go.md) | `go.opentelemetry.io/otel/sdk 1.47.0` and matching API modules | `go test -race`: local span parentage, permitted attribute set, completion and bounded flush/shutdown |

Both Python fixtures passed strict mypy with explicit/unimported `Any` forbidden;
the corrected retrieval fixture passed again with its regression test after the
independent review. All three Go fixtures passed `go vet`; the subsequent Go
repairs change only grouping/comments, with behavioral evidence retained.
Library artifact/bundle checks and the review outcome are recorded in the plan.
The fixture tests are
deliberately local: no model quality, live backend ACLs, vector synchronization,
durable crash recovery, Langfuse ingestion or provider schema support is claimed.
Source-reviewed features beyond these examples remain source-review evidence.
