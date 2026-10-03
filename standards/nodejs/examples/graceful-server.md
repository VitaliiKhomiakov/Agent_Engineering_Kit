# HTTP shutdown with owned application work

Read for HTTP/1 shutdown and the distinction between socket and task lifetime.
[Lifecycle guidance](../lifecycle-verification.md) owns the broader obligations.
Use a framework's lifecycle facilities when available; this example does not
replace them or implement a general server scaffold.

## Contract and setup

Copy these two files into one temporary directory and run with Node 24.13.0 or a
compatible supported release. No packages are required. Tests bind ephemeral ports
only on `127.0.0.1`; the environment must allow loopback listeners. This older test
patch is not a deployment recommendation.

`readMessage(signal)` is an application capability returning a trusted string. It
must settle and finish its owned cleanup after cancellation. `release()` disposes
its shared dependency after all admitted work settles. `report(error)` is a
synchronous, nonthrowing error reporter. Request/response objects stay at the
transport boundary; no DTO class or DI container is needed.

The executable must finish initialization and successful `listen` before calling
`stop`; it owns startup-failure cleanup and any signal handlers. `stop` immediately
closes admission and returns the same promise on repeated calls. It awaits HTTP
closure and a snapshot of tracked application promises before releasing the
shared dependency. No new application promise can enter after that snapshot.

At the grace deadline it requests cancellation and closes HTTP/1 connections.
If a client disconnects earlier, the request signal aborts, while cleanup remains
tracked. The timer is cleared when draining settles. A failed release rejects
shutdown and is not silently retried. Unexpected application failures are reported
and mapped to a generic 500; expected cancellation does not leak an error body.
Cancellation is recognized by the exact signal reason or the Node-style
`AbortError` carrying that reason as its cause. Adapt other clients' cancellation
errors at their boundary. An unrelated error after abort is still reported;
checking `signal.aborted` alone would hide a failing cleanup operation.

## service.mjs

```js
import { createServer } from 'node:http';

/**
 * @typedef {object} Dependencies
 * @property {(signal: AbortSignal) => Promise<string>} readMessage
 * @property {() => Promise<void>} release
 * @property {(error: unknown) => void} report Synchronous, nonthrowing reporter.
 */

/**
 * @param {import('node:http').ServerResponse} response
 * @param {Dependencies} dependencies
 * @param {AbortSignal} stopping
 * @returns {Promise<void>}
 */
async function respond(response, dependencies, stopping) {
  const disconnected = new AbortController();
  const signal = AbortSignal.any([stopping, disconnected.signal]);
  const onClose = () => {
    if (!response.writableFinished) disconnected.abort(new Error('Client disconnected'));
  };
  response.once('close', onClose);
  try {
    signal.throwIfAborted();
    const message = await dependencies.readMessage(signal);
    signal.throwIfAborted();
    if (!response.destroyed) {
      response.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
      response.end(message);
    }
  } catch (error) {
    const cancelled = signal.aborted && (
      error === signal.reason ||
      (error instanceof Error && error.name === 'AbortError' && error.cause === signal.reason)
    );
    if (!cancelled) dependencies.report(error);
    if (!response.destroyed) {
      response.writeHead(cancelled ? 503 : 500);
      response.end(cancelled ? 'Unavailable' : 'Internal error');
    }
  } finally {
    response.off('close', onClose);
  }
}

/**
 * Called after listen succeeds. Dependencies must settle after cancellation.
 * @param {import('node:http').Server} server
 * @param {Set<Promise<void>>} active
 * @param {AbortController} cancellation
 * @param {() => Promise<void>} release
 * @param {number} graceMs
 * @returns {Promise<void>}
 */
async function drain(server, active, cancellation, release, graceMs) {
  const closed = new Promise((resolve, reject) => {
    server.close(error => error ? reject(error) : resolve(undefined));
  });
  const timer = setTimeout(() => {
    cancellation.abort(new Error('Drain deadline exceeded'));
    server.closeAllConnections();
  }, graceMs);
  const outcomes = await Promise.allSettled([closed, ...active]);
  clearTimeout(timer);
  /** @type {unknown[]} */
  const failures = outcomes.filter(item => item.status === 'rejected').map(item => item.reason);
  try {
    await release();
  } catch (error) {
    failures.push(error);
  }
  if (failures.length > 0) throw new AggregateError(failures, 'Shutdown failed');
}

/**
 * @param {Dependencies} dependencies
 * @param {number} graceMs
 * @returns {{server: import('node:http').Server, stop: () => Promise<void>}}
 */
export function createService(dependencies, graceMs) {
  if (!Number.isSafeInteger(graceMs) || graceMs < 1 || graceMs > 2147483647) {
    throw new RangeError('graceMs must fit a positive Node timer');
  }
  const cancellation = new AbortController();
  /** @type {Set<Promise<void>>} */
  const active = new Set();
  /** @type {Promise<void> | undefined} */
  let stopping;
  let accepting = true;
  const server = createServer((request, response) => {
    if (!accepting || request.method !== 'GET' || request.url !== '/message') {
      response.writeHead(accepting ? 404 : 503, { Connection: 'close' });
      response.end();
      return;
    }
    const task = respond(response, dependencies, cancellation.signal);
    active.add(task);
    task.then(
      () => { active.delete(task); },
      error => { active.delete(task); dependencies.report(error); },
    );
  });
  function stop() {
    if (stopping === undefined) {
      accepting = false;
      stopping = drain(server, active, cancellation, dependencies.release, graceMs);
    }
    return stopping;
  }
  return { server, stop };
}
```

