# LlamaIndex ingestion and retrieval

Read for source loading, updates or retrieval. [Corpus lifecycle](../rag/ingestion.md)
and [retrieval](../rag/retrieval.md) own the common policies; this topic maps them
to Python LlamaIndex. LlamaIndex.TS needs its own package/connector check.

## Documents, nodes and stores

Give source documents stable IDs. Distinguish `Document` identity from individual
`TextNode`/node identity, source relationship, revision and location. Preserve that
mapping across splitting and reindexing. De-duplicate identical evidence units,
not all nodes that share a source document. An access or metadata change must
reach the serving index even when the source text is unchanged.

Configure ingestion transformations explicitly. Chunking, embeddings and any
model-based extraction are separate operations with separate costs and versions.
An ingestion cache is not the serving index or a guarantee that deletions and ACL
changes propagated. Record the transformation/embedding revision used to build
an index and verify the actual integration's refresh behavior.

When using a docstore-backed Python `IngestionPipeline`, select the intended
`DocstoreStrategy` rather than relying on a name or default:

| Strategy | Intended use and limitation |
| --- | --- |
| `DUPLICATES_ONLY` | Suppress already-seen content hashes; not a full source synchronization protocol |
| `UPSERTS` | Track document identity/hash and reprocess changed inputs with the compatible docstore/vector-store path |
| `UPSERTS_AND_DELETE` | Also remove stored source IDs absent from this input set; use only when that set is the complete authoritative snapshot for the isolated store scope |

Do not apply absence-based deletion to an incremental batch or one tenant in a
shared docstore. In the inspected Python version, a pipeline without a vector
store falls back to duplicate handling for upsert strategies. Verify writes and
deletes against the actual vector adapter; a docstore operation alone does not
prove old vectors disappeared. Partial failures between stores need an application
reconciliation path, not an assumption of atomic cross-store updates.

## Retrieval output

Use `as_retriever()`/`retrieve()` when the application owns answer composition.
Keep `NodeWithScore` provenance through postprocessors and reranking. A score is
backend-specific and may be absent; do not treat it as universal confidence.
Configure the actual embedding model and query/index compatibility instead of
accidentally resolving a paid default provider. Apply access scope at the backend
before evidence reaches the model.

The [retrieval-only fixture](examples/retrieval.md) uses a `SummaryIndex` that
returns all supplied nodes. It verifies evidence conversion and chunk identity;
it does not demonstrate semantic ranking, ACL enforcement or vector updates.

## Contract references

[Documents/nodes](https://developers.llamaindex.ai/python/framework/module_guides/loading/documents_and_nodes/),
[ingestion pipeline](https://developers.llamaindex.ai/python/framework/module_guides/loading/ingestion_pipeline/),
[document management](https://developers.llamaindex.ai/python/examples/ingestion/document_management_pipeline/),
[pipeline source, v0.14.25](https://github.com/run-llama/llama_index/blob/v0.14.25/llama-index-core/llama_index/core/ingestion/pipeline.py).
