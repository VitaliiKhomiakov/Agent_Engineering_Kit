# Example: immutable Store state and a memoized OnPush view

Optional illustration of [Store/selectors](../store-selectors.md). The fixture
receives already validated catalog records and performs local filtering; it is
not an HTTP workflow or a server cache. Supply records by dispatching
`catalogReceived`. Error/request ownership belongs to the feature's Effects.
Use the versions supported by the target project; verification is recorded in
the [research note](../../../docs/research/2026-09-29-angular-ngrx-engineering-practices.md).

`catalog-state.ts`:

```ts
import { createAction, createFeature, createReducer, createSelector, on, props } from '@ngrx/store';

export interface Product {
  readonly id: string;
  readonly name: string;
}

export interface CatalogState {
  readonly products: readonly Product[];
  readonly query: string;
}

export interface CatalogViewModel {
  readonly products: readonly Product[];
  readonly query: string;
}

export interface CatalogReceived {
  readonly products: readonly Product[];
}

export interface QueryChanged {
  readonly query: string;
}

export const catalogReceived = createAction('[Catalog API] Received', props<CatalogReceived>());
export const queryChanged = createAction('[Catalog Page] Query Changed', props<QueryChanged>());

const initialState: CatalogState = { products: [], query: '' };

export const catalogFeature = createFeature({
  name: 'catalog',
  reducer: createReducer(
    initialState,
    on(catalogReceived, (state, { products }): CatalogState => ({ ...state, products })),
    on(queryChanged, (state, { query }): CatalogState => ({ ...state, query })),
  ),
});

export const selectVisibleProducts = createSelector(
  catalogFeature.selectProducts,
  catalogFeature.selectQuery,
  (products, query): readonly Product[] => {
    const normalized = query.trim().toLowerCase();
    return normalized
      ? products.filter((product) => product.name.toLowerCase().includes(normalized))
      : products;
  },
);

export const selectCatalogVm = createSelector(
  selectVisibleProducts,
  catalogFeature.selectQuery,
  (products, query): CatalogViewModel => ({ products, query }),
);
```

`catalog-page.ts`:

```ts
import { AsyncPipe } from '@angular/common';
import { ChangeDetectionStrategy, Component, inject } from '@angular/core';
import { Store } from '@ngrx/store';
import { queryChanged, selectCatalogVm } from './catalog-state';

@Component({
  selector: 'app-catalog-page',
  standalone: true,
  imports: [AsyncPipe],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    @if (vm$ | async; as vm) {
      <label>Filter products
        <input #query [value]="vm.query" (input)="filterProducts(query.value)" />
      </label>
      <ul>
        @for (product of vm.products; track product.id) {
          <li>{{ product.name }}</li>
        } @empty {
          <li>No matching products</li>
        }
      </ul>
    }
  `,
})
export class CatalogPage {
  private readonly store = inject(Store);
  protected readonly vm$ = this.store.select(selectCatalogVm);

  protected filterProducts(query: string): void {
    this.store.dispatch(queryChanged({ query }));
  }
}
```

`catalog-config.ts` (minimal root fixture; in an app with an existing Store,
register only the feature at its chosen boundary):

```ts
import type { ApplicationConfig } from '@angular/core';
import { provideState, provideStore } from '@ngrx/store';
import { catalogFeature } from './catalog-state';

export const catalogConfig: ApplicationConfig = {
  providers: [provideStore(), provideState(catalogFeature)],
};
```

The selected inputs are stable; filtering happens in the projector and the
template creates one AsyncPipe subscription. An unrelated root-state change can
reuse the same view-model object. A query change updates the result, preserving
unaffected entity references. `selectSignal(selectCatalogVm)` is an alternative
view API when supported, not a second writable state copy.

When this contract is changed, check a matching/nonmatching query, unchanged
input state, identical result identity after unrelated root changes, and actual
DOM updates after dispatch. Do not test memoization solely through `.projector`.
