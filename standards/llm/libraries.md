# Library selection for RAG and tool applications

Select components against the [application contract](architecture.md), existing
stack and measured needs. This shortlist is optional, not an installation plan.
Language/host and vendor profiles remain independent choices; a library name does
not establish compatible APIs or authorize an upgrade.

## Framework selection across languages

| Responsibility | Python | Node.js / TypeScript | Go and other languages |
| --- | --- | --- | --- |
| Retrieval-centric application | LlamaIndex; Haystack as an alternative | LlamaIndex.TS or LangChain components | Native store/API clients; evaluate Eino or LangChainGo against required connectors |
| Model and tool integration | LangChain; Pydantic AI as a typed alternative | LangChain JavaScript; direct model SDKs | Eino, LangChainGo or direct model SDK/HTTP contracts |
| Stateful routing and pause/resume | LangGraph when justified | LangGraph JavaScript when justified | Eino or an application-owned state machine; validate actual persistence/replay support |
| Tracing and experiments | Langfuse Python SDK with compatible integrations | Langfuse JS/TS SDK with compatible integrations | OTel spans to Langfuse; use supported APIs for remaining platform features |
| Database/vector retrieval | Store/driver selected for the project | Same storage contract with a native client | Same storage contract with a native client |

Do not describe LangChainGo as API-compatible with current Python/JS LangChain or
as an automatic LangGraph replacement. The name is insufficient evidence of
feature parity. Likewise, a Python LlamaIndex recipe is not a Go package or a
TypeScript API specification. A separate service around a Python-only component
is an option when its benefit warrants deployment, authentication and operational
cost; it is not a prerequisite for Go/Node RAG. These are language-specific starting points, not a tested interoperability matrix.

## Supporting-library shortlist

The choices below are conditional recommendations. Preserve an existing working
component when it meets the same acceptance criteria; this list is not an install
manifest, procurement recommendation or comparative benchmark.

| Need | Candidate and selection criterion | Boundary to verify |
| --- | --- | --- |
| Vectors beside relational data | pgvector when PostgreSQL is already an appropriate owner | Filtered ANN recall, index/memory cost, row access, backup and rebuild |
| Dedicated vector/hybrid retrieval | Qdrant when its search capabilities or operational separation solve a requirement | Payload filters, tenant isolation, collection versioning and extra service operations |
| Lexical search | Existing search engine or PostgreSQL full-text search | Language analysis, identifiers and ranking; PostgreSQL full-text is not automatically BM25 |
| Document parsing/chunking | Docling when document structure materially affects retrieval | OCR/table/reading-order quality on actual files; parser/worker runtime and resource limits |
| Embedding/reranking | Sentence Transformers for supported local models; hosted APIs remain alternatives | Model language/domain quality, license, dimensions, tokenizer, latency and deployment hardware |
| Explicit Python pipelines | Haystack | Component and document-store compatibility for the selected major version |
| Typed Python agent/tool boundary | Pydantic AI | Runtime validation and actual model/provider behavior; not a replacement for database authorization |
| Go composition | Eino or LangChainGo | Required tools, streaming, cancellation, state persistence and supported provider integration at a selected revision |
| Offline quality evaluation | Ragas, or existing evaluation functions recorded in Langfuse | Metric inputs, human calibration, data export and grader cost; no universal pass score |
| Web discovery and extraction | Tavily or Exa if a hosted search service is permitted | Source coverage, raw evidence availability, quotas, confidential-query handling and provider terms |
| Cross-language observability | Native OTel plus Langfuse where selected | Attribute mapping, redaction, exporter lifecycle and trace propagation |

External Python evaluation/parsing workers can consume language-neutral fixtures
from a Go/Node service. This is a deliberate subsystem boundary, not permission to
introduce Python into every production service. Every selected executable/model
artifact still needs its own supported-version and licensing check.

## Go alternatives

Eino provides native Go model/tool/retriever components and agent/workflow building
blocks. LangChainGo supplies another Go composition option. Assess the
actual release's connectors, streaming, cancellation, persistence, interrupts and
replay before mapping the workflow onto it. Do not label either as a tested
drop-in LangGraph or LlamaIndex replacement. A native state machine with database
and HTTP clients is a valid baseline for Go and other languages.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee.

[LlamaIndex.TS](https://developers.llamaindex.ai/typescript/framework/),
[LangChain JavaScript tools](https://docs.langchain.com/oss/javascript/langchain/tools),
[LangGraph JavaScript overview](https://docs.langchain.com/oss/javascript/langgraph/overview),
[pgvector](https://github.com/pgvector/pgvector),
[Qdrant hybrid queries](https://qdrant.tech/documentation/search/hybrid-queries/),
[Sentence Transformers retrieve and rerank](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html),
[Docling chunking](https://docling-project.github.io/docling/concepts/chunking/),
[Ragas metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/),
[Haystack pipelines](https://docs.haystack.deepset.ai/docs/pipelines),
[Pydantic AI function tools](https://pydantic.dev/docs/ai/tools-toolsets/tools/),
[Tavily search API](https://docs.tavily.com/documentation/api-reference/endpoint/search),
[Exa search API](https://exa.ai/docs/reference/search),
[PostgreSQL full-text search](https://www.postgresql.org/docs/current/textsearch-intro.html),
[LangChainGo](https://github.com/tmc/langchaingo),
[Eino overview](https://www.cloudwego.io/docs/eino/overview/),
[Langfuse OpenTelemetry integration](https://langfuse.com/integrations/native/opentelemetry),
[OpenTelemetry Go](https://opentelemetry.io/docs/languages/go/).
