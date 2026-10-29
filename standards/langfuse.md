# Langfuse

Apply only when Langfuse tracing, prompts or experiments are used, with the
[core rules](core.md). It does not select RAG, tools, LangGraph or a language.
Read only the relevant section and the shared [evaluation guidance](llm/evaluation.md)
when choosing datasets, metrics or telemetry acceptance.

## Read by task

| Task touches | Read |
| --- | --- |
| SDK/server choice, trace propagation, exporters or Go OTel | [Instrumentation](langfuse/instrumentation.md) |
| Masking, prompts, datasets or experiments | [Privacy and evaluation](langfuse/privacy-evaluation.md) |
| A small executable Go trace boundary | [Local OTel fixture](langfuse/examples/otel-go.md) |

## Integration and compatibility

Langfuse owns observability, prompt versions and evaluation data, not retrieval
policy or answer correctness. The instrumentation topic owns compatibility,
attribute mapping and lifecycle for the selected SDK or native OTel integration.
Other platform features require their supported API contracts.

## Trace privacy and experiments

The privacy/evaluation topic owns capture limits, masking coverage, prompt
provenance and experiment export. Read it when changing what data leaves the
application or what an experiment result claims.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee. The
Go fixture verifies local OTel behavior; it does not contact a Langfuse server.

[Langfuse overview](https://langfuse.com/docs),
[Langfuse compatibility](https://langfuse.com/docs/compatibility),
[Langfuse masking](https://langfuse.com/docs/observability/features/masking),
[Langfuse SDK experiments](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk),
[Langfuse with LangChain/LangGraph](https://langfuse.com/integrations/frameworks/langchain),
[Langfuse with LlamaIndex](https://langfuse.com/integrations/frameworks/llamaindex),
[Langfuse OpenTelemetry integration](https://langfuse.com/integrations/native/opentelemetry),
[OpenTelemetry Go](https://opentelemetry.io/docs/languages/go/).
