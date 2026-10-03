# Local Compose contract

Use for an existing Linux application image whose contract already supports UID/GID
10001, a read-only root, temporary writes under `/tmp`, HTTP on `0.0.0.0:8080`, and an
executable `/app/healthcheck`. Its existing entrypoint handles SIGTERM and exits within
20 seconds. Adapt these assumptions to the actual image; this document supplies no
application or healthcheck implementation. See [Compose integration](../compose-integration.md).

### `compose.yaml`

```yaml
services:
  app:
    image: "${APP_IMAGE:?Set APP_IMAGE to the reviewed application image}"
    user: "10001:10001"
    init: true
    read_only: true
    tmpfs:
      - /tmp:size=64m,mode=1777
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    environment:
      PORT: "8080"
    ports:
      - "127.0.0.1:8080:8080"
    stop_grace_period: 20s
    healthcheck:
      test: ["CMD", "/app/healthcheck"]
      interval: 10s
      timeout: 2s
      retries: 3
      start_period: 10s
```

With `APP_IMAGE` set to an approved reference, run `docker compose -f compose.yaml
config --quiet` in this example's directory. A nonempty placeholder is enough for
configuration-only validation; it proves no image exists. Missing/empty APP_IMAGE
must be rejected. No `up`, pull or build is needed for this check.

The image owns the command and configuration validation. Temporary files disappear
with the container; durable application data needs a separate storage contract.
The probe reports health; it neither restarts this service nor validates a business
operation. Loopback publishing expresses local intent, not a universal firewall
guarantee across Engine versions. `init` and restrictions must suit the real image.

Checked with Compose **2.40.3**: configuration acceptance and required-variable refusal
only. No container, signal handling, probe, permissions or network isolation was tested.
Basis: [config validation](https://docs.docker.com/reference/cli/docker/compose/config/)
and [service configuration](https://docs.docker.com/reference/compose-file/services/).
