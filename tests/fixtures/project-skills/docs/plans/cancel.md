# Reservation cancellation

Status: design requested; implementation is not authorized.
Canonical owner: this file. Instruction/execution root: the fixture root.
Mode: inline design, no Git actions, setup, delegation or dependency changes.

Outcome: design `POST /reservations/{id}/cancel`. First cancellation changes an
active reservation to cancelled and restores its quantity exactly once. Repeated
and concurrent cancellation returns the same cancelled representation with HTTP
200. ID and quantity are preserved; GET reflects the transition. Missing IDs
return 404 with `detail: reservation_not_found` and leave state unchanged.

Preserve existing endpoints, in-memory storage, locking, versions and dependencies.
Use current project files and applicable adopted rules. Record the design here,
including affected owners/interfaces, consequential alternatives and proposed
acceptance checks. Keep current facts separate from proposals and executed checks.

- [ ] CANCEL-DESIGN: Produce the reviewable design; no application implementation.
