# PHP engineering practices: research and adoption

Research started and primary sources checked: **2026-09-21**. Scope: **K06, PHP**,
under the [practice plan](../plans/2026-09-21-engineering-practices.md). The
[PHP/Symfony/Doctrine profile](../../standards/php-symfony-doctrine.md) remains the
entry; four conditional PHP sections and two optional examples add language
detail. This note is evidence, not a required instruction or installed resource.

## Baseline, tools, and scope

The existing profile already required matching PSR-4 type files, named boundary
contracts, typed collections/maps, centralized meaningful construction, DI, and
preserved autoload/registration contracts. K06 explains PHP language/runtime and
tooling mechanisms behind those practices. Existing Symfony validation/controller
and Doctrine domain-placement guidance is preserved for K07/K08. This stage does
not implement a PHP service, select an ORM, or change workspace dependencies.

| Evidence checked | Applicability and limits |
| --- | --- |
| [PHP support schedule](https://www.php.net/supported-versions.php) | On 2026-09-21, 8.2/8.3 are in security support; 8.4/8.5 have active support. Recheck dates for a real migration rather than treating this as a permanent version recommendation |
| **PHP 8.3.6 CLI NTS**, Zend Engine 4.3.6, 64-bit Linux | Executed from Ubuntu package **8.3.6-0ubuntu0.24.04.11**, built 2026-09-02; this distribution build is not presented as the latest upstream PHP |
| **Composer 2.10.3**, **PHPStan 2.2.14** | Official PHARs, versions observed locally; PHPStan level max resolves to 10 here. Language target configured as 80200 |
| Example language scope | PHP 8.2-compatible syntax, including a readonly class; behavior executed on 8.3 only. No evidence for FPM, a persistent server, another architecture, or other PHP versions |
| [PHP 8.4 features](https://www.php.net/manual/en/migration84.new-features.php), [8.5 features](https://www.php.net/manual/en/migration85.new-features.php) | Property hooks/asymmetric visibility/lazy objects and the pipe operator are versioned options; their availability is not a reason to rewrite existing code |

PHP, Composer, PHPStan, Psalm, and PHPUnit were initially absent. Downloaded the
two PHP CLI/common packages from the configured Ubuntu archive, checked their
SHA256 against APT metadata, and extracted them under the stage's `/tmp` directory
without package installation. Downloaded pinned PHARs from the
[Composer release source](https://getcomposer.org/download/) and
[PHPStan 2.2.14 release](https://github.com/phpstan/phpstan/releases/tag/2.2.14),
checking Composer's published SHA256 and PHPStan's release-asset SHA256 digest.
No installer was executed. The temporary PHP configuration loads the extracted
Phar/ctype/tokenizer/iconv extensions; JSON is built in. Composer home/cache and
analyzer output stay under `/tmp`; checks disable Composer network, plugins and
scripts. The plan retains artifact/version/hash evidence.

## Coverage and strength

**R** is an Agent_Engineering_Kit requirement inherited from
[core](../../standards/core.md) or the existing PHP profile: named contracts,
owned invariants/effects, explicit dependencies, or reliable PSR-4 conventions.
**D** is a recommended default with a meaningful alternative; **O** is an optional
technique for a stated condition. PHP/Composer capability does not independently
require an architecture, package, or pattern. Recommendations were checked on
2026-09-21; specific minimum versions and untested configurations are identified.

| Research area | Decision and adoption owner |
| --- | --- |
| Architecture/modules | PSR-4 name/path/case, cohesive namespaces, independent business boundaries; [structure](../../standards/php/structure.md) |
| Construction/dependencies/patterns | Named constructors for rules, direct DTO construction, injected services/callables, conditional interfaces/factories; structure |
| Typed contracts/input/invariants/errors | Native/PHPDoc types, caller strictness, parsed mixed, presence/coercions, valid drafts, Throwable; [types/contracts](../../standards/php/types-contracts.md) |
| State/concurrency/cancellation/lifetime | Shallow readonly/clone, generator ownership, worker state, Fibers and external deadlines; [state/effects](../../standards/php/state-effects.md) |
| Persistence/integrations | Prepared values, transaction/effect ordering, driver limits, external adapters; state/effects |
| Tests/review | Runtime behavior, analyzer target, autoload checks, contract preservation and proportionate scope; [verification](../../standards/php/verification.md) |
| Security/operations/performance | Input/execution boundaries, encoding/secret handling, Composer execution, measured resource use; verification and structure |
| Versions/migration | Supported branch/build distinction, SAPI/extensions, lock/platform semantics and conditional modern features; verification |

PHP core does not provide a universal async scheduler, cancellation token, job
queue, or cross-system transaction. Those decisions belong to the selected
runtime/application and integration contract; K06 does not invent counterparts.

## Structure, dependencies, and pattern decisions

| Strength; problem and condition | Adopted form | Simpler alternative or cost; evidence |
| --- | --- | --- |
| R: named PSR-4 types must load reliably | One matching, case-correct file per named class/interface/trait/enum, grouped by cohesive namespace | Existing profile convention; PHP permits several declarations per file. PSR-4 specifies mapping, not a layer hierarchy. [PSR-4](https://www.php-fig.org/psr/psr-4/) |
| D: reproducible application/package loading | Existing Composer autoload/autoload-dev mappings; explicit files mechanism for functions when needed | Avoid scattered includes and competing loaders; a small explicit script remains possible. Autoloaded files should not perform hidden I/O. [Composer schema](https://getcomposer.org/doc/04-schema.md#autoload) |
| R: dependency/effect boundaries must remain visible | Ready dependencies in constructors/parameters, assembled in bootstrap | A container is optional assembly machinery, not a service locator in business code. Keep existing simple modules without mandatory scaffolding; core policy owns this rule |
| R: domain rules/complex assembly need one owner; O: factory/port | Named constructor or factory for meaningful creation; interface or precise callable for an actual integration/variation | Direct construction for ordinary DTOs; a branch or function before Strategy/Facade/Repository/Result hierarchies. [Interfaces](https://www.php.net/manual/en/language.oop5.interfaces.php), [enums](https://www.php.net/manual/en/language.enumerations.overview.php) |
| D: repeatable dependencies and known platform | Preserve application lock/install workflow; check real PHP/extensions and direct requirements | Update re-resolves; a library lock does not test all consumers. Platform emulation is not runtime verification. [Composer basics](https://getcomposer.org/doc/01-basic-usage.md), [platform config](https://getcomposer.org/doc/06-config.md#platform) |

Traits and inheritance can share behavior when their coupling/override semantics
are justified. Composition with a small consumer contract is simpler for ordinary
delegation. No one-interface-per-class, universal base model, global container,
or mandatory monadic package is adopted. These are policy decisions about current
requirements, not claims that PHP forbids the alternative mechanisms.

## Contracts, validation, and errors

**D — native types plus the analyzer's useful PHPDoc.** Use native declarations
and strict callers for ordinary application code; express collection members,
resources, and callable signatures in PHPDoc. Keep named DTOs at operation
boundaries. **R — narrow actual external data** instead of propagating `mixed` or
silencing analysis with an asserted shape. Generic annotations/array shapes can
help represent integration data but are not executable validation.
[Type declarations](https://www.php.net/manual/en/language.types.declarations.php),
[PHPDoc types](https://phpstan.org/writing-php-code/phpdoc-types).

A focused three-file probe established two easily confused facts: a weak caller
coerces a numeric string passed to a function declared in a strict file; a strict
caller rejects it. `array_map` still coerces through its internal callback path.
Consequently, a `strict_types` declaration in a DTO file is not a parser for all
its callers. Native strictness also does not replace bounds, presence rules, or
business invariants; it leaves other language conversions intact.
[Type juggling](https://www.php.net/manual/en/language.types.type-juggling.php).

**R — preserve wire meaning.** Distinguish missing, null, false, zero, and `"0"`.
Use `array_key_exists` where null differs from omission, and strict sentinel
comparisons where loose conversion is unwanted. **D — explicit JSON failure**
with JSON_THROW_ON_ERROR, followed by checked structure/values and chosen limits.
A cast can be an intentional conversion after validation, but is not a generic
validation strategy. Ordinary arrays remain appropriate for typed lists/maps and
serialization. [Presence](https://www.php.net/manual/en/function.array-key-exists.php),
[comparisons](https://www.php.net/manual/en/language.operators.comparison.php),
[JSON decoding](https://www.php.net/manual/en/function.json-decode.php).

**R — state transitions own live invariants.** A valid incomplete draft should
remain possible when the domain permits it. The input model can accept an empty
title while `publish()` rejects it; publication success can prevent later edits.
That distinction is illustrated in the
[input/domain example](../../standards/php/examples/input-domain.md), using an
independent Article and a parsing DTO. The domain can also be called without the
parser. Storage/concurrency checks and authorization remain outside the example.

**D — specific exceptions or an established typed result.** Nullable absence,
input rejection, domain refusal and infrastructure failure are different meanings.
Catch Throwable at an entry boundary only with a defined reporting/cleanup role;
it includes Errors such as TypeError. Preserve causes and safe public mapping,
without exposing rejected payloads or database details. Warnings/false results
need their actual API handling. An Option/Result package is optional where the
existing composition style warrants it; it is not required for one branch.
[Exceptions](https://www.php.net/manual/en/language.exceptions.php).

## State, resources, persistence, and concurrency

**D — readonly values when reassignment is unwanted.** Readonly does not make
the nested object immutable; ordinary clone also shares nested object state.
Both behaviors were reproduced locally. Use immutable nested values or an explicit
copy/transition policy when needed, rather than claiming deep immutability from
a modifier. Preserve aliases/capture ownership and reset job/request context in
persistent processes. [Properties](https://www.php.net/manual/en/language.oop5.properties.php),
[cloning](https://www.php.net/manual/en/language.oop5.cloning.php).

**R — explicit resource ownership.** Use finally around the actual consumption
scope and check false/error/partial-progress contracts. Destructors and shutdown
are unsuitable hidden commit boundaries. **O — lazy generators** when they avoid
unnecessary materialization; a retained generator after break can retain its
resource. A local probe observed the handle stay open after break and close only
when the generator was released. The
[resource example](../../standards/php/examples/resources.md) uses a simpler
bounded loop whose owner closes on early return, EOF and rejection.
[Generators](https://www.php.net/manual/en/language.generators.overview.php),
[fgets](https://www.php.net/manual/en/function.fgets.php),
[destructors](https://www.php.net/manual/en/language.oop5.decon.php).

**O — concurrency only for an actual workload.** Fibers suspend and resume a call
stack; they do not create a scheduler, make blocking I/O nonblocking, or provide
CPU parallelism. Reuse the application's runtime and cancellation contracts with
bounded work. **R — external effect budgets and honest failure.** PHP execution
time limits and client disconnect detection do not guarantee an I/O wall-clock
deadline or rollback. Set client/runtime budgets and idempotent retries where
needed. [Fibers](https://www.php.net/manual/en/language.fibers.php),
[time limits](https://www.php.net/manual/en/function.set-time-limit.php),
[connection handling](https://www.php.net/manual/en/features.connection-handling.php).

**R — persistence values and atomicity have owners.** Bind data values rather
than concatenate SQL, while selecting identifiers/fragments from an owned
allowlist. Commit required writes before reporting success; respect driver
rollback/implicit-commit behavior. A direct transaction block is simpler than a
unit-of-work abstraction for one cohesive operation. PDO is evidence for generic
PHP database boundaries, not a new application dependency or the K08 Doctrine
adoption. Remote calls do not become atomic because a database transaction is
open. [Prepared statements](https://www.php.net/manual/en/pdo.prepared-statements.php),
[PDO transactions](https://www.php.net/manual/en/pdo.transactions.php).

## Verification, security, operations, and compatibility

**D — combine the cheapest meaningful checks.** Syntax/PSR-4/static checks catch
different problems from runtime input/state/lifetime behavior. Use the existing
PHPStan/Psalm/test setup and applicable framework extensions; do not establish a
new test platform for a file move. PHPStan's versioned maximum is level 10 in
2.2.14; future `max` can change. Production invariants and these example tests do
not depend on runtime assert settings. **R — preserve existing contracts** when
moving code, including named arguments, class case, string registrations, and
serialization/mapping; a move is not authorization for a schema migration.
[PHPStan levels](https://phpstan.org/user-guide/rule-levels),
[Composer checks](https://getcomposer.org/doc/03-cli.md#dump-autoload-dumpautoload),
[assertions](https://www.php.net/manual/en/function.assert.php).

**R — protect exposed execution/disclosure boundaries.** Do not deserialize
untrusted native objects or pass input into eval/include/shell paths. Choose
output encoding for its context, use parameterized SQL separately, and preserve
safe errors/logs. **D — established security mechanisms** such as password_hash/
password_verify and random_bytes when the task handles passwords/tokens, with the
project's actual session/auth/CSRF policy. Avoid creating an auth framework for
unrelated work. Composer plugins/scripts are code execution and follow the
project's approved policy. [Unserialize](https://www.php.net/manual/en/function.unserialize.php),
[HTML encoding](https://www.php.net/manual/en/function.htmlspecialchars.php),
[passwords](https://www.php.net/manual/en/function.password-hash.php),
[randomness](https://www.php.net/manual/en/function.random-bytes.php),
[Composer execution](https://getcomposer.org/doc/faqs/how-to-install-untrusted-packages-safely.md).

**O — performance changes from measurement.** Bound/stream actual large inputs,
measure memory and downstream calls, and evaluate OPcache/JIT/caches/worker count
in the deployment SAPI. No blanket claim makes a generator, functional pipeline,
cache, or additional process faster for every task. Additional lifetime and
invalidation complexity needs a current benefit.

Compatibility review distinguishes library/runtime features and guarantees:
8.1 enums/readonly properties/Fibers; 8.2 readonly classes and dynamic-property
deprecation; 8.3 typed constants/readonly clone reinitialization; 8.4 property
hooks/asymmetric visibility/lazy objects and implicit-nullability deprecations;
8.5 pipelines. Existing named construction and intent methods remain useful.
The current properties manual still contains older restrictive wording below its
8.4 note about protected-set readonly initialization; K06 records the version
distinction rather than applying a timeless same-class-only rule.
[Properties](https://www.php.net/manual/en/language.oop5.properties.php),
[8.4 migration](https://www.php.net/manual/en/migration84.php),
[8.5 migration](https://www.php.net/manual/en/migration85.php).

## Evidence and limits

Both exact examples passed Composer strict manifest validation and optimized
PSR-4/duplicate-class checks, syntax checks, PHPStan level 10 targeting 8.2, and
runtime checks with assertions disabled. The input example covers ten rejected
wire inputs plus valid nullable/non-null notes, incomplete drafts, publication,
idempotent publication and forbidden edits. The resource example covers seven
EOF/early-return/boundary/acquisition/rejection cases and verifies closed handles.
Probe files separately establish the version-sensitive language observations.

No real database, framework controller, authentication system, network service,
worker scheduler, FPM deployment, concurrent write, failed device/close, or live
disconnect was exercised. Static PHP targeting is not a multi-version execution
matrix. Checks do not prove production performance or cleanup under forced
termination. The [practice plan](../plans/2026-09-21-engineering-practices.md)
records exact commands, delivery/portability checks, scoped baseline evidence,
remaining limits and the human review checkpoint. K07/K08 and P3–P7 remain planned.
