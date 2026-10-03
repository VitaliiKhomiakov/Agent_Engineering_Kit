# Node.js I/O and concurrency

Read for streams, file operations, CPU work, workers, event callbacks or concurrency
limits. [Shared async rules](../javascript/async-effects.md) own promise sequencing
and general cancellation semantics. The optional [bounded stream example](examples/bounded-stream.md)
shows byte limits, pipeline failure and abort with actual Node streams.

## Capacity follows the resource

Asynchronous I/O usually lets other requests progress, but parsing a huge JSON
document, pathological regular expressions, compression or expensive callbacks can
still exhaust CPU or shared capacity. Many filesystem/crypto operations use the
libuv worker pool; that pool is distinct from JavaScript `worker_threads`. Bound
input size and active operations according to measured cost and available clients,
connections and memory. A queue with no admission limit only moves overload.

Prefer ordinary async I/O for I/O work. For evidenced CPU pressure, first reduce
the work or partition it where correctness permits; consider a bounded worker pool
when parallel JavaScript work pays for startup, transfer and coordination. A worker
per request is not the default. A durable job queue solves durability/scheduling
requirements, not merely the presence of `async`. Avoid recursive microtask or
`nextTick` chains that starve I/O; do not assume exact timer ordering across versions.

## Stream ownership and backpressure

Use `node:stream/promises` pipeline for a sequence whose stream lifetimes it owns.
Await completion and pass the operation's signal. Errors/abort can destroy the
participating streams; an async generator must also honor its signal while awaiting
other work. Do not reuse failed streams as a general retry mechanism. Mixing
`data` listeners, piping and iteration makes consumption ownership hard to establish.

When manually writing, stop after `write()` returns false and await drain or failure
with proper listener cleanup; prefer pipeline when it already expresses the flow.
`highWaterMark` controls buffering pressure, not a hard memory quota or total body
size. Validate/count bytes at the relevant boundary, bound object sizes for object
mode, and account for decompression expansion. A limit after a giant allocation
cannot recover memory already consumed. Keep decoding boundaries correct when UTF-8
characters span chunks; do not decode each arbitrary chunk independently.

Pipeline is not an HTTP error-response policy: destruction of an incoming request
or outgoing response can close its socket before a structured error is sent. Use
the framework's bounded body mechanism or explicitly own that HTTP failure path.
For files, failure can leave partial output; temporary-file publication, cleanup and
durability require a separate contract. Do not describe pipeline success as fsync or
transactional replacement.

## Files and event-driven APIs

Use `try`/`finally` around an acquired file handle, or a verified disposal protocol.
Avoid access/existence checks as a substitute for attempting the operation and
handling its actual error: the filesystem can change between check and use. Sequence
writes to the same file/handle, use exclusive creation where required, and define
the allowed path/root and symlink behavior for external filenames. `path.join` is
not an authorization boundary. Cancellation of a write may leave some data written.

`EventEmitter` invokes listeners synchronously and does not generally await their
returned promises. At callback boundaries, register owned completion/error handling
and account for in-flight tasks during shutdown. Handle an emitter's `error` event
where its API requires it; an outer `try` around registration cannot catch a later
event. `captureRejections` can route rejections but does not join or cancel tasks.
Do not raise listener limits merely to hide a subscription leak. Remove owned
listeners and timers when their scope ends.

Use an executable and argument array with `spawn`/`execFile` where a child process
is needed; avoid interpolating untrusted input into a shell command. Argument arrays
still need validation against the called program's options and file semantics.
Bound/capture output appropriately, handle spawn errors and exit status, and define
child shutdown; sending a signal is not proof of completion or descendant cleanup.

## Basis

[Event-loop and pool guidance](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop),
[worker threads](https://nodejs.org/download/release/v24.13.0/docs/api/worker_threads.html),
[streams](https://github.com/nodejs/node/blob/v24.13.0/doc/api/stream.md),
[filesystem](https://nodejs.org/download/release/v24.13.0/docs/api/fs.html),
[events](https://nodejs.org/download/release/v24.13.0/docs/api/events.html) and
[child processes](https://nodejs.org/download/release/v24.13.0/docs/api/child_process.html)
support these mechanisms. Capacity limits and resource contracts are chosen for the
application; there is no universal safe fan-out count.
