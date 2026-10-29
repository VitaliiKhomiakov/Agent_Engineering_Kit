# LangChain models and tools

Read for Python/JavaScript LangChain integration. LangChainGo has its own
[Go contract](go.md). The [shared tool rules](../llm-tools/contracts.md) own
authorization, input/output meaning and public failure categories.

## Define the boundary

- Use the selected version's tool constructor and a runtime schema: for example,
  Python `@tool` with supported type/Pydantic schemas, or JavaScript `tool` with
  Zod. Type annotations alone do not establish domain validity or authorization.
  Validate constraints that the chosen provider's schema subset cannot express.
- Expose only model-selectable arguments. Python `ToolRuntime` injection and
  JavaScript invocation context have different APIs. Authenticate before building
  that context and authorize inside the operation. A per-request closure is also
  sufficient when the application directly owns invocation; do not mutate a
  process-wide tool to switch tenants between requests.
- Keep a model's tool request separate from execution. In an application-owned
  loop, dispatch only allowed names, validate complete arguments and correlate
  every result with its original call ID. In a framework-owned agent, use its
  supported executor and error hooks rather than running the same call twice.
- Accumulate streamed tool-call fragments using the selected provider/message
  API before validation and execution. A partial JSON fragment is not an action.
  Pass cancellation to actual I/O; classify denied access, invalid arguments,
  empty results and transient failures using the shared execution policy.
- For tools with both model-facing content and an application artifact, keep the
  evidence artifact available for answer checks. Do not expose raw internal
  records merely because the model-facing result is a string.

## Structured output

Choose the selected model's supported provider-native or tool-based strategy.
Python agent APIs expose `ProviderStrategy`/`ToolStrategy` through
`response_format`; direct model structured-output methods and JavaScript agent
APIs are separate contracts. Check whether the provider supports tools and the
chosen output strategy together. Do not copy Python option names into JS or Go.

Validate the returned structure and handle refusal, truncation, invalid data and
bounded repair explicitly. Do not execute a routing decision until it is valid.
A schema-valid answer can still lack supporting evidence; apply the shared
[answer checks](../llm/answers.md). Provider repair/retry behavior counts toward
the application's budget.

## Verification and references

The [JavaScript tool fixture](examples/validated-tool.md) uses `@langchain/core`
without an agent or model. It checks argument rejection, trusted scope and backend
failure propagation, not provider JSON Schema support or tool selection quality.
Test those separately only when the integration depends on them.

[Python tools](https://docs.langchain.com/oss/python/langchain/tools),
[JavaScript tools](https://docs.langchain.com/oss/javascript/langchain/tools),
[Python structured output](https://docs.langchain.com/oss/python/langchain/structured-output),
[JavaScript structured output](https://docs.langchain.com/oss/javascript/langchain/structured-output).
Use the installed language/package versions; do not mix old chain/agent tutorials
with a different major API.
