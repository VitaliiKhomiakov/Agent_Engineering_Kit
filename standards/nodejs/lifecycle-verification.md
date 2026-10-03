# Node.js lifecycle and verification

Read for signals, shutdown, resource cleanup, diagnostics, security verification
or runtime upgrades. The optional [HTTP shutdown example](examples/graceful-server.md)
distinguishes open connections from application tasks. Apply the shared
[verification policy](../verification.md) to choose sufficient checks.

## Start, drain and release

The executable owns readiness and termination; library imports do not install
global process handlers. Start listening/consuming after required initialization.
If startup fails, release resources already acquired, preserve failure evidence,
and return a failing exit status. Do not mark readiness merely because a socket
exists when a required dependency is unavailable.

For a long-running service, make shutdown idempotent: stop admission/readiness,
stop new consumption, finish or cooperatively cancel tracked work within its
budget, then release pools, workers, clients and telemetry in dependency order.
`server.close()` stops accepting connections and, in modern Node, closes idle
HTTP keep-alive connections. It does not join all async work in request callbacks.
A disconnected socket may still have a running database operation behind it.

When the drain deadline expires, abort cooperative work and apply the transport's
force-close policy. For HTTP/1, call `closeAllConnections()` after `close()` to avoid
an admission race; it does not close upgraded WebSocket/HTTP2 sockets. Own those
protocols separately. A promise race or an abort signal cannot stop a dependency
that ignores cancellation; use an external supervisor's hard termination deadline
and make unresolved effects visible. Resource release itself also needs a budget.

Install signal handlers once in the executable and remove them when that owner
ends. Signal delivery/termination differs by OS and process/container setup. An
installed SIGTERM/SIGINT listener replaces default exit behavior on supported
platforms, so it must actually drive shutdown and report failure. Use normal exit
after awaited cleanup with an appropriate `process.exitCode` where possible;
`process.exit()` can truncate asynchronous output. The `exit` event cannot await
cleanup, and `beforeExit` is not a general shutdown hook for every termination.

Unhandled exceptions are a last-resort failure path, not a recover-and-continue
strategy. Report them without claiming the process remains healthy; synchronous
last-resort cleanup differs from orderly signal-driven draining. An external
process supervisor owns restart. Handle expected errors where their contracts are
known rather than adding a global rejection listener that hides defects.

## Diagnostics and security

Use existing structured logging and redact secrets/untrusted payloads. Carry a
correlation context explicitly or use `AsyncLocalStorage.run()` where many async
boundaries warrant it. Prefer that API over hand-built async hooks; keep business
dependencies explicit rather than turning request context into a hidden service
locator. Verify context propagation across the actual callback/worker boundary.

Investigate observed latency/memory pressure with appropriate CPU, event-loop
delay/utilization, heap, queue and pool evidence. A utilization metric alone does
not identify the bottleneck. Bound observability buffers and label cardinality;
diagnostic dumps can contain secrets. Do not add a benchmark or profiler to every
ordinary change.

Use a supported, security-patched runtime for deployment and the accepted lockfile
workflow. Review dependency/lifecycle-script changes where they occur; `npm ci`
checks lock agreement but executes allowed install scripts by default. Disabling
scripts is useful for suitable tooling fixtures, not a guarantee every native
package still works. Node's permission model limits trusted code's accidental
access; it is not an isolation boundary for malicious dependencies or user code.

## Checks and version changes

Verify the real executable/build entry after module/path changes, not just editor
resolution. Use the existing runner; Node's built-in runner is an option, not a
mandatory replacement. Await tests/subtests and owned background work. Check
material runtime boundaries with the relevant cases: truncated/oversize input,
source/sink failure, pre-abort and in-flight cancellation, client disconnect,
shutdown ordering, startup failure or dependency-release failure when affected.

Use temporary files and loopback ports for I/O contracts; mock a narrow collaborator
for business timing/failure. Neither mocks nor type checks prove socket closure,
backpressure, real SQL rollback or distributed durability. Check task/listener and
resource cleanup alongside the result, and use bounded test deadlines without
asserting fragile wall-clock timings. Run only the supported-version/consumer
matrix relevant to a runtime or packaging change; do not infer it from one machine.

Reconcile `engines`, CI, deployment image, native addons, lockfile and package tools
when upgrading. Check official API history for newer features and release/security
notes for the target line. The recorded Node 24.13.0 example run is historical test
evidence, not a current patch recommendation. Avoid permanent rules based on an
assumed even/odd release schedule; consult the maintained release table.

## Basis

[Process](https://nodejs.org/download/release/v24.13.0/docs/api/process.html),
[HTTP](https://nodejs.org/download/release/v24.13.0/docs/api/http.html),
[async context](https://nodejs.org/download/release/v24.13.0/docs/api/async_context.html),
[performance hooks](https://nodejs.org/download/release/v24.13.0/docs/api/perf_hooks.html),
[test runner](https://nodejs.org/download/release/v24.13.0/docs/api/test.html),
[permissions](https://nodejs.org/download/release/v24.13.0/docs/api/permissions.html),
[npm ci](https://docs.npmjs.com/cli/v11/commands/npm-ci/) and
[release support](https://nodejs.org/en/about/previous-releases) distinguish host
guarantees from the application's ownership and verification obligations.
