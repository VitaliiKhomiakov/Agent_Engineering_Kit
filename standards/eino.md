# Eino for Go

Apply only to actual Eino integrations, with the [Go rules](go.md) and relevant
[tool/workflow guidance](llm-tools.md). The `eino` profile makes both available.
It does not select a retrieval system, model provider or observability backend.
Select `rag` separately when the task includes corpus or retrieval work.

## Read by task

| Task touches | Read |
| --- | --- |
| Components, Chain, Graph, Workflow or ADK choice | [Composition](eino/composition.md) |
| Tool schema, trusted context, ToolsNode or retriever adapter | [Tools and retrieval](eino/tools-retrieval.md) |
| Streaming, cancellation, checkpoints or resume | [Runtime and recovery](eino/runtime-recovery.md) |
| A small executable Go integration | [Tool/graph fixture](eino/examples/tool-graph.md) |
| Framework choice or quality targets | [Library selection](llm/libraries.md) or [evaluation](llm/evaluation.md) |

## Integration

Use the smallest Eino surface that solves the task. A component or ordinary Go
function may be sufficient; a tool does not require a graph, ADK or multiple agents.
The application owns authorization, source scope, deadlines and external effects.
Keep these decisions outside model-visible arguments and preserve them through
the selected execution layer.

## Sources and compatibility

Official contracts reviewed on **2026-10-29**. The fixture pins Eino **v0.9.22**;
its local checks do not establish provider, ADK or durable-storage compatibility.
Use the consuming application's selected module versions, including separately
versioned `eino-ext` integrations. Consult migration notes before copying APIs
from a different release; this profile is not an upgrade instruction.

[Eino overview](https://www.cloudwego.io/docs/eino/overview/),
[Eino source at v0.9.22](https://github.com/cloudwego/eino/tree/v0.9.22).
