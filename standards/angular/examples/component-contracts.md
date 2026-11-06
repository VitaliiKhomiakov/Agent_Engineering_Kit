# Example: component contracts and composed behavior

Use this optional fixture for [component queries and projection](../components.md)
and [directive composition/lifetime](../directives.md). It is an independently
authored contract example, not an application scaffold or a required test runner.
The [dated evidence](../../../docs/research/2026-11-06-angular-component-contracts.md)
records actual checks and their limits.

## Scenario and ownership

A consumer opens a details panel and owns its expanded state. The panel exposes
its host directive's `enabled` input as `expanded` and `dismissed` output as
`closeRequested`. Closing emits intent; the consumer updates state and restores
focus. The panel's conditional close button is an optional view query; the
consumer's unconditional trigger and panel use required queries after rendering.

A marker directive identifies an optional projected action. The consumer's `@if`
creates/removes that action; the panel's static `ng-content` slot does not control
its lifetime. Hiding the panel preserves projected content. Absence displays a
fallback, and recreating either queried control must not reuse a stale element.

Native buttons supply the interaction surface. Focus moves to the close control
after rendering and returns to the trigger on dismissal. This is an expandable
section, not a modal dialog or a complete design-system widget. No stylesheet is
needed for the fixture; authored application styles still follow the SCSS owner.

The manual listener intentionally illustrates browser-adapter resource ownership:
`afterNextRender` owns its setup timing and `DestroyRef` removes the listener.
For an ordinary synchronous host event without an adapter lifecycle, prefer
Angular `host` metadata as the directive rules describe. Stopping an output
subscription alone would not demonstrate removal of a manually created listener.

## Setup and checks

Extract the eight named files using the [maintenance procedure](../../../docs/maintenance/verification.md#reproduce-an-affected-executable-example)
with selector `angular`. Inside that temporary directory, using Node 24.13.0 and
npm 11.6.2 for the recorded run:

```sh
npm install --ignore-scripts --engine-strict --no-audit --no-fund
npm run build
npm test
```

Keep optional dependencies enabled: esbuild uses its platform binary package even
when install scripts are disabled. Retain the generated lockfile and resolved
package versions with the run evidence; a new installation may resolve different
transitive versions. Do not install this manifest at the AEK root or replace a
consuming application's established build/test toolchain.

`build` first runs Angular 20.3.0 `ngc` with strict template checks, then bundles
its emitted local test modules for Node. Angular's generated cross-file imports
can omit extensions; the bundler resolves them without rewriting emitted code.
Package imports and the DOM setup remain external. This is not an Angular CLI
application build, style build, browser bundle or package-publication check.

The Node runner uses one process (`--test-isolation=none`) for this single suite;
TestBed resets between cases. DOM setup loads before the test imports. Explicit
zoneless scheduling and `whenStable()` exercise signal/template-event/render
notifications without forced `detectChanges()` or arbitrary waits. The six cases
cover absence and recreation, intent propagation, projected-content ownership,
focus, ignored keys and listener destruction. The cleanup case retains an enabled
host after destruction and checks whether Escape was consumed, independently of
Angular's output-subscription cleanup.

jsdom evidence covers DOM state, synthetic events and focus bookkeeping. It does
not establish browser keyboard defaults, layout, assistive-technology behavior,
visual accessibility, SSR or hydration. Run the consuming project's affected
checks when those contracts matter.

### `package.json`

```json
{
  "name": "aek-angular-component-contracts",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "engines": {
    "node": "^24.0.0"
  },
  "scripts": {
    "build": "ngc -p tsconfig.json && esbuild dist/tests/component-contracts.test.js --bundle --platform=node --format=esm --packages=external --external:./setup.js --outfile=dist/tests/component-contracts.test.bundle.js",
    "test": "node --unhandled-rejections=strict --import ./dist/tests/setup.js --test-isolation=none --test dist/tests/component-contracts.test.bundle.js"
  },
  "dependencies": {
    "@angular/common": "20.3.0",
    "@angular/compiler": "20.3.0",
    "@angular/core": "20.3.0",
    "@angular/platform-browser": "20.3.0",
    "rxjs": "7.8.2",
    "tslib": "2.8.1"
  },
  "devDependencies": {
    "@angular/compiler-cli": "20.3.0",
    "@types/jsdom": "21.1.7",
    "@types/node": "24.13.6",
    "jsdom": "26.1.0",
    "typescript": "5.9.3",
    "esbuild": "0.25.10"
  }
}
```

### `tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "types": ["node"],
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,
    "noImplicitReturns": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "experimentalDecorators": true,
    "skipLibCheck": false,
    "rootDir": ".",
    "outDir": "dist"
  },
  "angularCompilerOptions": {
    "strictTemplates": true,
    "compilationMode": "full"
  },
  "include": ["src/**/*.ts", "tests/**/*.ts"]
}
```

### `src/escape-dismiss.directive.ts`

```ts
import { afterNextRender, DestroyRef, Directive, ElementRef, inject, input, output } from '@angular/core';

