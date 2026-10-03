# Exported provider capability and awaited disposal

Read for module exports, asynchronous factories, aliases and lifecycle ownership.
[Modules/providers](../modules-providers.md) and [application/lifecycle](../application-lifecycle.md)
own the general rules. The fixture runs Nest 12.0.4 on Node 24.13.0 without an HTTP
adapter. It uses a real temporary file and a small pure use case.

`ExportTotal` depends on the named `ReportSink` capability. `REPORT_SINK` supplies
its runtime token. `ReportModule` asynchronously opens one output file with exclusive
creation and aliases the managed adapter via `useExisting`; it exports only that
capability. `ExporterModule` imports it, constructs the pure consumer through an
explicit factory and exports the use case. Each independent module/provider has its
own file; there is no decorator requirement on the pure use case.

The sink accepts one report, marks that attempt before its first await and refuses
another write. A failed write may leave partial output and is not retried implicitly.
The executable awaits the operation, then closes its application in `finally`.
The owned adapter's hook awaits file-handle closure. The dynamic modules configure
a per-application path; a static module is simpler when no such variation is needed.

The path is trusted assembly configuration, not an unvalidated HTTP filename.
Exclusive creation protects an existing file, but this is not atomic publication,
fsync, rollback, a multi-writer journal or a general database adapter. Partial
acquisition/other dependency failures require the owning factory's cleanup contract.
No broader hook ordering or automatic joining of detached work is assumed.

## Setup and checks

Copy the files below into the shown paths in a temporary directory. Install with
`npm install --ignore-scripts`, retain the generated lockfile, then use `npm ci`
with the same script policy for repeats. These fixtures' dependencies do not need
install scripts; do not apply that assumption to arbitrary native packages.

```sh
npm run check
npm run lint
npm run build
npm test
```

The scripts execute emitted JavaScript rather than stripping TS syntax. Keep
`experimentalDecorators`, `emitDecoratorMetadata` and the `reflect-metadata` import:
this is the configured class-metadata path. Direct Node type stripping is not an
alternative for these decorators. The two TypeScript package aliases supply a
native compiler and the compatibility API needed by typed ESLint, as in the
[TypeScript toolchain rules](../../typescript/toolchain-verification.md).

## package.json

```json
{
  "name": "af-nestjs-provider-lifecycle",
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
    "test": "node --unhandled-rejections=strict dist/tests/run.js"
  },
  "devDependencies": {
    "@types/node": "24.13.6",
    "@typescript/native": "npm:typescript@7.0.2",
    "typescript": "npm:@typescript/typescript6@6.0.2",
    "eslint": "10.11.0",
    "typescript-eslint": "8.70.0",
    "@nestjs/testing": "12.0.4"
  },
  "dependencies": {
    "@nestjs/common": "12.0.4",
    "@nestjs/core": "12.0.4",
    "reflect-metadata": "0.2.2",
    "rxjs": "7.8.2"
  }
}
```

## tsconfig.json

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
      "ES2024"
    ],
    "types": [
      "node"
    ],
    "rootDir": ".",
    "outDir": "dist",
    "noEmitOnError": true,
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true
  },
  "include": [
    "src/**/*.ts",
    "tests/**/*.ts"
  ]
}
```

## eslint.config.mjs

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

## src/report.ts

```ts
export interface Report {
  readonly total: number;
}

export interface ReportSink {
  write(report: Report): Promise<void>;
}

export const REPORT_SINK = Symbol('REPORT_SINK');
```

## src/export-total.ts

```ts
import type { ReportSink } from './report.js';

export class ExportTotal {
  constructor(private readonly sink: ReportSink) {}

  public async execute(values: readonly number[]): Promise<void> {
    if (values.some(value => !Number.isSafeInteger(value) || value < 0)) {
      throw new RangeError('Expected nonnegative safe integers');
    }
    const total = values.reduce((sum, value) => sum + value, 0);
    if (!Number.isSafeInteger(total)) throw new RangeError('Total exceeds safe range');
    await this.sink.write({ total });
  }
}
```

## src/file-report-sink.ts

```ts
import type { OnModuleDestroy } from '@nestjs/common';
import type { FileHandle } from 'node:fs/promises';
import type { Report, ReportSink } from './report.js';

export class FileReportSink implements ReportSink, OnModuleDestroy {
  #written = false;

  constructor(private readonly handle: FileHandle) {}

