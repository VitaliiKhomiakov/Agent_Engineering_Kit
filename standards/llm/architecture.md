# LLM application architecture

Apply to the selected RAG or tool-enabled application with the [core rules](../core.md).
Application tools and workflows are distinct from the coding assistant's own
permissions. Language profiles remain separate selections from the catalog.

## Establish the project contract

Reuse the project passport and actual implementation. Record the supported languages
and runtime versions, selected libraries/integrations, model and embedding revisions,
storage, source owners, access model, latency/cost constraints and expected output.
Identify whether the application needs document Q&A, current record lookup,
cross-source research or actions with side effects; these are different contracts.

Define which source is authoritative for each fact type, the acceptable freshness,
how citations reach the user, and the supported insufficient-evidence response.
Keep event time, publication time, effective period and retrieval time distinct.
Define corpus languages, important query categories and measurable acceptance
criteria before selecting chunk sizes, retrieval limits or a framework.

Use a direct lookup, retrieval/generation path or ordinary tool call when sufficient. Add query
planning, dynamic tools, a graph or multiple agents only for a demonstrated need.
Do not require an LLM call for a step that ordinary validation or routing can settle.
Do not select every available library, database or observability service by default.

## Responsibilities and boundaries

| Owner | Responsibility | Boundary |
| --- | --- | --- |
| Request transport | Receive input, authenticate, stream permitted events | No retrieval policy or business decisions in a thin HTTP handler |
| Application workflow | Intent, transitions, deadlines, clarification and completion | One owner of state and overall retry/tool budget |
| Tool registry and executor | Expose applicable operations, validate inputs, enforce capabilities, dispatch calls | Model-proposed arguments cannot establish identity or authority |
| Source adapters | Query stores/APIs, parse provider results, enforce scoped access | Return explicit evidence and errors rather than provider SDK objects |
| Ingestion service/job | Parse, version, index, update and retire source material | Separate from ordinary answer requests |
| Retrieval/context assembly | Rank, deduplicate and select usable evidence | Preserve original provenance and access boundaries |
| Answer composer | Produce a draft from the question and selected evidence | Cannot invent missing sources or certify its own result |
| Verification and delivery | Check evidence/output contract; publish the permitted result | A successful model call is not permission to skip the gate |

Use only responsibilities needed by the actual features. These are boundaries,
not mandatory microservices, classes or one-file-per-step rules. A small application can implement them with cohesive
functions. Avoid nested agent loops or several libraries independently owning
retries, conversation history or final answer generation.

## Language-neutral implementation contract

| Concern | Go | Python | Node.js / TypeScript |
| --- | --- | --- | --- |
| Request/result contracts | Named structs and explicit validation | Named typed models with runtime validation at boundaries | Named types plus runtime schemas; TypeScript alone does not validate JSON |
| Dependency/context injection | Application-owned services and `context.Context` | Explicit dependencies and request context | Explicit dependencies and invocation context |
| Cancellation | Propagate context deadlines through providers/drivers | Propagate async cancellation and timeouts; isolate blocking I/O | Propagate AbortSignal where supported; bound promises and blocking work |
| Concurrency | Bounded goroutines with owned lifetime | Bounded async tasks/workers | Bounded async work/queues; worker/process boundary for heavy CPU work |
| Recovery | Persisted application state or selected Go framework | Application state or compatible workflow runtime | Application state or compatible workflow runtime |

Use the selected existing language profile for naming, ownership and resource
lifetime. Keep JSON/HTTP/protocol contracts versioned when components use different
languages. Do not emulate Python APIs through untyped maps or add a remote service
solely to imitate a tutorial.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee.

[Retrieval architectures](https://docs.langchain.com/oss/python/deepagents/retrieval),
[LangGraph workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents),
[Building effective agents](https://www.anthropic.com/research/building-effective-agents).
