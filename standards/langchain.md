# LangChain

Apply only where LangChain model/tool integrations are used, with the
[core rules](core.md) and task-relevant [tool guidance](llm-tools.md).
Select the language/host separately. This profile does not require LangGraph,
Langfuse, LlamaIndex or a retrieval system.

## Read by task

| Task touches | Read |
| --- | --- |
| Tool schemas, injected context or results | [Tool contracts](llm-tools/contracts.md) and integration rules below |
| Database/web/enterprise tools | [Source access](llm-tools/source-access.md) |
| Tool errors, retry limits or effects | [Execution](llm-tools/execution.md) |
| Structured routing or answer output | [Workflow transitions](llm-tools/workflows.md) or [answer checks](llm/answers.md) |
| Quality or framework selection | [Evaluation](llm/evaluation.md) or [language/library choices](llm/libraries.md) |

## Integration

Use its model/tool/retrieval integrations when they reduce concrete adapter work.
Python tool schemas and ToolRuntime, and JavaScript tool schemas/context, have
separate APIs. Inject authenticated context outside model-visible arguments; hidden
context still requires authorization checks in the operation.

Use structured output for routing and answer contracts with the selected model's
supported strategy. Handle schema failures, tool errors, refusals and incomplete
outputs explicitly. Schema validation is not factual verification.
Keep tool result IDs paired with their calls. Avoid mixing old chain/agent examples
with a different installed major version. LangChainGo follows its own repository
contracts; select it by required functionality, not by assumed Python/JS parity.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee.

[LangChain Python tools](https://docs.langchain.com/oss/python/langchain/tools),
[LangChain structured output](https://docs.langchain.com/oss/python/langchain/structured-output),
[LangChain SQL agent](https://docs.langchain.com/oss/python/langchain/sql-agent),
[LangChain JavaScript tools](https://docs.langchain.com/oss/javascript/langchain/tools),
[LangChainGo](https://github.com/tmc/langchaingo).
