# Eino tools and retrieval adapters

Read when exposing an operation through Eino or connecting a retriever. The
[tool contract](../llm-tools/contracts.md) owns input/output policy;
[source access](../llm-tools/source-access.md) owns authorization and query scope.

## Tool definition and invocation

- In the standard text interface, `BaseTool.Info(ctx)` exposes `schema.ToolInfo`;
  `InvokableTool.InvokableRun` consumes a JSON argument string and returns a string.
  `utils.InferTool` derives the schema from a typed Go input, decodes arguments and
  serializes the typed result. Check schema construction and invocation errors.
- Use JSON field names and descriptions meaningful to the model. In the inspected
  version, `jsonschema_description` avoids comma parsing problems in descriptions
  embedded in the `jsonschema` tag. Inspect the generated schema for the selected
  provider's supported JSON Schema subset.
- Schema generation and JSON decoding do not enforce the complete tool contract.
  Validate required values, ranges, lengths and domain rules before I/O. Do not
  assume inferred constraints reject invalid arguments at invocation time. If
  rejecting unknown fields is part of the contract, enforce it in the decoder or
  boundary validator and test it explicitly.
- Inject authenticated dependencies through request-scoped construction or the
  chosen runtime's context/options. Never let model arguments select a principal,
  credential or unrestricted tenant. The backend still authorizes each operation.
- When using `ToolsNode` or ADK tool execution, preserve tool-call/result pairing.
  Set concurrency and retry behavior for the actual tools: independent reads can
  differ from writes or order-dependent actions. Map failures deliberately instead
  of presenting a failed operation as successful empty evidence.

Enhanced and streaming tool interfaces have different argument/result contracts;
v0.9.22 includes `schema.ToolArgument`/`schema.ToolResult` variants. Choose one
supported by the actual executor and model integration. Do not substitute a
multimodal result into the standard string interface by assumption.

## Retrieval boundary

An Eino retriever returns `[]*schema.Document` from `Retrieve(ctx, query, ...)`.
Map its IDs/content/metadata to the application's evidence contract. Preserve
document identity, chunk/record identity, revision, location and access scope;
do not discard separate relevant chunks just because their document ID matches.

Select `rag` and its ingestion/retrieval topics for corpus work. Eino's component
interface does not establish ACL filtering, freshness, score comparability or
embedding compatibility for an `eino-ext` backend. Check those capabilities at
the selected adapter and storage boundary. Retrieval is usable without an agent
loop; an answer tool must distinguish retrieved evidence from synthesized text.

## Contract references

[Creating tools](https://www.cloudwego.io/docs/eino/core_modules/components/tools_node_guide/how_to_create_a_tool/),
[tool utilities, v0.9.22](https://github.com/cloudwego/eino/blob/v0.9.22/components/tool/utils/invokable_func.go),
[retriever interface, v0.9.22](https://github.com/cloudwego/eino/blob/v0.9.22/components/retriever/interface.go).
The [offline fixture](examples/tool-graph.md) exercises decoding, explicit validation,
context cancellation and a backend denial; it does not test a model's tool choice.
