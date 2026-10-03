# Bounded byte pipeline

Read when choosing Node stream ownership, total byte limits or cancellation.
[The I/O section](../io-concurrency.md) owns the general guidance. This example
copies byte streams; transport validation and live business invariants remain
separate concerns in the shared JavaScript examples.

## Contract and setup

Copy these two files into one temporary directory. Run with Node 24.13.0 or a
compatible supported release; no package installation is needed. `.mjs` makes the
ESM mode explicit. The recorded version is test evidence, not a patch recommendation.

`copyLimited` accepts fresh byte streams. After capacity validation it owns their
pipeline lifetime; invalid capacity leaves ownership with the caller. A pre-aborted
signal still enters the pipeline's cleanup path. Accepted chunks are forwarded only
while they fit the byte budget; UTF-8 character count is not byte count. Success
returns bytes copied after pipeline completion, including zero for empty input.

Failure can leave partial output. The caller chooses its allowed paths, creation
mode and cleanup/publication policy. This is not atomic file replacement, fsync,
HTTP body parsing, a decompression limit or a strict total-memory quota. The source
must itself produce suitably bounded chunks; backpressure cannot prevent a giant
allocation that already happened. Failed stream instances are discarded, not reused.

## copy.mjs

```js
import { Buffer } from 'node:buffer';
import { Transform } from 'node:stream';
import { pipeline } from 'node:stream/promises';

/**
 * Fresh byte streams become owned by this operation after argument validation.
 * @param {import('node:stream').Readable} source
 * @param {import('node:stream').Writable} destination
 * @param {number} maxBytes
 * @param {AbortSignal} signal
 * @returns {Promise<number>}
 */
export async function copyLimited(source, destination, maxBytes, signal) {
  if (!Number.isSafeInteger(maxBytes) || maxBytes < 0) {
    throw new RangeError('maxBytes must be a nonnegative safe integer');
  }
  let accepted = 0;
  const limit = new Transform({
    /** @param {unknown} chunk */
    transform(chunk, _encoding, callback) {
      if (!Buffer.isBuffer(chunk)) {
        callback(new TypeError('Expected byte chunks'));
        return;
      }
      if (chunk.length > maxBytes - accepted) {
        callback(new RangeError('Byte limit exceeded'));
        return;
      }
      accepted += chunk.length;
      callback(null, chunk);
    },
  });
  await pipeline(source, limit, destination, { signal });
  return accepted;
}
```

## run.mjs

