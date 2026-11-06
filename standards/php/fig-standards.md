# PHP-FIG style and interoperability

Read when writing/reviewing PHP layout, selecting a PSR/PER baseline, or changing
one of the integrations below. Use [shared layout](../core.md#readable-code-layout)
for semantic grouping and [PHP verification](verification.md) for check selection.
This topic owns standards selection; it does not introduce application subsystems.

## Coding style and autoloading

Establish the project's documented style, formatter/linter configuration and
installed tool versions first. Preserve an existing PSR-12, PER, framework or
explicit project baseline. A style update does not authorize public API renames,
an unrelated reformat, tool installation or a PHP/dependency upgrade.

For new PHP code without an established style, this library selects
[PSR-1](https://www.php-fig.org/psr/psr-1/) plus a released, versioned
[PER Coding Style](https://www.php-fig.org/per/coding-style/) baseline.
PER-CS 3.1.0 is the reviewed release as of 2026-11-06; use its
[versioned specification](https://github.com/php-fig/per-coding-style/blob/3.1.0/spec.md)
with the project's supported syntax and actual tooling. Record the chosen
release/preset rather than relying on a moving `latest` alias. If tooling cannot
cover that release, make the supported baseline and remaining manual checks
explicit; do not label partial coverage as complete conformance.

- Apply PSR-1's file encoding/tag and naming conventions: UTF-8 without BOM,
  `<?php`/`<?=` opening tags, PascalCase class names, camelCase methods and
  uppercase underscore-separated class constants. Keep declaration files free
  of bootstrap effects under [structure](structure.md#modules-and-autoloading).
- Use the selected PER/PSR-12 layout: four-space indentation, LF line endings,
  a final newline, no trailing whitespace and no closing tag in PHP-only files.
  Keep independent statements on separate lines and use its multiline formatting
  rules. Preserve its allowed compact expressions and empty bodies; do not require
  every construct to span several lines.
- Apply [semantic grouping](../core.md#readable-code-layout) within those rules.
  The mandatory separation of meaningful phases is AEK policy; PER/PSR-12 permit
  readability blank lines but do not prescribe AEK's phase boundaries. Keep
  docblocks/attributes attached and respect places where the chosen style forbids
  an extra blank line.
- Keep [PSR-4](https://www.php-fig.org/psr/psr-4/) autoload mappings and class moves
  under [their existing owner](structure.md#modules-and-autoloading). PSR-4 does
  not specify source formatting or application layers.

PER extends and replaces [PSR-12](https://www.php-fig.org/psr/psr-12/) as the
evolving style guide; the [FIG index](https://www.php-fig.org/psr/) still lists
PSR-12 as Accepted. Keep it where already adopted rather than declaring it
deprecated. Ignore rules for syntax absent from the supported PHP range; PER
3.1 does not require upgrading a PHP 8.2 project to use newer language features.
[Scalar strictness and native/PHPDoc typing](types-contracts.md) remain separate
contracts, not guarantees supplied by a coding-style preset.

## Select interface standards by boundary

Prefer an applicable accepted PSR at a new reusable interoperability boundary
when it supplies the contract actually needed. Reuse the framework's existing
contract when that is sufficient. Adding logging, a container, middleware, a
cache, events or a clock merely to satisfy this table is not required. Read only
the selected standard's relevant contract, including its failure semantics.

| Actual boundary | Relevant standard | Contract to preserve |
| --- | --- | --- |
| Receiving or implementing a reusable logger | [PSR-3](https://www.php-fig.org/psr/psr-3/) | `LoggerInterface`, log levels and context; an exception supplied in context uses the `exception` key. Reporting ownership and safe context stay under [diagnostics](../core.md#diagnostic-error-ownership). |
| Exchanging cache items/pools or simple key/value caches | [PSR-6](https://www.php-fig.org/psr/psr-6/) or [PSR-16](https://www.php-fig.org/psr/psr-16/) | Select the matching API; preserve keys, misses and expiry/TTL behavior. They are different contracts, not two mandatory cache layers. |
| Exchanging HTTP request/response objects | [PSR-7](https://www.php-fig.org/psr/psr-7/) | Retain returned message instances from `with*` methods; body streams may still be mutable. Do not infer deep immutability. |
| Constructing PSR-7 objects independently of an implementation | [PSR-17](https://www.php-fig.org/psr/psr-17/) | Use the relevant HTTP factory interface; it neither sends a request nor prescribes factories for ordinary DTOs. |
| A reusable outbound HTTP client boundary | [PSR-18](https://www.php-fig.org/psr/psr-18/) | Valid 4xx/5xx responses are returned; transport/request failures retain their specified exception contracts. Apply application status policy above that boundary. |
| A PSR-7 server handler/middleware pipeline | [PSR-15](https://www.php-fig.org/psr/psr-15/) | Produce a response or delegate through the handler contract; preserve ordering and exception-to-response ownership. |
| Container interoperability at application assembly | [PSR-11](https://www.php-fig.org/psr/psr-11/) | Preserve lookup/missing-entry behavior and [explicit dependency construction](structure.md#construction-and-useful-abstraction); container compatibility is not a reason to inject a service locator everywhere. |
| Interoperable in-process event dispatch | [PSR-14](https://www.php-fig.org/psr/psr-14/) | Preserve synchronous listener order, stoppable-event and failure behavior; this is not a durable queue/delivery guarantee. |
| A replaceable current-time source for time-dependent behavior | [PSR-20](https://www.php-fig.org/psr/psr-20/) | `ClockInterface::now()` returns `DateTimeImmutable`; use the injected clock where controllable time is needed. It is not a monotonic duration timer. |
| Exchanging hypermedia link objects/providers | [PSR-13](https://www.php-fig.org/psr/psr-13/) | Preserve relation, URI/template and link-provider semantics only when the application exposes this kind of contract. |

The table does not require converting native framework request/response, HTTP
client, cache or dependency-injection APIs to PSR interfaces. Add an adapter only
for a real interoperability requirement, preserving both sides' observable
behavior. Standard numbers are not Composer package major versions: check the
actual installed `psr/*` interfaces, supported PHP range and implementation
compatibility. Reuse suitable dependencies; do not copy old signatures from a
specification into a project or add packages merely because a standard is listed.

## Status and evidence limits

Check the [official status index](https://www.php-fig.org/psr/) when adopting or
revising a standard. As reviewed on 2026-11-06, PSR-0 and PSR-2 are Deprecated;
do not select them for new adoption. PSR-5 and PSR-19 remain Draft, so do not
claim an accepted PHPDoc standard or require their adoption. Follow the project's
actual analyzer-supported PHPDoc conventions under [types](types-contracts.md).

The [dated research](../../docs/research/2026-11-06-readable-code-and-php-standards.md)
records the reviewed sources and scope. Reading a specification, having a `psr/*`
package installed, or passing a formatter does not prove implementation compliance.
