# JavaScript example: parsed input and current business state

Read this example when deciding where a JSON contract ends and mutable business
behavior begins. The [values/state section](../values-state.md) owns the rules.

A plain `ReservationInput` describes a request. Parsing rejects malformed or
unsupported representations and produces a fresh frozen object. A `Capacity`
instance owns private state and refuses an unavailable reservation before mutation.
Valid input can still be refused; direct callers cannot bypass the invariant.
No DTO class, factory, dependency container or repository is needed.

The deliberately small contract requires both fields, including an explicit
nullable `note`, rejects unknown fields, and accepts numeric units from 1 to 1000.
The 4096/120 limits count UTF-16 code units, not bytes or grapheme clusters; a real
transport must enforce its own byte/body limits. `Object.hasOwn` checks presence;
the additional `in` check lets this checker narrow the unknown property without
a cast. Input comes from JSON text, not arbitrary objects with getters/proxies.

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
  "name": "af-javascript-input-state",
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

### `src/reservation-input.js`

```js
/**
 * @typedef {object} ReservationInput
 * @property {number} units
 * @property {string | null} note
 */

export class InputError extends Error {
  name = 'InputError';
}

/**
 * Decode a small JSON message. The caller owns transport byte limits.
 * @param {unknown} text
 * @returns {Readonly<ReservationInput>}
 */
export function parseReservation(text) {
  if (typeof text !== 'string' || text.length > 4096) {
    throw new InputError('Expected a bounded JSON string.');
  }
  /** @type {unknown} */
  let value;
  try {
    value = JSON.parse(text);
  } catch (cause) {
    throw new InputError('Invalid JSON.', { cause });
  }
  if (typeof value !== 'object' || value === null || Array.isArray(value)) {
    throw new InputError('Expected an object.');
  }
  if (Object.keys(value).some((key) => key !== 'units' && key !== 'note')) {
    throw new InputError('Unexpected field.');
  }
  if (!Object.hasOwn(value, 'units') || !('units' in value)
      || typeof value.units !== 'number' || !Number.isSafeInteger(value.units)
      || value.units < 1 || value.units > 1000) {
    throw new InputError('units must be an integer between 1 and 1000.');
  }
  if (!Object.hasOwn(value, 'note') || !('note' in value)
      || (value.note !== null && (typeof value.note !== 'string' || value.note.length > 120))) {
    throw new InputError('note must be present, null or a string of at most 120 UTF-16 units.');
  }
  return Object.freeze({ units: value.units, note: value.note });
}
```

### `src/capacity.js`

```js
/**
 * @typedef {object} CapacitySnapshot
 * @property {number} remaining
 */

export class CapacityExceeded extends Error {
  name = 'CapacityExceeded';
}

export class Capacity {
  /** @type {number} */
  #remaining;

  /** @param {number} initial */
  constructor(initial) {
    if (!Number.isSafeInteger(initial) || initial < 0 || initial > 1000) {
      throw new RangeError('Invalid initial capacity.');
    }
    this.#remaining = initial;
  }

  /**
   * This business invariant also protects direct, non-transport callers.
   * @param {number} units
   * @returns {Readonly<CapacitySnapshot>}
   */
  reserve(units) {
    if (!Number.isSafeInteger(units) || units < 1 || units > 1000) {
      throw new RangeError('Invalid reservation units.');
    }
    if (units > this.#remaining) {
      throw new CapacityExceeded('Insufficient capacity.');
    }
    this.#remaining -= units;
    return this.snapshot();
  }

  /** @returns {Readonly<CapacitySnapshot>} */
  snapshot() {
    return Object.freeze({ remaining: this.#remaining });
  }
}
```

### `tests/reservation.test.js`

```js
import assert from 'node:assert/strict';
import test from 'node:test';
import { InputError, parseReservation } from '../src/reservation-input.js';
import { Capacity, CapacityExceeded } from '../src/capacity.js';

test('owned input preserves explicit null and empty string', () => {
  assert.deepEqual(parseReservation('{"units":2,"note":null}'), { units: 2, note: null });
  const input = parseReservation('{"units":2,"note":""}');
  assert.equal(input.note, '');
  assert.equal(Reflect.set(input, 'units', 999), false);
  assert.equal(input.units, 2);
});

/** @type {ReadonlyArray<readonly [string, unknown]>} */
const invalid = [
  ['non-string', 12],
  ['too large', ' '.repeat(4097)],
  ['malformed', '{'],
  ['null root', 'null'],
  ['array root', '[]'],
  ['missing units', '{"note":null}'],
  ['missing nullable field', '{"units":2}'],
  ['numeric string', '{"units":"2","note":null}'],
  ['fraction', '{"units":1.5,"note":null}'],
  ['unsafe integer', '{"units":9007199254740993,"note":null}'],
  ['non-finite number', '{"units":1e999,"note":null}'],
  ['zero', '{"units":0,"note":null}'],
  ['invalid note', '{"units":2,"note":false}'],
  ['long note', JSON.stringify({ units: 2, note: 'x'.repeat(121) })],
  ['unknown field', '{"units":2,"note":null,"admin":true}'],
  ['prototype key', '{"units":2,"note":null,"__proto__":{"admin":true}}'],
];
for (const [name, payload] of invalid) {
  test(`reject ${name}`, () => assert.throws(() => parseReservation(payload), InputError));
}

test('JSON syntax error retains its cause', () => {
  assert.throws(() => parseReservation('{'),
    /** @param {unknown} failure */
    (failure) => failure instanceof InputError && failure.cause instanceof SyntaxError);
});

test('valid input can still fail against current business state without mutation', () => {
  const capacity = new Capacity(3);
  const before = capacity.snapshot();
  const input = parseReservation('{"units":2,"note":null}');
  assert.deepEqual(capacity.reserve(input.units), { remaining: 1 });
  assert.throws(() => capacity.reserve(input.units), CapacityExceeded);
  assert.deepEqual(capacity.snapshot(), { remaining: 1 });
  assert.deepEqual(before, { remaining: 3 });
  assert.equal(Reflect.set(before, 'remaining', 1000), false);
  assert.deepEqual(capacity.reserve(1), { remaining: 0 });
});

test('direct callers cannot bypass the business invariant', () => {
  const capacity = new Capacity(3);
  for (const units of [0, -1, 1.5, NaN, Infinity, Number.MAX_SAFE_INTEGER + 1]) {
    assert.throws(() => capacity.reserve(units), RangeError);
    assert.deepEqual(capacity.snapshot(), { remaining: 3 });
  }
  assert.throws(() => new Capacity(-1), RangeError);
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
tests/reservation.test.js` directly exposed **20 passing scenarios**, with no failed,
cancelled or skipped tests. An intentional failing probe returned exit 1 through
both forms, so the aggregate was not treated as a detailed scenario count.

The checks cover explicit null/empty string, sixteen invalid-input cases,
syntax-error cause, refusal without mutation, snapshot independence, exact
exhaustion and invalid direct calls. All frozen fields in this example are
primitive; this does not demonstrate deep immutability of arbitrary objects.

Capacity is local process state with synchronous transitions. No database,
concurrent writer, authorization system, duplicate-request policy or transaction
is implemented. A persistent reservation needs its own concurrency/transaction
contract. A parsed `note` is data, not proof it is safe at every output sink.

The [K09 record](../../../docs/plans/2026-09-21-engineering-practices.md#k09-result-and-verification)
contains verification commands, delivery checks and limits. This example does
not authorize replacing the consumer project's runtime, checker or test framework.
