# Docker build and runtime boundaries

Apply to container changes with the [core rules](core.md). Docker's presence does
not require an image build after every code or documentation edit. Keep application
behavior in the application; container configuration owns packaging and runtime wiring.

## Essential rules

- Record the context, base image, target platform, runtime command/user, configuration,
  ports and writable paths. Preserve the existing startup and shutdown contract.
- Use maintained, appropriate bases and reviewed dependency inputs. If pinning image
  digests, assign an update policy; a fixed digest does not maintain itself.
- Exclude credentials, caches and unrelated files from the context. Supply build
  secrets through the builder's secret mechanism, never persistent ARG/ENV or COPY.
- Separate build tooling from runtime dependencies when useful; stages and shared
  base images need a concrete purpose. Containerization does not create domain layers.
- Own process signals, dependency recovery and persistent data explicitly. A running
  container, a passing probe and a successful business operation are different claims.
- Validate the affected build/runtime scenario under the shared verification policy.
  Do not publish images or change deployment settings during an ordinary local edit.

## Read for the task

Read only relevant sections and stop when their rules are known; do not load all
links recursively. Separate examples are optional, not automatic reading routes.

| Task condition | Read |
| --- | --- |
| Dockerfile, context, base/dependencies, stages, secrets or cache | [Build and context](docker/build-context.md) |
| Command, user, permissions, signals, shutdown, probes or resource limits | [Runtime and lifetime](docker/runtime-lifetime.md) |
| Compose configuration, service dependencies, networks, mounts or durable data | [Compose and integration](docker/compose-integration.md) |
| Local dev loop, Watch/bind mounts, environment overrides or production Compose | [Development and production](docker/development-production.md) |
| Tool versions, migration, platform support or choosing checks | [Verification and compatibility](docker/verification-compatibility.md) |

## Basis

Checked **2026-09-22** against official Docker documentation. Guidance targets
Linux containers, BuildKit where used, and the current Compose Specification;
feature support depends on installed tools. Compose example validation used 2.40.3;
no image was built or run. Existing detection fixtures are not production recipes.
Evidence: framework source `docs/research/2026-09-22-docker-engineering-practices.md`
(optional research).

[Development/production research](../docs/research/2026-09-27-docker-development-production.md)
extends this on **2026-09-27** with explicit environment composition and a
[Node/Nest example](docker/examples/development-production.md). Production Compose
is conditional on the host, availability and operations contract; it is not a
default instruction to deploy or a substitute for multi-host orchestration.
