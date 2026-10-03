# Build-secret fragment

Use when a Node build needs a private npm registry. This is a fragment for an existing
BuildKit Dockerfile with a compatible frontend, Node/npm stage and working directory;
it is not a complete image. Keep the project's chosen runtime and lockfile policy.
See [build and context](../build-context.md).

### Dockerfile fragment

```dockerfile
COPY package.json package-lock.json ./
RUN --mount=type=secret,id=npmrc,target=/run/secrets/npmrc,required=true \
    NPM_CONFIG_USERCONFIG=/run/secrets/npmrc npm ci
```

Supply `id=npmrc` through the builder's `--secret` option from an approved file outside
the context. The secret file must be readable by this build stage's user; the default
mount is root-owned mode 0400. A non-root stage needs an appropriate mount UID/GID.
Do not COPY `.npmrc` or put the token into ARG/ENV. Keep project credentials excluded
even if a later step copies source. Workspaces may require additional manifest inputs.

The mounted config is temporary, but npm lifecycle scripts run with access to it.
Use trusted dependencies and scoped credentials; the mount cannot guarantee that a
script or diagnostic log does not disclose them. Preserve required install flags;
`npm ci` requires a matching lockfile. Credential rotation alone does not invalidate
the cached RUN step. Copy only required artifacts to the final runtime stage.

Verified by source review only: no private registry, install or image build was run.
The local Buildx command was unavailable; no new builder was installed for this
instruction example. A consuming project validates its actual build if adopting it.

Basis: [secret mounts](https://docs.docker.com/build/building/secrets/),
[mount options](https://docs.docker.com/reference/dockerfile/#run---mounttypesecret),
and [npm ci](https://docs.npmjs.com/cli/v11/commands/npm-ci/).
