# Example: publish only the current integration result

Read when a small client-only integration needs explicit Effect cleanup and stale
result handling. This optional example supports [effects](../effects-integrations.md).
Prefer the accepted loader/query cache when it already supplies this behavior.

The port returns validated, unique result labels used here as stable item IDs;
real data usually carries separate IDs and labels. The composition owner provides
a stable service instance. If it intentionally replaces that instance, the UI hides
old-owner data until the replacement settles. Changing the query remounts the
private viewing session, intentionally clearing its state. This reset would be
wrong for a child draft that must survive input changes; use an explicit state
owner and input-keyed results for that case.

Each setup owns an AbortController and a publication guard. Even a port that ignores
abort cannot publish after its setup is retired. Both synchronous throws and rejected
promises become a safe current error, while obsolete failures stay handled. The
integration owner retains diagnostics; this example is not a logging implementation.
Cancellation signals are not evidence of remote work termination or rollback.

## Reproduce

Use the pinned package/configuration and `tests/setup.ts` from the
[form example](reservation-form.md#reproduce-in-a-temporary-directory), then add the
two files below. `npm run test:latest` runs just this example; `npm test` runs both
when all example files are present. React 19.3.0 was executed; the component uses
ordinary Effects/state rather than requiring Action or Effect Event APIs.

```sh
npm run check
npm run lint
npm run build
npm run test:latest
```

## Files

### `src/LatestResult.tsx`

```tsx
import { useEffect, useState } from 'react';
import type { ReactElement } from 'react';

export interface SearchPort {
  search(query: string, signal: AbortSignal): Promise<readonly string[]>;
}
export interface LatestResultProps {
  readonly query: string;
  readonly service: SearchPort;
}
type SearchState = { readonly kind: 'loading' }
  | { readonly kind: 'ready'; readonly service: SearchPort; readonly rows: readonly string[] }
  | { readonly kind: 'failed'; readonly service: SearchPort };

export function LatestResult({ query, service }: LatestResultProps): ReactElement {
  // A new input starts a new viewing session; it also discards descendant state.
  return <ResultSession key={query} query={query} service={service} />;
}

function ResultSession({ query, service }: LatestResultProps): ReactElement {
  const [state, setState] = useState<SearchState>({ kind: 'loading' });
  useEffect(() => {
    let active = true;
    const controller = new AbortController();
    async function load(): Promise<void> {
      try {
        const rows = await service.search(query, controller.signal);
        if (active) setState({ kind: 'ready', service, rows });
      } catch {
        if (active) setState({ kind: 'failed', service });
      }
    }
    // load handles both synchronous throws and promise rejection from the port.
    void load();
    return () => {
      active = false;
      controller.abort();
    };
  }, [query, service]);
  if (state.kind === 'loading' || state.service !== service) return <p role="status">Loading {query}…</p>;
  if (state.kind === 'failed') return <p role="alert">Search failed for {query}.</p>;
  if (state.rows.length === 0) return <p role="status">No results for {query}.</p>;
  return <ul aria-label={`Results for ${query}`}>
    {state.rows.map(row => <li key={row}>{row}</li>)}
  </ul>;
}
```

### `tests/latest.test.tsx`

```tsx
import assert from 'node:assert/strict';
import { afterEach, test } from 'node:test';
import { StrictMode } from 'react';
import { act, cleanup, render, screen } from '@testing-library/react';
import { LatestResult } from '../src/LatestResult.js';
import type { SearchPort } from '../src/LatestResult.js';

afterEach(cleanup);
interface Request {
  readonly query: string;
  readonly signal: AbortSignal;
  readonly result: PromiseWithResolvers<readonly string[]>;
}
class SearchFixture implements SearchPort {
  readonly requests: Request[] = [];
  search(query: string, signal: AbortSignal): Promise<readonly string[]> {
    const result = Promise.withResolvers<readonly string[]>();
    this.requests.push({ query, signal, result });
    return result.promise; // Deliberately ignores abort; publication still must be safe.
  }
  current(): Request {
    const request = this.requests.at(-1);
    assert.ok(request);
    return request;
  }
}

await test('obsolete success and failure cannot overwrite the current query', async () => {
  const service = new SearchFixture();
  const view = render(<StrictMode><LatestResult query="old" service={service} /></StrictMode>);
  const old = [...service.requests];
  view.rerender(<StrictMode><LatestResult query="new" service={service} /></StrictMode>);
  assert.ok(old.every(request => request.signal.aborted));
  await act(async () => {
    service.current().result.resolve(['new row']);
    await Promise.allSettled([service.current().result.promise]);
  });
  assert.ok(screen.getByRole('list', { name: 'Results for new' }));
  await act(async () => {
    old.forEach((request, index) => index % 2 === 0
      ? request.result.resolve(['obsolete row'])
      : request.result.reject(new Error('obsolete failure')));
    await Promise.allSettled(old.map(request => request.result.promise));
  });
  assert.ok(screen.getByText('new row'));
  assert.equal(screen.queryByText('obsolete row'), null);
  assert.equal(screen.queryByRole('alert'), null);
  view.unmount();
  assert.ok(service.requests.every(request => request.signal.aborted));
});

await test('switching input hides old results immediately and owns empty/failure states', async () => {
  const service = new SearchFixture();
  const view = render(<LatestResult query="first" service={service} />);
  await act(async () => {
    service.current().result.resolve(['first row']);
    await Promise.allSettled([service.current().result.promise]);
  });
  view.rerender(<LatestResult query="empty" service={service} />);
  assert.equal(screen.queryByText('first row'), null);
  assert.ok(screen.getByText('Loading empty…'));
  await act(async () => {
    service.current().result.resolve([]);
    await Promise.allSettled([service.current().result.promise]);
  });
  assert.ok(screen.getByText('No results for empty.'));
  view.rerender(<LatestResult query="broken" service={service} />);
  await act(async () => {
    service.current().result.reject(new Error('private failure'));
    await Promise.allSettled([service.current().result.promise]);
  });
  assert.equal(screen.getByRole('alert').textContent, 'Search failed for broken.');
});

await test('Strict Mode cleanup invalidates the earlier setup with the same input', async () => {
  const service = new SearchFixture();
  const view = render(<StrictMode><LatestResult query="same" service={service} /></StrictMode>);
  const obsolete = service.requests.filter(request => request.signal.aborted);
  assert.ok(obsolete.length > 0);
  await act(async () => {
    service.current().result.resolve(['current row']);
    await Promise.allSettled([service.current().result.promise]);
  });
  await act(async () => {
    obsolete.forEach(request => request.result.resolve(['obsolete setup']));
    await Promise.allSettled(obsolete.map(request => request.result.promise));
  });
  assert.ok(screen.getByText('current row'));
  assert.equal(screen.queryByText('obsolete setup'), null);
  view.unmount();
  assert.ok(service.current().signal.aborted);
});

await test('unmount aborts pending work and handles its later rejection', async () => {
  const service = new SearchFixture();
  const view = render(<LatestResult query="gone" service={service} />);
  const request = service.current();
  view.unmount();
  assert.ok(request.signal.aborted);
  await act(async () => {
    request.result.reject(new Error('late failure'));
    await Promise.allSettled([request.result.promise]);
  });
  assert.equal(document.body.textContent, '');
});

await test('replacing the integration hides the previous owner data before settlement', async () => {
  const first = new SearchFixture();
  const second = new SearchFixture();
  const view = render(<LatestResult query="same" service={first} />);
  await act(async () => {
    first.current().result.resolve(['first owner']);
    await first.current().result.promise;
  });
  view.rerender(<LatestResult query="same" service={second} />);
  assert.equal(screen.queryByText('first owner') === null, true);
  assert.ok(screen.getByText('Loading same…'));
  assert.ok(first.current().signal.aborted);
  await act(async () => {
    second.current().result.resolve(['second owner']);
    await second.current().result.promise;
  });
  assert.ok(screen.getByText('second owner'));
});
```

## Observed evidence and limits

Five cases passed: obsolete success/failure, immediate input reset with empty/current
error states, same-input Strict Mode cleanup, unmount/late rejection, and replacement
of the integration owner. The final case reproduced stale owner data with the
identity check removed, then passed with the fix. Strict TS, typed/Hooks lint and
emitted JS execution passed on the exact blocks above.

Strict Mode replay is observed in this development/root fixture, not a universal
request-count promise. The fake intentionally ignores cancellation to challenge the
publication contract. No real request, cache/deduplication, retries, Suspense, SSR,
hydration, browser layout or React 18 runtime was exercised. Key reset discards child
state and can affect focus; the example has no editable descendants. This is not a
general query library, a benchmark or a backend cancellation guarantee.
