# Example: mapped input before a state-changing use case

Read when a Symfony JSON endpoint needs executed DTO validation, a separate live
business rule, and a safe public response. This fixture uses a real FrameworkBundle
kernel, container, route import, payload resolver, Validator and exception event.
A plain controller injects an application operation; it has no SQL/flush or
business calculation. Only the remaining seat count crosses the output boundary.
See [HTTP/validation](../http-validation.md).

Save the following files in a new isolated folder. The manifest targets Symfony
7.4 and PHP 8.2+; actual execution used PHP 8.3.6. Preserve the resulting lockfile
for repetition. In an existing application, use its dependencies/configuration
and existing KernelTestCase/WebTestCase instead of replacing them with this fixture.
The tiny kernel keeps wiring visible and does not prescribe an application layout.

`composer.json`:

```json
{
  "name": "af-example/symfony-request-boundary",
  "description": "Isolated Symfony engineering examples",
  "type": "project",
  "license": "proprietary",
  "require": {
    "ext-ctype": "*",
    "ext-iconv": "*",
    "ext-xml": "*",
    "php": "^8.2",
    "symfony/dependency-injection": "7.4.*",
    "symfony/event-dispatcher": "7.4.*",
    "symfony/framework-bundle": "7.4.*",
    "symfony/http-foundation": "7.4.*",
    "symfony/http-kernel": "7.4.*",
    "symfony/property-access": "7.4.*",
    "symfony/routing": "7.4.*",
    "symfony/serializer": "7.4.*",
    "symfony/validator": "7.4.*"
  },
  "config": {
    "allow-plugins": false,
    "sort-packages": true
  },
  "autoload": {
    "psr-4": {
      "AfExample\\RequestBoundary\\": "src/"
    }
  }
}
```

`src/ReservationInput.php`:

```php
<?php
declare(strict_types=1);

namespace AfExample\RequestBoundary;

use Symfony\Component\Validator\Constraints as Assert;

final readonly class ReservationInput
{
    public function __construct(
        #[Assert\Positive]
        public int $seats,
        #[Assert\NotBlank]
        #[Assert\Length(max: 100)]
        public string $privateNote,
    ) {
    }
}
```

`src/ReserveSeats.php`:

```php
<?php
declare(strict_types=1);

namespace AfExample\RequestBoundary;

use DomainException;
use InvalidArgumentException;

final class ReserveSeats
{
    private int $remaining = 2;

    public function reserve(int $seats): int
    {
        if ($seats < 1) {
            throw new InvalidArgumentException('Seat count must be positive');
        }
        if ($seats > $this->remaining) {
            throw new DomainException('Insufficient capacity');
        }
        $this->remaining -= $seats;
        return $this->remaining;
    }

    public function remaining(): int
    {
        return $this->remaining;
    }
}
```

`src/ReservationController.php`:

```php
<?php
declare(strict_types=1);

namespace AfExample\RequestBoundary;

use DomainException;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpKernel\Attribute\MapRequestPayload;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Serializer\Normalizer\AbstractNormalizer;

final class ReservationController
{
    public function __construct(private readonly ReserveSeats $reserveSeats)
    {
    }

    #[Route('/reservations', name: 'reserve_seats', methods: ['POST'], format: 'json')]
    public function __invoke(
        #[MapRequestPayload(
            acceptFormat: 'json',
            serializationContext: [AbstractNormalizer::ALLOW_EXTRA_ATTRIBUTES => false],
        )]
        ReservationInput $input,
    ): JsonResponse {
        try {
            $remaining = $this->reserveSeats->reserve($input->seats);
        } catch (DomainException) {
            return new JsonResponse(['error' => 'Capacity unavailable'], 409);
        }
        return new JsonResponse(['remaining' => $remaining], 201);
    }
}
```

`src/RequestErrorListener.php`:

