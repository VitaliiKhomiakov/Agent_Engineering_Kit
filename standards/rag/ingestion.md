# RAG corpus lifecycle

Read when loading or changing a corpus; return to the [RAG entry](../rag.md).

## Build and maintain the corpus

1. Identify permitted source collections and ownership. Attach stable document IDs,
   source URI/record ID, version/content hash, access metadata and available dates.
   Treat uploaded files and fetched pages as untrusted input; constrain parser
   resources and network access according to the supported source types.
2. Parse structure before splitting. Preserve headings, table headers/units, code
   boundaries and page/section locators. Verify OCR and reading order on actual
   representative documents. An extraction failure is not an empty valid document.
3. Split along useful semantic/structural boundaries with the selected tokenizer.
   Choose chunk size and overlap from measured retrieval cases; no universal token
   count is required. Preserve parent/neighbor relationships when needed for meaning.
4. Version the parser, chunker, embedding model, dimensions and relevant settings.
   Match query/document embedding formats, prefixes, normalization and distance
   metric to that model. Equal vector dimensions do not establish model compatibility.
5. Make ingestion repeatable with stable identity and content-aware updates.
   Record partial failures. Handle deleted documents, replaced versions and access
   revocations, including cached results; do not leave superseded chunks silently
   searchable. Incomplete synchronization must not delete unseen documents as though
   a full authoritative inventory had completed.
6. For an incompatible embedding/index change, build and validate a new generation
   before switching readers. Keep a rollback path consistent with data-retention
   and deletion requirements; do not preserve revoked access through old caches.

LlamaIndex transformations/document management and Docling structure-aware chunking
are implementation options. Their presence does not implement the
application's deletion, access or publication policy automatically.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee.

[LlamaIndex ingestion pipeline](https://developers.llamaindex.ai/python/framework/module_guides/loading/ingestion_pipeline/),
[Docling chunking](https://docling-project.github.io/docling/concepts/chunking/).
