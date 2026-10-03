# Docker engineering practices: evidence and adoption

Researched **2026-09-22** for K18 of the [practice plan](../plans/2026-09-21-engineering-practices.md).
The [short entry](../../standards/docker.md) routes to four conditional sections and
two separate illustrations. Scope is agent instructions and their delivery, not a
new containerized application. K17's user-approved proportional verification applies.

## Evidence and version contract

Sources below are official Docker manuals/references, with npm's own manual for the
small installation fragment. These are moving documents, checked on the research
date; they are not evidence that every installed version supports every feature.
Locally observed: Docker CLI **29.1.3** and Compose **2.40.3**. `docker buildx version`
reports an unknown command. The daemon and BuildKit versions were not queried; no
daemon, image registry, builder installation or container is required for this stage.

Instructions target Linux containers, BuildKit where needed and the Compose
Specification. They do not prescribe a Docker/Compose upgrade. Build checks require
Buildx 0.15+ and were introduced with Dockerfile 1.8; the official page labels them
Beta. A moving frontend is separate from the Engine version. Windows and alternative
Compose implementations need explicit compatibility work before adopting these examples.

**R** means a framework requirement grounded in correctness, trust, ownership or
existing scope policy; **D** is a recommended default for the stated condition;
**O** is optional when useful. Docker behavior is evidence, not itself a mandate to
adopt every vendor recommendation. Core owns general architecture and verification.

## Coverage and adopted decisions

| Research area | Decision and instruction owner |
| --- | --- |
| Architecture/dependencies | D: packaging and runtime wiring outside business logic; cohesive service boundaries; entry/build/runtime |
| Idioms/construction | D: explicit context and dependencies; O: multi-stage/cache/reusable bases when useful; build |
| Contracts/validation/invariants/errors | R: explicit configuration/command/user/ports and application validation; Compose schema is not a domain validator; Compose/runtime |
| State/concurrency/cancellation/lifetime | R: signal, grace-period and data owners; replicas do not imply safe concurrent writes; runtime/Compose |
| Persistence/integrations | R: deliberate mounts, service addressing, dependency recovery and migration ownership; Compose |
| Testing/review | D: smallest reliable check for the changed contract; R: distinguish static validation from runtime evidence; verification |
| Security/operations/performance | R: protect credentials and authorized host access; D: non-root/limited writes where compatible; O: measured caching and platform strategies |
| Versions/migration | R: actual tool/frontend/platform matrix and explicit legacy migration; verification |

Typed application DTOs, SQL transactions and business invariants are not container
primitives. Their existing profile owners remain authoritative; no container-oriented
repository/factory/DTO layer is introduced to fill those research categories.

## Build decisions and alternatives

