# Example: ORM persistence and failed units of work

Read when the distinction between entity invariants, managed state and committed
storage affects a decision. This deliberately illustrates the already-supported
`mapped-rich` option; it does not choose that architecture for another project.
See [model placement](../models-mapping.md#domain-model-placement) and
[transaction ownership](../unit-of-work-transactions.md).

The entity has an intent method, private state and an optimistic version. The
small executable harness owns persistence; it is not an HTTP controller or a
complete application scaffold. No service or EntityManager is injected into the
entity. Separate-domain projects can apply the same persistence checks to their
record/adapter while keeping behavior in their independent model.

Create these files in an **empty temporary directory**. Use PHP 8.2+ with the
listed SQLite extensions and Composer. The shown configuration is for PHP 8.2/8.3
and generated proxies; the class is deliberately non-final. For native lazy
objects on PHP 8.4+, consult the installed ORM configuration API. Composer ranges
are example constraints; keep the generated lockfile to reproduce the resolution.

## Files

### `composer.json`

```json
{
  "name": "agents-framework/orm-unit-of-work",
  "description": "Isolated executable Doctrine example for K08.",
  "type": "project",
  "license": "MIT",
  "require": {
    "php": "^8.2",
    "ext-pdo": "*",
    "ext-pdo_sqlite": "*",
    "doctrine/orm": "^3.7",
    "doctrine/dbal": "^4.4",
    "symfony/cache": "^7.4"
  },
  "autoload": {
    "psr-4": {
      "Example\\": "src/"
    }
  },
  "config": {
    "allow-plugins": false,
    "sort-packages": true
  }
}
```

### `src/StockItem.php`

```php
<?php

declare(strict_types=1);

namespace Example;

use Doctrine\DBAL\Types\Types;
use Doctrine\ORM\Mapping as ORM;
use DomainException;
use InvalidArgumentException;

#[ORM\Entity]
#[ORM\Table(name: 'stock_items')]
class StockItem
{
    #[ORM\Id]
    #[ORM\Column(type: Types::STRING, length: 32)]
    private string $sku;

    #[ORM\Column(type: Types::INTEGER)]
    private int $available;

    #[ORM\Version]
    #[ORM\Column(type: Types::INTEGER)]
    private int $version = 1;

    public function __construct(string $sku, int $available)
    {
        if (preg_match('/^[A-Z][A-Z0-9-]{0,31}$/D', $sku) !== 1
            || $available < 0 || $available > 1000) {
            throw new InvalidArgumentException('Invalid initial stock.');
        }
        $this->sku = $sku;
        $this->available = $available;
    }

    public function reserve(int $units): void
    {
        if ($units < 1 || $units > 1000) {
            throw new InvalidArgumentException('Units must be between 1 and 1000.');
        }
        if ($units > $this->available) {
            throw new DomainException('Insufficient stock.');
        }
        $this->available -= $units;
    }

    public function sku(): string { return $this->sku; }
    public function available(): int { return $this->available; }
    public function version(): int { return $this->version; }
}
```

### `tests/run.php`

```php
<?php

declare(strict_types=1);

use Doctrine\DBAL\DriverManager;
use Doctrine\DBAL\Exception\UniqueConstraintViolationException;
use Doctrine\ORM\EntityManager;
use Doctrine\ORM\EntityManagerInterface;
use Doctrine\ORM\OptimisticLockException;
use Doctrine\ORM\ORMSetup;
use Doctrine\ORM\Tools\SchemaTool;
use Doctrine\ORM\Tools\SchemaValidator;
use Example\StockItem;

require dirname(__DIR__) . '/vendor/autoload.php';

function check(bool $condition, string $message): void
{
    if (!$condition) {
        throw new RuntimeException($message);
    }
}

/** @param class-string<Throwable> $type */
function expectFailure(string $type, Closure $operation): void
{
    try {
        $operation();
    } catch (Throwable $failure) {
        if ($failure instanceof $type) {
            return;
        }
        throw $failure;
    }
    throw new RuntimeException('Expected ' . $type);
}

function openManager(string $path): EntityManager
{
    // PHP 8.2/8.3 configuration with generated proxies; test caches only.
    $config = ORMSetup::createAttributeMetadataConfiguration(
        paths: [dirname(__DIR__) . '/src'], isDevMode: true,
    );
    return new EntityManager(
        DriverManager::getConnection(['driver' => 'pdo_sqlite', 'path' => $path]),
        $config,
    );
}

function loadStock(EntityManager $em): StockItem
{
    return $em->find(StockItem::class, 'CHAIR')
        ?? throw new RuntimeException('Fixture stock missing.');
}

$stock = new StockItem('CHAIR', 8);
expectFailure(InvalidArgumentException::class, fn () => new StockItem('', 8));
expectFailure(InvalidArgumentException::class, fn () => new StockItem('CHAIR', -1));
expectFailure(InvalidArgumentException::class, fn () => $stock->reserve(0));
expectFailure(DomainException::class, fn () => $stock->reserve(9));
check($stock->available() === 8, 'Refusal must not mutate stock.');

$path = tempnam(sys_get_temp_dir(), 'af-orm-');
if ($path === false) {
    throw new RuntimeException('Cannot allocate database fixture.');
}
/** @var list<EntityManager> $managers */
$managers = [];
try {
    $em = openManager($path);
    $managers[] = $em;
    check((new SchemaValidator($em))->validateMapping() === [], 'Mapping invalid.');
    // Disposable fixture only. Production schema changes need reviewed migrations.
    (new SchemaTool($em))->createSchema([$em->getClassMetadata(StockItem::class)]);
    check((new SchemaValidator($em))->schemaInSyncWithMetadata(), 'Schema mismatch.');

    $em->persist($stock);
    check($em->getConnection()->fetchOne('SELECT sku FROM stock_items') === false,
        'persist() must not be confused with insertion.');
    $em->wrapInTransaction(static function () use ($stock): void {
        $stock->reserve(2);
    });
    check(loadStock($em) === $stock, 'Identity map must return the managed instance.');
    $em->clear();
    $loaded = loadStock($em);
    check($loaded !== $stock && $loaded->available() === 6 && $loaded->sku() === 'CHAIR',
        'Check persisted state after clearing the identity map.');

    // Two independent managers load the same version before either writes.
    $rival = openManager($path);
    $managers[] = $rival;
    $stale = loadStock($rival);
    check($stale->version() === $loaded->version(), 'Expected same starting version.');
    $em->wrapInTransaction(static function () use ($loaded): void {
        $loaded->reserve(2);
    });
    expectFailure(OptimisticLockException::class, static function () use ($rival, $stale): void {
        $rival->wrapInTransaction(static function () use ($stale): void {
            $stale->reserve(1);
        });
    });
    check(!$rival->isOpen() && !$rival->getConnection()->isTransactionActive(),
        'Failed optimistic write must close its manager and end its transaction.');
    check($stale->available() === 5, 'Rollback does not rewind PHP objects.');
    $em->clear();
    check(loadStock($em)->available() === 4, 'Lost update must not overwrite committed stock.');

    // Even an executed flush remains reversible inside the outer transaction.
    $changing = loadStock($em);
    $failure = new RuntimeException('Required later database step failed.');
    try {
        $em->wrapInTransaction(static function (EntityManagerInterface $em) use ($changing, $failure): void {
            $changing->reserve(1);
            $em->flush();
            throw $failure;
        });
    } catch (RuntimeException $caught) {
        check($caught === $failure, 'Preserve the original failure.');
    }
    check(!$em->isOpen() && $changing->available() === 3, 'Discard failed context and objects.');
    $fresh = openManager($path);
    $managers[] = $fresh;
    check(loadStock($fresh)->available() === 4, 'Outer rollback must undo the flushed change.');

    $fresh->clear();
    expectFailure(UniqueConstraintViolationException::class, static function () use ($fresh): void {
        $fresh->wrapInTransaction(static function (EntityManagerInterface $em): void {
            $em->persist(new StockItem('CHAIR', 1));
        });
    });
    check(!$fresh->isOpen(), 'Database constraint failure must close the manager.');
    $final = openManager($path);
    $managers[] = $final;
    check(loadStock($final)->available() === 4, 'Constraint failure must preserve existing stock.');
    check($final->find(StockItem::class, 'MISSING') === null, 'Missing entity is explicit absence.');
    echo "ORM: mapping, persistence, identity map, refusal, optimistic conflict, rollback and constraint checks passed.\n";
} finally {
    foreach ($managers as $manager) {
        $manager->close();
        $manager->getConnection()->close();
    }
    if (!unlink($path)) {
        throw new RuntimeException('Cannot remove database fixture.');
    }
}
```

## Run and check

```sh
composer --no-plugins --no-scripts install --no-interaction --prefer-dist
composer --no-plugins --no-scripts validate --strict
composer --no-plugins --no-scripts dump-autoload --optimize --strict-psr --strict-ambiguous
composer --no-plugins --no-scripts check-platform-reqs --no-dev
php -d zend.assertions=-1 tests/run.php
```

For static checking with an existing PHPStan installation, save this as
`phpstan.neon` and run `php /path/to/phpstan.phar analyse --no-progress --debug`.
The temporary cache path is only an example-local setting.

```neon
parameters:
    level: max
    phpVersion: 80200
    paths:
        - src
        - tests
    tmpDir: var/phpstan
```

The runner allocates a fresh SQLite file, checks mapping/schema consistency and
removes its own database after closing every manager/connection. SchemaTool here
operates only on that disposable fixture. Do not run it against an application DB.

Verified on 2026-09-21 with PHP 8.3.6, ORM 3.7.1, DBAL 4.4.4, Collections 2.6.0,
Symfony Cache 7.4.19 and SQLite 3.45.1. Syntax, strict Composer/autoload/platform
checks, runtime checks with `zend.assertions=-1`, and PHPStan 2.2.14 at max (10),
PHP target 80200, passed. No type ignores or baseline were used.

The checks cover refusal without mutation, delayed insertion, flush/clear/reload,
identity-map reuse, an optimistic conflict between two independently loaded
versions, rollback after an executed flush, manager closure, a database uniqueness
failure, preserved state and explicit absence. A failed object remains changed;
new work loads a fresh object with a fresh manager.

This is a deterministic stale-version interleaving, not a simultaneous lock or
load test. It does not exercise association hydration/cascades, native lazy
objects, production migrations, another database's isolation or network failure.
The example's integer limits and SKU grammar are local business rules, not Doctrine
limits. Direct SQL writers need equivalent constraints/version handling. See
[schema verification](../schema-verification.md) for task-dependent checks.
