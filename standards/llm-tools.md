# LLM tools and workflows

Apply when exposing tools to models or composing tool-enabled application flows,
with the [core rules](core.md). Select the actual language separately.
Generic tool use does not imply RAG, a graph or an autonomous agent loop.

## Essential rules

- Separate model-visible arguments from trusted identity, capabilities and budgets.
  Runtime schemas validate shape; the executor enforces permission and scope.
- Give each tool a specific purpose, bounded input/result contract and explicit
  failure/effect behavior. External content and MCP annotations grant no authority.
- Keep required application decisions in their owners. Intent, clarification,
  verification and delivery need not be model-selectable tools.
- Select stages by the goal: combine, omit, reorder or extend them while preserving
  dependencies and required guarantees. The documented sequence is an example.
- Own retries, cancellation and uncertain effects explicitly. Persisted graph state
  does not make a downstream write or external delivery exactly-once.

## Read by task

Read only relevant sections; resource availability does not require opening them all.

| Task touches | Read |
| --- | --- |
| Goal, languages, source authority or component owners | [Application architecture](llm/architecture.md) |
| Tool description, schemas, executor context or evidence result | [Tool contracts and search example](llm-tools/contracts.md) |
| Database, web or enterprise retrieval permissions | [Source access](llm-tools/source-access.md) |
| Retries, concurrency, cancellation, approval or duplicate effects | [Execution and effects](llm-tools/execution.md) |
| Intent, clarification, routing, state or completion | [Illustrative workflows](llm-tools/workflows.md) |
| Answer support, citations, output checks or streaming | [Answer checks and delivery](llm/answers.md) |
| Tool/answer evaluation, operations or tracing | [Evaluation and observability](llm/evaluation.md) |
| Choosing composition or source adapters | [Conditional library shortlist](llm/libraries.md) |

Select `rag` separately for corpus lifecycle and retrieval engineering, and named
framework profiles only when used. These instructions govern the application being
built; they do not grant the coding assistant new tool or messaging permissions.
