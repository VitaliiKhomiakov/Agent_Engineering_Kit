# TypeScript example: a typed operation with an executed decoder

Read when a generic external-data operation must preserve the relationship between
a validated value and its result type. The [composition section](../composition-effects.md)
owns the rules. A concrete non-generic function remains simpler for a single fixed
contract; this example demonstrates a justified variation through the decoder.

`RawSource` belongs inside an adapter and returns unknown external data. The
consumer-oriented `Decoder<T>` establishes T by executing validation. `loadDecoded`
returns its actual result, observes failure, and checks cancellation before the
read and before decoding a late response. The business-facing result is concrete.
`preferencesDecoder` uses `satisfies` on an authored capability object; the checks
inside its method, not the operator, validate the received data. Extra upstream
fields are allowed but do not leave the deliberate public projection.

The source must honor its real cleanup/deadline contract. A signal and a
`Promise<T>` type do not force cancellation or make a never-settling read finish.
This example does not create a parallel group, a retry policy or a transaction.

## Setup

Verified on 2026-09-21 with Node 24.13.0, npm 11.6.2, native TypeScript 7.0.2,
ESLint 10.11.0, typescript-eslint 8.70.0 and `@types/node` 24.13.6. The
`@typescript/typescript6` compatibility package is pinned at 6.0.2; its locked
compiler/API dependency and `tsc6 --version` report **6.0.3**. The two executables
and imported API were inspected separately. These are executed versions, not a
requirement to upgrade a consumer project or install two compilers everywhere.

TypeScript 7 supplies the build/check command. Typed lint uses the compatible
6.x programmatic API through the documented package aliases; the additional
`check:compat` command verifies the same source with it. All tools are development
dependencies; the emitted program has no runtime package dependencies.

Save the files below in a separate temporary directory, preserving the paths.
The verified projects retain npm locks and integrity values under the stage's
`/tmp` directory. In a real project preserve its package manager/lock; a new
install from the manifest may resolve different transitive versions, including
the compatibility wrapper's compiler. `target`/`lib` describe the example's
supported APIs; they do not install globals or establish browser compatibility.

### `package.json`

```json
{
  "name": "af-typescript-typed-operation",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "engines": {
    "node": ">=24"
  },
  "scripts": {
    "check": "tsc -p tsconfig.json --noEmit",
    "check:compat": "tsc6 -p tsconfig.json --noEmit",
    "build": "tsc -p tsconfig.json",
    "lint": "eslint src tests --max-warnings=0",
    "test": "node --unhandled-rejections=strict dist/tests/run.js"
  },
  "devDependencies": {
    "@types/node": "24.13.6",
    "@typescript/native": "npm:typescript@7.0.2",
    "typescript": "npm:@typescript/typescript6@6.0.2",
    "eslint": "10.11.0",
    "typescript-eslint": "8.70.0"
  }
}
```

### `tsconfig.json`

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,
    "noFallthroughCasesInSwitch": true,
    "noImplicitReturns": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noUncheckedSideEffectImports": true,
    "verbatimModuleSyntax": true,
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": [
      "ES2022"
    ],
    "types": [
      "node"
    ],
    "rootDir": ".",
    "outDir": "dist",
    "noEmitOnError": true
  },
  "include": [
    "src/**/*.ts",
    "tests/**/*.ts"
  ]
}
```

### `eslint.config.mjs`

```js
import tseslint from 'typescript-eslint';

export default tseslint.config(
  { ignores: ['dist/**', 'negative/**'] },
  ...tseslint.configs.recommendedTypeChecked,
  {
    files: ['src/**/*.ts', 'tests/**/*.ts'],
    languageOptions: {
      parserOptions: { projectService: true, tsconfigRootDir: import.meta.dirname },
    },
    rules: {
      '@typescript-eslint/no-explicit-any': 'error',
      '@typescript-eslint/no-floating-promises': ['error', { ignoreVoid: false }],
      '@typescript-eslint/consistent-type-imports': 'error',
    },
  },
);
```

## Implementation and behavior checks

### `src/load.ts`

```ts
// The unknown response exists only inside this external-data adapter boundary.
export interface RawSource {
  readonly read: (key: string, signal: AbortSignal) => Promise<unknown>;
}

export interface Decoder<T> {
  readonly parse: (input: unknown) => T;
}

export async function loadDecoded<T>(
  source: RawSource,
  decoder: Decoder<T>,
  key: string,
  signal: AbortSignal,
): Promise<T> {
  signal.throwIfAborted();
  const raw = await source.read(key, signal);
  signal.throwIfAborted();
  return decoder.parse(raw);
}

export interface Preferences {
  readonly theme: 'light' | 'dark';
}

