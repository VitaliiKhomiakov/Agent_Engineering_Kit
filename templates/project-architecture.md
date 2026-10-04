# Project architecture passport

Record current evidence and target decisions separately. Keep it short and link
to detailed decisions. Do not copy versions from examples or assume `latest`
matches the project. Existing implementation is not automatically the standard.
Retain only applicable fields/sections; a gameplay or editor project does not need
HTTP, ORM or other backend fields merely because this template lists them.

## Adopted rules

- Profiles and task routes: `<selected IDs, actual components and reachable entry paths>`.
- Provenance: `<reachable .agents-framework/adoption.md for this target>` owns source
  identity and accepted exceptions. Read it only for import/update/recovery; keep
  applicable operational constraints in this passport or the local entry.

## Purpose and boundaries

- Project/service/plugin: `<name and relative path>`.
- Purpose: `<one or two sentences>`.
- Data and contract ownership: `<bounded context and responsibility>`.
- Entry points: `<HTTP / CLI / queue / gameplay input or event / editor action and locations>`.

## Stack and version evidence

| Component | Supported version/range | Locked or verified version | Source |
| --- | --- | --- | --- |
| Language/runtime | `<compatibility>` | `<actual version or unverified>` | `<Dockerfile / CI / runtime>` |
| Framework | `<manifest constraint>` | `<resolved version>` | `<lockfile / environment>` |
| ORM/DB client | `<constraint>` | `<resolved version>` | `<source>` |
| Validator/serializer | `<constraint>` | `<resolved version>` | `<source>` |

Verification date: `<date>`.
Documentation/lockfile/environment differences: `<findings or none found>`.

Optional structured notes: fill only evidence that applies to this project.
This block is a concise reference for agents, not input to an installed parser.
Empty tables make no technology or command assignment; run checks only when needed.

<!-- agents-framework:project -->
```toml
[technologies]
# postgresql = "<version declared by this project>"
# unreal-engine = "<engine version declared by this project>"

[checks]
# api = "<existing project check command>"
```
<!-- /agents-framework:project -->

## Flow and dependencies

Describe a principal flow using the project's real owners: for example entry →
application use case → domain rules → infrastructure adapter, or gameplay event →
Actor/Component → state transition → engine effect. Name permitted dependencies
and actual paths. Do not present target layers as already implemented.

| Interaction | Contract | Owner | Material conditions |
| --- | --- | --- | --- |
| `<from → to>` | `<HTTP / event / interface>` | `<project/component>` | `<transaction, retry, errors, compatibility>` |

## Internal layers and permitted dependencies

Describe the layers/responsibilities that exist or are explicitly planned for
this project. Adapt the names to its language and purpose; do not create empty
folders or force a frontend/gameplay/editor project to copy a backend layer hierarchy.

| Layer/module and real path | Responsibility | Public interface | May depend on | Must not depend on |
| --- | --- | --- | --- | --- |
| `<entry / feature / application / domain / adapter as applicable>` | `<owned behavior>` | `<DTO / interface / event>` | `<allowed modules>` | `<forbidden coupling>` |

Distinguish runtime calls from source-code dependencies. A use case may call an
injected adapter through an interface while remaining independent of its SDK.
Identify the composition root, validation boundary, transaction owner, and
mapping points when those responsibilities are present.

For multi-project behavior, link to the root workspace interaction map and the
owned contracts rather than copying every other project's implementation here.

## Target state and transition

| Area | Current evidence | Target decision | Transition |
| --- | --- | --- | --- |
| `<boundary/typing/structure>` | `<path and fact>` | `<rule and reason>` | `<stage and acceptance>` |

Frequent defects do not become useful conventions. Distinguish contracts to
preserve from behavior intentionally being corrected.

## Models and engineering decisions

- Input DTOs and their validation: `<location and invocation mechanism>`.
- Current-state business rules: `<owners>`.
- Domain/object construction and service assembly: `<actual creation rules / DI or engine-managed composition>`;
  use factories, facades, strategies, or monadic composition only for a current
  problem described in the relevant core/language rule.
- Doctrine/TypeORM, when used: choose `mapped-rich` or `separate-domain`, describe permitted entity
  behavior and mapping ownership. Record an unresolved choice; do not decide silently.
  Business mutation uses named intent methods, with coupled values checked before
  any assignment; no generated attribute setters or generic DTO patches.
- Other ORMs: describe how persistence and domain models relate; SQLAlchemy
  Core/ORM choice does not choose a database or require a second domain model.
