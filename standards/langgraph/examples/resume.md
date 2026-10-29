# LangGraph interrupt/resume fixture

This [recovery boundary](../recovery-streaming.md) exercises the real Python
`StateGraph`, `interrupt` and `Command` APIs. It proves that a resumed node starts
again, handles approval/rejection and rejects an invalid decision value.

## Fixture and reproduction

Executed on **2026-10-29**, Python **3.12.3**, `langgraph` **1.2.18**, `langgraph-checkpoint` **4.3.1**, `langchain-core` **1.7.1**; strict typing checked with
mypy **2.1.0**. Save the code as `resume.py` in an empty temporary directory.
Dependency installation uses the package registry; execution needs no model,
API keys or remote service.

```python
from typing import NotRequired, TypedDict
import unittest

from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


class State(TypedDict):
    request_id: str
    approved: NotRequired[bool]
    outcome: NotRequired[str]


class ResumeBoundaryTest(unittest.TestCase):
    def test_pause_resume_and_node_restart(self) -> None:
        entered: list[str] = []  # Test probe, not application state or an effect.

        def review(state: State) -> dict[str, bool]:
            entered.append(state["request_id"])
            decision = interrupt({"request_id": state["request_id"]})
            if not isinstance(decision, bool):
                raise ValueError("resume decision must be boolean")
            return {"approved": decision}

        def finish(state: State) -> dict[str, str]:
            # No external effect. A real effect needs the shared execution policy.
            return {"outcome": "approved" if state["approved"] else "rejected"}

        builder = StateGraph(State)
        builder.add_node("review", review)
        builder.add_node("finish", finish)
        builder.add_edge(START, "review")
        builder.add_edge("review", "finish")
        builder.add_edge("finish", END)
        saver = InMemorySaver()
        graph = builder.compile(checkpointer=saver)

        for request_id, approved in (("job-1", True), ("job-2", False)):
            # An authenticated server must own this mapping in the application.
            config: RunnableConfig = {"configurable": {"thread_id": request_id}}
            paused = graph.invoke({"request_id": request_id}, config)
            self.assertIn("__interrupt__", paused)
            self.assertNotIn("outcome", paused)
            completed = graph.invoke(Command(resume=approved), config)
            self.assertEqual(completed["outcome"], "approved" if approved else "rejected")
            self.assertEqual(entered.count(request_id), 2)

        config = {"configurable": {"thread_id": "bad-decision"}}
        graph.invoke({"request_id": "bad-decision"}, config)
        with self.assertRaisesRegex(ValueError, "boolean"):
            graph.invoke(Command(resume="yes"), config)

        # A different saver has no durable state; this is not a process restart test.
        empty_graph = builder.compile(checkpointer=InMemorySaver())
        self.assertFalse(empty_graph.get_state({"configurable": {"thread_id": "job-1"}}).values)


if __name__ == "__main__":
    unittest.main()
```

### Checks

```sh
python3 -m venv .venv
.venv/bin/python -m pip install 'langgraph==1.2.18' 'langgraph-checkpoint==4.3.1' 'langchain-core==1.7.1' 'mypy==2.1.0'
LANGSMITH_TRACING=false LANGCHAIN_TRACING_V2=false .venv/bin/python resume.py
.venv/bin/python -m mypy --strict --disallow-any-explicit --disallow-any-unimported --python-version 3.12 resume.py
```

These are demonstrated package pins, not a full transitive dependency lock. Retain
the resolved environment/lockfile for repeat runs and preserve the consuming
application's selected compatible versions.

## Evidence limits

The list mutation before `interrupt` is a test probe that makes node restart
visible; do not place an irreversible application effect there. `InMemorySaver`
keeps data only within the process. Constructing a fresh saver checks that it has
no state; it is not a crash/restart durability test. The fixture does not authenticate
users, authorize thread access, execute external effects or test streaming/replay
around a downstream service. It needs `langchain-core` as a runtime dependency,
but does not select the LangChain agent framework.
