# LLM system evaluation and observability

Read when evaluating or observing the application's actual features. Keep online
checks separate from change validation; use [proportionate verification](../verification.md)
for engineering work. Selecting this topic adds no evaluation service or framework.

## Evaluation and observability

Separate **online response checks**, which decide whether this response may be
delivered, from **offline evaluation**, which compares system changes over a
representative dataset. Use the shared verification policy; this guidance does not require running a
full evaluation suite after each edit.

For offline quality evaluation, build or reuse a held-out dataset from permitted
real questions and reviewed synthetic cases. Include relevant languages, ambiguity,
exact identifiers, current records, multi-source questions, conflicting/stale
documents and unanswerable requests.
Record expected facts, acceptable sources, access scope and allowed outcomes.
Keep train/tuning cases separate from acceptance cases. Version corpus, pipeline,
prompt, model and grader settings with each experiment.

| Layer | Measure or inspect | Failure it distinguishes |
| --- | --- | --- |
| Intent/clarification | Route correctness and unnecessary/missed clarification | Wrong task or unnecessary question before retrieval |
| Retrieval | Recall@k, ranking quality and required-evidence coverage where labels exist | Relevant evidence never reaches the answer stage |
| Answer | Correctness, supported claims, citation correctness and completeness | Fluent answer that misses or contradicts evidence |
| Abstention | Unsupported-answer rate and unnecessary abstention | Guessing when evidence is absent, or refusing answerable requests |
| Tools/actions | Valid selection/arguments, authorization and actual effect | Successful-looking text despite an incorrect/duplicate operation |
| Operations | Latency percentiles, cost, token/tool counts, errors and freshness | Quality gain that violates the product's operational constraints |

Calibrate LLM-based metrics against reviewed human labels and audit disagreements.
Track grader changes; repeated trials estimate variability where material. Avoid
an unqualified universal score threshold or requiring one exact tool sequence when
several correct paths exist. Enforce required partial ordering and final outcomes.

Trace the stages actually present in the chosen flow, such as retrieval, source
fetch, model/tool calls, verification and delivery, under a common correlation ID.
Record necessary source/index/model/prompt versions, stage timings, retries,
truncation and terminal status. Keep telemetry outages
visible without pretending they prove an application error or silently waiving a
required audit contract. Use failure traces to add focused regression cases.

## Acceptance scenarios for an implementation

| Scenario | Expected behavior |
| --- | --- |
| Straightforward answerable documentation question | Returns supported answer and valid locators without unnecessary loops |
| Current database fact differs from an old document | Applies the declared authoritative source and timestamp policy |
| Important entity/time range is missing | Asks a focused question and resumes the correct owned request |
| Query has no supporting evidence | Returns insufficient evidence or only the supported portion |
| One source times out while another succeeds | Reports partial coverage or fails according to the required-source contract |
| Retrieved document instructs the model to call an unrelated tool | Treats it as data; permissions and route remain unchanged |
| Another tenant's matching document exists | It never reaches unauthorized context, caches, reranker or output |
| Access is revoked after checkpoint/cache creation | Revalidation prevents stale evidence from being disclosed |
| Search result has a plausible URL but no supporting passage | Does not cite it as verified support |
| Exact numeric answer or aggregate is required | Computes from typed records with correct units and scope |
| Concurrent hybrid searches return duplicates | Produces stable deduplicated evidence without score-scale confusion |
| Tool returns malformed/truncated output | Rejects or marks incomplete; does not claim complete evidence |
| Graph pauses after a non-idempotent downstream effect | Resume/retry reconciles the effect instead of duplicating it |
| Delivery times out after the downstream system accepted it | Uses the receipt/idempotency contract; no blind resend |
| Retry, token or elapsed-time budget is exhausted | Reaches a bounded terminal outcome |
| User cancels while a tool is running | Propagates cancellation and suppresses later actions/delivery |
| Tracing includes sensitive payload through another exporter | Selected export/redaction policy is exercised and verified |
| Prompt/model/index revision changes | Evaluates relevant held-out cases; retains valid unrelated evidence |

These are acceptance cases to adapt to the application's actual features, not a
requirement to build every feature or introduce a new testing framework.

## Sources and compatibility

Documentation reviewed on **2026-10-29**. Use the application's actual versions;
this source review is not a runtime test or interoperability guarantee.

[LlamaIndex evaluation](https://developers.llamaindex.ai/python/framework/module_guides/evaluating/),
[Langfuse SDK experiments](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk),
[Demystifying agent evaluations](https://www.anthropic.com/research/demystifying-evals-for-ai-agents),
[Ragas metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/).
