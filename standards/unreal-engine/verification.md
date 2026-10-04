# Unreal: sufficient verification and evidence reuse

Read when selecting checks or reporting Unreal work. The shared
[verification policy](../verification.md) owns baselines, necessary tests, review,
required gates and evidence reuse. Apply the relevant rows below to the changed
contract; they are not a sequence to run after every edit.

## Complete a coherent block, then verify

Before editing, name the observable result, affected objects/packages and cheapest
sufficient checks in the existing task record. A block is a checkable outcome:
one completed Blueprint interaction, a prop group placed in a room, or an asset
prepared in Blender and imported into Unreal. Do not define it as an arbitrary
number of calls or postpone all verification until an entire game is finished.
Select the phase/task verification boundary under the shared
[timing policy](../verification.md#what-to-run-and-when); the block cadence below
applies at that boundary, retaining required intermediate checks.

1. Establish the relevant context and recoverable baseline once.
2. Finish the related edits using known schemas and returned identifiers. Read
   each operation's status/errors and completion state immediately; this is not
   a separate build, scene scan, screenshot or gameplay verification cycle.
3. At the block boundary, run the selected checks together and inspect their
   results. Save affected work deliberately, distinguishing live and persisted
   state. Reuse any still-valid intermediate evidence.
4. Fix observed defects and repeat only affected checks and required gates.
   Stop when acceptance is met; no extra reassurance pass or final screenshot.

Check earlier only for a failure, an uncertain operation outcome, a risky
dependency, selected TDD or a required gate. For example, compile a Blueprint
before using a newly generated class, or validate one representative import
before repeating an unfamiliar export/import setup across many assets. Wait for
required compilation/loading before dependent edits. Batching never means
ignoring errors, duplicating uncertain writes or executing shared-editor calls
concurrently.

For Blender-to-Unreal work, complete the scoped modeling/material/export edits,
then check the imported asset's relevant scale, orientation, normals, material
slots, collision or animation in Unreal. File existence and a Blender render
alone do not prove a correct import. Inspect only properties relevant to the
task; a geometry-only edit does not automatically require lighting renders.

For visual work, use a targeted viewport capture or low-cost preview at a useful
milestone. Use a final-quality render only when that quality is an acceptance
criterion. A single frame cannot establish animation timing or gameplay behavior.
There is no fixed screenshot quota; take additional views only to resolve a
specific occlusion or unanswered visual criterion.

This cadence is framework policy applying the user's cost constraint. It is
consistent with [Epic's editor automation guidance](https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-and-automating-the-unreal-editor)
and [on-demand MCP/code execution](https://www.anthropic.com/engineering/code-execution-with-mcp),
not a vendor-mandated check count or a measured token-saving claim.

## Select evidence by changed contract

| Change | Useful evidence | Reason to widen |
| --- | --- | --- |
| Instructions or wording | Affected links, formats and concrete reading/decision scenarios | Executable content or a routing contract changed |
| Ordinary C++ behavior | Relevant target compilation and focused existing or meaningful regression test | Engine interaction or target-specific behavior changed |
| Reflected declaration or module contract | Applicable UHT/UBT build and dependent Blueprint/asset compatibility | Layout, loading, restart or packaged runtime boundary is affected |
| Blueprint graph or interface dispatch | Compile affected Blueprints; relevant PIE/functional scenario for behavior | Derived classes, callers or native/Blueprint dispatch changed |
| Asset settings or references | Inspect affected assets and applicable scoped validation | Rename dependencies, loading or cook inclusion changed |
| Multiplayer behavior | Relevant authority/client/ownership scenario | Late join, reconnect or network conditions are affected or required |
| Cook/package configuration | Relevant target cook/package and required launch check | Additional targets or gates require coverage |
| Performance | Comparable bounded numeric capture of the affected workload | Acceptance concerns another workload or the bottleneck moved |

Choose actual project commands and supported target/configuration/platform, not a
command copied from another workstation. A source-only task can proceed without
MCP; record editor-dependent evidence that is unavailable. A mandatory unavailable
gate remains outstanding rather than being declared passed.

## Reuse checks and tests

Prefer existing project tests and validation hooks that cover the changed contract.
Use engine-dependent automation/functional tests for engine behavior; module-oriented
Low-Level Tests can suit isolated native logic. Their availability does not require
installing both frameworks or adding a test for every class, accessor or reflected
field. Keep test data and editor state isolated and restore changes owned by the test.
[Automation Framework](https://dev.epicgames.com/documentation/unreal-engine/automation-test-framework-in-unreal-engine),
[Low-Level Tests](https://dev.epicgames.com/documentation/unreal-engine/lowlevel-tests-in-unreal-engine?lang=en-US).

For content changes, select relevant assets/dependencies and confirm which validators
actually execute. The Data Validation commandlet's default coverage must not be
assumed to include all Blueprint/Python validators. Running it successfully with no
relevant validator is not evidence for the intended content contract.
[Data Validation](https://dev.epicgames.com/documentation/unreal-engine/data-validation-in-unreal-engine).

Add coverage for a material regression or uncovered requirement, at the cheapest
reliable level. Avoid duplicating the same assertions in unit, editor, functional
and screenshot tests without distinct failure modes. Preserve established CI gates;
a small diff does not waive them. Documentation alone needs no engine test project.

## Preserve the state being checked

Distinguish source/asset bytes on disk, current editor objects, unsaved packages
and loaded binaries. Before a mutation or required restart, preserve the relevant
baseline, including user edits. A disk snapshot does not capture unsaved editor
work. Use a supported recoverable state or resolve that limitation before dependent
mutations; do not save all unrelated user packages as verification housekeeping.

A source build validates a different state from a patched editor. A Blueprint
compile does not establish correct gameplay dispatch. A tool response may confirm
submission rather than completion or persistence; check the operation's actual
result. A screenshot supports a visual claim, not object ownership or numeric
performance by itself.

Build, cook, package and run have different purposes. Select the ones needed by the
changed contract rather than treating editor success as proof of a target release.
[Build operations](https://dev.epicgames.com/documentation/unreal-engine/build-operations-cooking-packaging-deploying-and-running-projects-in-unreal-engine).
Use representative conditions and bounded profiling for performance claims.
[Performance profiling](https://dev.epicgames.com/documentation/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine).

## Stop when the evidence is sufficient

Before repeating a build, test, search, scene scan, diff review or screenshot, reuse
the recorded result if applicable. State the changed input, unreliable result,
concrete unanswered failure or required fresh gate that makes a repeat necessary.
Use the smallest check that answers it; a final report or new agent is not a reason.

After a fix, repeat affected checks and retain unrelated results. An editor restart
can invalidate object handles and loaded state without invalidating an unchanged
source check. A world change can invalidate runtime evidence without requiring
another whole-project compilation. A report-only edit does not invalidate code tests.

Observe unfinished operations with bounded waits. Do not restart an operation
merely because it has not completed; inspect uncertain mutation outcomes before
retrying. No fixed count of screenshots, review rounds or complete build/cook/test
cycles is required at stage end.

Record scope, relevant artifact/editor state, command or inspection, outcome and
limits in the existing task record. Distinguish documented behavior, library artifact
checks and observed runtime results. Fix confirmed in-scope defects; once criteria
and required gates are satisfied, report and follow the agreed stage checkpoint.
