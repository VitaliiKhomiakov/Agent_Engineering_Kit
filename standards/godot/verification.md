# Godot verification and evidence

Use [shared verification](../verification.md) for baseline preservation, cadence,
test selection, required review and evidence reuse. This topic selects engine-specific
evidence; it adds no new approval gate, agent or reporting form.

## Select checks by changed contract

Reuse the actual engine/edition, renderer, platform and tool versions from the
project context. Inspect final changed source and meaningfully affected scenes,
resources or settings; do not run every export or audit every scene for a local task.

| Changed contract | Relevant evidence and limit |
| --- | --- |
| GDScript | Relevant engine parsing/warnings, selected mechanical checks and [readability](gdscript.md#scoped-acceptance); focused behavior evidence when warranted |
| Scene/resource/import references | Relevant import/load and reference/UID inspection; instantiate or save/reopen when that contract changes |
| Gameplay, state, lifecycle or physics | Focused existing tests or a reproducible in-engine scenario including affected transitions/failure cases |
| UI, rendering or animation appearance | Actual rendered observation at the relevant scene/state, viewport and renderer/target |
| C# | Appropriate .NET build/tests and affected engine contracts; see [interop](interop.md#c) |
| GDExtension | Selected native build, extension load and affected runtime/export configuration |
| Export or asset pipeline | Actual selected preset/templates and relevant target smoke check; editor success covers a different environment |
| MCP mutation | Resulting project/editor/runtime state under [the provider workflow](tooling-mcp.md#editor-and-mcp-operations), not just its success response |

Keep a suitable existing runner; establish [discovery/failure exits](tooling-mcp.md#formatting-and-tests)
when adding or changing test automation. A short scene run without assertions is
a smoke observation, not a replacement for all behavior tests. Missing engine,
target, renderer or client access is an evidence limit, not a silent pass.

## Command scope

The following are illustrative shapes from the versioned
[command-line contract](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html),
not universal project checks or commands executed by adopting this profile:

```sh
godot --version
godot --headless --path /absolute/project --import
godot --headless --path /absolute/project --script res://scripts/example.gd --check-only
godot --headless --path /absolute/project --scene res://scenes/example.tscn --quit-after 30
```

Use the actual executable/path and confirm flags with its help; unsupported options
must not yield a false claim of coverage. Import performs editor/import work and
can execute enabled editor code; it is not read-only. The script check covers the
supplied script, not an all-project build, runtime or visual assertion. The quit
limit counts iterations, not seconds. Bound process time when appropriate, inspect
diagnostics as well as exit status, and distinguish the intended run from unrelated
editor/game processes. On a checkout without `.godot/`, run an import first; even
then, `class_name` and autoload references can produce false script-check errors
(engine issues [#78587](https://github.com/godotengine/godot/issues/78587) and
[#93424](https://github.com/godotengine/godot/issues/93424)). Confirm a suspected
false error in the editor or after a repeated import rather than editing code to
silence it. Export commands additionally need the actual preset, matching
templates and output location. Use the selected runner's real version-specific CLI.

Do not treat successful parsing/import, compiler output, rendered inspection and
target export as interchangeable evidence. A headless check cannot establish
appearance; C# text editing is not compilation; a native host build is not proof
that an extension loads in the exported target.

## Readability and role handoff

[GDScript](gdscript.md) owns its detailed typing/style/grouping requirements;
[architecture](architecture.md) owns engine-specific responsibility placement.
The [shared acceptance policy](../verification.md#readability-acceptance) requires
implementers to inspect final changed code after formatting, reviewers to cover
binding requirements in the existing scoped review, and coordinators to confirm
the evidence and resolve in-scope violations before acceptance.

Record scope and outcome separately from formatter output in the existing evidence
note. Reviewers locate concrete violated requirements; optional preferences or a
cohesive sequence already satisfying the rule need no finding. No per-function
form, second checklist or additional whitespace review is required. Reading an
instruction, an empty diagnostic list or a clean formatter does not prove the
semantic check happened.

## Reuse and reporting

Use [evidence reuse](../verification.md#reuse-evidence-before-repeating-work) when
code, relevant context, tools and criteria remain covered. Moved unchanged scripts
can retain behavior/style evidence while changed paths/UIDs need scoped checks.
A newly adopted or clarified requirement needs an explicit coverage assessment;
historical clean acceptance is not proof of an unexamined rule. Close that gap
without initiating a repository-wide cleanup.

Report the checked scope, outcomes and material remaining limits compactly, including
which evidence is manual or source-only. Artifact checks can verify delivered rules
and links; engine/tool checks can establish their stated mechanical/runtime scope.
Responsibility placement, semantic readability and adequate coverage still depend
on agent judgment. Instruction changes cannot guarantee future agent compliance.
