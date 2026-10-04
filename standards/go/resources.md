# Go: persistence and external resources

Read when changing database access, transactions, HTTP integrations, or resource lifetimes. Return to the [Go entry](../go-gin.md).


- Where `database/sql` is used, reuse `sql.DB` as the connection pool. Size it
  from the database budget and observed workload, not a universal constant.
- Make transaction ownership explicit for an atomic use case. Execute its
  statements through the same `sql.Tx`, handle rollback and commit errors, and
  do not accidentally escape the transaction through `sql.DB`. Domain methods
  do not replace database constraints, isolation, or conflict detection.
- Parameterize SQL values. Match placeholders to the driver; dynamic identifiers
  need an explicit allowed set or a suitable builder, not value placeholders.
- Close acquired rows, check scanning and iteration errors, and propagate query
  deadlines through supported context APIs. Keep a resource's lifetime bounded;
  deferring every close until the end of a long loop may retain many resources.
- Reuse HTTP clients/transports, close response bodies, and interpret status
  codes according to the remote API: a non-2xx response is not itself a transport
  error. Choose finite request budgets and bounded input/output handling where
  required; account for streaming and long-running operations explicitly.
- For HTTP/1 connection reuse, consume the required body within its budgets and
  close it. Unread bytes can prevent reuse; keeping the same Client is not proof
  of reusing its TCP connection. Check the supported Go version and RoundTripper:
  newer Transport implementations may attempt a bounded read after close, but
  close alone is no universal reuse guarantee. Any explicit drain needs both
  byte and time limits. Rejecting oversized/stalled content may properly sacrifice
  reuse; do not drain unbounded input just to save a connection or apply this
  HTTP/1 rule indiscriminately to HTTP/2. When reuse is required, observe it with
  `httptrace` or server connection accounting on the target transport.
- For servers, set appropriate header/body limits, timeouts, and graceful
  shutdown behavior from the service contract. Do not prescribe one timeout
  value for every endpoint or assume a header limit bounds the body.

See [transactions](https://go.dev/doc/database/execute-transactions),
[connection pools](https://go.dev/doc/database/manage-connections),
[query lifecycle](https://go.dev/doc/database/querying),
[query cancellation](https://go.dev/doc/database/cancel-operations),
[SQL parameters](https://go.dev/doc/database/sql-injection), and
[`net/http` contracts](https://go.dev/src/net/http/doc.go), including
[Client](https://go.dev/src/net/http/client.go) and
[Server](https://go.dev/src/net/http/server.go).
