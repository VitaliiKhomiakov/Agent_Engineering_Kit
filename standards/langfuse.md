# Langfuse

Apply only when Langfuse tracing, prompts or experiments are used, with the
[core rules](core.md). It does not select RAG, tools, LangGraph or a language.
Read only the relevant section and the shared [evaluation guidance](llm/evaluation.md)
when choosing datasets, metrics or telemetry acceptance.

## Integration and compatibility

Langfuse owns observability, prompt versions and evaluation data, not retrieval
policy or answer correctness. Match SDK/instrumentation to server version
using the compatibility matrix. Initialize exporters deliberately, propagate trace
context, avoid duplicate instrumentation, and flush/shut down according to process
lifetime.

Use compatible Python/JS SDK integrations when selected. Go and other languages
can emit native OpenTelemetry spans to Langfuse; validate supported attributes,
authentication and exporter behavior rather than inventing native SDK parity. Other platform features require their supported API contracts.

## Trace privacy and experiments

Minimize logged inputs/outputs and redact before export, including third-party
spans, metadata, error text and media paths. Confirm which exporter/hook sees each
field; configuring one masking function does not necessarily protect other
exporters. Record observable decisions and evidence, not hidden reasoning.
Local experiment inputs may still be transmitted to the selected Langfuse server; choose retention and access policy accordingly.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee.

[Langfuse overview](https://langfuse.com/docs),
[Langfuse compatibility](https://langfuse.com/docs/compatibility),
[Langfuse masking](https://langfuse.com/docs/observability/features/masking),
[Langfuse SDK experiments](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk),
[Langfuse with LangChain/LangGraph](https://langfuse.com/integrations/frameworks/langchain),
[Langfuse with LlamaIndex](https://langfuse.com/integrations/frameworks/llamaindex),
[Langfuse OpenTelemetry integration](https://langfuse.com/integrations/native/opentelemetry),
[OpenTelemetry Go](https://opentelemetry.io/docs/languages/go/).
