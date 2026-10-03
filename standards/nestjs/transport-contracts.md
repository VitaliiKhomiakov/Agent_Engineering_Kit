# NestJS transport contracts

Read for DTOs/schemas, pipes, guards, filters, transformation or output serialization.
The optional [validated command example](examples/validated-command.md) exercises the
actual Nest/Fastify boundary. [Strict TypeScript](../typescript.md) still applies.

## Entry points, DTOs, and validation

- A controller or queue consumer invokes an application operation and converts
  the result. An HTTP controller contains no business calculations, SQL, or
  transaction management.
- When using `ValidationPipe` with class-validator, define input DTOs as concrete
  classes with suitable decorators. An `interface` or generic alone does not
  provide the required runtime metadata.
- Import a DTO used as the validator's runtime class as a value, not only through
  `import type`. Confirm that the pipe is actually connected.
- Nested objects and arrays require validation by the chosen mechanism; an
  annotation such as `CreateOrderDto[]` does not prove its elements are validated.
- Define unknown-field and value-transformation policy explicitly according to
  the contract. `whitelist`, `forbidNonWhitelisted`, and `transform` change API
  behavior; do not enable them globally in an existing project as a side effect.
- Queue and CLI input must also invoke an appropriate validation mechanism. An
  HTTP pipe does not cover arbitrary method calls.
- Guards, pipes, interceptors, and filters perform their transport and cross-cutting
  responsibilities; do not hide an application use case in an interceptor or
  validator. Authorization for a specific resource remains behind the business boundary.

## Verify the real input path

`ValidationPipe` plus class-validator uses runtime class metadata; interfaces,
generics, `import type` and a bare array annotation cannot supply it. Check emitted
decorator metadata and the actual compiler/loader, including inherited/mapped DTOs.
For nested class DTOs, supply validation decorators and the transformer's element
constructor (`@ValidateNested`/`@Type` where applicable). Validate the container and
size as well as each item. `@Type` performs transformation, not validation.

Choose strip/reject/preserve rules for unknown fields. With class-validator,
whitelist membership is based on validation decorators, not every TS field or
Swagger annotation. `forbidUnknownValues` is a different option from rejecting
extra fields. Audit validation groups and missing-field settings for the selected
version. In particular, `@IsOptional()` skips null as well as undefined; PATCH
semantics that permit omission but reject null need a different explicit rule.

Separate route/query conversion from JSON-body policy. `transform: true` can return
DTO instances and convert known primitive route parameters; it does not mean every
nested value must be coerced. Broad implicit conversion can turn an invalid string
into an accepted value, and Boolean conversion is not textual boolean parsing.
Prefer explicit parse pipes or a tested schema rule for that actual parameter.
Body byte limits belong to the adapter/parser before expensive DTO validation.

In Nest 12, `StandardSchemaValidationPipe` is an alternative for an already chosen
compatible schema library: attach the actual schema to the route parameter and
register the pipe. Schema-derived types do not remove that runtime registration.
Follow its output/transformation and unknown-field policy; do not duplicate class
DTOs only to satisfy a class-validator convention that this mechanism does not use.
Do not mix both pipelines blindly or migrate validation libraries during a local fix.

## Request order, authorization and errors

Guards run before pipes in the normal Nest HTTP flow. A guard cannot assume that
its raw body/params have already passed the controller's validation. Use trusted
identity and independently validated lookup data for its boundary decision; retain
resource/state-dependent authorization in the application operation across entry points.
Interceptors surround the downstream pipeline; keep business sequencing and
transactions out of generic transport wrappers unless explicitly designed otherwise.

Register global components through `APP_PIPE`, `APP_GUARD`, `APP_INTERCEPTOR` or
`APP_FILTER` when they need module DI; a manually constructed bootstrap instance
needs explicitly supplied collaborators. Verify which controller/transport receives
it. A hybrid microservice does not inherit the HTTP app's global configuration by
default; queue/CLI/direct calls need their own boundary. Context-specific errors
and acknowledgments differ from HTTP status responses.

Map documented domain outcomes at the boundary and preserve unexpected causes for
internal reporting. A catch-all filter must not disguise every defect as 400/404 or
leak raw exception/upstream data. Use typed contracts for transport-specific access,
or the adapter abstraction when portability matters; avoid a raw Express response
inside otherwise Fastify-compatible code.

## Output is a separate contract

Returning an ORM entity or an annotated interface does not establish the public
response shape. Prefer an explicit projection when that is enough. If using
`ClassSerializerInterceptor`, connect it and supply the runtime class instances or
a verified `@SerializeOptions({ type: ResponseDto })` path for plain data. Envelopes,
nested collections and raw adapter responses require checking their actual path.
`@Res()` manual response handling can bypass normal Nest response transformations.

Class-transformer exposure/exclusion is not class-validator output validation.
Input whitelist settings do not remove response secrets, and TS return annotations
do not sanitize data. Use intentional exposed fields and test the final serialized
HTTP payload. Avoid copying unrelated persistence fields into a response model.
For Nest 12's `StandardSchemaSerializerInterceptor`, supply a response schema and
verify its projection/validation/failure contract; do not assume the class-based
interceptor has the same behavior. In checked 12.0.4, the schema serializer applies
the schema per array element and bypasses primitive/null and StreamableFile results;
it is not a universal validator of every possible response. Verify the actual
envelope and collection schema. Streaming responses need their own output contract.

## Basis

[Validation](https://docs.nestjs.com/techniques/validation),
[class-validator](https://github.com/typestack/class-validator),
[class-transformer](https://github.com/typestack/class-transformer),
[serialization](https://docs.nestjs.com/techniques/serialization),
[request lifecycle](https://docs.nestjs.com/faq/request-lifecycle),
[authorization](https://docs.nestjs.com/security/authorization),
[filters](https://docs.nestjs.com/exception-filters) and
[hybrid configuration](https://docs.nestjs.com/faq/hybrid-application) describe the
mechanisms. Verify installed implementations where broad documentation wording
could conflate transforming, validating and exposing fields.
