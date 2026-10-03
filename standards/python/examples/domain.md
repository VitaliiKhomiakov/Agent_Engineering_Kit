# Python example: an incomplete draft and a protected transition

Read when the distinction between parsed input and state invariants is unclear.
Return to [types and contracts](../typing-contracts.md). These are illustrative
module names, not a required application layout. Requires Python 3.11+ and only
the standard library; no validation framework is selected by this example.

The boundary accepts an empty title because saving an incomplete draft is valid.
Its 200-character input limit is this transport's contract. Publication has a
different rule: the document must have a nonblank title and still be a draft.
That rule also applies to typed CLI/worker calls that never use the input parser.

Save as `title_input.py` (a presentation contract):

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class TitleInput:
    title: str


def parse_title(raw: object) -> TitleInput:
    if not isinstance(raw, str):
        raise ValueError("title must be text")
    if len(raw) > 200:
        raise ValueError("title exceeds the input limit")
    return TitleInput(title=raw)
```

Save as `document.py` (domain behavior, without a transport import):

```python
class DocumentError(ValueError):
    pass


class Document:
    def __init__(self, title: str = "") -> None:
        self._title: str = title
        self._published: bool = False

    @property
    def title(self) -> str:
        return self._title

    @property
    def published(self) -> bool:
        return self._published

    def rename(self, title: str) -> None:
        if self._published:
            raise DocumentError("a published document cannot be renamed")
        self._title = title

    def publish(self) -> None:
        if self._published:
            raise DocumentError("the document is already published")
        if not self._title.strip():
            raise DocumentError("publication requires a title")
        self._published = True
```

The application passes `parsed.title` into a domain operation; it need not pass
the presentation DTO or duplicate it just to cross a folder boundary. Normal
internal calls rely on established types. A dataclass annotation alone would not
validate `raw`; `parse_title` does so explicitly. In a real API use its existing
validator for a larger input schema.

Save as `test_document.py` beside the two modules:

```python
import unittest

from document import Document, DocumentError
from title_input import parse_title


class DocumentTests(unittest.TestCase):
    def test_parser_accepts_incomplete_draft_input(self) -> None:
        self.assertEqual(parse_title("").title, "")
        self.assertEqual(parse_title("x" * 200).title, "x" * 200)

    def test_parser_rejects_wrong_types_and_excess_length(self) -> None:
        invalid_values: tuple[object, ...] = (None, 23, False, b"title", "x" * 201)
        for raw in invalid_values:
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                parse_title(raw)

    def test_direct_domain_call_rejects_blank_publication(self) -> None:
        for title in ("", " \t\n"):
            document = Document(title)
            with self.subTest(title=title), self.assertRaises(DocumentError):
                document.publish()
            self.assertEqual(document.title, title)
            self.assertFalse(document.published)

    def test_draft_can_be_completed_then_published(self) -> None:
        document = Document()
        document.rename(parse_title("Release notes").title)
        document.publish()
        self.assertEqual(document.title, "Release notes")
        self.assertTrue(document.published)

    def test_published_state_rejects_changes_without_mutation(self) -> None:
        document = Document("Release notes")
        document.publish()
        with self.assertRaises(DocumentError):
            document.rename("Changed")
        with self.assertRaises(DocumentError):
            document.publish()
        self.assertEqual(document.title, "Release notes")
        self.assertTrue(document.published)
```

Run `python -m unittest -v test_document` in that directory. For mypy use the
project's pinned analyzer, targeting its supported Python version with `--strict
--disallow-any-explicit --disallow-any-unimported`; the example modules also pass
`--disallow-any-expr`. Check both the modules and tests, not just imports.

The entity is an in-memory owner, not a transaction, authorization, persistence,
or concurrent-update solution. Underscore attributes are a caller convention;
Python code can bypass it. A real persistence operation must enforce its database
and concurrency contract separately. No factory, repository, inheritance tree,
or HTTP framework is needed to demonstrate this invariant.

Execution evidence and interpreter/checker versions are recorded in the
[practice plan](../../../docs/plans/2026-09-21-engineering-practices.md).
