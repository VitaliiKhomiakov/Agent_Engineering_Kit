# LangGraph

Apply only where LangGraph stateful workflows are used, with the [core rules](core.md).
Use [tool/workflow guidance](llm-tools.md) for the relevant contracts. Select the
actual language separately; LangChain, RAG and Langfuse are separate choices.

## Read by task

| Task touches | Read |
| --- | --- |
| Graph choice, state, reducers or transitions | [State and execution](langgraph/state-execution.md), with [illustrative workflows](llm-tools/workflows.md) |
| Interrupts, replay, cancellation, streams or effects | [Recovery and streaming](langgraph/recovery-streaming.md), with [execution](llm-tools/execution.md) |
| Thread/source authorization across pauses | [Source access](llm-tools/source-access.md) |
| Answer delivery or behavior evaluation | [Answer checks](llm/answers.md) or [evaluation](llm/evaluation.md) |
| A small executable pause/resume boundary | [Resume fixture](langgraph/examples/resume.md) |

## State and recovery

Use a graph when explicit state, conditional routes, pause/resume or recovery are
material. The state and recovery topics above own reducer behavior, thread access,
checkpoint durability, interrupt replay and the external-effect boundary.

Use the appropriate Python or JavaScript API; neither establishes a Go runtime.
LangGraph can be selected without LangChain. Do not choose a graph solely to
draw a fixed sequence that ordinary code already expresses clearly.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee. The
resume fixture records its own package pin and in-process coverage.

[LangGraph workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents),
[LangGraph Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api),
[LangGraph checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers),
[LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts),
[LangGraph JavaScript overview](https://docs.langchain.com/oss/javascript/langgraph/overview).
