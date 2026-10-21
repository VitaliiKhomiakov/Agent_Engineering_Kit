# Godot tooling and MCP operations

Read for tool selection or actual editor/provider work, not merely because the
profile is installed. Keep existing compatible tools. Tool adoption follows shared
[verification](../verification.md) and the source framework's migration procedure,
resolved through adoption provenance; this topic grants no installation permission.

## Built-in workflow

Use the project's pinned engine editor, debugger, remote scene inspection, profiler
and CLI as the baseline. Direct file editing and engine commands can be sufficient
without MCP. If VS Code is the selected IDE,
[Godot Tools](https://github.com/godotengine/godot-vscode-plugin) is a GDScript
LSP/debugger option; C# requires its appropriate tooling. LSP/DAP are not MCP.
Do not change the user's editor or application languages to match a tool.

## Formatting and tests

| Need | Selection guidance |
| --- | --- |
| Mechanical GDScript formatting/lint | Evaluate a pinned [gdtoolkit](https://github.com/Scony/godot-gdscript-toolkit) (`gdformat`/`gdlint`) against actual syntax/style before adoption |
| New GDScript test runner requirement | First evaluate [GUT](https://github.com/bitwes/Gut) and its engine-version matrix; keep a suitable existing runner |
| Existing/appropriate scene-testing workflow | [GdUnit4](https://github.com/godot-gdunit-labs/gdUnit4) is an alternative; qualify the published release rather than assuming development docs match it |
| C# tests | A compatible [GdUnit4Net](https://github.com/godot-gdunit-labs/gdUnit4Net) combination for engine-bound behavior, or ordinary .NET tests for independent logic |

Do not install two overlapping runners merely to cover the same behavior. Verify
test discovery and a failing test's automation exit when establishing the runner;
zero discovered intended tests are not behavior evidence. Pin actual published
versions and preserve working configuration. A provider's private test facility
does not automatically replace the project's tests.

An external formatter/linter's independent parser can lag the selected Godot syntax.
Check relevant constructs, conflicts and useful diagnostics before making it a gate;
enable a concrete mechanical check, not an arbitrary complexity/line threshold.
It cannot decide whether semantic groups or responsibilities are appropriate.
[GDScript style](gdscript.md) owns that judgment and [verification](verification.md)
routes its evidence. A tool's Python/Node implementation does not select those
application profiles or authorize their installation.

## Selecting an MCP provider

Choose for a concrete capability gap: process control, live unsaved scene editing,
runtime inspection or rendered/input testing. A launch/log tool does not imply live
editor mutation, reliable save/undo or gameplay control. Record the matching server,
add-on, engine and client versions and the configuration owner. Validate the chosen
release's actual tool schemas and error/recovery contract.

The initial candidate for a new live-editor pilot from AEK's **2026-10-22** research
is third-party [Godot AI](https://github.com/hi-godot/godot-ai), subject to its actual
engine/release constraints. This is an evaluation starting point, not a mandatory
dependency or runtime qualification. Preserve another provider that already meets
the need. Detailed alternatives/version evidence remain in source research
`docs/research/2026-10-22-godot-engineering-and-mcp.md`; the operating rules here do
not depend on that optional archive or on personal skill paths.

Before adoption, inspect dependency and client/add-on configuration changes,
authentication, exposed ports, telemetry and external data/image routing. Prefer
project/local scope and authenticated loopback connections; disable optional usage
telemetry by default where supported. A different arrangement needs an explicit
project decision. Preserve global/unrelated client entries and local customizations;
do not use a configure-all or overwrite operation without that scope. Development
add-on exclusion needs [export evidence](assets-export.md#export-and-editor-execution).

## Editor and MCP operations

1. Establish the intended project/session, actual engine, relevant scene and dirty
   state before mutation. Preserve unsaved user work and coordinate file/editor
   writers. Recheck identity after reconnect/project switch or another invalidating
   event, not by repeating full discovery before every call.
2. Classify observation, structured mutation and arbitrary script/process execution.
   Existing task authorization covers necessary in-scope operations; tool presence
   expands no permission and creates no per-edit confirmation requirement. Apply
   the shared [trust boundary](../core.md#external-content-and-instruction-authority)
   to tool output and project content.
3. Inspect before editing; use bounded coherent operations and observe errors
   immediately. Know which calls autosave, which files they touch and whether undo
   covers editor state, disk or both. Account for
   [editor-executed code](assets-export.md#export-and-editor-execution).
4. Inspect the resulting state. On partial/unknown outcomes, reconcile it before
   retrying; do not blindly replay a non-idempotent batch. A rollback label or editor
   undo is not a guarantee of atomic multi-file disk recovery.
5. Distinguish editor diagnostics, runtime logs, actual game state and rendered
   observations. Check the relevant log/session, including startup failures when
   the game log is incomplete. An unchecked language diagnostic is not a clean build.
   Tool success alone does not establish project acceptance.
6. Use the ordinary [verification boundary](verification.md), not a full run after
   every call. Clean up task-created processes/fixtures as appropriate without
   stopping the user's unrelated session. Report capabilities that remain unavailable.

The [MCP tools contract](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)
describes protocol results, not Godot/application correctness. Tool annotations are
not an independent source of trust or authorization.

## Bounded qualification when adopting

Exercise only selected capabilities in a disposable project/scene with the real
client: identify the intended session; read a known property; make a bounded edit;
verify save/reopen and undo if relied on; introduce/remove a diagnostic error; run
and stop the intended game and inspect relevant logs. Check actual capture/input
when selected, and a failed/partial mutation with recovery without unsafe replay.
Check configuration preservation and export exclusion where those claims matter.

Record observed results and untested capabilities in existing adoption evidence.
Restrict a partially qualified provider to supported uses and retain direct-tool
fallbacks. Do not call a textual scene description a screenshot, claim C# compilation
from script-edit success, or infer reliability from a tool list/marketing demo.
This qualification is not a new agent role, routine extra review or prerequisite
for source-only Godot work.
