# Langfuse instrumentation

Read for SDK setup, native OpenTelemetry or trace lifetime. Langfuse records
observations; it does not own source authorization or certify answer correctness.

## Choose a compatible integration

Check the server/deployment, language SDK, framework instrumentation and feature
against the [compatibility matrix](https://langfuse.com/docs/compatibility).
Cloud removals and self-hosted minimum versions differ. Record the selected
combination when integrating or upgrading; do not infer compatibility from the
latest SDK documentation or matching-looking major numbers.

Use supported Python/JS SDK integrations where selected. For Go, use native OTel
for traces and supported APIs for other features. Do not invent Go equivalents of
Python/JS experiment or prompt methods. A working OTLP exporter alone does not
establish those platform features.

## Trace construction and export

- Initialize instrumentation once at the correct process lifecycle boundary.
  Reuse compatible provider/client instances. Avoid instrumenting the same model
  or tool call twice through overlapping framework and manual wrappers.
- Propagate context to child work and remote boundaries deliberately. An unrelated
  background job needs its own lifecycle/correlation decision; do not fabricate
  parentage or use a trace ID as authorization.
- Emit operation names, timing, status and permitted identifiers. Add model/usage
  fields only when known, and distinguish measured usage from estimates. Keep
  input/output logging subject to [privacy rules](privacy-evaluation.md).
- For direct OTel ingestion, use the selected Langfuse region/deployment and its
  OTLP/HTTP endpoint contract. The base endpoint is `/api/public/otel`; a
  trace-specific URL includes `/v1/traces`. Do not append that suffix twice.
  The reviewed contract supports HTTP JSON/protobuf, not OTLP/gRPC.
- Configure project-key Basic authentication through secret configuration. For
  the reviewed v4 direct-ingestion path, configure `x-langfuse-ingestion-version: 4`
  as documented. Check the target deployment before copying headers or legacy
  endpoints; never embed credentials in examples or client-side code.
- Use documented attribute mappings, including `langfuse.observation.type` when
  needed. Verify ingestion/rendering with a harmless span on the actual target;
  an accepted request can still map fields differently than intended. Propagate
  attributes required for filtering to the spans that need them according to the
  selected data model, rather than assuming a root attribute is inherited.
- End spans and flush/shut down exporters within a bounded shutdown context.
  A short-lived script may otherwise exit before export; a service must not flush
  every request by default. Decide how export failures are observed without leaking
  payloads or unnecessarily failing the business request.

## Evidence and references

The [Go OTel fixture](examples/otel-go.md) checks local parentage, approved
attributes and exporter lifetime. It does not contact Langfuse or test transport,
authentication, server mapping or retention.

[Native OpenTelemetry](https://langfuse.com/integrations/native/opentelemetry),
[OpenTelemetry Go](https://opentelemetry.io/docs/languages/go/),
[Go SDK lifecycle](https://pkg.go.dev/go.opentelemetry.io/otel/sdk/trace).
