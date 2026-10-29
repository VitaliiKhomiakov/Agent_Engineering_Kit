# Langfuse privacy, prompts and experiments

Read for captured data, prompt versions or experiments. The shared
[evaluation policy](../llm/evaluation.md) owns datasets, quality measures and
acceptance; these rules address Langfuse's integration boundaries.

## Capture and masking

Minimize data at creation: prefer permitted identifiers, counts and sanitized
statuses over raw prompts, documents, credentials or exception text. Keep hidden
reasoning out of telemetry. Apply the application's access and retention policy
to traces, checkpoints, dataset items and exported results independently.

Determine which instrumentation and exporter sees each field. The reviewed Python
SDK's `mask_otel_spans` hook patches attributes on spans exported by that Langfuse
client; it does not rewrite span names, events, resource attributes or another
exporter's copy. Its position after media handling does not establish that sensitive
media was never uploaded. The older `mask` hook covers SDK-created data, not every
third-party span. Verify the actual SDK version/hook; JS contracts differ.

Sanitize before a sensitive value reaches an uncovered surface. Test representative
input/output, error, metadata and media paths in the actual capture chain when
those paths are enabled. Do not claim system-wide redaction from one hook test.

## Prompts and experiments

- If using managed prompts, record the resolved prompt version, application/model
  configuration and fallback/cache behavior needed to reproduce a result. A
  mutable label alone does not identify the evaluated prompt. Loading a prompt
  does not authorize new tools, sources or actions.
- For an offline evaluation run, select or create a representative dataset and
  freeze the relevant version. “Local dataset” means where inputs originate; a
  Langfuse experiment runner can still transmit inputs, outputs and traces.
  Confirm the destination and permitted fields before executing it.
- Distinguish the task under test from item-level and run-level evaluators. Bound
  concurrency and cost, record failed/skipped cases, and identify evaluator/model
  versions. A high score without coverage or failure accounting is insufficient.
- Use the current SDK experiment runner or a separately verified supported API.
  Do not mix removed dataset-run helpers with a newer major. For other languages,
  check the documented OpenTelemetry experiment attributes/API instead of claiming
  Python/JS runner parity.
- Report what was checked: local fixture, exported telemetry, server acceptance,
  retrieval quality or answer quality. A trace proves an observed execution path,
  not that the answer or evaluator judgment was correct.

## Contract references

[Masking](https://langfuse.com/docs/observability/features/masking),
[prompt management](https://langfuse.com/docs/prompt-management/overview),
[SDK experiments](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk),
[OTel experiments](https://langfuse.com/integrations/native/opentelemetry/experiments).
Compatibility and data handling remain deployment-specific; the bundled OTel
fixture exercises neither prompt management nor an experiment runner.
