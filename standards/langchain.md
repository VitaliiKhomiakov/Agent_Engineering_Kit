# LangChain

Apply only where LangChain model/tool integrations are used, with the
[core rules](core.md) and task-relevant [tool guidance](llm-tools.md).
Select the language/host separately. This profile does not require LangGraph,
Langfuse, LlamaIndex or a retrieval system.

## Read by task

| Task touches | Read |
| --- | --- |
| Python/JS tools, context, streamed calls or structured output | [Models and tools](langchain/models-tools.md), with [tool contracts](llm-tools/contracts.md) |
| LangChainGo adapter, model/tool integration or runtime | [Go-specific guidance](langchain/go.md) |
| Database/web/enterprise tools | [Source access](llm-tools/source-access.md) |
| Tool errors, retry limits or effects | [Execution](llm-tools/execution.md) |
| Structured routing or answer output | [Workflow transitions](llm-tools/workflows.md) or [answer checks](llm/answers.md) |
| Quality or framework selection | [Evaluation](llm/evaluation.md) or [language/library choices](llm/libraries.md) |
| A small executable tool boundary | [JavaScript fixture](langchain/examples/validated-tool.md) or [Go fixture](langchain/examples/go-tool.md), only for that language |

## Integration

Use its model/tool/retrieval integrations when they reduce concrete adapter work.
Read the relevant language topic above for runtime schemas, trusted context,
execution ownership and result pairing. LangChainGo follows a separate module
contract; Python/JavaScript examples do not establish its APIs. A tool integration
does not require a model-directed agent loop.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee. Each
executable fixture records its own pins and the boundaries it actually checks.

[LangChain Python tools](https://docs.langchain.com/oss/python/langchain/tools),
[LangChain structured output](https://docs.langchain.com/oss/python/langchain/structured-output),
[LangChain SQL agent](https://docs.langchain.com/oss/python/langchain/sql-agent),
[LangChain JavaScript tools](https://docs.langchain.com/oss/javascript/langchain/tools),
[LangChainGo](https://github.com/tmc/langchaingo).
