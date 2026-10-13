# Symfony Serializer roles and application transformations

## Task contract and specification

Prevent agents from assigning Symfony Serializer role names to ordinary payload
processing classes. The user approved the distinction between framework extension
contracts and application responsibilities and requested its implementation with
a specification and plan. This document combines both for a bounded prose change.

The authoritative policy will live in
[Symfony structure and services](../../standards/symfony/structure-services.md).
The Symfony entry and HTTP/validation topic will route relevant tasks there.
The existing [naming policy](../../standards/core.md#names-and-evolving-responsibilities)
remains the general owner; this change supplies Symfony-specific decisions.

### Required behavior

- Determine input/output, responsibility, and actual caller before choosing a
  class name or a Serializer extension point.
- Distinguish normalization, denormalization, serialization, and standalone
  application transformations. An array-to-DTO method alone is not a Symfony
  denormalizer; a method called `normalize` does not establish framework membership.
- Prefer existing Serializer capabilities for supported conversion needs. Create
  a custom extension only for a real gap in the intended Serializer path, using
  the installed version's interface, supported-type contract, and registration.
- Reserve potentially misleading role names by explicit local naming policy;
  do not attribute a general naming prohibition to Symfony. Preserve legitimate
  serialization services and explicit third-party contracts.
- Name independent parsing, mapping, canonicalization, or application operations
  for their actual responsibility. Neither a new service nor a `Mapper` suffix is
  mandatory. Do not add a framework interface merely to justify an existing name.
- Keep acceptance decisions and business effects with their application owner;
  do not move them into Serializer hooks as a naming repair. Representation/type
  checks needed by the conversion contract remain legitimate in those hooks.

### Global Constraints

- English artifacts; Russian user-facing communication.
- No external project paths, class names, code, or source attribution in artifacts.
- Symfony 7.4 is the source-review baseline; use actual installed versions in
  consuming projects. Do not upgrade fixtures or imply fresh runtime evidence.
- Documentation only: no PHP implementation, new dependencies, checker changes,
  mandatory class hierarchy, or unrelated renames.
- One authoritative rule owner; entry files contain routes, not duplicate policies.

### Acceptance scenarios

| Scenario | Expected guidance |
| --- | --- |
| Existing Serializer mapping/context satisfies conversion | Reuse it; no custom extension or forwarding wrapper by default |
| Custom output representation is needed in Serializer | A normalizer with the actual framework contract and registration |
| Custom input construction is needed in Serializer | A denormalizer with its own supported-type and invocation contract |
| Direct payload processing produces a DTO and acceptance result | Application parsing/processing name; no automatic Serializer integration |
| A local value is cleaned up or canonicalized | Descriptive method or cohesive helper; no obligatory new service |
| A service genuinely converts to/from an encoded format | Serializer naming can be valid; make the actual Symfony or other contract explicit |
| An existing misleading class is touched | Inspect behavior/callers; correct naming within scope, preserve external contracts |

## Execution and baseline

- Workspace/instruction root and only affected checkout:
  `/home/vitalii/Documents/Local_Projects/Agent_Engineering_Kit`.
- Canonical specification, plan, and progress owner: this document; coordinator.
- Baseline: clean checkout at `4509fdd6487d7258b0b83026ff78435b4507f593`.
  The three targeted standards files are recoverable from that commit; this plan
  did not exist before the task.
- Mode: one coherent documentation stage, inline in the current checkout under
  [local Superpowers adaptations](../../standards/superpowers.md).
- Git actions: implementation initially authorized no Git writes. At the review
  checkpoint the user authorized committing and pushing this task to `origin/main`.
  No branches or worktrees requested. No delegation selected; no model-routing
  configuration is required.
- Review: coordinator review of scoped changes and the scenarios above; artifact
  checks at the stage boundary. No application runtime changes need execution.
- Human checkpoint: documentation stage reviewed; commit and push authorized.

## Implementation plan and progress

Status: complete. D1, I1, and V1 are complete; the user accepted the documentation
stage and authorized commit/push. No further implementation stage is proposed.

- [x] D1 — Record the agreed specification, official source baseline, scope,
  acceptance scenarios, and implementation/check plan before policy edits.
- [x] I1 — Add the authoritative decision rule to
  `standards/symfony/structure-services.md`; route naming/Serializer tasks from
  `standards/symfony.md` and `standards/symfony/http-validation.md`.
- [x] V1 — Review the final diff and new plan against the scenarios; run the
  artifact checker on all four files and `git diff --check`. Inspect the new
  file separately. Record actual results and limits here.

## Source review and evidence

Official Symfony 7.4 sources reviewed on 2026-10-13:
[custom normalizers](https://symfony.com/doc/7.4/serializer/custom_normalizer.html),
[Serializer](https://symfony.com/doc/7.4/serializer.html),
[NormalizerInterface](https://github.com/symfony/symfony/blob/7.4/src/Symfony/Component/Serializer/Normalizer/NormalizerInterface.php),
and [DenormalizerInterface](https://github.com/symfony/symfony/blob/7.4/src/Symfony/Component/Serializer/Normalizer/DenormalizerInterface.php).
These establish framework conversion and extension contracts, not a vendor naming
ban. The naming restriction is local engineering policy. This is source review,
not an executed Serializer fixture or proof of future agent compliance.

Stage verification on 2026-10-13 covered the working-tree changes above the
recorded baseline:

- `python3 tools/check_instruction_artifacts.py standards/symfony.md standards/symfony/structure-services.md standards/symfony/http-validation.md docs/plans/2026-10-13-symfony-serializer-roles.md`
  passed: four artifacts, zero errors, including catalog resource checks.
- `git diff --check` passed for tracked changes. The new plan was separately read
  and included explicitly in the artifact check.
- Coordinator review covered every acceptance scenario against the complete
  scoped diff and new plan. No unresolved findings. The rule distinguishes local
  naming policy from vendor contracts and preserves actual serialization roles,
  standalone registration, and small local transformations.
- The authoritative topic was already a catalog resource; only task routes needed
  additions. The plan is conditional maintenance history, not a bundle dependency.
- No external project identifiers or implementation were copied. No runtime tests,
  independent agent review, or automated behavioral evaluation of LLM compliance
  were performed; this change supplies instructions, not programmatic enforcement.
