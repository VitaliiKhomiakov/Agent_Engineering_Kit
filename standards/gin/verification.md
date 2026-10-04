# Gin: verification and compatibility

Read when choosing checks for changed Gin behavior, upgrading dependencies,
changing a JSON codec/build tag, or investigating performance. Return to the
[Gin entry](../gin.md). The shared [verification policy](../verification.md)
owns test depth and review; this file identifies Gin-specific failure modes.

## Check observable HTTP behavior

Use `net/http/httptest` with the constructed router's `ServeHTTP` for binding,
route, and middleware contracts. A manually allocated Gin context bypasses route
registration and may miss the very failure under review. Start a real test server
only when transport/disconnect/streaming behavior needs it; a recorder does not
establish those properties.

| Changed concern | Meaningful evidence when relevant |
| --- | --- |
| Request contract | Valid input; malformed input; absent/null versus explicit zero; wrong media type; size bounds including unknown length; strictness choices |
| Application boundary | Rejected transport input never reaches effects; state conflict maps separately; wrapped errors retain intended status; request context reaches the dependency |
| Middleware or routes | Denied requests never reach protected work; intended public routes remain accessible; final status/body/headers reflect actual order; path/method changes preserve the API |
| Response/error ownership | An attached error has the intended responder; a committed body is not appended/replaced; private details are absent from public output |
| Cancellation or background work | Cooperative cancellation, bounded work, and owned completion; use events rather than sleeps to coordinate actors |
| Startup/ingress change | Proxy trust and spoofed headers; required limits/timeouts; shutdown completion, including separately owned long-lived connections |

Select rows for the actual change, not as a mandatory suite for every handler.
Keep domain invariants in domain tests and use real adapters when verifying
transaction or remote-system behavior; a fake publisher cannot establish it.
The [binding](examples/binding.md) and [middleware](examples/middleware.md)
examples specify their own checked behavior and omissions.

Set Gin mode and process-wide validator/decoder settings before concurrent tests;
do not race global mutations through `t.Parallel`. Use independently constructed
routers. Run `gofmt`, relevant package tests and static checks; use `-race` for
affected concurrent behavior as described in [Go verification](../go/verification.md).
See [Gin testing](https://gin-gonic.com/en/docs/testing/).

## Versions and migration

Evidence was checked on 2026-09-21 against Gin **v1.12.0** and its default
validator **v10.30.1**. Gin 1.12's tagged `go.mod` requires Go **1.25.0**;
Gin 1.11's requires **1.23.0**. This is applicability evidence, not a request to
upgrade. Inspect the project's resolved module graph, toolchain, middleware
versions, build tags, and codec, rather than copying current website prerequisites
onto an older supported project.

For an authorized upgrade, review release changes that touch actual use: binding
and validator semantics, proxy parsing, routing/escaped paths, response writers,
and middleware compatibility. Compare affected HTTP contracts before/after.
Do not introduce newer APIs, runtime codec selection, HTTP/3, or another decoder
solely because a release offers them. They need a real requirement and their own
transport/compatibility evidence.

Gin's default JSON binder/codec and a local `encoding/json` binder may differ.
Codec changes can affect number handling, unknown/duplicate keys, escaping,
trailing input, and size-error propagation. A clean build is not wire compatibility.
Global decoder switches must remain consistent with the application's startup
and test model. Pin example dependencies and record the toolchain actually used.

See [releases](https://github.com/gin-gonic/gin/releases),
[1.12 module](https://github.com/gin-gonic/gin/blob/v1.12.0/go.mod),
[1.11 module](https://github.com/gin-gonic/gin/blob/v1.11.0/go.mod), and
[codec interface](https://github.com/gin-gonic/gin/blob/v1.12.0/codec/json/json.go).

## Performance and limits of evidence

Profile the endpoint workload before changing codecs, adding pools, buffering
bodies, caching repeated binding, or increasing concurrency. Include dependency
latency, payload sizes, allocation pressure, and relevant middleware. A router
microbenchmark does not predict a DB-backed endpoint's throughput or tail latency.
For repeated body inspection, account for bounded buffering and lifetime; do not
pay that cost when one bind suffices. Existing [Go performance guidance](../go/verification.md)
owns measurement practice.

This research checks examples and policy delivery. It does not certify a deployed
service, an alternate codec, or model adherence to conditional reading. Actual
commands/results and the native-pilot boundary are recorded in the
[K02 plan](../../docs/plans/2026-09-21-engineering-practices.md#k02-working-scope).
