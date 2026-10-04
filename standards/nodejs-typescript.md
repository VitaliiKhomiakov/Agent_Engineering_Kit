# Node.js / JavaScript / TypeScript

Compatibility entry for existing `nodejs-typescript` selections. New imports
select [JavaScript](javascript.md), [Node.js](nodejs.md) and
[TypeScript](typescript.md) for the actual stack. This aggregate keeps its original
JavaScript/Node resources available; TypeScript remains a separate selection.
Read only applicable task sections, without traversing every link recursively.

## Versions and modules

Use [JavaScript targets and modules](javascript.md#versions-and-modules),
[Node versions](nodejs.md#versions-and-modules) when that host is used, and the
[TypeScript toolchain](typescript/toolchain-verification.md) when TypeScript is used.

## Read by task

Use the relevant [JavaScript](javascript.md#read-by-task),
[Node.js](nodejs.md#read-by-task) or [TypeScript](typescript.md#read-by-task) table.
Examples and framework profiles stay conditional on the task and actual stack.

## Typed boundaries

[JavaScript boundaries](javascript.md#typed-boundaries) own shared validation;
[TypeScript](typescript.md#external-data) adds its mandatory static contracts
only where TypeScript is used.

## Server execution and responsibility

Use [Node responsibilities](nodejs.md#server-execution-and-responsibility) for
Node host work and the relevant framework profile where one is used.

## Verification

Follow [JavaScript verification](javascript.md#verification) and, for actual Node
work, [Node verification](nodejs.md#verification). Use existing proportionate checks.

## Basis

The [JavaScript](javascript.md#basis), [Node.js](nodejs.md#basis) and
[TypeScript](typescript.md#basis) entries own their evidence and version limits.
This compatibility entry adds no runtime evidence.
