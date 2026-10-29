# LangGraph recovery and streaming

Read for pause/resume, replay or delivery. The shared
[execution rules](../llm-tools/execution.md) own effect safety;
[answer checks](../llm/answers.md) own the final answer boundary.

## Interrupts and resume

Python `interrupt(payload)` requires serializable data, a checkpointer and a thread
ID. Resume with `Command(resume=...)` on the same authorized thread. The interrupted
node starts again; code before `interrupt` can execute again. Do not swallow the
interrupt inside a broad exception handler, or reorder interrupt calls in a node
that must resume a stored execution. Validate the resumed value before use.

The host authenticates the responder, loads the intended suspended operation and
checks that approval still covers its current scope. Treat resume data as input,
not proof that these checks happened. Define expiration/rejection behavior when
approval is needed. A paused workflow is not a failed tool invocation to retry.

Keep replayed code deterministic where the runtime relies on recorded execution.
Isolate external effects and nondeterministic operations with the selected
runtime's task/node persistence mechanism when needed. Even a persisted task can
finish an external action before its result is saved: checkpoints alone cannot
guarantee exactly-once effects. Follow downstream idempotency/reconciliation rules
for that gap. Do not duplicate a completed action to reconstruct graph state.

The [offline resume fixture](examples/resume.md) proves node restart, accepted and
rejected decisions, and invalid resume input. It sends no external action and
does not prove authentication, restart durability or exactly-once execution.

## Streaming and cancellation

Select the actual API/version and consume its documented event shape. Python
`stream`/`astream` modes distinguish state updates, full values, model message
chunks and other events. The v2 stream format requires a compatible release;
the v1.2 event-streaming API is a different interface. Do not parse them as though
their payloads were interchangeable, or copy Python event options into JavaScript.

Map internal events into a deliberate public stream. Full state/debug/tool events
can expose restricted evidence or internal metadata. Emit only authorized fields;
partial model text is not yet a verified final answer. Distinguish completion,
interruption, cancellation and failure in delivery status.

On client disconnect, apply the application's chosen cancellation or background-job
policy. Stopping consumption alone does not prove a remote operation stopped.
Propagate cancellation to actual I/O and reconcile uncertain effects. For durable
execution changes, verify the configured checkpoint write timing and failure
boundary; an in-process happy path does not test recovery after a crash.

## Contract references

[Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts),
[checkpointers and durability](https://docs.langchain.com/oss/python/langgraph/checkpointers),
[streaming](https://docs.langchain.com/oss/python/langgraph/streaming),
[JavaScript interrupts](https://docs.langchain.com/oss/javascript/langgraph/interrupts).
