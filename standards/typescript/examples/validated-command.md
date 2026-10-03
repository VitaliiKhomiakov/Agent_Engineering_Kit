# TypeScript example: validated command and stateful refusal

Read when deciding what a DTO, type checker and current-state invariant each
establish. The [validation/state section](../validation-state.md) owns the rules.

`LimitChange` is a named interface with an exact optional note. Parsing rejects
invalid data and constructs an owned plain object. Omission preserves a previous
note, null clears it, and an empty string is meaningful. `Quota` owns private
state, rejects an invalid numeric limit for direct callers, and returns a named
union when current usage prevents the change. It checks refusal before mutation.
`describeChange` demonstrates exhaustive outcome handling at a consumer boundary.

The parser accepts JSON-decoded data; it does not promise safe introspection of
hostile getters/proxies. Its note limit counts UTF-16 code units. Frozen snapshots
contain primitives only. Numeric/domain guards and runtime snapshots serve actual
invariants; no DTO class, factory, schema dependency or repository is introduced.

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
  "name": "af-typescript-validated-command",
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

### `src/change.ts`

```ts
export interface LimitChange {
  readonly limit: number;
  readonly note?: string | null;
}

export class InvalidChange extends Error {}

// This boundary accepts data decoded from JSON, not arbitrary executable objects.
export function parseLimitChange(input: unknown): LimitChange {
  if (typeof input !== 'object' || input === null || Array.isArray(input)) {
    throw new InvalidChange('Expected an object.');
  }
  if (Object.keys(input).some((key) => key !== 'limit' && key !== 'note')) {
    throw new InvalidChange('Unexpected field.');
  }
  if (!Object.hasOwn(input, 'limit') || !('limit' in input)
      || typeof input.limit !== 'number' || !Number.isSafeInteger(input.limit)
      || input.limit < 0 || input.limit > 1000) {
    throw new InvalidChange('limit must be a safe integer from 0 to 1000.');
  }
  const limit = input.limit;
  if (!Object.hasOwn(input, 'note')) return Object.freeze({ limit });
  if (!('note' in input)
      || (input.note !== null && (typeof input.note !== 'string' || input.note.length > 120))) {
    throw new InvalidChange('note must be null or at most 120 UTF-16 code units.');
  }
  return Object.freeze({ limit, note: input.note });
}
```

### `src/quota.ts`

```ts
import type { LimitChange } from './change.js';

export interface QuotaSnapshot {
  readonly limit: number;
  readonly used: number;
  readonly note: string | null;
}

export interface Changed {
  readonly kind: 'changed';
  readonly snapshot: QuotaSnapshot;
}

export interface BelowUsage {
  readonly kind: 'below-usage';
  readonly minimum: number;
}

export type ChangeOutcome = Changed | BelowUsage;

export class Quota {
  #limit: number;
  readonly #used: number;
  #note: string | null = null;

  public constructor(limit: number, used: number) {
    this.validateLimit(limit);
    if (!Number.isSafeInteger(used) || used < 0 || used > limit) {
      throw new RangeError('Invalid current usage.');
    }
    this.#limit = limit;
    this.#used = used;
  }

  public changeLimit(command: LimitChange): ChangeOutcome {
    this.validateLimit(command.limit);
    if (command.limit < this.#used) {
      return { kind: 'below-usage', minimum: this.#used };
    }
    this.#limit = command.limit;
    // Omission keeps the note; null clears it; an empty string is a value.
    if (command.note !== undefined) this.#note = command.note;
    return { kind: 'changed', snapshot: this.snapshot() };
  }

  public snapshot(): QuotaSnapshot {
    return Object.freeze({ limit: this.#limit, used: this.#used, note: this.#note });
  }

  private validateLimit(limit: number): void {
    if (!Number.isSafeInteger(limit) || limit < 0 || limit > 1000) {
      throw new RangeError('Invalid limit.');
    }
  }
}

export function describeChange(outcome: ChangeOutcome): string {
  switch (outcome.kind) {
    case 'changed': return `Limit: ${outcome.snapshot.limit}`;
    case 'below-usage': return `Minimum: ${outcome.minimum}`;
    default: return unreachable(outcome);
  }
}

function unreachable(value: never): never {
  throw new Error(`Unsupported change outcome: ${String(value)}`);
}
```

