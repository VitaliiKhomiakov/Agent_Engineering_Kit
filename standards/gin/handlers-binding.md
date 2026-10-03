# Gin: handlers, binding, and HTTP contracts

Read for Gin handlers, input sources, validation, or response/error contracts.
Return to the [Go/Gin entry](../go-gin.md). Requirements protect the affected
contract; defaults below allow a concrete project exception.

## Transport and application boundary

- A handler translates HTTP input into a typed operation, calls application
  behavior, and maps the outcome. Use a closure or a cohesive handler struct
  with explicit dependencies; a base controller, DI container, or interface per
  handler is unnecessary. Organize related routes around their feature.
- Keep Gin types and binding tags at the transport boundary. Pass
  `c.Request.Context()` and explicit typed values into application work. Do not
  turn `gin.H`, `map[string]any`, or context keys into an implicit command bus.
  Domain maps of typed values remain valid.
- Input tags/custom validators check shape and local consistency. The use case
  coordinates authorization, domain behavior, transactions, and effects; domain
  objects retain their state invariants. Follow [Go contracts](../go/contracts.md) when those rules change;
  a valid DTO is not proof that a document can be published.
- Use explicit response contracts to avoid accidentally serializing persistence
  fields or private state. A small local error writer is sufficient until a
  repeated policy warrants shared middleware.

## Choose the input contract explicitly

| Source or decision | Gin form and condition |
| --- | --- |
| Path parameters | `ShouldBindUri` with `uri` tags, or explicit typed parsing for one parameter |
| Query-only input | `ShouldBindQuery` with `form` tags; avoid accidental body/form merging |
| Headers | `ShouldBindHeader` with `header` tags; authentication still verifies the credential |
| JSON body | `ShouldBindJSON` with `json`/`binding` tags when its decoder policy fits |
| Negotiated form/body input | `ShouldBind` selects from method/content type; use only when those sources and precedence are intended |
| A local decoder policy | `ShouldBindWith` with a focused binder; preserve validation and error propagation |

Reject unsupported media types where the endpoint contract requires it. Selecting
the JSON binder alone does not check that the request declared JSON. Bind path,
query, and body separately when they have distinct meanings; specify which source
owns a value rather than letting a later bind silently replace it.

`ShouldBind*` returns errors for the caller to handle. `Bind*`/`MustBindWith`
can abort and commit a response before the handler maps its own error. Do not
switch families mechanically or assume every version/codec yields the same
status. Explicit handling is the default for an API with a defined error body.
See [binding](https://gin-gonic.com/en/docs/binding/binding-and-validation/) and
the [versioned API implementation](https://github.com/gin-gonic/gin/blob/v1.12.0/context.go).

## Presence and validation

- `binding:"required"` rejects zero scalar values, including `false` and `0`.
  Use a pointer/presence type when an explicitly supplied zero must be accepted.
  For JSON into a fresh pointer field, omission and `null` both produce nil;
  PATCH contracts needing all three states require an explicit representation.
- Do not infer validity from a non-nil pointer or from JSON `omitempty` tags.
  Choose range, length, and cross-field checks according to the operation.
  Reject or bound pagination and collection sizes before expensive work.
- Register shared custom validation before concurrent serving; validators should
  be deterministic input checks, not database queries or side effects. Verify
  the actual validator configuration; Gin's default initializer and an example
  using `validator.New(validator.WithRequiredStructEnabled())` are not equivalent.

See [validator semantics](https://pkg.go.dev/github.com/go-playground/validator/v10@v10.30.1),
[custom validation](https://gin-gonic.com/en/docs/binding/custom-validators/), and
[Gin's initializer](https://github.com/gin-gonic/gin/blob/v1.12.0/binding/default_validator.go).

## JSON, limits, and errors

- Decide unknown-field, duplicate-key, and trailing-data behavior deliberately.
  Gin 1.12's default JSON binder decodes once and has unknown-field rejection
  disabled by default. It does not promise exactly one value through EOF.
  Changing JSON codec or strictness changes the wire contract.
- Global decoder/validator switches affect other routes and concurrent tests.
  Set an application-wide policy once at startup; use a local binder for an
  endpoint-specific policy. Strict unknown-field rejection is optional and can
  break clients. Rejecting trailing values is a separate decision.
- Apply body limits before reading. Map a size failure distinctly when the API
  promises it, and do not treat a limited reader as proof that unconsumed trailing
  bytes were checked. [Runtime guidance](runtime.md) owns upload/server bounds.
- Translate inspectable application errors into the API's stable statuses and
  public codes. Keep raw parser, validator, storage, and panic details out of
  public errors; record useful diagnostics through the designated log owner.
  Preserve the project's 400/422, 403/404, and conflict conventions.
- After rejecting input, abort pending handlers where relevant and return from
  the current function. Do not invoke the use case or append a second response.

The optional [binding example](examples/binding.md) implements an explicitly
strict single-JSON command and maps a business conflict independently of binding.
Its extra binder is unnecessary when the default contract already suffices.
See the [JSON binder source](https://github.com/gin-gonic/gin/blob/v1.12.0/binding/json.go).
