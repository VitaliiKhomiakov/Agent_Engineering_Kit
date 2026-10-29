# RAG and tool workflow engineering research

Date: **2026-10-29**. Scope: source-grounded recommendations for the
[RAG and tool instructions](../specs/2026-10-29-rag-tools-instructions.md).
Progress and check evidence belong to the
[canonical task](../plans/2026-10-29-rag-tools-research.md).

The user requires language-independent guidance, including Go, Python and Node.js.
Choose workflow complexity from the application's goals and constraints. The
question-to-answer sequence is illustrative; valid designs can be simpler or
more complex. Add agent-controlled routing or durable orchestration when the task
needs them. Select libraries by their responsibility and actual language support.
The four named projects are useful
options, not a mandatory combined stack.

## Evidence and version boundaries

Sources below were opened during this research. Technical recommendations use
project documentation, maintainer repositories, original engineering articles and
primary research. Search snippets and mirrors were discovery aids only.

This stage did not install libraries, call paid model/search APIs, run an example
application or benchmark retrieval. Documentation review establishes advertised
contracts, not measured quality, interoperability or production readiness.
Project-specific evaluation is still needed to select models, stores and budgets.

- Most framework links are moving documentation. Record the application's actual
  package versions, integration packages, model revisions and server versions
  before implementing examples; do not interpret this research date as a version pin.
- LlamaIndex's older `docs.llamaindex.ai` routes redirected to
  `developers.llamaindex.ai`. Python and TypeScript have separate documentation.
- The LangChain retrieval route redirected to its Deep Agents retrieval page;
  its RAG architecture discussion does not require installing Deep Agents.
  LangGraph's former durable-execution route redirected to persistence;
  current graph/checkpointer/interrupt pages provide the relevant replay details.
- Langfuse's compatibility page distinguishes server v3/v4, Python SDK v4/v5 and
  JS/TS SDK v5/v6. At review time it marks Python v5 and JS/TS v6 as requiring
  server v4 and lists a Cloud transition on 2026-11-16. Check the current matrix
  and selected deployment before adopting an SDK; old tutorial imports are not
  a compatibility guarantee. This is an observed vendor statement, not an upgrade
  request. F16 owns the detailed matrix.
- MCP tool semantics were reviewed against the dated **2026-07-28** specification.
  A deployed client/server may negotiate another supported version.
- Original engineering articles and the 2024 long-context study retain their
  model, corpus and publication limits. Their measured gains are not predictions
  for this user's application or current models.

## Source register

The IDs provide traceability for the synthesis and proposal. Each row names the
specific contract reviewed; they are not an unconditional reading list for agents.

### Named frameworks