@Directive({ selector: '[aekEscapeDismiss]', standalone: true })
export class EscapeDismissDirective {
  readonly enabled = input(false);
  readonly dismissed = output<void>();

  private readonly host = inject<ElementRef<HTMLElement>>(ElementRef);
  private readonly destroyRef = inject(DestroyRef);

  constructor() {
    afterNextRender((): void => {
      const element = this.host.nativeElement;
      const onKeydown = (event: KeyboardEvent): void => {
        if (!this.enabled() || event.key !== 'Escape' || event.defaultPrevented) {
          return;
        }
        event.preventDefault();
        this.requestDismissal();
      };
      element.addEventListener('keydown', onKeydown);
      this.destroyRef.onDestroy((): void => {
        element.removeEventListener('keydown', onKeydown);
      });
    });
  }

  requestDismissal(): void {
    if (this.enabled()) {
      this.dismissed.emit();
    }
  }
}
```

### `src/panel-action.directive.ts`

```ts
import { Directive } from '@angular/core';

@Directive({ selector: '[aekPanelAction]', standalone: true })
export class PanelActionDirective {}
```

### `src/details-panel.ts`

```ts
import {
  ChangeDetectionStrategy, Component, contentChild, inject, input, viewChild,
} from '@angular/core';
import type { ElementRef } from '@angular/core';
import { EscapeDismissDirective } from './escape-dismiss.directive.js';
import { PanelActionDirective } from './panel-action.directive.js';

@Component({
  selector: 'aek-details-panel',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  hostDirectives: [{
    directive: EscapeDismissDirective,
    inputs: ['enabled: expanded'],
    outputs: ['dismissed: closeRequested'],
  }],
  template: `
    <section [hidden]="!expanded()" [attr.aria-label]="title()">
      <h2>{{ title() }}</h2>
      <ng-content select="[aekPanelAction]" />
      @if (!action()) {
        <p data-state="no-action">No additional action.</p>
      }
      @if (expanded()) {
        <button #closeButton type="button" (click)="requestClose()">Close details</button>
      }
    </section>
  `,
})
export class DetailsPanelComponent {
  readonly title = input.required<string>();

  private readonly dismiss = inject(EscapeDismissDirective);
  private readonly closeButton = viewChild<ElementRef<HTMLButtonElement>>('closeButton');
  protected readonly expanded = this.dismiss.enabled;
  protected readonly action = contentChild(PanelActionDirective);

  /** Returns false while the conditional close control is absent. Call after rendering. */
  focusCloseButton(): boolean {
    const button = this.closeButton();
    if (!button) {
      return false;
    }
    button.nativeElement.focus();
    return true;
  }

  protected requestClose(): void {
    this.dismiss.requestDismissal();
  }
}
```

### `tests/fixture-host.ts`

```ts
import {
  afterNextRender, ChangeDetectionStrategy, Component, inject, Injector,
  signal, viewChild,
} from '@angular/core';
import type { ElementRef } from '@angular/core';
import { DetailsPanelComponent } from '../src/details-panel.js';
import { PanelActionDirective } from '../src/panel-action.directive.js';

