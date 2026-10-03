# JavaScript example: ownership of two required reads

Read this example when an operation needs two independent results and must own
failure/cancellation until its dependencies settle. The [async section](../async-effects.md)
owns the rules. Sequential awaits remain simpler when parallelism is unnecessary.

`loadOverview` accepts an explicit capability object and caller signal. Both reads
must succeed; on failure it aborts its owned group, joins settlement/cleanup and
returns the original failure. Deferred calls also capture a synchronous adapter
throw. The parent listener is removed on exit. A final cancellation check prevents
late results from turning an aborted operation into success.

Adapters must validate their output, own resource cleanup/deadlines and settle
after abort. Cancellation is cooperative. An adapter that never settles can keep
the join pending indefinitely; this example cannot force it to stop. It has two
fixed reads, not an arbitrary-input pool, automatic timeout or retry protocol.
It uses host abort APIs and Node's runner; it is not a browser/fetch integration.

## Setup

Both projects use the installed Node 24.13.0 runner, npm 11.6.2, TypeScript
5.9.3 and `@types/node` 24.13.6 for optional JSDoc checking. These are the executed
versions, not a claim about the newest releases or all compatible runtimes.
The source uses established ES2022 features; DOM declarations describe the abort
API where applicable. A declared type library does not install a host API.
There are no runtime dependencies and no `.ts` implementation files.

Save the following files in a separate temporary directory, retaining the paths.
Install the development tools only when running the static check; `npm test` needs
only Node. The checked temporary projects retain npm locks with package integrity
values. In an existing project, preserve its package manager and lock workflow;
a fresh install from these manifests can resolve different transitive versions.

### `package.json`

```json
{
  "name": "af-javascript-async-ownership",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "engines": {
    "node": ">=24"
  },
  "scripts": {
    "test": "node --unhandled-rejections=strict --test",
    "check": "tsc -p jsconfig.json"
  },
  "devDependencies": {
    "@types/node": "24.13.6",
    "typescript": "5.9.3"
  }
}
```

### `jsconfig.json`

```json
{
  "compilerOptions": {
    "allowJs": true,
    "checkJs": true,
    "noEmit": true,
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": [
      "ES2022",
      "DOM"
    ],
    "types": [
      "node"
    ]
  },
  "include": [
    "src/**/*.js",
    "tests/**/*.js"
  ]
}
```

## Implementation and behavior checks

### `src/overview.js`

```js
/**
 * @typedef {object} Profile
 * @property {string} displayName
 * @typedef {object} Task
 * @property {string} title
 * @typedef {object} Overview
 * @property {Profile} profile
 * @property {Task[]} tasks
 * @typedef {object} OverviewSource
 * @property {(signal: AbortSignal) => Promise<Profile>} loadProfile
 * @property {(signal: AbortSignal) => Promise<Task[]>} loadTasks
 */

/**
 * Two required reads, with one owner for completion, failure and cancellation.
 * Adapters must validate data, own deadlines and settle after abort/cleanup.
 * @param {OverviewSource} source
 * @param {AbortSignal} signal
 * @returns {Promise<Overview>}
 */
export async function loadOverview(source, signal) {
  signal.throwIfAborted();
  const controller = new AbortController();
  const relayAbort = () => controller.abort(signal.reason);
  signal.addEventListener('abort', relayAbort, { once: true });

  // Defer each call so a synchronous adapter throw is an observed rejection too.
  const profile = Promise.resolve().then(() => {
    controller.signal.throwIfAborted();
    return source.loadProfile(controller.signal);
  });
  const tasks = Promise.resolve().then(() => {
    controller.signal.throwIfAborted();
    return source.loadTasks(controller.signal);
  });
  try {
    const [loadedProfile, loadedTasks] = await Promise.all([profile, tasks]);
    controller.signal.throwIfAborted();
    return { profile: loadedProfile, tasks: loadedTasks };
  } catch (failure) {
    controller.abort(failure);
    // Rejection of Promise.all alone neither cancels nor joins the other read.
    await Promise.allSettled([profile, tasks]);
    throw failure;
  } finally {
    signal.removeEventListener('abort', relayAbort);
  }
}
```

### `tests/overview.test.js`