| ID | Primary source | Contract used |
| --- | --- | --- |
| F01 | [LlamaIndex ingestion pipeline](https://developers.llamaindex.ai/python/framework/module_guides/loading/ingestion_pipeline/) | Transformations, caching and document identity/deduplication |
| F02 | [LlamaIndex querying](https://developers.llamaindex.ai/python/framework/understanding/rag/querying/) | Retrieval, node postprocessing and response synthesis |
| F03 | [LlamaIndex tools](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/tools/) | FunctionTool and QueryEngineTool boundaries |
| F04 | [LlamaIndex evaluation](https://developers.llamaindex.ai/python/framework/module_guides/evaluating/) | Retrieval and response metrics measure different failures |
| F05 | [LlamaIndex agents](https://developers.llamaindex.ai/python/framework/understanding/agent/) | FunctionAgent and workflow-based application composition |
| F06 | [CitationQueryEngine](https://developers.llamaindex.ai/python/examples/query_engine/citation_query_engine/) | Citation granularity and source-node inspection |
| F07 | [Retrieval architectures](https://docs.langchain.com/oss/python/deepagents/retrieval) | Two-step, agentic and hybrid RAG; existing stores can remain authoritative |
| F08 | [LangChain Python tools](https://docs.langchain.com/oss/python/langchain/tools) | Input schemas, descriptions and injected ToolRuntime |
| F09 | [LangChain structured output](https://docs.langchain.com/oss/python/langchain/structured-output) | Provider/tool strategies and validation |
| F10 | [LangChain SQL agent](https://docs.langchain.com/oss/python/langchain/sql-agent) | SQL workflow and narrow database permissions |
| F11 | [LangGraph workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents) | Fixed workflows versus model-selected execution |
| F12 | [LangGraph Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api) | Typed state, reducers, edges, replay and idempotency |
| F13 | [LangGraph checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers) | Thread-scoped checkpoints and recovery boundaries |
| F14 | [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) | Pause/resume, persistent state and repeated node execution |
| F15 | [Langfuse overview](https://langfuse.com/docs) | Tracing, prompts and evaluation responsibilities |
| F16 | [Langfuse compatibility](https://langfuse.com/docs/compatibility) | Server/SDK compatibility and migration limits |
| F17 | [Langfuse masking](https://langfuse.com/docs/observability/features/masking) | Redaction before export; coverage differs by hook/exporter |
| F18 | [Langfuse SDK experiments](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk) | Local/hosted datasets and item/run evaluation |
| F19 | [Langfuse with LangChain/LangGraph](https://langfuse.com/integrations/frameworks/langchain) | Callbacks and trace propagation |
| F20 | [Langfuse with LlamaIndex](https://langfuse.com/integrations/frameworks/llamaindex) | OpenInference instrumentation exporting OTel spans |
| F21 | [LlamaIndex.TS](https://developers.llamaindex.ai/typescript/framework/) | Separate JavaScript/TypeScript implementation |
| F22 | [LangChain JavaScript tools](https://docs.langchain.com/oss/javascript/langchain/tools) | Tool functions, runtime schemas and invocation context |
| F23 | [LangGraph JavaScript overview](https://docs.langchain.com/oss/javascript/langgraph/overview) | Stateful orchestration; LangChain is not required |

### Original engineering and research

| ID | Primary source | Contract or observation used |
| --- | --- | --- |
| E01 | [Building effective agents](https://www.anthropic.com/research/building-effective-agents) | Start with simpler workflows; add autonomy for a concrete benefit |
| E02 | [Writing effective tools](https://www.anthropic.com/research/writing-tools-for-agents) | Task-oriented tools, descriptions, bounded outputs and empirical evaluation |
| E03 | [Contextual retrieval](https://www.anthropic.com/research/contextual-retrieval) | Context-enriched chunks, lexical+dense retrieval and reranking as evaluated techniques |
| E04 | [Demystifying agent evaluations](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) | Outcome-based grading, multiple trials and different grader types |
| E05 | [Lost in the Middle](https://aclanthology.org/2024.tacl-1.9/) | In the studied models/tasks, evidence position affected long-context performance |

### Supporting libraries and services

| ID | Primary source | Relevant capability |
| --- | --- | --- |
| S01 | [pgvector](https://github.com/pgvector/pgvector) | Exact/approximate vector search; filtering can reduce ANN recall |
| S02 | [Qdrant hybrid queries](https://qdrant.tech/documentation/search/hybrid-queries/) | Multiple retrieval stages and rank fusion |
| S03 | [Sentence Transformers retrieve and rerank](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) | Candidate retrieval followed by cross-encoder scoring |
| S04 | [Docling chunking](https://docling-project.github.io/docling/concepts/chunking/) | Structure-aware, tokenizer-aware chunks and metadata |
| S05 | [Ragas metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/) | Retrieval, faithfulness and tool-use metric families |
| S06 | [Haystack pipelines](https://docs.haystack.deepset.ai/docs/pipelines) | Explicit component pipelines with branches and loops |
| S07 | [Pydantic AI function tools](https://pydantic.dev/docs/ai/tools-toolsets/tools/) | Typed functions, dependency context and generated schemas |
| S08 | [Tavily search API](https://docs.tavily.com/documentation/api-reference/endpoint/search) | Search results, source content and filtering controls |
| S09 | [Exa search API](https://exa.ai/docs/reference/search) | Search with optional content/highlights and source metadata |
| S10 | [PostgreSQL full-text search](https://www.postgresql.org/docs/current/textsearch-intro.html) | Lexical processing and indexed text search |
| S11 | [LangChainGo](https://github.com/tmc/langchaingo) | Separately maintained Go implementation; assess its own integrations |
| S12 | [Eino overview](https://www.cloudwego.io/docs/eino/overview/) | Go components, tool/retriever interfaces and agent/workflow composition |
| S13 | [Langfuse OpenTelemetry integration](https://langfuse.com/integrations/native/opentelemetry) | Native OTel export for languages beyond Python/JS |
| S14 | [OpenTelemetry Go](https://opentelemetry.io/docs/languages/go/) | Native Go tracing API/SDK and component status |

### Tool and retrieval trust boundaries

| ID | Primary source | Contract used |
| --- | --- | --- |
| T01 | [MCP tools, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) | Input/output schemas, results, errors and untrusted annotations |
| T02 | [MCP security guidance](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) | Token audience, confused deputies, SSRF and state-handle protection |
| T03 | [OWASP prompt injection guidance](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) | Indirect injection through retrieved content and layered controls |

## Recommended architecture

The following is AEK's proposed synthesis, not a mandatory vendor architecture.
Separate the offline ingestion lifecycle from the online answer lifecycle.
For an answer, use an application-owned route with explicit evidence and completion
conditions. An LLM can classify intent, formulate a search or draft prose; it must
not own authorization, retry budgets or whether an unverified answer is published.

Three reasonable implementation choices are:

| Choice | Appropriate when | Tradeoff |
| --- | --- | --- |
| Native SDK/HTTP clients and ordinary application code | Retrieval and answer flow are small and predictable | Few abstractions; the application owns validation, telemetry and recovery |
| Retrieval framework with a bounded workflow | Parsing/connectors/search composition are substantial | Reuses integration code; adds SDK/version contracts |
| Durable graph with selected retrieval adapters | Clarification, branching, resumable work or multiple source families are material | Explicit state/recovery; more operational complexity and replay tests |

The user's sequence illustrates a possible flow, not a required architecture.
A direct lookup or retrieval-and-answer path can meet a narrow goal; cross-source
research may need decomposition, parallel retrieval, iterative refinement or human
review. Select the stages, ordering and execution model from those requirements.
Use a durable graph when state, pauses or recovery justify it. A graph can call
LlamaIndex or ordinary retrievers without embedding another autonomous agent loop.
Choose one owner for
top-level routing, state, retries and the generation step. Combining LangChain,
LangGraph and LlamaIndex is justified only by specific non-overlapping needs.
F01–F14 and E01 inform this choice.

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
cost; it is not a prerequisite for Go/Node RAG. F21–F23 and S11–S14 establish the
language-specific starting points, not a tested interoperability matrix.

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

## Recommendations to carry into instructions

**Retrieval and indexing.** Keep stable source identity, version and access scope
through extraction, chunks and citations. Make updates/deletions and access
revocations visible at query time. Tune chunking and candidate limits against
actual documents and queries. Compare lexical, dense and hybrid retrieval; add
reranking only if it improves the relevant quality/latency tradeoff. Contextual
enrichment is optional and must remain distinguishable from original evidence.
F01–F02, E03 and S01–S04 support these techniques; exact policy and budgets are AEK choices.

**Tool ergonomics.** Tools should express useful operations with clear input and
result contracts. Descriptions state when to use them, what they return and what
they cannot do. Return bounded evidence with stable IDs and source locators; avoid
dumping whole stores into context. A workflow node can call a tool directly;
classifying intent or verifying an answer need not be exposed as model-selectable
tools. E02, F03, F08–F09, F22 and T01 inform this separation.

**Source routing.** Live structured facts should come from their authoritative
database/API, not a stale embedding of those facts. Documents answer contextual
questions; current external facts may require permitted web search. An empty
private search is not permission to send the private question to a public provider.
Use explicit routes and a supported insufficient-evidence outcome. F07, F10,
S08–S10 and the existing AEK trust boundary inform this policy.

**Verification.** Separate valid schemas, valid citations and actual claim support.
A source link may exist while not supporting a claim. Retrieval quality, answer
quality and tool-action correctness require different evidence. Model-based graders
are fallible and should be calibrated against human-labelled cases; exact data,
permissions and arithmetic should use deterministic checks where feasible.
F04, F06, F18, E04 and S05 support separate evaluation layers.

**Recovery and delivery.** A saved checkpoint does not make remote side effects
exactly-once. External writes and message delivery need idempotency and an explicit
uncertain-result state. Resume only the correct authorized conversation/action.
If the product promises verification before delivery, stream progress while holding
the answer until its gate passes; an already emitted token cannot be retracted by
a later checker. F12–F14 establish replay behavior; the publication contract is
the proposed AEK policy.

**Telemetry.** Record stage spans, source/version identifiers, tool outcomes,
latency, token/cost usage and final answer status. Do not log credentials or collect
full private reasoning. Minimize corpus/question data and redact across every
export path, including third-party instrumentation. A successful trace is not a
correctness certificate. F15–F20 and S13–S14 inform this design.

## Disagreements and limits worth preserving

- More agents, bigger context and more retrieved chunks are not inherently better.
  E05 demonstrates a position effect for its tested models; measure current models
  rather than converting that paper into a universal context-size prohibition.
- E03 reports improvements for a particular contextual-retrieval experiment.
  Do not copy its percentages, candidate counts or chunk lengths as project targets.
- Framework examples often use in-memory stores, permissive SQL tools and minimal
  schemas to teach an API. They do not establish durability, authorization or
  correctness for production data. Apply the application's actual contracts.
- Similarity/reranker scores are not interchangeable probabilities of answer
  correctness. Calibrate route thresholds on labelled queries; preserve score type.
- Tool schema validation does not prove permission or trustworthy output. MCP
  annotations and retrieved instructions cannot grant capabilities (T01–T03).
- Langfuse local-dataset experiments still send experiment data to the configured
  server (F18). Local execution is not evidence of local-only data handling.
- A masking hook may cover one exporter or attribute path while another exporter
  retains raw data (F17). Check the selected SDK's coverage, including media paths.
- Documentation review did not establish which stack is fastest, cheapest or best
  for this user's data. The proposal deliberately leaves those choices conditional.

## Next application boundary

The accompanying instruction proposal is usable for design/review and supplies
concrete tool contracts and workflow exits. Its suggested catalog decomposition
keeps `rag`, `llm-tools` and framework adapters independent of language selection.
Activating profiles should preserve the existing catalog schema, conditional
reading routes, language standards and artifact-checking contracts. The present
research does not alter any downstream project or select its provider/model.

Implementation note, **2026-10-29**: the user authorized promoting the proposal
into library profiles. The [design and ownership map](../specs/2026-10-29-rag-tools-instructions.md)
now points to the operational rules; the [canonical task](../plans/2026-10-29-rag-tools-research.md)
records integration checks separately from this earlier documentation research.
