# Build and context

Read when changing the image recipe or its inputs. The [entry](../docker.md) owns
the essential contract; language profiles own application dependencies and behavior.

## Inputs and stages

Declare the build context explicitly: COPY sources are relative to it, not simply
to the Dockerfile's directory. Keep the context narrow and review `.dockerignore`,
including any Dockerfile-specific ignore file that takes precedence. Exclude local
credentials, dependency caches and unrelated repositories without excluding required
lockfiles, workspace packages or generated inputs. Prefer explicit COPY inputs.

Choose a maintained base compatible with the application's ABI, native libraries,
certificates, timezone and debugging needs. A smaller image is useful only if it
can run the supported workload. Do not mandate Alpine, scratch or a custom base.
Record tags/digests and target architecture. Digest pinning stabilizes a base input,
not every package download or generated artifact; pair it with reviewed updates.

Use multi-stage builds when a build toolchain or test dependencies can be left out
of the final image. Copy the runtime artifacts and libraries actually needed. A
single stage is reasonable for an already packaged application. Introduce reusable
base stages only for a real shared maintenance boundary, not a new generic platform.

## Secrets and cache

Use BuildKit secret/SSH mounts for credentials needed during a build. ARG, ENV,
copying then deleting a file, or hiding a value in an earlier stage are not secret
delivery mechanisms. A secret mount does not prevent the invoked tool or install
script from logging, copying or exfiltrating its contents; trust and scope still matter.

Order stable dependency inputs before frequently changing source when their build
semantics allow it. Treat cache as an optimization: a clean build must still work.
Secret contents do not invalidate the build cache. If changed credentials or remote
inputs must force work, use an explicit nonsecret revision or scoped cache invalidation;
never use the credential itself as an ARG/cache key. Review exported-cache access.

`--no-cache` reruns steps; `--pull` refreshes base resolution. Neither replaces lockfile
or digest review. Add cache mounts/remote cache only for measured iteration needs.
Optional illustration: [a build-secret fragment](examples/build-secret.md).

Basis: [context and ignore files](https://docs.docker.com/build/concepts/context/),
[build practices](https://docs.docker.com/build/building/best-practices/),
[multi-stage builds](https://docs.docker.com/build/building/multi-stage/),
[build secrets](https://docs.docker.com/build/building/secrets/), and
[cache invalidation](https://docs.docker.com/build/cache/invalidation/).
