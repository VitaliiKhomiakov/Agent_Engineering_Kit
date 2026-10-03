# Example: bounded reading with one resource owner

Read when an operation must release a stream even after finding its answer early
or rejecting a record. A typed opener transfers ownership of a new stream to
LineReader; the reader closes it in `finally`. This sequential operation does
not benefit from a resource-owning generator or a general context framework.
See [state and effects](../state-effects.md).

Save these files in their own temporary folder. They use PHP 8.2-compatible syntax,
the standard stream API, and Composer PSR-4; no external I/O or test framework is
required. PHP cannot declare a native `resource` return type, so PHPDoc expresses
that checked acquisition contract and the Closure's precise return type.

`composer.json`:

```json
{
  "name": "af-example/resources",
  "description": "Isolated PHP stream ownership example",
  "type": "project",
  "license": "proprietary",
  "require": {"php": "^8.2"},
  "autoload": {"psr-4": {"AfExample\\Resources\\": "src/"}}
}
```

`src/LineReader.php`:

```php
<?php
declare(strict_types=1);

namespace AfExample\Resources;

use Closure;
use LengthException;
use RuntimeException;

final class LineReader
{
    /** @param Closure(): resource $open Returns a new owned readable stream. */
    public function __construct(private readonly Closure $open)
    {
    }

    public function firstNonEmpty(): ?string
    {
        $stream = ($this->open)();
        try {
            while (($line = fgets($stream, 1026)) !== false) {
                // Bound the complete record including its newline, if present.
                if (strlen($line) > 1024) {
                    throw new LengthException('Record exceeds the byte limit');
                }
                $value = rtrim($line, "\r\n");
                if ($value !== '') {
                    return $value;
                }
            }
            if (!feof($stream)) {
                throw new RuntimeException('Stream read failed');
            }
            return null;
        } finally {
            fclose($stream);
        }
    }
}
```

`tests/run.php`:

```php
<?php
declare(strict_types=1);

use AfExample\Resources\LineReader;

require dirname(__DIR__) . '/vendor/autoload.php';

function check(bool $condition, string $message): void
{
    if (!$condition) {
        throw new RuntimeException($message);
    }
}

/** @return resource */
function streamWith(string $content)
{
    $stream = tmpfile();
    if ($stream === false) {
        throw new RuntimeException('Cannot create test stream');
    }
    try {
        if (fwrite($stream, $content) !== strlen($content) || !rewind($stream)) {
            throw new RuntimeException('Cannot prepare test stream');
        }
    } catch (Throwable $error) {
        fclose($stream);
        throw $error;
    }
    return $stream;
}

$cases = [
    ['', null],
    ["\n\r\n", null],
    ["\n0\nignored\n", '0'],
    ["\nfirst\nsecond\n", 'first'],
    [str_repeat('x', 1024), str_repeat('x', 1024)],
];
foreach ($cases as [$content, $expected]) {
    $stream = streamWith($content);
    $reader = new LineReader(static fn () => $stream);
    check($reader->firstNonEmpty() === $expected, 'Unexpected first record');
    check(get_resource_type($stream) === 'Unknown', 'Reader did not close its stream');
}

$stream = streamWith(str_repeat('x', 1025));
$reader = new LineReader(static fn () => $stream);
try {
    $reader->firstNonEmpty();
    throw new RuntimeException('Expected an oversized record rejection');
} catch (LengthException) {
    check(get_resource_type($stream) === 'Unknown', 'Rejected input leaked the stream');
}

$failure = new RuntimeException('Opening failed');
$reader = new LineReader(static function () use ($failure): never {
    throw $failure;
});
try {
    $reader->firstNonEmpty();
    throw new LogicException('Expected an acquisition failure');
} catch (RuntimeException $error) {
    check($error === $failure, 'Acquisition failure was replaced');
}
echo "resources: 7 EOF/early-return/boundary/failure cases passed\n";
```

Run with the project's installed tools:

```sh
composer --no-plugins --no-scripts validate --strict
composer --no-plugins --no-scripts dump-autoload --optimize --strict-psr --strict-ambiguous
php -l src/LineReader.php
php -l tests/run.php
php -d zend.assertions=-1 tests/run.php
phpstan analyse --level=max --no-progress src tests
```

The checked setup used PHP 8.3.6 and PHPStan 2.2.14 level 10 targeting PHP 8.2.
Actual commands and outcomes are in the
[practice plan](../../../docs/plans/2026-09-21-engineering-practices.md).

The opener must return a new valid readable stream or throw; it must not lend a
handle another consumer still owns. The tests create real temporary streams and
observe closure after consumption, but do not simulate a device failure or a
failed close. The reader assumes a local blocking stream: it is not a network
timeout, cancellation protocol, total-input limit, or generator-close API. An
endless sequence of empty records needs an operation budget in a streaming service.
The fixture writer rejects partial preparation; it is not a general production
write-all implementation. `get_resource_type()` returns `Unknown` for a closed
handle; runtime tests establish that lifetime fact rather than a PHPDoc assertion.
