# Node.js

Apply only to work in the Node.js host, with [JavaScript](javascript.md) and the
[common rules](core.md). This includes services, workers, tools and CLI programs;
a browser bundle or package manifest alone does not select Node server guidance.
Select [TypeScript](typescript.md) when used and [NestJS](nestjs.md) for actual
Nest work. Examples and research are optional; read only task-relevant sections.

## Versions and modules

- Establish the Node.js, package manager, and, when used, TypeScript versions;
  the ESM/CommonJS mode; and how the project runs and builds. Reconcile
  `package.json`, the lockfile, build configuration, and CI. Do not migrate
  JavaScript to TypeScript or CommonJS to ESM as part of an ordinary fix.

## Read by task

| Task touches | Read |
| --- | --- |
| Startup/configuration, package loading, dependency assembly or direct TS execution | [Runtime and composition](nodejs/runtime-composition.md) |
| Streams, files, CPU work, workers, event callbacks or bounded concurrency | [I/O and concurrency](nodejs/io-concurrency.md) |
| HTTP servers/clients, body limits, deadlines, persistence or external effects | [HTTP and integrations](nodejs/http-integrations.md) |
| Signals, shutdown, resource cleanup, diagnostics, security checks or runtime upgrades | [Lifecycle and verification](nodejs/lifecycle-verification.md) |

## Server execution and responsibility

Keep handlers thin, dependencies explicit and effects bounded and observed.
Assembly owns resource lifetimes; shutdown must account for application work as
well as sockets. The detailed obligations are in the applicable Node sections.

## Verification

Use [JavaScript verification](javascript.md#verification) for shared checks and
[Node lifecycle and verification](nodejs/lifecycle-verification.md) for actual
host behavior. Type resolution alone does not prove that a runtime loads a module.

## Basis

[Node.js research](../docs/research/2026-09-21-nodejs-engineering-practices.md)
records runtime evidence checked on 2026-09-21 and the examples' version limits.
The [practice plan](../docs/plans/2026-09-21-engineering-practices.md) records checks.
[Don't Block the Event Loop](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop)
explains the constraints on synchronous work in handlers.
