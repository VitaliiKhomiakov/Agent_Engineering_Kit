# Docker development and production: extension evidence

Researched **2026-09-27** for the user's request for container/Compose development
and conditional production practice. Extends the
[2026-09-22 research](2026-09-22-docker-engineering-practices.md), preserving its
historical results. The [Docker entry](../../standards/docker.md) now routes to
[environment guidance](../../standards/docker/development-production.md).

## Gaps and adopted choices

Existing build/runtime/wiring guidance already covered secrets, signals, health
and volumes. Missing detail concerned the developer loop, environment composition
and the operating assumptions for production Compose. The new instructions offer
dependencies-only and full-container development, source mounts or Watch, and an
explicit base+dev/prod pattern. An optional Nest/npm example connects those choices.

| Official source checked | Applied finding |
| --- | --- |
| [Production](https://docs.docker.com/compose/how-tos/production/) | Single-host use with an explicit production configuration and release procedure |
| [Watch](https://docs.docker.com/compose/how-tos/file-watch/) and [Develop spec](https://docs.docker.com/reference/compose-file/develop/) | Sync/rebuild choices, writable target/utilities, version-gated features |
| [Multiple-file merge](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/) and [merge reference](https://docs.docker.com/reference/compose-file/merge/) | Ordered overrides, base-relative paths, sequence accumulation and explicit reset/replace semantics |
| [Build practices](https://docs.docker.com/build/building/best-practices/) | Separate dependency/build/runtime inputs and a maintained reviewed base |
| [Service reference](https://docs.docker.com/reference/compose-file/services/) | Runtime configuration, secrets, limits, logging and health have distinct contracts |
| [Startup order](https://docs.docker.com/compose/how-tos/startup-order/) | Dependency health/completion can gate startup but does not supervise later availability |
| [Secrets](https://docs.docker.com/compose/how-tos/use-secrets/) | Per-service file access; application/image owns `_FILE` interpretation |
| [Restart command](https://docs.docker.com/reference/cli/docker/compose/restart/) | Restart does not apply modified configuration |
| [Official PostgreSQL image](https://hub.docker.com/_/postgres) | Version-specific volume layout, bootstrap superuser, existing-data initialization and `_FILE` support |

The source documents describe supported mechanisms. Our neutral base, immutable
release promotion, least-privilege app credential and explicit operational owners
are framework choices for the requested scenario. They do not require Compose for
every project or authorize deployment during rule integration.

## Alternatives and failure scenarios

- Host application plus containerized dependencies can be sufficient. Full app
  containers improve environment consistency at the cost of file sync/permissions.
  Watch avoids copying host dependency trees but needs supported tools and a reloader;
  bind mounts remain useful for deliberate host coupling.
- A neutral base avoids having to erase dev-only values in production. Separate
  complete files are also valid if shared contracts are kept aligned. A later
  override does not necessarily remove a published debug port or source volume.
- Single-host Compose fits services that accept that host's failure and replacement
  downtime. Multi-host failover and rolling availability need another deployment
  mechanism; resource/health settings alone do not supply it.
- Database storage needs backup/restore and schema-compatible recovery. An older app
  digest is not a safe rollback after every migration. One-shot completion must
  refer to the current release, not a previously successful container.

## Executed checks and limits

The exact three YAML blocks from the
[development/production example](../../standards/docker/examples/development-production.md)
were extracted into an isolated temporary directory. **Docker Compose
2.40.3+ds1-0ubuntu1~24.04.1** accepted both base+dev and base+production with
`config --quiet`; JSON renders were inspected using synthetic values and a dummy
secret fixture. No real credentials were printed or used.

Checks passed for loopback app publishing, no database host port, service DNS,
dependency health gating and application access only to its designated secret.
Development selects the development build target and Watch initial sync.
Production has no active build, Watch, source mount or command override and uses
the specified image/read-only root. All **10** required-value refusal cases passed
(five per environment). Compose emits an unspecified command as JSON `null`;
the checker was corrected to test active overrides, without changing valid YAML.

The Dockerfile was reviewed for its documented input/stage/runtime contract;
no application was supplied or image built. Hot reload, secret permissions,
non-root startup, signals, app health, database provisioning and recovery were not
executed. Compose config does not prove these. No daemon operations, registry
publication, production deployment or volume changes occurred.

Artifact acceptance covers the expanded catalog resources/globs, affected local
links and the actual selected-profile closure. A Compose-only project is selected
from task/stack evidence: globs remain hints, not a detector or a restored CLI.
The [TypeORM note](2026-09-27-typeorm-engineering-practices.md) records the shared
pre-edit baseline for accountable scoped review. Research files remain optional
source evidence and need not be copied into every adopted bundle.
