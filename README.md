# Agent_Engineering_Kit

A reusable library of engineering instructions for AI coding agents in Codex,
Claude Code, and Cursor. Select the rules that fit your project; the agent adapts
them to its languages, frameworks and existing local requirements.

**Start with the integration wizard in your AI chat.** It helps you choose a
project, inspect its stack, review the proposed changes and apply the agreed scope.
After integration, work through normal development requests in that project.

## Adopt in your project

1. Clone or download this library to a location your coding agent can read.
2. Open the target project in your AI coding client. For a new project, open the
   intended parent workspace. Use paths accessible in the agent's environment,
   including when it runs remotely or in a container.
3. Replace `<framework-path>` below with the library's actual path and send:

> Read `<framework-path>/templates/skills/aek-integrate-project/SKILL.md` and open
> the Agent_Engineering_Kit integration wizard in this chat. Show the menu and ask
> only for missing information.

If this library is the current workspace, the source-relative path is
`templates/skills/aek-integrate-project/SKILL.md`. You can also include the target
path, client and desired operation in the first request to skip answered questions.

The wizard offers four actions, using your conversation language:

| Action | What happens |
| --- | --- |
| **1. Existing project** | Inspect technologies and current instructions, then prepare the applicable profiles and changes |
| **2. New project** | Ask about intended languages, frameworks and goals, then prepare instructions for that selection |
| **3. Update an adoption** | Reuse recorded choices, compare the selected source with installed instructions, and preserve local edits |
| **4. Check an adoption** | Inspect the installed instructions and report issues without changing project files |

Use the client's choice controls where available, or reply with a number or your
own words. You can correct a choice, go back, pause or cancel. This is a guided
conversation; it does not launch a separate terminal application or automatically
register a slash command.

For an existing project, the agent first examines relevant manifests, configuration
and source evidence. It shows which technologies were observed, which are uncertain
and which you requested for future work. In a monorepo, evidence stays associated
with each application. You can correct the proposed profiles; a sample file or
transitive dependency alone does not choose a framework.

The agent reports progress as it inspects, selects profiles, prepares changes,
applies authorized edits and checks the result. The preview includes affected
paths, content changes, conflict decisions and the model-selection outcome.
Existing model choices are reused; unresolved choices are made explicit.

Opening the menu or selecting a project type begins preparation and leaves the
target untouched. When the preview is ready, you can request application:

> Apply the prepared Agent_Engineering_Kit import to `<project-path>` for `<client>`
> within the reviewed scope. Preserve unrelated changes and existing model choices,
> and follow the agreed checkpoints.

If your original request already authorizes the concrete import/update scope, the
agent reuses that permission. It asks again only for a missing material decision
or an action outside that scope. Preparation-only and check-only requests remain
read-only. An interrupted operation reports completed and remaining changes.

The final report identifies changed files, checks, remaining decisions and where
the adoption was recorded. File validation, saved model settings and observed
client activation are reported separately. Copying instructions does not prove
that the client has loaded or followed them.

## Work after integration

Open the project normally and describe the task to your coding agent. Its adopted
entry routes it to the relevant instructions; you do not need to reopen the wizard
before every change. For example:

| Goal | Example request |
| --- | --- |
| Plan a feature | "Using this project's instructions, propose a design for `<feature>` and identify decisions that need my input." |
| Implement a task | "Implement `<task>` within the agreed scope. Follow the project rules and run the relevant checks." |
| Review changes | "Review the current changes for correctness, unnecessary complexity and conflicts with project instructions." |
| Continue work | "Continue the task recorded at `<task-path>`, reusing completed work and valid checks." |
| Deliver through Git | "Commit these reviewed changes and push to `<remote>/<branch>`." |

These are ordinary requests, not registered commands. Review and confirm the
checkpoints required by your project's work mode. Importing instructions itself
does not authorize application-code changes, commits, pushes or deployments.

For an update or check, invoke the same source skill and name the operation directly:

> Read `<framework-path>/templates/skills/aek-integrate-project/SKILL.md`. Check the
> existing AEK adoption in `<project-path>` without changing files.

> Read `<framework-path>/templates/skills/aek-integrate-project/SKILL.md`. Prepare an
> update of the AEK adoption in `<project-path>` from this source. Preserve local
> edits and current selections; show the proposed differences before applying them.

Keep the library source accessible for future updates. The wizard reuses adoption
records and supplied context instead of repeating the initial questionnaire.

## Technologies

- **Python:** FastAPI, Pydantic, SQLAlchemy, Psycopg.
- **PHP:** Symfony, Doctrine.
- **Go:** Gin; Eino and LangChainGo where selected.
- **JavaScript / TypeScript:** Node.js, NestJS, React, Next.js, Angular, NgRx, TypeORM.
- **Database and containers:** PostgreSQL, Docker.
- **RAG and LLM applications:** language-neutral [RAG](standards/rag.md) and
  [tool/workflow rules](standards/llm-tools.md); optional [LlamaIndex](standards/llamaindex.md),
  [Eino for Go](standards/eino.md), [LangChain/LangChainGo](standards/langchain.md),
  [LangGraph](standards/langgraph.md) and [Langfuse](standards/langfuse.md)
  integration topics and bounded executable examples.
- **Game development:** Unreal Engine, including C++ and Blueprints; [Godot](standards/godot.md),
  with GDScript and conditional C#/GDExtension guidance.

Select only applicable profiles from [the catalog](standards/catalog.toml).
The language used by an application remains independent of how the wizard runs.

## How the framework is used

No package or global skill installation is required. Integration and model-setup
skills are read from the library source by default. Persistent native skills are
an explicit choice with client-specific discovery checks; opening the wizard
does not install one. Optional design/review task skills are selected separately.

- [Integration skill](templates/skills/aek-integrate-project/SKILL.md): the menu and conversation contract.
- [MIGRATION.md](MIGRATION.md): preparation, adoption, checks, updates and recovery.
- [Catalog guide](standards/catalog.md): profile selection and conditional reading.
- [ARCHITECTURE.md](ARCHITECTURE.md): how this instruction library is organized.
