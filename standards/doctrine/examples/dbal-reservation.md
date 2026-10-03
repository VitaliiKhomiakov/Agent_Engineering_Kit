# Example: a DBAL reservation with one transaction owner

Read when a direct SQL operation needs an atomic state predicate, typed results
and rollback across several writes. See [queries and DBAL](../queries-dbal.md).
This infrastructure adapter uses no ORM entity, Symfony kernel or generic CRUD
repository. An application may expose it behind its existing consumer-owned port.

The operation changes stock only when enough remains and then records the
reservation in the same transaction. Missing and insufficient stock deliberately
share `Unavailable`; this contract avoids inferring a more precise reason from a
racy follow-up read. Accepted returns only after the outer commit. Nesting is
explicitly rejected because this operation owns that boundary.

A reference is unique, but duplicate requests are **not** implemented as idempotent
success: they raise the database constraint error and roll back. A production
idempotency protocol would need to compare the original request/result. Translate
only known database errors at an application adapter boundary; do not expose SQL
or exception details as public responses.

Create these files in an **empty temporary directory** with PHP 8.2+, PDO SQLite, Filter
and Composer. The limits and schema belong to this example. Retain its generated
Composer lockfile for repeatable dependency resolution.

## Files

### `composer.json`

```json
{
  "name": "agents-framework/dbal-reservation",
  "description": "Isolated executable Doctrine example for K08.",
  "type": "project",
  "license": "MIT",
  "require": {
    "doctrine/dbal": "^4.4",
    "ext-filter": "*",
    "ext-pdo": "*",
    "ext-pdo_sqlite": "*",
    "php": "^8.2"
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

### `src/ReservationOutcome.php`

```php
<?php

declare(strict_types=1);

namespace Example;

enum ReservationOutcome
{
    case Accepted;
    case Unavailable;
}
```

### `src/StockReservations.php`

```php
<?php

declare(strict_types=1);

namespace Example;

use Doctrine\DBAL\Connection;
use Doctrine\DBAL\ParameterType;
use InvalidArgumentException;
use LogicException;
use UnexpectedValueException;

final class StockReservations
{
    public function __construct(private readonly Connection $connection) {}

    public function reserve(string $sku, int $units, string $reference): ReservationOutcome
    {
        if ($sku === '' || strlen($sku) > 32 || $units < 1 || $units > 1000
            || $reference === '' || strlen($reference) > 64) {
            throw new InvalidArgumentException('Invalid reservation values.');
        }
        if ($this->connection->isTransactionActive()) {
            throw new LogicException('This operation owns its outer transaction.');
        }
        return $this->connection->transactional(
            static function (Connection $db) use ($sku, $units, $reference): ReservationOutcome {
                $affected = $db->executeStatement(
                    'UPDATE stock SET available = available - ? WHERE sku = ? AND available >= ?',
                    [$units, $sku, $units],
                    [ParameterType::INTEGER, ParameterType::STRING, ParameterType::INTEGER],
                );
                if ($affected === 0 || $affected === '0') {
                    // Missing and insufficient stock share this operation's refusal contract.
                    return ReservationOutcome::Unavailable;
                }
                if ($affected !== 1 && $affected !== '1') {
                    throw new UnexpectedValueException('Unexpected affected-row count.');
                }
                $db->executeStatement(
                    'INSERT INTO reservations (reference, sku, units) VALUES (?, ?, ?)',
                    [$reference, $sku, $units],
                    [ParameterType::STRING, ParameterType::STRING, ParameterType::INTEGER],
                );
                return ReservationOutcome::Accepted;
            },
        );
    }

    public function available(string $sku): ?int
    {
        $result = $this->connection->executeQuery(
            'SELECT available FROM stock WHERE sku = ?', [$sku], [ParameterType::STRING],
        );
        try {
            $row = $result->fetchAssociative();
        } finally {
            $result->free();
        }
        if ($row === false) {
            return null;
        }
        $value = $row['available'] ?? null;
        if (is_string($value) && preg_match('/^(0|[1-9][0-9]*)$/D', $value) === 1) {
            $value = filter_var($value, FILTER_VALIDATE_INT);
        }
        if (!is_int($value) || $value < 0 || $value > 1000) {
            throw new UnexpectedValueException('Invalid stored stock.');
        }
        return $value;
    }
}
```

### `tests/run.php`

```php
<?php

declare(strict_types=1);

