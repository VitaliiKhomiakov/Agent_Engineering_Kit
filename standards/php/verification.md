# PHP verification and compatibility

Read for tests/review, static analysis, file moves, security/performance work, or
runtime/dependency migration. Use the shared [verification policy](../verification.md)
and existing project tools; no new test framework is required for a local move.

## Proportionate checks

Run syntax checks with the target interpreter and relevant existing behavior
tests. Linting does not prove autoloading, types, runtime behavior, or extension
availability. For contracts/state changes, check meaningful valid and rejected
inputs, explicit null versus omission, false/zero values, failed transitions
without mutation, and safe output/errors. For resource changes, exercise normal
completion, early exit, and relevant failures. Production invariants must not
depend on `assert()`, which may be disabled.
[Assertions](https://www.php.net/manual/en/function.assert.php).

Run the project's configured PHPStan or Psalm over affected code and callers,
including relevant tests. New standalone code should aim for strong checks; do
not weaken an established level or add ignore/baseline entries to hide a defect
introduced by the change. Existing baselines can support incremental adoption,
but do not prove the suppressed code is correct. For PHPStan, record the exact
version/level: `max` means its highest available level, currently 10 in 2.2.14.
[PHPStan levels](https://phpstan.org/user-guide/rule-levels).

Use precise PHPDoc that the analyzer can verify, without broad `mixed`, untyped
collection members, guessed casts, or suppressions inside owned logic. Legitimate
external `mixed` values must be narrowed first. Framework reflection/ORM magic
can need the installed analyzer extension; do not add one speculatively to a
language-only task. Static analysis complements runtime boundary tests.

For a PSR-4 move, check namespace/path/case, public imports and parameter names,
Composer maps, string/CLI entry points, and relevant container/ORM registration.
Use the project's autoload check; where supported,
`composer dump-autoload --optimize --strict-psr --strict-ambiguous` detects invalid
mapping/duplicate classes. Follow its script/plugin policy. Preserve the public
serialization/mapping contract; a file move alone does not authorize schema DDL.
[Composer commands](https://getcomposer.org/doc/03-cli.md#dump-autoload-dumpautoload).

## Exposed security and operations

When handling untrusted input, bound decoding and collection/file work, keep
secrets out of errors/logs, and do not pass user data to `unserialize`, `eval`,
dynamic include paths, or a shell command. `allowed_classes` does not turn
unserialize into a safe public format. Prefer a constrained data format and
validated destination/storage names at integration boundaries.
[Unserialization warning](https://www.php.net/manual/en/function.unserialize.php).

Encode output for its actual HTML/JSON/URL context; `htmlspecialchars` is not SQL
parameterization or JavaScript-context escaping. Use established authentication
and session/CSRF controls where applicable. Use `password_hash`/`password_verify`
for passwords and cryptographic randomness such as `random_bytes` for tokens;
do not invent a password/hash protocol for an unrelated task. Keep production
displayed diagnostics separate from appropriately redacted server logs.
[HTML escaping](https://www.php.net/manual/en/function.htmlspecialchars.php),
[password hashing](https://www.php.net/manual/en/function.password-hash.php),
[randomness](https://www.php.net/manual/en/function.random-bytes.php).

Measure representative latency, memory, and downstream calls before changing
iteration, caches, OPcache/JIT, or worker count. CLI behavior is not an FPM/worker
benchmark. Account for request/job lifetime and memory growth in persistent
processes. Preserve output and isolation guarantees when optimizing; an array or
simple loop can be clearer and fast enough.

## Versions and migration

Record the supported PHP range, actual CLI/deployment versions, architecture,
SAPI, extensions, configuration, and dependency lock state. Composer's simulated
platform does not replace checks on the real target. Check upstream support
dates and the distribution's patch policy; a distro backport version is not the
same statement as the latest upstream release.
[Supported PHP branches](https://www.php.net/supported-versions.php).

Use versioned capabilities only when they solve the current problem: enums,
readonly properties and Fibers need 8.1; readonly classes need 8.2; typed class
constants and readonly clone reinitialization need 8.3. Property hooks,
asymmetric visibility, and lazy objects are 8.4 features; the pipe operator is
8.5. Hooks or pipelines do not replace intent methods or justify rewriting simple
calls. Review signature/coercion/deprecation and extension changes when crossing
versions, including implicit nullable declarations and dynamic properties.
[8.2 migration](https://www.php.net/manual/en/migration82.php),
[8.3 migration](https://www.php.net/manual/en/migration83.php),
[8.4 migration](https://www.php.net/manual/en/migration84.php),
[8.5 migration](https://www.php.net/manual/en/migration85.php).

K06 examples ran on PHP 8.3.6 from Ubuntu's 8.3.6-0ubuntu0.24.04.11 packages,
with Composer 2.10.3 and PHPStan 2.2.14. Analyzer targeting of PHP 8.2 syntax
does not establish execution on 8.2/8.4/8.5 or another SAPI. Optional examples:
[input/domain](examples/input-domain.md) and [resources](examples/resources.md).
The [research note](../../docs/research/2026-09-21-php-engineering-practices.md)
records evidence/alternatives; the
[practice plan](../../docs/plans/2026-09-21-engineering-practices.md) records actual
checks. Neither is mandatory reading for routine PHP work.
