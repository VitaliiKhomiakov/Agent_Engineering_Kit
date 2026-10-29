# LangGraph

Apply only where LangGraph stateful workflows are used, with the [core rules](core.md).
Use [tool/workflow guidance](llm-tools.md) for the relevant contracts. Select the
actual language separately; LangChain, RAG and Langfuse are separate choices.

## Read by task

| Task touches | Read |
| --- | --- |
| Graph choice, state or transitions | Integration rules below and [illustrative workflows](llm-tools/workflows.md) |
| Interrupts, replay, cancellation or downstream effects | Integration rules below and [execution](llm-tools/execution.md) |
| Thread/source authorization across pauses | [Source access](llm-tools/source-access.md) |
| Answer delivery or behavior evaluation | [Answer checks](llm/answers.md) or [evaluation](llm/evaluation.md) |

## State and recovery

Use a graph when explicit state, conditional routes, pause/resume or recovery are
material. Define state and reducers for parallel updates deliberately; avoid
concurrent writes that overwrite evidence or append duplicate messages on retries.
Keep evidence references and decisions structured instead of storing only a giant
prompt/transcript.

Use persistent checkpoint storage for recovery across process restarts. Bind each
thread to its authenticated owner and the relevant conversation, job or workflow
instance. A thread ID is a lookup key, not authorization. Revalidate permission and
approval when resuming.
An interrupted node can rerun from its start; isolate effects and make replay safe.
Do not catch an interrupt as a generic tool failure or duplicate a completed
external effect merely to reconstruct state. Test the exact runtime's resume behavior.

Use the appropriate Python or JavaScript API; neither establishes a Go runtime.
LangGraph can be selected without LangChain. Do not choose a graph solely to
draw a fixed sequence that ordinary code already expresses clearly.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee.

[LangGraph workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents),
[LangGraph Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api),
[LangGraph checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers),
[LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts),
[LangGraph JavaScript overview](https://docs.langchain.com/oss/javascript/langgraph/overview).