```js
import assert from 'node:assert/strict';
import test from 'node:test';
import { loadOverview } from '../src/overview.js';

/**
 * Deterministic gate: no sleeps, sockets or timing-dependent ordering.
 * @template T
 * @returns {{promise: Promise<T>, resolve: (value: T) => void}}
 */
function deferred() {
  /** @type {((value: T) => void) | undefined} */
  let complete;
  const promise = new Promise(
    /** @param {(value: T) => void} resolve */
    (resolve) => { complete = resolve; },
  );
  return {
    promise,
    resolve(value) {
      if (complete === undefined) throw new Error('Deferred gate was not initialized.');
      complete(value);
    },
  };
}

test('both required reads finish before returning their named result', async () => {
  /** @type {ReturnType<typeof deferred<import('../src/overview.js').Profile>>} */
  const profile = deferred();
  /** @type {ReturnType<typeof deferred<import('../src/overview.js').Task[]>>} */
  const tasks = deferred();
  const pending = loadOverview({
    loadProfile: () => profile.promise,
    loadTasks: () => tasks.promise,
  }, new AbortController().signal);
  tasks.resolve([{ title: 'Review' }]);
  profile.resolve({ displayName: 'Ada' });
  assert.deepEqual(await pending, { profile: { displayName: 'Ada' }, tasks: [{ title: 'Review' }] });
});

test('sibling abort and cleanup settle before the original failure is returned', async () => {
  /** @type {ReturnType<typeof deferred<void>>} */
  const abortSeen = deferred();
  /** @type {ReturnType<typeof deferred<void>>} */
  const cleanup = deferred();
  let cleaned = false;
  const failure = new Error('Profile read failed.');
  const pending = loadOverview({
    loadProfile: async () => { throw failure; },
    loadTasks: async (signal) => {
      signal.addEventListener('abort', () => abortSeen.resolve(), { once: true });
      await cleanup.promise;
      cleaned = true;
      signal.throwIfAborted();
      return [];
    },
  }, new AbortController().signal);
  const rejected = assert.rejects(pending,
    /** @param {unknown} error */ (error) => error === failure);
  let settled = false;
  const observed = pending.then(() => { settled = true; }, () => { settled = true; });
  await abortSeen.promise;
  assert.equal(settled, false);
  assert.equal(cleaned, false);
  cleanup.resolve();
  await rejected;
  await observed;
  assert.equal(cleaned, true);
});

test('a synchronous adapter throw still cancels the other owned read', async () => {
  const failure = new Error('Synchronous task failure.');
  let aborted = false;
  const pending = loadOverview({
    loadProfile: (signal) => new Promise((_resolve, reject) => {
      signal.addEventListener('abort', () => {
        aborted = true;
        reject(signal.reason);
      }, { once: true });
    }),
    loadTasks: () => { throw failure; },
  }, new AbortController().signal);
  await assert.rejects(pending, /** @param {unknown} error */ (error) => error === failure);
  assert.equal(aborted, true);
});

test('pre-aborted calls do not start dependencies', async () => {
  const caller = new AbortController();
  const reason = new Error('No longer needed.');
  caller.abort(reason);
  let started = false;
  await assert.rejects(loadOverview({
    loadProfile: async () => { started = true; return { displayName: 'Ada' }; },
    loadTasks: async () => { started = true; return []; },
  }, caller.signal), /** @param {unknown} error */ (error) => error === reason);
  assert.equal(started, false);
});

test('parent cancellation reaches both in-flight operations', async () => {
  const caller = new AbortController();
  const reason = new Error('Caller cancelled.');
  /** @type {ReturnType<typeof deferred<void>>} */
  const started = deferred();
  let starts = 0;
  let aborts = 0;
  /** @param {AbortSignal} signal @returns {Promise<never>} */
  function untilAbort(signal) {
    return new Promise((_resolve, reject) => {
      signal.addEventListener('abort', () => {
        aborts += 1;
        reject(signal.reason);
      }, { once: true });
      starts += 1;
      if (starts === 2) started.resolve();
    });
  }
  const pending = loadOverview({ loadProfile: untilAbort, loadTasks: untilAbort }, caller.signal);
  const rejected = assert.rejects(pending, /** @param {unknown} error */ (error) => error === reason);
  await started.promise;
  caller.abort(reason);
  await rejected;
  assert.equal(aborts, 2);
});

test('an adapter ignoring cancellation cannot turn an aborted operation into success', async () => {
  const caller = new AbortController();
  const reason = new Error('Discard this result.');
  /** @type {ReturnType<typeof deferred<void>>} */
  const started = deferred();
  /** @type {ReturnType<typeof deferred<void>>} */
  const release = deferred();
  const pending = loadOverview({
    loadProfile: async () => {
      started.resolve();
      await release.promise;
      return { displayName: 'Late result' };
    },
    loadTasks: async () => [],
  }, caller.signal);
  const rejected = assert.rejects(pending, /** @param {unknown} error */ (error) => error === reason);
  await started.promise;
  caller.abort(reason);
  release.resolve();
  await rejected;
});
```

## Run and verified scope

```sh
npm install --ignore-scripts --no-fund
npm run check
npm test
```

Verified on 2026-09-21: `node --check` for each source/test file, `npm run check`
with strict JSDoc settings and no emit, and `npm test` all passed. The local process
runner reported a file aggregate. Running `node --unhandled-rejections=strict
tests/overview.test.js` directly exposed **6 passing scenarios**, with no failed,
cancelled or skipped tests. An intentional failing probe returned exit 1 through
both forms, so the aggregate was not treated as a detailed scenario count.

The six checks cover both results, sibling abort with delayed cleanup,
synchronous dependency failure, pre-abort, parent cancellation of both operations
and a late result from an adapter ignoring cancellation. Controlled promises make
the interleaving deterministic without sleeps or sockets. The delayed-cleanup
check asserts that the outer operation is still pending before releasing cleanup.

The adapter fakes establish orchestration, not network behavior. No fetch, DOM,
worker, timer deadline, database transaction, durable handoff or forced resource
termination is exercised. Aborting a read does not imply undoing a remote write.
The result objects use a named contract; no deep-copy/immutability guarantee is
added to those adapter-owned data values.

The [K09 record](../../../docs/plans/2026-09-21-engineering-practices.md#k09-result-and-verification)
contains verification commands, delivery checks and limits. This example does
not authorize replacing the consumer project's runtime, checker or test framework.
