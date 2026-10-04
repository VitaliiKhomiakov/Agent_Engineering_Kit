# FastAPI transport and contracts

Read when changing HTTP routes, request/response models, domain calls, or errors.
Use the installed versions; the checked baseline is FastAPI 0.138.0 with Pydantic
V2. [Common policy](../core.md) owns design and strict-typing requirements;
[Pydantic validation](../pydantic/validation.md) owns model-level semantics.
Return to the [FastAPI entry](../fastapi.md).

## Organization and construction

Use `APIRouter` for cohesive groups of HTTP operations when the application needs
them. Preserve an existing small app without creating a mandatory directory tree,
base controller, generic service, or Repository hierarchy. Router prefixes, tags,
dependencies, and inclusion belong to transport/bootstrap, not the business core.
An app factory is useful for independent configurations, resource ownership, or
tests; a simple module-level app remains reasonable when those needs are absent.
[Router organization](https://fastapi.tiangolo.com/tutorial/bigger-applications/).

An endpoint parses HTTP input, receives dependencies, calls the application
operation, and projects its result. Independent business code uses ordinary typed
values, dataclasses, enums, or ports where needed, without `Request`, `Depends`,
`HTTPException`, or transport DTOs. Wire ready dependencies in bootstrap. A typed
function is sufficient for a single operation; introduce a protocol/adapter when
the integration boundary warrants it. Related definitions may share a module.

Keep HTTP DTOs distinct from ORM entities and public output when their contracts
differ. Do not duplicate identical shapes only to cross a folder. Parse dynamic
SDK/JSON data at its adapter into named contracts; typed collections and genuine
domain maps remain appropriate. See [Python contracts](../python/typing-contracts.md).

## Input and public output

Declare the intended source of each parameter with the applicable `Path`, `Query`,
`Header`, `Cookie`, `Body`, `Form`, or `File` mechanism. Preserve aliases, required
versus nullable fields, repeated parameters, content types, and numeric bounds.
Do not silently reinterpret a query field as a JSON body during a refactor.

Test coercion through HTTP. On the checked stack, JSON is decoded before
Pydantic's Python-mode validation; passing `model_validate_json()` in isolation
does not establish endpoint behavior. For example, a globally strict date field
can reject an ISO date string in HTTP JSON even though strict Pydantic JSON mode
accepts it. Choose the wire conversion deliberately, often per field; strict
typing does not require globally strict runtime parsing.
[Versioned request handling](https://github.com/fastapi/fastapi/blob/0.138.0/fastapi/routing.py),
[Pydantic strict modes](https://docs.pydantic.dev/latest/concepts/strict_mode/).

Local field/cross-field validation establishes input consistency. Authorization,
live availability, domain transitions, and atomic writes belong to the owning
application/domain/storage operation. Dependencies can run even when another
input is invalid; dependency setup and validators must not perform the requested
business write as a side effect of parsing.

Prefer an accurate typed public return model. Use `response_model` when the wire
contract differs from the Python return type, while keeping that return annotation
accurate. FastAPI validates/serializes ordinary return values against the selected
model. Do not adopt tutorial `Any` annotations as a typing workaround. Explicit
public projection avoids accidental lazy ORM access and internal-field exposure.
[Response models](https://fastapi.tiangolo.com/tutorial/response-model/).

A directly returned `Response`, including `JSONResponse` and `StreamingResponse`,
bypasses that automatic conversion/filtering. Own its bytes, media type, headers,
status, disclosure, and documentation explicitly. An OpenAPI `responses` entry
documents a contract; it does not enforce the body returned by an exception
handler. Avoid serializing an internal object wholesale.
[Direct responses](https://fastapi.tiangolo.com/advanced/response-directly/).

## Errors and compatibility

Translate expected application failures at the HTTP boundary, preserving the
project's chosen status and stable public error shape. Keep malformed input
(normally 422), authentication/authorization failures, missing resources, domain
conflicts, upstream failures, and programming/response-validation defects distinct.
Do not turn every exception into a client error or a successful empty response.
[Error handling](https://fastapi.tiangolo.com/tutorial/handling-errors/).

Review error bodies and logs for secrets. The default request-validation response
can include rejected input; hiding formatted Pydantic errors does not redact it.
When needed, use a typed allowlisted error representation or a fixed safe message,
and document the actual 422 response. Keep internal causes for appropriately
redacted diagnostics. Replacing an established detailed error schema is an API
change, not a harmless cleanup.

Check affected OpenAPI paths, schemas, aliases, required fields, status codes, and
operation IDs when moving or renaming models/routes. Separate input/output schemas
can be correct; keep their behavior deliberate for generated clients. Follow
[verification](verification.md) for file moves and upgrades.

Optional example: [HTTP boundary and domain capacity](examples/http-boundary.md).
