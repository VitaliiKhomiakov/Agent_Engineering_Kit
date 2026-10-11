# Reservation fixture architecture

This is a disposable design-observation fixture. No application runtime or
dependency installation is claimed. Declared target: Python 3.12, FastAPI 0.138.0,
Pydantic v2; preserve these constraints. Persistence is intentionally in memory.

`app/domain.py` owns stock and reservation state, protected by one inventory lock.
`app/http.py` maps HTTP input/output and errors. The inventory lives for the
process lifetime. This task does not introduce a database, queue or new dependency.
No shared library or ORM layer is planned. Source files are the current state;
the cancellation design is the requested target state.

Local profiles: `.agents-framework/standards/python.md`,
`.agents-framework/standards/pydantic.md`, `.agents-framework/standards/fastapi.md`.
Planning policy: `PLANS.md`. Canonical task: `docs/plans/cancel.md`.
Checks for future implementation: focused stock/idempotency/concurrency tests,
HTTP status/body tests, and strict Python analysis. No runtime check is needed
for the current design-only observation; record proposed checks as unexecuted.
