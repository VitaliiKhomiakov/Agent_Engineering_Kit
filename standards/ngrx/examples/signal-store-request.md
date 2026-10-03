# Example: component-scoped SignalStore with replaceable reads

Optional illustration of [SignalStore](../signal-store.md). Each submitted search
replaces the previous read immediately; this is an explicit-submit search, not a
debounced keystroke search. The host supplies `PRODUCT_SEARCH` using its validated
HTTP adapter. The example deliberately does not own authentication or an HTTP cache.
The adapter emits once then completes, or errors; it does not complete empty.

`product-search.ts`:

```ts
import { InjectionToken } from '@angular/core';
import type { Observable } from 'rxjs';

export interface Product {
  readonly id: string;
  readonly name: string;
}

export interface ProductSearch {
  search(query: string): Observable<readonly Product[]>;
}

export const PRODUCT_SEARCH = new InjectionToken<ProductSearch>('PRODUCT_SEARCH');
```

`product-search-store.ts`:

```ts
import { computed, inject } from '@angular/core';
import { patchState, signalStore, withComputed, withMethods, withState } from '@ngrx/signals';
import { rxMethod } from '@ngrx/signals/rxjs-interop';
import { tapResponse } from '@ngrx/operators';
import { defer, pipe, switchMap } from 'rxjs';
import { PRODUCT_SEARCH } from './product-search';
import type { Product } from './product-search';

export type SearchStatus = 'idle' | 'loading' | 'success' | 'error';

export interface SearchState {
  readonly products: readonly Product[];
  readonly status: SearchStatus;
  readonly message: string | null;
}

const initialState: SearchState = { products: [], status: 'idle', message: null };

export const ProductSearchStore = signalStore(
  withState(initialState),
  withComputed(({ products }) => ({ count: computed(() => products().length) })),
  withMethods((store, api = inject(PRODUCT_SEARCH)) => ({
    search: rxMethod<string>(
      pipe(
        switchMap((query) =>
          defer(() => {
            // switchMap has cancelled the previous inner subscription first.
            patchState(store, { status: 'loading', message: null, products: [] });
            return api.search(query.trim());
          }).pipe(
            tapResponse({
              next: (products): void => {
                patchState(store, { products, status: 'success' });
              },
              error: (_error: unknown): void => {
                patchState(store, { status: 'error', message: 'Search failed. Try again.' });
              },
            }),
          ),
        ),
      ),
    ),
  })),
);
```

`product-search-page.ts`:

```ts
import { ChangeDetectionStrategy, Component, inject } from '@angular/core';
import { ProductSearchStore } from './product-search-store';

@Component({
  selector: 'app-product-search',
  standalone: true,
  providers: [ProductSearchStore],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <form (submit)="$event.preventDefault(); searchProducts(query.value)">
      <label>Search products <input #query type="search" /></label>
      <button type="submit">Search</button>
    </form>
    <section aria-live="polite" [attr.aria-busy]="store.status() === 'loading'">
      @switch (store.status()) {
        @case ('loading') { <p>Searching…</p> }
        @case ('error') { <p>{{ store.message() }}</p> }
        @case ('success') {
          <p>{{ store.count() }} products</p>
          <ul>
            @for (product of store.products(); track product.id) {
              <li>{{ product.name }}</li>
            } @empty { <li>No matching products</li> }
          </ul>
        }
      }
    </section>
  `,
})
export class ProductSearchPage {
  protected readonly store = inject(ProductSearchStore);

  protected searchProducts(query: string): void {
    this.store.search(query);
  }
}
```

Provide the adapter token in the host's injector. No root store is created;
each component gets its own instance. A new search cancels the old subscription,
errors become view state, and another submit can retry the same query. There is
no global loading cleanup racing with the next request. Imperative static calls
preserve explicit commands; a reactive signal input would have different timing.

Check two out-of-order reads (only the latest wins), a failure followed by a
successful retry, separate store instances, subscription cleanup on destruction,
and an OnPush template update. This cancellation policy must not be copied to a
payment/save operation that requires every command to finish. See the
[research note](../../../docs/research/2026-09-29-angular-ngrx-engineering-practices.md)
for the exact executed checks and their limits.