- Persistence, when present: `<database/dialect, driver, transaction/session owner,
  migration owner and resource lifetime; separate version evidence for each>`.
- Containers, when present: `<build context, runtime command/user, shutdown,
  configuration and durable-data owners; affected build/runtime checks>`.
  Record the dev mode (dependencies-only / app in containers), exact Compose
  file order/project names, source sync and dependency refresh. For production,
  record image promotion, secrets, migration runner, ingress, backups/restore,
  resource/log budgets and accepted host failure/downtime limits.
- Node.js: ESM/CommonJS, build/runtime, and DTO validation mechanism.
- NestJS: module boundaries, exports, and actually connected validation pipes.
  With TypeORM, also record data-source names, entity/CLI discovery, transaction
  manager propagation and the actual concurrency protocol.
- Angular, when present: `<resolved Angular/CLI/TypeScript/RxJS versions,
  standalone/NgModule composition, ZoneJS/zoneless providers, change detection,
  CSR/SSR/hydration, feature/public boundaries, form and styling choices>`.
  Record the section names and access policies, including the project-chosen
  name of any authenticated section; do not assume it is named `core`. Map section
  routes/layouts, simple pages, nested domains, presentation components and shared
  infrastructure to their actual paths and public import contracts.
  Record local/route/application state owners, injector lifetime and explicit
  reset behavior; distinguish URL state, drafts, canonical entities and derivations.
  With NgRx, record used package versions, Store/Effects versus SignalStore or
  existing ComponentStore. For classic Store, record the root provider entry,
  eager/lazy feature registration locations and feature Store file owners.
  For SignalStore or ComponentStore, record store paths and root/route/component
  provider scope; do not introduce classic Store wiring for those packages alone.
  Record applicable selectors/computed values, request concurrency and stale-result
  policy, cache keys/invalidation, Entity
  query membership and Router Store serializer/timing only where used.
- Related class/type grouping: `<profile or justified exception>`.
- TypeScript/Python: `<checker/version, strict settings, no any/Any, checked scope,
  interface/Protocol ownership, and remaining legacy gaps>`.
- Exceptions and legacy size excesses: `<scope, reason, limits>`.

## Unreal Engine, when present

Fill only facts relevant to the project/task; distinguish intended choices from
observations. Reuse stable context and update it when affected inputs change.

- Engine: `<version/build identity and evidence; installed or source build>`.
- Project/plugin and targets: `<descriptor path, host OS, supported target platforms,
  build targets/configurations, Blueprint/C++ usage and required plugins>`.
- Ownership: `<runtime/editor modules, gameplay/component/subsystem roles,
  world/player/session lifetimes and actual composition points>`.
- Assets: `<reference/load/retention owners, cook inclusion, relevant redirects,
  source-control and unsaved-work preservation contracts>`.
- Multiplayer, if required: `<authority/ownership and affected client/server contracts>`.
- Checks: `<existing commands/scenarios with triggers; compilation, affected
  asset/Blueprint validation, PIE, package or profiling only where needed>`.
- Editor provider, only when used: `<provider/version, capability evidence,
  connection configuration owner and relevant editor/world/PIE context; revalidate
  ephemeral handles/state after reload or world change, not on every source edit>`.
- Rules: `<reachable unreal-engine profile entry and accepted local exceptions>`.

## Frontend, when present

- Host/framework and routing: `<actual renderer/router; App / Pages for Next.js>`.
- Next.js target structure: compact product capability modules without mandatory
  full FSD; use the actual framework's conventions for other React hosts.
- Existing structure and transition: `<evidence and migration stage>`.
- Feature boundaries and public imports: `<owners and rules>`.
- Server/Client and server-only code: `<locations and boundary enforcement>`.
- UI, styling, forms, validation, query/cache, and local state: `<selected tools and roles>`.
- Mutation update strategy: `<compatible with the selected data tools and framework;
  record cache/revalidation semantics for the installed Next.js version when used>`.

## Agent workflow and evidence

- Workspace model selection: `<path to .agents-framework/model-routing.toml>`.
- Default work mode: current directory, no commits/worktrees, one logical stage,
  then stop for user review. Any explicit task override belongs in its contract.
- Existing checks and triggers: `<CHECKS.md or a short command list>`.
- Test constraints: `<data isolation and external/paid dependencies>`.
- Critical scenarios: `<concrete project risks>`.
- Official documentation for actual versions: `<short relevant link list>`.
- Current specifications and decisions: `<links with reading conditions>`.

Update the affected section when a version, boundary, or contract changes.
Do not require reading the entire passport before every local edit.