```php
<?php
declare(strict_types=1);

namespace AfExample\RequestBoundary;

use Symfony\Component\EventDispatcher\Attribute\AsEventListener;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpKernel\Event\ExceptionEvent;
use Symfony\Component\HttpKernel\Exception\HttpExceptionInterface;
use Symfony\Component\HttpKernel\KernelEvents;
use Symfony\Component\Serializer\Exception\ExtraAttributesException;

#[AsEventListener(event: KernelEvents::EXCEPTION)]
final class RequestErrorListener
{
    public function __invoke(ExceptionEvent $event): void
    {
        $error = $event->getThrowable();
        if ($error instanceof ExtraAttributesException
            && $event->getRequest()->attributes->get('_route') === 'reserve_seats') {
            $event->setResponse(new JsonResponse(['error' => 'Request rejected'], 400));
            return;
        }
        if (!$error instanceof HttpExceptionInterface) {
            return;
        }
        $status = $error->getStatusCode();
        if ($status >= 400 && $status < 500) {
            $event->setResponse(new JsonResponse(
                ['error' => 'Request rejected'], $status, $error->getHeaders(),
            ));
        }
    }
}
```

`src/ExampleKernel.php`:

```php
<?php
declare(strict_types=1);

namespace AfExample\RequestBoundary;

use Symfony\Bundle\FrameworkBundle\FrameworkBundle;
use Symfony\Bundle\FrameworkBundle\Kernel\MicroKernelTrait;
use Symfony\Component\HttpKernel\Bundle\BundleInterface;
use Symfony\Component\HttpKernel\Kernel;

final class ExampleKernel extends Kernel
{
    use MicroKernelTrait;

    /** @return iterable<BundleInterface> */
    public function registerBundles(): iterable
    {
        yield new FrameworkBundle();
    }

    public function getProjectDir(): string
    {
        return dirname(__DIR__);
    }

}
```

`config/services.php`:

```php
<?php
declare(strict_types=1);

use AfExample\RequestBoundary\RequestErrorListener;
use AfExample\RequestBoundary\ReservationController;
use AfExample\RequestBoundary\ReserveSeats;
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

return static function (ContainerConfigurator $container): void {
    $container->extension('framework', [
        'secret' => 'local-example-only',
        'router' => ['utf8' => true],
        'http_method_override' => false,
        'validation' => ['enable_attributes' => true],
        'serializer' => ['enabled' => true],
    ]);
    $services = $container->services()->defaults()->autowire()->autoconfigure();
    $services->set(ReserveSeats::class)->public(); // Inspect the example's state in tests.
    $services->set(ReservationController::class)->tag('controller.service_arguments');
    $services->set(RequestErrorListener::class);
};
```

`config/routes.php`:

```php
<?php
declare(strict_types=1);

use Symfony\Component\Routing\Loader\Configurator\RoutingConfigurator;

return static function (RoutingConfigurator $routes): void {
    $routes->import(dirname(__DIR__) . '/src/ReservationController.php', 'attribute');
};
```

`tests/run.php`:

