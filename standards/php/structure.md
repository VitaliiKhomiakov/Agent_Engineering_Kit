# PHP structure and dependencies

Read when changing namespaces/autoloading, packages, construction, dependency
boundaries, or patterns. [Common policy](../core.md) owns general design rules
and size signals. Language guidance targets PHP 8.2+ where compatible with the
project; newer APIs are conditional, not an instruction to upgrade.

## Modules and autoloading

Keep each named PSR-4-loaded class, interface, trait, or enum in its matching file
and namespace, with exact case. This is the existing profile convention; PHP
itself permits several declarations per file. Group cohesive responsibilities
through namespaces/directories instead of creating a folder for each pattern.
The PSR-4 specification defines name/path mapping, not a mandatory application
layer hierarchy. [PSR-4](https://www.php-fig.org/psr/psr-4/).

Use the project's Composer autoloader and declared `autoload`/`autoload-dev`
mapping rather than scattered manual includes or a second bespoke loader.
Namespaced functions are not loaded by PSR-4 class lookup; when needed, declare
them through the existing `files` mechanism or an explicit entry-point include.
Keep autoloaded files free of output, network calls, and hidden bootstrap effects.
[Composer autoload schema](https://getcomposer.org/doc/04-schema.md#autoload).

Put HTTP/CLI/queue parsing in adapters, application coordination behind them,
and independent state rules in the business owner. Persistence and SDK adapters
translate their external formats. A small script or read model need not acquire
an entity/service/repository hierarchy. When Doctrine ORM is used, preserve the
chosen approach under its [model placement rules](../doctrine/models-mapping.md#domain-model-placement).
Other persistence tools retain their own mapping and domain contracts.

## Construction and useful abstraction

Pass ready dependencies through constructors or function parameters; assemble
them in bootstrap. A container can help a large application assemble its graph,
but does not belong in every service as a global lookup catalog. Prefer an
explicit configuration object over ambient reads of environment variables from
business methods. Keep constructors free of hidden network or persistence work.

Centralize domain creation rules or complex assembly in a named constructor,
factory, or existing composition function. Ordinary creation of a simple DTO is
direct. A parsing constructor such as `fromJson()` has a real boundary purpose;
a factory forwarding identical arguments to every class does not.

Use a small interface for a real replaceable integration or consumer contract;
do not create one for every implementation. A typed callable/Closure can model
one operation. Choose composition when behavior merely delegates to another
component; inheritance must preserve the parent's semantics and substitutability.
Traits share implementation, not dependency ownership or an excuse for a hidden
service locator. [Interfaces](https://www.php.net/manual/en/language.oop5.interfaces.php),
[traits](https://www.php.net/manual/en/language.oop5.traits.php).

An enum suits a finite domain set with distinct cases; plain constants or a
validated string can be sufficient for open external values. Strategy/Facade/
Repository or a Result/Option abstraction is optional when an actual variation,
subsystem boundary, or established composition style benefits. A branch, function,
nullable result, or specific exception is often simpler. Do not add a monadic
library, universal base entity, or service hierarchy solely to name a pattern.
[Enums](https://www.php.net/manual/en/language.enumerations.overview.php).

## Dependency reproducibility

Inspect `composer.json`, the existing lockfile policy, PHP/extensions in the
actual CLI and deployment SAPI, and any Composer platform override. For an
application with a lockfile, `install` reproduces locked versions; `update`
resolves versions and changes the lock. Libraries must also test their supported
dependency ranges; their lockfile alone does not establish consumer compatibility.
Use the existing workflow and avoid an unrelated dependency refresh.
[Composer basics](https://getcomposer.org/doc/01-basic-usage.md).

Declare direct package and extension requirements used by production code;
development analyzers/test tools belong in development requirements. Composer's
`config.platform` simulates a platform for solving, not the actual runtime.
Use `check-platform-reqs` against the deployment environment when applicable;
`--ignore-platform-reqs` is not a compatibility fix.
[Platform configuration](https://getcomposer.org/doc/06-config.md#platform),
[platform checks](https://getcomposer.org/doc/03-cli.md#check-platform-reqs).

Plugins and scripts may execute code during Composer commands. Use the project's
reviewed plugin/script policy; inspect unfamiliar packages and avoid granting
blanket plugin permission. Local documentation examples need neither a global
Composer installation nor execution of a real project's scripts.
[Composer execution model](https://getcomposer.org/doc/faqs/how-to-install-untrusted-packages-safely.md).
