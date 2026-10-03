# Example: a reservation form and an independent operation

Read when text validation, Action state and current-state refusal need to be
separated. This optional example supports [form contracts](../forms-contracts.md).

The form accepts decimal positive whole quantities without leading zeroes or
whitespace. It preserves its controlled draft after invalid/failed submissions,
exposes pending state, and reports insufficient stock separately from an uncertain
integration failure. `useActionState` requires React 19; an explicit submit handler
is the simpler compatible option for React 18. Controlled input is intentional:
React's successful Action reset of uncontrolled fields must not erase this draft.

`Inventory` is a deterministic authoritative-operation fixture for tests. Its
synchronous check/decrement is confined to one JavaScript instance. Never ship it
as browser-side authoritative inventory: a real backend validates/authorizes again,
owns atomic storage/concurrency and maps a validated transport contract. No database,
network, durable idempotency or multiple-process guarantee is demonstrated here.
The port's integration owner must retain safe diagnostics. The form does not retry
an ambiguous failure or cancel/roll back a mutation when it unmounts.

## Reproduce in a temporary directory

Verified on 2026-09-21 with Node 24.13.0, React/React DOM 19.3.0, native TypeScript
7.0.2, compatibility TypeScript package 6.0.2 (compiler/API 6.0.3), ESLint 10.11.0,
typescript-eslint 8.70.0, Hooks plugin 7.1.1, Testing Library 16.3.3 and jsdom 30.1.0.
Versions below are an execution baseline, not an instruction to migrate a project.
The Node patch is not a deployment recommendation. The stage retains the resolved
lock; manifest-only reinstall can resolve different transitive packages.

Create the files below outside your project. The shared setup also supports the
[latest-result example](latest-result.md); copy its two files only when running that
example. `npm test` runs both, while `npm run test:form` runs this example alone.
The native compiler owns `tsc`; the compatibility TS API serves typed lint.

```sh
npm install --ignore-scripts --no-audit --no-fund
npm run check
npm run lint
npm run build
npm run test:form
```

## Files

### `package.json`

```json
{
  "name": "af-react-examples",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "engines": {
    "node": ">=24"
  },
  "scripts": {
    "check": "tsc -p tsconfig.json --noEmit",
    "build": "tsc -p tsconfig.json",
    "lint": "eslint src tests --max-warnings=0",
    "test": "npm run test:form && npm run test:latest",
    "test:form": "node --unhandled-rejections=strict --import ./dist/tests/setup.js dist/tests/reservation.test.js",
    "test:latest": "node --unhandled-rejections=strict --import ./dist/tests/setup.js dist/tests/latest.test.js"
  },
  "dependencies": {
    "react": "19.3.0",
    "react-dom": "19.3.0"
  },
  "devDependencies": {
    "@types/react": "19.3.0",
    "@types/react-dom": "19.3.0",
    "@types/node": "24.13.6",
    "@types/jsdom": "30.0.0",
    "jsdom": "30.1.0",
    "@testing-library/react": "16.3.3",
    "@typescript/native": "npm:typescript@7.0.2",
    "typescript": "npm:@typescript/typescript6@6.0.2",
    "eslint": "10.11.0",
    "typescript-eslint": "8.70.0",
    "eslint-plugin-react-hooks": "7.1.1"
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
    "target": "ES2024",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": [
      "ES2024",
      "DOM",
      "DOM.Iterable"
    ],
    "types": [
      "node",
      "react",
      "react-dom"
    ],
    "rootDir": ".",
    "outDir": "dist",
    "noEmitOnError": true,
    "jsx": "react-jsx"
  },
  "include": [
    "src/**/*.ts",
    "src/**/*.tsx",
    "tests/**/*.ts",
    "tests/**/*.tsx"
  ]
}
```

### `eslint.config.mjs`

```js
import tseslint from 'typescript-eslint';
import reactHooks from 'eslint-plugin-react-hooks';

export default tseslint.config(
  { ignores: ['dist/**'] },
  ...tseslint.configs.recommendedTypeChecked,
  {
    files: ['src/**/*.{ts,tsx}', 'tests/**/*.{ts,tsx}'],
    languageOptions: {
      parserOptions: { projectService: true, tsconfigRootDir: import.meta.dirname },
    },
    plugins: { 'react-hooks': reactHooks },
    rules: {
      ...reactHooks.configs.recommended.rules,
      '@typescript-eslint/no-explicit-any': 'error',
      '@typescript-eslint/no-floating-promises': 'error',
      '@typescript-eslint/consistent-type-imports': 'error',
    },
  },
);
```

