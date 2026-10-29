# LangChain JavaScript tool fixture

This [tool boundary](../models-tools.md) uses a runtime Zod schema and per-request
closure for trusted context. It checks successful/empty reads, invalid arguments,
an attempted tenant argument and a backend denial without a model or agent loop.

## Fixture and reproduction

Executed on **2026-10-29** with Node.js **24.13.0**, npm **11.6.2**,
`@langchain/core` **1.3.1** and Zod **4.3.6**. In an empty temporary directory,
save these files. Registry access is needed to install dependencies; the test
uses no remote API or credentials.

### `package.json`

```json
{
  "private": true,
  "type": "module",
  "dependencies": {
    "@langchain/core": "1.3.1",
    "zod": "4.3.6"
  }
}
```

### `tool.test.mjs`

```javascript
import assert from "node:assert/strict";
import test from "node:test";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

// Create per request with already authenticated context; do not mutate a shared tool.
function createLookup({ tenantId, read }) {
  if (!tenantId || typeof read !== "function") throw new Error("missing context");
  return tool(async ({ id }) => {
    // read must authorize the tenant and constrain the query before reading data.
    const record = await read(tenantId, id);
    return JSON.stringify(record === null ? { status: "not_found" } : {
      status: "found", id: record.id, text: record.text,
    });
  }, {
    name: "lookup_note",
    description: "Read one note visible to the current user by its ID",
    schema: z.strictObject({ id: z.string().min(1).max(64) }),
  });
}

test("validates arguments and binds trusted scope before the backend read", async () => {
  const calls = [];
  const read = async (tenantId, id) => {
    calls.push({ tenantId, id });
    if (tenantId !== "tenant-a") throw new Error("denied");
    return id === "n1" ? { id, text: "Example evidence" } : null;
  };
  const lookup = createLookup({ tenantId: "tenant-a", read });
  assert.deepEqual(JSON.parse(await lookup.invoke({ id: "n1" })), {
    status: "found", id: "n1", text: "Example evidence",
  });
  assert.deepEqual(JSON.parse(await lookup.invoke({ id: "missing" })), {
    status: "not_found",
  });
  await assert.rejects(lookup.invoke({ id: "" }));
  await assert.rejects(lookup.invoke({ id: "n1", tenantId: "tenant-b" }));
  assert.deepEqual(calls, [
    { tenantId: "tenant-a", id: "n1" }, { tenantId: "tenant-a", id: "missing" },
  ]);
  const denied = createLookup({ tenantId: "tenant-b", read });
  await assert.rejects(denied.invoke({ id: "n1" }), /denied/);
});
```

### Checks

```sh
npm install --ignore-scripts --no-audit --no-fund
LANGSMITH_TRACING=false LANGCHAIN_TRACING_V2=false node --test tool.test.mjs
```

Retain the generated lockfile for repeat runs; use `npm ci` thereafter. These pins
document this fixture, not an instruction to change an application's dependencies.

## Evidence limits

The host must authenticate the context and the real `read` dependency must enforce
access. The example directly invokes a tool with validated arguments; it does not
exercise agent runtime context injection, provider schemas, tool-call IDs,
streaming, remote cancellation or structured model output. Do not treat those
integration paths as tested by this fixture.
