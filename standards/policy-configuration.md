# Project policy settings

Read when a task depends on verification timing, independent-review preference,
size/cohesion thresholds or instruction-length guidelines, or when changing these
settings. This document owns schema, resolution and field meanings. The
[defaults file](policy-defaults.toml) is the single operational source of default
values; the Markdown procedure owners below retain conditions and exceptions.
These are local engineering choices, not client settings or vendor limits.

## Locations and resolution

1. Read `standards/policy-defaults.toml` from the selected bundle root: the source
   root in this library, normally `.agents-framework/` in an adopted project.
2. If present, read `.agents-framework/policy.toml` from the target instruction
   root, including when the bundle is flat or uses a custom directory. It is an
   optional sparse override; do not create an identical copy on import.
3. Validate the complete defaults and each explicitly supplied override field,
   then resolve each setting as its override value or the corresponding default.
   Validate cross-field constraints in the merged result as well. Omitted fields
   or tables inherit; omission never means zero, disabled or reset to an example.

Source maintenance uses its bundled defaults without installing target settings.
No override means no onboarding or questionnaire. Read only settings relevant to
the task, reusing them while their inputs remain valid. A changed value invalidates
only affected decisions/evidence, not every previous check. There is no background
monitor, automatic reload or runtime enforcement.

Changing defaults or project overrides is a reviewed policy change within the
task's existing authorization/checkpoint. Copying a template does not authorize
new settings. Explicit user instructions, higher-priority rules and mandatory
project/client requirements take precedence. Settings cannot grant Git writes,
delegation or task progression, remove acceptance criteria, waive failed checks
or turn incomplete work into success. Models, efforts, roles and concurrency
remain owned by [model configuration](model-configuration.md); do not copy them here.

## Schema version 1

Defaults and overrides require integer `schema_version = 1`, independent of catalog
and model-routing schemas. Defaults contain every field below. Overrides may omit
recognized fields/tables, but still declare their schema. No other keys are allowed.

| Field | Allowed values and meaning | Procedure owner |
| --- | --- | --- |
| `verification.timing` | `phase_end` batches necessary checks at the logical phase boundary; `task_end` batches them at the planned task boundary. Neither means per-file/per-edit checks or repeating still-valid earlier results. | [Verification timing](verification.md#what-to-run-and-when) |
| `verification.diagnostic_reset_after_stalled_attempts` | Positive integer: consecutive unsuccessful attempts on the same problem without new evidence trigger diagnosis. Legitimate TDD red steps do not count. This is not a fix-round limit or permission to abandon a defect. | [Lack of progress](verification.md#completion-and-lack-of-progress) |
| `review.independent` | `risk_based` selects independent review for material risk/complexity or an explicit request; `on_request` selects it when explicitly requested or required by project policy. Coordinator review remains required in both cases. | [Review boundaries](verification.md#review-boundaries) |
| `size.function_review_lines` | Positive integer: review extraction above this function/method declaration-span threshold. | [Size and cohesion](core.md#size-and-cohesion) |
| `size.class_review_lines` | Positive integer: review class cohesion above this declaration-span threshold. | [Size and cohesion](core.md#size-and-cohesion) |
| `size.file_review_lines` | Positive integer: review module composition above this physical-line threshold. | [Size and cohesion](core.md#size-and-cohesion) |
| `size.growth_review_from_lines` | Positive integer: review class/file cohesion before further growth at or above this threshold. It cannot exceed `size.documented_review_above_lines`. | [Size and cohesion](core.md#size-and-cohesion) |
| `size.documented_review_above_lines` | Positive integer: new/substantially rewritten behavior classes/files above this threshold need a documented cohesion review. | [Size and cohesion](core.md#size-and-cohesion) |
| `size.react_component_review_lines` | Positive integer: review mixed component responsibilities above this threshold; shared size rules still apply. | [React boundaries](react/components-boundaries.md#cohesive-owners), only for React work |
| `instructions.root_guideline_lines` | Exactly two positive integers in strictly ascending order: soft substantive-line range for a root instruction entry. | Entry adaptation under source `MIGRATION.md`; resolve through adoption provenance |
| `instructions.local_guideline_lines` | Exactly two positive integers in strictly ascending order: soft substantive-line range for a local supplement. | Entry adaptation under source `MIGRATION.md`; resolve through adoption provenance |

Ranges and size thresholds are review signals, not splitting or truncation quotas.
Never remove necessary instructions, conceal lines or fragment cohesive behavior
to meet them. Preserve the size owner's documented exceptions and explicit project
gates. The instruction ranges are not token measurements or savings guarantees.
The React route is conditional: bundling this contract does not select React or
require copying an otherwise unselected technology profile. Adapt that optional
route under the [catalog contract](catalog.md#assemble-a-portable-bundle).

Reject Booleans where integers are required, unknown keys/schemas, invalid enums,
nonpositive thresholds, malformed/inverted/equal-endpoint ranges and inconsistent
growth thresholds. Report the file and field; leave invalid/unknown contents
unchanged. Never treat an invalid override as absent or silently substitute defaults.
Only dependent decisions wait for resolution; independent authorized work continues
under known binding rules. No `max_tests`, `max_reviews`, `max_fix_rounds`, token/time
budgets or test-count quotas are supported. Mandatory gates, necessary repairs and
the acceptance criteria survive every setting.

## Legacy and incomplete adoption

A genuinely older catalog that declares neither policy asset, with neither asset
nor override present, retains its recorded Markdown policy until an authorized
update. Do not manufacture settings or alter the catalog automatically. A declared
asset that is missing remains a catalog error. One policy asset without the other,
or an override without both the defaults and this contract, is an unsupported
partial setup; do not interpret it as a legacy absence or repair it automatically.

Source `MIGRATION.md` owns adoption and comparison with local changes. Preserve
project override ownership and accepted contents under that procedure; installing
new defaults does not silently replace a project override or an older accepted base.

## Validation and evidence limits

The source `tools/check_instruction_artifacts.py` validates present policy files
alongside catalog checks, including when explicit Markdown paths narrow the body
scan. Use `--root <instruction-root>` and the selected profiles, adding
`--bundle-dir <relative-bundle>` for a contained/custom layout. Defaults and this
contract must stay inside that bundle; the override stays inside the instruction
root. Parsing TOML alone is insufficient: field types, enums, completeness and the
merged growth constraint are checked. The checker reports schema field errors at
line 1 with the field name; syntax errors retain the parser's detail.

Validation does not prove agent cadence, honest progress updates, native role
permissions or client adherence. Progress semantics belong to the adopted root
`PLANS.md` ([inactive template](../templates/PLANS.md#progress-and-stopping)); policy
settings cannot disable them. Required reviews still need actual authorization,
available capabilities and the existing orchestration rules, without a duplicate
review merely because a preference is configured.
