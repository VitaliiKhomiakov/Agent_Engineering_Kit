# PostgreSQL migrations and verification

Read for schema/data evolution, server upgrades or selecting evidence for a change.
Use the shared [verification policy](../verification.md) for proportional checks.

## Change the deployed contract deliberately

Preserve migration compatibility and existing data. Assess locking and rollback
consequences before changing live schema. Ordinary development does not authorize
executing migrations against production.

Use the project's migration owner and order. For rolling deployments, add compatible
schema first, deploy compatible readers/writers, backfill with resumable bounded work,
validate, and remove old behavior only after its callers retire. This sequence is a
recommended response to overlap, not a mandatory multi-release ritual for an empty
local table. Backfill from an authoritative mapping; an invented default can corrupt
the meaning while satisfying the type. Estimate row rewrites, lock acquisition/hold,
replica impact, WAL/disk and abort/restart behavior.

A supported `NOT VALID` constraint protects new writes before scanning historical
rows. On 16, use it for CHECK/foreign keys; the
[online example](examples/online-constraint.md) stages a CHECK before SET NOT NULL.
The 18 interface also supports not-null constraint forms unavailable in 16.
Validation and initial addition have different locks; neither means no blocking.
Use bounded lock/statement timeouts and commit separate phases as intended.

`CREATE INDEX CONCURRENTLY` keeps ordinary writes possible but does more work, waits
for transactions and cannot run inside a transaction block. Verify the migration
runner's actual transaction mode. A failed build can leave an invalid index; inspect
and deliberately repair/drop it before retry. A matching name with IF NOT EXISTS
does not prove a valid matching definition. Where eligible, attach a concurrent
unique index as a constraint; partial/expression indexes cannot be attached this way.

Distinguish application rollback, transactional DDL rollback and recovery of dropped
or transformed data. Some migrations need a forward repair or restore plan. Do not
claim a down migration can recover lost information. Coordinate logical subscribers,
extensions and collations when those contracts are affected.

## Version and test evidence

Record server major/minor, extension and driver/tool versions, pool mode, locale and
migration runner semantics. Verify server capabilities directly when available.
Major upgrades require their migration procedure and intervening release notes;
minor updates also require release-note review. PostgreSQL 18 features such as native
`uuidv7`, virtual generated columns, temporal constraints and skip scan are optional
choices, not compatible defaults for the initial PostgreSQL 16 fixture.

For changed SQL, use a real supported PostgreSQL version: a mock or SQLite does not
establish PostgreSQL locking, SQLSTATE, type or DDL behavior. Cover affected required/
invalid values, constraints and rollback. For a concurrency contract, interleave
separate connections deliberately and assert committed outcomes; observe a wait or
synchronize milestones rather than trusting a timing sleep. For RLS, exercise both
allowed and denied cases as a non-owner runtime role. For migrations, check existing
data, old/new writers where relevant, failed validation/builds, restart and final
catalog state. Use representative plans/load only when performance is a requirement.

The optional examples have executed SQL/controlled concurrency evidence, not a
production load, real driver/pool, RLS deployment or recovery rehearsal. These limits
must accompany reuse. A synthetic policy bundle proves portable resources, not that
a native assistant actually reads only the relevant sections.

Basis: [16 ALTER TABLE](https://www.postgresql.org/docs/16/sql-altertable.html),
[18 ALTER TABLE](https://www.postgresql.org/docs/18/sql-altertable.html),
[concurrent indexes](https://www.postgresql.org/docs/18/sql-createindex.html),
[version policy](https://www.postgresql.org/support/versioning/), and
[18 release](https://www.postgresql.org/docs/18/release-18.html).
