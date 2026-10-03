# Compose and integration

Read when changing a Compose service contract, connectivity or data lifetime.
Container configuration wires application boundaries; it does not enforce domain
invariants or replace database transactions. See the [entry](../docker.md).

For environment file composition, source sync, development dependencies or
production releases, read [development and production](development-production.md).

## Configuration and dependencies

Treat environment values as external input: the application parses and validates
its named configuration contract. Use required interpolation for required deployment
values; do not silently invent successful defaults. Quote ambiguous YAML scalar values.
Compose `.env` interpolation and a service's `env_file`/`environment` are distinct;
an interpolation value is not automatically a variable in the container. `$$` escapes
Compose interpolation when a value must reach a container-side shell literally.

Short `depends_on` orders startup without proving readiness. Use `service_healthy`
with a meaningful dependency probe when startup truly requires it; a successful
one-shot prerequisite can use `service_completed_successfully`. Applications still
need bounded reconnect/failure handling after startup. Nested `depends_on.restart`
concerns explicit Compose dependency operations, not continuous health supervision.
Run migrations through their agreed owner; parallel replicas must not race a shell
startup migration merely because containers can start together.

Prefer file-based secrets when supported by the application. A `_FILE` variable is
an image/application convention, not a universal Compose feature. Local file-backed
Compose secrets rely on host-file access/bind mounts, not an encrypted secret store;
do not assume uid/gid/mode remapping works for that source. Check actual access without
logging secret values. Rendered configuration can expose sensitive environment values.

## Network and storage

Use service DNS names and container ports for peer connections, not ephemeral IPs
or host-published ports. `localhost` inside a container names that container. Publish
only needed host endpoints and choose the bind address deliberately; local development
normally uses loopback. EXPOSE documents a port; it does not publish it. Account for
Engine version and host routing/firewall behavior when relying on network isolation.

Put durable state in the project's deliberate volume/storage contract; container
replacement must not discard it. Use bind mounts for intentional host coupling and
tmpfs for disposable state. Mounting over an image path can hide its contents. Check
ownership, database compatibility, backup/restore and migration procedures; a volume
is not a backup. Do not use `down -v`, volume pruning or data-directory replacement as
routine troubleshooting. Docker does not make multiple writers transaction-safe.

Optional illustration: [a local Compose contract](examples/compose-contract.md).
Basis: [interpolation](https://docs.docker.com/reference/compose-file/interpolation/),
[startup order](https://docs.docker.com/compose/how-tos/startup-order/),
[secrets](https://docs.docker.com/compose/how-tos/use-secrets/),
[service options](https://docs.docker.com/reference/compose-file/services/),
[networking](https://docs.docker.com/compose/how-tos/networking/),
[port publishing](https://docs.docker.com/engine/network/port-publishing/), and
[volumes](https://docs.docker.com/engine/storage/volumes/).
