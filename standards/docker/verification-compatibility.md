# Verification and compatibility

Read when selecting checks or changing tooling/platforms. Apply the shared
[verification policy](../verification.md) and [Docker entry](../docker.md).

## Check the affected contract

- Instruction/link/catalog edits need artifact and affected delivery checks. They
  do not justify a new application, a broad test suite or an image build by default.
- For Compose changes, render/validate the effective configuration with the real
  file order, profiles and intended nonsecret environment. `docker compose config
  --quiet` checks configuration; it does not run an application, check credentials,
  prove volume permissions or establish readiness. Keep sensitive renders out of logs.
- For dev/prod additions, check both exact file combinations. Inspect production
  for inherited source mounts, debug/database publishing, Watch and dev commands.
  Check missing required values fail. Watch/build/probe execution needs separate
  evidence; configuration acceptance does not establish those behaviors.
- For Dockerfile changes, inspect the context, stages and final image contract.
  Use existing build checks when supported, then build/run the affected scenario
  when its behavior requires it. Static checks do not prove dependency installation,
  secret non-disclosure or runtime correctness. Builder checks may resolve remote
  image/frontend metadata; “no build steps” does not mean “offline”.
- For runtime changes, focus checks on changed obligations: actual user/writable
  paths, readiness, shutdown, resource limits or persistence across replacement.
  Use disposable owned data when needed; do not publish or alter deployment settings
  as part of ordinary validation. Report unexecuted checks without implying a pass.

## Version and migration boundaries

Record Docker CLI and daemon separately, Compose, builder/Buildx, Dockerfile frontend,
base/digest, architecture and relevant host/Desktop mode. CLI version does not prove
the daemon or builder version. Windows containers require their own path/user/signal
contracts; these Linux-oriented examples are not a Windows recipe.

Target the Compose Specification and the installed `docker compose` implementation.
Top-level `version` is obsolete and does not enable newer features. For legacy
`docker-compose`/deployment migrations, inspect effective configuration, naming,
mounts and lifecycle behavior before changing invocations. Do not infer support from
a schema label or upgrade unrelated services to copy a new field.

BuildKit secret mounts need a compatible builder/frontend. Build checks were introduced
with Dockerfile 1.8 and require Buildx 0.15 or later; verify installed support. A moving
`docker/dockerfile:1` frontend can acquire new checks; strict CI needs a reviewed update
strategy. Multi-platform outputs need actual target-platform validation; emulation or
a successful host build does not prove native dependencies work on every target.

Select Docker from actual Dockerfile/Compose work, a declared technology or an
explicit profile choice, including Compose-only dependency environments. Catalog
globs are applicability hints, not an executable detector. Inspect the task and
project evidence; no removed framework CLI is required for profile selection.

Basis: [config command](https://docs.docker.com/reference/cli/docker/compose/config/),
[build checks](https://docs.docker.com/build/checks/),
[Compose version field](https://docs.docker.com/reference/compose-file/version-and-name/),
and [multi-platform builds](https://docs.docker.com/build/building/multi-platform/).
