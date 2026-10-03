# Example: finish a lazy HTTP response before returning stock

Read when an integration must distinguish absence from failure, validate external
JSON, and release remaining response work. The adapter accepts a client scoped to
a trusted service, uses one fixed relative endpoint, and returns a named snapshot.
It owns HTTP status, idle/overall budgets, body bounds and decoding before success.
See [runtime/effects](../runtime-effects.md).

Save these files in a separate isolated folder. The manifest uses Symfony 7.4 and
PHP 8.2+; execution used PHP 8.3.6. Preserve the generated lockfile for repetition.
In an application, inject its configured scoped HttpClientInterface. Tests use the
real MockHttpClient/MockResponse components and make no network requests.

`composer.json`:

```json
{
  "name": "af-example/symfony-http-client",
  "description": "Isolated Symfony HTTP client boundary example",
  "type": "project",
  "license": "proprietary",
  "require": {
    "ext-json": "*",
    "php": "^8.2",
    "symfony/http-client": "7.4.*",
    "symfony/http-client-contracts": "^3.7"
  },
  "config": {
    "allow-plugins": false,
    "sort-packages": true
  },
  "autoload": {
    "psr-4": {
      "AfExample\\HttpClient\\": "src/"
    }
  }
}
```

`src/StockSnapshot.php`:

```php
<?php
declare(strict_types=1);

namespace AfExample\HttpClient;

final readonly class StockSnapshot
{
    public function __construct(public int $quantity)
    {
    }
}
```

`src/StockClient.php`:

```php
<?php
declare(strict_types=1);

namespace AfExample\HttpClient;

use JsonException;
use RuntimeException;
use Symfony\Contracts\HttpClient\Exception\TransportExceptionInterface;
use Symfony\Contracts\HttpClient\HttpClientInterface;
use Symfony\Contracts\HttpClient\ResponseInterface;

final class StockClient
{
    // Inject a client scoped to the trusted stock service's base URI.
    public function __construct(private readonly HttpClientInterface $client)
    {
    }

    public function current(): ?StockSnapshot
    {
        $response = null;
        try {
            $response = $this->client->request('GET', 'stock', [
                'timeout' => 1.0,
                'max_duration' => 3.0,
                'max_redirects' => 0,
                'buffer' => false,
            ]);
            $status = $response->getStatusCode();
            if ($status === 404) {
                return null;
            }
            if ($status !== 200) {
                throw new RuntimeException('Stock service rejected the request');
            }
            return $this->decode($this->readBody($response));
        } catch (TransportExceptionInterface $error) {
            throw new RuntimeException('Stock transport failed', 0, $error);
        } finally {
            $response?->cancel();
        }
    }

    private function readBody(ResponseInterface $response): string
    {
        $body = '';
        foreach ($this->client->stream($response) as $chunk) {
            if ($chunk->isTimeout()) {
                throw new RuntimeException('Stock response timed out');
            }
            $part = $chunk->getContent();
            if (strlen($body) + strlen($part) > 1024) {
                throw new RuntimeException('Stock response is too large');
            }
            $body .= $part;
        }
        return $body;
    }

    private function decode(string $body): StockSnapshot
    {
        try {
            $data = json_decode($body, true, 8, JSON_THROW_ON_ERROR);
        } catch (JsonException $error) {
            throw new RuntimeException('Invalid stock response', 0, $error);
        }
        if (!is_array($data) || !array_key_exists('quantity', $data)
            || !is_int($data['quantity']) || $data['quantity'] < 0) {
            throw new RuntimeException('Invalid stock response');
        }
        return new StockSnapshot($data['quantity']);
    }
}
```

`tests/run.php`:

