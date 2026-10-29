# LangChainGo

Read only when the Go application uses `github.com/tmc/langchaingo`. Select the
`go` profile separately. This topic being available in `langchain` does not make
Go a dependency of Python/JavaScript instruction bundles.

## Actual Go contract

At **v0.1.15**, `tools.Tool` requires `Name() string`, `Description() string` and
`Call(context.Context, string) (string, error)`. It does not itself require or
validate a JSON Schema. Choose and document the argument encoding of your tool.
If it is JSON, parse once at the boundary, validate required values and limits,
and reject trailing data or unknown fields when the contract requires that.

The [Go fixture](examples/go-tool.md) implements this string interface directly.
Provider function-calling descriptions use the selected `llms`/provider adapter
contract; a `tools.Tool` implementation alone does not prove the provider sees a
structured schema or can call it. Inspect the actual agent/executor adapter before
connecting the two, and preserve tool-call IDs in the provider message format.

## Application integration

- Bind authenticated context and typed dependencies in a request-scoped adapter.
  Check access in the backend and constrain reads before fetching records.
  A model-supplied tenant or SQL string is not trusted scope.
- Pass `context.Context` to provider, database and HTTP clients. A cancellation
  check at entry cannot stop I/O that discards that context. Own client/stream
  lifetime and error mapping according to the selected adapter.
- Choose ordinary Go control flow or the specific supported chain/agent surface
  from the task. Python `create_agent`, `ToolRuntime`, JS middleware and LangGraph
  checkpoint semantics are not established by this module's name.
- Keep one owner for retries and tool execution. For writes or resume, apply the
  shared [execution rules](../llm-tools/execution.md); neither the tool interface
  nor a model loop supplies a durable effect ledger by itself.

## Compatibility evidence

[Module v0.1.15](https://github.com/tmc/langchaingo/tree/v0.1.15),
[tool interface](https://github.com/tmc/langchaingo/blob/v0.1.15/tools/tool.go),
[LLM tool definitions](https://github.com/tmc/langchaingo/blob/v0.1.15/llms/options.go),
[tool-call/result messages](https://github.com/tmc/langchaingo/blob/v0.1.15/llms/generatecontent.go).
The module declares Go **1.24.4**; the fixture was exercised on Go **1.26.1**.
Check provider support, module Go requirements and selected dependencies before
adoption. These pins are fixture evidence, not a mandate to upgrade an application.
