# Runtime and lifetime

Read when changing how the container starts, runs or stops. Preserve the documented
command, configuration, user, ports, signals and writable paths from the [entry](../docker.md).

## Process ownership

Prefer exec-form ENTRYPOINT/CMD for the main executable. If a shell wrapper is needed
for small initialization, forward arguments and finish with `exec` so the application
receives stop signals. Do not move business operations into the wrapper. One cohesive
service may have worker children; “one process” is not a universal correctness rule.
Use a small init process when child reaping/signal forwarding requires it, not as a
substitute for application shutdown handling.

On Linux, plan for the configured stop signal and eventual SIGKILL. Let the application
stop accepting work, drain or cancel bounded operations and release resources within
the grace period. Forced termination cannot guarantee transaction completion or delivery
acknowledgement. The application owns replay/idempotency and uncertain outcomes.
Coordinate the grace period with real request/worker deadlines rather than increasing
it indefinitely to hide a hang. A probe must be bounded and available in the final image.

## Privilege and operations

Default application processes to a suitable non-root user when the image contract
permits it. Check file ownership and mounted paths with the actual UID/GID. A database
image may need its documented initialization behavior; blindly overriding USER can
break it. Rootless Docker changes daemon/container privilege and has host constraints;
it is distinct from USER in an image.

Avoid privileged mode, daemon-socket mounts and broad host mounts unless the actual
task requires and authorizes that host-level access. Review capabilities and use
read-only roots plus explicit writable mounts/tmpfs where compatible. Do not add
hardening flags mechanically without checking startup, temporary files and runtime
ownership. Keep secrets out of logs and baked configuration.

Set CPU/memory/process budgets for the real workload; worker counts and heap settings
must fit them. Record exit/OOM/probe evidence before raising limits or adding retries.
Use the project's log/metrics contract, with rotation/retention owned by operations.
Docker restart policies react to process exits; an unhealthy status alone does not
make a standalone Engine container restart. Health, restart and readiness policies
need separate meanings and owners.

Basis: [command and signal semantics](https://docs.docker.com/reference/dockerfile/),
[Engine security](https://docs.docker.com/engine/security/),
[rootless mode](https://docs.docker.com/engine/security/rootless/),
[resource constraints](https://docs.docker.com/engine/containers/resource_constraints/),
and [restart policies](https://docs.docker.com/engine/containers/start-containers-automatically/).
