# Eino composition

Read for an Eino composition decision. [Shared architecture](../llm/architecture.md)
owns workflow complexity; these rules map the decision to Eino surfaces.

## Choose the execution owner

| Need | Candidate | Boundary to keep explicit |
| --- | --- | --- |
| One model, embedding, retriever or tool operation | Component interface and ordinary Go | Application controls calls and errors |
| Sequential typed composition | `compose.Chain` | Data types and stage ordering |
| Conditional routing, branching or cycles | `compose.Graph` | State, transitions and a bounded exit |
| A dependency DAG with field-level mappings | `compose.Workflow` | Mapping names/types and prerequisites |
| A model-directed tool loop or agent composition | Eino ADK | Agent runtime owns that loop; application owns permissions and budgets |

These are choices, not a required progression. Do not wrap an ADK agent inside
another model-directed loop unless their separate responsibilities are necessary
and bounded. Multiple agents require a concrete separation of work or access.

## Typed construction

- Define node input/output and graph state independently from provider message
  formats. Convert at adapters; keep evidence references available to later checks.
- Check errors from node/edge construction and `Compile`. Treat compilation as a
  structural check, not proof of correct routes, authorization or termination.
- For branches, define the destinations and fallback for unsupported decisions.
  For loops, define completion, failure and budget exhaustion explicitly. A runtime
  step limit supplements the business stop condition.
- Keep per-run state and authenticated dependencies out of mutable package globals
  and shared closures. Parallel branches must not mutate shared maps/slices without
  ownership or synchronization. Merge results using explicit identities/order.
- Pass `context.Context` through each adapter to the actual I/O. Decide which
  runtime owns retries so a graph, tool wrapper and provider client do not multiply
  the same retry budget. Follow [execution](../llm-tools/execution.md) for effects.

The [tool/graph fixture](examples/tool-graph.md) tests a minimal typed connection.
It deliberately needs no model or ADK. In a real one-operation application,
calling the tool directly may be simpler than that demonstration graph.

## Contract references

[Chain/Graph](https://www.cloudwego.io/docs/eino/core_modules/chain_and_graph_orchestration/chain_graph_introduction/),
[Workflow source, v0.9.22](https://github.com/cloudwego/eino/blob/v0.9.22/compose/workflow.go),
[ADK overview](https://www.cloudwego.io/docs/eino/core_modules/eino_adk/agent_preview/).
Verify the actual module contract before adopting a different release's builder
or ADK API; the surfaces are not interchangeable.
