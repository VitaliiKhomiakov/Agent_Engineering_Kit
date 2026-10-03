# Example: parse a draft, enforce publication in the domain

Read when a well-formed input can still describe a valid incomplete draft. The
parser owns JSON shape/presence/type/size rules; the article owns publication and
editing transitions. A nullable editor note is required and remains outside the
domain object. Empty titles are valid input but cannot be published; `"0"` is a
valid title. See [types and contracts](../types-contracts.md).

Save the following files in an isolated folder, preserving their indicated paths.
The example uses PHP 8.2+ syntax (readonly class), the built-in JSON extension,
and Composer PSR-4 autoloading, with no third-party runtime/test package. Checked
tools and actual results are recorded in the
[practice plan](../../../docs/plans/2026-09-21-engineering-practices.md).

`composer.json`:

```json
{
  "name": "af-example/input-domain",
  "description": "Isolated PHP boundary and domain example",
  "type": "project",
  "license": "proprietary",
  "require": {"php": "^8.2", "ext-json": "*"},
  "autoload": {"psr-4": {"AfExample\\InputDomain\\": "src/"}}
}
```

`src/DraftInput.php`:

```php
<?php
declare(strict_types=1);

namespace AfExample\InputDomain;

use InvalidArgumentException;
use JsonException;

final readonly class DraftInput
{
    private function __construct(
        public string $title,
        public ?string $editorNote,
    ) {
    }

    public static function fromJson(string $json): self
    {
        if (strlen($json) > 1024) {
            throw new InvalidArgumentException('Invalid draft input');
        }
        try {
            $data = json_decode($json, true, 16, JSON_THROW_ON_ERROR);
        } catch (JsonException $error) {
            throw new InvalidArgumentException('Invalid draft input', 0, $error);
        }
        if (!is_array($data) || array_is_list($data) || count($data) !== 2) {
            throw new InvalidArgumentException('Invalid draft input');
        }
        if (!array_key_exists('title', $data) || !array_key_exists('editorNote', $data)) {
            throw new InvalidArgumentException('Invalid draft input');
        }
        if (!is_string($data['title']) || strlen($data['title']) > 80) {
            throw new InvalidArgumentException('Invalid draft input');
        }
        $note = $data['editorNote'];
        if ($note !== null && (!is_string($note) || strlen($note) > 200)) {
            throw new InvalidArgumentException('Invalid draft input');
        }
        return new self($data['title'], $note);
    }
}
```

`src/Article.php`:

```php
<?php
declare(strict_types=1);

namespace AfExample\InputDomain;

use DomainException;

final class Article
{
    private bool $published = false;

    private function __construct(private string $title)
    {
    }

    public static function draft(string $title): self
    {
        return new self($title);
    }

    public function rename(string $title): void
    {
        if ($this->published) {
            throw new DomainException('Published articles cannot be renamed');
        }
        $this->title = $title;
    }

    public function publish(): void
    {
        if (trim($this->title) === '') {
            throw new DomainException('Publication requires a title');
        }
        $this->published = true;
    }

    public function title(): string
    {
        return $this->title;
    }

    public function isPublished(): bool
    {
        return $this->published;
    }
}
```

`tests/run.php` uses explicit failing checks, independent of `zend.assertions`:

```php
<?php
declare(strict_types=1);

use AfExample\InputDomain\Article;
use AfExample\InputDomain\DraftInput;

require dirname(__DIR__) . '/vendor/autoload.php';

function check(bool $condition, string $message): void
{
    if (!$condition) {
        throw new RuntimeException($message);
    }
}

/** @param callable(): void $operation */
function rejectsTransition(callable $operation): void
{
    try {
        $operation();
    } catch (DomainException) {
        return;
    }
    throw new RuntimeException('Expected a rejected transition');
}

$invalid = [
    'malformed' => '{',
    'wrong root' => '[]',
    'missing nullable field' => '{"title":"A"}',
    'missing title' => '{"editorNote":null}',
    'wrong title type' => '{"title":0,"editorNote":null}',
    'wrong note type' => '{"title":"A","editorNote":false}',
    'extra field' => '{"title":"A","editorNote":null,"admin":true}',
    'title byte bound' => json_encode(['title' => str_repeat('x', 81), 'editorNote' => null], JSON_THROW_ON_ERROR),
    'note byte bound' => json_encode(['title' => 'A', 'editorNote' => str_repeat('x', 201)], JSON_THROW_ON_ERROR),
    'body byte bound' => str_repeat(' ', 1025),
];
foreach ($invalid as $name => $json) {
    try {
        DraftInput::fromJson($json);
    } catch (InvalidArgumentException $error) {
        check($error->getMessage() === 'Invalid draft input', 'Unsafe parser error');
        continue;
    }
    throw new RuntimeException('Expected rejection: ' . $name);
}

$input = DraftInput::fromJson('{"title":"","editorNote":null}');
check($input->editorNote === null, 'Explicit null must be preserved');
$article = Article::draft($input->title);
rejectsTransition(static function () use ($article): void {
    $article->publish();
});
check(!$article->isPublished() && $article->title() === '', 'Failed publication changed state');

$article->rename('0');
$article->publish();
check($article->isPublished() && $article->title() === '0', 'Zero-string title is valid');
rejectsTransition(static function () use ($article): void {
    $article->rename('Replacement');
});
check($article->title() === '0', 'Rejected rename changed the article');

$direct = Article::draft('   ');
rejectsTransition(static function () use ($direct): void {
    $direct->publish();
});
check(!$direct->isPublished(), 'Domain rule must apply without the parser');
$direct->rename('Ready');
$direct->publish();
$direct->publish();
check($direct->isPublished(), 'Publication is idempotent in this example');

$noted = DraftInput::fromJson('{"title":"Ready","editorNote":"private note"}');
check($noted->editorNote === 'private note', 'Non-null note must be preserved');
echo "input-domain: 10 invalid inputs and draft/publication/editing cases passed\n";
```

Run the following using the project's installed tools, without changing its
dependency versions solely to run this example:

```sh
composer --no-plugins --no-scripts validate --strict
composer --no-plugins --no-scripts dump-autoload --optimize --strict-psr --strict-ambiguous
php -l src/DraftInput.php
php -l src/Article.php
php -l tests/run.php
php -d zend.assertions=-1 tests/run.php
phpstan analyse --level=max --no-progress src tests
```

Use the existing analyzer configuration with the supported PHP target; no
baseline/ignore is needed for these owned files. The checked setup used PHPStan
2.2.14 level 10 targeting PHP 8.2 and executed on PHP 8.3.6.

The byte limits are illustrative wire-contract choices, not Unicode character
limits or a network request cap. `trim()` here defines blank as PHP's default
trimmed characters; a richer Unicode editorial rule needs an explicit contract.
Required-null versus omission is intentional. This example has no HTTP framework,
public serializer, storage, concurrent publication, or authorization; an adapter
must not serialize the input DTO wholesale and expose its editor note.
