# Workspace architecture

Use this as the root ARCHITECTURE.md for a workspace containing several projects.
Keep the system map here and implementation detail in each project's passport.
For one project, combine this map with the project passport instead of duplicating it.

## Scope and evidence

- Workspace purpose: `<business outcome>`.
- Architecture status: `<observed current state / agreed target / illustrative proposal>`.
- Evidence and last verification: `<specific files/contracts and date>`.
- Included projects: `<scope; link elsewhere for unrelated systems>`.

Mark uncertain relationships explicitly. Existing code is evidence, not a standard.
Do not present a proposed target as an already implemented architecture.

## Project responsibilities

| Project/path | Responsibility | Owned data and decisions | Entry points | Stack and version evidence | Detailed passport |
| --- | --- | --- | --- | --- | --- |
| `<project>` | `<one bounded responsibility>` | `<authoritative owner>` | `<UI / HTTP / queue / CLI>` | `<runtime/framework summary; authoritative version source>` | `<relative path>` |

Include the exact relevant runtime/framework versions once established. A range
in a manifest is not proof of the installed version. Keep detailed dependency
versions in the project passport and avoid maintaining competing version lists.

## Runtime interactions

Add one compact diagram of the important calls or messages. Label each arrow with
its purpose; a runtime communication arrow is not a source-code import direction.

| Producer/caller → consumer | Purpose and contract | Transport and sync/async behavior | Contract owner/source | Failure and compatibility conditions |
| --- | --- | --- | --- | --- |
| `<A → B>` | `<command/query/event and required fields>` | `<actual HTTP/queue/etc. or explicitly undecided>` | `<schema/API/spec path>` | `<authorization, timeout/retry, idempotency, version compatibility as applicable>` |

Describe logical result delivery separately from its mechanism. A result flowing
from B to A might be a response, callback, event, or polling result; do not invent
an endpoint or broker from the direction of an arrow.

## Representative end-to-end scenario

Describe one important user scenario in a short sequence:

1. `<entry point receives and validates input>`.
2. `<owning project makes the business decision and changes its state>`.
3. `<another project performs its assigned operation through an explicit contract>`.
4. `<the owner accepts the result and exposes the final user-visible state>`.

State the relevant failure path, correlation identifiers, source of truth, and
transaction boundaries. Include retries, ordering, or duplicate handling only
where the actual interaction requires them.

## Data ownership and architectural boundaries

| Data/state | Authoritative owner | Who may read or write it | Access contract |
| --- | --- | --- | --- |
| `<business record/job/file/result>` | `<project>` | `<permitted actors>` | `<API/event/storage interface>` |

List the material forbidden dependencies: for example, a UI bypassing its API,
one service writing another service's tables, or a domain module importing a
transport SDK. Distinguish shared infrastructure from shared business ownership.
Wire contracts and implementation choices through the relevant project passports.

## Layers inside each project

Link to the layer/dependency section of each passport. At workspace level,
summarize only the responsibilities needed to understand interactions.
Do not impose identical layer folders on frontend, backend, and processing services.

## Current gaps and target decisions

| Area | Current evidence | Target decision | Migration stage/acceptance |
| --- | --- | --- | --- |
| `<boundary or ownership>` | `<observed path/contract>` | `<agreed change or open question>` | `<bounded transition>` |

## Navigation and maintenance

- UI-only work: `<frontend passport and relevant feature>`.
- Backend behavior: `<backend passport and affected contract>`.
- Processing behavior: `<processing passport and input/output contract>`.
- Cross-project change: this interaction map and the affected contract owners.

Update the affected row when a responsibility, contract, version, or dependency
changes. Keep historical plans elsewhere; do not copy all service internals into
this root file or require reading every passport before a local edit.
