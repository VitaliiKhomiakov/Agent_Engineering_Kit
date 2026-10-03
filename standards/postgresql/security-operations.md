# PostgreSQL security and operations

Read for access control, multi-tenancy, pool/session behavior or deployment/recovery.

## Identity, privileges and object resolution

Separate application DML privileges from migration/ownership administration. Do not
run ordinary requests as superuser or a role with BYPASSRLS. Authorize operations in
the application and bind tenant identity from trusted context; a submitted tenant ID
is not proof of authority. A tenant-scoped foreign key protects references, not access.

Row-level security is optional defense for an actual isolation model. Define both
visible rows and permitted new row values, enable it deliberately and test as the
real runtime role. Owners normally bypass policies unless FORCE ROW LEVEL SECURITY
applies; superusers/BYPASSRLS remain exceptional. Referential integrity checks can
reveal information through errors. RLS is not an excuse to grant broader privileges.
A session variable settable by the same untrusted SQL role is not authenticated
identity. Review how pooled transactions obtain and clear their context.

Restrict CREATE in trusted schemas and control `search_path`; an untrusted object
can change name resolution. Qualify sensitive object references. Prefer invoker
rights for routines; use SECURITY DEFINER only for a specific privilege boundary,
with a trusted path (including safe `pg_temp` placement), narrowly granted EXECUTE
and an audited owner. Schema separation alone does not enforce a service boundary.

For remote connections, use the actual driver's TLS verification and authentication
contract; libpq `verify-full` verifies hostname and trust chain. Do not copy local
trust authentication into a deployed service. Keep credentials and parameter values
out of ordinary logs; query text/plans may also contain sensitive data.

## Resource budgets and diagnosis

Bound the aggregate connection budget across application replicas and workers.
Pool acquire time, statement time, lock waits and idle-in-transaction lifetime are
different budgets. Prefer operation-local settings where supported; session-level
state, prepared statements, temporary objects and session locks must match the
pooler mode and cleanup policy. Cancellation is not proof that a write did not commit.

Start diagnosis from active transactions, blockers/wait events, error rates, disk/WAL
and query evidence. Keep autovacuum and statistics maintenance effective; long-lived
snapshots and replication slots can retain tuples/WAL. Plain VACUUM reclaims space
for reuse; VACUUM FULL rewrites and locks, so it is not a routine latency fix.
Tune from evidence and capacity, not copied universal constants.

## Recovery and replication

Define acceptable data loss and recovery time, then select backups/WAL retention and
prove a restore into an isolated target. Replication is not protection from accidental
deletes. A successful backup command alone proves no recovery objective. For PITR,
retain a usable base backup, the required WAL chain and configuration/credentials.
Test monitoring of archival failures and retention before relying on the design.

Replicas may lag; route reads requiring current post-write state appropriately.
Failover needs fencing, reconnection and uncertain-outcome handling. Logical
replication does not automatically copy DDL or sequence state; plan those explicitly
for migrations and switchovers. Do not introduce replication for a simple local task.

Basis: [row policies](https://www.postgresql.org/docs/18/ddl-rowsecurity.html),
[schemas](https://www.postgresql.org/docs/18/ddl-schemas.html),
[function security](https://www.postgresql.org/docs/18/sql-createfunction.html),
[TLS](https://www.postgresql.org/docs/18/libpq-ssl.html),
[timeouts](https://www.postgresql.org/docs/18/runtime-config-client.html),
[vacuum](https://www.postgresql.org/docs/18/routine-vacuuming.html),
[recovery](https://www.postgresql.org/docs/18/continuous-archiving.html), and
[logical replication limits](https://www.postgresql.org/docs/18/logical-replication-restrictions.html).
