# Readable source layout and PHP-FIG standards

Reviewed: 2026-11-06. Scope: source-policy review for AEK, with official primary
sources. This record adds evidence; it does not replace the PHP example runs
recorded on 2026-09-21 or claim a new runtime/formatter execution.

## Existing guidance and ownership

At baseline `b69e3f6cc9d40318f758db3bb529ed32cfb76163`, core discouraged dense
expressions and the shared verification policy already required readability
acceptance. Detailed layout/grouping rules existed for Go, GDScript and Angular
SCSS, but core had no explicit all-language indentation and phase-spacing owner.
The PHP entry and structure topic covered PSR-4 but lacked a style/PSR selection
policy. These are repository observations, not claims about language requirements.

The change places the shared rule in
[core](../../standards/core.md#readable-code-layout), retains acceptance in
[verification](../../standards/verification.md#readability-acceptance), and adds
[PHP-FIG selection](../../standards/php/fig-standards.md) as a conditional PHP topic.
Language-specific layouts remain authoritative for their details.

## Layout evidence

| Primary source | Relevant observation | AEK decision |
| --- | --- | --- |
| [PEP 8: blank lines](https://peps.python.org/pep-0008/#blank-lines) | Python guidance uses blank lines for logical sections and distinguishes spacing between declarations. | Require meaningful grouping while preserving language-specific declaration layout. |
| [Effective Go: formatting](https://go.dev/doc/effective_go#formatting) | `gofmt` uses tabs; Go has no universal hard line-length bound. This is established formatting guidance, not a complete modern Go engineering guide. | Do not impose four spaces or a fixed width across languages. Keep the existing Go owner and tools. |
| [PSR-12 lines/indentation](https://www.php-fig.org/psr/psr-12/#23-lines) and [PER-CS 3.1.0](https://github.com/php-fig/per-coding-style/blob/3.1.0/spec.md) | These PHP styles use four-space indentation and permit readability blank lines; PER also defines compact empty bodies and attachment of attributes/docblocks. | Keep mechanical style specific to PHP. Mandatory semantic phase separation is AEK's stronger local policy, not a quoted FIG requirement. |

A formatter's success is mechanical evidence. The conclusion that agents must
also inspect semantic grouping is an AEK maintenance decision; no tool benchmark
or measured improvement in agent output was performed in this task.

## PHP standards and version evidence

The [official PSR index](https://www.php-fig.org/psr/) lists PSR-1, 3, 4, 6, 7,
11, 12, 13, 14, 15, 16, 17, 18 and 20 as Accepted on the review date. It lists
PSR-0/2 as Deprecated and PSR-5/19 as Draft. The latter are not accepted PHPDoc
requirements; analyzer-supported documentation remains the existing policy.

[PSR-1](https://www.php-fig.org/psr/psr-1/) supplies basic file/naming conventions;
[PSR-4](https://www.php-fig.org/psr/psr-4/) supplies autoload name/path mapping.
Neither alone is a complete layout policy. The
[PER page](https://www.php-fig.org/per/coding-style/) states its relationship to
PSR-12 and permits omitting guidance for unavailable language syntax.
[The release announcement](https://www.php-fig.org/blog/2026/08/per-cs-31-released/)
is dated 2026-08-28; the reviewed stable text is
[tag 3.1.0](https://github.com/php-fig/per-coding-style/blob/3.1.0/spec.md).
The live page can change; this review does not automatically track future releases.

Selecting versioned PER for new code without a style is AEK policy. Existing
PSR-12/framework/project styles remain valid local contracts. PSR-12's Accepted
status is distinct from PER superseding it as an evolving guide. The PHP 8.2+
profile remains conditional on each consuming project's actual supported range.

## Interoperability evidence and boundaries

| Sources reviewed | Decision supported |
| --- | --- |
| [PSR-3](https://www.php-fig.org/psr/psr-3/), [PSR-11](https://www.php-fig.org/psr/psr-11/) | Reuse suitable logging/container contracts; retain exception context semantics and keep dependency assembly explicit. |
| [PSR-6](https://www.php-fig.org/psr/psr-6/), [PSR-16](https://www.php-fig.org/psr/psr-16/) | Select pool/item or simple-cache contracts as needed, accounting for different miss and expiry semantics rather than installing both. |
| [PSR-7](https://www.php-fig.org/psr/psr-7/), [PSR-17](https://www.php-fig.org/psr/psr-17/), [PSR-18](https://www.php-fig.org/psr/psr-18/) | Separate messages, factories and clients. Message replacement does not make streams immutable; PSR-18 returns well-formed 4xx/5xx responses. |
| [PSR-15](https://www.php-fig.org/psr/psr-15/) | Handler/middleware contracts apply to a PSR-7 pipeline, not every framework controller. |
| [PSR-14](https://www.php-fig.org/psr/psr-14/) | Synchronous event dispatch is distinct from asynchronous/durable messaging. |
| [PSR-20](https://www.php-fig.org/psr/psr-20/) | A replaceable current-time source returns `DateTimeImmutable`; it does not specify a monotonic elapsed-time API. |
| [PSR-13](https://www.php-fig.org/psr/psr-13/) | Hypermedia links/providers are a conditional interoperability concern. |

These sources establish interface intent and selected contract details, not the
installed version or conformance of a consuming application. A PSR number does
not identify a Composer package major version. Native framework APIs are not
rewritten merely because an equivalent PSR exists.

## Execution evidence

The [task plan](../plans/2026-11-06-readable-code-and-php-standards.md) owns the
artifact/catalog checks, profile-selection results and scoped review. No PHP
application, Composer install, formatter preset or adapter implementation was
executed or changed here. Existing executable examples and their dated evidence
remain unchanged. The shared rule is instructional policy; automated enforcement
and effectiveness across agent clients are not established by this review.