## run.mjs

```js
import assert from 'node:assert/strict';
import { once } from 'node:events';
import { get } from 'node:http';
import { setImmediate as nextTurn, setTimeout as delay } from 'node:timers/promises';
import test from 'node:test';
import { createService } from './service.mjs';

/** @param {import('node:http').Server} server @returns {Promise<number>} */
async function listen(server) {
  const listening = once(server, 'listening');
  server.listen(0, '127.0.0.1');
  await listening;
  const address = server.address();
  assert.ok(address !== null && typeof address !== 'string');
  return address.port;
}

/**
 * @typedef {{status: number | undefined, body: string}} Reply
 * @param {number} port
 * @returns {{request: import('node:http').ClientRequest, reply: Promise<Reply>}}
 */
function send(port) {
  /** @type {PromiseWithResolvers<Reply>} */
  const completed = Promise.withResolvers();
  const request = get({ hostname: '127.0.0.1', port, path: '/message', agent: false }, response => {
    let body = '';
    response.setEncoding('utf8');
    response.on('data', /** @param {unknown} chunk */ chunk => {
      assert.equal(typeof chunk, 'string');
      body += chunk;
    });
    response.on('error', completed.reject);
    response.on('end', () => completed.resolve({ status: response.statusCode, body }));
  });
  request.on('error', completed.reject);
  return { request, reply: completed.promise };
}

await test('finishes admitted work, rejects new connections and releases once', { timeout: 3000 }, async () => {
  const entered = Promise.withResolvers();
  const continueWork = Promise.withResolvers();
  /** @type {string[]} */
  const events = [];
  const application = createService({
    async readMessage() {
      entered.resolve(undefined);
      await continueWork.promise;
      events.push('work');
      return 'Hello';
    },
    async release() { events.push('release'); },
    report(error) { assert.fail(String(error)); },
  }, 2000);
  const port = await listen(application.server);
  const response = send(port).reply;
  const observed = assert.doesNotReject(response);
  await entered.promise;
  const stopping = application.stop();
  assert.equal(application.stop(), stopping);
  assert.equal(application.server.listening, false);
  try {
    await assert.rejects(send(port).reply, { code: 'ECONNREFUSED' });
    assert.deepEqual(events, []);
  } finally {
    continueWork.resolve(undefined);
    await observed;
    await stopping;
  }
  assert.deepEqual(await response, { status: 200, body: 'Hello' });
  assert.deepEqual(events, ['work', 'release']);
});

await test('drain deadline aborts work and force-closes the active HTTP socket', { timeout: 3000 }, async () => {
  const entered = Promise.withResolvers();
  /** @type {string[]} */
  const events = [];
  const application = createService({
    async readMessage(signal) {
      entered.resolve(undefined);
      try { await delay(60000, undefined, { signal }); }
      finally { events.push('work-ended'); }
      return 'too late';
    },
    async release() { events.push('release'); },
    report(error) { assert.fail(String(error)); },
  }, 10);
  const port = await listen(application.server);
  const disconnected = assert.rejects(send(port).reply, { code: 'ECONNRESET' });
  await entered.promise;
  await application.stop();
  await disconnected;
  assert.deepEqual(events, ['work-ended', 'release']);
  assert.equal(application.server.listening, false);
});

await test('client disconnection does not release dependencies before work cleanup', { timeout: 3000 }, async () => {
  const entered = Promise.withResolvers();
  const cancelled = Promise.withResolvers();
  const finishCleanup = Promise.withResolvers();
  /** @type {string[]} */
  const events = [];
  const application = createService({
    async readMessage(signal) {
      entered.resolve(undefined);
      try { await delay(60000, undefined, { signal }); }
      finally {
        cancelled.resolve(undefined);
        await finishCleanup.promise;
        events.push('work-ended');
      }
      return 'too late';
    },
    async release() { events.push('release'); },
    report(error) { assert.fail(String(error)); },
  }, 2000);
  const port = await listen(application.server);
  const client = send(port);
  const disconnected = assert.rejects(client.reply, { code: 'ECONNRESET' });
  await entered.promise;
  client.request.destroy();
  await cancelled.promise;
  const stopping = application.stop();
  try {
    await nextTurn();
    assert.deepEqual(events, []);
  } finally {
    finishCleanup.resolve(undefined);
    await stopping;
    await disconnected;
  }
  assert.deepEqual(events, ['work-ended', 'release']);
});

await test('reports application failure and sends only a generic response', { timeout: 3000 }, async () => {
  const failure = new Error('private upstream detail');
  /** @type {unknown[]} */
  const reported = [];
  const application = createService({
    async readMessage() { throw failure; },
    async release() {},
    report(error) { reported.push(error); },
  }, 2000);
  const port = await listen(application.server);
  try {
    assert.deepEqual(await send(port).reply, { status: 500, body: 'Internal error' });
    assert.deepEqual(reported, [failure]);
  } finally {
    await application.stop();
  }
});

await test('dependency-release failure is observable and is not retried implicitly', { timeout: 3000 }, async () => {
  const failure = new Error('release failed');
  let releases = 0;
  const application = createService({
    async readMessage() { return 'Hello'; },
    async release() { releases += 1; throw failure; },
    report(error) { assert.fail(String(error)); },
  }, 2000);
  await listen(application.server);
  const stopping = application.stop();
  await assert.rejects(stopping, error => error instanceof AggregateError && error.errors[0] === failure);
  assert.equal(application.stop(), stopping);
  assert.equal(releases, 1);
});

await test('does not hide a cleanup failure merely because cancellation occurred', { timeout: 3000 }, async () => {
  const entered = Promise.withResolvers();
  const failure = new Error('cleanup failed after abort');
  /** @type {unknown[]} */
  const reported = [];
  const application = createService({
    async readMessage(signal) {
      entered.resolve(undefined);
      const result = await Promise.allSettled([delay(60000, undefined, { signal })]);
      assert.equal(result[0]?.status, 'rejected');
      throw failure;
    },
    async release() {},
    report(error) { reported.push(error); },
  }, 10);
  const port = await listen(application.server);
  const disconnected = assert.rejects(send(port).reply, { code: 'ECONNRESET' });
  await entered.promise;
  await application.stop();
  await disconnected;
  assert.deepEqual(reported, [failure]);
});
```

