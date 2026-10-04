# Node.js runtime and composition

Read for Node startup, configuration, modules/packages, dependency assembly or
direct TypeScript execution. Shared module cohesion and language contracts remain
in [JavaScript structure](../javascript/modules-structure.md); strict typing remains
in [TypeScript](../typescript.md) when TypeScript is used. These rules apply to services, workers and CLI
programs as relevant, not to every browser module in a package-managed project.
Return to the [Node.js entry](../nodejs.md).

## Server execution and responsibility

- An HTTP or queue handler parses input, invokes a use case, and formats the result.
  Business branching and operation sequencing belong in the business layer.
- Pass dependencies explicitly; application assembly defines their configuration
  and lifetime. Do not recreate an infrastructure client in every handler.
- Perform I/O with suitable asynchronous mechanisms. `async` does not make heavy
  synchronous computation nonblocking. Move work to a worker or queue only when
  actual load and requirements justify it; do not add them preemptively.
- Do not lose errors in an empty `catch` or an unplanned fallback. Map application
  errors to transport responses at the boundary.
- Define concurrency limits, cancellation, and retries for external calls according
  to the contract and resources. Do not run unbounded fan-out over arbitrary input.

## Assembly and configuration

Keep one explicit assembly path for each executable: read and validate configuration,
construct shared clients/use cases, start consumers, and own their disposal. A
small factory taking concrete collaborators usually suffices. Use an existing DI
container where the framework needs it; do not create a container or a class per
function to emulate another ecosystem. Importing a reusable module should not
start listening, install process handlers or open a hidden global connection.

Environment values are strings or absent. Parse booleans, numbers, URLs, paths and
required secrets once into a named configuration contract; `Boolean("false")` and
unchecked numeric conversion do not validate it. Distinguish a missing value from
an empty one according to the contract. Keep secrets out of diagnostics and pass
only needed configuration to each collaborator. Loading a dotenv file is not schema
validation; use the project's accepted loader and precedence rather than another
configuration framework.

Create a shared connection pool/client where its API permits reuse; lease a
connection or transaction for the actual operation. A shared client is not a shared
mutable request DTO. Roll back acquired resources if later startup fails, and
report readiness only when required initialization succeeds. Functions or focused
objects can own assembly/disposal without a universal application base class.

## Packages and executable contracts

Establish the actual Node version, package-manager/lockfile pair, launch command,
module mode and deployment artifact. Prefer explicit package `type` or `.mjs`/`.cjs`
markers to reliance on syntax detection. Use `node:` imports for built-ins. Native
ESM relative imports need real extensions; test emitted paths as executed, including
case on the target filesystem. Do not change CommonJS/ESM as incidental cleanup.

For a published package, `exports` defines accessible subpaths and can break existing
deep imports when introduced. Verify the consumer paths actually supported, including
`import`/`require` conditions when both are promised. Dual outputs may duplicate
stateful instances; do not publish both formats without a consumer requirement.
Node's ability to `require()` synchronous ESM does not make a graph with top-level
`await` load synchronously. An export boundary is not a security sandbox.

Direct execution of `.ts` is a separate run mode. In the checked Node 24.13.0,
default type stripping performs no type checking, ignores `tsconfig.json`, and
does not provide TSX, decorator transforms or path-alias rewriting. Use the
project's real compiler/loader when those features are required, and retain strict
checking even when stripping works. Verify target-version support before adopting
new runtime syntax; this stage does not replace a NestJS/Next.js build pipeline.

## Basis

[Packages](https://nodejs.org/download/release/v24.13.0/docs/api/packages.html),
[Node TypeScript support](https://nodejs.org/download/release/v24.13.0/docs/api/typescript.html)
and [environment variables](https://nodejs.org/download/release/v24.13.0/docs/api/environment_variables.html)
describe runtime mechanisms. Assembly boundaries, configuration validation and
resource ownership are project policy; Node does not prescribe a layered tree.
