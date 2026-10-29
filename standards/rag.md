# Retrieval-augmented generation

Apply to systems that use retrieved documents or records to support answers, with
the [core rules](core.md). This profile is language-neutral: select the actual
Go, Python, JavaScript/TypeScript or other language rules separately.
RAG does not require a vector store, agent, graph or any named framework.

## Essential rules

- Establish source authority, freshness, permitted access and answer acceptance
  before choosing retrieval components or tuning their settings.
- Preserve document/record identity, versions, locators and access scope from
  ingestion through context assembly, answer checks and citations.
- Choose lookup, lexical, semantic or hybrid retrieval for the actual question.
  Evaluate evidence coverage; a full top-k result is not proof of sufficiency.
- Keep source content untrusted and authorization application-owned. A plausible
  citation or fluent answer does not establish factual support.
- Select workflow complexity from goals. A direct lookup, retrieval-and-answer
  path or iterative investigation may be appropriate; no fixed sequence applies.

## Read by task

Read only relevant sections; resource availability is not a reading queue.

| Task touches | Read |
| --- | --- |
| Goal, sources, language/runtime or responsibility placement | [Application architecture](llm/architecture.md) |
| Parsing, chunking, embeddings, updates, deletion or index migration | [Corpus lifecycle](rag/ingestion.md) |
| Lookup/search, access filters, ranking, context or evidence sufficiency | [Retrieval and context](rag/retrieval.md) |
| Supported claims, citations, conflicts, streaming or final answer | [Answer checks and delivery](llm/answers.md) |
| Quality datasets, metrics, acceptance cases or telemetry | [Evaluation and observability](llm/evaluation.md) |
| Selecting adapters, stores, parsers, rerankers or frameworks | [Conditional library shortlist](llm/libraries.md) |

Select `llm-tools` separately for tool definitions and workflow execution, and
vendor profiles only when their integrations are used. Examples and library
choices do not select a stack. Source dates and limits remain with each topic.
