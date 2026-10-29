# RAG retrieval and context

Read when selecting evidence for an answer; return to the [RAG entry](../rag.md).
Use the declared [source and application contract](../llm/architecture.md#establish-the-project-contract)
and pass evidence to the [answer checks](../llm/answers.md).

## Retrieve evidence for the actual question

- Preserve the original question. A rewritten query resolves conversational context
  and improves retrieval; it must not invent constraints or silently change intent.
  Keep material entities, identifiers, time ranges and requested source scope.
- Choose exact lookup/structured queries for current record values and aggregates;
  lexical search for identifiers or exact terms; semantic search for meaning.
  Compare a hybrid route where both matter. RAG does not require a vector database.
- Enforce authorization in the retrieval service/store before candidate contents
  reach a model, external reranker or client. Apply it consistently to every hybrid
  branch, source fetch, pagination path, cache and conversation resume. Do not rely
  on a model to discard unauthorized snippets it has already received.
- Distinguish database filter enforcement from ANN candidate generation. A valid
  filter can still leave too few candidates after an approximate scan; assess
  recall and index/query settings rather than removing the access filter.
- Deduplicate repeated instances of the same evidence unit across retrieval branches.
  Identify that unit by source and version plus chunk or record identity, or by an
  equivalent stable locator. Preserve distinct relevant passages from the same
  document and separate sources that supply independent evidence. Treat document-level
  diversity limits as a separate selection policy. Use a defined rank-fusion strategy;
  do not add unrelated similarity scores as if they shared a scale.
- Rerank a bounded candidate set when evaluation justifies its latency/cost.
  Reranking cannot recover an absent candidate. Select models appropriate to the
  corpus language and domain; scores are not probabilities of answer correctness. Use parent or neighboring content when a chunk lacks necessary context.
- Build a context budget that reserves space for instructions, the question,
  relevant conversation and the answer. Retain evidence locators and important
  qualifications when compressing. A generated summary or contextual prefix must
  not masquerade as a verbatim source passage.
- Define evidence sufficiency by the answer's required claims, source authority,
  freshness and coverage. Do not answer solely because a top-k search returned k hits.
  Preserve conflicts and limitations; additional searching needs a specific gap.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee.

[LlamaIndex querying](https://developers.llamaindex.ai/python/framework/understanding/rag/querying/),
[LlamaIndex documents and nodes](https://developers.llamaindex.ai/python/framework/module_guides/loading/documents_and_nodes/),
[pgvector](https://github.com/pgvector/pgvector),
[Qdrant hybrid queries](https://qdrant.tech/documentation/search/hybrid-queries/),
[Sentence Transformers retrieve and rerank](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html),
[Contextual retrieval](https://www.anthropic.com/research/contextual-retrieval),
[Lost in the Middle](https://aclanthology.org/2024.tacl-1.9/).
