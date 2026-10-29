# Tool execution and effects

Read when changing retries, concurrency, cancellation, actions or delivery effects;
return to the [tool entry](../llm-tools.md). [Workflow decisions](workflows.md) use
these shared limits; provider/SDK retries do not create a second budget owner.

Retry only classified transient failures within a shared deadline and attempt
budget. Respect provider backoff guidance; do not multiply hidden SDK retries by
workflow retries without accounting for them. Invalid schemas, denied access and
an empty valid search need correction or a different route, not blind repetition.
Model-assisted repair gets a bounded budget and a changed hypothesis/query.

Propagate cancellation to model, store and network operations; bound parallelism.
Independent read branches may run together. Dependent searches wait for the
facts they need; writes and publication follow their ordering/approval contract.

For actions, the authenticated application decides whether approval is required
and binds it to the concrete operation, arguments and relevant state. A model's
claim of approval or a previously approved different action is insufficient.
Preserve existing valid authorization rather than asking again for harmless reads.

Use a stable idempotency key and persisted action/delivery outcome where duplicate
effects matter. Treat an external timeout or lost receipt as an unknown outcome,
not evidence that nothing happened. Retry an uncertain action or send only under
a verified downstream idempotency guarantee, using the same persisted key and
payload within its validity window, or after reconciliation with the downstream
operation ID/state establishes that retry is safe. Otherwise, do not automatically
repeat the action or send. Existing authorization, cancellation and shared
deadline/retry limits still apply.
Do not claim exactly-once external execution from a local checkpoint or tool flag.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee.

[LangGraph Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api),
[LangGraph checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers),
[LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts),
[Resend idempotency contract](https://resend.com/docs/dashboard/emails/idempotency-keys)
(a concrete provider guarantee, not a required delivery service).