```php
<?php
declare(strict_types=1);

use AfExample\HttpClient\StockClient;
use AfExample\HttpClient\StockSnapshot;
use Symfony\Component\HttpClient\Exception\TransportException;
use Symfony\Component\HttpClient\MockHttpClient;
use Symfony\Component\HttpClient\Response\MockResponse;

require dirname(__DIR__) . '/vendor/autoload.php';

function check(bool $condition, string $message): void
{
    if (!$condition) {
        throw new RuntimeException($message);
    }
}

function clientFor(MockResponse $response, bool &$canceled): StockClient
{
    $canceled = false;
    /** @param array<string, mixed> $info Transport metadata is narrowed here. */
    $observe = static function (int $downloaded, int $total, array $info) use (&$canceled): void {
        $canceled = $canceled || ($info['canceled'] ?? false) === true;
    };
    $client = (new MockHttpClient($response, 'https://stock.example/'))->withOptions(['on_progress' => $observe]);
    return new StockClient($client);
}

$response = new MockResponse('{"quantity":0,"internal":"private"}');
$canceled = false;
$snapshot = clientFor($response, $canceled)->current();
check($snapshot instanceof StockSnapshot && $snapshot->quantity === 0, 'Zero stock is valid');
check($response->getRequestMethod() === 'GET' && $response->getRequestUrl() === 'https://stock.example/stock', 'Wrong integration destination');
$options = $response->getRequestOptions();
check($options['buffer'] === false && $options['max_redirects'] === 0, 'Unexpected buffering or redirects');
check($options['timeout'] === 1.0 && $options['max_duration'] === 3.0, 'Missing request budgets');
check($canceled, 'Response owner did not finish');

$missing = new MockResponse('not a stock document', ['http_code' => 404]);
check(clientFor($missing, $canceled)->current() === null, '404 is absence');
check($canceled, '404 response leaked');

$failures = [
    [new MockResponse('internal failure', ['http_code' => 503]), 'Stock service rejected the request'],
    [new MockResponse('', ['http_code' => 302]), 'Stock service rejected the request'],
    [new MockResponse('{'), 'Invalid stock response'],
    [new MockResponse('{"quantity":"1"}'), 'Invalid stock response'],
    [new MockResponse('{"quantity":-1}'), 'Invalid stock response'],
    [new MockResponse('[]'), 'Invalid stock response'],
    [new MockResponse([str_repeat('x', 1024), 'x']), 'Stock response is too large'],
    [new MockResponse(['']), 'Stock response timed out'],
    [new MockResponse([new TransportException('private transport detail')]), 'Stock transport failed'],
];
foreach ($failures as [$response, $message]) {
    try {
        clientFor($response, $canceled)->current();
        throw new LogicException('Expected upstream rejection');
    } catch (RuntimeException $error) {
        check($error->getMessage() === $message, 'Wrong integration error: ' . $error->getMessage());
        check($canceled, 'Failure left response active');
    }
}

$transport = new TransportException('request creation failed');
$client = new StockClient(new MockHttpClient(static function () use ($transport): never {
    throw $transport;
}, 'https://stock.example/'));
try {
    $client->current();
    throw new LogicException('Expected request failure');
} catch (RuntimeException $error) {
    check($error->getPrevious() === $transport, 'Transport cause was lost');
}
echo "http-client: 12 success/absence/status/data/budget/transport cases passed\n";
```

Run from the isolated folder:

```sh
composer --no-plugins --no-scripts install --no-interaction
composer --no-plugins --no-scripts validate --strict
composer --no-plugins --no-scripts dump-autoload --optimize --strict-psr --strict-ambiguous
php -d zend.assertions=-1 tests/run.php
phpstan analyse --level=max --no-progress src tests
```

Exact checked versions, syntax/static checks and runtime outcomes are in the
[practice plan](../../../docs/plans/2026-09-21-engineering-practices.md).
A fresh install without the retained lockfile resolves the declared ranges again.

MockHttpClient issues a distinct response from the supplied MockResponse fixture.
The tests therefore observe cancellation through the supported on_progress metadata
of the issued response, narrowing that external metadata before use. The captured
flag belongs only to the test; checking the original fixture's canceled info would
observe the wrong object. An empty mock chunk models idle timeout and a yielded
exception models transfer failure. These are behavioral checks, not timing tests.

The byte limit bounds accumulated body data, not the size of a transport chunk
already allocated or all client/process memory. Timeout/max_duration options are
verified as configured; no real DNS, TLS, redirect, wall-clock timeout, retry,
backpressure or disconnect was exercised. Cancellation releases remaining local
response work; it does not roll back an upstream effect. This read uses no retries.

404 means absence by this integration contract; other status codes are failures.
The adapter ignores extra upstream fields and projects only a validated nonnegative
quantity. Runtime errors here carry fixed integration messages and preserve causes;
a public entry adapter still owns status mapping and redacted diagnostics. The
trusted base URI is a composition prerequisite, not a general arbitrary-URL API.