@Component({
  selector: 'aek-fixture-host',
  standalone: true,
  imports: [DetailsPanelComponent, PanelActionDirective],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <button #trigger type="button" aria-controls="delivery-details"
      [attr.aria-expanded]="expanded()" (click)="openDetails()">Show details</button>
    <aek-details-panel id="delivery-details" title="Delivery details"
      [expanded]="expanded()" (closeRequested)="closeDetails()">
      @if (includeAction()) {
        <button type="button" aekPanelAction (click)="requestReceipt()">Download receipt</button>
      }
    </aek-details-panel>
    <p data-state="receipt-count">{{ receiptCount() }}</p>
  `,
})
export class FixtureHostComponent {
  readonly expanded = signal(false);
  readonly includeAction = signal(true);
  readonly closeCount = signal(0);
  readonly receiptCount = signal(0);
  readonly panel = viewChild.required(DetailsPanelComponent);

  private readonly trigger = viewChild.required<ElementRef<HTMLButtonElement>>('trigger');
  private readonly injector = inject(Injector);

  openDetails(): void {
    this.expanded.set(true);
    afterNextRender((): void => {
      this.panel().focusCloseButton();
    }, { injector: this.injector });
  }

  closeDetails(): void {
    this.expanded.set(false);
    this.closeCount.update((count): number => count + 1);
    this.trigger().nativeElement.focus();
  }

  requestReceipt(): void {
    this.receiptCount.update((count): number => count + 1);
  }
}
```

### `tests/setup.ts`

```ts
import '@angular/compiler';
import { JSDOM } from 'jsdom';

const dom = new JSDOM('<!doctype html><html><body></body></html>', {
  url: 'http://localhost/',
  pretendToBeVisual: true,
});

Object.defineProperties(globalThis, {
  window: { value: dom.window, configurable: true },
  document: { value: dom.window.document, configurable: true },
  Node: { value: dom.window.Node, configurable: true },
  Element: { value: dom.window.Element, configurable: true },
  HTMLElement: { value: dom.window.HTMLElement, configurable: true },
  HTMLButtonElement: { value: dom.window.HTMLButtonElement, configurable: true },
  Event: { value: dom.window.Event, configurable: true },
  KeyboardEvent: { value: dom.window.KeyboardEvent, configurable: true },
  requestAnimationFrame: { value: dom.window.requestAnimationFrame.bind(dom.window), configurable: true },
  cancelAnimationFrame: { value: dom.window.cancelAnimationFrame.bind(dom.window), configurable: true },
});

export function closeDom(): void {
  dom.window.close();
}
```

### `tests/component-contracts.test.ts`

```ts
import assert from 'node:assert/strict';
import { after, afterEach, beforeEach, test } from 'node:test';
import { destroyPlatform, provideZonelessChangeDetection } from '@angular/core';
import { TestBed } from '@angular/core/testing';
import type { ComponentFixture } from '@angular/core/testing';
import { BrowserTestingModule, platformBrowserTesting } from '@angular/platform-browser/testing';
import { FixtureHostComponent } from './fixture-host.js';
import { closeDom } from './setup.js';

TestBed.initTestEnvironment(BrowserTestingModule, platformBrowserTesting(), {
  teardown: { destroyAfterEach: true },
});

let fixture: ComponentFixture<FixtureHostComponent>;

beforeEach(async (): Promise<void> => {
  TestBed.configureTestingModule({
    imports: [FixtureHostComponent],
    providers: [provideZonelessChangeDetection()],
  });
  fixture = TestBed.createComponent(FixtureHostComponent);
  await fixture.whenStable();
});

afterEach((): void => { TestBed.resetTestingModule(); });
after((): void => {
  TestBed.resetTestEnvironment();
  destroyPlatform();
  closeDom();
});

function rootElement(): HTMLElement {
  const element: unknown = fixture.nativeElement;
  assert.ok(element instanceof HTMLElement);
  return element;
}

function element(selector: string): HTMLElement {
  const result = rootElement().querySelector(selector);
  assert.ok(result instanceof HTMLElement, `Missing element: ${selector}`);
  return result;
}

function button(selector: string): HTMLButtonElement {
  const result = element(selector);
  assert.ok(result instanceof HTMLButtonElement);
  return result;
}

function keyEvent(key: string): KeyboardEvent {
  return new KeyboardEvent('keydown', { key, bubbles: true, cancelable: true });
}

async function openDetails(): Promise<void> {
  button('[aria-controls]').click();
  await fixture.whenStable();
}

test('hidden projection remains created while the optional view control is absent', (): void => {
  assert.equal(element('section').hidden, true);
  assert.ok(button('[aekPanelAction]'));
  assert.equal(rootElement().querySelector('section > button:not([aekPanelAction])'), null);
  assert.equal(fixture.componentInstance.panel().focusCloseButton(), false);
});

test('open and Escape use notification paths and return focus to the trigger', async (): Promise<void> => {
  await openDetails();
  const close = button('section > button:not([aekPanelAction])');
  assert.equal(element('section').hidden, false);
  assert.equal(button('[aria-controls]').getAttribute('aria-expanded'), 'true');
  assert.equal(document.activeElement, close);

  const escape = keyEvent('Escape');
  close.dispatchEvent(escape);
  await fixture.whenStable();

  assert.equal(escape.defaultPrevented, true);
  assert.equal(fixture.componentInstance.closeCount(), 1);
  assert.equal(element('section').hidden, true);
  assert.equal(button('[aria-controls]').getAttribute('aria-expanded'), 'false');
  assert.equal(document.activeElement, button('[aria-controls]'));
  assert.equal(fixture.componentInstance.panel().focusCloseButton(), false);

  await openDetails();
  const recreated = button('section > button:not([aekPanelAction])');
  assert.notEqual(recreated, close);
  assert.equal(document.activeElement, recreated);
});

test('the consumer creates and removes the queried projected action', async (): Promise<void> => {
  await openDetails();
  const original = button('[aekPanelAction]');
  original.click();
  await fixture.whenStable();
  assert.equal(element('[data-state="receipt-count"]').textContent?.trim(), '1');
  assert.equal(rootElement().querySelector('[data-state="no-action"]'), null);

  fixture.componentInstance.includeAction.set(false);
  await fixture.whenStable();
  assert.equal(rootElement().querySelector('[aekPanelAction]'), null);
  assert.equal(element('[data-state="no-action"]').textContent?.trim(), 'No additional action.');

  fixture.componentInstance.includeAction.set(true);
  await fixture.whenStable();
  assert.notEqual(button('[aekPanelAction]'), original);
  assert.equal(rootElement().querySelector('[data-state="no-action"]'), null);
});

test('the close button emits through the deliberate host-directive alias', async (): Promise<void> => {
  await openDetails();
  button('section > button:not([aekPanelAction])').click();
  await fixture.whenStable();
  assert.equal(fixture.componentInstance.closeCount(), 1);
  assert.equal(element('section').hidden, true);
  assert.equal(document.activeElement, button('[aria-controls]'));
});

test('disabled, unrelated and already handled keys do not dismiss the panel', async (): Promise<void> => {
  const disabled = keyEvent('Escape');
  element('aek-details-panel').dispatchEvent(disabled);
  assert.equal(disabled.defaultPrevented, false);
  assert.equal(fixture.componentInstance.closeCount(), 0);

  await openDetails();
  const otherKey = keyEvent('Enter');
  element('aek-details-panel').dispatchEvent(otherKey);
  const handled = keyEvent('Escape');
  handled.preventDefault();
  element('aek-details-panel').dispatchEvent(handled);
  await fixture.whenStable();
  assert.equal(otherKey.defaultPrevented, false);
  assert.equal(fixture.componentInstance.closeCount(), 0);
  assert.equal(element('section').hidden, false);
});

test('destroying an enabled panel removes its owned listener', async (): Promise<void> => {
  await openDetails();
  const retainedHost = element('aek-details-panel');
  fixture.destroy();

  const afterDestroy = keyEvent('Escape');
  retainedHost.dispatchEvent(afterDestroy);
  assert.equal(afterDestroy.defaultPrevented, false);
});
```
