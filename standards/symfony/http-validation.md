# Symfony HTTP, validation, and public contracts

Read when changing routes/controllers, request mapping, DTO constraints, forms,
serialization, public errors, or authorization. [PHP contracts](../php/types-contracts.md)
own native typing/coercion; framework mapping and validation have additional rules.

## Request mapping is an executed boundary

Define route methods, input media types, path/query/body sources, and response
format deliberately. JSON APIs should select JSON error rendering; a route's
format alone does not validate Content-Type, body size, or authorization.
Use the established argument resolver or explicit adapter parsing. On a supported
stack, `MapRequestPayload` maps a typed body and invokes the configured Validator;
`MapQueryString` has its own defaults and should not be assumed identical.
[Controller mapping](https://symfony.com/doc/7.4/controller.html).

Put input constraints on owned DTOs, using Validator attributes when the version
and project convention support them. Merely adding attributes or constructing a
DTO does not execute validation. A CLI entry must invoke the agreed validator;
Messenger needs the configured validation middleware when that is the intended
boundary. A direct service call does not reproduce the HTTP resolver pipeline.
[Validator](https://symfony.com/doc/7.4/validation.html),
[message validation](https://symfony.com/doc/7.4/messenger.html#middleware).

Choose coercion, missing/null/default semantics, validation groups, unknown-field
policy and collection limits explicitly. Native `strict_types` is not a promise
about serializer construction. Nullable constructor arguments may be filled with
null when absent; `require_all_properties` changes this behavior. `NotBlank` and
`NotNull` have different contracts; use them according to permitted values, not
as interchangeable markers. Bound request bodies/uploads at the appropriate
server/application boundary before expensive decoding, and constrain nested data.
[Serializer](https://symfony.com/doc/7.4/serializer.html).

On the checked 7.4 stack, malformed JSON produces 400, unsupported accepted format
415, and payload validation/type failures normally 422. These are configurable
framework behaviors, not a universal API contract. Unknown fields are ignored by
default; with `allow_extra_attributes: false`, the checked Serializer throws
ExtraAttributesException, which the default payload resolver does not convert to
a client error. The optional [request example](examples/request-boundary.md)
maps that specific input-path error to a redacted 400. Do not relabel every
serializer/programming failure as invalid user input; check the installed version.

## Arrays of nested DTOs

When a payload contains child objects, such as an order's `lines`, establish three
separate contracts:

- **Construction:** native `array` does not identify its element class. Supply
  element metadata, such as constructor PHPDoc `@param LineDto[] $lines`, through
  the configured Serializer/PropertyInfo extraction path. The Symfony 7.4
  [payload-mapping documentation](https://symfony.com/doc/7.4/controller.html#mapping-request-payload)
  identifies `phpstan/phpdoc-parser` and `phpdocumentor/type-resolver` as prerequisites
  for this PHPDoc-based mapping. Verify the installed stack's configuration and
  compatible packages only when this mapping is used; scalar DTOs need no such addition.
- **Child validity:** apply [Assert\Valid](https://symfony.com/doc/7.4/reference/constraints/Valid.html)
  to the collection to traverse child constraints with the intended validation
  groups. It neither constructs DTOs nor establishes element shape. Reject null
  or non-DTO elements at the mapping/validation boundary; where needed,
  [Assert\All](https://symfony.com/doc/7.4/reference/constraints/All.html) can apply
  `NotNull` and [Type](https://symfony.com/doc/7.4/reference/constraints/Type.html)
  for the child class to each element, alongside recursive validation.
- **Container contract:** decide missing/null/empty semantics, list versus keyed
  shape and permitted keys. `Valid` does not validate array keys. Bound the number
  of children with [Count](https://symfony.com/doc/7.4/reference/constraints/Count.html)
  according to the operation; this does not replace pre-decoding request-size limits.

For an affected endpoint, check successful child construction, a child field
constraint failure, malformed children (including null, scalars and nested arrays),
and an oversized collection through the real payload resolver. A valid parent or
direct DTO construction alone does not prove these cases. These prerequisites were
source-reviewed against Symfony 7.4 on 2026-10-04; no new runtime fixture is implied.

## Local validity, state, and output

Keep field/cross-field checks deterministic and free of writes or remote calls.
DTO validation does not settle live uniqueness, available capacity, permissions,
or concurrent invariants. Invoke the business operation after input validation;
it owns state-dependent refusal and required effects across HTTP, CLI and queue
entry points. ORM attributes describe persistence and Validator constraints
describe validity; neither substitutes for the other.

Project intended public fields through an explicit response contract or a
deliberate serializer context. A JsonResponse containing an object/array is not
an automatic response-schema validator or field allowlist. Serializer groups are
effective only on the path that actually applies that context. Avoid serializing
request DTOs, security users, or ORM graphs wholesale: secrets, internal fields,
circular references, lazy queries and unstable schemas can cross that boundary.

Map expected application refusals to the agreed status/error shape. Preserve
headers such as Allow or WWW-Authenticate when replacing an HTTP error response.
Keep internal types, rejected payloads and infrastructure details out of public
messages, while retaining useful redacted diagnostics. Current controller docs
identify a custom-type error-disclosure change in 8.1; do not assume its behavior
on 7.4 or expose raw exception messages because a serializer produced them.

## Forms and authorization where applicable

Symfony Forms are useful for their actual rendering/mapping/validation workflow;
a JSON endpoint need not introduce a Form type. With forms, bind only fields the
operation allows, check submission and validity, and deliberately map editable
data. Binding to an entity is a project choice, not authorization for arbitrary
setters or all-field updates. Input constraints still need an actual consumer.

Separate authentication from object/action authorization. Check the current actor
and target through the established Security/voter policy; loading an entity via
a resolver does not grant access to it. Access-control entries use the first
matching rule, so order and route/method conditions affect exposure. Authorization
must still hold when the operation has another entry path.
[Access control](https://symfony.com/doc/7.4/security/access_control.html),
[voters](https://symfony.com/doc/7.4/security/voters.html).

Keep CSRF protection for applicable state-changing browser flows. Symfony Forms
can perform it when configured; a raw JSON/manual endpoint does not acquire that
protection from a DTO attribute. Choose session/token behavior and caching for
the actual authentication mode. CORS is not authorization or a CSRF policy.
[CSRF](https://symfony.com/doc/7.4/security/csrf.html).
