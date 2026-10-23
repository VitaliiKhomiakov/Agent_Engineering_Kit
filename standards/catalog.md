# Rule catalog: bundling and reading

Read when selecting a portable rule bundle, adapting entry routes, or resolving
catalog semantics. Ordinary tasks follow their adopted entry routes and the
applicable profile's task table. This guide defines the existing
[catalog](catalog.toml) format, `schema_version = 1`; it is not an installer.

## Field meanings

Paths in the TOML catalog resolve from the bundle root, not from the `standards/`
directory containing the catalog or necessarily the project root. The source
library root is its bundle root; a new target defaults to `.agents-framework/`.
Thus `standards/core.md` keeps its catalog value and becomes target
`.agents-framework/standards/core.md`. Schema 1 and existing IDs stay unchanged.
Source `MIGRATION.md`, section "Layout and path contract", owns placement and
relocation; resolve it through the identified source. Existing flat imports stay
flat until relocation is explicitly selected and reconciled.

| Field | Meaning |
| --- | --- |
| `schema_version` | Version of the documented catalog layout |
| `assets` | Shared files supplied with the bundle, including this guide |
| `templates` | Named template paths to adapt for the selected client's entry mechanism |
| `profiles[].id` | Unique stable profile ID; `dependencies` refer to these IDs |
| `source` | The profile's entry document |
| `dependencies` | Profiles whose files must remain available with this profile; follow transitively when assembling the bundle, not when reading for a task |
| `resources` | Supporting detail sections and examples available with the profile; availability does not require opening them |
| `required = true` | Shared policy to include in an adopted bundle; reading still depends on the task and its `when` condition |
| `activities`, `technologies`, `globs` | Applicability hints; confirm the actual task and stack rather than treating a match as an unconditional instruction |
| `when` | The condition for reading the profile; its own routes then select relevant sections |

## Assemble a portable bundle

Select profiles for the actual project stack and intended work. Include shared
`required` and selected profiles with their transitive dependencies, sources and
resources, shared assets and needed catalog `templates`. Other entry and passport
templates are read from the source library's MIGRATION section "Entry and passport
templates". Keep each file once when it appears through several routes. Preserve these IDs and bundle-relative paths;
change the bundle's placement without prefixing catalog values.

Check reachable references from the adopted entry and copied documents. Templates
may resolve links from their intended installed location; validate that location
after adaptation. Copying a file neither loads it into an agent's context nor
installs a client, activates a skill, or selects a framework for the application.

The catalog itself is a shared asset so adopted bundle-selection routes remain
reachable. Its entries describe the source library: an unselected profile's files
need not exist in a selected target bundle. Validate the selected closure, not
every unselected entry. The model-configuration resources keep routing examples,
native role templates and setup/reassignment skills available in their inactive
`templates/` locations. Copying them does not create active role definitions or
model settings; activate only the chosen client's enabled roles during authorized
setup. Ordinary imports can remain inline without this setup.

Optional source research and historical plans are not bundle dependencies. When
omitting them, adapt their links in copied documents to clearly labelled source
references resolved through adoption provenance, or an actually known source URL
with content identity where available. A local author-machine Markdown link is
not portable, even when reachable during preparation. Keep the rule/procedure
complete without those archives; do not silently leave a required route broken or
recursively copy history just to satisfy an optional evidence link. Treat these
reference adaptations as part of the accepted imported content.

For cross-profile links, check the stated condition against the target stack.
If it is inapplicable, remove that optional route or retain a labelled source
reference instead of a dangling target link. For example, the JavaScript entry's
NestJS link does not require copying NestJS into a React-only project. If the
condition applies, include the relevant profile and its closure. Never drop a
required route merely to make a bundle check pass.

The shared [adoption-record template](../templates/framework/adoption-record.md)
is an available asset, not an active record. Adapt it to
`.agents-framework/adoption.md` only during authorized import. Read it for import,
update or recovery, never merely because ordinary work loads a profile. Preparation
keeps the proposed record outside the target. It owns provenance/managed scope;
task progress and model assignments retain their existing owners. The source
library's `MIGRATION.md` owns comparison and recovery; resolve that procedure from
the identified accessible source when needed, without assuming it was copied.

