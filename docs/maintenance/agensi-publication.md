# Maintaining the Agensi publication

Use this document when updating the existing
[Agent Engineering Kit listing](https://www.agensi.io/skills/agent-engineering-kit).
It holds proposed listing copy and publication-specific checks; engineering rules
remain in their existing owners. The [canonical task](../plans/2026-11-02-agensi-publication.md)
records observations, progress and authorization.

Status of the copy below: prepared on 2026-11-02, not applied to Agensi.
It describes the existing hosted-reference approach and does not introduce a
new package, license, installation mechanism or compatibility guarantee.

## Positioning and distribution

Keep one free listing with a task-routing entry and references loaded on demand.
AEK is a source library of engineering instructions; the hosted skill applies
relevant guidance to a user's task. Persistent adoption follows the independent
source library's [SETUP](../../SETUP.md) and [MIGRATION](../../MIGRATION.md).

This fits Agensi's [hosted loading contract](https://www.agensi.io/docs/how-agents-load-skills):
agents retrieve text references as needed and must not install the hosted skill.
Project-specific outputs can be produced from templates, as explained in the
[creator FAQ](https://www.agensi.io/docs/creator-faq). Do not represent the hosted
reference snapshot as an installed or automatically synchronized AEK bundle.

A pack with separate design, review and adoption entries is a possible later
change if actual use demonstrates routing problems. Forty-four catalog profiles
are not forty-four independently usable skills. Native source skill templates
are inactive preparation inputs and must not accidentally become pack entries.

## Proposed listing fields

Keep the existing name, slug, free price and approved logo.

**Name:** Agent Engineering Kit

**Summary:**

Help your coding agent design features, review code and choose project rules using stack-specific engineering guidance. Free reference edition for Codex, Claude Code and Cursor; persistent project setup uses the separate source repository.

**Description:**

### Engineering guidance for the project you actually have

Agent Engineering Kit (AEK) helps an AI coding agent apply consistent architecture,
implementation and review practices to your stack. Ask for a focused result:

- A feature design with clear responsibilities, contracts and acceptance criteria.
- A code review with prioritized findings, concrete failure scenarios and evidence.
- Guidance during authorized implementation, using the relevant technology rules.
- A recommendation of project rules, followed by a reviewable adoption proposal
  when you want persistent integration.

Provide the relevant code or project context and your intended outcome. The agent
selects the applicable references and explains missing context and checks it has
not run. Editing and execution depend on the tools and permissions you provide.

### Two ways to use AEK

**Use through Agensi:** connect your agent to Agensi and ask it to use Agent
Engineering Kit on a specific task. This edition supplies a dated reference
snapshot loaded on demand. It does not install project instructions.

**Integrate into a project:** obtain the
[source repository](https://github.com/VitaliiKhomiakov/Agent_Engineering_Kit)
separately and ask your agent to read its SETUP.md. The wizard inspects or asks
about your stack, proposes applicable instructions and follows MIGRATION.md for
authorized application and updates.

### Coverage

The 2026-11-02 catalog has 44 profiles, including shared workflows and compatibility
entries. Coverage includes Python, JavaScript/TypeScript, PHP, Go, PostgreSQL,
Docker, RAG and LLM applications, Unreal Engine and Godot. Framework guidance
includes React, Next.js, Angular, FastAPI, Symfony, Gin and others listed in the
source catalog. Select only what applies to your project.

### Requirements and limits

Use an agent connected to Agensi that can read text references, plus the relevant
project context or supplied code. No language runtime or Unreal MCP is required
for advice on supplied text. Local edits, tests and specialized integrations need
the tools for the specific task.

AEK targets Codex, Claude Code and Cursor workflows. Other MCP-capable agents may
read the references; native instruction loading and configuration need separate
verification. Superpowers is a separate plugin and is not included. Examples
retain their version conditions. AEK does not upgrade dependencies automatically
or guarantee agent behavior.

Hosted reference snapshot: 2026-11-02. Check the source repository for current
contents; an existing project adoption is updated separately.

## Structured metadata corrections

These are editor actions, not additional text to paste into the description.
The [submission guide](https://www.agensi.io/docs/submit-on-the-website) says detected
permissions and requirements should be reviewed by the creator.

| Field | Proposed value or action |
| --- | --- |
| Categories | Keep Prompt & Skill Engineering primary, Code Quality & Review and Agents & Orchestration secondary |
| Tags | Keep focused terms for engineering standards, architecture, code review, agent instructions, Codex, Claude Code and Cursor |
| Required capabilities | Agensi connection; agent able to read packaged text; relevant project context or supplied code |
| Conditional capabilities | Local read/write/terminal tools for authorized project work; network for requested research or source acquisition |
| Detected requirements | Remove Python, Git, Node.js, Editor MCP, Tooling MCP, Unreal Engine MCP and Unreal MCP from unconditional requirements |
| Source checker | Python 3.11+ only when running AEK's source-maintenance checkers; this is not a requirement for all users |
| Persistent adoption | Independently obtained AEK source; follow SETUP/MIGRATION |
| Documentation URL | Keep the source repository URL, whose README now explains both entry paths |
| Compatibility | State the three intended clients in the note; select native compatibility badges only to the extent verified in the editor and actual use |
| FAQ | Preserve the existing distinctions about installation, conditional execution and separately installed Superpowers |

Do not remove real task-specific requirements from source examples to silence
automatic detection. If the editor cannot correct a detected requirement, record
the limitation and keep its conditional nature explicit; do not claim it fixed.

## Demo and next release evidence

The current React + TypeScript example is explicitly a supplied-context
recommendation, which is appropriate. Keep that boundary. The platform adds labels
such as "installed" and "Compiled"; those do not establish execution or installation.
Before replacing the demo with a claimed real run, capture an actual request and
full result from the live skill, with the available tools and actions stated.

For the next package update, preserve the entry, listing fields and packaging
recipe in versioned source, with a source commit, package version, manifest and
checksums. The previous temporary build is historical evidence, not a reproducible
release input. Do not hand-edit a generated reference copy as a second rule owner.

Verify against the current [packaging contract](https://www.agensi.io/docs/packaging):
one intended SKILL.md for a single skill; at most 200 supporting text files and
6 million served characters; ZIP within the website's 50 MB limit. Check actual
source coverage, original-path resolution in grouped documents, conditional routes
and exclusion of source-maintenance AGENTS, installed plugins and irrelevant history.

The next live acceptance run should cover these distinct cases:

| Request | Evidence to capture |
| --- | --- |
| Review supplied code without files or shell | Useful findings, no invented inspection or checks, no runtime/MCP prerequisite unrelated to the code |
| Recommend browser-only React + TypeScript profiles | Relevant closure; no inferred backend, database or automatic installation |
| Prepare persistent adoption | Explicit independent source route; reviewable proposal; no installation of hosted reference files |
| Work on a version-specific stack | Applicable reference files load; source/version limits remain visible |

Inspect the actual Creator Studio scan findings before interpreting the public
badge. Preserve the reason and affected file for each real finding; investigate
false positives without hiding examples or weakening engineering rules.

Update the existing listing through its
[editor](https://www.agensi.io/dashboard/submit/6965a1f9-5be8-4d57-bea7-bab91c091609).
Agensi documents that [text edits go live immediately](https://www.agensi.io/docs/updates),
while a replacement ZIP receives a new review and the current version remains live.
Verify the saved public fields and the separately served package after changes.