### `tests/setup.ts`

```ts
import { JSDOM } from 'jsdom';
const dom = new JSDOM('<!doctype html><html><body></body></html>', {
  url: 'https://example.invalid/',
});
Object.defineProperties(globalThis, {
  window: { configurable: true, value: dom.window },
  document: { configurable: true, value: dom.window.document },
  navigator: { configurable: true, value: dom.window.navigator },
  HTMLElement: { configurable: true, value: dom.window.HTMLElement },
  HTMLInputElement: { configurable: true, value: dom.window.HTMLInputElement },
  FormData: { configurable: true, value: dom.window.FormData },
  IS_REACT_ACT_ENVIRONMENT: { configurable: true, writable: true, value: true },
});
```

### `src/reservation.ts`

```ts
export interface ReserveCommand { readonly quantity: number }
export type ReserveResult = { readonly kind: 'reserved'; readonly remaining: number }
  | { readonly kind: 'unavailable' };
export interface ReservationPort {
  reserve(command: ReserveCommand): Promise<ReserveResult>;
}
export type ParsedQuantity = { readonly kind: 'valid'; readonly command: ReserveCommand }
  | { readonly kind: 'invalid' };

export function parseQuantity(value: unknown): ParsedQuantity {
  if (typeof value !== 'string' || !/^[1-9][0-9]*$/.test(value)) {
    return { kind: 'invalid' };
  }
  const quantity = Number(value);
  return Number.isSafeInteger(quantity)
    ? { kind: 'valid', command: { quantity } }
    : { kind: 'invalid' };
}

// Authoritative operation fixture. A deployed backend needs atomic persistence.
export class Inventory implements ReservationPort {
  private available: number;
  constructor(available: number) {
    if (!Number.isSafeInteger(available) || available < 0) {
      throw new RangeError('Invalid inventory');
    }
    this.available = available;
  }
  reserve(command: ReserveCommand): Promise<ReserveResult> {
    if (!Number.isSafeInteger(command.quantity) || command.quantity <= 0) {
      return Promise.reject(new RangeError('Invalid reservation'));
    }
    if (command.quantity > this.available) return Promise.resolve({ kind: 'unavailable' });
    this.available -= command.quantity;
    return Promise.resolve({ kind: 'reserved', remaining: this.available });
  }
}
```

### `src/ReservationForm.tsx`

```tsx
import { useActionState, useId, useState } from 'react';
import type { ReactElement } from 'react';
import { parseQuantity } from './reservation.js';
import type { ReservationPort } from './reservation.js';

export interface ReservationFormProps { readonly service: ReservationPort }
type Outcome = { readonly kind: 'idle' } | { readonly kind: 'invalid' }
  | { readonly kind: 'unavailable' } | { readonly kind: 'failed' }
  | { readonly kind: 'reserved'; readonly remaining: number };

export function ReservationForm({ service }: ReservationFormProps): ReactElement {
  const id = useId();
  const [draft, setDraft] = useState('1');
  const [outcome, action, pending] = useActionState<Outcome, FormData>(
    async (_previous, data): Promise<Outcome> => {
      const parsed = parseQuantity(data.get('quantity'));
      if (parsed.kind === 'invalid') return parsed;
      try {
        return await service.reserve(parsed.command);
      } catch {
        // The integration owner retains diagnostics; do not expose raw errors.
        return { kind: 'failed' };
      }
    },
    { kind: 'idle' },
  );
  const invalid = outcome.kind === 'invalid';
  return (
    <form action={action} aria-label="Reserve inventory" aria-busy={pending}>
      <label htmlFor={id}>Quantity</label>
      <input id={id} name="quantity" inputMode="numeric" value={draft}
        onChange={event => setDraft(event.currentTarget.value)} disabled={pending}
        aria-invalid={invalid} aria-describedby={invalid ? `${id}-error` : undefined} />
      <button type="submit" disabled={pending}>Reserve</button>
      {invalid && <p id={`${id}-error`} role="alert">Enter a positive whole quantity.</p>}
      {outcome.kind === 'unavailable' && <p role="alert">Insufficient stock.</p>}
      {outcome.kind === 'failed' && <p role="alert">Reservation could not be confirmed.</p>}
      <p role="status">{pending ? 'Reserving…' : outcome.kind === 'reserved'
        ? `Reserved. Remaining: ${outcome.remaining}` : ''}</p>
    </form>
  );
}
```

