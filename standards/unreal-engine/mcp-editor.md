# Unreal MCP and editor operations

Read for editor-provider setup, discovery, mutation or missing-tool evaluation.
This procedure is complete without an installed skill. Source-only work need not
connect an editor; report unavailable dependent checks under [verification](verification.md).

## Native provider basis

The researched UE 5.8 `ModelContextProtocol` plugin is experimental. Its default
local HTTP endpoint is `http://127.0.0.1:8000/mcp`, without authentication; do not
expose it remotely. Toolsets may be enabled individually. Native calls execute
serially on the game thread: clients must not overlap them. Tool-search discovery
uses `list_toolsets`, `describe_toolset`, then `call_tool`.

`ModelContextProtocol.StartServer` supports on-demand startup;
`ModelContextProtocol.StopServer` stops the server.
`ModelContextProtocol.GenerateClientConfig` writes client configuration; inspect
its resolved path and existing contents first. JSON merging and Codex TOML's
write-once behavior differ. Preserve existing configuration rather than deleting
it to bypass an overwrite refusal.

`ModelContextProtocol.RefreshTools` refreshes discovery after tool changes. New C++
`UFUNCTION` tools require an editor restart; body-only Live Coding has a different
contract. Python and C++ toolsets are supported. Runtime modules also exist;
local editor use is framework scope, not a claim that runtime hosting is impossible.
[Native MCP documentation](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor).

## Context and setup

Resolve the intended project/build, provider/version, endpoint/editor instance,
relevant map/world and PIE state. Reuse these facts until an event invalidates them.
Do not start another instance simply because one tool lookup failed.

When setup is necessary and in scope, select only needed plugins/capabilities and
one intended client. Preserve existing settings and required source control.
Resolve paths from the actual installation/project; do not copy another machine's
launch environment or native-client CLI syntax. Confirm connection with a scoped
read of the intended editor context, not merely a successful registration message.

Personal configuration, installation, restarts and remote/runtime exposure are
separate effects; use existing task authorization and clarify only material gaps.
For an older engine or another MCP provider, establish its capabilities and
transport/concurrency contract before dependent work. Do not apply native command
or tool names to a different provider.

## Bounded discovery

Read only needed tool schemas and request relevant objects/properties. Preserve
returned identifiers. A filesystem path, package path, object path and generated
class reference are different inputs; follow the selected tool's actual contract
rather than appending a suffix to every string.

Use supported structured tools before UI automation. A missing operation is a
reason to inspect the relevant capability, not dump all schemas, properties or
the entire scene. Keep discovered schema evidence until provider/tool changes
invalidate it; a new conversational step does not require discovery again.

## Mutation and recovery

Use the [block-level verification cadence](verification.md#complete-a-coherent-block-then-verify).
For repeated, understood operations, prefer an existing supported batch tool or
bounded editor script over one model round-trip per object/property. Discover
the actual schema first; batch support is provider/version dependent. Otherwise,
use serial calls and keep the same block boundary for verification.

A batch must report affected identifiers, completed/failed/skipped operations and
completion/persistence state, with detailed logs retained outside model context.
Stop dependent operations on failure. Do not assume atomicity, rollback or safe
whole-batch retry. Split at uncertain imports, required compiles/reloads and other
dependencies that need observation before more writes. Return concise summaries
and relevant errors, not whole scenes, every property or full successful logs.

1. **Set scope and baseline.** Identify affected objects/packages, intended changes
   and existing dirty state. A disk backup does not preserve unsaved editor work.
   Obtain a supported recoverable state or resolve the limitation before dependent
   mutations. Do not save unrelated packages just to manufacture a baseline.
2. **Coordinate ownership.** Use one mutation owner for a shared editor, and honor
   the provider's execution contract. Native reads and writes both follow its
   serial-call rule. Other agents may work on independent source tasks only when
   their edits/builds cannot invalidate the active operation.
3. **Execute and observe.** Use the established selection and schema. Interpret
   structured errors and completion state. Submission, completion and saving are
   distinct outcomes; a transport success is not enough. Observe pending work with
   bounded waits rather than submitting it again.
4. **Resolve uncertainty.** After a timeout/disconnection, inspect operation status
   or affected state before retrying a mutation. Avoid duplicate spawns/imports or
   partially repeated batches. If the effect cannot be established, stop dependent
   writes and report what is known; do not invent success or automatic rollback.
5. **Persist deliberately.** Save affected work within scope and report any remaining
   unsaved state. Preserve intervening user edits. A transaction/undo facility is
   useful only for effects it actually covers, not arbitrary files/external actions.
   Recover only owned changes whose prior state and intervening edits are understood.
6. **Verify and release.** Inspect the changed contract and perform selected checks.
   After reload/restart/world replacement, reacquire affected handles/context.
   Restore temporary selection/PIE state owned by the task when appropriate; do not
   stop a pre-existing server/editor or discard user work as generic cleanup.

Choose evidence under [Unreal verification](verification.md). Reuse relevant results
and do not append a full scene scan, screenshot series or second review for reassurance.
[ToolsetRegistry](https://dev.epicgames.com/documentation/unreal-engine/API/Plugins/ToolsetRegistry)
documents descriptors and async result types; inspect the actual tool's completion
contract instead of assuming every operation completes with the first reply.

## Optional skills and custom tools

See [recommended skills and compatibility limits](skills.md) when selecting an
execution aid. Load only the relevant skill and references, not every listed
skill or the entire provider catalog.

Use a compatible installed `unreal-engine-mcp` skill as an execution aid, subject to
the framework's [Superpowers/workflow policy](../superpowers.md) and task scope.
Do not copy its absolute paths, source-control flags, environment changes, optional
parameter workarounds or camera assumptions as universal defaults. Client reconnect
or session restart depends on actual discovery behavior, not the skill's assertion.

For a genuinely missing operation, inspect existing tools and supported editor
APIs first. Consider a custom tool only for a present workflow that warrants it.
Specify bounded inputs, structured results, affected state, completion/failure and
recovery semantics. Keep provider implementation and installation separately scoped.
Python editor scripting is useful for supported content automation; it is not a
general packaged-game scripting facility.
[Editor Python](https://dev.epicgames.com/documentation/unreal-engine/scripting-the-unreal-editor-using-python).

Select Python or native implementation from required API access, reflected types
and measured costs. Read the chosen version's tool-authoring contract when needed.
A documented vendor skill is not proof of local availability. This profile neither
installs a skill/plugin nor requires one for ordinary editor work.
