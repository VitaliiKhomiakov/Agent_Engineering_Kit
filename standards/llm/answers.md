# Evidence, answer checks and delivery

Apply when a selected RAG or tool workflow produces an answer. The application's
source-authority, output and publication contract determines the applicable checks;
verification need not be a separate model call or workflow node.

## Verification and delivery

Check deterministic constraints first: schema, permitted source IDs, resolvable
locators, access scope, version/date applicability, arithmetic and required fields.
Then check material claims against the cited passages/records. Citation existence
and factual entailment are separate criteria. Do not fabricate URLs, page numbers,
quotations or reference IDs; final citations come from the evidence registry.

Use an LLM judge for semantic checks where it adds value, with explicit criteria
and only the necessary evidence. Treat its verdict as fallible; formatting success
or an approving second model does not prove truth. Exact record values and access
checks remain deterministic. Choose checks proportionate to the application's
failure cost rather than requiring an extra model call for every response.

On conflict, apply the source-authority and effective-date policy or disclose the
unresolved conflict. Repair only the identified failure. If a required fact remains
unsupported, remove or qualify the claim, return the supported portion, or abstain.
An infrastructure failure must not be concealed as a successful verified answer.

If the product promises checking before delivery, buffer answer content until its
gate passes; stream progress separately. A product choosing provisional answer
streaming must explicitly define that weaker contract and correction behavior.
Internal verification findings, credentials and private reasoning are not user
output. Show the answer, relevant sources, freshness/uncertainty when material,
and a useful next step when clarification or missing access prevents completion.

The transport owns final formatting and escaping. Sending the answer in the current
chat is part of answering; sending it to a different person, channel or external
system is a separate action with its own authorization and duplicate-send handling.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee.

[CitationQueryEngine](https://developers.llamaindex.ai/python/examples/query_engine/citation_query_engine/),
[LangChain structured output](https://docs.langchain.com/oss/python/langchain/structured-output),
[Demystifying agent evaluations](https://www.anthropic.com/research/demystifying-evals-for-ai-agents).
