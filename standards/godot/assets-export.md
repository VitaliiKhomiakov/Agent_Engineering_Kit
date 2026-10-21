# Godot assets, serialization and export

Read for changed scenes/resources, asset imports, file moves, VCS or export contracts.
Preserve user-authored content and unsaved editor work through the shared baseline
policy and, when operating an editor provider, [its workflow](tooling-mcp.md#editor-and-mcp-operations).

## Scenes and resource identity

Godot's `Node.owner` controls which nodes are saved with a scene; it is not the
gameplay responsibility owner or a replacement for tree parenting. Editor-created
nodes intended to persist need correct serialization ownership. Save/reopen the
affected scene when that contract changes; visibility in the current editor is
insufficient. Runtime-only children do not all need serialization owners. Consult
the [Node API](https://docs.godotengine.org/en/4.7/classes/class_node.html).

Prefer an editor or proven structured operation when it preserves serialization
correctly. Bounded text edits to `.tscn`/`.tres` are valid when IDs/references and
format are understood and the result is loaded/checked. Avoid unrelated ordering,
float or generated-data churn and reconstruction that discards user-authored fields.
Respect inherited scenes and instance overrides instead of silently flattening them.

Preserve existing resource identities, including applicable script/shader UID
sidecars. Move them with their source and check affected references. Do not invent
new UIDs, regenerate the cache or mass-resave unrelated scenes to work around a
local path edit. UID support is version-sensitive; see the
[4.4 change history](https://godotengine.org/article/uid-changes-coming-to-godot-4-4/)
and current [ResourceUID contract](https://docs.godotengine.org/en/4.7/classes/class_resourceuid.html).

## Source assets and imports

Keep original assets, authored resources and applicable import settings in the
project's source pipeline. Generated `.godot/` caches/import products are not the
durable source of an edit. Use the version-appropriate ignore rules, preserving
relevant sidecars. Optional LFS is for selected suitable binaries, not all text
scenes or an automatic history rewrite. Sources:
[import process](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/import_process.html),
[version control](https://docs.godotengine.org/en/4.7/tutorials/best_practices/version_control_systems.html).

For 3D assets, keep the authoring source/import and intentional overrides distinct.
glTF is a suitable interchange default. Direct `.blend` import is valid when its
Blender dependency is deliberately provisioned, including in CI. Do not fix an
imported model by changing only generated output that the next import replaces.
Use the [format/import contract](https://docs.godotengine.org/en/4.7/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html)
for the selected version and target.

## Export and editor execution

Load imported engine resources with appropriate resource APIs. Raw filesystem reads
that work in the editor checkout can fail after export. Check dynamic inclusion,
case-sensitive paths, presets, templates and platform dependencies when affected.
An editor run does not validate an exported build. Keep signing material/credentials
out of committed configuration, without indiscriminately applying older Godot
export-preset ignore rules to newer releases. See
[exporting projects](https://docs.godotengine.org/en/4.7/tutorials/export/exporting_projects.html).

Keep development add-ons from becoming accidental runtime dependencies or exposing
privileged development behavior in an export. Verify the selected inclusion/exclusion
mechanism; an `addons` directory or `@tool` annotation alone does not prove exclusion.
Editor scripts and plug-ins can execute during editor/import work and mutate project
state. Account for that execution when selecting operations and recovery; arbitrary
file changes are not automatically covered by editor undo. See
[running code in the editor](https://docs.godotengine.org/en/4.7/tutorials/plugins/running_code_in_the_editor.html).

Select scoped import/load, save/reopen and export evidence through
[verification](verification.md). Preserve valid evidence for unchanged behavior;
a file move still needs the affected reference/identity checks.
