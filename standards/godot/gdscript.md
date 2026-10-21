# GDScript contracts and readability

Read for changed GDScript and its scoped review. These are AEK conventions for
the project's supported Godot version, not universal language requirements.
Reconcile explicitly adopted local conventions during integration rather than
silently replacing them.

## Types and warnings

Use useful declared types for function parameters/returns, exported properties,
signals and collections whose element contracts are known. Prefer clear local
inference where it retains the intended type. Do not let an inferred `Variant`
silently weaken a known contract or substitute an unstructured dictionary for
an established named domain contract. Genuine dynamic data is valid at a boundary;
validate and narrow it before passing it into ordinary typed code.

Use collection/type syntax available in the actual engine version. A cast can
fail; handle the real nullable/dynamic boundary instead of asserting it away.
GDScript permits gradual typing; this profile's stronger application-contract
convention is a local policy choice. Consult
[static typing](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/static_typing.html).

Resolve relevant warnings in changed code. Preserve the project's warning policy;
do not make every category fatal or disable a category globally just to clear a
local issue. A necessary narrow suppression explains the intentional boundary or
false positive. The [warning system](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/warning_system.html)
provides diagnostics, not proof of behavior or readability.

## Mechanical conventions

Use the versioned [GDScript style guide](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/gdscript_styleguide.html)
as the baseline: tabs for indentation, UTF-8/LF, snake_case functions/variables and
script paths, PascalCase classes/nodes and uppercase constants. Keep one statement
per line, two blank lines between function/class definitions and consistent
declaration ordering. Prefer lines below 100 characters, with shorter lines where
practical; wrap expressions without hiding their structure. Explicit project
adaptations remain governed by the adopted local style.

GDScript is not Python. A Python formatter/type checker is not a GDScript check.
Select optional mechanical tools through [tooling](tooling-mcp.md#formatting-and-tests),
checking compatibility with the actual syntax and established layout.

## Semantic grouping inside functions

Separate meaningful phases with blank lines while keeping tightly related
statements together. This section is the canonical owner of AEK's GDScript
grouping requirement. A blank line after every statement obscures the groups.

Creation, configuration and returning the configured result are distinct phases
in this illustrative Godot 4.7 function. Related configuration stays together:

```gdscript
func create_progress_bar() -> ProgressBar:
	var bar := ProgressBar.new()

	bar.min_value = 0.0
	bar.max_value = 1.0
	bar.show_percentage = false

	return bar
```

Removing the two internal blank lines hides those phases and violates this
convention even if parsing/formatting succeeds. The three configuration assignments
are cohesive and need no internal blank lines. The caller attaches/manages the
returned node; this example does not prescribe a factory architecture or UI design.
API reference: [ProgressBar](https://docs.godotengine.org/en/4.7/classes/class_progressbar.html).

An operation and its immediate failure guard ordinarily belong together. This
illustrative function-body excerpt assumes an existing resource path and caller's
failure contract:

```gdscript
var resource := ResourceLoader.load(path)
if resource == null:
	return
```

Do not insert space between that operation and its guard solely because the next
statement is an `if`. An early return belongs inside the guard. A final return can
be a separate phase in a multi-step function, as above; it is not always one.
Do not require blank lines before every conditional/return, after every block or
at fixed line counts. A short cohesive sequence may remain one group. Do not extract
functions or add comments merely to manufacture visual separation.

These examples explain the policy; they are not executed engine regression fixtures.
The engine-compatible API shape does not establish runtime or UI acceptance.

## Scoped acceptance

Apply the rule while writing and inspect final changed functions after formatting,
including meaningfully affected surrounding code. Follow shared
[readability acceptance](../verification.md#readability-acceptance) for implementation,
review and coordination; use the existing evidence note rather than a second form.

For example: `ui/progress.gd: create_progress_bar — creation, configuration and
result groups checked; no violations.` That path is illustrative, not a required
directory. A compact statement can cover several functions. Formatter output
cannot establish semantic grouping. A binding violation is a located finding;
a cohesive sequence that already meets the requirement needs no stylistic finding.
