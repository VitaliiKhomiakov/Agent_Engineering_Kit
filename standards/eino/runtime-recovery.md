# Eino runtime and recovery

Read for streams, checkpoints or ADK execution. Apply
[Go resource ownership](../go/resources.md) and the shared
[execution contract](../llm-tools/execution.md) to the actual operation.

## Streams and cancellation

Eino distinguishes `Invoke` (single to single), `Stream` (single to stream),
`Collect` (stream to single) and `Transform` (stream to stream). Adapters can
aggregate chunks; calling `Stream` does not prove that every internal stage emits
incrementally. Check the component's actual supported modes and buffering.

The consumer of a returned `schema.StreamReader` owns closing it, including early
exit. Handle `Recv` until `io.EOF`; propagate other errors. Stop upstream work on
client cancellation through the request context and close the stream. A partial
answer or a canceled request is not evidence that an external effect did not occur.

With ADK, inspect event errors/actions as well as output, and drain or cancel its
iterator according to the selected runner contract. Apply the same deadline and
budget to model calls and tools. Do not infer success merely from receiving text.

## Choose one checkpoint contract

| Surface inspected at v0.9.22 | Configuration and resume boundary |
| --- | --- |
| `compose` graph | Compile with `WithCheckPointStore`; address a run with `compose.WithCheckPointID`. Distinguish interrupts with `ExtractInterruptInfo`; use the graph's matching interrupt/resume API. |
| ADK runner | Configure `RunnerConfig.CheckPointStore`; use ADK run options and `Runner.ResumeWithParams` for targeted resume. These are not `compose` invocation options. |

Static before/after-node breaks and dynamic interrupts are different mechanisms.
For dynamic graph interrupts, the inspected API includes `compose.ResumeWithData`
for an interrupt ID; pass the selected checkpoint ID on the resumed invocation.
Do not combine snippets across mechanisms or releases. Resume with a compatible
graph/agent definition, serialized state and required runtime options/dependencies.
Check migration notes before changing any of those while runs are suspended.

The checkpoint store is application-provided. Bind checkpoint IDs to their
authenticated owner and job/conversation, revalidate access and approval on resume,
and preserve the chosen state schema. In-memory storage cannot recover across
process loss. A checkpoint is not a transaction with an external service.
Keep effects safe under replay using the shared execution policy, including
reconciliation or valid downstream idempotency for uncertain outcomes.

For a recovery change, check the actual relevant boundary: interrupted execution,
resume, state persistence after restart, or replay around an external operation.
Do not claim all of those from a successful in-process graph invocation.

## Contract references

[Streaming modes](https://www.cloudwego.io/docs/eino/core_modules/chain_and_graph_orchestration/stream_programming_essentials/),
[graph checkpoints](https://www.cloudwego.io/docs/eino/core_modules/chain_and_graph_orchestration/checkpoint_interrupt/),
[graph resume source, v0.9.22](https://github.com/cloudwego/eino/blob/v0.9.22/compose/resume.go),
[ADK runner source, v0.9.22](https://github.com/cloudwego/eino/blob/v0.9.22/adk/runner.go).
Recovery rules are based on documentation/source review; the bundled Eino fixture
does not execute these persistence or ADK paths.