### `tests/reservation.test.tsx`

```tsx
import assert from 'node:assert/strict';
import { afterEach, test } from 'node:test';
import { StrictMode } from 'react';
import { act, cleanup, fireEvent, render, screen } from '@testing-library/react';
import { ReservationForm } from '../src/ReservationForm.js';
import { Inventory, parseQuantity } from '../src/reservation.js';
import type { ReserveResult } from '../src/reservation.js';

afterEach(cleanup);

function submit(quantity: string): void {
  fireEvent.change(screen.getByLabelText('Quantity'), { target: { value: quantity } });
  fireEvent.submit(screen.getByRole('form', { name: 'Reserve inventory' }));
}

await test('representation rules reject malformed input without spending stock', async () => {
  const service = new Inventory(3);
  render(<StrictMode><ReservationForm service={service} /></StrictMode>);
  for (const value of ['', '0', '-1', '1.5', ' 2', '02', '1e2', '9007199254740992']) {
    submit(value);
    await screen.findByText('Enter a positive whole quantity.');
    const input = screen.getByLabelText('Quantity');
    assert.ok(input instanceof HTMLInputElement);
    assert.equal(input.value, value);
    assert.equal(input.getAttribute('aria-invalid'), 'true');
    assert.equal(document.getElementById(input.getAttribute('aria-describedby') ?? '')?.textContent,
      'Enter a positive whole quantity.');
  }
  assert.deepEqual(parseQuantity(null), { kind: 'invalid' });
  assert.deepEqual(parseQuantity(new FormData()), { kind: 'invalid' });
  assert.deepEqual(await service.reserve({ quantity: 3 }), { kind: 'reserved', remaining: 0 });
});

await test('current stock refusal leaves stock available for a later valid command', async () => {
  const service = new Inventory(3);
  await service.reserve({ quantity: 2 }); // Another caller already consumed stock.
  render(<StrictMode><ReservationForm service={service} /></StrictMode>);
  submit('2');
  await screen.findByText('Insufficient stock.');
  submit('1');
  await screen.findByText('Reserved. Remaining: 0');
  assert.equal(screen.queryByRole('alert'), null);
});

await test('pending and safe failure feedback retain the controlled draft', async () => {
  const work = Promise.withResolvers<ReserveResult>();
  render(<ReservationForm service={{ reserve: () => work.promise }} />);
  submit('2');
  await screen.findByText('Reserving…');
  assert.equal(screen.getByRole('button', { name: 'Reserve' }).hasAttribute('disabled'), true);
  await act(async () => {
    work.reject(new Error('private backend details'));
    await Promise.allSettled([work.promise]);
  });
  await screen.findByText('Reservation could not be confirmed.');
  assert.equal(screen.queryByText(/private backend/), null);
  assert.equal(screen.getByRole('button', { name: 'Reserve' }).hasAttribute('disabled'), false);
  const input = screen.getByLabelText('Quantity');
  assert.ok(input instanceof HTMLInputElement);
  assert.equal(input.value, '2');
});

await test('direct callers cannot bypass the operation invariant', async () => {
  assert.throws(() => new Inventory(-1), RangeError);
  const service = new Inventory(2);
  for (const quantity of [0, -1, 0.5, Number.NaN, Number.POSITIVE_INFINITY]) {
    await assert.rejects(service.reserve({ quantity }), RangeError);
  }
  assert.deepEqual(await service.reserve({ quantity: 3 }), { kind: 'unavailable' });
  assert.deepEqual(await service.reserve({ quantity: 2 }), { kind: 'reserved', remaining: 0 });
});
```

## Observed evidence and limits

Four cases passed with zero failures/cancellations/skips: eight malformed textual
representations preserve stock and draft, stateful refusal permits a smaller later
command, pending/rejected work shows safe feedback, and direct calls still enforce
the operation invariant. Strict checking, typed lint plus Hooks rules, and emitted
JS execution passed. Tests query labels/roles and actual React DOM output in jsdom.
They do not establish browser layout, native keyboard/form behavior, screen-reader
announcements, focus movement, duplicate-submit idempotency or backend correctness.
There is no claim that disabling the button prevents all repeated commands.