```js
import assert from 'node:assert/strict';
import { Buffer } from 'node:buffer';
import { createReadStream, createWriteStream } from 'node:fs';
import { mkdtemp, readFile, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { Readable, Writable } from 'node:stream';
import { setImmediate as nextTurn } from 'node:timers/promises';
import test from 'node:test';
import { copyLimited } from './copy.mjs';

/** @returns {{sink: Writable, chunks: Buffer[]}} */
function collector() {
  /** @type {Buffer[]} */
  const chunks = [];
  const sink = new Writable({
    /** @param {unknown} chunk */
    write(chunk, _encoding, done) {
      assert.ok(Buffer.isBuffer(chunk));
      chunks.push(Buffer.from(chunk));
      done();
    },
  });
  return { sink, chunks };
}

await test('copies real files and releases handles, including an empty input', async () => {
  const directory = await mkdtemp(join(tmpdir(), 'node-copy-'));
  try {
    const input = join(directory, 'in');
    const output = join(directory, 'out');
    for (const data of [Buffer.from('A€B'), Buffer.alloc(0)]) {
      await writeFile(input, data);
      const source = createReadStream(input, { highWaterMark: 2 });
      const sink = createWriteStream(output);
      assert.equal(await copyLimited(source, sink, data.length, new AbortController().signal), data.length);
      assert.deepEqual(await readFile(output), data);
      assert.equal(source.closed, true);
      assert.equal(sink.closed, true);
    }
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
});

await test('counts bytes and rejects oversize input without forwarding that chunk', async () => {
  const source = Readable.from([Buffer.from('A'), Buffer.from('€')], { objectMode: false });
  const { sink, chunks } = collector();
  await assert.rejects(copyLimited(source, sink, 3, new AbortController().signal), /Byte limit exceeded/);
  assert.equal(Buffer.concat(chunks).toString(), 'A');
  assert.equal(source.destroyed, true);
  assert.equal(sink.destroyed, true);
});

await test('propagates source and destination failures and destroys both sides', async () => {
  const failure = new Error('I/O unavailable');
  for (const failingSide of ['source', 'destination']) {
    const source = failingSide === 'source'
      ? new Readable({ read() { this.destroy(failure); } })
      : Readable.from([Buffer.from('ok')], { objectMode: false });
    const sink = failingSide === 'destination'
      ? new Writable({ write(_chunk, _encoding, done) { done(failure); } })
      : collector().sink;
    await assert.rejects(copyLimited(source, sink, 10, new AbortController().signal), error => error === failure);
    assert.equal(source.destroyed, true);
    assert.equal(sink.destroyed, true);
  }
});

await test('owns cleanup for both pre-abort and in-flight cancellation', async () => {
  for (const beforeStart of [true, false]) {
    const controller = new AbortController();
    const source = new Readable({ read() {} });
    const { sink } = collector();
    if (beforeStart) controller.abort();
    const result = assert.rejects(copyLimited(source, sink, 10, controller.signal), { name: 'AbortError' });
    if (!beforeStart) controller.abort();
    await result;
    assert.equal(source.destroyed, true);
    assert.equal(sink.destroyed, true);
  }
});

await test('backpressure pauses a large source while the first sink write is held', { timeout: 2000 }, async () => {
  const started = Promise.withResolvers();
  const release = Promise.withResolvers();
  let produced = 0;
  let written = 0;
  const source = new Readable({
    highWaterMark: 1024,
    read() {
      if (produced === 256) this.push(null);
      else { produced += 1; this.push(Buffer.alloc(1024)); }
    },
  });
  const sink = new Writable({
    highWaterMark: 1024,
    write(_chunk, _encoding, done) {
      written += 1;
      if (written === 1) {
        started.resolve(undefined);
        release.promise.then(() => done(), done);
      } else done();
    },
  });
  const operation = copyLimited(source, sink, 256 * 1024, new AbortController().signal);
  const observed = assert.doesNotReject(operation);
  try {
    await started.promise;
    await nextTurn();
    assert.ok(produced < 256, `all ${produced} chunks were buffered`);
  } finally {
    release.resolve(undefined);
    await observed;
  }
  assert.equal(await operation, 256 * 1024);
  assert.equal(written, 256);
});

await test('invalid capacity is rejected before stream ownership transfers', async () => {
  const source = new Readable({ read() {} });
  const { sink } = collector();
  try {
    for (const limit of [-1, 0.5, Infinity, Number.MAX_SAFE_INTEGER + 1]) {
      await assert.rejects(copyLimited(source, sink, limit, new AbortController().signal), RangeError);
      assert.equal(source.destroyed, false);
      assert.equal(sink.destroyed, false);
    }
  } finally {
    source.destroy();
    sink.destroy();
  }
});
```

## Run and evidence

```sh
node --check copy.mjs
node --check run.mjs
node --unhandled-rejections=strict run.mjs
```

Six tests passed on Node 24.13.0: real file/empty input and closed handles,
byte-limit rejection with partial-output semantics, source/sink failure identity,
pre-abort and in-flight abort destroying streams, observed backpressure with the
first sink write held, and invalid capacity before ownership transfer. Test files
are created under the OS temporary directory and removed in `finally`.

JSDoc in both files passed strict TypeScript 7.0.2 `allowJs`/`checkJs` with Node
24.13.6 types; that optional development check is separate from executing Node.
The [plan](../../../docs/plans/2026-09-21-engineering-practices.md#k11-result-and-verification)
records the exact tool command and artifact equality check.

The held-sink check establishes that this source is not completely consumed while
blocked; it is not a universal buffer-size benchmark. No malformed custom stream,
real disk failure, concurrent writer, malicious path or HTTP response behavior was
tested. See the [versioned stream reference](https://github.com/nodejs/node/blob/v24.13.0/doc/api/stream.md)
for pipeline lifetime and implementation-specific limits.
