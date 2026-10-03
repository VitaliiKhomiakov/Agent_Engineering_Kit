# Explicit development and production Compose contracts

Optional illustration for [environment rules](../development-production.md).
Linux, npm single-package Nest/Node service; package-lock.json is committed,
`npm run build` emits `dist/main.js`, `start:dev` reloads source, and the app listens
on `0.0.0.0:3000`. Adapt paths for a monorepo or a different Nest output layout.
The app implements `/health/ready`, reads `DB_PASSWORD_FILE` itself and supports
SIGTERM draining. Those capabilities are assumptions, not supplied by Compose.
The service uses PostgreSQL 17's `/var/lib/postgresql/data` layout; changing the
database major requires its own data/mount upgrade procedure.

## Image recipe

`Dockerfile` (the supplied NODE_IMAGE must be the same reviewed Node Debian-family
image in all stages, with a compatible non-root `node` user):

```dockerfile
ARG NODE_IMAGE
FROM ${NODE_IMAGE} AS dependencies
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

FROM dependencies AS development
COPY --chown=node:node . .
RUN chown node:node /app
USER node
CMD ["npm", "run", "start:dev"]

FROM dependencies AS build
COPY . .
RUN npm run build

FROM ${NODE_IMAGE} AS production-dependencies
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev

FROM ${NODE_IMAGE} AS runtime
ENV NODE_ENV=production
WORKDIR /app
COPY --from=production-dependencies --chown=node:node /app/node_modules ./node_modules
COPY --from=build --chown=node:node /app/dist ./dist
COPY --chown=node:node package.json ./
USER node
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

This recipe assumes dependency-install scripts need no missing source/build tools;
adapt it if native dependencies, workspaces or generation require additional inputs.
Copy required templates/assets explicitly. The production artifact must also
contain compiled migrations and the agreed migration runner if it runs migrations.
Do not change the app command to run migrations in every replica.

`.dockerignore`:

```text
.git
node_modules
dist
coverage
.env
.env.*
!.env.example
.secrets
.npmrc
*.log
```

Private package credentials need a BuildKit secret mount, as in the separate
[build-secret example](build-secret.md), not a copied `.npmrc` with tokens.
Add actual credential paths to the context exclusions.

## Neutral base: `compose.yaml`

```yaml
services:
  app:
    init: true
    environment:
      PORT: "3000"
      DB_HOST: db
      DB_PORT: "5432"
      DB_USER: "${APP_DB_USER:?Set the provisioned application database role}"
      DB_NAME: app
      DB_PASSWORD_FILE: /run/secrets/app_db_password
    secrets:
      - app_db_password
    depends_on:
      db:
        condition: service_healthy
    stop_grace_period: 30s
    healthcheck:
      test: ["CMD", "node", "-e", "fetch('http://127.0.0.1:3000/health/ready', {signal: AbortSignal.timeout(1500)}).then(r => process.exit(r.ok ? 0 : 1)).catch(() => process.exit(1))"]
      interval: 10s
      timeout: 2s
      retries: 5
      start_period: 20s
  db:
    image: "${POSTGRES_IMAGE:?Set a reviewed PostgreSQL 17 image reference}"
    environment:
      POSTGRES_USER: app
      POSTGRES_DB: app
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
    volumes:
      - database:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U \"$${POSTGRES_USER}\" -d \"$${POSTGRES_DB}\""]
      interval: 5s
      timeout: 3s
      retries: 10
secrets:
  db_password:
    file: "${DB_PASSWORD_PATH:?Set a protected host secret file path}"
  app_db_password:
    file: "${APP_DB_PASSWORD_PATH:?Set the application role secret file path}"
volumes:
  database:
```

No host database port is needed for the containerized app. The official image's
POSTGRES_USER is a bootstrap superuser. In disposable development only, APP_DB_USER
can be `app` and both secret paths can reference the same local file. Before
production, provision a least-privilege application role and separate migration
credentials through the deployment's database setup. Set APP_DB_USER and
APP_DB_PASSWORD_PATH to that role; the app never mounts the bootstrap secret.
Changing the bootstrap variables does not rotate credentials in an existing volume.
`pg_isready` only probes server availability, not app authorization or schema readiness.

## Development addition: `compose.dev.yaml`

```yaml
services:
  app:
    build:
      context: .
      target: development
      args:
        NODE_IMAGE: "${NODE_IMAGE:?Set the reviewed development/build Node image}"
    environment:
      NODE_ENV: development
    ports:
      - "127.0.0.1:${APP_PORT:-3000}:3000"
    develop:
      watch:
        - action: sync
          path: ./src
          target: /app/src
          initial_sync: true
        - action: rebuild
          path: package.json
        - action: rebuild
          path: package-lock.json
```

This Watch form including `initial_sync` was configuration-checked with Compose
2.40.3; verify feature support in the installed client. Add rebuild rules
for changed tsconfig/Nest configuration and assets used by the actual app, or
rebuild explicitly. Source is initially copied; dependencies stay inside the image.
Watch utilities and write permissions must exist in the development image.

## Production addition: `compose.production.yaml`

Apply only after the database-role/secret and operational prerequisites above:

```yaml
services:
  app:
    image: "${APP_IMAGE:?Set the tested application image digest}"
    environment:
      NODE_ENV: production
    ports:
      - "127.0.0.1:${APP_PORT:-3000}:3000"
    read_only: true
    tmpfs:
      - /tmp:size=64m,mode=1777
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    restart: unless-stopped
    cpus: 1.0
    mem_limit: 512m
    pids_limit: 128
    logging:
      driver: local
      options:
        max-size: "10m"
        max-file: "3"
  db:
    restart: unless-stopped
    logging:
      driver: local
      options:
        max-size: "10m"
        max-file: "3"
```

The host reverse proxy owns public TLS/ingress. A containerized proxy instead uses
its shared network and service port. Budgets above illustrate syntax; size app and
database resources for the real workload. Validate read-only paths and secret-file
access as the actual image user. Configure database backups, recovery, monitoring
and deployment serialization before using this in production.

## Commands and evidence boundaries

Set nonsecret image references and DB_PASSWORD_PATH in the invoking environment;
also set APP_DB_USER and APP_DB_PASSWORD_PATH; provide protected files separately.
Required interpolation checks presence,
not digest syntax or whether an image exists. Use a distinct project per checkout;
production must also have its own data/project scope.

```sh
docker compose -p service-dev -f compose.yaml -f compose.dev.yaml config --quiet
docker compose -p service-dev -f compose.yaml -f compose.dev.yaml up --build --watch
docker compose -p service-prod -f compose.yaml -f compose.production.yaml config --quiet
```

Inspect the production effective model: no build, source mount, Watch, dev command,
debug or database host port. After authorized image delivery, backups and release
migrations, the deployment procedure can pull reviewed references and run
`docker compose -p service-prod -f compose.yaml -f compose.production.yaml up -d
--no-build --wait --wait-timeout 120`. This may replace containers and interrupt
traffic; it is not an instruction to deploy while reviewing the example.

Configuration checks do not build an image or prove health, hot reload, credentials,
migration execution or data recovery. The research record states what was actually
checked. No application or deployable secret is included here.

Image contract: [official PostgreSQL image](https://hub.docker.com/_/postgres).