### `tests/run.ts`

```ts
import assert from 'node:assert/strict';
import test from 'node:test';
import { InvalidChange, parseLimitChange } from '../src/change.js';
import { Quota, describeChange } from '../src/quota.js';

await test('JSON data becomes a named command; absence differs from null/empty string', () => {
  const raw: unknown = JSON.parse('{"limit":4}');
  const command = parseLimitChange(raw);
  assert.equal(Object.hasOwn(command, 'note'), false);
  assert.deepEqual(parseLimitChange({ limit: 4, note: null }), { limit: 4, note: null });
  assert.deepEqual(parseLimitChange({ limit: 4, note: '' }), { limit: 4, note: '' });
  assert.equal(Reflect.set(command, 'limit', 99), false);
});

await test('invalid external representations are rejected at runtime', () => {
  const invalid: readonly unknown[] = [
    null, [], {}, { limit: '4' }, { limit: 1.5 }, { limit: NaN },
    { limit: Infinity }, { limit: -1 }, { limit: 1001 },
    { limit: 4, note: undefined }, { limit: 4, note: false },
    { limit: 4, note: 'x'.repeat(121) }, { limit: 4, admin: true },
  ];
  for (const input of invalid) {
    assert.throws(() => parseLimitChange(input), InvalidChange);
  }
});

await test('valid command can be refused against current usage without partial mutation', () => {
  const quota = new Quota(5, 3);
  assert.equal(describeChange(quota.changeLimit({ limit: 4, note: 'keep' })), 'Limit: 4');
  const before = quota.snapshot();
  const outcome = quota.changeLimit(parseLimitChange({ limit: 2, note: null }));
  assert.equal(describeChange(outcome), 'Minimum: 3');
  assert.deepEqual(quota.snapshot(), before);
  assert.equal(Reflect.set(before, 'limit', 100), false);
  assert.equal(describeChange(quota.changeLimit({ limit: 3 })), 'Limit: 3');
  assert.deepEqual(quota.snapshot(), { limit: 3, used: 3, note: 'keep' });
  assert.deepEqual(before, { limit: 4, used: 3, note: 'keep' });
  quota.changeLimit({ limit: 3, note: '' });
  assert.equal(quota.snapshot().note, '');
  quota.changeLimit({ limit: 3, note: null });
  assert.equal(quota.snapshot().note, null);
});

await test('number annotations do not establish the domain range for direct callers', () => {
  const quota = new Quota(5, 3);
  for (const limit of [-1, 1.5, NaN, Infinity, 1001]) {
    assert.throws(() => quota.changeLimit({ limit }), RangeError);
    assert.deepEqual(quota.snapshot(), { limit: 5, used: 3, note: null });
  }
  assert.throws(() => new Quota(2, 3), RangeError);
  assert.equal(describeChange(new Quota(0, 0).changeLimit({ limit: 0 })), 'Limit: 0');
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
passed. Node reported **4 passing tests**, with zero failed, cancelled or skipped.

The runtime checks cover omitted/null/empty values, thirteen rejected external
representations, refusal without partial mutation, preserved snapshots, direct
invalid quantities and the zero-usage boundary. The stateful refusal is distinct
from invalid input; the description consumer handles both union variants.

Stage verification also compiled isolated invalid consumers with both compilers:
explicit undefined for the optional note (TS2375), readonly write (TS2540),
unknown-to-command assignment, an omitted outcome variant and unchecked indexed
access (TS2322). Those probes intentionally fail and are separate from normal
source/tests, with no `@ts-ignore` or expected-error suppression in these files.

There is no persisted quota, authorization, concurrent writer or transactional
side effect. The readonly interface alone does not create the frozen snapshot;
the explicit runtime operation does. The numeric type alone permits values the
domain rejects. The example's state/limits are illustrative, not a product schema.

The [K10 record](../../../docs/plans/2026-09-21-engineering-practices.md#k10-result-and-verification)
contains final commands, negative-check evidence, delivery checks and limits.
