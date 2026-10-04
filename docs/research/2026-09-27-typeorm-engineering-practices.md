# TypeORM engineering practices and rich domain models

Researched **2026-09-27** in response to the user's request to extend the library
like Doctrine, with rich domain behavior and no generated attribute setters.
The [profile](../../standards/typeorm.md) owns the entry routes. This is optional
source evidence, not a required document in adopted bundles.

## Scope and decisions

Existing Doctrine/core policy already assigns invariants to intent methods. The
gap was TypeORM-specific persistence/hydration rules and conditional selection
from NestJS. This change retains the short-entry/detail/example structure and
adds TypeORM independently of Nest. It does not select an ORM for an existing app,
change dependencies in a target project, or mandate a second domain model.

The framework requires rich behavior for business state and atomic in-memory
validation of coupled changes. `mapped-rich` and `separate-domain` describe where
that behavior lives, not whether it exists. DTO/read/storage records may remain
data. A one-field operation can express valid business intent. These are the
user's architectural rules; TypeORM itself offers both Active Record and Data Mapper.

## Evidence and instruction owners

| Official primary source | Finding applied in the library | Owner |
| --- | --- | --- |
| [Entities](https://typeorm.io/docs/entity/entities/) | Optional constructor inputs for hydration; explicit types and column contracts | Models/mapping |
| [Data Mapper and Active Record](https://typeorm.io/docs/guides/active-record-data-mapper/) | Persistence can stay outside mapped classes; behavior does not require Active Record | Models/mapping |
| [Repository API](https://typeorm.io/docs/working-with-entity-manager/repository-api/) | Assignment helpers and partial writes do not call domain intent methods; save has its own write boundary | Models/transactions |
| [Transactions](https://typeorm.io/docs/transactions/) | Use the supplied manager throughout the transaction and own connection cleanup | Transactions/lifetime |
| [Custom repositories](https://typeorm.io/docs/working-with-entity-manager/custom-repository/) | Transaction repositories must be obtained/rebound in that scope | Transactions/lifetime |
| [QueryBuilder](https://typeorm.io/docs/query-builder/select-query-builder/) | Parameter binding, loading shape, locks and pagination need explicit choices | Queries/transactions |
| [Null handling](https://typeorm.io/docs/data-source/null-and-undefined-handling/) | High-level filter validation does not cover direct QueryBuilder predicates or omitted keys | Queries/relations |
| [Relations](https://typeorm.io/docs/relations/relations/) and [relation FAQ](https://typeorm.io/docs/relations/relations-faq/) | Relation ownership, cascade scope and unloaded-vs-empty state matter during save | Queries/relations |
| [Listeners/subscribers](https://typeorm.io/docs/listeners-and-subscribers/) | Persistence hooks are distinct from application operations and durable remote effects | Models/transactions |
| [Migration setup](https://typeorm.io/docs/migrations/setup/) and [execution](https://typeorm.io/docs/migrations/executing/) | CLI artifact/discovery and transaction mode must suit the deployment | Schema/verification |
| [Nest database options](https://docs.nestjs.com/techniques/database) and [integration](https://docs.nestjs.com/data/typeorm) | Named sources, feature registration and auto-load limitations; TypeORM remains optional | Nest integration |
| [Upgrade from 0.3 to 1.0](https://typeorm.io/docs/releases/1.0/upgrading-from-0.3/) | Null defaults, orphan behavior and discovery/naming changes require version checks | Entry/schema/queries |

These are moving manuals, not evidence of a target project's installed versions.
Current documentation advertises 1.0. Executable example verification below uses
an explicitly pinned 0.3 version; no 1.0 compatibility execution is claimed.

## Alternatives and boundaries

- `mapped-rich` minimizes conversion when mapping dependencies are acceptable;
  `separate-domain` pays mapping cost for a meaningful independence or representation
  requirement. Preserve existing placement; clarify an unresolved material choice.
- TypeScript private fields and named creation methods can support rich mapping.
  They do not make ORM hydration a business transition, enforce runtime secrecy,
  or make ECMAScript private slots suitable for default property mapping.
- DataSource/manager operations are not Doctrine's identity map and deferred flush.
  Database rollback does not restore JavaScript state. The example verifies this
  difference rather than merely translating Doctrine API names.
- Row locks, conditional versioned writes and suitable isolation are alternatives
  selected by the actual invariant. Incrementing a version field alone is not a
  complete conflict protocol. Bulk operations need an explicit invariant-preserving
  contract; unrestricted request-to-record patches remain prohibited.

## Executed checks and limits

Checks use a temporary harness outside the library, with **Node 24.13.0,
TypeScript 5.9.3, TypeORM 0.3.27, reflect-metadata 0.2.2 and sql.js 1.13.0**.
Dependencies were installed only in that harness with lifecycle scripts disabled;
the library gained no package manifest, runtime dependency or test runner.

The exact two TypeScript blocks in
[rich booking](../../standards/typeorm/examples/rich-booking.md) were extracted and
compiled with `strict`, legacy decorators and metadata enabled. Compilation passed.
The executed sql.js check passed: invalid/equal/reversed intervals preserve the old
state; mutating a caller Date does not mutate the model; save/reload retains values
and methods; null/undefined IDs throw with explicit configuration; a transaction
failure rolls back the row but leaves the mutated JavaScript object changed;
a reloaded cancelled booking rejects rescheduling; SQL rejects a zero-length interval.

The PostgreSQL locking operation was compiled, not executed. No target database,
Nest container, deployed migration or production concurrency check ran. sql.js
does not establish those guarantees. A target project uses its own affected checks.

Artifact checks passed: TOML parses, all 165 catalog paths exist, profile IDs and
dependencies are valid, and all 154 local links in the 23 changed files resolve.
Conditional dependency checks passed for Nest+TypeORM, Nest-only, TypeORM-only
and Docker-only selection. Scoped review found no unresolved material issue;
the example's public interval result was aligned with the existing named-interface
policy and recompiled. No rule permits attribute setters, global repositories in
a transaction, or implicit schema synchronization on persistent environments.

Pre-edit contents/absence for this combined TypeORM/Docker task were saved at
`/tmp/af-typeorm-docker-gty94pab/before` with its `manifest.json`. The checkout has
no usable Git metadata; review uses those scoped copies and all listed new files.
This temporary evidence location is session-local, not a portable dependency.

## 2026-10-04 follow-up: ORM-01

Source review of the [repository API](https://typeorm.io/docs/working-with-entity-manager/repository-api/)
confirms that `save` skips undefined properties. The
[WHERE-value policy](https://typeorm.io/docs/data-source/null-and-undefined-handling/)
concerns criteria and does not select a write-time clear operation. Transactions
owns that distinction; mapping supplies a short nullable-contract route.

Reviewed three acceptance scenarios: omission retains the stored value, an
intentional nullable clear persists SQL NULL, and a required column rejects null.
They are checks for an affected adapter, not newly executed results. The guidance
preserves intent methods and does not generalize `save` semantics to every
update/upsert or driver. No example, entity, schema, dependency or database was
changed; the earlier 0.3.27 harness evidence does not establish these new scenarios.