use Doctrine\DBAL\DriverManager;
use Doctrine\DBAL\Exception\UniqueConstraintViolationException;
use Example\ReservationOutcome;
use Example\StockReservations;

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

$db = DriverManager::getConnection(['driver' => 'pdo_sqlite', 'memory' => true]);
try {
    $db->executeStatement('PRAGMA foreign_keys = ON');
    $db->executeStatement('CREATE TABLE stock (sku VARCHAR(32) PRIMARY KEY NOT NULL,
        available INTEGER NOT NULL CHECK (available BETWEEN 0 AND 1000))');
    $db->executeStatement('CREATE TABLE reservations (reference VARCHAR(64) PRIMARY KEY NOT NULL,
        sku VARCHAR(32) NOT NULL REFERENCES stock(sku), units INTEGER NOT NULL CHECK (units > 0))');
    $db->executeStatement('INSERT INTO stock (sku, available) VALUES (?, ?)', ['CHAIR', 5]);
    $store = new StockReservations($db);
    expectFailure(InvalidArgumentException::class, fn () => $store->reserve('CHAIR', 0, 'bad'));
    check($store->available('CHAIR') === 5, 'Invalid input must not change stock.');
    check($store->available('MISSING') === null, 'Absence differs from zero.');
    check($store->reserve('CHAIR', 3, "r'; DROP TABLE stock; --") === ReservationOutcome::Accepted,
        'Reference must be bound as data.');
    check(!$db->isTransactionActive() && $store->available('CHAIR') === 2, 'Success follows commit.');
    check($store->reserve('CHAIR', 3, 'too-many') === ReservationOutcome::Unavailable,
        'The UPDATE predicate enforces current availability.');
    check($store->reserve("' OR 1=1 --", 1, 'injection') === ReservationOutcome::Unavailable,
        'SKU must be bound as data.');
    check($store->available('CHAIR') === 2, 'Refusal must preserve stock.');
    expectFailure(UniqueConstraintViolationException::class,
        fn () => $store->reserve('CHAIR', 1, "r'; DROP TABLE stock; --"));
    check(!$db->isTransactionActive() && $store->available('CHAIR') === 2,
        'Failure in the second write must roll back the first write.');
    check($db->fetchOne('SELECT reference FROM reservations WHERE reference = ?', ['too-many']) === false,
        'Refusal must not leave a reservation.');
    check($store->reserve('CHAIR', 2, 'last') === ReservationOutcome::Accepted, 'Exact depletion.');
    check($store->available('CHAIR') === 0, 'Zero remains a valid result.');
    check($store->reserve('CHAIR', 1, 'empty') === ReservationOutcome::Unavailable, 'No overselling.');
    $db->beginTransaction();
    expectFailure(LogicException::class, fn () => $store->reserve('CHAIR', 1, 'nested'));
    check($db->isTransactionActive(), 'Reject nesting without changing caller transaction.');
    $db->rollBack();
    echo "DBAL: atomic acceptance/refusal, binding, absence/zero, rollback and transaction ownership passed.\n";
} finally {
    $db->close();
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

The runner owns an in-memory SQLite database and enables foreign keys. Parameter
binding keeps the deliberately SQL-like reference and SKU as data. The row decoder
distinguishes absence from zero and accepts only an in-range integer or validated
integer string; it does not assert that every driver returns PHP ints. Its Result
is released in `finally`, and the runner closes the connection.

Verified on 2026-09-21 with PHP 8.3.6, DBAL 4.4.4 and SQLite 3.45.1. Strict Composer,
optimized autoload/platform, syntax, executable success/failure and PHPStan 2.2.14
max (10), PHP target 80200, checks passed, with no type ignores/baseline. Runtime
checks remain active with `zend.assertions=-1`.

The checks cover invalid input without mutation, accepted reservation, current
stock refusal, SQL-like values, missing versus zero stock, exact depletion,
rollback of the stock update when the audit insert fails, and caller transaction
preservation on rejected nesting. The same connection remains usable after the
observed uniqueness rollback; this is not a promise about a broken connection.

Only SQLite's actual integer rows were executed; other driver's string/decimal
representations, simultaneous writers, deadlocks, ambiguous commits and production
migration deployment were not tested. The conditional UPDATE has a single-row
predicate, but target-platform concurrency/isolation still needs relevant checks.
This example sends no external messages and makes no distributed-transaction claim.