  public async write(report: Report): Promise<void> {
    if (this.#written) throw new Error('This sink accepts one report');
    this.#written = true;
    await this.handle.writeFile(JSON.stringify(report) + '\n');
  }

  public async onModuleDestroy(): Promise<void> {
    await this.handle.close();
  }
}
```

## src/report.module.ts

```ts
import { Module } from '@nestjs/common';
import type { DynamicModule } from '@nestjs/common';
import { open } from 'node:fs/promises';
import { FileReportSink } from './file-report-sink.js';
import { REPORT_SINK } from './report.js';

@Module({})
export class ReportModule {
  public static forFile(path: string): DynamicModule {
    return {
      module: ReportModule,
      providers: [
        {
          provide: FileReportSink,
          useFactory: async (): Promise<FileReportSink> => new FileReportSink(await open(path, 'wx')),
        },
        { provide: REPORT_SINK, useExisting: FileReportSink },
      ],
      exports: [REPORT_SINK],
    };
  }
}
```

## src/exporter.module.ts

```ts
import { Module } from '@nestjs/common';
import type { DynamicModule } from '@nestjs/common';
import { ExportTotal } from './export-total.js';
import { REPORT_SINK } from './report.js';
import type { ReportSink } from './report.js';
import { ReportModule } from './report.module.js';

@Module({})
export class ExporterModule {
  public static forFile(path: string): DynamicModule {
    return {
      module: ExporterModule,
      imports: [ReportModule.forFile(path)],
      providers: [
        {
          provide: ExportTotal,
          useFactory: (sink: ReportSink): ExportTotal => new ExportTotal(sink),
          inject: [REPORT_SINK],
        },
      ],
      exports: [ExportTotal],
    };
  }
}
```

## tests/run.ts

```ts
import 'reflect-metadata';
import assert from 'node:assert/strict';
import { mkdtemp, open, readFile, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { setImmediate as nextTurn } from 'node:timers/promises';
import test from 'node:test';
import type { OnModuleDestroy } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';
import { Test } from '@nestjs/testing';
import { ExportTotal } from '../src/export-total.js';
import { ExporterModule } from '../src/exporter.module.js';
import { FileReportSink } from '../src/file-report-sink.js';
import { REPORT_SINK } from '../src/report.js';
import type { Report, ReportSink } from '../src/report.js';

await test('exported token supplies the pure consumer and aliases one async-created adapter', async () => {
  const directory = await mkdtemp(join(tmpdir(), 'nest-report-'));
  try {
    const path = join(directory, 'report.json');
    const app = await NestFactory.createApplicationContext(ExporterModule.forFile(path), { logger: false, abortOnError: false });
    try {
      assert.equal(app.get<ReportSink>(REPORT_SINK), app.get(FileReportSink));
      await app.get(ExportTotal).execute([2, 3]);
      assert.equal(await readFile(path, 'utf8'), '{"total":5}\n');
      await assert.rejects(app.get(ExportTotal).execute([1]), /one report/);
      assert.equal(await readFile(path, 'utf8'), '{"total":5}\n');
    } finally { await app.close(); }
  } finally { await rm(directory, { recursive: true, force: true }); }
});

await test('real managed file handle is closed by the application lifecycle', async () => {
  const directory = await mkdtemp(join(tmpdir(), 'nest-close-'));
  const handle = await open(join(directory, 'report.json'), 'wx');
  try {
    const module = await Test.createTestingModule({ imports: [ExporterModule.forFile('unused')] })
      .overrideProvider(FileReportSink).useValue(new FileReportSink(handle)).compile();
    try { await module.init(); }
    finally { await module.close(); }
    assert.equal(handle.fd, -1);
  } finally {
    await handle.close();
    await rm(directory, { recursive: true, force: true });
  }
});

await test('close awaits the owned asynchronous release hook', { timeout: 2000 }, async () => {
  let closed = false;
  const entered = Promise.withResolvers<void>();
  const finish = Promise.withResolvers<void>();
  const delayed: ReportSink & OnModuleDestroy = {
    write(): Promise<void> { return Promise.resolve(); },
    async onModuleDestroy(): Promise<void> { entered.resolve(); await finish.promise; closed = true; },
  };
  const module = await Test.createTestingModule({ imports: [ExporterModule.forFile('unused')] })
    .overrideProvider(FileReportSink).useValue(delayed).compile();
  await module.init();
  let returned = false;
  const stopping = module.close().then(() => { returned = true; });
  try {
    await entered.promise;
    await nextTurn();
    assert.equal(returned, false);
    assert.equal(closed, false);
  } finally {
    finish.resolve();
    await stopping;
  }
  assert.equal(closed, true);
  assert.equal(returned, true);
});

await test('failed async acquisition rejects startup without overwriting a file', async () => {
  const directory = await mkdtemp(join(tmpdir(), 'nest-exists-'));
  try {
    const path = join(directory, 'report.json');
    await writeFile(path, 'existing');
    await assert.rejects(
      NestFactory.createApplicationContext(ExporterModule.forFile(path), { logger: false, abortOnError: false }),
      { code: 'EEXIST' },
    );
    assert.equal(await readFile(path, 'utf8'), 'existing');
  } finally { await rm(directory, { recursive: true, force: true }); }
});

await test('invalid business values have no sink effect without booting Nest', async () => {
  const reports: Report[] = [];
  const sink: ReportSink = {
    write(report: Report): Promise<void> { reports.push(report); return Promise.resolve(); },
  };
  const operation = new ExportTotal(sink);
  await assert.rejects(operation.execute([-1]), RangeError);
  await assert.rejects(operation.execute([Number.MAX_SAFE_INTEGER, 1]), RangeError);
  assert.deepEqual(reports, []);
  await operation.execute([2, 3]);
  assert.deepEqual(reports, [{ total: 5 }]);
});
```

## Evidence and limits

Five tests passed: a parent consumer receives the exported capability and shares
one async-created adapter; its real output and one-attempt policy; closure of a real
managed file handle; waiting for an asynchronous release hook; failed exclusive
acquisition without overwriting a file; and invalid pure-business input without a
sink effect. Narrow provider overrides are used only for specific lifecycle checks;
the normal wiring test uses the actual module imports/exports and file factory.

Strict native TypeScript 7.0.2, typed ESLint and the emitted ESM run passed. This
fixture targets ES2024 for the test gates' `Promise.withResolvers`, supported by
its Node 24 runtime. The delayed hook is a controlled collaborator for ordering;
it does not prove a database driver cancels work or releases connections. No OS
signal, request-scoped resource, concurrent shutdown, broad hook-order matrix,
crash-durability or real database behavior was executed.

Both examples pin direct tool/runtime dependencies and retain temporary locks;
manifest-only installation can resolve newer transitive versions. The old Node
patch is an execution baseline, not a deployment recommendation. The
[plan](../../../docs/plans/2026-09-21-engineering-practices.md#k12-result-and-verification)
records actual checks, versions and exact Markdown/source equality.
