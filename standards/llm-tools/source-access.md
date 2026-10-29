# Tool source access

Read for database, web or enterprise adapters; return to the [tool entry](../llm-tools.md).
Use the [trusted input/output contract](contracts.md) and [execution limits](execution.md).

For databases, prefer existing typed domain queries with parameterized values and
restricted result columns. If natural-language-to-SQL is an explicit requirement,
limit schemas/views and database privileges, enforce read-only execution where
applicable, bound time/rows/cost, and validate the permitted query structure.
An LLM query checker or a string beginning with `SELECT` is not an access-control
boundary. Preserve units, currencies, time zones and aggregation semantics in
results; deterministic computation owns exact arithmetic.

For web retrieval, apply confidentiality policy before transmitting a query.
Keep public discovery separate from fetching/reading evidence; a search snippet
or provider-generated answer is not automatic support for the final claim.
Use controlled fetch adapters with redirect, destination, size and timeout limits
appropriate to SSRF and parser risks. A domain supplied by the model cannot loosen
the server's permitted network scope. Keep retrieval/publication dates and canonical
source URLs when available.

For enterprise connectors, preserve source-level access checks on both search and
fetch. Revalidate after long pauses or permission changes; an old evidence handle
or cache hit does not grant continuing access. Partition caches by effective access
scope and relevant source/query/model versions. Apply the same restrictions to
summaries, memory, traces and external reranking services.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee.

[LangChain SQL agent](https://docs.langchain.com/oss/python/langchain/sql-agent),
[Tavily search API](https://docs.tavily.com/documentation/api-reference/endpoint/search),
[Exa search API](https://exa.ai/docs/reference/search),
[MCP security guidance](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices),
[OWASP prompt injection guidance](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html).