## Run and evidence

```sh
node --check service.mjs
node --check run.mjs
node --unhandled-rejections=strict run.mjs
```

Six tests passed on Node 24.13.0 with real loopback HTTP: admitted work completes
before dependency release; new connections are refused; repeated stop reuses its
promise; the grace deadline aborts and force-closes; a disconnected client's async
cleanup delays release; an application failure is logged/mapped; release failure
remains observable; an unrelated error after abort is still reported. Gates establish ordering without fixed sleeps or timing ratios.
The small deadline test checks its effect rather than exact elapsed milliseconds.

Both files also passed strict JSDoc `allowJs`/`checkJs` with TypeScript 7.0.2 and
Node 24.13.6 types. The [plan](../../../docs/plans/2026-09-21-engineering-practices.md#k11-result-and-verification)
records commands and exact Markdown/source equality. The direct test-file command
awaits every `node:test` registration and reports the individual test results.

## Limits when adapting

The grace timer bounds the cooperative drain phase; it cannot force arbitrary
JavaScript/dependencies to settle, and it does not time-bound `release`. A service
needs a supervisor's hard deadline, release budgets, readiness/admission capacity,
ordinary operation deadlines and its actual input/authentication policies. This
one read-only GET endpoint and its trusted message capability do not demonstrate
body parsing, bounded response size or durable write cancellation semantics.

The executable must own server errors, OS-signal wiring and partial-startup cleanup.
No HTTP2/WebSocket, proxy/TLS, keep-alive matrix, process signal or real database
was tested. Every requested side effect must remain inside its tracked capability;
launching an unowned task from it would violate this example's contract.
[Node HTTP](https://nodejs.org/download/release/v24.13.0/docs/api/http.html) documents
connection-closing mechanisms; tracking application promises is our ownership policy.
