# Doctrine ORM/DBAL engineering practices

Research and verification date: **2026-09-21**. K08 of the approved
[practice plan](../plans/2026-09-21-engineering-practices.md), following completed
PHP and Symfony work. The [combined profile](../../standards/php-symfony-doctrine.md)
is the short entry; its Doctrine sections and examples are conditional resources.
This note is evidence, not a required context expansion or an installed resource.

Strength labels: **R** = library contract required when using that feature, with
its project correctness reason stated; **D** = recommended project default;
**O** = optional technique justified by the problem. Existing
[core policy](../../standards/core.md) owns boundaries, named contracts, meaningful
construction and invariant placement. Doctrine does not mandate a universal DDD,
Repository, service-bus or second-model architecture.

## Applicability and versions

The directly opened [ORM release page](https://www.doctrine-project.org/projects/orm.html)
listed **3.7.1 stable**, 3.6.9 unmaintained and 4.0/3.8 upcoming. The
[DBAL release page](https://www.doctrine-project.org/projects/dbal.html) listed
**4.4.4 stable**, also a stable 3.10.6 branch, and 5.0/4.5 upcoming. An initial search
snippet still described ORM 3.6.8 as current and 3.7 as upcoming; direct release
pages and installed locks resolved that discrepancy. Do not infer project version
selection or branch support from a cached snippet or an unversioned tutorial.

Installed package manifests confirmed ORM 3.7.1 accepts PHP `^8.1` and DBAL
`^3.8.2 || ^4`, while DBAL 4.4.4 requires PHP `^8.2`. Our temporary fixtures use
PHP **8.3.6 CLI NTS**, Composer **2.10.3**, PHPStan **2.2.14**, PDO SQLite and SQLite
**3.45.1**. The ORM fixture also resolved Collections **2.6.0**, Persistence **4.2.0**
and Symfony Cache **7.4.19**. Direct dependencies belong in the fixture manifests;
using Symfony Cache does not mean the fixture uses the Symfony web framework.

Native lazy objects need PHP 8.4. ORM 3.7.1's `ORMSetup` source and
[configuration reference](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/advanced-configuration.html)
distinguish `createAttributeMetadataConfig()` from the older
`createAttributeMetadataConfiguration()` used by the PHP 8.2/8.3 fixture. Final or
readonly entity advice is therefore conditional on the lazy mechanism. No native
lazy objects or PHP 8.4 execution was performed. ORM 4's future requirements are
not the current project's baseline.

[ORM 3.7 upgrade notes](https://github.com/doctrine/orm/blob/3.7.1/UPGRADE.md), also
inspected in the installed archive, describe changes to `LockMode::NONE`, the old
Paginator and Collections 3 integration. In particular, NONE no longer refreshes
a managed identity; code needing refresh must say so. New offset/cursor APIs do
not justify automatically rewriting an older supported application's queries.
Check the relevant [DBAL upgrade notes](https://github.com/doctrine/dbal/blob/4.4.4/UPGRADE.md)
and dependent integrations for the project's actual transition.

## 1. Architecture and responsibility

**Problem:** confusing persistence mapping with either a ban on behavior or a
requirement to create a complete domain hierarchy. **D:** preserve the approved
`mapped-rich` or `separate-domain` approach, using intent methods at the business
state owner and infrastructure for persistence. Separate models are **O** when
independence, representation or lifecycle merits conversion cost. A simple read
projection needs no rich counterpart.

The [Doctrine getting-started tutorial](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/tutorials/getting-started.html#adding-behavior-to-entities)
recommends rich entities and illustrates other designs. That preference is not a
runtime requirement, a reason to ban accessors, or permission to inject services
into entities. The existing project policy also keeps independent core contracts
free of EntityManager and lazy query machinery. Its model-placement text is
preserved verbatim in the new conditional section.

[DBAL introduction](https://www.doctrine-project.org/projects/doctrine-dbal/en/4.4/reference/introduction.html)
confirms independent DBAL use. This makes a DBAL adapter a valid simpler choice
for SQL projections or atomic row operations. Adopting it for one operation does
not select ORM, a framework or a wholesale persistence rewrite.

## 2. Construction, dependencies and useful patterns

**D:** instantiate ordinary entities/values directly; centralize real creation
rules with an appropriate constructor or factory. Inject persistence services at
infrastructure assembly. Doctrine's existing finders can handle simple retrieval;
a consumer-owned repository port is **O** for a genuine architectural boundary.
A generic CRUD wrapper for each mapped table adds indirection without necessarily
protecting any contract.

**R:** ORM hydrates without invoking the entity constructor; creation checks do
not validate every historical row. The [architecture reference](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/architecture.html)
also distinguishes the entity and persistent collection contracts. Thus a record
adapter or mapped domain model needs coherent mapping and stored-data guarantees,
not side-effectful constructor assumptions. Keeping multiple managers explicit
costs wiring but avoids accidentally writing to the wrong persistence context.

Entity lifecycle callbacks remain **O** for small lifecycle-local work. They are
not the owner of an application use case. This applies independently of whether
the application uses Symfony service registration.

## 3. Mapping, types, validation and errors

**R:** property nullability, column metadata and database constraints are separate
contracts. **D:** specify persistent meaning and validate the affected round trip;
use input validation for external shape and domain methods for state transitions.
The [basic mapping guide](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/basic-mapping.html)
explains metadata/default/type inference; nullable PHP types do not by themselves
make a column nullable. An ORM attribute is not an executed Validator path.

[DBAL types](https://www.doctrine-project.org/projects/doctrine-dbal/en/4.4/reference/types.html)
distinguishes decimal strings from approximate floats and DBAL 4 bigint's range-
dependent int/string conversion. Plain SQL results are a different boundary.
**D:** decode once into a meaningful scalar/projection; separate absence from
NULL/zero and classify recognized conflicts without translating every database
error into the same public failure. **O:** custom types/embeddables for repeated
value semantics; simpler scalars avoid conversion and schema-comparison overhead.

The local examples intentionally use bounded integer stock. They are not a money,
JSON-schema, timezone or large-identifier model. Those representations need their
own driver-specific evidence when a task changes them.

## 4. State, associations and concurrency

**R:** the identity map can return an existing managed instance; `persist()` and
`flush()` have different effects. **D:** make the operation own its unit of work,
and clear/recreate before assertions intended to read stored state. Workers need
an actual reset/lifetime boundary and fresh dependencies after manager reset.
The [object reference](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/working-with-objects.html)
provides these semantics; its per-request examples are not permission to share
one context among independent worker jobs or overlapping tasks.

**R:** association updates follow the owning side; **D:** keep both sides coherent
when the same operation reads them. Unidirectional navigation is the simpler
alternative. Cascades and orphan removal are **O** for actual ownership, with
hydration/deletion costs. [Association guidance](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/working-with-associations.html)
also explains why exposing or converting a whole collection has consequences.

**O:** optimistic versions, conditional writes or pessimistic locks according to
contention and consistency needs. An invariant checked in a stale PHP object
cannot alone prevent lost updates. Preserve a user's expected version across
requests; use target-platform tests for lock/isolation behavior. Our real SQLite
interleaving demonstrates the optimistic conflict, not concurrent lock scheduling.

## 5. Transactions and integration effects

**R:** ORM `wrapInTransaction()` flushes and handles failed-context closure; DBAL
`transactional()` coordinates its connection only. **D:** choose one outer owner,
keep it short, propagate meaningful failures, and replace a closed manager for
new work. A database rollback does not restore PHP state. These are specified by
[ORM transactions](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/transactions-and-concurrency.html)
and the versioned [EntityManager source](https://github.com/doctrine/orm/blob/3.7.1/src/EntityManager.php),
and exercised by our rollback/conflict/constraint cases.

**R:** DBAL 4 nested transactions use savepoints; the outer commit remains decisive.
Do not mix raw PDO transaction controls with DBAL's tracked state.
[DBAL transactions](https://www.doctrine-project.org/projects/doctrine-dbal/en/4.4/reference/transactions.html)
also documents error categories. **D:** retry only understood transient failures
when the complete operation can safely repeat, with fresh state and a bounded
budget. Duplicate constraints are not generically transient; ambiguous commits
need reconciliation rather than blind repetition.

**O:** a durable handoff/outbox when external delivery must accompany a database
write; simpler in-process completion suffices where no such guarantee exists.
[ORM events](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/events.html)
place several post events inside flush and forbid unsafe flush re-entry. An event
name therefore does not establish outer commit or make an email rollbackable.

## 6. Testing and review

**D:** use direct business tests for intent methods and real persistence tests for
mapping, queries, constraints and rollback. A mock call sequence is cheaper but
cannot establish the database's behavior. Mapping validation, schema comparison
and behavioral tests have different coverage. Match checks to changed paths under
the shared policy rather than importing Doctrine contributor gates wholesale.
The [DBAL testing guide](https://www.doctrine-project.org/projects/doctrine-dbal/en/4.4/reference/testing.html)
explains the role of actual drivers/platforms for externally defined semantics.

The ORM example verifies a reload after clear, two independently read versions,
a failed outer transaction after an executed flush, uniqueness and manager
replacement. The independent DBAL example verifies acceptance/refusal, bound
SQL-like values, absence versus zero, rollback of the first write after a second
write fails, and rejection of nesting without disturbing the caller's transaction.
SQLite does not prove PostgreSQL/MySQL locking, migration deployment or all scalar
representations. Keep that cost/coverage distinction explicit in project reviews.

## 7. Security, performance and operations

**R:** placeholders bind values, not arbitrary SQL structure. **D:** allowlist
sort/filter expressions and preserve tenant/authorization predicates in every
query path. DBAL's [QueryBuilder reference](https://www.doctrine-project.org/projects/doctrine-dbal/en/4.4/reference/query-builder.html)
and [retrieval API](https://www.doctrine-project.org/projects/doctrine-dbal/en/4.4/reference/data-retrieval-and-manipulation.html)
explain parameter positions, array expansion and raw result conversion. Fixed
parameterized SQL is often simpler than a generic dynamic query language.

**D:** inspect the SQL/row shape for the actual operation. Fetch joins or explicit
projections are **O** responses to observed N+1; globally eager graphs exchange
query count for hydration/row multiplication. [Pagination](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/tutorials/pagination.html)
handles root identity and introduces version-specific APIs. Offset/cursor choice
also depends on product navigation and ordering, not only a benchmark claim.

**O:** bounded iteration/flush/clear for large jobs, bulk SQL/DQL where its bypass
of entity behavior is acceptable, and result caching with explicit scope/freshness.
[Batch guidance](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/batch-processing.html)
warns about collection fetch joins and driver buffering;
[DQL semantics](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/dql-doctrine-query-language.html)
explain bulk lifecycle/version differences. Include cache/context reconciliation.
Metadata/query caches do not establish a business result's freshness; avoid logging
sensitive bound values while collecting performance evidence.

## 8. Migration and existing-project compatibility

**D:** preserve mappings/architecture during ordinary changes. Check autoload,
discovery, DI and proxies after file moves before deciding a schema change exists.
When it does, review generated SQL against intended data meaning, ownership and
deployed-version compatibility. **O:** staged expansion/backfill/contraction for
rolling compatibility; a simple reviewed migration may be sufficient otherwise.

[ORM tools](https://www.doctrine-project.org/projects/doctrine-orm/en/3.7/reference/tools.html)
reserves SchemaTool for development rather than production migration. Its mapping
validator skips some checks, so a pass is not a complete mapping proof.
[Migrations generation](https://www.doctrine-project.org/projects/doctrine-migrations/en/3.9/reference/generating-migrations.html)
can include drops for unmapped tables and supports DBAL-only schema providers.
Review/filter ownership and data operations; a generated diff is not execution
approval or an understanding of a rename/backfill.

**R:** transactional settings cannot override platform DDL behavior. Doctrine
Migrations 3.9's [implicit-commit explanation](https://www.doctrine-project.org/projects/doctrine-migrations/en/3.9/explanation/implicit-commits.html)
uses MySQL/Oracle cases to motivate DML/DDL separation. Recovery, irreversible data
changes, migration ordering and lock duration remain project decisions. Migrations
was researched but not installed or executed in this stage.

## Adoption and evidence

The existing profile ID and selection metadata remain unchanged. Discovery
recognizes `doctrine/orm`; a DBAL-only Composer manifest currently supplies the
PHP fact, which still selects the combined profile. No separate DBAL technology
fact is claimed or added. Four conditional
Doctrine sections and two optional examples are added as explicit catalog
resources. The entry gates ORM reading on actual ORM use, preserves PHP/Symfony
routes and essentials, and retains the framework file-move obligation. Research
is linked as optional framework-source evidence and is not copied into bundles.

The two examples are intentionally different: mapped entity/unit-of-work behavior
and standalone SQL transaction ownership. They use ordinary constructors and
infrastructure dependencies without factory/repository scaffolding. Exact PHP and
Composer snippets are extracted from the tested temporary projects. The recorded
[stage result](../plans/2026-09-21-engineering-practices.md#k08-result-and-verification)
owns commands, scope hashes, delivery checks and the user's next checkpoint.

Initial ORM PHPStan diagnostics identified callback parameters narrower than the
library's `EntityManagerInterface` contract and an unreachable assertion after an
always-throwing callback. The example now uses the published callback interface
and checks the original propagated failure without dead code. Runtime persistence
cases passed; the corrected static check also passed without suppression.

PHP's initial stream-based Composer access timed out while curl could retrieve
the same public metadata. A matching, checksum-verified PHP curl module and IPv4
transport completed the temporary installs. SQLite/curl modules were extracted
under `/tmp`; nothing was installed system-wide. This is setup evidence, not an
application change or a reason to require curl in a Doctrine consumer.

No association example, benchmark, multi-PHP/driver matrix, production database,
lock/deadlock/network-failure experiment, migration deployment, external-project
installation or live native-client pilot was performed. Synthetic composition
can verify conditional routes and portability, not actual model reading behavior
or token savings. K09 JavaScript and P3–P7 native adoption remain unstarted.