## Independent and legacy selections

For new bundles, select the language plus the hosts, frameworks and libraries
actually used. Entries route to their existing topic directories; short entries
and detailed topics have different responsibilities. TypeScript adds shared static
contracts to JavaScript without selecting Node server guidance. Select it alongside
React, Next.js or Node.js for TypeScript code; NestJS and Angular already depend on
it under this library's policy. Host selection follows the actual task/runtime.

| Intended selection | Profile IDs |
| --- | --- |
| PHP; optional Symfony or Doctrine | `php`; add `symfony` and/or `doctrine` when used |
| Go; optional Gin | `go`; add `gin` when used |
| Python; validation or HTTP framework | `python`; add `pydantic` or `fastapi` when used |
| Browser JavaScript or TypeScript | `javascript` or `typescript` |
| Node.js JavaScript or TypeScript | `nodejs`; add `typescript` when used |
| React JavaScript or TypeScript, without Next.js | `react`; add `typescript` when used |
| Next.js JavaScript or TypeScript | `nextjs-framework`; add `typescript` when used and `nodejs` for Node host work |
| Angular or NestJS; optional packages | `angular` or `nestjs`; add `ngrx` or `typeorm` only when used |
| Godot; conditional C# or GDExtension | `godot`; read additional language sections only where used |
| Unreal Engine project or plugin | `unreal-engine` |
| PostgreSQL; optional Python database access | `postgresql`; add `sqlalchemy` and/or `psycopg` when used (`psycopg` depends on `postgresql`) |
| Container builds or Compose environments | `docker` |

Dependencies supply shared bases automatically; explicitly selecting the same
base again does not duplicate its files. Examples retain their stated language
and version requirements; a TypeScript example does not convert a JavaScript task.

The stable IDs `php-symfony-doctrine`, `go-gin`, `python-fastapi`,
`nodejs-typescript` and `nextjs` remain compatibility aggregates with their old
paths, anchors and resource availability. In particular, `nodejs-typescript`
still does not select TypeScript automatically, while old `nextjs` retains its
React/TypeScript/Node resource set. The independent Next.js ID is
`nextjs-framework`. `nextjs-feature-structure` is a separate optional profile for
feature-boundary work, not a compatibility aggregate; it depends on `nextjs-framework`,
which also lists its document as a resource.
Do not reinterpret an old ID as a new narrow selection. A reviewed selection
change during adoption follows the source library's MIGRATION repeat/update
procedure; a smaller closure is not permission to delete previously managed files.

## Read for the current task

The optional `project-workflows` profile supplies the
[project-skill contract](project-skills.md) and inactive design and review templates.
Select it explicitly during adoption when those optional project task skills are wanted;
technology selections alone do not include it, and it selects no technology.
Bundle availability is separate from installing a chosen native skill. Source
MIGRATION owns destination adaptation and recording the managed native path.
Projects without this profile keep their existing direct task routes; adapt this
optional link when omitting the profile from a target bundle.

1. Identify the changed behavior, actual language/framework and applicable project
   constraints. A broad filename match cannot establish the stack by itself.
2. Follow the entry route and matching profile's `when` condition. Read only the
   relevant sections in its task table; do not traverse catalog dependencies as
   a reading queue.
3. Read examples or research only to resolve a specific decision or evidence gap.
   Stop following links once the relevant rules are known.

Applicable mandatory rules and project checks remain binding. Conditional reading
does not waive them. A combined profile applies only its relevant components;
its name or bundled dependencies do not require adding a language or framework.

