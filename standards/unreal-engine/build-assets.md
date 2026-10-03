# Unreal build, assets and compatibility

Read the affected section for modules, build/reload decisions, asset references or
packaging. Use the project's actual engine/build identity, host and target; the
documented reference is UE 5.8. Select checks with [Unreal verification](verification.md).

## Modules and build inputs

- Use UBT/UHT with the actual `.uproject` or plugin host, target, configuration and
  platform. An IDE-generated project is not the authority for module dependencies.
  Do not introduce a parallel generic C++ build just to compile Unreal examples.
- Keep cohesive runtime and editor modules distinct. Runtime public contracts must
  not accidentally require editor-only modules. Add a module for a meaningful
  responsibility or loading/deployment boundary, not every small class.
- Declare public dependencies for types needed by public headers; implementation
  dependencies remain private. Keep dependencies acyclic rather than enabling
  legacy circular allowances to silence a build error.

Basis: [Modules](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-modules),
[module properties](https://dev.epicgames.com/documentation/unreal-engine/module-properties-in-unreal-engine).

Include the headers actually needed; keep headers self-sufficient and include the
matching header first in its implementation. Do not rely on an unrelated unity
build file or transitive include for correctness. Respect the project's supported
IWYU/PCH settings rather than globally changing them for a local fix.
[IWYU](https://dev.epicgames.com/documentation/unreal-engine/include-what-you-use-iwyu-for-unreal-engine-programming).
Edit reflected declarations, not generated output; UHT processing precedes C++
compilation. [UHT](https://dev.epicgames.com/documentation/unreal-engine/unreal-header-tool-for-unreal-engine).

Preserve diagnostic/build failures and identify the affected module or missing
input. A local change does not justify an engine rebuild, global flag override,
cache purge or deletion of Intermediate. Use an established clean-build gate when
required, or a scoped rebuild when a diagnosed stale artifact warrants it.

## Iteration and reload

Choose the iteration path for the changed contract and actual host capability:

| Change | Decision |
| --- | --- |
| Existing function body | Use supported Live Coding if sufficient for the task; verify the affected behavior |
| Reflected/layout/default or module change | Establish whether rebuild, reinstancing or restart is needed; do not infer it from a body-only patch success |
| Reloaded objects cached by tools/gameplay | Invalidate or rebind affected references through supported reload/lifecycle mechanisms |
| Cold start or packaged target contract | Use the corresponding normal build/launch or package evidence |

Live Coding supports reinstancing, but cached object references and constructor
defaults require care. Do not disable reinstancing to suppress symptoms or assume
every structural edit has the same reload behavior. Preserve unsaved work before
restart, and reacquire changed editor handles afterward.
[Live Coding](https://dev.epicgames.com/documentation/unreal-engine/using-live-coding-to-recompile-unreal-engine-applications-at-runtime).

## Binary assets and reference migrations

- Change `.uasset` and `.umap` through supported editor APIs/tools; do not text-patch
  or text-merge them. Respect the selected source-control locking/ownership policy;
  do not disable it, check in, or change providers as routine editing housekeeping.
- Identify the affected packages, relevant references and prior dirty state before
  a move or rename. Use editor-aware operations so asset references can be updated.
  An asset redirector and a reflected Core Redirect serve different contracts.
- Asset redirector fixup can resave referencing packages. Bound that work; do not
  run project-wide fixup/resave commands or copied auto-checkout/check-in flags for
  a local task without scope that includes those effects.
- A reflected class/property/function rename may need Core Redirects for serialized
  consumers. Preserve required saved-content compatibility and keep redirects until
  the supported migration contract permits removal, not merely until code compiles.

Basis: [Binary assets and source control](https://dev.epicgames.com/documentation/unreal-engine/using-perforce-as-source-control-for-unreal-engine),
[asset redirectors](https://dev.epicgames.com/documentation/unreal-engine/asset-redirectors-in-unreal-engine),
[Core Redirects](https://dev.epicgames.com/documentation/unreal-engine/core-redirects-in-unreal-engine).
For editor mutations and partial recovery, use [MCP/editor workflow](mcp-editor.md#mutation-and-recovery)
when operating through that provider; the asset ownership contract also applies
to other supported editing tools.

## Loading, cook and package

Choose hard references when the dependency belongs in the owning object's loading
contract. Use soft references for deliberate deferred loading, with a load request,
completion/failure behavior and retention owner. A valid asset path does not prove
that the object is loaded or will stay alive; see [reference ownership](cpp-lifetime.md#references-and-ownership).

Use Asset Manager for an actual discovery/loading/audit or chunking requirement;
do not make every reference soft or every small feature a primary-asset system.
Verify that dynamically selected assets are included by the project's actual cook
rules. Presence in the Content Browser is insufficient.
[Asset management](https://dev.epicgames.com/documentation/unreal-engine/asset-management-in-unreal-engine).

Build compiles code; cook prepares target content; stage/package assemble it;
deploy/run exercise a target. Use the selected project commands and required gates.
An editor build is not evidence that an editor-only dependency or dynamically
loaded asset works in the package. Avoid full cook/package cycles for unchanged
contracts; [verification](verification.md) determines what evidence is needed.
[Build operations](https://dev.epicgames.com/documentation/unreal-engine/build-operations-cooking-packaging-deploying-and-running-projects-in-unreal-engine).