export const preferencesDecoder = {
  parse(input: unknown): Preferences {
    if (typeof input !== 'object' || input === null || Array.isArray(input)
        || !Object.hasOwn(input, 'theme') || !('theme' in input)
        || (input.theme !== 'light' && input.theme !== 'dark')) {
      throw new Error('Invalid preferences response.');
    }
    // The upstream may add fields. Only the public projection leaves the adapter.
    return Object.freeze({ theme: input.theme });
  },
} satisfies Decoder<Preferences>;
```

### `tests/run.ts`

```ts
import assert from 'node:assert/strict';
import test from 'node:test';
import { loadDecoded, preferencesDecoder } from '../src/load.js';
import type { Decoder, Preferences, RawSource } from '../src/load.js';

await test('validated output and generic result type come from the decoder', async () => {
  const caller = new AbortController();
  const source: RawSource = {
    read: (key: string, signal: AbortSignal): Promise<unknown> => {
      assert.equal(key, 'prefs');
      assert.equal(signal, caller.signal);
      return Promise.resolve({ theme: 'dark', internalToken: 'not-public' });
    },
  };
  const result: Preferences = await loadDecoded(source, preferencesDecoder, 'prefs', caller.signal);
  assert.deepEqual(result, { theme: 'dark' });
  assert.equal(Reflect.set(result, 'theme', 'light'), false);
  const lengthDecoder: Decoder<number> = {
    parse: (input: unknown): number => {
      if (typeof input !== 'string') throw new Error('Expected a string.');
      return input.length;
    },
  };
  const length: number = await loadDecoded(
    { read: (): Promise<unknown> => Promise.resolve('abc') }, lengthDecoder, 'text', caller.signal,
  );
  assert.equal(length, 3);
});

await test('a declared generic return does not allow invalid remote data through', async () => {
  await assert.rejects(loadDecoded(
    { read: (): Promise<unknown> => Promise.resolve({ theme: 'unknown' }) },
    preferencesDecoder, 'prefs', new AbortController().signal,
  ), /Invalid preferences response/);
});

await test('dependency rejection and synchronous throw retain their identity', async () => {
  const failure = new Error('Source failed.');
  const sources: readonly RawSource[] = [
    { read: (): Promise<unknown> => Promise.reject(failure) },
    { read: (): Promise<unknown> => { throw failure; } },
  ];
  for (const source of sources) {
    await assert.rejects(loadDecoded(source, preferencesDecoder, 'prefs', new AbortController().signal),
      (error: unknown): boolean => error === failure);
  }
});

await test('pre-abort does not start the source', async () => {
  const caller = new AbortController();
  const failure = new Error('Cancelled before starting.');
  caller.abort(failure);
  let started = false;
  const source: RawSource = {
    read: (): Promise<unknown> => { started = true; return Promise.resolve({ theme: 'dark' }); },
  };
  await assert.rejects(loadDecoded(source, preferencesDecoder, 'prefs', caller.signal),
    (error: unknown): boolean => error === failure);
  assert.equal(started, false);
});

await test('cancellation while awaiting prevents decoding a late response', async () => {
  const caller = new AbortController();
  const failure = new Error('Cancelled while reading.');
  let decoded = false;
  const decoder: Decoder<Preferences> = {
    parse: (input: unknown): Preferences => { decoded = true; return preferencesDecoder.parse(input); },
  };
  const source: RawSource = {
    read: (): Promise<unknown> => {
      caller.abort(failure);
      return Promise.resolve({ theme: 'dark' });
    },
  };
  await assert.rejects(loadDecoded(source, decoder, 'prefs', caller.signal),
    (error: unknown): boolean => error === failure);
  assert.equal(decoded, false);
});
```

## Run and verified scope

```sh
npm install --ignore-scripts --no-fund
npm run check
npm run check:compat
npm run lint
npm run build
npm test
```

All commands passed in the verified temporary project. The two compilers checked
source and tests with the supplied project config; typed lint reported no warnings
or errors. TypeScript 7 emitted ESM; syntax checks and execution of that output
passed. Node reported **5 passing tests**, with zero failed, cancelled or skipped.

Runtime checks establish two decoder/result relationships, output projection,
invalid remote-data rejection, preserved synchronous/asynchronous failure,
pre-abort without starting I/O and cancellation before late data is decoded.
The tests use typed fakes, no sockets or arbitrary sleeps. The second decoder
returns a number; its generic relationship is also checked by explicit consumers.

Stage verification compiled invalid consumers with both compilers: assigning a
Preferences-producing operation to `Promise<string>`, and supplying a string-only
parser where an unknown-input decoder is required. Both fail with TS2322. A
separate, never-executed enforcement probe confirmed that strict compilers accept
explicit/vendor `any` and an unowned promise, while typed lint rejects explicit
any, all five unsafe-operation categories and floating promises. The intentionally
invalid probes are excluded from normal source/tests; these files have no casts,
`any` annotations or diagnostic suppressions.

No real HTTP/database adapter, browser API, timing deadline, forced abort, durable
handoff or retry was exercised. The fake that ignores cancellation still settles;
this does not prove real I/O termination. Public output projection is demonstrated;
a broader serialization/authorization policy remains with the actual application.

The [K10 record](../../../docs/plans/2026-09-21-engineering-practices.md#k10-result-and-verification)
contains final commands, negative-check evidence, delivery checks and limits.