```php
<?php
declare(strict_types=1);

use AfExample\RequestBoundary\ExampleKernel;
use AfExample\RequestBoundary\ReservationInput;
use AfExample\RequestBoundary\ReserveSeats;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Validator\Validation;

require dirname(__DIR__) . '/vendor/autoload.php';

function check(bool $condition, string $message): void
{
    if (!$condition) {
        throw new RuntimeException($message);
    }
}

function send(ExampleKernel $kernel, string $body, string $type = 'application/json', string $method = 'POST'): Response
{
    $request = Request::create('/reservations', $method, server: ['CONTENT_TYPE' => $type], content: $body);
    $response = $kernel->handle($request);
    $kernel->terminate($request, $response);
    return $response;
}

$kernel = new ExampleKernel('test', false);
try {
    $kernel->boot();
    $operation = $kernel->getContainer()->get(ReserveSeats::class);
    if (!$operation instanceof ReserveSeats) {
        throw new RuntimeException('Unexpected service contract');
    }
    $invalid = [
        ['{', 'application/json', 400],
        ['{"seats":1,"privateNote":"private","admin":true}', 'application/json', 400],
        ['{"seats":0,"privateNote":"private"}', 'application/json', 422],
        ['{"seats":"1","privateNote":"private"}', 'application/json', 422],
        ['{"privateNote":"private"}', 'application/json', 422],
        ['{"seats":null,"privateNote":"private"}', 'application/json', 422],
        ['{"seats":1,"privateNote":""}', 'application/json', 422],
        ['{"seats":1,"privateNote":"private"}', 'text/plain', 415],
    ];
    foreach ($invalid as [$body, $type, $status]) {
        $response = send($kernel, $body, $type);
        check($response->getStatusCode() === $status, 'Unexpected invalid-input status: ' . $body . ' => ' . $response->getStatusCode());
        check($response->getContent() === '{"error":"Request rejected"}', 'Unsafe error response');
        check($operation->remaining() === 2, 'Rejected input changed capacity');
    }
    $wrongMethod = send($kernel, '', method: 'GET');
    check($wrongMethod->getStatusCode() === 405, 'Route must enforce POST');
    check($wrongMethod->headers->get('Allow') === 'POST', 'Error mapping lost Allow');

    $success = send($kernel, '{"seats":1,"privateNote":"private"}');
    check($success->getStatusCode() === 201 && $success->getContent() === '{"remaining":1}', 'Public projection is wrong');
    $conflict = send($kernel, '{"seats":2,"privateNote":"private"}');
    check($conflict->getStatusCode() === 409 && $operation->remaining() === 1, 'Failed reservation changed state');
    check(send($kernel, '{"seats":1,"privateNote":"private"}')->getStatusCode() === 201, 'Failed request consumed capacity');

    $dto = new ReservationInput(0, ''); // Attributes do not run on construction.
    $validator = Validation::createValidatorBuilder()->enableAttributeMapping()->getValidator();
    check(count($validator->validate($dto)) === 2, 'Non-HTTP entry must invoke validation');
    try {
        (new ReserveSeats())->reserve(0);
        throw new LogicException('Expected the application invariant');
    } catch (InvalidArgumentException) {
    }
    echo "request-boundary: HTTP rejection, state, projection, wiring and explicit validation passed\n";
} finally {
    $kernel->shutdown();
}
```

Run from that isolated folder with the available tools:

```sh
composer --no-plugins --no-scripts install --no-interaction
composer --no-plugins --no-scripts validate --strict
composer --no-plugins --no-scripts dump-autoload --optimize --strict-psr --strict-ambiguous
php -d zend.assertions=-1 tests/run.php
phpstan analyse --level=max --no-progress src config tests
```

Use the analyzer's supported PHP target; exact checked versions/configuration,
syntax checks and outcomes are in the
[practice plan](../../../docs/plans/2026-09-21-engineering-practices.md).
A fresh install without the retained lockfile resolves the declared ranges again.

The specific ExtraAttributesException mapping is needed on the checked 7.4.19
stack: the payload resolver leaves that exception unconverted and it otherwise
becomes 500. The listener is scoped to this input-only serialization route and
preserves ordinary HTTP error status/headers while hiding implementation details.
A larger app must distinguish input mapping from response serialization; do not
make every Serializer exception a client error. Keep unexpected failures on the
normal internal-error path. The private note is deliberately not returned.

The stateful ReserveSeats service is an in-process demonstration of a live rule,
shared across these requests so rejected writes can be observed. It is not durable
inventory, concurrency control, or appropriate global user state in a worker.
The public registration exists only to inspect this fixture's state; ordinary
services stay private. The fixed secret is local fixture configuration, not a
deployment secret. When changing fixture wiring with debug disabled, rebuild only
its generated cache before checking the new container.

No SecurityBundle, real authentication, database, network server, message bus,
request-body cap or persistence transaction is configured. This example establishes
mapping/state/output behavior, not production authorization or atomicity. Attribute
metadata alone does not protect a direct call: the final checks explicitly invoke
Validator and the application invariant outside HTTP.