**Problem:** accidental context access and mutable dependencies hide build inputs.
**R:** record context and required artifacts; exclude credentials because the builder
is a trust boundary. **D:** explicit copies and maintained compatible bases.
[Context rules](https://docs.docker.com/build/concepts/context/) distinguish context
paths and Dockerfile-specific ignore precedence. [Build guidance](https://docs.docker.com/build/building/best-practices/)
supports narrower inputs and base updates. **Alternative/cost:** whole-repository
contexts can be necessary for a monorepo but need deliberate exclusions; tiny bases
trade tooling/library support for size. Digest pinning is **O** unless reproducibility
policy requires it, with **R** update ownership; a digest does not pin package servers.

**Problem:** compiler/test tools inflate the runtime image or stage reuse becomes a
framework of its own. [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
support **D** separation when a toolchain can be omitted. **Alternative/cost:** a single
stage is simpler for prebuilt artifacts; shared stages add release coupling. Copying
artifacts still requires compatible runtime libraries, user and platform. This is an
engineering choice, not a compulsory stage count or “one process” rule.

**Problem:** credentials survive in image history/layers or cache behavior is mistaken
for freshness. [Build secrets](https://docs.docker.com/build/building/secrets/) support
**R** transient secret delivery rather than ARG/ENV/COPY. **Alternative/cost:** public
dependencies need no secret; secret mounts require BuildKit and trusted consuming tools.
[Invalidation rules](https://docs.docker.com/build/cache/invalidation/) distinguish
cache keys from secret contents. **O:** scoped invalidation or a nonsecret revision
when a rerun is needed; never use secret values as cache-busting arguments.
The [npm fragment](../../standards/docker/examples/build-secret.md) preserves a matching
lockfile via [npm ci](https://docs.npmjs.com/cli/v11/commands/npm-ci/), with explicit
user/workspace/script-access assumptions. It is not a standalone build recipe.

## Runtime, integration and state decisions

**Problem:** shell/PID ownership breaks graceful shutdown or masks failure. The
[Dockerfile contract](https://docs.docker.com/reference/dockerfile/) supports **D**
exec-form commands and explicit wrapper handoff. **R:** preserve stop/deadline semantics
under ownership policy. **Alternative/cost:** wrappers/init can solve initialization
and child management, but application draining and uncertain operations remain in the
application. No wrapper makes SIGKILL transactional.

**Problem:** generic hardening breaks image initialization or promises isolation it
does not provide. [Engine security](https://docs.docker.com/engine/security/) and
[rootless mode](https://docs.docker.com/engine/security/rootless/) support **D** reduced
privilege, with **R** explicit host-access authorization. **Alternative/cost:** changing
USER, capabilities or writable paths can invalidate an image's initialization contract;
rootless deployment also has host requirements. [Resource constraints](https://docs.docker.com/engine/containers/resource_constraints/)
inform workload budgets; settings must match runtime worker/heap requirements rather
than universal numbers. No load, isolation or vulnerability claim is made here.

**Problem:** configuration validity, startup and readiness are conflated.
[Interpolation](https://docs.docker.com/reference/compose-file/interpolation/) supports
**R** required configuration where missing values would invalidate the deployment;
the application still validates types/ranges. [Startup order](https://docs.docker.com/compose/how-tos/startup-order/)
supports **O** health/completion gates for real prerequisites. **Alternative/cost:**
simple ordering suffices where startup tolerates unavailability; gates cannot prevent
later disconnects. [Restart policies](https://docs.docker.com/engine/containers/start-containers-automatically/)
govern exit recovery, not automatic restarts on unhealthy status. Application retry
and migration ownership remain separate.

**Problem:** host networking and storage shortcuts become accidental public/durable
contracts. **D:** service DNS/container ports and deliberate host publishing, based on
[Compose networking](https://docs.docker.com/compose/how-tos/networking/) and
[port publishing](https://docs.docker.com/engine/network/port-publishing/).
**Alternative/cost:** loopback publication suits local access, but version/host-specific
routing still matters. **R:** durable-state ownership under existing data-protection
policy. [Volumes](https://docs.docker.com/engine/storage/volumes/) support replaceable
containers; bind mounts deliberately couple to the host and tmpfs is disposable.
Neither volumes nor containers supply database isolation, migrations or backups.

**Problem:** local secrets are mistaken for a managed encrypted store.
[Compose secrets](https://docs.docker.com/compose/how-tos/use-secrets/) and
[service options](https://docs.docker.com/reference/compose-file/services/) support
**D** scoped file access where the application supports it. **Alternative/cost:** an
existing external secret manager may be appropriate; local file-backed secrets retain
host permission and UID mapping constraints. `_FILE` support is image-specific.
Avoid copying secrets into environment/log output merely to simplify an example.

## Verification, migration and reconciliation

**R:** claims match executed evidence under shared verification policy. **D:** artifact
checks for instruction changes and [Compose config](https://docs.docker.com/reference/cli/docker/compose/config/)
for syntax/interpolation. **Alternative/cost:** real builds/runtime checks are necessary
when changed image behavior warrants them; they are disproportionate for this stage's
illustrative fragment. [Build checks](https://docs.docker.com/build/checks/) are useful
where available but may access builder/registry metadata and do not execute build steps.
No mandatory new test harness or universal image-build gate is adopted.

[Compose version semantics](https://docs.docker.com/reference/compose-file/version-and-name/)
explain why a top-level version label does not enable features. **R:** inspect actual
installed behavior before migrating legacy invocations/configuration. **O:**
[multi-platform builds](https://docs.docker.com/build/building/multi-platform/) only
for required targets; cross-compilation/emulation/native workers have different costs.
A host-only build is insufficient evidence for target-specific native dependencies.

The existing `docker` profile retains its ID, core dependency, activities, technologies
and native globs. Six optional resources are added; no new profile, detector, runtime
code, templates or permanent tests. Discovery remains root Dockerfile, declared
technology or explicit selection. Compose-only automatic discovery is not implemented
by file globs; document explicit selection rather than silently expanding this stage.
Research stays outside generated instruction bundles, and copied sections/examples
are not additional automatic reading routes. K19 owns broader reconciliation.

Verification commands, results and limits are recorded once in the
[K18 result](../plans/2026-09-21-engineering-practices.md#k18-result-and-verification).
The stage checks configuration and instruction delivery, not an image build, secrets
against a real registry, runtime behavior or actual native-assistant reading adherence.
