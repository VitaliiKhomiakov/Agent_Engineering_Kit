# PHP types and contracts

Read when changing signatures, DTOs, arrays, parsers, null/presence behavior,
domain rules, or errors. Existing [core policy](../core.md) owns named boundary
contracts; PHP does not require every collection to become an object.

## Native types, static checks, and coercion

Use native parameter/property/return types where the supported PHP version can
express the contract. Prefer `declare(strict_types=1)` in new application files;
introducing it into existing code requires checking coercion-dependent callers.
For scalar arguments it is the calling file that chooses strictness. Internal
function callbacks have different behavior; an `int` can still satisfy `float`.
This setting does not validate HTTP/CLI/JSON payloads or array members, and does
not change all comparison or operator conversions.
[Type declarations](https://www.php.net/manual/en/language.types.declarations.php).

Use PHPDoc for information native types cannot express: `list<T>`, map key/value
types, precise callable signatures, resource handles, and generics where useful.
A local array shape can describe an external representation, but it does not
replace the existing requirement for named DTOs/commands/results across operation
boundaries. Arrays remain appropriate for typed collections, genuine maps,
configuration and serialization. Avoid bare `array $data` with implied keys.
[PHPDoc types](https://phpstan.org/writing-php-code/phpdoc-types).

Treat `mixed` returned by JSON/SDK APIs as untrusted boundary data and narrow it
with executable checks before use. Do not propagate it through business code,
cast it into a guessed shape, or use an unchecked `@var` assertion to silence the
analyzer. PHPDoc assertions describe facts; they cannot make external data valid.
Do not blindly copy Python's/TypeScript's type spellings or impose a second
analyzer on a project already using PHPStan or Psalm.

## Input presence and parsing

Define accepted coercions, required/nullable/default semantics, bounds, unknown
keys, and public output deliberately. `isset` and `??` treat null as absent;
`array_key_exists` distinguishes an explicit null from a missing key. `empty()`
also treats values such as `0`, `false`, and `"0"` as empty. Use strict comparisons
for sentinels/statuses and a chosen parser when a string represents a number or
boolean; `(bool) "false"` is true and a cast is not validation.
[Comparisons](https://www.php.net/manual/en/language.operators.comparison.php),
[presence](https://www.php.net/manual/en/function.array-key-exists.php).

For JSON, handle decoding failures explicitly, usually `JSON_THROW_ON_ERROR` on
this baseline. Check the decoded top-level kind and each required value before
constructing the owned contract. Choose byte/depth/collection limits at the
appropriate input boundary; validating a string already in memory is not a
network body limit. Preserve large identifiers as strings when integer precision
is not guaranteed. JSON decoding alone does not validate a domain schema.
[JSON decoding](https://www.php.net/manual/en/function.json-decode.php).

Keep field and cross-field checks deterministic and local. Do not perform
database queries, authorization decisions, or external writes merely to validate
a DTO. Attribute metadata only has an effect when the relevant runtime consumer
executes it; Symfony's validation mechanism retains its separate owner.

## Business state and errors

An input can be well-formed yet unsuitable for a particular state transition.
Keep valid incomplete drafts possible where the domain allows them; enforce
publication/approval/payment preconditions at the intent method or application
operation that owns the transition. Check before mutating state. Transactions
and storage constraints enforce concurrent invariants that a DTO cannot settle.
The optional [input/domain example](examples/input-domain.md) makes this distinction.

Use a specific expected exception, nullable result, or the project's existing
typed result convention according to the contract. Keep an absent optional value,
invalid input, domain rejection, and an infrastructure/programming failure
distinct. PHP's `Throwable` includes `Exception` and `Error`; catch broadly only
at a boundary with a real cleanup/reporting responsibility, preserving the cause.
Do not convert a TypeError into successful empty output or invalid user input by
default. Warnings/false-returning APIs are not automatically exceptions.
[Exceptions](https://www.php.net/manual/en/language.exceptions.php).

Map expected failures to safe public responses in the entry adapter; preserve
appropriate internal diagnostics without payloads, credentials, or database
details leaking to clients. Project only intended public fields. Neither
`json_encode` nor implementing `JsonSerializable` automatically establishes the
right visibility, validation, or failure policy.

Use supported native types/enum cases for real distinctions rather than broad
unions that hide unrelated alternatives. Named arguments make parameter names a
caller-visible contract; preserve them during a refactor or treat renames as an
API change. [Named arguments](https://www.php.net/manual/en/functions.arguments.php#functions.named-arguments).
