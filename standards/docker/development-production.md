# Docker development and production

Read when designing a local container workflow or deploying Compose. Combine with
[build](build-context.md), [runtime](runtime-lifetime.md) and
[Compose wiring](compose-integration.md) only as the task requires.

## Choose the environment contract

| Environment | Suitable baseline |
| --- | --- |
| App runs on host, dependencies in Compose | Publish required dependency ports on loopback; host app uses those ports |
| App and dependencies run in Compose | Service DNS/container ports; source bind mount or Watch for app iteration |
| CI | Isolated project/data; repeatable locked build and commands; remove only owned disposable resources |
| Single-host production | Reviewed immutable images, explicit runtime configuration and operational ownership |
| Required multi-host failover or rolling availability | Evaluate a suitable orchestrator/managed platform; standalone Compose does not supply those guarantees |

Do not require all developers to containerize the application when dependency-only
Compose meets the project contract. Record the chosen commands, versions and data
lifetime so another developer can reproduce the environment.

## Development loop

- Build a development target with the required compiler, watcher and debug tools;
  retain a separate runtime target when those are unnecessary in production.
  Use the package manager's lockfile-based install, cache stable dependency inputs,
  and rebuild when manifests/lockfiles change.
- Choose source bind mounts for deliberate host coupling or Compose Watch for
  selective sync/rebuild. Avoid managing the same target through both mechanisms.
  Watch needs compatible Compose features, writable targets and image utilities;
  `sync` alone does not restart an application without its own reloader.
- Keep host `node_modules`, virtualenvs and native build artifacts out of Linux
  containers. A full-workspace mount can hide dependencies installed in the image;
  mount source paths selectively, or define a container-owned dependency volume
  and refresh policy. An old volume can hide newly built dependencies too.
- Listen on the intended container interface (often `0.0.0.0`) and publish local
  app/debug ports on loopback. Configure hot-reload/proxy URLs deliberately. Use
  service DNS inside Compose; a host-run app uses the published endpoint.
- Keep developer secrets outside source control and build context; commit only a
  nonsecret configuration example. Use profiles for optional debug/admin tools,
  not as a security boundary or a replacement for required service dependencies.
- Give parallel checkouts/CI runs distinct project names and nonconflicting host
  ports. Avoid fixed `container_name` and global volume names unless deliberate
  sharing is required. Reset only explicitly owned disposable data; never suggest
  `down -v` as routine startup repair.

## Compose file composition

Prefer a neutral `compose.yaml` plus explicitly selected `compose.dev.yaml` or
`compose.production.yaml`. The base should not contain source mounts, reload
commands or debug publishing that production must undo. Separate complete files
are acceptable for materially different environments, with drift checks on shared
contracts. Record the exact `-f` order and project name.

Merge is not blanket replacement: ports and other sequences may accumulate, while
mounts merge by target. Paths resolve against the first/base file for this workflow.
Render the actual combination and inspect it before use. Explicit `-f` selection
avoids accidentally loading a default development override. When truly needed,
use `!reset`/`!override` only with verified client support (`!override` requires
Compose 2.24.4+). Profiles do not erase settings on an enabled service.

## Production operation

Standalone Compose is a reasonable choice when one host and its failure/downtime
budget satisfy the service requirements. Record the host owner, ingress/TLS,
resource budgets, secret provisioning, backups/restore, monitoring and release
procedure. A Compose file alone is not evidence those operations exist.

Build/test the release artifact in CI or the agreed build environment and promote
the same immutable digest across environments. Do not deploy from a mutable source
bind mount, a dev server or an unreviewed `latest` reference. Runtime configuration
and secrets remain external. Do not rebuild separately on each production host
unless a documented deployment contract specifically requires it.

Use suitable non-root runtime images, bounded logs/resources and explicit writable
paths. Publish only ingress endpoints; database ports normally remain internal.
Local Compose file secrets are host-file mounts, not an encrypted secret service.
Backup and restore must cover persistent data and version-compatible recovery;
retaining a named volume is not a backup strategy.

Assign migrations to one release operation. Check their success before dependent
app rollout and avoid one migration process per replica. A repeatable one-shot
Compose service may use `service_completed_successfully`, but an old successful
container is not evidence that the new release's migrations ran. Recreate/run the
release's job explicitly and prevent concurrent deployments.

Define health, readiness, dependency recovery and restart separately. Production
commands must use the reviewed image, preserve volumes, and enforce bounded waits.
`compose restart` does not apply changed image/configuration; recreation via `up`
is needed. A replacement can interrupt traffic; healthchecks and `--wait` do not
provide rolling deployment or zero downtime. Roll back an image only if its schema
and data remain compatible; preserve the previous digest and a recovery procedure.

Optional: [development and production example](examples/development-production.md).
Basis: [production](https://docs.docker.com/compose/how-tos/production/),
[Watch](https://docs.docker.com/compose/how-tos/file-watch/),
[merge rules](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/),
[merge reference](https://docs.docker.com/reference/compose-file/merge/),
[services](https://docs.docker.com/reference/compose-file/services/) and
[restart command](https://docs.docker.com/reference/cli/docker/compose/restart/).