| Task | Relevant reading | Not selected merely by the bundle |
| --- | --- | --- |
| Python-only fix, without FastAPI or Pydantic | Common rules and Python entry/sections for the affected behavior | FastAPI, Pydantic, SQLAlchemy or database instructions |
| JavaScript React change, without Next.js or TypeScript | Common rules, shared JavaScript guidance and the `react` entry/topics | TypeScript obligations, Next.js routes or Node.js server guidance |
| Substantive inline plan with an existing configured session selection | Adopted planning policy, relevant delivery/design rules and the selected skill's adaptations | Delegation and model setup merely because they are dependencies of delivery/Superpowers |
| Blueprint-only Unreal asset change | `unreal-engine` entry, affected gameplay/assets and verification sections; editor procedure when operating that provider | C++ details, networking or mandatory MCP installation |
| Source-only Unreal change | `unreal-engine` entry and affected C++/build sections | Editor setup or an external skill merely to edit source |
| GDScript-only Godot change | `godot` entry, affected architecture/GDScript/runtime and verification sections | C#, GDExtension, Python/Node application profiles or MCP installation |
| Godot scene/import or editor operation | `godot` entry, affected assets/runtime and verification sections; provider procedure when used | Every runtime topic, native compiler or a provider merely because scenes are involved |
| Generic C++ outside an Unreal project | Applicable common/project guidance | Unreal solely from a `.cpp` or `.h` filename |
| NestJS with TypeORM | NestJS and TypeORM entries, relevant integration/model/query sections | A different ORM, second domain model or every persistence section |
| NestJS without TypeORM | NestJS and the actual persistence profile | TypeORM solely from NestJS or an `*.entity.ts` filename |
| TypeORM without NestJS | TypeORM and its language dependencies | NestJS integration solely from TypeORM |
| Angular without NgRx | Angular entry, TypeScript and relevant Angular sections | NgRx, React/Next.js or Node.js server rules merely from TypeScript |
| Angular with classic NgRx Store | Angular and NgRx entries; Store/selectors and used Effects/Entity/Router Store sections | SignalStore migration or every optional NgRx package |
| Angular with SignalStore only | Angular and NgRx entries; state ownership, SignalStore and relevant verification | Classic Store/Effects, Router Store or ComponentStore installation |
| Compose-only local dependencies or dev/prod overrides | Docker entry and relevant Compose/environment sections | Image build, production deploy or mandatory application containerization |
| Python editor scripting in Unreal | Unreal editor workflow and relevant Python sections | FastAPI or other unused backend components |

Unreal descriptor globs are applicability hints, not a detector or a requirement
to touch the descriptor before selecting the profile. A declared target stack or
the actual project context also selects it. Keep every resource declared for
`unreal-engine` in [the catalog](catalog.toml) available; route by task, including
subsection routes for concurrency/networking/performance.
An independently opened target uses its reachable local entry and selected copies.

Godot selection likewise follows declared/evidenced project context, with
`project.godot` and related resource files as hints. Generic C# or C++ does not
establish Godot. Keep the complete `godot` resource set available, route by task
and retain actual engine/platform compatibility. C#/GDExtension sections are
conditional; an MCP server's language does not select a Python/Node application
profile. Importing instructions installs no engine or provider.

Angular/NgRx globs are hints too: modern suffix-free Angular files still select
Angular through declared/actual use, and NgRx globs cover both dotted names and
this library's hyphenated `<domain>-actions.ts` style; a generic `*.store.ts` or
`*-actions.ts` does not prove NgRx.

A rendered glob applies only after its profile is selected for the project.
SQLAlchemy and psycopg carry no `**/*.py` glob because most Python files in such a
project are not persistence work. PostgreSQL keeps `**/*.sql`: once PostgreSQL is selected, a
changed SQL file is normally the schema/query work its `when` covers, and migration
or query paths vary too much to narrow safely. SQL for another engine or a vendored
dump does not select PostgreSQL guidance.
NgRx resources cover alternative packages, not a requirement to install them all.

Profiles need not share an application architecture. Unreal selects an engine/editor
integration model, including lifecycle, reflection, assets and live editor state;
it is not a generic C++ alias. Apply shared principles through its engine contracts,
without importing unrelated backend/frontend profile patterns or check routines.

Independent setup or delegation triggers still follow their owning procedures.
Planning alone does not trigger them. For example, bundling
`core -> delivery-workflow -> superpowers -> orchestration -> model-configuration`
keeps the relevant procedures reachable; it does not make every code edit read
or execute all five procedures.
