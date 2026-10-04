# A validated Nest command and an explicit response

Read for class-based input validation, current-state refusal and response exposure.
[Transport contracts](../transport-contracts.md) owns the guidance. This example
uses Nest 12.0.4, Fastify 5.12.5, class-validator 0.15.1 and class-transformer 0.5.1
on Node 24.13.0. It introduces no authentication or production deployment scaffold.

A single-stock inventory accepts one to three quantity lines. The pipe rejects
extra fields and malformed/nested values without implicit body coercion. After that,
the pure inventory enforces available stock; a valid request can still receive 409.
The controller only maps input and the documented refusal. Direct callers remain
subject to the domain invariant even though they do not invoke an HTTP pipe.

The plain internal receipt deliberately includes an internal-only field.
`ClassSerializerInterceptor` plus `@SerializeOptions({ type: ReceiptView })` selects
only the exposed response fields. The final HTTP payload is checked. A simpler
explicit projection would also work; returning arbitrary ORM models is not the
pattern being recommended. The serializer does not run class-validator or validate
all possible output values merely because a response class exists.

DTO `declare` fields describe properties supplied by the selected runtime
transformation; they are not constructors or validation by themselves. The tested
pipe and decorators establish the input contract before the controller receives it.
The input DTO value import is intentionally retained for emitted parameter metadata.
Global pipe/interceptor registrations are made once in the fixture module; this
strict policy is not an instruction to change existing applications globally.

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
  "name": "af-nestjs-validated-command",
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
    "typescript-eslint": "8.70.0"
  },
  "dependencies": {
    "@nestjs/common": "12.0.4",
    "@nestjs/core": "12.0.4",
    "reflect-metadata": "0.2.2",
    "rxjs": "7.8.2",
    "@nestjs/platform-fastify": "12.0.4",
    "class-validator": "0.15.1",
    "class-transformer": "0.5.1"
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

## src/reserve.dto.ts

```ts
import { Type } from 'class-transformer';
import { ArrayMaxSize, ArrayMinSize, IsArray, IsInt, IsObject, Max, Min, ValidateNested } from 'class-validator';

export class QuantityLineDto {
  @IsInt()
  @Min(1)
  @Max(10)
  declare quantity: number;
}

export class ReserveDto {
  @IsArray()
  @ArrayMinSize(1)
  @ArrayMaxSize(3)
  @IsObject({ each: true })
  @ValidateNested({ each: true })
  @Type(() => QuantityLineDto)
  declare lines: QuantityLineDto[];
}
```

## src/inventory.ts

```ts
export interface ReserveCommand {
  readonly quantities: readonly number[];
}

export interface Receipt {
  readonly id: number;
  readonly remaining: number;
  readonly internalNote: string;
}

export class InsufficientStock extends Error {
  constructor() { super('Insufficient stock'); }
}

export class Inventory {
  #available: number;
  #sequence = 0;

  constructor(available: number) {
    if (!Number.isSafeInteger(available) || available < 0) throw new RangeError('Invalid stock');
    this.#available = available;
  }

  public reserve(command: ReserveCommand): Receipt {
    if (command.quantities.length === 0 || command.quantities.some(value => !Number.isSafeInteger(value) || value < 1)) {
      throw new RangeError('Invalid quantities');
    }
    const total = command.quantities.reduce((sum, value) => sum + value, 0);
    if (!Number.isSafeInteger(total)) throw new RangeError('Invalid total');
    if (total > this.#available) throw new InsufficientStock();
    this.#available -= total;
    this.#sequence += 1;
    return { id: this.#sequence, remaining: this.#available, internalNote: 'internal-only' };
  }
}
```

## src/receipt.view.ts

```ts
import { Exclude, Expose } from 'class-transformer';

@Exclude()
export class ReceiptView {
  @Expose()
  declare id: number;

  @Expose()
  declare remaining: number;
}
```

## src/reservations.controller.ts

```ts
import { Body, ConflictException, Controller, Inject, Post, SerializeOptions } from '@nestjs/common';
import { InsufficientStock, Inventory } from './inventory.js';
import type { Receipt } from './inventory.js';
import { ReceiptView } from './receipt.view.js';
import { ReserveDto } from './reserve.dto.js';

@Controller('reservations')
export class ReservationsController {
  constructor(@Inject(Inventory) private readonly inventory: Inventory) {}

  @Post()
  @SerializeOptions({ type: ReceiptView })
  public reserve(@Body() input: ReserveDto): Receipt {
    try {
      return this.inventory.reserve({ quantities: input.lines.map(line => line.quantity) });
    } catch (error) {
      if (error instanceof InsufficientStock) throw new ConflictException('Insufficient stock');
      throw error;
    }
  }
}
```

## src/reservations.module.ts

```ts
import { ClassSerializerInterceptor, Module, ValidationPipe } from '@nestjs/common';
import { APP_INTERCEPTOR, APP_PIPE } from '@nestjs/core';
import { Inventory } from './inventory.js';
import { ReservationsController } from './reservations.controller.js';

@Module({
  controllers: [ReservationsController],
  providers: [
    { provide: Inventory, useFactory: (): Inventory => new Inventory(5) },
    {
      provide: APP_PIPE,
      useFactory: (): ValidationPipe => new ValidationPipe({
        transform: true,
        whitelist: true,
        forbidNonWhitelisted: true,
        forbidUnknownValues: true,
        transformOptions: { enableImplicitConversion: false },
        validationError: { target: false, value: false },
      }),
    },
    { provide: APP_INTERCEPTOR, useClass: ClassSerializerInterceptor },
  ],
})
export class ReservationsModule {}
```

## src/application.ts

```ts
import 'reflect-metadata';
import { NestFactory } from '@nestjs/core';
import { FastifyAdapter } from '@nestjs/platform-fastify';
import type { NestFastifyApplication } from '@nestjs/platform-fastify';
import { ReservationsModule } from './reservations.module.js';

export async function createApplication(): Promise<NestFastifyApplication> {
  const adapter = new FastifyAdapter({ bodyLimit: 1024 });
  const app = await NestFactory.create<NestFastifyApplication>(ReservationsModule, adapter, {
    logger: false, abortOnError: false,
  });
  try {
    await app.init();
    await adapter.getInstance().ready();
    return app;
  } catch (error) {
    try { await app.close(); }
    catch (cleanup) { throw new AggregateError([error, cleanup], 'Initialization failed'); }
    throw error;
  }
}
```

## tests/run.ts

```ts
import assert from 'node:assert/strict';
import test from 'node:test';
import { createApplication } from '../src/application.js';
import { InsufficientStock, Inventory } from '../src/inventory.js';

await test('validates nested input and serializes only the selected public fields', async () => {
  const app = await createApplication();
  try {
    const response = await app.inject({ method: 'POST', url: '/reservations', payload: { lines: [{ quantity: 2 }] } });
    assert.equal(response.statusCode, 201);
    assert.deepEqual(response.json<unknown>(), { id: 1, remaining: 3 });
  } finally { await app.close(); }
});

await test('rejects malformed, extra and coerced fields before changing inventory', async () => {
  const app = await createApplication();
  const invalid: readonly unknown[] = [
    {}, { lines: null }, { lines: [] }, { lines: {} }, { lines: [null] },
    { lines: [[]] }, { lines: [[{ quantity: 1 }]] },
    { lines: [{}] }, { lines: [{ quantity: '2' }] }, { lines: [{ quantity: true }] },
    { lines: [{ quantity: null }] }, { lines: [{ quantity: 0 }] }, { lines: [{ quantity: 1.5 }] },
    { lines: [{ quantity: 11 }] }, { lines: [{ quantity: 1, extra: 'x' }] },
    { lines: [{ quantity: 1 }], extra: 'x' },
    { lines: [{ quantity: 1 }, { quantity: 1 }, { quantity: 1 }, { quantity: 1 }] },
  ];
  try {
    for (const payload of invalid) {
      const response = await app.inject({ method: 'POST', url: '/reservations', headers: { 'content-type': 'application/json' }, payload: JSON.stringify(payload) });
      assert.equal(response.statusCode, 400, JSON.stringify(payload));
    }
    const valid = await app.inject({ method: 'POST', url: '/reservations', payload: { lines: [{ quantity: 5 }] } });
    assert.deepEqual(valid.json<unknown>(), { id: 1, remaining: 0 });
  } finally { await app.close(); }
});

await test('valid representation may be refused by current stock without partial mutation', async () => {
  const app = await createApplication();
  try {
    const refused = await app.inject({ method: 'POST', url: '/reservations', payload: { lines: [{ quantity: 3 }, { quantity: 3 }] } });
    assert.equal(refused.statusCode, 409);
    const accepted = await app.inject({ method: 'POST', url: '/reservations', payload: { lines: [{ quantity: 5 }] } });
    assert.deepEqual(accepted.json<unknown>(), { id: 1, remaining: 0 });
  } finally { await app.close(); }
});

await test('adapter enforces its body budget before DTO processing', async () => {
  const app = await createApplication();
  try {
    const response = await app.inject({ method: 'POST', url: '/reservations', payload: { lines: [{ quantity: 1 }], extra: 'x'.repeat(1100) } });
    assert.equal(response.statusCode, 413);
    const accepted = await app.inject({ method: 'POST', url: '/reservations', payload: { lines: [{ quantity: 5 }] } });
    assert.deepEqual(accepted.json<unknown>(), { id: 1, remaining: 0 });
  } finally { await app.close(); }
});

await test('direct callers retain the business invariant without an HTTP pipe', () => {
  const inventory = new Inventory(5);
  assert.throws(() => inventory.reserve({ quantities: [6] }), InsufficientStock);
  assert.throws(() => inventory.reserve({ quantities: [0] }), RangeError);
  assert.deepEqual(inventory.reserve({ quantities: [5] }), { id: 1, remaining: 0, internalNote: 'internal-only' });
});
```

## Evidence and limits

On 2026-09-21, five tests passed: accepted nested input and final public fields; fifteen invalid
representations rejected before mutation; state-dependent refusal followed by a
successful unchanged-stock reservation; adapter byte limit; and the direct-call
domain invariant. `createApplication` is shared setup, so the tests use its actual
DI, pipe, serializer and adapter configuration. Fastify injection runs the HTTP
pipeline in process, without a network listener.

Strict native TypeScript 7.0.2, typed ESLint and the emitted ESM run passed. This
fixture targets ES2022; it uses the compatible Node 24 runtime. No SQL transaction,
simultaneous writers, authorization, schema-based serializer, Express adapter,
legacy Nest major, TCP/TLS or proxy behavior was executed. Real persisted stock
requires its storage concurrency contract; the synchronous in-memory operation
illustrates ownership only.

Both examples pin direct tool/runtime dependencies and retain temporary locks;
manifest-only installation can resolve newer transitive versions. The old Node
patch is an execution baseline, not a deployment recommendation. The
[plan](../../../docs/plans/2026-09-21-engineering-practices.md#k12-result-and-verification)
records actual checks, versions and exact Markdown/source equality.

Rechecked on 2026-10-03 for NEST-01: both added nested-array shapes reproduced
HTTP 500 before the fix. With per-item `@IsObject`, all seventeen invalid inputs
return 400 and the following valid request still receives receipt 1 with zero
stock remaining. All five tests, strict TS, typed lint and build passed on Node
24.21.0 with the same pinned dependencies. See the dated
[follow-up evidence](../../../docs/research/2026-09-21-nestjs-engineering-practices.md#2026-10-03-follow-up-nest-01).
