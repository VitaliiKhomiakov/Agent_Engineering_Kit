# LangGraph state and execution

Read for graph state, routing or concurrency. [Workflow policy](../llm-tools/workflows.md)
owns architectural choices; a short fixed sequence can remain ordinary code.
Python APIs below are examples of the inspected contract, not JavaScript aliases.

## State and updates

- Define minimal state fields, node inputs and returned updates. Keep evidence
  references, validated decisions and execution status structured. Put live clients,
  authenticated runtime dependencies and secrets outside persisted graph state.
- Python `TypedDict` describes types; it does not validate untrusted runtime data.
  Validate external input and model decisions at their boundaries. State schemas
  and reducers do not replace business constraints.
- Define a reducer only for fields that need merged updates. For a field without
  a reducer, multiple writes in the same super-step can raise an update error;
  do not assume a deterministic last writer. For merged lists, an empty update
  normally does not clear existing data. Use the selected version's supported
  replacement/reset mechanism when clearing is intended.
- Appending is not deduplication. Choose stable message/evidence IDs and explicit
  merge order where retries or parallel branches can produce duplicates. Python
  `add_messages` merges by message identity; it is not a generic evidence reducer.
- Return updates through the runtime contract instead of relying on in-place state
  mutations becoming checkpoints. Test conflicting updates or ordering only when
  the workflow actually uses parallel writers.

## Routing and persistence boundaries

Compile `StateGraph` before execution and check its routes with representative
valid, invalid and terminal decisions. Keep static edges and dynamic routing
deliberate: a dynamic destination does not implicitly remove other configured
outgoing paths. Bound loops by a business stop condition plus a runtime budget.

A checkpointer persists thread-scoped graph state. A store serves separately
defined data that may span threads; it does not automatically replace checkpoint
state or provide an authorization boundary. Select only the persistence needed by
the application. For restart recovery, use a durable backend with the application's
lifecycle/retention policy; in-memory fixtures are insufficient.

Bind each `thread_id` to its authenticated owner and conversation, job or workflow
instance. Recheck this mapping before reading state or resuming. Pass trusted
context again for the new request; possession of an ID is not authorization.
When changing nodes or state schemas, account for suspended runs and stored state
instead of assuming an old checkpoint can resume under any new graph definition.

## Contract references

[Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api),
[persistence](https://docs.langchain.com/oss/python/langgraph/persistence),
[checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers),
[JavaScript Graph API](https://docs.langchain.com/oss/javascript/langgraph/graph-api).
Follow [recovery and streaming](recovery-streaming.md) for interrupt/effect boundaries.
