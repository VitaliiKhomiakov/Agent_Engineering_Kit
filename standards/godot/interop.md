# Conditional Godot C# and GDExtension guidance

Read only the language boundary actually used or changed. A GDScript-only project
needs neither .NET nor a native compiler because this topic is bundled. Shared
[architecture](architecture.md), [runtime](lifecycle-runtime.md) and
[assets/export](assets-export.md) contracts still apply.

## C#

Establish the project's .NET editor, target framework/SDK, engine version and
compatible packages before choosing build commands. Preserve C# naming and .NET
conventions rather than translating GDScript naming mechanically. Separate existing
independent logic and engine/tree responsibilities at suitable owners; a second
assembly is justified by a real boundary, not by a desire for smaller files.

Declare `GodotObject`-derived types `partial` (diagnostic GD0001) and name an
attached script's class after its `.cs` file. Use useful types and explicit
nullable/dynamic boundaries. Managed garbage
collection and native Godot object lifetime are different contracts. Do not assume
that a non-null managed reference means its native object remains usable; use
`GodotObject.IsInstanceValid` at a boundary where it may already be freed. Respect
the affected lifecycle when subscribing, awaiting or delivering callbacks.

Use typed signals/events where appropriate and rebuild when required for generated
editor-visible contracts. Disconnection behavior has exceptions, including capturing
lambdas and custom signal cases; verify and release the actual subscription rather
than assuming every connection is automatically safe. See
[C# signals](https://docs.godotengine.org/en/4.7/tutorials/scripting/c_sharp/c_sharp_signals.html).

Build changed C# and verify affected engine behavior. A text write, successful MCP
call or empty GDScript diagnostic result is not a C# compiler result. For independent
logic, ordinary .NET tests may suffice; engine-bound tests need the compatible
runner/engine combination selected through [tooling](tooling-mcp.md#formatting-and-tests).

The reviewed [Godot 4.7 C# contract](https://docs.godotengine.org/en/4.7/tutorials/scripting/c_sharp/c_sharp_basics.html)
does not support Godot 4 C# web export and describes Android/iOS support as
experimental. Check actual version/target support before promising delivery; do
not silently switch languages or upgrade the engine to bypass a constraint. Take
SDK requirements from the selected project/engine contract, not a stale generic
minimum copied into all projects.

## GDExtension

Choose a native boundary for a concrete native-library integration or measured
performance need. Do not convert GDScript to native code on an assumed speed benefit.
Keep the exported boundary narrow and preserve engine ownership/lifetime semantics;
native code does not make scene-tree access from worker threads safe.

Record and pin the target engine API, bindings, compiler/toolchain, operating system,
architecture, debug/release mode and precision where applicable. An extension built
for an earlier 4.x minor version should load in later minor versions, not the
reverse, and 4.0-targeted extensions do not load in 4.1+; do not promise one binary
works across all Godot 4.x versions. Custom engine builds may require matching API/binding inputs.
Use [godot-cpp's contract](https://docs.godotengine.org/en/4.7/tutorials/scripting/cpp/about_godot_cpp.html)
when that binding is selected; it does not select Unreal guidance.

Keep `.gdextension` compatibility bounds and library mappings consistent with the
actual built libraries and export targets: `compatibility_minimum` is the lowest
engine version actually targeted, and optional `compatibility_maximum` (4.3+) only
records a known upper bound. Verify extension loading and relevant
runtime behavior in addition to compilation, including the affected exported
configuration when needed. A successful host build is not a target/ABI check.
Descriptor reference:
[GDExtension files](https://docs.godotengine.org/en/4.7/engine_details/engine_api/gdextension/gdextension_file.html).

Select proportionate checks through [verification](verification.md). Report a missing
SDK/compiler/target separately from any source review already completed; an MCP
provider does not supply that missing evidence merely by editing the files.
