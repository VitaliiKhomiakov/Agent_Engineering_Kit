# LlamaIndex retrieval-only fixture

This [retrieval boundary](../ingestion-retrieval.md) uses `SummaryIndex` and
`NodeWithScore` to convert already-authorized fixture nodes to explicit evidence.
It preserves separate chunks from one document and rejects missing provenance.

## Fixture and reproduction

Executed on **2026-10-29**, Python **3.12.3**, `llama-index-core` **0.14.25**; strict typing checked with
mypy **2.1.0**. Save the code as `retrieval.py` in an empty temporary directory.
Dependency installation uses the package registry; execution needs no model,
API keys or remote service.

```python
from dataclasses import dataclass
import unittest

from llama_index.core import SummaryIndex
from llama_index.core.schema import (
    MetadataMode, NodeRelationship, NodeWithScore, RelatedNodeInfo, TextNode,
)


@dataclass(frozen=True)
class Evidence:
    document_id: str
    node_id: str
    revision: str
    source_uri: str
    text: str


def to_evidence(hits: list[NodeWithScore]) -> list[Evidence]:
    result: list[Evidence] = []
    seen: set[tuple[str, str, str]] = set()
    for hit in hits:
        node = hit.node
        document_id = node.ref_doc_id
        node_id = node.node_id
        revision = node.metadata.get("revision")
        source_uri = node.metadata.get("source_uri")
        if not document_id or not isinstance(revision, str) or not revision:
            raise ValueError("missing document identity or revision")
        if not node_id:
            raise ValueError("missing node identity")
        if not isinstance(source_uri, str) or not source_uri:
            raise ValueError("missing source location")
        key = (document_id, revision, node_id)
        if key not in seen:
            seen.add(key)
            result.append(Evidence(document_id, node_id, revision, source_uri,
                                   node.get_content(metadata_mode=MetadataMode.NONE)))
    return result


class RetrievalBoundaryTest(unittest.TestCase):
    def test_preserves_two_chunks_from_one_document(self) -> None:
        # Fixture corpus is already authorized. SummaryIndex returns all nodes;
        # it does not implement relevance ranking or tenant authorization.
        nodes = [TextNode(
            id_=f"policy:chunk-{number}", text=text,
            metadata={"revision": "rev-1", "source_uri": "https://example.test/policy"},
            relationships={NodeRelationship.SOURCE: RelatedNodeInfo(node_id="policy")},
        ) for number, text in enumerate(("Returns: 30 days.", "Exceptions: custom goods."))]
        retriever = SummaryIndex(nodes=nodes).as_retriever()
        hits = retriever.retrieve("What are the return rules?")
        self.assertEqual(len(hits), 2)
        evidence = to_evidence(hits + [hits[0]])
        self.assertEqual([item.node_id for item in evidence],
                         ["policy:chunk-0", "policy:chunk-1"])
        self.assertEqual({item.document_id for item in evidence}, {"policy"})
        self.assertEqual(evidence[1].text, "Exceptions: custom goods.")
        self.assertEqual(to_evidence([]), [])

    def test_refuses_evidence_without_source_identity(self) -> None:
        with self.assertRaisesRegex(ValueError, "identity"):
            to_evidence([NodeWithScore(node=TextNode(text="Unattributed text"))])

    def test_rejects_empty_node_identity_before_deduplication(self) -> None:
        hits = [NodeWithScore(node=TextNode(
            id_="", text=text,
            metadata={"revision": "rev-1", "source_uri": "https://example.test/policy"},
            relationships={NodeRelationship.SOURCE: RelatedNodeInfo(node_id="policy")},
        )) for text in ("Returns: 30 days.", "Exceptions: custom goods.")]
        with self.assertRaisesRegex(ValueError, "node identity"):
            to_evidence(hits)


if __name__ == "__main__":
    unittest.main()
```

### Checks

```sh
python3 -m venv .venv
.venv/bin/python -m pip install 'llama-index-core==0.14.25' 'mypy==2.1.0'
LANGSMITH_TRACING=false LANGCHAIN_TRACING_V2=false .venv/bin/python retrieval.py
.venv/bin/python -m mypy --strict --disallow-any-explicit --disallow-any-unimported --python-version 3.12 retrieval.py
```

These are demonstrated package pins, not a full transitive dependency lock. Retain
the resolved environment/lockfile for repeat runs and preserve the consuming
application's selected compatible versions.

## Evidence limits

`SummaryIndex` here returns every supplied node without semantic ranking. No
embedding or LLM provider is selected. The source URI is a fixture and is never
fetched. Tests cover identity/conversion only, not source ingestion, vector-store
upserts/deletes, freshness, backend ACLs, retrieval quality or answer synthesis.
Do not copy this all-nodes retriever as a production ranking strategy by default.
